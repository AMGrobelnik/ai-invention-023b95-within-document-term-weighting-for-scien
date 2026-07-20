# upd_hypo — test_idea

> Phase: `invention_loop` · round 1 · `upd_hypo`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 11:40:51 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Within-Doc Term Rarity Fixes Section Retrieval
hypothesis: >-
  Standard dense retrieval systematically mis-ranks sections within scientific PDFs because it treats query-term matches uniformly,
  regardless of how many sections in the same document share that term. We hypothesize that replacing cross-corpus IDF with
  an Intra-Document Inverse Section Frequency (ISF) — ISF(t) = log(N_sections / (1 + SF(t))), where SF(t) is the count of
  sections in the target paper containing term t — produces a TF-ISF score that better identifies the evidence-bearing sections.
  Specifically, 'document theme terms' (e.g., the paper's topic words) appear in nearly every section, providing no discriminative
  signal; meanwhile, section-specific terms (precise technique names, numeric variable identifiers, unique experimental conditions)
  appear in only one or two sections and are the true discriminative signal for locating evidence. TF-ISF up-weights section-specific
  terms and down-weights document theme terms, thereby counteracting the retrieval bias toward claim-dense sections (Abstract,
  Introduction, Conclusion) that repeat theme terms in query-friendly language while directing retrieval toward evidence-dense
  sections (Methods, Results) that contain section-unique terms. We predict this training-free, self-contained score improves
  section recall and downstream answer F1 on QASPER relative to a fixed-k cosine-similarity baseline.
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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
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

--- Item 2 ---
id: art_E7rG9mK6gbrb
type: experiment
title: TF-ISF vs BM25 vs Cosine Section Retrieval
summary: >-
  Experiment benchmarking three retrieval methods on the QASPER scientific QA dataset (180 questions, 888 papers). Methods:
  (A) Cosine similarity using sentence-transformers all-MiniLM-L6-v2, (B) BM25Okapi using rank_bm25, (C) TF-ISF (Term Frequency-Inverse
  Section Frequency) — a novel document-local scoring method that computes IDF within a document across its sections rather
  than across a corpus. For each question, top-3 sections are retrieved per method, fed to a free LLM reader (tencent/hy3:free
  via OpenRouter), and scored with token-level F1 against gold answers. Results: TF-ISF achieves mean F1=0.221 (best), BM25
  F1=0.213, Cosine F1=0.206. TF-ISF beats cosine by +0.015 F1 overall and wins on Methods and Results section subgroups —
  the technically dense sections where document-local IDF most suppresses document-theme terms. Section recall: cosine highest
  (0.154), TF-ISF lower (0.098), suggesting TF-ISF improves downstream QA beyond raw retrieval recall. API cost: $0.00 (free
  model). Hypothesis CONFIRMED: TF-ISF outperforms cosine on answer F1, with largest gains on methods/results sections.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 3 ---
id: art_r9whYzfM2OVO
type: evaluation
title: TF-ISF vs Cosine vs BM25 Section Retrieval on QASPER
summary: |-
  Full statistical evaluation of three section-retrieval methods (cosine similarity via all-MiniLM-L6-v2, BM25Okapi, and TF-ISF) on 200 QASPER scientific QA examples.

  KEY RESULTS (n=200 questions):
  - Token F1: TF-ISF=0.1872, Cosine=0.1978, BM25=0.1794
  - Section Recall@3: TF-ISF=0.484, Cosine=0.467, BM25=0.525

  STATISTICAL SIGNIFICANCE (paired t-test, Holm-Bonferroni corrected):
  - TF-ISF vs Cosine F1: delta=-0.011, p=0.419 (not significant), Cohen's d=-0.060
  - TF-ISF vs BM25 F1: delta=+0.008, p=0.373 (not significant), Cohen's d=+0.045
  - TF-ISF vs Cosine Recall: delta=+0.017, p=0.683 (not significant), d=+0.036
  - TF-ISF vs BM25 Recall: delta=-0.042, p=0.158 (not significant), d=-0.090
  All comparisons are non-significant; no method clearly dominates.

  SUBGROUP ANALYSIS by gold evidence section type:
  - Abstract/Introduction: per-method F1 and Recall@3 computed
  - Methods/Results: per-method F1 and Recall@3 computed
  - Discussion/Conclusion: per-method F1 and Recall@3 computed

  ISF DIAGNOSTIC (mechanism test):
  - Introduction: mean ISF=1.335, Methods: mean ISF=1.228, Results: mean ISF=1.243
  FINDING: Methods/Results have LOWER ISF than Introduction — hypothesized mechanism DISCONFIRMED.

  LLM READER: meta-llama/llama-3.2-3b-instruct via OpenRouter ($0.014 total cost).

  FILES: eval.py (full implementation), eval_out.json (200 examples with all per-example metrics and aggregate stats).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

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

id: art_E7rG9mK6gbrb
type: experiment
title: TF-ISF vs BM25 vs Cosine Section Retrieval
summary: >-
  Experiment benchmarking three retrieval methods on the QASPER scientific QA dataset (180 questions, 888 papers). Methods:
  (A) Cosine similarity using sentence-transformers all-MiniLM-L6-v2, (B) BM25Okapi using rank_bm25, (C) TF-ISF (Term Frequency-Inverse
  Section Frequency) — a novel document-local scoring method that computes IDF within a document across its sections rather
  than across a corpus. For each question, top-3 sections are retrieved per method, fed to a free LLM reader (tencent/hy3:free
  via OpenRouter), and scored with token-level F1 against gold answers. Results: TF-ISF achieves mean F1=0.221 (best), BM25
  F1=0.213, Cosine F1=0.206. TF-ISF beats cosine by +0.015 F1 overall and wins on Methods and Results section subgroups —
  the technically dense sections where document-local IDF most suppresses document-theme terms. Section recall: cosine highest
  (0.154), TF-ISF lower (0.098), suggesting TF-ISF improves downstream QA beyond raw retrieval recall. API cost: $0.00 (free
  model). Hypothesis CONFIRMED: TF-ISF outperforms cosine on answer F1, with largest gains on methods/results sections.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_r9whYzfM2OVO
type: evaluation
title: TF-ISF vs Cosine vs BM25 Section Retrieval on QASPER
summary: |-
  Full statistical evaluation of three section-retrieval methods (cosine similarity via all-MiniLM-L6-v2, BM25Okapi, and TF-ISF) on 200 QASPER scientific QA examples.

  KEY RESULTS (n=200 questions):
  - Token F1: TF-ISF=0.1872, Cosine=0.1978, BM25=0.1794
  - Section Recall@3: TF-ISF=0.484, Cosine=0.467, BM25=0.525

  STATISTICAL SIGNIFICANCE (paired t-test, Holm-Bonferroni corrected):
  - TF-ISF vs Cosine F1: delta=-0.011, p=0.419 (not significant), Cohen's d=-0.060
  - TF-ISF vs BM25 F1: delta=+0.008, p=0.373 (not significant), Cohen's d=+0.045
  - TF-ISF vs Cosine Recall: delta=+0.017, p=0.683 (not significant), d=+0.036
  - TF-ISF vs BM25 Recall: delta=-0.042, p=0.158 (not significant), d=-0.090
  All comparisons are non-significant; no method clearly dominates.

  SUBGROUP ANALYSIS by gold evidence section type:
  - Abstract/Introduction: per-method F1 and Recall@3 computed
  - Methods/Results: per-method F1 and Recall@3 computed
  - Discussion/Conclusion: per-method F1 and Recall@3 computed

  ISF DIAGNOSTIC (mechanism test):
  - Introduction: mean ISF=1.335, Methods: mean ISF=1.228, Results: mean ISF=1.243
  FINDING: Methods/Results have LOWER ISF than Introduction — hypothesized mechanism DISCONFIRMED.

  LLM READER: meta-llama/llama-3.2-3b-instruct via OpenRouter ($0.014 total cost).

  FILES: eval.py (full implementation), eval_out.json (200 examples with all per-example metrics and aggregate stats).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Scientific question answering over long research papers is a critical task for automated literature review, clinical evidence synthesis, and research acceleration. However, despite advances in dense retrieval methods and large language models, a systematic failure mode remains poorly understood: when a reader queries a paper for specific evidence, standard retrieval often returns sections that are high in rhetorical clarity (Abstract, Introduction, Conclusion) while ranking evidence-bearing sections (Methods, Results) lower in the retrieval list. This is not random error—it reflects a structural property of scientific writing itself. The IMRaD (Introduction, Methods, Results, and Discussion) convention, by design, separates claims and their accessible restatement in early and concluding sections from the detailed, specialized evidence in Methods and Results.

The problem is acute in modern retrieval-augmented generation (RAG) systems. Dense passage retrievers like DPR [1] or sentence-transformers embeddings score text similarity using neural embeddings, which excel at semantic matching. Yet semantic similarity, when applied to scientific papers, tends to reward sections that paraphrase the paper's topic in accessible language—precisely what Abstract and Introduction are designed to do. Meanwhile, the technical vocabulary, specific parameter values, and precise experimental conditions in Methods and Results sections are sparse and section-unique; they may not score highly under cosine similarity with a natural-language query. This is reminiscent of a classic problem in information retrieval: the vocabulary gap between query and document, which traditional term-weighting methods like TF-IDF address by down-weighting high-frequency (document-theme) terms and up-weighting rare (discriminative) terms [2].

We hypothesize that applying this principle within a single document—replacing cross-corpus IDF with within-document Inverse Section Frequency (ISF)—could correct the retrieval bias. The intuition is simple: if a term appears in nearly every section of a paper, it is a document theme term and provides little discriminative signal for ranking sections; if a term appears in only one or two sections, it is section-specific and should strongly indicate those sections. A training-free, self-contained scoring function could identify evidence-bearing sections without external discourse models, citation graphs, or LLM inference at retrieval time [ARTIFACT:art_HHk7NUDMfOf5].

We conducted a controlled evaluation on 200 examples from QASPER [3], a public benchmark of information-seeking questions over NLP papers. Three retrieval methods were compared: (1) cosine similarity with sentence-transformers embeddings, (2) BM25 with corpus-level IDF, and (3) TF-ISF using within-document section frequency. For each method, the top-3 sections were retrieved and fed to a small LLM reader to generate answers, which were then scored against gold answers using token-level F1. We also computed section-level recall and performed subgroup analysis by section type.

Our results disconfirm the core hypothesis. TF-ISF achieved F1=0.187, performing no better than cosine (F1=0.198) or BM25 (F1=0.179). Differences were statistically non-significant (p > 0.37). Notably, the intended mechanism—lowering ISF for claim-dense sections and raising it for evidence sections—was inverted: Methods and Results sections had lower mean ISF (1.23–1.24) than Introduction sections (1.34). This suggests the vocabulary gap is either not the primary retrieval bottleneck or manifests differently than our hypothesis predicted.

[FIGURE:fig_main_results]

These findings provide a valuable boundary condition: while term-weighting strategies have long been effective for keyword search and sparse retrieval, their naive within-document application does not rescue dense retrieval in scientific QA. The challenge in section retrieval may instead lie in the quality and training of dense embeddings, the granularity and structural clarity of document sections, or a fundamental mismatch between how readers phrase queries and how evidence is presented in technical sections. This paper contributes a rigorous negative result, showing both what does not work and why—and pointing toward future directions in scientific document understanding.

# Related Work

**Dense Retrieval for Question Answering.** Dense passage retrieval (DPR) [4] and related methods like ColBERT [5] have become standard approaches for open-domain QA by learning dual encoders for queries and documents. These methods have been extended to long documents through hierarchical retrieval (e.g., retrieving paragraphs or sections before sentences). However, most work focuses on short passages or web documents, where vocabulary structure is less stratified than in scientific papers.

**Scientific Document Understanding.** QASPER [3] is the first large-scale QA dataset anchored to full research papers, designed to measure the difficulty of complex reasoning across paper sections. Prior work on scientific document processing has focused on section classification, rhetorical role labeling, and citation analysis, but less on within-document section ranking for evidence retrieval. Cohan et al. [6] explored hierarchical attention over paper sections, but did not isolate the effect of term frequency on ranking.

**Term Weighting and Vocabulary Effects.** TF-IDF, introduced by Spärck Jones [2], is foundational to information retrieval and has inspired decades of variants (BM25, TF-IDF-smooth, etc.). The principle is well-established: high-frequency terms in a corpus are poor discriminators; rare terms are good discriminators. Our work applies this intuition at document-local scope, but we find the effect does not transfer to dense retrieval. This resonates with recent critiques of DPR [7], which argue that dense embeddings can be brittle and fail to capture fine-grained term relevance.

**Retrieval-Augmented Generation.** Lewis et al. [1] proposed RAG, combining retrieval with generation to answer knowledge-intensive questions. Subsequent work has explored improving retrieval through reranking, query expansion, and semantic parsing. However, retrieval quality remains a bottleneck in many domains, especially for domain-specific terminology in scientific papers.

# Methods

## Dataset and Task Setup

We used the QASPER dataset [3], selecting 200 examples from the development split for statistical robustness. Each example consists of: (1) a natural-language question written by an NLP practitioner who read only the paper's title and abstract, (2) a full research paper parsed into typed sections (Abstract, Introduction, Methods, Results, Discussion, Conclusion, Other), (3) gold evidence section IDs identifying which sections contain the answer, and (4) a gold answer string. The 200 questions span 150+ unique papers [ARTIFACT:art_HHk7NUDMfOf5].

## Retrieval Methods

**Baseline 1: Cosine Similarity (Dense Embedding).** For each question-section pair, we encoded the question and section text using all-MiniLM-L6-v2, a lightweight sentence-transformers model. Cosine similarity between embeddings was computed, and the top-3 sections were ranked by score.

**Baseline 2: BM25.** We implemented standard BM25 ranking using the rank_bm25 library, with corpus-level inverse document frequency computed over all 81,550 sections across 289 papers in the QASPER dataset. BM25 is a probabilistic retrieval model that combines term frequency, inverse document frequency, and document length normalization, and serves as a strong lexical baseline [8].

**Proposed Method: TF-ISF.** For each section within a target paper, we computed a TF-ISF score for each query term as follows:

$$\text{TF-ISF}(q, s) = \sum_{t \in q} \text{TF}(t, s) \times \log\left(\frac{N_\text{sections}}{1 + \text{SF}(t)}\right)$$

where $q$ is the query, $s$ is the section, TF(t, s) is the raw term frequency of term $t$ in section $s$, $N_\text{sections}$ is the total number of sections in the paper, and SF(t) is the count of sections in that paper containing term $t$ (section frequency). The within-document ISF score is computed as $\log(N_\text{sections} / (1 + \text{SF}(t)))$, analogous to corpus-level IDF but scoped to a single document.

Terms were lowercased and stopwords (common English words) were removed. Section frequency was computed by simple presence (binary: section contains term or not), not raw count. The intuition is that terms appearing in most sections of a paper (high SF) receive low ISF and contribute little to ranking; terms appearing in few sections receive high ISF and are strong section indicators.

## Answer Generation and Evaluation

For each question, the top-3 retrieved sections (per method) were concatenated with the original question and passed to a small LLM reader for answer generation. We used meta-llama/llama-3.2-3b-instruct via OpenRouter, a freely available model that balances cost and capability. The LLM was prompted to extract or synthesize an answer from the provided section text.

Answers were evaluated using token-level F1 against gold answers, computed as the harmonic mean of precision and recall of token overlaps (after lowercasing and punctuation removal). This metric is standard in QASPER evaluation and captures both partial credit and answer completeness.

We also computed section-level recall: the fraction of gold evidence sections appearing in the top-3 retrieved by each method. This diagnostic metric measures retrieval quality independently of LLM answer quality.

## Statistical Analysis

We conducted paired t-tests with Holm-Bonferroni correction for multiple comparisons. Cohen's d was computed to estimate effect size. Bootstrap confidence intervals (95%, 10,000 resamples) were computed for mean F1 and recall per method. All comparisons are two-tailed.

# Results

[FIGURE:fig_method_comparison]

## Overall Performance

On 200 questions (n=200), the three methods achieved the following mean token F1 scores and section recall@3:

- **Cosine Similarity**: F1 = 0.198 (95% CI: [0.174, 0.223]), Recall = 0.467 (95% CI: [0.403, 0.531])
- **BM25**: F1 = 0.179 (95% CI: [0.157, 0.202]), Recall = 0.525 (95% CI: [0.462, 0.589])
- **TF-ISF**: F1 = 0.187 (95% CI: [0.163, 0.213]), Recall = 0.484 (95% CI: [0.418, 0.548])

None of the pairwise differences were statistically significant (all p > 0.37; Holm-corrected). TF-ISF vs. Cosine: Δ = −0.011 (p = 0.419, d = −0.060). TF-ISF vs. BM25: Δ = +0.008 (p = 0.373, d = +0.045). Cosine vs. BM25: Δ = +0.018 (p = 0.153, d = +0.053).

## Subgroup Analysis by Section Type

We stratified results by the type of gold evidence section to test whether TF-ISF specifically rescues questions whose answers are in Methods or Results sections.

**Abstract/Introduction (n=31)**: Cosine F1=0.192, TF-ISF F1=0.158, BM25 F1=0.170. TF-ISF underperforms, not a win.

**Methods/Results (n=137)**: Cosine F1=0.208, TF-ISF F1=0.201, BM25 F1=0.185. TF-ISF is slightly closer to cosine but does not exceed it. Recall: TF-ISF 0.493 vs. Cosine 0.490 (negligible difference).

**Discussion/Conclusion (n=12)**: TF-ISF F1=0.134 (worst), Cosine F1=0.192, BM25 F1=0.156. TF-ISF significantly underperforms on this small group.

**Other (n=53)**: Cosine F1=0.193, TF-ISF F1=0.172, BM25 F1=0.181. No advantage for TF-ISF.

Across all subgroups, TF-ISF never significantly outperforms the baselines. The intended mechanism—boosting Methods/Results retrieval—is not observed [ARTIFACT:art_r9whYzfM2OVO].

## Mechanism Diagnostic: ISF by Section Type

To diagnose why TF-ISF underperformed, we computed mean ISF (Inverse Section Frequency) scores for all terms in each section type across all papers:

- **Introduction**: Mean ISF = 1.335 (median = 1.415, SD = 0.275, n=149 sections)
- **Methods**: Mean ISF = 1.227 (median = 1.237, SD = 0.224, n=839 sections)
- **Results**: Mean ISF = 1.243 (median = 1.234, SD = 0.208, n=161 sections)
- **Related Work**: Mean ISF = 1.327 (median = 1.361, SD = 0.260, n=147 sections)
- **Conclusion**: Mean ISF = 1.127 (median = 1.154, SD = 0.235, n=130 sections)
- **Discussion**: Mean ISF = 1.247 (median = 1.314, SD = 0.161, n=33 sections)
- **Other**: Mean ISF = 1.326 (median = 1.324, SD = 0.265, n=531 sections)

**Key Finding**: Methods (1.227) and Results (1.243) have *lower* mean ISF than Introduction (1.335). This directly contradicts the hypothesis that evidence sections contain more rare, section-specific terms. Instead, the data suggest that either: (1) Methods and Results use vocabulary that is common across sections (contrary to expectation), (2) the within-document scope is too narrow to reveal vocabulary differences (e.g., papers reuse method terminology), or (3) the mechanism operates at a finer granularity than section boundaries (e.g., within-sentence specificity matters more than within-section frequency).

[FIGURE:fig_isf_analysis]

## Retrieval Quality: Absolute Performance

All three methods achieved modest section recall (~0.48 mean). Only 46–53% of gold evidence sections appeared in the top-3 retrieved. This suggests that the core bottleneck is not the choice of ranking function but rather the retrieval space itself: dense embeddings may not capture the query-evidence section relationship well, or sections may be too coarse-grained to isolate specific evidence.

# Discussion

## Disconfirmation of the Hypothesis

The TF-ISF method was motivated by a clear intuition: vocabulary in scientific papers is stratified by section, with evidence-bearing sections using rare, section-specific terminology. Under this assumption, within-document term reweighting should rescue evidence sections from being outranked by claim-dense sections. However, the empirical data show that this stratification, if it exists, is either not strong enough to influence ranking or is orthogonal to the information in dense embeddings.

The ISF diagnostic is particularly revealing. If Methods and Results sections used more unique vocabulary, we would expect higher ISF scores (rarer terms). Instead, they have lower ISF—suggesting either that technical terminology is *shared* across multiple sections (e.g., hyperparameter names are discussed in both Methods and Results) or that the sections are not sufficiently different in vocabulary profile.

## Why All Methods Underperform

The fact that cosine similarity, BM25, and TF-ISF all achieve similar (low) retrieval recall (~0.48) indicates that the bottleneck is not ranking function selection, but something deeper:

1. **Dense Embedding Quality.** Sentence-transformers models are trained on general-domain data (web sentences, STS tasks). They may not capture domain-specific relationships between queries and evidence in scientific papers. A query like "What is the seed lexicon?" may not embed similarly to the specific methods section where seed lexicon is defined, because the embedding space conflates different senses of common terms.

2. **Section Granularity.** QASPER sections are subsections (e.g., "Experiments ::: Results and Discussion"). A gold evidence section might be very specific, while retrieved sections are broader siblings. Top-3 retrieval may miss the exact subsection.

3. **Query-Evidence Mismatch.** Queries are phrased in plain natural language ("What is...?"), while Methods and Results sections use dense technical exposition. Even with TF-ISF reweighting, the vocabulary gap may be too wide for token-level matching or shallow embedding models to bridge.

4. **Small Sample and Budget.** With n=200 and modest LLM capability, statistical power is limited. The LLM reader may also contribute noise: it could fail to extract answers from correct sections (reader error) or hallucinate answers from partial information (reader hallucination).

## Alternative Hypotheses and Future Directions

Our negative result suggests several avenues for future work:

- **Discourse-Aware Retrieval.** Rhetorical role tagging (identifying which sections contain claims vs. evidence) could explicitly bias retrieval toward evidence. This is more expensive than TF-ISF (requires an external classifier) but may be necessary.

- **Query-Specific Term Weighting.** Rather than static within-document ISF, learn a query-specific reweighting that reflects which terms are most informative for answering the query. This would require training data.

- **Hybrid Retrievers.** Combine dense and sparse signals (cosine + BM25) via learned aggregation or simple averaging. Preliminary results suggest cosine and BM25 disagree on many examples; ensemble might improve robustness.

- **Larger Models and Fine-tuning.** The LLM reader (3B parameters, free tier) is a potential bottleneck. Larger or task-specific readers might better exploit retrieved sections.

- **Cross-Document Structure.** Extend from within-document ISF to cross-document: a term is rare if it appears in few documents *and* few sections. This could help distinguish domain-specific terminology from paper-specific terminology.

## Limitations

1. **Sample Size**: n=200 is modest; confidence intervals are wide (≈ ±0.025 for F1). With larger n, some comparisons might become significant (though effect sizes are small).

2. **Single Reader Model**: We used a single small LLM. Different readers (or different prompts) might yield different relative rankings of methods.

3. **Single Dataset**: QASPER is NLP-focused. Results may not generalize to biomedical or physics papers, which have different vocabulary and section conventions.

4. **Retrieval Granularity**: QASPER sections are often long (hundreds of words). Finer-grained retrieval (sentences or paragraphs) might reveal the vocabulary gap that section-level retrieval obscures.

5. **Evaluation Metric**: Token-level F1 is coarse-grained; it does not distinguish retrieval success (did we get the right section?) from reader success (did the reader extract the answer?). Section-level recall isolates retrieval, but is a binary metric and may miss nuanced ranking improvements.

# Conclusion

We investigated the hypothesis that within-document Inverse Section Frequency (TF-ISF) could improve section retrieval in scientific papers by down-weighting document-theme vocabulary and up-weighting section-specific terms. Evaluation on 200 QASPER questions found no significant advantage of TF-ISF over cosine similarity or BM25 retrieval. Moreover, the hypothesized mechanism—lower term frequency in evidence sections—was not supported: Methods and Results sections had lower (not higher) ISF than Introduction sections.

This negative result provides a useful boundary condition: naive within-document term reweighting does not rescue dense retrieval in scientific QA. The core retrieval bottleneck lies elsewhere—likely in dense embedding quality, document granularity, or fundamental query-evidence vocabulary mismatch.

For practitioners building scientific QA systems, our findings suggest that simple term-weighting alone is insufficient and that more sophisticated approaches (discourse parsing, hybrid dense-sparse retrieval, or stronger embedding models) may be necessary to achieve high recall on evidence sections.

## Acknowledgments

We thank the QASPER authors for the public dataset and the OpenRouter team for free-tier LLM access that enabled this evaluation within a modest budget. All code and results are available in the project repository.

## References

[1] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Kuttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, and D. Kiela. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In Neural Information Processing Systems, 2020.

[2] K. Spärck Jones. A statistical interpretation of term specificity and its application in retrieval. Journal of Documentation, 28(1):11–21, 1972.

[3] P. Dasigi, K. Lo, I. Beltagy, A. Cohan, N. A. Smith, and M. Gardner. A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers. In North American Chapter of the Association for Computational Linguistics, 2021.

[4] V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Schwenk, A. Schwab, and J. Perez. Dense Passage Retrieval for Open-Domain Question Answering. In Empirical Methods in Natural Language Processing, 2020.

[5] O. Khattab and M. Potts. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. In International ACM SIGIR Conference on Research and Development in Information Retrieval, 2020.

[6] A. Cohan, S. Feldman, I. Beltagy, D. Downey, and D. S. Weld. SPECTER: Document-level Representation Learning using Citation-informed Transformers. In Findings of the Association for Computational Linguistics: ACL 2020, 2020.

[7] B. Z. Reichman and L. Heck. Dense Passage Retrieval: Is it Retrieving? In Findings of the Empirical Methods in Natural Language Processing, 2024.

[8] S. Robertson and H. Zaragoza. The Probabilistic Relevance Framework: BM25 and Beyond. Foundations and Trends in Information Retrieval, 3(4):333–389, 2009.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) Contradictory experiment result is not disclosed. The supplementary artifact art_E7rG9mK6gbrb contains a prior experiment run (method.py, n=180, LLM=tencent/hy3:free) whose summary explicitly states 'Hypothesis CONFIRMED: TF-ISF outperforms cosine on answer F1' with TF-ISF F1=0.221 vs Cosine F1=0.206. The paper reports only the evaluation run (art_r9whYzfM2OVO, n=200, LLM=llama-3.2-3b-instruct) which shows TF-ISF F1=0.187 vs Cosine F1=0.198 (DISCONFIRMED). These two runs used different LLMs, different data loading paths (local JSON vs HuggingFace), different evidence matching strategies, and slightly different n. Reporting only the negative run to frame a clean negative-result narrative — when an earlier positive run exists in the same artifact set — is a serious methodological integrity issue, regardless of which run is more trustworthy.
  Action: Add a dedicated section or appendix that presents both runs side by side, explains all differences in setup (LLM, n, data source, evidence matching, tokenization), argues which is more reliable and why, and acknowledges that the conclusion depends on this methodological choice. If the evaluation run (n=200) is preferred, explain why the experiment run (n=180) produced different results — likely the different LLM and evidence matching strategy.
- [MAJOR] (methodology) The BM25 baseline is described as corpus-level ('IDF computed over all 81,550 sections across 289 papers in the QASPER dataset') but eval.py instantiates BM25Okapi per-question using only the target paper's sections. This makes BM25 a within-document sparse ranker, the same locality constraint as TF-ISF. The claimed differentiator between BM25 and TF-ISF — corpus-level vs. document-local IDF — does not exist in the implementation. This undermines the comparison and the paper's conclusion that TF-ISF adds nothing over BM25.
  Action: Either (a) implement true corpus-level BM25 by building an index over all 81,550 sections before evaluation and querying it to retrieve from the target paper's sections, or (b) explicitly state that the BM25 baseline is also within-document (i.e., both methods compute IDF locally), and rewrite the comparison accordingly. Option (a) is preferable as it provides a more informative baseline.
- [MAJOR] (rigor) The ISF diagnostic — the mechanistic evidence that Methods/Results have lower ISF than Introduction, which drives the core disconfirmation explanation — is computed only on the subset of records where gold sections are Methods or Results (compute_isf_diagnostics filters: 'if not any(t in rec["gold_section_types"] for t in ["Methods", "Results"]): continue'). This subset is not disclosed in the paper, which presents the ISF values as if they describe all papers. Computing ISF means only on papers already filtered to have Methods/Results gold answers may introduce selection bias.
  Action: Re-run the ISF diagnostic on all 200 records (remove the gold-section-type filter). Report whether the ISF ordering (Introduction > Methods/Results) holds across all papers, not just the Methods/Results-gold subset. Disclose the filtering in the paper regardless.
- [MAJOR] (clarity) Reference [6] is factually wrong. The paper states 'Cohan et al. [6] explored hierarchical attention over paper sections, but did not isolate the effect of term frequency on ranking.' Reference [6] in the bibliography is 'SPECTER: Document-level Representation Learning using Citation-informed Transformers' — this paper is about learning document embeddings from citation signals, not hierarchical attention over sections. The described claim does not match the cited paper.
  Action: Replace reference [6] with the correct citation. For hierarchical attention over paper sections, the relevant work includes Cohan et al. 2018 'A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents' (NAACL 2018) or relevant section-aware scientific NLP work. Verify all other citations are correctly attributed.
- [MINOR] (methodology) The paper describes TF(t,s) as 'raw term frequency' but the code (both eval.py and method.py) uses length-normalized TF: tf[t] = count / len(section_tokens). This is a standard normalization but the formula and text description should match the implementation.
  Action: Update the formula and description to say 'length-normalized term frequency' and revise the TF-ISF formula to include the normalization explicitly: TF(t, s) = count(t, s) / |s|.
- [MINOR] (scope) The n=200 sample is drawn from the first 200 questions encountered in the QASPER train+validation split (in order), which may not be representative. QASPER has ~2,593 QA pairs; using only 200 (7.7%) risks sampling bias, especially since the code breaks at n_max without any stratification.
  Action: Sample 200 examples with stratification by paper and by gold-section type (ensure proportional representation of Methods/Results gold sections). Alternatively, run on the full validation split (~900 examples) to improve statistical power. Report which split was used and how examples were selected.
- [MINOR] (novelty) The TF-ISF method is a trivially obvious extension of TF-IDF. Within-document IDF has been considered in the literature (e.g., Singhal et al. 1996, Hiemstra 1998 language models, and various field-weighted retrieval schemes). The paper does not cite any prior work on within-document term weighting, which means the novelty claim rests on an incomplete literature review.
  Action: Search for prior work on within-document IDF, field-weighted retrieval (e.g., BM25F), and section-aware term weighting. Cite and differentiate from any relevant prior work. If within-document IDF has been studied before in other domains, the novelty claim must be scoped accordingly.
- [MINOR] (evidence) The subgroup sizes are very small: Abstract/Introduction n=31, Discussion/Conclusion n=12. With such small groups, the subgroup F1 comparisons have very wide confidence intervals and essentially no statistical power. Yet the paper reports these comparisons as if they are informative (e.g., 'TF-ISF significantly underperforms on this small group' for Discussion/Conclusion).
  Action: Add per-subgroup confidence intervals to the Results table. Remove claims of 'significant' underperformance for groups with n<20. Instead, describe these as 'directional observations with insufficient power to draw conclusions' and focus interpretation on the Methods/Results subgroup (n=137) which is adequately powered.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
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
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-20 11:40:51 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```
