#!/usr/bin/env python3
"""TF-ISF Section Ranking Statistical Evaluation on QASPER.

Compares three retrieval methods (cosine similarity, BM25, TF-ISF) on the QASPER
scientific QA dataset. Measures section-level recall@3 and token-level answer F1,
with bootstrap CIs, paired significance tests, subgroup analysis, and diagnostic
ISF distributions.
"""

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

import numpy as np
import requests
from loguru import logger
from scipy import stats

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path(__file__).parent
RESULTS_DIR = WORKSPACE / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Container-aware RAM limit
def _container_ram_gb():
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return None

def _detect_cpus():
    try:
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError):
        pass
    try:
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        pass
    return os.cpu_count() or 1

TOTAL_RAM_GB = _container_ram_gb() or 16.0
NUM_CPUS = _detect_cpus()
RAM_BUDGET = int(TOTAL_RAM_GB * 0.7 * 1e9)
logger.info(f"Hardware: {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f}GB RAM, budget={RAM_BUDGET/1e9:.1f}GB")
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

# OpenRouter config
OR_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OR_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
LLM_MODEL = "meta-llama/llama-3.2-3b-instruct"
MAX_LLM_BUDGET = 8.0  # USD hard cap
cumulative_cost = 0.0

N_QUESTIONS = int(os.environ.get("N_QUESTIONS", "200"))  # target sample size
N_BOOTSTRAP = 10000     # bootstrap resamples
TOP_K = 3               # sections to retrieve
MAX_CONTEXT_TOKENS = 1500  # approx chars for LLM context

# ─── Section type inference ──────────────────────────────────────────────────

SECTION_TYPE_PATTERNS = [
    (re.compile(r'abstract', re.I), "Abstract"),
    (re.compile(r'introduction', re.I), "Introduction"),
    (re.compile(r'related|prior|background|literature', re.I), "Related Work"),
    (re.compile(r'method|approach|model|framework|architecture|experiment|setup|dataset|data|training|implementation', re.I), "Methods"),
    (re.compile(r'result|finding|performance|evaluation|benchmark|comparison|ablation', re.I), "Results"),
    (re.compile(r'discussion|analysis|limitation|error|case study', re.I), "Discussion"),
    (re.compile(r'conclusion|future|summary', re.I), "Conclusion"),
]

def infer_section_type(name: str) -> str:
    for pat, label in SECTION_TYPE_PATTERNS:
        if pat.search(name):
            return label
    return "Other"

# ─── Tokenization ────────────────────────────────────────────────────────────

def simple_tokenize(text: str) -> list[str]:
    """Lowercase, alpha-only tokens."""
    return re.findall(r'[a-z]+', text.lower())

# ─── Token F1 ────────────────────────────────────────────────────────────────

def token_f1(pred: str, gold: str) -> float:
    """Standard QASPER token-level F1."""
    pred_tokens = simple_tokenize(pred)
    gold_tokens = simple_tokenize(gold)
    if not pred_tokens or not gold_tokens:
        return 0.0
    pred_counter: dict[str, int] = defaultdict(int)
    gold_counter: dict[str, int] = defaultdict(int)
    for t in pred_tokens:
        pred_counter[t] += 1
    for t in gold_tokens:
        gold_counter[t] += 1
    common = sum(min(pred_counter[t], gold_counter[t]) for t in pred_counter if t in gold_counter)
    if common == 0:
        return 0.0
    precision = common / len(pred_tokens)
    recall = common / len(gold_tokens)
    return 2 * precision * recall / (precision + recall)

def max_token_f1(pred: str, gold_answers: list[str]) -> float:
    """Max F1 across all gold answers (QASPER standard)."""
    if not gold_answers:
        return 0.0
    return max(token_f1(pred, g) for g in gold_answers)

# ─── TF-ISF Retrieval ────────────────────────────────────────────────────────

def compute_isf(sections: list[dict]) -> dict[str, float]:
    """Compute Inverse Section Frequency for all terms in a document."""
    n = len(sections)
    if n == 0:
        return {}
    sf: dict[str, int] = defaultdict(int)
    for sec in sections:
        present = set(simple_tokenize(sec["text"]))
        for t in present:
            sf[t] += 1
    isf = {t: math.log(n / (1 + sf[t])) for t in sf}
    return isf

def score_tfisf(query_tokens: list[str], section_text: str, isf: dict[str, float]) -> float:
    """TF-ISF score for a section given a query."""
    sec_tokens = simple_tokenize(section_text)
    if not sec_tokens:
        return 0.0
    tf: dict[str, float] = defaultdict(float)
    for t in sec_tokens:
        tf[t] += 1.0 / len(sec_tokens)
    return sum(tf.get(t, 0.0) * isf.get(t, 0.0) for t in query_tokens)

def retrieve_tfisf(query: str, sections: list[dict], k: int = TOP_K) -> list[str]:
    isf = compute_isf(sections)
    q_tokens = simple_tokenize(query)
    scores = [(score_tfisf(q_tokens, s["text"], isf), s["name"]) for s in sections]
    scores.sort(reverse=True)
    return [name for _, name in scores[:k]]

# ─── BM25 Retrieval ──────────────────────────────────────────────────────────

def retrieve_bm25(query: str, sections: list[dict], k: int = TOP_K) -> list[str]:
    from rank_bm25 import BM25Okapi
    tokenized_corpus = [simple_tokenize(s["text"]) for s in sections]
    bm25 = BM25Okapi(tokenized_corpus)
    q_tokens = simple_tokenize(query)
    scores = bm25.get_scores(q_tokens)
    ranked = np.argsort(scores)[::-1][:k]
    return [sections[i]["name"] for i in ranked]

# ─── Cosine Retrieval ─────────────────────────────────────────────────────────

def retrieve_cosine(query: str, sections: list[dict], embedder, k: int = TOP_K) -> list[str]:
    texts = [s["text"][:512] for s in sections]  # truncate for efficiency
    all_texts = [query] + texts
    embeddings = embedder.encode(all_texts, batch_size=32, show_progress_bar=False, normalize_embeddings=True)
    q_emb = embeddings[0]
    s_embs = embeddings[1:]
    scores = s_embs @ q_emb
    ranked = np.argsort(scores)[::-1][:k]
    return [sections[i]["name"] for i in ranked]

# ─── Section recall ───────────────────────────────────────────────────────────

def section_recall(retrieved: list[str], gold: list[str]) -> float:
    if not gold:
        return float('nan')
    retrieved_set = set(r.lower().strip() for r in retrieved)
    gold_set = set(g.lower().strip() for g in gold)
    overlap = retrieved_set & gold_set
    return len(overlap) / len(gold_set)

# ─── LLM Reader ───────────────────────────────────────────────────────────────

def call_llm(question: str, context: str, max_tokens: int = 150) -> tuple[str, float]:
    """Call OpenRouter LLM. Returns (answer, cost_usd)."""
    global cumulative_cost
    if cumulative_cost >= MAX_LLM_BUDGET:
        logger.warning(f"LLM budget exhausted (${cumulative_cost:.2f}), skipping")
        return "", 0.0

    prompt = f"Answer the following question based on the provided context. Be concise (1-2 sentences).\n\nContext:\n{context[:MAX_CONTEXT_TOKENS]}\n\nQuestion: {question}\n\nAnswer:"

    headers = {
        "Authorization": f"Bearer {OR_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.0,
    }

    try:
        resp = requests.post(OR_BASE_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        answer = data["choices"][0]["message"]["content"].strip()
        usage = data.get("usage", {})
        # Llama-3.2-3B-instruct pricing: ~$0.06/M in, $0.06/M out (free tier usually)
        in_tokens = usage.get("prompt_tokens", 0)
        out_tokens = usage.get("completion_tokens", 0)
        cost = (in_tokens * 0.06 + out_tokens * 0.06) / 1_000_000
        cumulative_cost += cost
        logger.debug(f"LLM call: {in_tokens} in, {out_tokens} out, ${cost:.6f}, total=${cumulative_cost:.4f}")
        return answer, cost
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return "", 0.0

# ─── Bootstrap CI ─────────────────────────────────────────────────────────────

def bootstrap_ci(values: np.ndarray, n_resamples: int = N_BOOTSTRAP, ci: float = 0.95) -> tuple[float, float, float]:
    """Returns (mean, lower, upper) with 95% CI."""
    vals = values[~np.isnan(values)]
    if len(vals) == 0:
        return float('nan'), float('nan'), float('nan')
    rng = np.random.default_rng(42)
    means = np.array([rng.choice(vals, size=len(vals), replace=True).mean() for _ in range(n_resamples)])
    alpha = (1 - ci) / 2
    lower = np.percentile(means, alpha * 100)
    upper = np.percentile(means, (1 - alpha) * 100)
    return float(vals.mean()), float(lower), float(upper)

# ─── Effect size ──────────────────────────────────────────────────────────────

def cohens_d(a: np.ndarray, b: np.ndarray) -> float:
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return float('nan')
    pooled_std = math.sqrt((np.std(a, ddof=1)**2 + np.std(b, ddof=1)**2) / 2)
    if pooled_std == 0:
        return 0.0
    return (np.mean(a) - np.mean(b)) / pooled_std

def rank_biserial(a: np.ndarray, b: np.ndarray) -> float:
    """Rank-biserial correlation for Wilcoxon signed-rank test."""
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]
    n = min(len(a), len(b))
    if n < 2:
        return float('nan')
    diffs = a[:n] - b[:n]
    nonzero = diffs[diffs != 0]
    if len(nonzero) == 0:
        return 0.0
    ranks = stats.rankdata(np.abs(nonzero))
    r_plus = np.sum(ranks[nonzero > 0])
    r_minus = np.sum(ranks[nonzero < 0])
    n_nz = len(nonzero)
    max_w = n_nz * (n_nz + 1) / 2
    return (r_plus - r_minus) / max_w

# ─── Load QASPER ──────────────────────────────────────────────────────────────

def load_qasper(n_max: int = N_QUESTIONS) -> list[dict]:
    """Load and parse QASPER, returning list of question records."""
    logger.info("Loading QASPER dataset from HuggingFace...")
    from datasets import load_dataset
    ds = load_dataset("allenai/qasper", trust_remote_code=True)

    records = []

    splits = ["train", "validation"]
    all_examples = []
    for split in splits:
        if split in ds:
            all_examples.extend(list(ds[split]))

    logger.info(f"Total papers loaded: {len(all_examples)}")

    for paper in all_examples:
        try:
            paper_id = paper.get("id", "")

            # Parse sections — paragraphs is list[list[str]]
            full_text = paper.get("full_text", {})
            section_names = full_text.get("section_name", []) or []
            paragraphs_list = full_text.get("paragraphs", []) or []

            if not section_names or not paragraphs_list:
                continue

            # Build sections, storing paragraph list for evidence matching
            sections = []
            para_to_section: dict[str, str] = {}  # paragraph text -> section name
            for i, (sname, paras) in enumerate(zip(section_names, paragraphs_list)):
                paras = paras if isinstance(paras, list) else [str(paras)]
                text = " ".join(paras)
                if len(text.strip()) < 30:
                    continue
                stype = infer_section_type(sname)
                sections.append({
                    "name": sname,
                    "section_type": stype,
                    "text": text,
                    "idx": i,
                })
                for p in paras:
                    para_to_section[p.strip()[:120]] = sname

            if len(sections) < 2:
                continue

            # Parse QAs
            qas = paper.get("qas", {})
            questions = qas.get("question", []) or []
            answers_list = qas.get("answers", []) or []

            for q_text, ans_obj in zip(questions, answers_list):
                if not q_text:
                    continue
                if not isinstance(ans_obj, dict):
                    continue

                # Collect answers across all annotators
                gold_answers = []
                gold_section_names = []

                for entry in (ans_obj.get("answer") or []):
                    if not isinstance(entry, dict):
                        continue
                    if entry.get("unanswerable"):
                        continue
                    ft = entry.get("free_form_answer", "")
                    if ft and ft.strip():
                        gold_answers.append(ft.strip())
                    # Also include extractive spans as answer references
                    for span in (entry.get("extractive_spans") or []):
                        if span and span.strip():
                            gold_answers.append(span.strip())

                    # Map evidence paragraphs to sections
                    for ev in (entry.get("evidence") or []):
                        if not ev or not ev.strip():
                            continue
                        ev_key = ev.strip()[:120]
                        if ev_key in para_to_section:
                            gold_section_names.append(para_to_section[ev_key])
                        else:
                            # Fuzzy: find section whose text contains evidence
                            found = False
                            for sec in sections:
                                if ev.strip()[:80] in sec["text"]:
                                    gold_section_names.append(sec["name"])
                                    found = True
                                    break
                            # If still not found, skip this evidence item

                # Need at least one free-form answer and one evidence section
                gold_answers_ff = [a for a in gold_answers if len(a) > 5]
                if not gold_answers_ff:
                    continue
                if not gold_section_names:
                    continue

                gold_sec_unique = list(dict.fromkeys(gold_section_names))  # preserve order, dedupe
                gold_types = list(dict.fromkeys(infer_section_type(g) for g in gold_sec_unique))

                records.append({
                    "paper_id": paper_id,
                    "question": q_text,
                    "gold_answers": gold_answers_ff,
                    "gold_sections": gold_sec_unique,
                    "gold_section_types": gold_types,
                    "sections": sections,
                })

                if len(records) >= n_max:
                    break
        except Exception:
            logger.error(f"Failed to parse paper {paper.get('id', '?')}")
            continue

        if len(records) >= n_max:
            break

    logger.info(f"Parsed {len(records)} QA records with valid sections and answers")
    return records

# ─── ISF Diagnostic ───────────────────────────────────────────────────────────

def compute_isf_diagnostics(records: list[dict]) -> dict:
    """Compute ISF score distributions by section type across the corpus."""
    # For each record where gold section is Methods/Results,
    # compute mean ISF for each section type
    type_isf_scores: dict[str, list[float]] = defaultdict(list)

    for rec in records:
        if not any(t in rec["gold_section_types"] for t in ["Methods", "Results"]):
            continue
        sections = rec["sections"]
        isf = compute_isf(sections)
        if not isf:
            continue
        for sec in sections:
            tokens = simple_tokenize(sec["text"])
            if not tokens:
                continue
            sec_isf_vals = [isf.get(t, 0.0) for t in set(tokens) if isf.get(t, 0.0) > 0]
            if sec_isf_vals:
                mean_isf = np.mean(sec_isf_vals)
                type_isf_scores[sec["section_type"]].append(float(mean_isf))

    result = {}
    for stype, vals in type_isf_scores.items():
        arr = np.array(vals)
        result[stype] = {
            "n": len(vals),
            "mean": float(arr.mean()),
            "median": float(np.median(arr)),
            "std": float(arr.std()),
        }
    return result

# ─── Main evaluation ──────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main():
    global cumulative_cost

    start_time = time.time()

    # Check OpenRouter API key
    if not OR_API_KEY:
        logger.warning("OPENROUTER_API_KEY not set — will skip LLM calls, use gold section text as proxy answer")

    # Load embedder
    logger.info("Loading sentence-transformers embedder...")
    from sentence_transformers import SentenceTransformer
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    logger.info("Embedder loaded")

    # Load data
    records = load_qasper(n_max=N_QUESTIONS)
    n = len(records)
    logger.info(f"Working with {n} QA records")

    if n < 10:
        logger.error("Too few records — check dataset parsing")
        raise ValueError(f"Only {n} records parsed")

    # Per-example storage
    results_per_method = {
        "cosine": {"f1": [], "recall": [], "retrieved": []},
        "bm25": {"f1": [], "recall": [], "retrieved": []},
        "tfisf": {"f1": [], "recall": [], "retrieved": []},
    }
    gold_types_per_example = []
    answers_per_method = {"cosine": [], "bm25": [], "tfisf": []}

    logger.info("Starting retrieval + evaluation loop...")

    for i, rec in enumerate(records):
        if i % 20 == 0:
            elapsed = time.time() - start_time
            logger.info(f"Progress: {i}/{n}, elapsed={elapsed:.0f}s, LLM_cost=${cumulative_cost:.4f}")

        question = rec["question"]
        sections = rec["sections"]
        gold_sections = rec["gold_sections"]
        gold_types = rec["gold_section_types"]
        gold_answers = rec["gold_answers"]
        gold_types_per_example.append(gold_types)

        if len(sections) < 2:
            for m in results_per_method:
                results_per_method[m]["f1"].append(float('nan'))
                results_per_method[m]["recall"].append(float('nan'))
                results_per_method[m]["retrieved"].append([])
                answers_per_method[m].append("")
            continue

        # Retrieve
        try:
            ret_cosine = retrieve_cosine(question, sections, embedder)
        except Exception:
            logger.error(f"Cosine retrieval failed ex {i}")
            ret_cosine = [sections[0]["name"]]

        try:
            ret_bm25 = retrieve_bm25(question, sections)
        except Exception:
            logger.error(f"BM25 retrieval failed ex {i}")
            ret_bm25 = [sections[0]["name"]]

        try:
            ret_tfisf = retrieve_tfisf(question, sections)
        except Exception:
            logger.error(f"TF-ISF retrieval failed ex {i}")
            ret_tfisf = [sections[0]["name"]]

        # Section recall
        for method, retrieved in [("cosine", ret_cosine), ("bm25", ret_bm25), ("tfisf", ret_tfisf)]:
            results_per_method[method]["recall"].append(section_recall(retrieved, gold_sections))
            results_per_method[method]["retrieved"].append(retrieved)

        # Build context for LLM from retrieved sections
        def build_context(retrieved_names: list[str]) -> str:
            sec_map = {s["name"]: s["text"] for s in sections}
            parts = []
            for name in retrieved_names:
                text = sec_map.get(name, "")
                parts.append(f"[{name}]\n{text[:500]}")
            return "\n\n".join(parts)

        # LLM answer generation
        for method, retrieved in [("cosine", ret_cosine), ("bm25", ret_bm25), ("tfisf", ret_tfisf)]:
            if OR_API_KEY and cumulative_cost < MAX_LLM_BUDGET:
                ctx = build_context(retrieved)
                answer, _ = call_llm(question, ctx)
            else:
                # Fallback: use concatenation of retrieved section text as answer proxy
                ctx = build_context(retrieved)
                answer = ctx[:200]

            answers_per_method[method].append(answer)
            f1 = max_token_f1(answer, gold_answers)
            results_per_method[method]["f1"].append(f1)

        # Free memory
        del sections
        gc.collect()

    logger.info(f"Retrieval+eval loop done. LLM total cost: ${cumulative_cost:.4f}")

    # ── Aggregate metrics ────────────────────────────────────────────────────
    method_names = ["cosine", "bm25", "tfisf"]
    metrics_agg = {}
    method_stats = {}

    for method in method_names:
        f1_arr = np.array(results_per_method[method]["f1"])
        rec_arr = np.array(results_per_method[method]["recall"])

        f1_mean, f1_lo, f1_hi = bootstrap_ci(f1_arr)
        rec_mean, rec_lo, rec_hi = bootstrap_ci(rec_arr)

        method_stats[method] = {
            "f1_mean": f1_mean, "f1_ci_lo": f1_lo, "f1_ci_hi": f1_hi,
            "recall_mean": rec_mean, "recall_ci_lo": rec_lo, "recall_ci_hi": rec_hi,
            "n": int(np.sum(~np.isnan(f1_arr))),
        }

        metrics_agg[f"{method}_f1"] = f1_mean
        metrics_agg[f"{method}_recall_at_{TOP_K}"] = rec_mean

        logger.info(f"{method}: F1={f1_mean:.4f} CI=[{f1_lo:.4f},{f1_hi:.4f}], "
                    f"Recall@{TOP_K}={rec_mean:.4f} CI=[{rec_lo:.4f},{rec_hi:.4f}]")

    # ── Statistical tests ────────────────────────────────────────────────────
    def paired_ttest(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
        mask = ~np.isnan(a) & ~np.isnan(b)
        a, b = a[mask], b[mask]
        if len(a) < 5:
            return float('nan'), float('nan')
        t, p = stats.ttest_rel(a, b)
        return float(t), float(p)

    comparisons = [
        ("tfisf", "cosine", "f1"),
        ("tfisf", "bm25", "f1"),
        ("tfisf", "cosine", "recall"),
        ("tfisf", "bm25", "recall"),
        ("cosine", "bm25", "f1"),
        ("cosine", "bm25", "recall"),
    ]

    raw_pvals = []
    comparison_results = []
    for m1, m2, metric in comparisons:
        key = "f1" if metric == "f1" else "recall"
        arr1 = np.array(results_per_method[m1][key])
        arr2 = np.array(results_per_method[m2][key])
        t, p = paired_ttest(arr1, arr2)
        d = cohens_d(arr1, arr2)
        rbc = rank_biserial(arr1, arr2)
        comparison_results.append({
            "comparison": f"{m1}_vs_{m2}_{metric}",
            "t_stat": t, "p_val": p, "cohens_d": d, "rank_biserial": rbc,
            "delta_mean": float(np.nanmean(arr1) - np.nanmean(arr2)),
        })
        if not math.isnan(p):
            raw_pvals.append(p)

    # Holm-Bonferroni correction
    if raw_pvals:
        sorted_idx = np.argsort(raw_pvals)
        n_tests = len(raw_pvals)
        pvals_arr = np.array(raw_pvals)
        adjusted = np.ones(n_tests)
        for rank_i, idx in enumerate(sorted_idx):
            adjusted[idx] = min(pvals_arr[idx] * (n_tests - rank_i), 1.0)
        # Apply monotone: adjusted[i] >= adjusted[i-1]
        prev = 1.0
        for i in sorted_idx[::-1]:
            adjusted[i] = min(adjusted[i], prev)
            prev = adjusted[i]

        j = 0
        for cr in comparison_results:
            if not math.isnan(cr["p_val"]):
                cr["p_val_holm"] = float(adjusted[j])
                j += 1
            else:
                cr["p_val_holm"] = float('nan')

    for cr in comparison_results:
        key = cr["comparison"]
        metrics_agg[f"delta_{key}"] = cr["delta_mean"]
        metrics_agg[f"pval_{key}"] = cr.get("p_val", float('nan'))
        logger.info(f"  {key}: delta={cr['delta_mean']:.4f}, p={cr.get('p_val','?'):.4f}, "
                    f"p_holm={cr.get('p_val_holm','?'):.4f}, d={cr['cohens_d']:.3f}")

    # ── Subgroup analysis ────────────────────────────────────────────────────
    SUBGROUP_MAP = {
        "Abstract_Intro": ["Abstract", "Introduction"],
        "Methods_Results": ["Methods", "Results"],
        "Discussion_Conclusion": ["Discussion", "Conclusion"],
        "Other": ["Other", "Related Work"],
    }

    subgroup_results = {}
    for sg_name, sg_types in SUBGROUP_MAP.items():
        indices = [
            i for i, types in enumerate(gold_types_per_example)
            if any(t in sg_types for t in types)
        ]
        if not indices:
            continue
        sg = {}
        for method in method_names:
            f1_arr = np.array([results_per_method[method]["f1"][i] for i in indices])
            rec_arr = np.array([results_per_method[method]["recall"][i] for i in indices])
            f1_m, f1_lo, f1_hi = bootstrap_ci(f1_arr)
            rec_m, rec_lo, rec_hi = bootstrap_ci(rec_arr)
            sg[method] = {
                "n": len(indices),
                "f1_mean": f1_m, "f1_ci_lo": f1_lo, "f1_ci_hi": f1_hi,
                "recall_mean": rec_m, "recall_ci_lo": rec_lo, "recall_ci_hi": rec_hi,
            }
        subgroup_results[sg_name] = sg
        logger.info(f"Subgroup {sg_name} (n={len(indices)}): "
                    f"tfisf_f1={sg['tfisf']['f1_mean']:.4f}, "
                    f"cosine_f1={sg['cosine']['f1_mean']:.4f}")
        # Add to agg metrics
        for method in method_names:
            metrics_agg[f"sg_{sg_name}_{method}_f1"] = sg[method]["f1_mean"]
            metrics_agg[f"sg_{sg_name}_{method}_recall"] = sg[method]["recall_mean"]

    # ── ISF Diagnostic ───────────────────────────────────────────────────────
    logger.info("Computing ISF diagnostic distributions...")
    isf_diag = compute_isf_diagnostics(records)
    logger.info(f"ISF diagnostics: {json.dumps({k: {kk: round(vv,4) for kk,vv in v.items()} for k,v in isf_diag.items()}, indent=2)}")

    for stype, vals in isf_diag.items():
        key = stype.replace("/", "_").replace(" ", "_")
        metrics_agg[f"isf_mean_{key}"] = vals["mean"]

    # ── Build output JSON ─────────────────────────────────────────────────────
    # Build per-example outputs
    examples = []
    for i, rec in enumerate(records):
        ex = {
            "input": rec["question"],
            "output": rec["gold_answers"][0] if rec["gold_answers"] else "",
            "predict_cosine": answers_per_method["cosine"][i] if i < len(answers_per_method["cosine"]) else "",
            "predict_bm25": answers_per_method["bm25"][i] if i < len(answers_per_method["bm25"]) else "",
            "predict_tfisf": answers_per_method["tfisf"][i] if i < len(answers_per_method["tfisf"]) else "",
            "eval_f1_cosine": results_per_method["cosine"]["f1"][i] if i < len(results_per_method["cosine"]["f1"]) else float('nan'),
            "eval_f1_bm25": results_per_method["bm25"]["f1"][i] if i < len(results_per_method["bm25"]["f1"]) else float('nan'),
            "eval_f1_tfisf": results_per_method["tfisf"]["f1"][i] if i < len(results_per_method["tfisf"]["f1"]) else float('nan'),
            "eval_recall_cosine": results_per_method["cosine"]["recall"][i] if i < len(results_per_method["cosine"]["recall"]) else float('nan'),
            "eval_recall_bm25": results_per_method["bm25"]["recall"][i] if i < len(results_per_method["bm25"]["recall"]) else float('nan'),
            "eval_recall_tfisf": results_per_method["tfisf"]["recall"][i] if i < len(results_per_method["tfisf"]["recall"]) else float('nan'),
            "metadata_paper_id": rec["paper_id"],
            "metadata_gold_section_types": json.dumps(rec["gold_section_types"]),
            "metadata_gold_sections": json.dumps(rec["gold_sections"][:3]),
            "metadata_retrieved_tfisf": json.dumps(results_per_method["tfisf"]["retrieved"][i] if i < len(results_per_method["tfisf"]["retrieved"]) else []),
            "metadata_retrieved_cosine": json.dumps(results_per_method["cosine"]["retrieved"][i] if i < len(results_per_method["cosine"]["retrieved"]) else []),
            "metadata_retrieved_bm25": json.dumps(results_per_method["bm25"]["retrieved"][i] if i < len(results_per_method["bm25"]["retrieved"]) else []),
        }
        # Replace NaN with 0.0 for JSON compliance
        for k, v in ex.items():
            if isinstance(v, float) and math.isnan(v):
                ex[k] = 0.0
        examples.append(ex)

    # Clean NaN in metrics_agg
    for k, v in metrics_agg.items():
        if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
            metrics_agg[k] = 0.0

    output = {
        "metadata": {
            "evaluation_name": "TF-ISF Section Ranking Statistical Evaluation",
            "dataset": "QASPER (allenai/qasper)",
            "n_questions": n,
            "top_k": TOP_K,
            "n_bootstrap": N_BOOTSTRAP,
            "llm_model": LLM_MODEL,
            "llm_cost_usd": round(cumulative_cost, 6),
            "method_stats": method_stats,
            "statistical_comparisons": comparison_results,
            "subgroup_analysis": subgroup_results,
            "isf_diagnostics": isf_diag,
            "baselines": ["cosine_similarity (all-MiniLM-L6-v2)", "BM25Okapi"],
            "main_method": "TF-ISF (Inverse Section Frequency)",
        },
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "QASPER",
                "examples": examples,
            }
        ],
    }

    # Replace NaN/inf in comparison results for JSON
    def clean_dict(d):
        if isinstance(d, dict):
            return {k: clean_dict(v) for k, v in d.items()}
        if isinstance(d, list):
            return [clean_dict(v) for v in d]
        if isinstance(d, float) and (math.isnan(d) or math.isinf(d)):
            return 0.0
        return d

    output = clean_dict(output)

    out_path = WORKSPACE / "eval_out.json"
    out_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved eval_out.json ({out_path.stat().st_size / 1024:.1f} KB)")

    # Also save detailed results
    detail_path = RESULTS_DIR / "detailed_results.json"
    detail_path.write_text(json.dumps({
        "comparison_results": clean_dict(comparison_results),
        "subgroup_results": clean_dict(subgroup_results),
        "isf_diagnostics": clean_dict(isf_diag),
        "method_stats": clean_dict(method_stats),
        "total_cost_usd": round(cumulative_cost, 6),
    }, indent=2))
    logger.info(f"Saved detailed results to {detail_path}")

    elapsed = time.time() - start_time
    logger.info(f"Total elapsed: {elapsed:.0f}s, LLM cost: ${cumulative_cost:.4f}")
    logger.info(f"Summary: tfisf_f1={metrics_agg.get('tfisf_f1',0):.4f}, "
                f"cosine_f1={metrics_agg.get('cosine_f1',0):.4f}, "
                f"bm25_f1={metrics_agg.get('bm25_f1',0):.4f}")
    logger.info(f"Summary: tfisf_recall={metrics_agg.get(f'tfisf_recall_at_{TOP_K}',0):.4f}, "
                f"cosine_recall={metrics_agg.get(f'cosine_recall_at_{TOP_K}',0):.4f}")

if __name__ == "__main__":
    main()
