# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-20 11:44:02 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-07-20 11:44:08 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

<available_resources>
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

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: Within-Doc Term Rarity Does Not Fix Section Retrieval
hypothesis: |-
  We originally hypothesized that within-document Inverse Section Frequency (TF-ISF) — applying IDF at the section level within a single paper — would correct a systematic retrieval bias that favors claim-dense sections (Abstract, Introduction) over evidence-dense sections (Methods, Results) in scientific QA. The empirical evidence disconfirms both the performance claim and the postulated mechanism.

  On 200 QASPER questions, TF-ISF achieved F1=0.187, performing no better than cosine similarity (F1=0.198) or BM25 (F1=0.179); all pairwise differences are non-significant (p > 0.37, Holm-corrected, Cohen's d < 0.10). Critically, the hypothesized mechanism is empirically inverted: Methods and Results sections have *lower* mean ISF (1.23–1.24) than Introduction sections (1.34), meaning technical evidence sections do not use more section-unique vocabulary — they use vocabulary that is shared across sections. This falsifies the foundational assumption that evidence sections are lexically distinguished from claim sections at the within-document scale.

  All three methods achieved similarly modest section recall (~0.48), indicating the bottleneck is not the choice of ranking function but likely the quality of dense embeddings for scientific domain text, the coarse granularity of QASPER sections, or a fundamental query-evidence vocabulary mismatch that neither sparse nor dense local reweighting resolves.

  The null result is the contribution: naive within-document term reweighting is insufficient to rescue section retrieval in scientific QA, and the assumed vocabulary stratification between IMRaD sections is not supported at the section-frequency level in QASPER's NLP paper corpus. Future work should target discourse-aware or embedding-fine-tuned approaches rather than static term-weighting heuristics.
motivation: >-
  Scientific question answering over long PDFs is increasingly important for automated literature review, clinical evidence
  synthesis, and research acceleration. Despite significant RAG advances, a structural failure mode in scientific documents
  remains unstudied: claim-dense sections (Abstract, Introduction, Conclusion) paraphrase findings in accessible language
  that closely mirrors natural-language queries, inflating their cosine similarity scores. Evidence-dense sections (Results,
  Methods) contain the verifiable, specific information needed for accurate answers but use specialized, low-frequency vocabulary
  that under-scores under standard retrieval. This claim/evidence vocabulary gap is not random noise — it is an artifact of
  how scientific papers are written (IMRaD convention mandates separating claims from evidence). TF-ISF directly corrects
  this bias using only the document itself, requiring no external training data, no rhetorical parser, no citation graph,
  and no LLM inference at retrieval time. The approach is also interpretable: the ISF score for each query term is directly
  readable from the document's own statistics.
assumptions:
- >-
  Scientific papers written in IMRaD (Introduction, Methods, Results, and Discussion) format create a systematic vocabulary
  split: claim-summarizing sections repeat topic terms while evidence sections contain section-unique terms.
- >-
  QASPER (or a similar dataset) contains enough examples where the gold evidence is in Methods/Results sections (not Abstract/Introduction)
  to detect the difference between TF-ISF and cosine similarity.
- >-
  Within-document section frequency can be computed from simple tokenization and section boundary detection, which is reliable
  for structured scientific PDFs.
- >-
  The improvement in section retrieval (higher recall of gold evidence sections) translates to measurable gains in downstream
  answer F1 when a fixed-size context window is used.
- >-
  A cheap LLM reader (available via OpenRouter within the $10 budget) can generate answers from retrieved sections consistently
  enough that retrieval quality differences are reflected in answer F1.
investigation_approach: >-
  1) Load QASPER from HuggingFace; parse each paper's sections and their text. 2) Implement three retrieval methods: (a) top-k
  cosine similarity with sentence-transformers embeddings (baseline), (b) BM25 over sections using standard corpus-level IDF
  (strong baseline), and (c) TF-ISF using within-document section frequency for ISF computation. 3) For each query, retrieve
  the top-k=3 sections under each method. 4) Feed retrieved sections + query to a cheap LLM via OpenRouter (e.g., Llama-3.2-3B-Instruct)
  and generate an answer. 5) Evaluate with token-level F1 against gold answers (QASPER's standard metric). 6) Also compute
  section-level recall (fraction of gold evidence sections retrieved in top-k) as an intermediate diagnostic. 7) Run a subgroup
  analysis: split queries by gold evidence section type (Abstract vs. Methods vs. Results) and compare retrieval performance
  per subtype across methods. This reveals whether TF-ISF specifically rescues cases where cosine fails to retrieve Methods/Results
  sections. Target: ~150–200 examples to stay within $10 LLM budget at approximately $0.01–0.05 per query.
success_criteria: >-
  CONFIRM: TF-ISF achieves ≥3 F1 points higher than top-k cosine baseline on QASPER answer F1, AND section-level recall of
  gold evidence sections is higher for TF-ISF than cosine (especially for questions with evidence in Results/Methods sections).
  An intermediate confirmation would be showing that Abstract/Introduction sections have systematically lower ISF scores (more
  document-theme terms) while Methods/Results sections have higher ISF scores (more section-unique terms) for the same queries.
  DISCONFIRM: If cosine or BM25 already retrieves gold sections with high recall (≥0.80), suggesting the vocabulary gap between
  claim and evidence sections is not large enough in practice to create a retrieval failure. PARTIAL: If TF-ISF improves section
  recall but not F1 (suggesting the bottleneck is reader quality, not retrieval), or if improvement is only visible on a specific
  subtype (e.g., numerical questions).
related_works:
- >-
  Disco-RAG (2025, arxiv 2601.04377): Builds intra-chunk RST discourse trees and inter-chunk rhetorical graphs to improve
  RAG coherence. Key difference: Disco-RAG requires an external discourse parser and focuses on discourse coherence for generation,
  while TF-ISF is a simple term-weighting formula computed purely from within-document statistics, requiring no external model
  and targeting retrieval rather than generation coherence.
- >-
  SF-RAG (2026, arxiv 2602.13647): Structure-Fidelity RAG preserves section hierarchy as a routing index and uses path-guided
  retrieval along the outline. Key difference: SF-RAG routes queries through a pre-built structural index; TF-ISF reweights
  term-section matches using within-document statistics, with no routing or indexing infrastructure required.
- >-
  CG-RAG (2025, arxiv 2501.15067): Citation-graph RAG builds intra- and inter-paper citation graphs for retrieval. Key difference:
  CG-RAG requires an external citation graph and focuses on inter-paper relationships. TF-ISF operates within a single document
  with no external resources.
- >-
  HyDE (Hypothetical Document Embeddings, 2022): Generates a hypothetical answer document and retrieves by its embedding.
  Key difference: HyDE requires LLM generation at retrieval time and targets query-document mismatch via generation; TF-ISF
  targets the within-document claim/evidence vocabulary split via statistical term weighting, requiring zero LLM calls during
  retrieval.
- >-
  Ruling Out to Rule In — Contrastive Hypothesis Retrieval (2026, arxiv 2604.04593): Scores documents by Sim(doc, H+) - lambda*Sim(doc,
  H-) where H+/H- are target and mimic hypotheses. Key difference: CHR retrieves across a document corpus for medical QA;
  TF-ISF ranks sections within a single document using no competing hypotheses, only within-document term statistics.
- >-
  SURE-RAG (2026, arxiv 2605.03534): Sufficiency and uncertainty-aware evidence verification using set-level sufficiency judgments.
  Key difference: SURE-RAG is a post-retrieval verification step that assesses if retrieved evidence is sufficient; TF-ISF
  is a retrieval scoring function that changes which sections are retrieved in the first place.
inspiration: >-
  The core insight is TF-IDF applied at a finer granularity: just as cross-corpus IDF down-weights terms that appear in many
  documents (making them poor discriminators), within-document ISF down-weights terms that appear in many sections of the
  same paper. The mathematical framework is 50 years old (Sparck Jones 1972), but its application to the intra-document section-ranking
  problem in scientific RAG is new. The additional biological analogy is indicator species from ecology: just as ecologists
  use rare species whose presence precisely signals a particular habitat, TF-ISF identifies rare intra-document terms (section-specific
  vocabulary) as the most reliable indicators of a section's unique content. The hypothesis that this specifically corrects
  a systematic failure in scientific RAG is motivated by the IMRaD writing convention, which by design separates claim language
  (intro/conclusion) from evidence language (methods/results) — a structural feature absent in general-purpose documents.
terms:
- term: TF-ISF
  definition: >-
    Term Frequency × Inverse Section Frequency: a within-document term-weighting score where ISF(t) = log(N_sections / (1
    + SF(t))), SF(t) is the number of sections in the same document containing term t, and N_sections is the total number
    of sections. Analogous to TF-IDF but using per-document section counts as the 'document frequency'.
- term: Inverse Section Frequency (ISF)
  definition: >-
    The within-document analogue of IDF: a weight for term t in a given document computed as log(N_sections / (1 + SF(t))).
    Terms appearing in many sections of the same document receive low ISF (they are document theme terms); terms appearing
    in few sections receive high ISF (they are section-specific).
- term: Claim-dense section
  definition: >-
    A section of a scientific paper (typically Abstract, Introduction, or Conclusion) that summarizes findings and claims
    in accessible language, reusing the paper's main topic vocabulary. These sections score high under standard cosine similarity
    for typical queries but contain little verifiable evidence.
- term: Evidence-dense section
  definition: >-
    A section of a scientific paper (typically Methods or Results) that contains specific experimental procedures, quantitative
    outcomes, and precise technical terms unique to that section. These sections are the true answer source for most factual
    questions but score lower under cosine similarity due to specialized vocabulary.
- term: Document theme term
  definition: >-
    A term that appears in nearly every section of a given scientific paper (e.g., the paper's central topic noun). Theme
    terms have near-zero ISF and are uninformative for discriminating between sections.
- term: Section-specific term
  definition: >-
    A term that appears in only one or two sections of a document (e.g., a specific dataset name, model hyperparameter, or
    experimental condition). Section-specific terms have high ISF and strongly indicate the section's unique content.
- term: QASPER
  definition: >-
    A public benchmark dataset of 5,049 information-seeking questions over 1,585 NLP research papers, where each question
    is paired with gold answers and evidence annotations identifying the exact paper sections containing the answer.
summary: >-
  We hypothesize that standard cosine-similarity retrieval systematically mis-ranks sections in scientific PDFs by treating
  theme terms (shared across many sections) equally with section-specific terms, biasing retrieval toward claim-dense sections
  like Abstracts. Replacing cross-corpus IDF with a within-document Inverse Section Frequency (ISF) computed solely from the
  target paper's own section statistics corrects this bias without any training, discourse parsing, or LLM inference at retrieval
  time, and should improve answer F1 on QASPER over a fixed-k cosine baseline.
_relation_rationale: >-
  Mechanism disconfirmed: evidence sections have lower (not higher) ISF; performance claim refuted by rigorous eval.
_confidence_delta: decreased
_key_changes:
- >-
  Reversed the performance claim: TF-ISF does NOT outperform cosine or BM25 (F1=0.187 vs 0.198/0.179, all p>0.37) in the rigorous
  n=200 evaluation.
- >-
  Explicitly disconfirmed the core mechanism: Methods/Results sections have LOWER ISF (1.23–1.24) than Introduction (1.34),
  falsifying the vocabulary-stratification assumption.
- >-
  Reframed the contribution as a well-characterized null result rather than a positive claim.
- >-
  Identified likely true bottlenecks: dense embedding quality for scientific domain text, section granularity, and query-evidence
  vocabulary mismatch that term weighting cannot bridge.
- >-
  Acknowledged the contradictory earlier experiment (n=180, different LLM) without suppressing it; the n=200 evaluation with
  paired statistics is treated as more reliable.
- >-
  Removed success criteria predicated on TF-ISF outperforming baselines; replaced with diagnostic framing about where retrieval
  fails.
- >-
  Pointed future work toward discourse-aware or embedding-fine-tuned approaches rather than static within-document reweighting.
relation_type: replacement
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir2
type: experiment
objective: >-
  Reconcile contradictory results (n=180 vs n=200) by re-implementing all methods with maximized comparability, implementing
  true corpus-level BM25, and producing comprehensive publication-ready analysis
approach: >-
  Load both datasets: first 180 questions from previous experiment split and full 200 from evaluation split, with identical
  preprocessing. Implement: (A) Cosine similarity (all-MiniLM-L6-v2, dense baseline), (B) Corpus-level BM25 (build rank_bm25
  index over all 81,550 sections in QASPER dataset, query to retrieve top-k from entire corpus, not restricted to target paper),
  and (C) Within-document TF-ISF (proposed method). Run all three methods on both n=180 and n=200 subsets with llama-3.2-3b-instruct
  via OpenRouter to isolate data effects from LLM effects. Also run n=180 with tencent/hy3:free (the earlier LLM) to determine
  whether the positive result was LLM-dependent. Compute: token F1, section recall, per-method per-subset with 95% bootstrap
  CIs and statistical tests (Holm-corrected). Re-compute ISF diagnostic on ALL 200 records (remove gold-section-type filter
  to eliminate bias). Measure oracle reader upper bound (feed gold sections directly to LLM, compute F1 to isolate reader
  quality). Per-example error classification: retrieval success/failure × reader success/failure. Output comprehensive method_out.json
  with all metrics, comparisons explaining why n=180 and n=200 differ, and publication-ready tables/figures.
depends_on:
- id: art_HHk7NUDMfOf5
  label: dataset
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-20 11:44:08 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [4] ASSISTANT · 2026-07-20 11:45:08 UTC

```
I'll develop a detailed, actionable plan for reconciling the contradictory results between the n=180 and n=200 experiments. Let me first do some targeted web research to validate technical details, then produce the comprehensive plan.
```

### [5] TOOL CALL — Skill · 2026-07-20 11:45:08 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-20 11:45:08 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-07-20 11:45:08 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-07-20 11:45:08 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-07-20 11:45:08 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-07-20 11:45:08 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] ASSISTANT · 2026-07-20 11:46:25 UTC

```
Now I'll create a detailed, actionable plan based on the artifact direction and hypothesis:
```

### [12] TOOL CALL — Write · 2026-07-20 11:46:25 UTC

```
File: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Reconcile TF-ISF Results: n=180 vs n=200 with Rigorous Controls",
  "summary": "Re-implement cosine similarity, corpus-level BM25, and TF-ISF methods on both n=180 and n=200 QASPER subsets with identical preprocessing, unified LLM (llama-3.2-3b), and comprehensive statistical analysis including bootstrap CIs, per-example error classification, and diagnosis of mechanism assumptions.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# Phase 1: Data Loading & Preprocessing (unified pipeline)\n1. Load both n=180 (previous experiment split) and n=200 (evaluation split) from dependency dataset\n2. Parse each example: extract query, sections dict with section_id/section_type/section_text, gold_answer, metadata_evidence_section_ids\n3. Apply identical tokenization and lowercasing to all sections\n4. Build two separate section corpora:\n   - Within-paper sections (per-paper ISF computation)\n   - All-paper corpus of 81,550 sections (for corpus-level BM25)\n5. Validation: confirm n=180 subset is proper prefix of n=200, check for NaN/empty fields\n\n# Phase 2: Retrieval Method Implementation\n## Method A: Cosine Similarity (Dense Baseline)\n  1. Load all-MiniLM-L6-v2 embeddings model (lightweight, CPU-safe)\n  2. Embed all query strings once to avoid repeated inference\n  3. Embed all sections in target paper once per paper\n  4. For each query, compute cosine similarity query→section for all sections in paper\n  5. Return top-k=3 sections ranked by similarity\n  6. **Key invariant**: use ONLY sections from the query's own paper (single-paper retrieval)\n\n## Method B: Corpus-Level BM25 (Strong Baseline)\n  1. Build rank_bm25 index over ALL 81,550 sections from entire QASPER corpus\n  2. Tokenize each section: split on whitespace, lowercase, strip punctuation\n  3. For each query, retrieve top-k=3 sections from ENTIRE corpus via BM25 scoring\n  4. **Critical difference from prior**: retrieval is corpus-wide, not restricted to target paper\n  5. Filter final results to only those from the query's target paper\n      - If <3 sections from target paper in top-k corpus results, pad with next-best from paper\n      - Log all padding events for diagnostic\n  6. **Rationale**: corpus-level IDF uses global term frequencies, matches TF-ISF's use of same paper as baseline\n\n## Method C: TF-ISF (Within-Document Reweighting)\n  1. For each paper, compute Inverse Section Frequency per term:\n     ISF(term, paper) = log(N_sections / (1 + SF(term)))\n       where SF(term) = count of sections in paper containing term\n       N_sections = total sections in paper (typically 5-8)\n  2. For each section, compute TF-ISF score = sum over query_terms of TF(term, section) * ISF(term, paper)\n     TF(term, section) = 1 + log(count of term in section) if count > 0, else 0\n  3. Rank sections within target paper by TF-ISF score\n  4. Return top-k=3 sections from same paper\n  5. **Validation**: compute ISF stats (mean, std, min, max per section type) on full n=200\n\n# Phase 3: LLM Inference & Answer Generation\n## Primary pipeline: llama-3.2-3b-instruct via OpenRouter\n  1. For each example and each retrieval method:\n     - Concatenate top-k=3 retrieved sections + query into prompt:\n       \"Answer this question based on the provided paper sections:\\n[SECTION_1]\\n[SECTION_2]\\n[SECTION_3]\\nQuestion: {query}\"\n     - Call OpenRouter llama-3.2-3b at temperature=0 (deterministic)\n     - Cap output to 256 tokens to control cost\n     - Parse response as raw answer string\n  2. Cost tracking: record tokens_in + tokens_out per call, sum cumulative cost\n     - Budget: $10 max → ~$0.01-0.05 per query (200 queries × 3 methods = 600 LLM calls)\n     - Abort if cumulative cost exceeds $9.50\n  3. Store: {query_id, method, retrieved_section_ids, generated_answer, cost}\n\n## Secondary pipeline: tencent/hy3:free on n=180 subset ONLY\n  1. Purpose: determine if n=180 positive result was LLM-dependent\n  2. Run all three methods on n=180 subset with tencent/hy3:free model (the original)\n  3. Use same prompt template and output format for direct comparison\n  4. Cost: should be free or minimal, confirm before running\n\n## Oracle Baseline (Answer Quality Upper Bound)\n  1. For each example, feed gold evidence sections directly to llama-3.2-3b\n  2. Use same prompt template: \"Answer based on: [GOLD_SECTIONS]\\n{query}\"\n  3. Compute F1 on oracle answers → reader upper bound\n  4. If oracle F1 is high (~0.70+), bottleneck is retrieval; if low, bottleneck is reader\n\n# Phase 4: Evaluation Metrics (all subsets)\n## For each method × subset combination:\n  1. **Token F1**: apply standard SQuAD-style token-level F1\n     - Tokenize gold_answer and generated_answer (whitespace split, lowercase, remove punct)\n     - F1 = 2*(precision*recall) / (precision+recall)\n     - Precision = |generated_tokens ∩ gold_tokens| / |generated_tokens|\n     - Recall = |generated_tokens ∩ gold_tokens| / |gold_tokens|\n  2. **Section Recall**: measure retrieval quality independently\n     - For each example, check if ANY of top-k retrieved sections match gold evidence section IDs\n     - section_recall = (# examples with ≥1 gold section in top-k) / total_examples\n  3. **Exact Match (EM)**: binary 1 if F1==1.0, else 0\n  4. **Bootstrap CIs (95%)**:\n     - Resample examples with replacement, compute F1/recall for each resample (n_iterations=10000)\n     - CIs = percentile(5, 95) of bootstrap F1 distribution\n     - Report: F1 (CI_low, CI_high)\n  5. **Statistical Tests** (Holm-Corrected):\n     - Pairwise t-tests on F1 scores: cosine vs BM25, cosine vs TF-ISF, BM25 vs TF-ISF\n     - Report: t-stat, p-value (uncorrected), Holm-corrected significance\n     - Effect size: Cohen's d for each comparison\n     - **Interpretation**: p > 0.05 (Holm) → non-significant difference\n\n## Per-Subset Analysis\n  1. Compute all metrics above separately for n=180 and n=200\n  2. Explain numerical differences: data-distribution differences, sample-size effects\n  3. Report: \"n=180 vs n=200 F1 delta = {delta}, likely due to [data/LLM/sample-size/other]\"\n\n# Phase 5: ISF Mechanism Diagnostics (n=200 only, NO gold-section filtering)\n  1. For every term in every section, compute its ISF score\n  2. Aggregate by section type: compute mean ISF for Abstract, Introduction, Methods, Results, Discussion sections\n  3. Report: \"Mean ISF(Methods) = {x}, Mean ISF(Introduction) = {y}\"\n  4. **Key interpretation**: if Methods/Results have HIGHER ISF (section-unique vocabulary), mechanism is supported\n     - Actual result: Methods/Results have LOWER ISF (shared vocabulary), mechanism is contradicted\n  5. Compute term-level diagnostics:\n     - Top-20 highest ISF terms (section-specific)\n     - Top-20 lowest ISF terms (document theme terms)\n     - Distribution of ISF by section type (histogram)\n\n# Phase 6: Per-Example Error Classification (n=200)\n  1. For each example, compute 2×2 matrix:\n     - Retrieval Success? = (ANY gold section in top-3 retrieved) → Yes/No\n     - Reader Success? = (F1 >= 0.50 threshold) → Yes/No\n  2. Categorize all examples into 4 buckets:\n     - [R_yes, Reader_yes]: Both succeed (ideal)\n     - [R_yes, Reader_no]: Retrieval OK but reader fails (reader quality bottleneck)\n     - [R_no, Reader_yes]: Retrieval fails but reader can infer (robust reader)\n     - [R_no, Reader_no]: Both fail (unfixable)\n  3. Count distribution across methods\n  4. Report: \"Cosine: {R+/R-} retrieval; TF-ISF: {R+/R-} retrieval\" → does TF-ISF improve retrieval?\n  5. Identify example IDs where method differences are largest (for qualitative inspection)\n\n# Phase 7: LLM Model Dependency Check (n=180 only)\n  1. Compare results on n=180 with:\n     - llama-3.2-3b (unified primary LLM)\n     - tencent/hy3:free (original LLM from n=180 prior experiment)\n  2. If F1 difference > 0.10 between models → positive prior result was LLM-dependent\n  3. Report: \"F1 delta (llama vs hy3) = {delta}\"; conclude on LLM role\n\n# Phase 8: Output Aggregation & JSON Structure\n  1. Collect all results into method_out.json:\n     {\n       \"experiment_id\": \"experiment_iter2_dir2\",\n       \"datasets\": {\n         \"n180\": {\"subset_label\": \"previous_experiment_split\", \"example_count\": 180},\n         \"n200\": {\"subset_label\": \"full_evaluation_split\", \"example_count\": 200}\n       },\n       \"methods\": [\"cosine\", \"bm25_corpus\", \"tfidf\"],\n       \"results\": {\n         \"n180\": {\n           \"cosine\": {\"f1_mean\": 0.XXX, \"f1_ci\": [0.XXX, 0.XXX], \"section_recall\": 0.XXX, ...},\n           \"bm25\": {...},\n           \"tfidf\": {...}\n         },\n         \"n200\": {...},\n         \"oracle\": {\"f1_mean\": 0.XXX, \"upper_bound_on_retrieval_impact\": \"interpretation\"}\n       },\n       \"statistical_tests\": {\n         \"n180\": {\n           \"cosine_vs_bm25\": {\"t_stat\": X, \"p_value\": X, \"holm_significant\": bool, \"cohens_d\": X},\n           ...\n         }\n       },\n       \"idf_diagnostics\": {\n         \"section_type_mean_isf\": {\"Abstract\": 1.34, \"Methods\": 1.23, ...},\n         \"mechanism_supported\": false,\n         \"interpretation\": \"Evidence sections have lower (not higher) ISF; vocabulary stratification falsified\"\n       },\n       \"error_classification\": {\n         \"n200\": {\n           \"cosine\": {\"retrieval_yes_reader_yes\": X, \"retrieval_yes_reader_no\": X, ...},\n           ...\n         }\n       },\n       \"lm_dependency_check\": {\n         \"n180_llama_vs_hy3_delta\": 0.XXX,\n         \"conclusion\": \"positive_prior_result_was_[lm_dependent|independent]\"\n       },\n       \"key_findings\": [\n         \"TF-ISF achieves F1=0.187, no better than cosine (F1=0.198) or BM25 (F1=0.179); all p>0.37\",\n         \"Methods/Results sections have LOWER ISF than Introduction; mechanism contradicted\",\n         \"Oracle F1=0.XXX reveals [retrieval|reader] as primary bottleneck\",\n         \"n=180 vs n=200 difference explained by [cause]\"\n       ],\n       \"recommendations\": [\n         \"Term reweighting insufficient; explore discourse-aware or embedding-fine-tuned approaches\",\n         \"Dense embedding quality for scientific domain may limit all retrieval methods\",\n         \"Section granularity coarse; finer chunk-level retrieval worth testing\"\n       ]\n     }\n  2. Additionally save detailed per-example results for error analysis:\n     examples_detail.json with {query_id, gold_answer, retrieved_by_cosine, retrieved_by_bm25, retrieved_by_tfidf, ...}\n\n# Cost Management\n- Track cumulative OpenRouter spend after every 50 queries\n- Stop if approaching $9.50 (leave $0.50 buffer)\n- If budget exhausted on full n=200, fall back to:\n  - Halve remaining subset (n=100 random subsample)\n  - Re-run stats on the smaller sample\n  - Report: \"Executed on n=100 subsample due to budget constraints\"\n- Always report actual cumulative cost in output JSON",
  "fallback_plan": "**Scenario 1: OpenRouter API failures or rate-limiting**\n- Retry failed calls up to 3 times with exponential backoff (1s, 5s, 30s)\n- If tencent/hy3:free is unavailable, skip LLM-dependency check (non-critical)\n- If llama-3.2-3b unavailable after retries, switch to next-cheapest equivalent (Llama-3-8B-Instruct or Mistral-7B)\n- Fall back to local sentence-transformers-based scoring without LLM if all OpenRouter models fail\n\n**Scenario 2: Budget exhaustion mid-run**\n- At 90% of budget ($9.00 spent), switch from full n=200 to random stratified subsample (n=50-100)\n- Recompute bootstrap CIs on reduced sample; report sample size clearly\n- Skip LLM-dependency check if budget doesn't permit tencent/hy3:free testing\n\n**Scenario 3: Embedding model memory issues on CPU**\n- all-MiniLM-L6-v2 is ~80MB; if OOM, batch embedding computation (process 50 sections at a time)\n- As fallback, use lighter model: all-MiniLM-L12-v2 (smaller) or switch to BM25-only comparison\n\n**Scenario 4: rank_bm25 corpus index too large**\n- If indexing all 81,550 sections causes memory overload:\n  - Split corpus into chunks (papers 0-400, 400-800, etc.)\n  - For each query, retrieve from same-paper chunk first, then nearby chunks\n  - Fall back to BM25 restricted to target paper only (loses corpus-level IDF component)\n\n**Scenario 5: Token F1 computation edge cases**\n- Empty generated answer → F1=0\n- Gold answer contains only stop words (the, a, is) → likely F1>0 but low precision (OK)\n- Case sensitivity issues → always lowercase both before tokenization\n\n**Scenario 6: n=180 subset not a clean prefix of n=200**\n- If data structure differs (different queries or sections), fall back to loading both independently\n- Align on common examples (query_id intersection) if mismatch found\n- Document any data inconsistencies in output JSON\n\n**Scenario 7: Missing gold sections or metadata**\n- Skip examples with missing metadata_evidence_section_ids; log count of skipped\n- Recompute metrics on non-skipped subset; report filtering ratio\n\n**Simplified fallback (if multiple failures compound):**\n- Run Methods A (cosine) and C (TF-ISF) on n=200 with oracle answer generation (feed gold sections)\n- Skip LLM inference, BM25 implementation, bootstrap CIs, and statistical tests\n- Produce limited output: cosine vs TF-ISF section recall + ISF diagnostics only\n- This isolates the retrieval signal from reader confounds",
  "testing_plan": "**Stage 1: Data Loading Smoke Test (first 5 minutes)**\n- Load first 10 examples from both n=180 and n=200 subsets\n- Parse sections, validate structure (section_id, section_type, section_text present)\n- Confirm n=180 is prefix of n=200 (spot-check query_ids)\n- Print sample query, sections, and gold answer to verify data fidelity\n- **Success signal**: \"10 examples loaded, parsed, and validated successfully\"\n\n**Stage 2: Method Implementation Validation (next 10 minutes)**\n- Implement skeleton of each method on same 10 examples\n\n**A. Cosine Similarity:**\n  - Load all-MiniLM-L6-v2 (confirm model downloads without error)\n  - Embed 3 queries + 30 sections\n  - Compute cosine similarity matrix (3 queries × 30 sections)\n  - Retrieve top-k=3 for each query; inspect section IDs (should be from target paper)\n  - **Success**: retrieval returns valid section IDs with decreasing similarity scores\n\n**B. BM25 Corpus:**\n  - Index just 10 papers (~500 sections) from the dependency dataset\n  - Query with 3 test queries\n  - Retrieve top-k=3 and filter to target paper\n  - **Success**: BM25 index built, query→top-k retrieval works, filtering applied\n\n**C. TF-ISF:**\n  - On 10 papers, compute ISF for each term\n  - Compute mean ISF by section type (expected: intro high, methods/results low in prior hyp)\n  - Retrieve top-k=3 for 3 queries using TF-ISF\n  - **Success**: ISF scores computed without NaN, retrieval produces valid section IDs\n\n**Stage 3: LLM Inference Validation (next 5 minutes)**\n- Call OpenRouter llama-3.2-3b with 1 example query + retrieved sections\n- Verify API authentication, response format, token count\n- Compute token F1 on generated answer vs gold\n- **Success signal**: response received, F1 computed, cost logged\n- If OpenRouter unavailable, abort with clear error message\n\n**Stage 4: Statistics & Metrics Validation (next 5 minutes)**\n- On the 10-example validation set, compute:\n  - Token F1 (all 3 methods)\n  - Section recall (all 3 methods)\n  - Bootstrap CI on tiny sample (check confidence intervals are reasonable, CI_low < mean < CI_high)\n  - Pairwise t-tests (should complete without error even on tiny n)\n- **Success signal**: all metrics computed without NaN or exception\n\n**Stage 5: Cost Tracking Validation (1 minute)**\n- After 10 LLM queries (3 methods × 3 examples + oracle), compute cumulative cost\n- Scale to full 200: verify that 200 queries × 3 methods × ~0.015 cost_per_call stays under $10\n- If projected cost > $10, alert before running full experiment\n- **Success signal**: \"Projected cost for full n=200: ${X.XX}, within budget\"\n\n**Stage 6: Full n=180 Subset Test (40 minutes, if stages 1-5 pass)**\n- Run all 3 methods on full n=180 with unified llama-3.2-3b\n- Compute F1, section recall, bootstrap CIs, statistical tests\n- Verify results are in expected range (F1 ~0.15-0.25 based on hypothesis disconfirmation)\n- Check for NaN, infinite, or missing values\n- **Success signal**: \"n=180 complete: F1 (cosine)={X}, F1 (bm25)={Y}, F1 (tfidf)={Z}, all p>0.37 (non-sig)\"\n\n**Stage 7: Full n=200 Run (remaining time, if stage 6 passes)**\n- Run all 3 methods on full n=200\n- Recompute all metrics\n- Compare n=180 vs n=200: are results stable? do CIs overlap?\n- **Success signal**: \"n=200 complete; F1 CI overlaps with n=180 CI, suggesting stable effect\"\n\n**Stage 8: ISF Mechanism Diagnostic Check**\n- Compute mean ISF by section type (Abstract, Introduction, Methods, Results)\n- Check: is Methods/Results ISF higher (supports mechanism) or lower (falsifies)?\n- **Expected result**: Methods/Results ISF **lower** than Introduction (falsifies hypothesis mechanism)\n\n**Stage 9: Error Classification & Final Outputs**\n- Classify all examples into [retrieval success/fail] × [reader success/fail] matrix\n- Generate method_out.json with all results, CIs, p-values, ISF diagnostics\n- Create examples_detail.json for spot-checking\n- **Success signal**: JSON valid, all required fields present, key findings populated\n\n**Abort Criteria (stop immediately if any triggered):**\n1. OpenRouter authentication fails after 3 retries → abort with clear error\n2. Cumulative cost exceeds $9.50 → halt and produce partial results on completed subset\n3. Data parsing fails on >10% of examples → abort and debug data loading\n4. Any method produces NaN or infinite scores on validation set → abort and fix algorithm\n5. Bootstrap CI computation crashes (e.g., all F1 scores identical) → fall back to standard error instead of bootstrap\n\n**Expected Outputs at Each Stage:**\n- Stage 1: `sample_data_loaded.txt` (10 examples printed)\n- Stage 2: `method_impl_validation.json` ({cosine, bm25, tfidf} retrieval outputs)\n- Stage 3: `lm_inference_test.json` ({answer, f1, cost})\n- Stage 4: `metrics_validation.json` ({f1_mean, recall, ci_low, ci_high, p_values})\n- Stage 5: `cost_projection.txt` (\"Projected: $X, within budget\")\n- Stages 6-9: `method_out.json` (final comprehensive output)"
}
```

### [13] TOOL RESULT — Write · 2026-07-20 11:46:25 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Reconcile TF-ISF Results: n=180 vs n=200 with Rigorous Controls\",\n  \"summary\": \"Re-implement cosine similarity, corpus-level BM25, and TF-ISF methods on both n=180 and n=200 QASPER subsets with identical preprocessing, unified LLM (llama-3.2-3b), and comprehensive statistical analysis including bootstrap CIs, per-example error classification, and diagnosis of mechanism assumptions.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# Phase 1: Data Loading & Preprocessing (unified pipeline)\\n1. Load both n=180 (previous experiment split) and n=200 (evaluation split) from dependency dataset\\n2. Parse each example: extract query, sections dict with section_id/section_type/section_text, gold_answer, metadata_evidence_section_ids\\n3. Apply identical tokenization and lowercasing to all sections\\n4. Build two separate section corpora:\\n   - Within-paper sections (per-paper ISF computation)\\n   - All-paper corpus of 81,550 sections (for corpus-level BM25)\\n5. Validation: confirm n=180 subset is proper prefix of n=200, check for NaN/empty fields\\n\\n# Phase 2: Retrieval Method Implementation\\n## Method A: Cosine Similarity (Dense Baseline)\\n  1. Load all-MiniLM-L6-v2 embeddings model (lightweight, CPU-safe)\\n  2. Embed all query strings once to avoid repeated inference\\n  3. Embed all sections in target paper once per paper\\n  4. For each query, compute cosine similarity query→section for all sections in paper\\n  5. Return top-k=3 sections ranked by similarity\\n  6. **Key invariant**: use ONLY sections from the query's own paper (single-paper retrieval)\\n\\n## Method B: Corpus-Level BM25 (Strong Baseline)\\n  1. Build rank_bm25 index over ALL 81,550 sections from entire QASPER corpus\\n  2. Tokenize each section: split on whitespace, lowercase, strip punctuation\\n  3. For each query, retrieve top-k=3 sections from ENTIRE corpus via BM25 scoring\\n  4. **Critical difference from prior**: retrieval is corpus-wide, not restricted to target paper\\n  5. Filter final results to only those from the query's target paper\\n      - If <3 sections from target paper in top-k corpus results, pad with next-best from paper\\n      - Log all padding events for diagnostic\\n  6. **Rationale**: corpus-level IDF uses global term frequencies, matches TF-ISF's use of same paper as baseline\\n\\n## Method C: TF-ISF (Within-Document Reweighting)\\n  1. For each paper, compute Inverse Section Frequency per term:\\n     ISF(term, paper) = log(N_sections / (1 + SF(term)))\\n       where SF(term) = count of sections in paper containing term\\n       N_sections = total sections in paper (typically 5-8)\\n  2. For each section, compute TF-ISF score = sum over query_terms of TF(term, section) * ISF(term, paper)\\n     TF(term, section) = 1 + log(count of term in section) if count > 0, else 0\\n  3. Rank sections within target paper by TF-ISF score\\n  4. Return top-k=3 sections from same paper\\n  5. **Validation**: compute ISF stats (mean, std, min, max per section type) on full n=200\\n\\n# Phase 3: LLM Inference & Answer Generation\\n## Primary pipeline: llama-3.2-3b-instruct via OpenRouter\\n  1. For each example and each retrieval method:\\n     - Concatenate top-k=3 retrieved sections + query into prompt:\\n       \\\"Answer this question based on the provided paper sections:\\\\n[SECTION_1]\\\\n[SECTION_2]\\\\n[SECTION_3]\\\\nQuestion: {query}\\\"\\n     - Call OpenRouter llama-3.2-3b at temperature=0 (deterministic)\\n     - Cap output to 256 tokens to control cost\\n     - Parse response as raw answer string\\n  2. Cost tracking: record tokens_in + tokens_out per call, sum cumulative cost\\n     - Budget: $10 max → ~$0.01-0.05 per query (200 queries × 3 methods = 600 LLM calls)\\n     - Abort if cumulative cost exceeds $9.50\\n  3. Store: {query_id, method, retrieved_section_ids, generated_answer, cost}\\n\\n## Secondary pipeline: tencent/hy3:free on n=180 subset ONLY\\n  1. Purpose: determine if n=180 positive result was LLM-dependent\\n  2. Run all three methods on n=180 subset with tencent/hy3:free model (the original)\\n  3. Use same prompt template and output format for direct comparison\\n  4. Cost: should be free or minimal, confirm before running\\n\\n## Oracle Baseline (Answer Quality Upper Bound)\\n  1. For each example, feed gold evidence sections directly to llama-3.2-3b\\n  2. Use same prompt template: \\\"Answer based on: [GOLD_SECTIONS]\\\\n{query}\\\"\\n  3. Compute F1 on oracle answers → reader upper bound\\n  4. If oracle F1 is high (~0.70+), bottleneck is retrieval; if low, bottleneck is reader\\n\\n# Phase 4: Evaluation Metrics (all subsets)\\n## For each method × subset combination:\\n  1. **Token F1**: apply standard SQuAD-style token-level F1\\n     - Tokenize gold_answer and generated_answer (whitespace split, lowercase, remove punct)\\n     - F1 = 2*(precision*recall) / (precision+recall)\\n     - Precision = |generated_tokens ∩ gold_tokens| / |generated_tokens|\\n     - Recall = |generated_tokens ∩ gold_tokens| / |gold_tokens|\\n  2. **Section Recall**: measure retrieval quality independently\\n     - For each example, check if ANY of top-k retrieved sections match gold evidence section IDs\\n     - section_recall = (# examples with ≥1 gold section in top-k) / total_examples\\n  3. **Exact Match (EM)**: binary 1 if F1==1.0, else 0\\n  4. **Bootstrap CIs (95%)**:\\n     - Resample examples with replacement, compute F1/recall for each resample (n_iterations=10000)\\n     - CIs = percentile(5, 95) of bootstrap F1 distribution\\n     - Report: F1 (CI_low, CI_high)\\n  5. **Statistical Tests** (Holm-Corrected):\\n     - Pairwise t-tests on F1 scores: cosine vs BM25, cosine vs TF-ISF, BM25 vs TF-ISF\\n     - Report: t-stat, p-value (uncorrected), Holm-corrected significance\\n     - Effect size: Cohen's d for each comparison\\n     - **Interpretation**: p > 0.05 (Holm) → non-significant difference\\n\\n## Per-Subset Analysis\\n  1. Compute all metrics above separately for n=180 and n=200\\n  2. Explain numerical differences: data-distribution differences, sample-size effects\\n  3. Report: \\\"n=180 vs n=200 F1 delta = {delta}, likely due to [data/LLM/sample-size/other]\\\"\\n\\n# Phase 5: ISF Mechanism Diagnostics (n=200 only, NO gold-section filtering)\\n  1. For every term in every section, compute its ISF score\\n  2. Aggregate by section type: compute mean ISF for Abstract, Introduction, Methods, Results, Discussion sections\\n  3. Report: \\\"Mean ISF(Methods) = {x}, Mean ISF(Introduction) = {y}\\\"\\n  4. **Key interpretation**: if Methods/Results have HIGHER ISF (section-unique vocabulary), mechanism is supported\\n     - Actual result: Methods/Results have LOWER ISF (shared vocabulary), mechanism is contradicted\\n  5. Compute term-level diagnostics:\\n     - Top-20 highest ISF terms (section-specific)\\n     - Top-20 lowest ISF terms (document theme terms)\\n     - Distribution of ISF by section type (histogram)\\n\\n# Phase 6: Per-Example Error Classification (n=200)\\n  1. For each example, compute 2×2 matrix:\\n     - Retrieval Success? = (ANY gold section in top-3 retrieved) → Yes/No\\n     - Reader Success? = (F1 >= 0.50 threshold) → Yes/No\\n  2. Categorize all examples into 4 buckets:\\n     - [R_yes, Reader_yes]: Both succeed (ideal)\\n     - [R_yes, Reader_no]: Retrieval OK but reader fails (reader quality bottleneck)\\n     - [R_no, Reader_yes]: Retrieval fails but reader can infer (robust reader)\\n     - [R_no, Reader_no]: Both fail (unfixable)\\n  3. Count distribution across methods\\n  4. Report: \\\"Cosine: {R+/R-} retrieval; TF-ISF: {R+/R-} retrieval\\\" → does TF-ISF improve retrieval?\\n  5. Identify example IDs where method differences are largest (for qualitative inspection)\\n\\n# Phase 7: LLM Model Dependency Check (n=180 only)\\n  1. Compare results on n=180 with:\\n     - llama-3.2-3b (unified primary LLM)\\n     - tencent/hy3:free (original LLM from n=180 prior experiment)\\n  2. If F1 difference > 0.10 between models → positive prior result was LLM-dependent\\n  3. Report: \\\"F1 delta (llama vs hy3) = {delta}\\\"; conclude on LLM role\\n\\n# Phase 8: Output Aggregation & JSON Structure\\n  1. Collect all results into method_out.json:\\n     {\\n       \\\"experiment_id\\\": \\\"experiment_iter2_dir2\\\",\\n       \\\"datasets\\\": {\\n         \\\"n180\\\": {\\\"subset_label\\\": \\\"previous_experiment_split\\\", \\\"example_count\\\": 180},\\n         \\\"n200\\\": {\\\"subset_label\\\": \\\"full_evaluation_split\\\", \\\"example_count\\\": 200}\\n       },\\n       \\\"methods\\\": [\\\"cosine\\\", \\\"bm25_corpus\\\", \\\"tfidf\\\"],\\n       \\\"results\\\": {\\n         \\\"n180\\\": {\\n           \\\"cosine\\\": {\\\"f1_mean\\\": 0.XXX, \\\"f1_ci\\\": [0.XXX, 0.XXX], \\\"section_recall\\\": 0.XXX, ...},\\n           \\\"bm25\\\": {...},\\n           \\\"tfidf\\\": {...}\\n         },\\n         \\\"n200\\\": {...},\\n         \\\"oracle\\\": {\\\"f1_mean\\\": 0.XXX, \\\"upper_bound_on_retrieval_impact\\\": \\\"interpretation\\\"}\\n       },\\n       \\\"statistical_tests\\\": {\\n         \\\"n180\\\": {\\n           \\\"cosine_vs_bm25\\\": {\\\"t_stat\\\": X, \\\"p_value\\\": X, \\\"holm_significant\\\": bool, \\\"cohens_d\\\": X},\\n           ...\\n         }\\n       },\\n       \\\"idf_diagnostics\\\": {\\n         \\\"section_type_mean_isf\\\": {\\\"Abstract\\\": 1.34, \\\"Methods\\\": 1.23, ...},\\n         \\\"mechanism_supported\\\": false,\\n         \\\"interpretation\\\": \\\"Evidence sections have lower (not higher) ISF; vocabulary stratification falsified\\\"\\n       },\\n       \\\"error_classification\\\": {\\n         \\\"n200\\\": {\\n           \\\"cosine\\\": {\\\"retrieval_yes_reader_yes\\\": X, \\\"retrieval_yes_reader_no\\\": X, ...},\\n           ...\\n         }\\n       },\\n       \\\"lm_dependency_check\\\": {\\n         \\\"n180_llama_vs_hy3_delta\\\": 0.XXX,\\n         \\\"conclusion\\\": \\\"positive_prior_result_was_[lm_dependent|independent]\\\"\\n       },\\n       \\\"key_findings\\\": [\\n         \\\"TF-ISF achieves F1=0.187, no better than cosine (F1=0.198) or BM25 (F1=0.179); all p>0.37\\\",\\n         \\\"Methods/Results sections have LOWER ISF than Introduction; mechanism contradicted\\\",\\n         \\\"Oracle F1=0.XXX reveals [retrieval|reader] as primary bottleneck\\\",\\n         \\\"n=180 vs n=200 difference explained by [cause]\\\"\\n       ],\\n       \\\"recommendations\\\": [\\n         \\\"Term reweighting insufficient; explore discourse-aware or embedding-fine-tuned approaches\\\",\\n         \\\"Dense embedding quality for scientific domain may limit all retrieval methods\\\",\\n         \\\"Section granularity coarse; finer chunk-level retrieval worth testing\\\"\\n       ]\\n     }\\n  2. Additionally save detailed per-example results for error analysis:\\n     examples_detail.json with {query_id, gold_answer, retrieved_by_cosine, retrieved_by_bm25, retrieved_by_tfidf, ...}\\n\\n# Cost Management\\n- Track cumulative OpenRouter spend after every 50 queries\\n- Stop if approaching $9.50 (leave $0.50 buffer)\\n- If budget exhausted on full n=200, fall back to:\\n  - Halve remaining subset (n=100 random subsample)\\n  - Re-run stats on the smaller sample\\n  - Report: \\\"Executed on n=100 subsample due to budget constraints\\\"\\n- Always report actual cumulative cost in output JSON\",\n  \"fallback_plan\": \"**Scenario 1: OpenRouter API failures or rate-limiting**\\n- Retry failed calls up to 3 times with exponential backoff (1s, 5s, 30s)\\n- If tencent/hy3:free is unavailable, skip LLM-dependency check (non-critical)\\n- If llama-3.2-3b unavailable after retries, switch to next-cheapest equivalent (Llama-3-8B-Instruct or Mistral-7B)\\n- Fall back to local sentence-transformers-based scoring without LLM if all OpenRouter models fail\\n\\n**Scenario 2: Budget exhaustion mid-run**\\n- At 90% of budget ($9.00 spent), switch from full n=200 to random stratified subsample (n=50-100)\\n- Recompute bootstrap CIs on reduced sample; report sample size clearly\\n- Skip LLM-dependency check if budget doesn't permit tencent/hy3:free testing\\n\\n**Scenario 3: Embedding model memory issues on CPU**\\n- all-MiniLM-L6-v2 is ~80MB; if OOM, batch embedding computation (process 50 sections at a time)\\n- As fallback, use lighter model: all-MiniLM-L12-v2 (smaller) or switch to BM25-only comparison\\n\\n**Scenario 4: rank_bm25 corpus index too large**\\n- If indexing all 81,550 sections causes memory overload:\\n  - Split corpus into chunks (papers 0-400, 400-800, etc.)\\n  - For each query, retrieve from same-paper chunk first, then nearby chunks\\n  - Fall back to BM25 restricted to target paper only (loses corpus-level IDF component)\\n\\n**Scenario 5: Token F1 computation edge cases**\\n- Empty generated answer → F1=0\\n- Gold answer contains only stop words (the, a, is) → likely F1>0 but low precision (OK)\\n- Case sensitivity issues → always lowercase both before tokenization\\n\\n**Scenario 6: n=180 subset not a clean prefix of n=200**\\n- If data structure differs (different queries or sections), fall back to loading both independently\\n- Align on common examples (query_id intersection) if mismatch found\\n- Document any data inconsistencies in output JSON\\n\\n**Scenario 7: Missing gold sections or metadata**\\n- Skip examples with missing metadata_evidence_section_ids; log count of skipped\\n- Recompute metrics on non-skipped subset; report filtering ratio\\n\\n**Simplified fallback (if multiple failures compound):**\\n- Run Methods A (cosine) and C (TF-ISF) on n=200 with oracle answer generation (feed gold sections)\\n- Skip LLM inference, BM25 implementation, bootstrap CIs, and statistical tests\\n- Produce limited output: cosine vs TF-ISF section recall + ISF diagnostics only\\n- This isolates the retrieval signal from reader confounds\",\n  \"testing_plan\": \"**Stage 1: Data Loading Smoke Test (first 5 minutes)**\\n- Load first 10 examples from both n=180 and n=200 subsets\\n- Parse sections, validate structure (section_id, section_type, section_text present)\\n- Confirm n=180 is prefix of n=200 (spot-check query_ids)\\n- Print sample query, sections, and gold answer to verify data fidelity\\n- **Success signal**: \\\"10 examples loaded, parsed, and validated successfully\\\"\\n\\n**Stage 2: Method Implementation Validation (next 10 minutes)**\\n- Implement skeleton of each method on same 10 examples\\n\\n**A. Cosine Similarity:**\\n  - Load all-MiniLM-L6-v2 (confirm model downloads without error)\\n  - Embed 3 queries + 30 sections\\n  - Compute cosine similarity matrix (3 queries × 30 sections)\\n  - Retrieve top-k=3 for each query; inspect section IDs (should be from target paper)\\n  - **Success**: retrieval returns valid section IDs with decreasing similarity scores\\n\\n**B. BM25 Corpus:**\\n  - Index just 10 papers (~500 sections) from the dependency dataset\\n  - Query with 3 test queries\\n  - Retrieve top-k=3 and filter to target paper\\n  - **Success**: BM25 index built, query→top-k retrieval works, filtering applied\\n\\n**C. TF-ISF:**\\n  - On 10 papers, compute ISF for each term\\n  - Compute mean ISF by section type (expected: intro high, methods/results low in prior hyp)\\n  - Retrieve top-k=3 for 3 queries using TF-ISF\\n  - **Success**: ISF scores computed without NaN, retrieval produces valid section IDs\\n\\n**Stage 3: LLM Inference Validation (next 5 minutes)**\\n- Call OpenRouter llama-3.2-3b with 1 example query + retrieved sections\\n- Verify API authentication, response format, token count\\n- Compute token F1 on generated answer vs gold\\n- **Success signal**: response received, F1 computed, cost logged\\n- If OpenRouter unavailable, abort with clear error message\\n\\n**Stage 4: Statistics & Metrics Validation (next 5 minutes)**\\n- On the 10-example validation set, compute:\\n  - Token F1 (all 3 methods)\\n  - Section recall (all 3 methods)\\n  - Bootstrap CI on tiny sample (check confidence intervals are reasonable, CI_low < mean < CI_high)\\n  - Pairwise t-tests (should complete without error even on tiny n)\\n- **Success signal**: all metrics computed without NaN or exception\\n\\n**Stage 5: Cost Tracking Validation (1 minute)**\\n- After 10 LLM queries (3 methods × 3 examples + oracle), compute cumulative cost\\n- Scale to full 200: verify that 200 queries × 3 methods × ~0.015 cost_per_call stays under $10\\n- If projected cost > $10, alert before running full experiment\\n- **Success signal**: \\\"Projected cost for full n=200: ${X.XX}, within budget\\\"\\n\\n**Stage 6: Full n=180 Subset Test (40 minutes, if stages 1-5 pass)**\\n- Run all 3 methods on full n=180 with unified llama-3.2-3b\\n- Compute F1, section recall, bootstrap CIs, statistical tests\\n- Verify results are in expected range (F1 ~0.15-0.25 based on hypothesis disconfirmation)\\n- Check for NaN, infinite, or missing values\\n- **Success signal**: \\\"n=180 complete: F1 (cosine)={X}, F1 (bm25)={Y}, F1 (tfidf)={Z}, all p>0.37 (non-sig)\\\"\\n\\n**Stage 7: Full n=200 Run (remaining time, if stage 6 passes)**\\n- Run all 3 methods on full n=200\\n- Recompute all metrics\\n- Compare n=180 vs n=200: are results stable? do CIs overlap?\\n- **Success signal**: \\\"n=200 complete; F1 CI overlaps with n=180 CI, suggesting stable effect\\\"\\n\\n**Stage 8: ISF Mechanism Diagnostic Check**\\n- Compute mean ISF by section type (Abstract, Introduction, Methods, Results)\\n- Check: is Methods/Results ISF higher (supports mechanism) or lower (falsifies)?\\n- **Expected result**: Methods/Results ISF **lower** than Introduction (falsifies hypothesis mechanism)\\n\\n**Stage 9: Error Classification & Final Outputs**\\n- Classify all examples into [retrieval success/fail] × [reader success/fail] matrix\\n- Generate method_out.json with all results, CIs, p-values, ISF diagnostics\\n- Create examples_detail.json for spot-checking\\n- **Success signal**: JSON valid, all required fields present, key findings populated\\n\\n**Abort Criteria (stop immediately if any triggered):**\\n1. OpenRouter authentication fails after 3 retries → abort with clear error\\n2. Cumulative cost exceeds $9.50 → halt and produce partial results on completed subset\\n3. Data parsing fails on >10% of examples → abort and debug data loading\\n4. Any method produces NaN or infinite scores on validation set → abort and fix algorithm\\n5. Bootstrap CI computation crashes (e.g., all F1 scores identical) → fall back to standard error instead of bootstrap\\n\\n**Expected Outputs at Each Stage:**\\n- Stage 1: `sample_data_loaded.txt` (10 examples printed)\\n- Stage 2: `method_impl_validation.json` ({cosine, bm25, tfidf} retrieval outputs)\\n- Stage 3: `lm_inference_test.json` ({answer, f1, cost})\\n- Stage 4: `metrics_validation.json` ({f1_mean, recall, ci_low, ci_high, p_values})\\n- Stage 5: `cost_projection.txt` (\\\"Projected: $X, within budget\\\")\\n- Stages 6-9: `method_out.json` (final comprehensive output)\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [14] ASSISTANT · 2026-07-20 11:46:46 UTC

```
Perfect! I've completed the comprehensive plan for the experiment. Here's what I've delivered:

## Plan Summary

I created a **detailed, executor-ready EXPERIMENT PLAN** (`method_out.json`) that directly addresses reconciling the contradictory n=180 vs n=200 results. The plan is organized into 8 concrete phases:

### Core Strengths:

1. **Unified Implementation Strategy**
   - Identical preprocessing pipeline for both n=180 and n=200 subsets
   - Three methods with precise algorithmic specifications:
     - **Cosine Similarity**: all-MiniLM-L6-v2 embeddings, single-paper retrieval
     - **Corpus-level BM25**: rank_bm25 index over all 81,550 sections, corpus-wide IDF
     - **TF-ISF**: Within-document term reweighting with formula ISF(t) = log(N_sections / (1 + SF(t)))

2. **Rigorous Statistical Evaluation**
   - Bootstrap CIs (95%, 10,000 resamples) for all metrics
   - Holm-corrected pairwise t-tests with Cohen's d effect sizes
   - Explicit success criteria: p>0.37 (non-significant differences) as shown in hypothesis

3. **Mechanism Diagnostics**
   - Compute mean ISF by section type to test core assumption
   - Expected result from hypothesis: Methods/Results have **lower** ISF than Introduction (mechanism falsified)
   - Per-term ISF analysis: top-20 highest/lowest and distribution plots

4. **Failure Mode Isolation**
   - 2×2 per-example error classification: (Retrieval success/fail) × (Reader success/fail)
   - Oracle baseline to determine bottleneck (retrieval vs reader quality)
   - LLM-dependency check: compare llama-3.2-3b vs tencent/hy3:free on n=180

5. **Comprehensive Testing Plan** (9 progressive stages)
   - Data loading validation (10 examples)
   - Method implementation tests (each method on sample)
   - LLM inference test (cost & API validation)
   - Full n=180 run (~40 min), then n=200 (~remaining time)
   - Abort criteria clearly specified (API failure, budget exhaustion >$9.50, data parsing >10% failures)

### Compute & Budget:
- **Profile**: `cpu_heavy` (4 vCPUs, 32GB RAM) — sufficient for embeddings (~80MB model) and 81,550-section BM25 indexing
- **LLM Budget**: $10 max; ~600 API calls (200 queries × 3 methods); paced with cost tracking every 50 queries

### Output Structure:
Comprehensive `method_out.json` with nested results for:
- Per-subset F1/recall with CIs (n=180, n=200, oracle)
- Statistical tests (p-values, effect sizes, Holm-corrected significance)
- ISF diagnostics (mean by section type, term distributions)
- Error classifications (4-way matrix per method)
- LLM-dependency delta
- Key findings and recommendations for future work

The plan is ready for the executor to implement without ambiguity.
```
