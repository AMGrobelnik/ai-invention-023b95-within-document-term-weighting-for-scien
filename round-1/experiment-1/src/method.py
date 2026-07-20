#!/usr/bin/env python3
"""TF-ISF vs Cosine vs BM25 section retrieval benchmark on QASPER scientific QA dataset."""

import gc
import json
import math
import os
import re
import resource
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import requests
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

WORKSPACE = Path(__file__).parent
LOGS_DIR = WORKSPACE / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOGS_DIR / "run.log"), rotation="30 MB", level="DEBUG")

# ── Hardware detection ──────────────────────────────────────────────────────
def _container_ram_gb() -> float:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    import psutil
    return psutil.virtual_memory().total / 1e9

TOTAL_RAM_GB = _container_ram_gb()
RAM_BUDGET = int(min(TOTAL_RAM_GB * 0.7, 20) * 1024**3)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
logger.info(f"RAM budget: {RAM_BUDGET / 1e9:.1f}GB (total={TOTAL_RAM_GB:.1f}GB)")

# ── Config ──────────────────────────────────────────────────────────────────
MAX_QUESTIONS = int(os.getenv("MAX_QUESTIONS", "180"))
TOP_K = 3
MAX_CONTEXT_TOKENS = 1800  # chars proxy for tokens
BUDGET_LIMIT_USD = 8.0
LLM_MODEL = "tencent/hy3:free"  # free model
OPENROUTER_BASE = "https://openrouter.ai/api/v1"

# ── OpenRouter client ────────────────────────────────────────────────────────
def _get_or_key() -> str:
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        # try reading from ability client env
        env_path = Path("/ai-inventor/.claude/skills/aii-openrouter-llms/../.ability_client_venv")
        for p in [Path("/ai-inventor/.env"), Path("/root/.env")]:
            if p.exists():
                for line in p.read_text().splitlines():
                    if line.startswith("OPENROUTER_API_KEY="):
                        key = line.split("=", 1)[1].strip().strip('"')
                        break
    return key

OR_KEY = _get_or_key()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=10))
def llm_call(prompt: str, max_tokens: int = 150) -> tuple[str, float]:
    """Returns (answer_text, cost_usd). Cost is 0 for free models."""
    headers = {
        "Authorization": f"Bearer {OR_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://ai-inventor.ai",
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.0,
    }
    resp = requests.post(
        f"{OPENROUTER_BASE}/chat/completions",
        headers=headers,
        json=payload,
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    answer = data["choices"][0]["message"]["content"].strip()
    # free model → cost = 0
    usage = data.get("usage", {})
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)
    cost = (in_tok * 0.0 + out_tok * 0.0) / 1e6  # free
    return answer, cost

# ── QASPER loading ───────────────────────────────────────────────────────────
DATA_DIR = WORKSPACE / "data"

def load_qasper(max_q: int) -> list[dict]:
    """Load QASPER from local raw JSON files and return flat QA records."""
    logger.info("Loading QASPER from local JSON files...")
    records = []

    for fname in ["qasper-train-v0.3.json", "qasper-dev-v0.3.json"]:
        fpath = DATA_DIR / fname
        if not fpath.exists():
            logger.warning(f"Missing {fpath}, skipping")
            continue
        papers = json.loads(fpath.read_text())
        logger.info(f"Loaded {len(papers)} papers from {fname}")

        for paper_id, paper in papers.items():
            title = paper.get("title", "")
            abstract = paper.get("abstract", "")

            # Build sections
            sections = []
            if abstract.strip():
                sections.append({"name": "Abstract", "text": abstract})
            for sec in paper.get("full_text", []):
                sname = sec.get("section_name") or "Unknown"
                paras = sec.get("paragraphs", [])
                text = " ".join(str(p) for p in paras if p).strip()
                if text:
                    sections.append({"name": sname, "text": text})

            if not sections:
                continue

            for qa in paper.get("qas", []):
                question = qa.get("question", "").strip()
                if not question:
                    continue

                gold_answers = []
                evidence_sections = []
                for ans_wrap in qa.get("answers", []):
                    ans = ans_wrap.get("answer", {})
                    fa = ans.get("free_form_answer", "")
                    if fa:
                        gold_answers.append(fa)
                    ev = ans.get("evidence", [])
                    if isinstance(ev, list):
                        evidence_sections.extend([str(e) for e in ev if e])

                if not gold_answers:
                    continue

                records.append({
                    "paper_id": paper_id,
                    "title": title,
                    "question": question,
                    "gold_answers": gold_answers,
                    "evidence_sections": evidence_sections,
                    "sections": sections,
                })

                if len(records) >= max_q:
                    logger.info(f"Reached {max_q} questions")
                    return records

    logger.info(f"Loaded {len(records)} QA records from QASPER")
    return records

# ── Text utilities ───────────────────────────────────────────────────────────
_STOP = frozenset(["the","a","an","is","in","of","to","and","or","for","with",
                    "on","at","by","from","as","it","its","this","that","are","was",
                    "were","be","been","have","has","had","not","but","if","we","our",
                    "they","their","can","which","who","what","how","when","where"])

def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return [t for t in tokens if len(t) > 1 and t not in _STOP]

def token_f1(pred: str, golds: list[str]) -> float:
    """Compute max token-level F1 against multiple gold answers (QASPER standard)."""
    pred_toks = set(re.findall(r"\w+", pred.lower()))
    best = 0.0
    for gold in golds:
        gold_toks = set(re.findall(r"\w+", gold.lower()))
        if not pred_toks or not gold_toks:
            continue
        common = pred_toks & gold_toks
        if not common:
            continue
        p = len(common) / len(pred_toks)
        r = len(common) / len(gold_toks)
        f1 = 2 * p * r / (p + r)
        best = max(best, f1)
    return best

# ── Method A: Cosine similarity ──────────────────────────────────────────────
_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        from sentence_transformers import SentenceTransformer
        logger.info("Loading sentence-transformer (all-MiniLM-L6-v2)...")
        _embedder = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedder

def cosine_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:
    emb = get_embedder()
    texts = [s["text"][:512] for s in sections]
    q_emb = emb.encode([query], normalize_embeddings=True)
    s_embs = emb.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    scores = (s_embs @ q_emb.T).flatten()
    top_idx = np.argsort(scores)[::-1][:k]
    return [{"section": sections[i], "score": float(scores[i])} for i in top_idx]

# ── Method B: BM25 ──────────────────────────────────────────────────────────
def bm25_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:
    from rank_bm25 import BM25Okapi
    tokenized = [tokenize(s["text"]) for s in sections]
    bm25 = BM25Okapi(tokenized)
    q_toks = tokenize(query)
    scores = bm25.get_scores(q_toks)
    top_idx = np.argsort(scores)[::-1][:k]
    return [{"section": sections[i], "score": float(scores[i])} for i in top_idx]

# ── Method C: TF-ISF ────────────────────────────────────────────────────────
def tf_isf_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:
    """TF-ISF: IDF computed within document sections (not across corpus)."""
    n_sections = len(sections)
    if n_sections == 0:
        return []

    # Tokenize all sections
    tok_sections = [tokenize(s["text"]) for s in sections]

    # Compute SF(t): how many sections contain term t
    sf: dict[str, int] = defaultdict(int)
    for toks in tok_sections:
        for t in set(toks):
            sf[t] += 1

    # Compute ISF(t) = log(N / (1 + SF(t)))
    def isf(t: str) -> float:
        return math.log(n_sections / (1 + sf.get(t, 0)))

    # Score each section
    q_toks = tokenize(query)
    if not q_toks:
        return [{"section": sections[i], "score": 0.0} for i in range(min(k, n_sections))]

    scores = []
    for toks in tok_sections:
        if not toks:
            scores.append(0.0)
            continue
        tf_map: dict[str, float] = defaultdict(float)
        for t in toks:
            tf_map[t] += 1.0 / len(toks)
        score = sum(tf_map.get(t, 0.0) * isf(t) for t in q_toks)
        scores.append(score)

    scores_arr = np.array(scores)
    top_idx = np.argsort(scores_arr)[::-1][:k]
    return [{"section": sections[i], "score": float(scores_arr[i])} for i in top_idx]

# ── Context builder ──────────────────────────────────────────────────────────
def build_context(retrieved: list[dict], max_chars: int = MAX_CONTEXT_TOKENS * 4) -> str:
    parts = []
    total = 0
    for item in retrieved:
        name = item["section"]["name"]
        text = item["section"]["text"]
        chunk = f"[{name}]\n{text}\n\n"
        if total + len(chunk) > max_chars:
            remaining = max_chars - total
            if remaining > 100:
                parts.append(chunk[:remaining])
            break
        parts.append(chunk)
        total += len(chunk)
    return "".join(parts).strip()

# ── Section recall ───────────────────────────────────────────────────────────
def section_recall(retrieved: list[dict], evidence: list[str]) -> float:
    if not evidence:
        return float("nan")
    ev_set = set(e.lower()[:100] for e in evidence)
    ret_set = set(r["section"]["text"].lower()[:100] for r in retrieved)
    hits = sum(1 for e in ev_set if any(e in r or r in e for r in ret_set))
    return hits / len(ev_set)

# ── Checkpoint helpers ────────────────────────────────────────────────────────
CKPT_PATH = WORKSPACE / "checkpoint.jsonl"

def load_checkpoint() -> list[dict]:
    """Load previously processed examples from checkpoint."""
    if not CKPT_PATH.exists():
        return []
    examples = []
    for line in CKPT_PATH.read_text().splitlines():
        line = line.strip()
        if line:
            try:
                examples.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    logger.info(f"Resumed from checkpoint: {len(examples)} examples already done")
    return examples

def save_checkpoint(example: dict) -> None:
    with open(CKPT_PATH, "a") as f:
        f.write(json.dumps(example, ensure_ascii=False) + "\n")

# ── Main ─────────────────────────────────────────────────────────────────────
@logger.catch(reraise=True)
def main():
    n_questions = int(os.getenv("MAX_QUESTIONS", str(MAX_QUESTIONS)))
    logger.info(f"Starting TF-ISF vs Cosine vs BM25 benchmark (max {n_questions} questions)")

    records = load_qasper(n_questions)
    if not records:
        raise RuntimeError("No QASPER records loaded")

    # Load checkpoint — skip already-done questions
    done_examples = load_checkpoint()
    done_count = len(done_examples)

    # Pre-load embedder once
    get_embedder()

    results_cosine = []
    results_bm25 = []
    results_tfisf = []

    total_cost = 0.0
    api_calls = 0
    per_method_data = {"cosine": [], "bm25": [], "tf_isf": []}
    examples_out = list(done_examples)

    # Rebuild per_method_data from checkpoint
    for ex in done_examples:
        f1_c = float(ex.get("metadata_f1_cosine", 0))
        f1_b = float(ex.get("metadata_f1_bm25", 0))
        f1_t = float(ex.get("metadata_f1_tf_isf", 0))
        sr_c = float(ex.get("metadata_section_recall_cosine", -1))
        sr_b = float(ex.get("metadata_section_recall_bm25", -1))
        sr_t = float(ex.get("metadata_section_recall_tf_isf", -1))
        stype = ex.get("metadata_gold_section_type", "Unknown")
        results_cosine.append(f1_c)
        results_bm25.append(f1_b)
        results_tfisf.append(f1_t)
        per_method_data["cosine"].append({"f1": f1_c, "section_recall": sr_c if sr_c >= 0 else float("nan"), "section_type": stype})
        per_method_data["bm25"].append({"f1": f1_b, "section_recall": sr_b if sr_b >= 0 else float("nan"), "section_type": stype})
        per_method_data["tf_isf"].append({"f1": f1_t, "section_recall": sr_t if sr_t >= 0 else float("nan"), "section_type": stype})

    for i, rec in enumerate(records):
        if i < done_count:
            continue  # already processed
        if total_cost >= BUDGET_LIMIT_USD:
            logger.warning(f"Budget limit ${BUDGET_LIMIT_USD} reached at q={i}")
            break

        q = rec["question"]
        sections = rec["sections"]
        gold_answers = rec["gold_answers"]
        evidence = rec["evidence_sections"]

        if not sections:
            logger.debug(f"q={i} no sections, skip")
            continue

        try:
            ret_cosine = cosine_retrieve(q, sections)
            ret_bm25 = bm25_retrieve(q, sections)
            ret_tfisf = tf_isf_retrieve(q, sections)
        except Exception:
            logger.error(f"Retrieval failed on q={i}")
            continue

        # Section recall
        sc_cosine = section_recall(ret_cosine, evidence)
        sc_bm25 = section_recall(ret_bm25, evidence)
        sc_tfisf = section_recall(ret_tfisf, evidence)

        # Build contexts
        ctx_cosine = build_context(ret_cosine)
        ctx_bm25 = build_context(ret_bm25)
        ctx_tfisf = build_context(ret_tfisf)

        # LLM answer generation for all 3 contexts
        def make_prompt(ctx: str) -> str:
            return (
                f"Answer the following question using only the provided context. "
                f"Be concise (1-2 sentences).\n\n"
                f"Question: {q}\n\nContext:\n{ctx}\n\nAnswer:"
            )

        ans_cosine = ans_bm25 = ans_tfisf = ""
        try:
            ans_cosine, c1 = llm_call(make_prompt(ctx_cosine))
            total_cost += c1; api_calls += 1
            ans_bm25, c2 = llm_call(make_prompt(ctx_bm25))
            total_cost += c2; api_calls += 1
            ans_tfisf, c3 = llm_call(make_prompt(ctx_tfisf))
            total_cost += c3; api_calls += 1
        except Exception:
            logger.error(f"LLM call failed on q={i}")

        # F1 scores
        f1_cosine = token_f1(ans_cosine, gold_answers) if ans_cosine else 0.0
        f1_bm25 = token_f1(ans_bm25, gold_answers) if ans_bm25 else 0.0
        f1_tfisf = token_f1(ans_tfisf, gold_answers) if ans_tfisf else 0.0

        results_cosine.append(f1_cosine)
        results_bm25.append(f1_bm25)
        results_tfisf.append(f1_tfisf)

        # Section type from first evidence section name
        gold_section_type = "Unknown"
        if evidence:
            ev_text = evidence[0].lower()
            for stype in ["abstract", "introduction", "method", "result", "discussion", "conclusion", "related"]:
                if stype in ev_text:
                    gold_section_type = stype.capitalize()
                    break

        per_method_data["cosine"].append({"f1": f1_cosine, "section_recall": sc_cosine, "section_type": gold_section_type})
        per_method_data["bm25"].append({"f1": f1_bm25, "section_recall": sc_bm25, "section_type": gold_section_type})
        per_method_data["tf_isf"].append({"f1": f1_tfisf, "section_recall": sc_tfisf, "section_type": gold_section_type})

        # Build exp_gen_sol_out example
        gold_str = gold_answers[0] if gold_answers else ""
        examples_out.append({
            "input": q,
            "output": gold_str,
            "predict_cosine_answer": ans_cosine,
            "predict_bm25_answer": ans_bm25,
            "predict_tf_isf_answer": ans_tfisf,
            "metadata_paper_id": rec["paper_id"],
            "metadata_f1_cosine": str(round(f1_cosine, 4)),
            "metadata_f1_bm25": str(round(f1_bm25, 4)),
            "metadata_f1_tf_isf": str(round(f1_tfisf, 4)),
            "metadata_section_recall_cosine": str(round(sc_cosine, 4) if not math.isnan(sc_cosine) else -1),
            "metadata_section_recall_bm25": str(round(sc_bm25, 4) if not math.isnan(sc_bm25) else -1),
            "metadata_section_recall_tf_isf": str(round(sc_tfisf, 4) if not math.isnan(sc_tfisf) else -1),
            "metadata_gold_section_type": gold_section_type,
            "metadata_retrieved_sections_cosine": str([r["section"]["name"] for r in ret_cosine]),
            "metadata_retrieved_sections_bm25": str([r["section"]["name"] for r in ret_bm25]),
            "metadata_retrieved_sections_tf_isf": str([r["section"]["name"] for r in ret_tfisf]),
        })

        save_checkpoint(examples_out[-1])

        if (i + 1) % 20 == 0:
            n = len(results_cosine)
            logger.info(
                f"q={i+1}/{n_questions} | cost=${total_cost:.3f} | "
                f"F1 cos={np.mean(results_cosine):.3f} bm25={np.mean(results_bm25):.3f} tfisf={np.mean(results_tfisf):.3f}"
            )

        del ret_cosine, ret_bm25, ret_tfisf, ctx_cosine, ctx_bm25, ctx_tfisf
        gc.collect()

    # ── Aggregate metrics ────────────────────────────────────────────────────
    def agg_method(name: str) -> dict:
        data = per_method_data[name]
        f1s = [d["f1"] for d in data]
        srs = [d["section_recall"] for d in data if not math.isnan(d["section_recall"])]

        by_type: dict[str, list] = defaultdict(list)
        by_type_sr: dict[str, list] = defaultdict(list)
        for d in data:
            by_type[d["section_type"]].append(d["f1"])
            if not math.isnan(d["section_recall"]):
                by_type_sr[d["section_type"]].append(d["section_recall"])

        return {
            "name": name,
            "mean_f1": float(np.mean(f1s)) if f1s else 0.0,
            "std_f1": float(np.std(f1s)) if f1s else 0.0,
            "mean_section_recall": float(np.mean(srs)) if srs else 0.0,
            "section_recall_by_type": {k: float(np.mean(v)) for k, v in by_type_sr.items()},
            "f1_by_type": {k: float(np.mean(v)) for k, v in by_type.items()},
            "n": len(f1s),
        }

    m_cos = agg_method("cosine")
    m_bm25 = agg_method("bm25")
    m_tfisf = agg_method("tf_isf")

    ranked = sorted([m_cos, m_bm25, m_tfisf], key=lambda x: x["mean_f1"], reverse=True)

    def find_winning_types() -> list[str]:
        wins = []
        for stype in set(m_tfisf["f1_by_type"]) | set(m_cos["f1_by_type"]):
            tf = m_tfisf["f1_by_type"].get(stype, 0)
            co = m_cos["f1_by_type"].get(stype, 0)
            if tf > co:
                wins.append(stype)
        return wins

    result_summary = {
        "dataset": "QASPER",
        "n_questions": len(examples_out),
        "methods": [m_cos, m_bm25, m_tfisf],
        "comparison": {
            "tf_isf_vs_cosine_f1_delta": round(m_tfisf["mean_f1"] - m_cos["mean_f1"], 4),
            "tf_isf_vs_cosine_section_recall_delta": round(
                m_tfisf["mean_section_recall"] - m_cos["mean_section_recall"], 4
            ),
            "methods_ranked_by_f1": [r["name"] for r in ranked],
        },
        "analysis": {
            "key_finding": (
                f"TF-ISF F1={m_tfisf['mean_f1']:.3f} vs Cosine F1={m_cos['mean_f1']:.3f} "
                f"vs BM25 F1={m_bm25['mean_f1']:.3f}. "
                f"Best method: {ranked[0]['name']}."
            ),
            "subgroups_where_tf_isf_wins": find_winning_types(),
            "api_cost_spent": round(total_cost, 4),
            "api_calls_made": api_calls,
        },
    }

    logger.info(f"Results: {json.dumps(result_summary['comparison'], indent=2)}")
    logger.info(f"Key finding: {result_summary['analysis']['key_finding']}")

    # ── Save outputs ─────────────────────────────────────────────────────────
    # method_out.json: exp_gen_sol_out schema
    method_out = {
        "metadata": {
            "method_name": "TF-ISF vs Cosine vs BM25 Section Retrieval",
            "description": "Compares three retrieval methods on QASPER scientific QA",
            "llm_model": LLM_MODEL,
            "top_k": TOP_K,
            "n_questions": len(examples_out),
            "results_summary": result_summary,
        },
        "datasets": [
            {
                "dataset": "QASPER",
                "examples": examples_out,
            }
        ],
    }

    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(method_out, indent=2, ensure_ascii=False))
    logger.info(f"Saved method_out.json with {len(examples_out)} examples")

    # Also save standalone results for easy inspection
    results_path = WORKSPACE / "results_summary.json"
    results_path.write_text(json.dumps(result_summary, indent=2, ensure_ascii=False))
    logger.info(f"Saved results_summary.json")

    # Print summary table
    logger.info("=" * 60)
    logger.info(f"{'Method':<20} {'F1 mean':>10} {'F1 std':>10} {'Sec Recall':>12}")
    logger.info("-" * 60)
    for m in [m_cos, m_bm25, m_tfisf]:
        logger.info(f"{m['name']:<20} {m['mean_f1']:>10.4f} {m['std_f1']:>10.4f} {m['mean_section_recall']:>12.4f}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
