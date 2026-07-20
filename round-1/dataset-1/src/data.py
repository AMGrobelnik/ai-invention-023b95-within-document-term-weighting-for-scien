#!/usr/bin/env python3
"""Load QASPER RAG dataset (DinoStackAI/qasper-rag), standardize to exp_sel_data_out schema.

Chosen dataset: qasper_rag — 890 QA examples with full paper sections, evidence section IDs,
and gold answers from the QASPER dev split. Supports section-level retrieval benchmarking.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import re
from collections import defaultdict

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_dataset_1")
DATASETS_DIR = WORKSPACE / "temp/datasets"

SECTION_TYPE_MAP = {
    r"abstract": "Abstract",
    r"introduction": "Introduction",
    r"related.?work|background|literature": "RelatedWork",
    r"method|approach|model|system|architecture|experiment|setup|implementation": "Methods",
    r"result|finding|evaluation|performance|comparison|experiment": "Results",
    r"discussion|analysis|ablation|error": "Discussion",
    r"conclusion|future|summary|limitation": "Conclusion",
}


def infer_section_type(name: str) -> str:
    if not name:
        return "Other"
    n = name.lower()
    for pattern, stype in SECTION_TYPE_MAP.items():
        if re.search(pattern, n):
            return stype
    return "Other"


def load_json(path: Path) -> list | dict:
    logger.info(f"Loading {path.name}")
    return json.loads(path.read_text())


@logger.catch(reraise=True)
def build_qasper_rag_examples() -> list[dict]:
    """Build examples from DinoStackAI/qasper-rag using dev split."""
    # Load all configs
    corpus_raw = load_json(DATASETS_DIR / "full_DinoStackAI_qasper-rag_corpus_train.json")
    queries_dev = load_json(DATASETS_DIR / "full_DinoStackAI_qasper-rag_queries_dev.json")
    qrels_dev = load_json(DATASETS_DIR / "full_DinoStackAI_qasper-rag_qrels_dev.json")
    answers_dev = load_json(DATASETS_DIR / "full_DinoStackAI_qasper-rag_answers_dev.json")

    logger.info(f"corpus: {len(corpus_raw)} rows, queries_dev: {len(queries_dev)}, qrels_dev: {len(qrels_dev)}, answers_dev: {len(answers_dev)}")

    # Index corpus by id
    corpus_by_id: dict[str, dict] = {row["id"]: row for row in corpus_raw}

    # Pre-index corpus by paper prefix for fast lookup
    def get_paper_prefix(cid: str) -> str:
        parts = cid.rsplit("_", 1)
        return parts[0] if len(parts) == 2 and parts[1].isdigit() else cid

    corpus_by_paper: dict[str, list[dict]] = defaultdict(list)
    for row in corpus_raw:
        corpus_by_paper[get_paper_prefix(row["id"])].append(row)
    logger.info(f"Indexed {len(corpus_by_paper)} unique papers in corpus")

    # Index qrels: query_id → list of corpus_ids (relevant sections)
    qrels_idx: dict[str, list[str]] = defaultdict(list)
    for row in qrels_dev:
        qrels_idx[row["query_id"]].append(row["corpus_id"])

    # Index answers: query_id → answer
    answers_idx: dict[str, str] = {row["query_id"]: row["answer"] for row in answers_dev}

    # Index queries: query_id → text
    queries_idx: dict[str, str] = {row["id"]: row["text"] for row in queries_dev}  # id, text

    examples = []
    skipped = 0

    for query in queries_dev:
        query_id = query["id"]
        query_text = query["text"]
        answer = answers_idx.get(query_id, "")
        relevant_corpus_ids = qrels_idx.get(query_id, [])

        if not relevant_corpus_ids:
            skipped += 1
            continue

        # Get paper title from first relevant section
        first_rel = corpus_by_id.get(relevant_corpus_ids[0])
        if not first_rel:
            skipped += 1
            continue

        paper_title = first_rel.get("title", "")

        # Get all corpus sections for this paper (same title prefix)
        # Extract paper_id prefix from corpus_id: "arxiv_00000" → paper_id = arxiv part
        paper_prefix = get_paper_prefix(relevant_corpus_ids[0])

        # Gather all sections for this paper from corpus (pre-indexed)
        paper_sections = corpus_by_paper.get(paper_prefix, [])

        if not paper_sections:
            skipped += 1
            continue

        # Sort sections by their index
        def section_idx(row: dict) -> int:
            parts = row["id"].rsplit("_", 1)
            try:
                return int(parts[1])
            except (IndexError, ValueError):
                return 0

        paper_sections.sort(key=section_idx)

        # Build sections list
        sections = []
        for sec in paper_sections:
            stype = infer_section_type(sec.get("section_name", ""))
            sections.append({
                "section_id": sec["id"],
                "section_type": stype,
                "section_name": sec.get("section_name", ""),
                "text": sec.get("text", ""),
            })

        # Abstract text
        abstract_text = ""
        for sec in sections:
            if sec["section_type"] == "Abstract":
                abstract_text = sec["text"]
                break

        # Evidence section ids and types
        evidence_section_ids = [cid for cid in relevant_corpus_ids if cid in corpus_by_id]
        evidence_section_types = list({
            infer_section_type(corpus_by_id[cid].get("section_name", ""))
            for cid in evidence_section_ids
        })

        # Determine metadata split source
        has_methods_results = any(t in ("Methods", "Results") for t in evidence_section_types)
        has_abstract_intro = any(t in ("Abstract", "Introduction") for t in evidence_section_types)
        if has_methods_results and has_abstract_intro:
            split_source = "mixed"
        elif has_methods_results:
            split_source = "methods_results"
        elif has_abstract_intro:
            split_source = "abstract_intro"
        else:
            split_source = "other"

        # Build input: question + paper sections as structured context
        sections_text = "\n\n".join(
            f"[{sec['section_type']}] {sec['section_name']}\n{sec['text'][:500]}"
            for sec in sections[:10]  # cap at 10 sections to keep input manageable
        )
        input_str = f"Question: {query_text}\n\nPaper: {paper_title}\n\n{sections_text}"

        example = {
            "input": input_str,
            "output": answer,
            "metadata_query_id": query_id,
            "metadata_doc_title": paper_title,
            "metadata_doc_abstract": abstract_text[:500] if abstract_text else "",
            "metadata_sections_json": json.dumps([
                {"section_id": s["section_id"], "section_type": s["section_type"],
                 "section_name": s["section_name"]}
                for s in sections
            ]),
            "metadata_num_sections": len(sections),
            "metadata_evidence_section_ids": json.dumps(evidence_section_ids),
            "metadata_evidence_section_types": json.dumps(evidence_section_types),
            "metadata_split_source": split_source,
            "metadata_paper_id": paper_prefix,
        }
        examples.append(example)

    logger.info(f"Built {len(examples)} examples (skipped {skipped})")
    return examples


@logger.catch(reraise=True)
def build_converted_qasper_examples() -> list[dict]:
    """Build examples from abertsch/converted_qasper train split."""
    rows = load_json(DATASETS_DIR / "full_abertsch_converted_qasper_default_train.json")
    logger.info(f"converted_qasper train: {len(rows)} rows")

    # Deduplicate by pid (question+passage pair id)
    seen_pids = set()
    examples = []
    for row in rows:
        pid = row.get("pid", "")
        if pid in seen_pids:
            continue
        seen_pids.add(pid)

        input_text = row.get("input", "")
        output_text = row.get("output", "")

        if not input_text or not output_text:
            continue

        example = {
            "input": input_text,
            "output": output_text,
            "metadata_query_id": row.get("id", ""),
            "metadata_pid": pid,
            "metadata_task_type": "qa_extraction",
        }
        examples.append(example)

    logger.info(f"Built {len(examples)} deduplicated examples")
    return examples


@logger.catch(reraise=True)
def main():
    Path("logs").mkdir(exist_ok=True)

    logger.info("Building qasper-rag examples (chosen single dataset)...")
    qasper_rag_examples = build_qasper_rag_examples()

    output = {
        "metadata": {
            "description": "QASPER scientific QA for section-level retrieval benchmarking (dev split)",
            "source": "DinoStackAI/qasper-rag",
            "paper": "Dasigi et al. 2021, NAACL — A Dataset of Information-Seeking Questions Anchored in Research Papers",
            "num_examples": len(qasper_rag_examples),
            "num_unique_papers": len({e["metadata_paper_id"] for e in qasper_rag_examples}),
        },
        "datasets": [
            {
                "dataset": "qasper_rag",
                "examples": qasper_rag_examples,
            }
        ]
    }

    out_path = WORKSPACE / "full_data_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    size_mb = out_path.stat().st_size / 1e6
    logger.info(f"Saved full_data_out.json: {size_mb:.1f} MB, {len(qasper_rag_examples)} examples")


if __name__ == "__main__":
    main()
