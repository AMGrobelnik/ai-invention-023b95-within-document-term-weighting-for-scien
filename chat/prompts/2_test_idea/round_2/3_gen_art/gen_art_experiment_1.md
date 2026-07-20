# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 11:49:14 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: 'Reconcile TF-ISF Results: n=180 vs n=200 with Rigorous Controls'
summary: >-
  Re-implement cosine similarity, corpus-level BM25, and TF-ISF methods on both n=180 and n=200 QASPER subsets with identical
  preprocessing, unified LLM (llama-3.2-3b), and comprehensive statistical analysis including bootstrap CIs, per-example error
  classification, and diagnosis of mechanism assumptions.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # Phase 1: Data Loading & Preprocessing (unified pipeline)
  1. Load both n=180 (previous experiment split) and n=200 (evaluation split) from dependency dataset
  2. Parse each example: extract query, sections dict with section_id/section_type/section_text, gold_answer, metadata_evidence_section_ids
  3. Apply identical tokenization and lowercasing to all sections
  4. Build two separate section corpora:
     - Within-paper sections (per-paper ISF computation)
     - All-paper corpus of 81,550 sections (for corpus-level BM25)
  5. Validation: confirm n=180 subset is proper prefix of n=200, check for NaN/empty fields

  # Phase 2: Retrieval Method Implementation
  ## Method A: Cosine Similarity (Dense Baseline)
    1. Load all-MiniLM-L6-v2 embeddings model (lightweight, CPU-safe)
    2. Embed all query strings once to avoid repeated inference
    3. Embed all sections in target paper once per paper
    4. For each query, compute cosine similarity query→section for all sections in paper
    5. Return top-k=3 sections ranked by similarity
    6. **Key invariant**: use ONLY sections from the query's own paper (single-paper retrieval)

  ## Method B: Corpus-Level BM25 (Strong Baseline)
    1. Build rank_bm25 index over ALL 81,550 sections from entire QASPER corpus
    2. Tokenize each section: split on whitespace, lowercase, strip punctuation
    3. For each query, retrieve top-k=3 sections from ENTIRE corpus via BM25 scoring
    4. **Critical difference from prior**: retrieval is corpus-wide, not restricted to target paper
    5. Filter final results to only those from the query's target paper
        - If <3 sections from target paper in top-k corpus results, pad with next-best from paper
        - Log all padding events for diagnostic
    6. **Rationale**: corpus-level IDF uses global term frequencies, matches TF-ISF's use of same paper as baseline

  ## Method C: TF-ISF (Within-Document Reweighting)
    1. For each paper, compute Inverse Section Frequency per term:
       ISF(term, paper) = log(N_sections / (1 + SF(term)))
         where SF(term) = count of sections in paper containing term
         N_sections = total sections in paper (typically 5-8)
    2. For each section, compute TF-ISF score = sum over query_terms of TF(term, section) * ISF(term, paper)
       TF(term, section) = 1 + log(count of term in section) if count > 0, else 0
    3. Rank sections within target paper by TF-ISF score
    4. Return top-k=3 sections from same paper
    5. **Validation**: compute ISF stats (mean, std, min, max per section type) on full n=200

  # Phase 3: LLM Inference & Answer Generation
  ## Primary pipeline: llama-3.2-3b-instruct via OpenRouter
    1. For each example and each retrieval method:
       - Concatenate top-k=3 retrieved sections + query into prompt:
         "Answer this question based on the provided paper sections:\n[SECTION_1]\n[SECTION_2]\n[SECTION_3]\nQuestion: {query}"
       - Call OpenRouter llama-3.2-3b at temperature=0 (deterministic)
       - Cap output to 256 tokens to control cost
       - Parse response as raw answer string
    2. Cost tracking: record tokens_in + tokens_out per call, sum cumulative cost
       - Budget: $10 max → ~$0.01-0.05 per query (200 queries × 3 methods = 600 LLM calls)
       - Abort if cumulative cost exceeds $9.50
    3. Store: {query_id, method, retrieved_section_ids, generated_answer, cost}

  ## Secondary pipeline: tencent/hy3:free on n=180 subset ONLY
    1. Purpose: determine if n=180 positive result was LLM-dependent
    2. Run all three methods on n=180 subset with tencent/hy3:free model (the original)
    3. Use same prompt template and output format for direct comparison
    4. Cost: should be free or minimal, confirm before running

  ## Oracle Baseline (Answer Quality Upper Bound)
    1. For each example, feed gold evidence sections directly to llama-3.2-3b
    2. Use same prompt template: "Answer based on: [GOLD_SECTIONS]\n{query}"
    3. Compute F1 on oracle answers → reader upper bound
    4. If oracle F1 is high (~0.70+), bottleneck is retrieval; if low, bottleneck is reader

  # Phase 4: Evaluation Metrics (all subsets)
  ## For each method × subset combination:
    1. **Token F1**: apply standard SQuAD-style token-level F1
       - Tokenize gold_answer and generated_answer (whitespace split, lowercase, remove punct)
       - F1 = 2*(precision*recall) / (precision+recall)
       - Precision = |generated_tokens ∩ gold_tokens| / |generated_tokens|
       - Recall = |generated_tokens ∩ gold_tokens| / |gold_tokens|
    2. **Section Recall**: measure retrieval quality independently
       - For each example, check if ANY of top-k retrieved sections match gold evidence section IDs
       - section_recall = (# examples with ≥1 gold section in top-k) / total_examples
    3. **Exact Match (EM)**: binary 1 if F1==1.0, else 0
    4. **Bootstrap CIs (95%)**:
       - Resample examples with replacement, compute F1/recall for each resample (n_iterations=10000)
       - CIs = percentile(5, 95) of bootstrap F1 distribution
       - Report: F1 (CI_low, CI_high)
    5. **Statistical Tests** (Holm-Corrected):
       - Pairwise t-tests on F1 scores: cosine vs BM25, cosine vs TF-ISF, BM25 vs TF-ISF
       - Report: t-stat, p-value (uncorrected), Holm-corrected significance
       - Effect size: Cohen's d for each comparison
       - **Interpretation**: p > 0.05 (Holm) → non-significant difference

  ## Per-Subset Analysis
    1. Compute all metrics above separately for n=180 and n=200
    2. Explain numerical differences: data-distribution differences, sample-size effects
    3. Report: "n=180 vs n=200 F1 delta = {delta}, likely due to [data/LLM/sample-size/other]"

  # Phase 5: ISF Mechanism Diagnostics (n=200 only, NO gold-section filtering)
    1. For every term in every section, compute its ISF score
    2. Aggregate by section type: compute mean ISF for Abstract, Introduction, Methods, Results, Discussion sections
    3. Report: "Mean ISF(Methods) = {x}, Mean ISF(Introduction) = {y}"
    4. **Key interpretation**: if Methods/Results have HIGHER ISF (section-unique vocabulary), mechanism is supported
       - Actual result: Methods/Results have LOWER ISF (shared vocabulary), mechanism is contradicted
    5. Compute term-level diagnostics:
       - Top-20 highest ISF terms (section-specific)
       - Top-20 lowest ISF terms (document theme terms)
       - Distribution of ISF by section type (histogram)

  # Phase 6: Per-Example Error Classification (n=200)
    1. For each example, compute 2×2 matrix:
       - Retrieval Success? = (ANY gold section in top-3 retrieved) → Yes/No
       - Reader Success? = (F1 >= 0.50 threshold) → Yes/No
    2. Categorize all examples into 4 buckets:
       - [R_yes, Reader_yes]: Both succeed (ideal)
       - [R_yes, Reader_no]: Retrieval OK but reader fails (reader quality bottleneck)
       - [R_no, Reader_yes]: Retrieval fails but reader can infer (robust reader)
       - [R_no, Reader_no]: Both fail (unfixable)
    3. Count distribution across methods
    4. Report: "Cosine: {R+/R-} retrieval; TF-ISF: {R+/R-} retrieval" → does TF-ISF improve retrieval?
    5. Identify example IDs where method differences are largest (for qualitative inspection)

  # Phase 7: LLM Model Dependency Check (n=180 only)
    1. Compare results on n=180 with:
       - llama-3.2-3b (unified primary LLM)
       - tencent/hy3:free (original LLM from n=180 prior experiment)
    2. If F1 difference > 0.10 between models → positive prior result was LLM-dependent
    3. Report: "F1 delta (llama vs hy3) = {delta}"; conclude on LLM role

  # Phase 8: Output Aggregation & JSON Structure
    1. Collect all results into method_out.json:
       {
         "experiment_id": "experiment_iter2_dir2",
         "datasets": {
           "n180": {"subset_label": "previous_experiment_split", "example_count": 180},
           "n200": {"subset_label": "full_evaluation_split", "example_count": 200}
         },
         "methods": ["cosine", "bm25_corpus", "tfidf"],
         "results": {
           "n180": {
             "cosine": {"f1_mean": 0.XXX, "f1_ci": [0.XXX, 0.XXX], "section_recall": 0.XXX, ...},
             "bm25": {...},
             "tfidf": {...}
           },
           "n200": {...},
           "oracle": {"f1_mean": 0.XXX, "upper_bound_on_retrieval_impact": "interpretation"}
         },
         "statistical_tests": {
           "n180": {
             "cosine_vs_bm25": {"t_stat": X, "p_value": X, "holm_significant": bool, "cohens_d": X},
             ...
           }
         },
         "idf_diagnostics": {
           "section_type_mean_isf": {"Abstract": 1.34, "Methods": 1.23, ...},
           "mechanism_supported": false,
           "interpretation": "Evidence sections have lower (not higher) ISF; vocabulary stratification falsified"
         },
         "error_classification": {
           "n200": {
             "cosine": {"retrieval_yes_reader_yes": X, "retrieval_yes_reader_no": X, ...},
             ...
           }
         },
         "lm_dependency_check": {
           "n180_llama_vs_hy3_delta": 0.XXX,
           "conclusion": "positive_prior_result_was_[lm_dependent|independent]"
         },
         "key_findings": [
           "TF-ISF achieves F1=0.187, no better than cosine (F1=0.198) or BM25 (F1=0.179); all p>0.37",
           "Methods/Results sections have LOWER ISF than Introduction; mechanism contradicted",
           "Oracle F1=0.XXX reveals [retrieval|reader] as primary bottleneck",
           "n=180 vs n=200 difference explained by [cause]"
         ],
         "recommendations": [
           "Term reweighting insufficient; explore discourse-aware or embedding-fine-tuned approaches",
           "Dense embedding quality for scientific domain may limit all retrieval methods",
           "Section granularity coarse; finer chunk-level retrieval worth testing"
         ]
       }
    2. Additionally save detailed per-example results for error analysis:
       examples_detail.json with {query_id, gold_answer, retrieved_by_cosine, retrieved_by_bm25, retrieved_by_tfidf, ...}

  # Cost Management
  - Track cumulative OpenRouter spend after every 50 queries
  - Stop if approaching $9.50 (leave $0.50 buffer)
  - If budget exhausted on full n=200, fall back to:
    - Halve remaining subset (n=100 random subsample)
    - Re-run stats on the smaller sample
    - Report: "Executed on n=100 subsample due to budget constraints"
  - Always report actual cumulative cost in output JSON
fallback_plan: |-
  **Scenario 1: OpenRouter API failures or rate-limiting**
  - Retry failed calls up to 3 times with exponential backoff (1s, 5s, 30s)
  - If tencent/hy3:free is unavailable, skip LLM-dependency check (non-critical)
  - If llama-3.2-3b unavailable after retries, switch to next-cheapest equivalent (Llama-3-8B-Instruct or Mistral-7B)
  - Fall back to local sentence-transformers-based scoring without LLM if all OpenRouter models fail

  **Scenario 2: Budget exhaustion mid-run**
  - At 90% of budget ($9.00 spent), switch from full n=200 to random stratified subsample (n=50-100)
  - Recompute bootstrap CIs on reduced sample; report sample size clearly
  - Skip LLM-dependency check if budget doesn't permit tencent/hy3:free testing

  **Scenario 3: Embedding model memory issues on CPU**
  - all-MiniLM-L6-v2 is ~80MB; if OOM, batch embedding computation (process 50 sections at a time)
  - As fallback, use lighter model: all-MiniLM-L12-v2 (smaller) or switch to BM25-only comparison

  **Scenario 4: rank_bm25 corpus index too large**
  - If indexing all 81,550 sections causes memory overload:
    - Split corpus into chunks (papers 0-400, 400-800, etc.)
    - For each query, retrieve from same-paper chunk first, then nearby chunks
    - Fall back to BM25 restricted to target paper only (loses corpus-level IDF component)

  **Scenario 5: Token F1 computation edge cases**
  - Empty generated answer → F1=0
  - Gold answer contains only stop words (the, a, is) → likely F1>0 but low precision (OK)
  - Case sensitivity issues → always lowercase both before tokenization

  **Scenario 6: n=180 subset not a clean prefix of n=200**
  - If data structure differs (different queries or sections), fall back to loading both independently
  - Align on common examples (query_id intersection) if mismatch found
  - Document any data inconsistencies in output JSON

  **Scenario 7: Missing gold sections or metadata**
  - Skip examples with missing metadata_evidence_section_ids; log count of skipped
  - Recompute metrics on non-skipped subset; report filtering ratio

  **Simplified fallback (if multiple failures compound):**
  - Run Methods A (cosine) and C (TF-ISF) on n=200 with oracle answer generation (feed gold sections)
  - Skip LLM inference, BM25 implementation, bootstrap CIs, and statistical tests
  - Produce limited output: cosine vs TF-ISF section recall + ISF diagnostics only
  - This isolates the retrieval signal from reader confounds
testing_plan: |-
  **Stage 1: Data Loading Smoke Test (first 5 minutes)**
  - Load first 10 examples from both n=180 and n=200 subsets
  - Parse sections, validate structure (section_id, section_type, section_text present)
  - Confirm n=180 is prefix of n=200 (spot-check query_ids)
  - Print sample query, sections, and gold answer to verify data fidelity
  - **Success signal**: "10 examples loaded, parsed, and validated successfully"

  **Stage 2: Method Implementation Validation (next 10 minutes)**
  - Implement skeleton of each method on same 10 examples

  **A. Cosine Similarity:**
    - Load all-MiniLM-L6-v2 (confirm model downloads without error)
    - Embed 3 queries + 30 sections
    - Compute cosine similarity matrix (3 queries × 30 sections)
    - Retrieve top-k=3 for each query; inspect section IDs (should be from target paper)
    - **Success**: retrieval returns valid section IDs with decreasing similarity scores

  **B. BM25 Corpus:**
    - Index just 10 papers (~500 sections) from the dependency dataset
    - Query with 3 test queries
    - Retrieve top-k=3 and filter to target paper
    - **Success**: BM25 index built, query→top-k retrieval works, filtering applied

  **C. TF-ISF:**
    - On 10 papers, compute ISF for each term
    - Compute mean ISF by section type (expected: intro high, methods/results low in prior hyp)
    - Retrieve top-k=3 for 3 queries using TF-ISF
    - **Success**: ISF scores computed without NaN, retrieval produces valid section IDs

  **Stage 3: LLM Inference Validation (next 5 minutes)**
  - Call OpenRouter llama-3.2-3b with 1 example query + retrieved sections
  - Verify API authentication, response format, token count
  - Compute token F1 on generated answer vs gold
  - **Success signal**: response received, F1 computed, cost logged
  - If OpenRouter unavailable, abort with clear error message

  **Stage 4: Statistics & Metrics Validation (next 5 minutes)**
  - On the 10-example validation set, compute:
    - Token F1 (all 3 methods)
    - Section recall (all 3 methods)
    - Bootstrap CI on tiny sample (check confidence intervals are reasonable, CI_low < mean < CI_high)
    - Pairwise t-tests (should complete without error even on tiny n)
  - **Success signal**: all metrics computed without NaN or exception

  **Stage 5: Cost Tracking Validation (1 minute)**
  - After 10 LLM queries (3 methods × 3 examples + oracle), compute cumulative cost
  - Scale to full 200: verify that 200 queries × 3 methods × ~0.015 cost_per_call stays under $10
  - If projected cost > $10, alert before running full experiment
  - **Success signal**: "Projected cost for full n=200: ${X.XX}, within budget"

  **Stage 6: Full n=180 Subset Test (40 minutes, if stages 1-5 pass)**
  - Run all 3 methods on full n=180 with unified llama-3.2-3b
  - Compute F1, section recall, bootstrap CIs, statistical tests
  - Verify results are in expected range (F1 ~0.15-0.25 based on hypothesis disconfirmation)
  - Check for NaN, infinite, or missing values
  - **Success signal**: "n=180 complete: F1 (cosine)={X}, F1 (bm25)={Y}, F1 (tfidf)={Z}, all p>0.37 (non-sig)"

  **Stage 7: Full n=200 Run (remaining time, if stage 6 passes)**
  - Run all 3 methods on full n=200
  - Recompute all metrics
  - Compare n=180 vs n=200: are results stable? do CIs overlap?
  - **Success signal**: "n=200 complete; F1 CI overlaps with n=180 CI, suggesting stable effect"

  **Stage 8: ISF Mechanism Diagnostic Check**
  - Compute mean ISF by section type (Abstract, Introduction, Methods, Results)
  - Check: is Methods/Results ISF higher (supports mechanism) or lower (falsifies)?
  - **Expected result**: Methods/Results ISF **lower** than Introduction (falsifies hypothesis mechanism)

  **Stage 9: Error Classification & Final Outputs**
  - Classify all examples into [retrieval success/fail] × [reader success/fail] matrix
  - Generate method_out.json with all results, CIs, p-values, ISF diagnostics
  - Create examples_detail.json for spot-checking
  - **Success signal**: JSON valid, all required fields present, key findings populated

  **Abort Criteria (stop immediately if any triggered):**
  1. OpenRouter authentication fails after 3 retries → abort with clear error
  2. Cumulative cost exceeds $9.50 → halt and produce partial results on completed subset
  3. Data parsing fails on >10% of examples → abort and debug data loading
  4. Any method produces NaN or infinite scores on validation set → abort and fix algorithm
  5. Bootstrap CI computation crashes (e.g., all F1 scores identical) → fall back to standard error instead of bootstrap

  **Expected Outputs at Each Stage:**
  - Stage 1: `sample_data_loaded.txt` (10 examples printed)
  - Stage 2: `method_impl_validation.json` ({cosine, bm25, tfidf} retrieval outputs)
  - Stage 3: `lm_inference_test.json` ({answer, f1, cost})
  - Stage 4: `metrics_validation.json` ({f1_mean, recall, ci_low, ci_high, p_values})
  - Stage 5: `cost_projection.txt` ("Projected: $X, within budget")
  - Stages 6-9: `method_out.json` (final comprehensive output)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_HHk7NUDMfOf5
type: dataset
title: QASPER Scientific QA Dataset for Section Retrieval
summary: |-
  Selected and processed the DinoStackAI/qasper-rag dataset (derived from QASPER, Dasigi et al. 2021 NAACL, 577 citations) for section-level retrieval benchmarking. The dataset contains 890 examples from the dev split, each consisting of: (1) a natural-language question about an NLP paper, (2) the full paper parsed into named, typed sections (Abstract, Introduction, Methods, Results, Discussion, Conclusion, Other), (3) gold evidence section IDs indicating which sections contain the answer, and (4) a gold answer string for F1 evaluation.

  Key statistics: 890 unique queries over 289 unique papers; 100% of examples have ≥2 sections; 46% of examples have Methods or Results as evidence sections (above the 40% hypothesis threshold); all examples have non-empty input/output. The corpus contains 81,550 section chunks from 1,585 NLP papers indexed by paper prefix for fast lookup.

  The input field encodes the question plus up to 10 paper sections with section type labels. The output field contains the gold answer. Metadata fields include: metadata_query_id (query hash), metadata_doc_title (paper title), metadata_doc_abstract (abstract text), metadata_sections_json (structured section list with section_id, section_type, section_name), metadata_num_sections (total sections per paper), metadata_evidence_section_ids (ground-truth relevant section IDs for retrieval evaluation), metadata_evidence_section_types (section types of evidence), metadata_split_source (methods_results/abstract_intro/mixed/other), metadata_paper_id (arXiv paper ID).

  This dataset directly supports the experiment: a retrieval-augmented summarizer that ranks sections by query relevance can be evaluated on retrieval accuracy (do evidence_section_ids appear in top-k?) and answer F1 (does the answer from retrieved sections match gold output?). File size: 10.4 MB (well within 100 MB limit).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-07-20 11:49:14 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [3] SKILL-INPUT — aii-python · 2026-07-20 11:49:18 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-07-20 11:49:22 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-07-20 11:49:28 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-use-hardware · 2026-07-20 11:49:28 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [7] SKILL-INPUT — aii-openrouter-llms · 2026-07-20 11:49:34 UTC

The agent loaded the **aii-openrouter-llms** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-openrouter-llms
description: Searches and calls LLMs from OpenRouter's extensive catalog (Claude, GPT, Gemini, Llama, Mistral, DeepSeek, etc.) with reasoning and temperature control. Use when user needs to access various LLMs, compare language models, call different model providers, find the best model for a task, or look up model pricing and costs per million tokens.
---

## Contents

- Workflow (2-phase model discovery and calling)
- Scripts (Search, Get Params, Call)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: Model Discovery and Calling

### Phase 1: Search for Models
Find models with pricing, context length, and descriptions
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

### Phase 2 (optional): Get Model Parameters
Check what parameters a specific model supports
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

### Phase 3: Call Model
Call a model using the API name from search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

---

## Scripts

### Search OpenRouter models (aii_or_search_llms.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_search_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 5' ::: 'claude' 'gpt' 'gemini'
```

**Example output:**
```
Found 5 models for query: claude

[1] Anthropic: Claude Opus 4.5
    API: anthropic/claude-opus-4.5
    Context: 200,000 tokens
    Price: $5.00/M in, $25.00/M out
    Claude Opus 4.5 is Anthropic's frontier reasoning model...

[2] Anthropic: Claude Haiku 4.5
    API: anthropic/claude-haiku-4.5
    Context: 200,000 tokens
    Price: $1.00/M in, $5.00/M out
    ...
```

**Parameters:**

`query` (optional, positional)
- Search query to filter models (e.g., 'claude', 'gpt', 'reasoning')

`--limit, -n` (optional)
- Maximum number of results (default: 10)

`--series, -s` (optional)
- Filter by model family
- Valid: GPT, Claude, Gemini, Grok, Cohere, Nova, Qwen, Yi, DeepSeek, Mistral, Llama2, Llama3, Llama4, RWKV, Qwen3, Router, Media, Other, PaLM

`--timeout` (optional)
- Request timeout in seconds (default: 60)

**Tips:**
- Use the `API` field from results for the `--model` parameter in calls
- Search is fast (queries OpenRouter's model list)

---

### Get model parameters (aii_or_get_llm_params.py)

Get detailed information and supported parameters for a specific model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

**Parallel execution (multiple models):**

IMPORTANT: When checking multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_get_llm_params.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: Anthropic: Claude Haiku 4.5
API: anthropic/claude-haiku-4.5

=== Capabilities ===
Context Length: 200,000 tokens
Max Output: 64,000 tokens
Modality: text+image->text
Input: image, text
Output: text
Moderated: Yes

=== Pricing ===
Input: $1.0000/M tokens
Output: $5.0000/M tokens

=== Supported Parameters ===
  - include_reasoning
  - max_tokens
  - reasoning
  - stop
  - temperature
  - tool_choice
  - tools
  - top_k
  - top_p
```

**Parameters:**

`model` (required, positional)
- Model API name (e.g., 'anthropic/claude-haiku-4.5', 'openai/o1')

`--timeout` (optional)
- Request timeout in seconds (default: 30)

**Tips:**
- Use after search to see which parameters a model supports
- Check supported_parameters before using --reasoning or other options

---

### Call OpenRouter model (aii_or_call_llms.py)

Make an API call to an OpenRouter LLM model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

**Parallel execution (multiple calls):**

IMPORTANT: When calling multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_call_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --model {} --input "What is 2+2?"' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: anthropic/claude-haiku-4.5

Response:
Four.

Tokens: 12 in, 5 out
```

**Parameters:**

`--model, -m` (required)
- API model name from search results (format: `provider/model-name`)
- Examples: `anthropic/claude-sonnet-4`, `openai/gpt-5`, `google/gemini-2.5-pro`

`--input, -i` (required, unless using --input-json)
- Simple string prompt

`--input-json` (optional)
- Full conversation JSON for multi-turn (mutually exclusive with --input)

`--max-tokens` (optional)
- Maximum output tokens (default: 9000)

`--reasoning` (optional)
- Reasoning effort for reasoning models: `minimal`, `low`, `medium`, `high`

`--temperature, -t` (optional)
- Randomness (0.0-2.0): 0.0=deterministic, 0.7=balanced, 1.5+=creative

`--top-p` (optional)
- Nucleus sampling (0.0-1.0)

`--instructions` (optional)
- System instructions/prompt

`--web-search` (optional)
- Enable web search with max results (e.g., 10)

`--params, -p` (optional)
- Extra model-specific parameters as JSON string
- Use `aii_or_get_llm_params.py` to see which params a model supports
- Example: `--params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'`

`--timeout` (optional)
- Request timeout in seconds (default: 120)

**Examples:**

Simple call:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "Write a haiku about coding" \
  --temperature 0.8
```

With system instructions:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-haiku-4.5" \
  --input "Explain recursion" \
  --instructions "You are a helpful programming tutor. Keep explanations concise."
```

With reasoning (for o1-style models):
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "openai/o1" \
  --input "Solve this complex math problem" \
  --reasoning high
```

With web search:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "What are the latest AI news?" \
  --web-search 10 \
  --max-tokens 15000
```

With extra model-specific params:
```bash
# Step 1: Check what params the model supports
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "meta-llama/llama-3.3-70b-instruct"
# Shows: frequency_penalty, top_k, seed, min_p, etc.

# Step 2: Call with those params
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "meta-llama/llama-3.3-70b-instruct" \
  --input "Write a short poem" \
  --params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'
```

---

## Tips

- Use `aii_or_search_llms.py` first to find models, then copy `API` field for `--model`
- Use `aii_or_get_llm_params.py` to check what params a model supports before using `--params`
- For web search, increase `--max-tokens` to handle larger responses (15000+)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [8] SYSTEM-USER prompt · 2026-07-20 12:04:32 UTC

```
[Your previous response had no visible output. Please continue and produce a user-visible response.]
```

### [9] SYSTEM-USER prompt · 2026-07-20 12:06:47 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: 'Reconcile TF-ISF Results: n=180 vs n=200 with Rigorous Controls'
summary: >-
  Re-implement cosine similarity, corpus-level BM25, and TF-ISF methods on both n=180 and n=200 QASPER subsets with identical
  preprocessing, unified LLM (llama-3.2-3b), and comprehensive statistical analysis including bootstrap CIs, per-example error
  classification, and diagnosis of mechanism assumptions.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # Phase 1: Data Loading & Preprocessing (unified pipeline)
  1. Load both n=180 (previous experiment split) and n=200 (evaluation split) from dependency dataset
  2. Parse each example: extract query, sections dict with section_id/section_type/section_text, gold_answer, metadata_evidence_section_ids
  3. Apply identical tokenization and lowercasing to all sections
  4. Build two separate section corpora:
     - Within-paper sections (per-paper ISF computation)
     - All-paper corpus of 81,550 sections (for corpus-level BM25)
  5. Validation: confirm n=180 subset is proper prefix of n=200, check for NaN/empty fields

  # Phase 2: Retrieval Method Implementation
  ## Method A: Cosine Similarity (Dense Baseline)
    1. Load all-MiniLM-L6-v2 embeddings model (lightweight, CPU-safe)
    2. Embed all query strings once to avoid repeated inference
    3. Embed all sections in target paper once per paper
    4. For each query, compute cosine similarity query→section for all sections in paper
    5. Return top-k=3 sections ranked by similarity
    6. **Key invariant**: use ONLY sections from the query's own paper (single-paper retrieval)

  ## Method B: Corpus-Level BM25 (Strong Baseline)
    1. Build rank_bm25 index over ALL 81,550 sections from entire QASPER corpus
    2. Tokenize each section: split on whitespace, lowercase, strip punctuation
    3. For each query, retrieve top-k=3 sections from ENTIRE corpus via BM25 scoring
    4. **Critical difference from prior**: retrieval is corpus-wide, not restricted to target paper
    5. Filter final results to only those from the query's target paper
        - If <3 sections from target paper in top-k corpus results, pad with next-best from paper
        - Log all padding events for diagnostic
    6. **Rationale**: corpus-level IDF uses global term frequencies, matches TF-ISF's use of same paper as baseline

  ## Method C: TF-ISF (Within-Document Reweighting)
    1. For each paper, compute Inverse Section Frequency per term:
       ISF(term, paper) = log(N_sections / (1 + SF(term)))
         where SF(term) = count of sections in paper containing term
         N_sections = total sections in paper (typically 5-8)
    2. For each section, compute TF-ISF score = sum over query_terms of TF(term, section) * ISF(term, paper)
       TF(term, section) = 1 + log(count of term in section) if count > 0, else 0
    3. Rank sections within target paper by TF-ISF score
    4. Return top-k=3 sections from same paper
    5. **Validation**: compute ISF stats (mean, std, min, max per section type) on full n=200

  # Phase 3: LLM Inference & Answer Generation
  ## Primary pipeline: llama-3.2-3b-instruct via OpenRouter
    1. For each example and each retrieval method:
       - Concatenate top-k=3 retrieved sections + query into prompt:
         "Answer this question based on the provided paper sections:\n[SECTION_1]\n[SECTION_2]\n[SECTION_3]\nQuestion: {query}"
       - Call OpenRouter llama-3.2-3b at temperature=0 (deterministic)
       - Cap output to 256 tokens to control cost
       - Parse response as raw answer string
    2. Cost tracking: record tokens_in + tokens_out per call, sum cumulative cost
       - Budget: $10 max → ~$0.01-0.05 per query (200 queries × 3 methods = 600 LLM calls)
       - Abort if cumulative cost exceeds $9.50
    3. Store: {query_id, method, retrieved_section_ids, generated_answer, cost}

  ## Secondary pipeline: tencent/hy3:free on n=180 subset ONLY
    1. Purpose: determine if n=180 positive result was LLM-dependent
    2. Run all three methods on n=180 subset with tencent/hy3:free model (the original)
    3. Use same prompt template and output format for direct comparison
    4. Cost: should be free or minimal, confirm before running

  ## Oracle Baseline (Answer Quality Upper Bound)
    1. For each example, feed gold evidence sections directly to llama-3.2-3b
    2. Use same prompt template: "Answer based on: [GOLD_SECTIONS]\n{query}"
    3. Compute F1 on oracle answers → reader upper bound
    4. If oracle F1 is high (~0.70+), bottleneck is retrieval; if low, bottleneck is reader

  # Phase 4: Evaluation Metrics (all subsets)
  ## For each method × subset combination:
    1. **Token F1**: apply standard SQuAD-style token-level F1
       - Tokenize gold_answer and generated_answer (whitespace split, lowercase, remove punct)
       - F1 = 2*(precision*recall) / (precision+recall)
       - Precision = |generated_tokens ∩ gold_tokens| / |generated_tokens|
       - Recall = |generated_tokens ∩ gold_tokens| / |gold_tokens|
    2. **Section Recall**: measure retrieval quality independently
       - For each example, check if ANY of top-k retrieved sections match gold evidence section IDs
       - section_recall = (# examples with ≥1 gold section in top-k) / total_examples
    3. **Exact Match (EM)**: binary 1 if F1==1.0, else 0
    4. **Bootstrap CIs (95%)**:
       - Resample examples with replacement, compute F1/recall for each resample (n_iterations=10000)
       - CIs = percentile(5, 95) of bootstrap F1 distribution
       - Report: F1 (CI_low, CI_high)
    5. **Statistical Tests** (Holm-Corrected):
       - Pairwise t-tests on F1 scores: cosine vs BM25, cosine vs TF-ISF, BM25 vs TF-ISF
       - Report: t-stat, p-value (uncorrected), Holm-corrected significance
       - Effect size: Cohen's d for each comparison
       - **Interpretation**: p > 0.05 (Holm) → non-significant difference

  ## Per-Subset Analysis
    1. Compute all metrics above separately for n=180 and n=200
    2. Explain numerical differences: data-distribution differences, sample-size effects
    3. Report: "n=180 vs n=200 F1 delta = {delta}, likely due to [data/LLM/sample-size/other]"

  # Phase 5: ISF Mechanism Diagnostics (n=200 only, NO gold-section filtering)
    1. For every term in every section, compute its ISF score
    2. Aggregate by section type: compute mean ISF for Abstract, Introduction, Methods, Results, Discussion sections
    3. Report: "Mean ISF(Methods) = {x}, Mean ISF(Introduction) = {y}"
    4. **Key interpretation**: if Methods/Results have HIGHER ISF (section-unique vocabulary), mechanism is supported
       - Actual result: Methods/Results have LOWER ISF (shared vocabulary), mechanism is contradicted
    5. Compute term-level diagnostics:
       - Top-20 highest ISF terms (section-specific)
       - Top-20 lowest ISF terms (document theme terms)
       - Distribution of ISF by section type (histogram)

  # Phase 6: Per-Example Error Classification (n=200)
    1. For each example, compute 2×2 matrix:
       - Retrieval Success? = (ANY gold section in top-3 retrieved) → Yes/No
       - Reader Success? = (F1 >= 0.50 threshold) → Yes/No
    2. Categorize all examples into 4 buckets:
       - [R_yes, Reader_yes]: Both succeed (ideal)
       - [R_yes, Reader_no]: Retrieval OK but reader fails (reader quality bottleneck)
       - [R_no, Reader_yes]: Retrieval fails but reader can infer (robust reader)
       - [R_no, Reader_no]: Both fail (unfixable)
    3. Count distribution across methods
    4. Report: "Cosine: {R+/R-} retrieval; TF-ISF: {R+/R-} retrieval" → does TF-ISF improve retrieval?
    5. Identify example IDs where method differences are largest (for qualitative inspection)

  # Phase 7: LLM Model Dependency Check (n=180 only)
    1. Compare results on n=180 with:
       - llama-3.2-3b (unified primary LLM)
       - tencent/hy3:free (original LLM from n=180 prior experiment)
    2. If F1 difference > 0.10 between models → positive prior result was LLM-dependent
    3. Report: "F1 delta (llama vs hy3) = {delta}"; conclude on LLM role

  # Phase 8: Output Aggregation & JSON Structure
    1. Collect all results into method_out.json:
       {
         "experiment_id": "experiment_iter2_dir2",
         "datasets": {
           "n180": {"subset_label": "previous_experiment_split", "example_count": 180},
           "n200": {"subset_label": "full_evaluation_split", "example_count": 200}
         },
         "methods": ["cosine", "bm25_corpus", "tfidf"],
         "results": {
           "n180": {
             "cosine": {"f1_mean": 0.XXX, "f1_ci": [0.XXX, 0.XXX], "section_recall": 0.XXX, ...},
             "bm25": {...},
             "tfidf": {...}
           },
           "n200": {...},
           "oracle": {"f1_mean": 0.XXX, "upper_bound_on_retrieval_impact": "interpretation"}
         },
         "statistical_tests": {
           "n180": {
             "cosine_vs_bm25": {"t_stat": X, "p_value": X, "holm_significant": bool, "cohens_d": X},
             ...
           }
         },
         "idf_diagnostics": {
           "section_type_mean_isf": {"Abstract": 1.34, "Methods": 1.23, ...},
           "mechanism_supported": false,
           "interpretation": "Evidence sections have lower (not higher) ISF; vocabulary stratification falsified"
         },
         "error_classification": {
           "n200": {
             "cosine": {"retrieval_yes_reader_yes": X, "retrieval_yes_reader_no": X, ...},
             ...
           }
         },
         "lm_dependency_check": {
           "n180_llama_vs_hy3_delta": 0.XXX,
           "conclusion": "positive_prior_result_was_[lm_dependent|independent]"
         },
         "key_findings": [
           "TF-ISF achieves F1=0.187, no better than cosine (F1=0.198) or BM25 (F1=0.179); all p>0.37",
           "Methods/Results sections have LOWER ISF than Introduction; mechanism contradicted",
           "Oracle F1=0.XXX reveals [retrieval|reader] as primary bottleneck",
           "n=180 vs n=200 difference explained by [cause]"
         ],
         "recommendations": [
           "Term reweighting insufficient; explore discourse-aware or embedding-fine-tuned approaches",
           "Dense embedding quality for scientific domain may limit all retrieval methods",
           "Section granularity coarse; finer chunk-level retrieval worth testing"
         ]
       }
    2. Additionally save detailed per-example results for error analysis:
       examples_detail.json with {query_id, gold_answer, retrieved_by_cosine, retrieved_by_bm25, retrieved_by_tfidf, ...}

  # Cost Management
  - Track cumulative OpenRouter spend after every 50 queries
  - Stop if approaching $9.50 (leave $0.50 buffer)
  - If budget exhausted on full n=200, fall back to:
    - Halve remaining subset (n=100 random subsample)
    - Re-run stats on the smaller sample
    - Report: "Executed on n=100 subsample due to budget constraints"
  - Always report actual cumulative cost in output JSON
fallback_plan: |-
  **Scenario 1: OpenRouter API failures or rate-limiting**
  - Retry failed calls up to 3 times with exponential backoff (1s, 5s, 30s)
  - If tencent/hy3:free is unavailable, skip LLM-dependency check (non-critical)
  - If llama-3.2-3b unavailable after retries, switch to next-cheapest equivalent (Llama-3-8B-Instruct or Mistral-7B)
  - Fall back to local sentence-transformers-based scoring without LLM if all OpenRouter models fail

  **Scenario 2: Budget exhaustion mid-run**
  - At 90% of budget ($9.00 spent), switch from full n=200 to random stratified subsample (n=50-100)
  - Recompute bootstrap CIs on reduced sample; report sample size clearly
  - Skip LLM-dependency check if budget doesn't permit tencent/hy3:free testing

  **Scenario 3: Embedding model memory issues on CPU**
  - all-MiniLM-L6-v2 is ~80MB; if OOM, batch embedding computation (process 50 sections at a time)
  - As fallback, use lighter model: all-MiniLM-L12-v2 (smaller) or switch to BM25-only comparison

  **Scenario 4: rank_bm25 corpus index too large**
  - If indexing all 81,550 sections causes memory overload:
    - Split corpus into chunks (papers 0-400, 400-800, etc.)
    - For each query, retrieve from same-paper chunk first, then nearby chunks
    - Fall back to BM25 restricted to target paper only (loses corpus-level IDF component)

  **Scenario 5: Token F1 computation edge cases**
  - Empty generated answer → F1=0
  - Gold answer contains only stop words (the, a, is) → likely F1>0 but low precision (OK)
  - Case sensitivity issues → always lowercase both before tokenization

  **Scenario 6: n=180 subset not a clean prefix of n=200**
  - If data structure differs (different queries or sections), fall back to loading both independently
  - Align on common examples (query_id intersection) if mismatch found
  - Document any data inconsistencies in output JSON

  **Scenario 7: Missing gold sections or metadata**
  - Skip examples with missing metadata_evidence_section_ids; log count of skipped
  - Recompute metrics on non-skipped subset; report filtering ratio

  **Simplified fallback (if multiple failures compound):**
  - Run Methods A (cosine) and C (TF-ISF) on n=200 with oracle answer generation (feed gold sections)
  - Skip LLM inference, BM25 implementation, bootstrap CIs, and statistical tests
  - Produce limited output: cosine vs TF-ISF section recall + ISF diagnostics only
  - This isolates the retrieval signal from reader confounds
testing_plan: |-
  **Stage 1: Data Loading Smoke Test (first 5 minutes)**
  - Load first 10 examples from both n=180 and n=200 subsets
  - Parse sections, validate structure (section_id, section_type, section_text present)
  - Confirm n=180 is prefix of n=200 (spot-check query_ids)
  - Print sample query, sections, and gold answer to verify data fidelity
  - **Success signal**: "10 examples loaded, parsed, and validated successfully"

  **Stage 2: Method Implementation Validation (next 10 minutes)**
  - Implement skeleton of each method on same 10 examples

  **A. Cosine Similarity:**
    - Load all-MiniLM-L6-v2 (confirm model downloads without error)
    - Embed 3 queries + 30 sections
    - Compute cosine similarity matrix (3 queries × 30 sections)
    - Retrieve top-k=3 for each query; inspect section IDs (should be from target paper)
    - **Success**: retrieval returns valid section IDs with decreasing similarity scores

  **B. BM25 Corpus:**
    - Index just 10 papers (~500 sections) from the dependency dataset
    - Query with 3 test queries
    - Retrieve top-k=3 and filter to target paper
    - **Success**: BM25 index built, query→top-k retrieval works, filtering applied

  **C. TF-ISF:**
    - On 10 papers, compute ISF for each term
    - Compute mean ISF by section type (expected: intro high, methods/results low in prior hyp)
    - Retrieve top-k=3 for 3 queries using TF-ISF
    - **Success**: ISF scores computed without NaN, retrieval produces valid section IDs

  **Stage 3: LLM Inference Validation (next 5 minutes)**
  - Call OpenRouter llama-3.2-3b with 1 example query + retrieved sections
  - Verify API authentication, response format, token count
  - Compute token F1 on generated answer vs gold
  - **Success signal**: response received, F1 computed, cost logged
  - If OpenRouter unavailable, abort with clear error message

  **Stage 4: Statistics & Metrics Validation (next 5 minutes)**
  - On the 10-example validation set, compute:
    - Token F1 (all 3 methods)
    - Section recall (all 3 methods)
    - Bootstrap CI on tiny sample (check confidence intervals are reasonable, CI_low < mean < CI_high)
    - Pairwise t-tests (should complete without error even on tiny n)
  - **Success signal**: all metrics computed without NaN or exception

  **Stage 5: Cost Tracking Validation (1 minute)**
  - After 10 LLM queries (3 methods × 3 examples + oracle), compute cumulative cost
  - Scale to full 200: verify that 200 queries × 3 methods × ~0.015 cost_per_call stays under $10
  - If projected cost > $10, alert before running full experiment
  - **Success signal**: "Projected cost for full n=200: ${X.XX}, within budget"

  **Stage 6: Full n=180 Subset Test (40 minutes, if stages 1-5 pass)**
  - Run all 3 methods on full n=180 with unified llama-3.2-3b
  - Compute F1, section recall, bootstrap CIs, statistical tests
  - Verify results are in expected range (F1 ~0.15-0.25 based on hypothesis disconfirmation)
  - Check for NaN, infinite, or missing values
  - **Success signal**: "n=180 complete: F1 (cosine)={X}, F1 (bm25)={Y}, F1 (tfidf)={Z}, all p>0.37 (non-sig)"

  **Stage 7: Full n=200 Run (remaining time, if stage 6 passes)**
  - Run all 3 methods on full n=200
  - Recompute all metrics
  - Compare n=180 vs n=200: are results stable? do CIs overlap?
  - **Success signal**: "n=200 complete; F1 CI overlaps with n=180 CI, suggesting stable effect"

  **Stage 8: ISF Mechanism Diagnostic Check**
  - Compute mean ISF by section type (Abstract, Introduction, Methods, Results)
  - Check: is Methods/Results ISF higher (supports mechanism) or lower (falsifies)?
  - **Expected result**: Methods/Results ISF **lower** than Introduction (falsifies hypothesis mechanism)

  **Stage 9: Error Classification & Final Outputs**
  - Classify all examples into [retrieval success/fail] × [reader success/fail] matrix
  - Generate method_out.json with all results, CIs, p-values, ISF diagnostics
  - Create examples_detail.json for spot-checking
  - **Success signal**: JSON valid, all required fields present, key findings populated

  **Abort Criteria (stop immediately if any triggered):**
  1. OpenRouter authentication fails after 3 retries → abort with clear error
  2. Cumulative cost exceeds $9.50 → halt and produce partial results on completed subset
  3. Data parsing fails on >10% of examples → abort and debug data loading
  4. Any method produces NaN or infinite scores on validation set → abort and fix algorithm
  5. Bootstrap CI computation crashes (e.g., all F1 scores identical) → fall back to standard error instead of bootstrap

  **Expected Outputs at Each Stage:**
  - Stage 1: `sample_data_loaded.txt` (10 examples printed)
  - Stage 2: `method_impl_validation.json` ({cosine, bm25, tfidf} retrieval outputs)
  - Stage 3: `lm_inference_test.json` ({answer, f1, cost})
  - Stage 4: `metrics_validation.json` ({f1_mean, recall, ci_low, ci_high, p_values})
  - Stage 5: `cost_projection.txt` ("Projected: $X, within budget")
  - Stages 6-9: `method_out.json` (final comprehensive output)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_HHk7NUDMfOf5
type: dataset
title: QASPER Scientific QA Dataset for Section Retrieval
summary: |-
  Selected and processed the DinoStackAI/qasper-rag dataset (derived from QASPER, Dasigi et al. 2021 NAACL, 577 citations) for section-level retrieval benchmarking. The dataset contains 890 examples from the dev split, each consisting of: (1) a natural-language question about an NLP paper, (2) the full paper parsed into named, typed sections (Abstract, Introduction, Methods, Results, Discussion, Conclusion, Other), (3) gold evidence section IDs indicating which sections contain the answer, and (4) a gold answer string for F1 evaluation.

  Key statistics: 890 unique queries over 289 unique papers; 100% of examples have ≥2 sections; 46% of examples have Methods or Results as evidence sections (above the 40% hypothesis threshold); all examples have non-empty input/output. The corpus contains 81,550 section chunks from 1,585 NLP papers indexed by paper prefix for fast lookup.

  The input field encodes the question plus up to 10 paper sections with section type labels. The output field contains the gold answer. Metadata fields include: metadata_query_id (query hash), metadata_doc_title (paper title), metadata_doc_abstract (abstract text), metadata_sections_json (structured section list with section_id, section_type, section_name), metadata_num_sections (total sections per paper), metadata_evidence_section_ids (ground-truth relevant section IDs for retrieval evaluation), metadata_evidence_section_types (section types of evidence), metadata_split_source (methods_results/abstract_intro/mixed/other), metadata_paper_id (arXiv paper ID).

  This dataset directly supports the experiment: a retrieval-augmented summarizer that ranks sections by query relevance can be evaluated on retrieval accuracy (do evidence_section_ids appear in top-k?) and answer F1 (does the answer from retrieved sections match gold output?). File size: 10.4 MB (well within 100 MB limit).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [10] SYSTEM-USER prompt · 2026-07-20 12:12:47 UTC

```
[Your previous response had no visible output. Please continue and produce a user-visible response.]
```

### [11] SYSTEM-USER prompt · 2026-07-20 12:12:49 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [12] SYSTEM-USER prompt · 2026-07-20 12:13:41 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [13] SYSTEM-USER prompt · 2026-07-20 12:17:43 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 2/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [14] SYSTEM-USER prompt · 2026-07-20 12:26:09 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 3/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
