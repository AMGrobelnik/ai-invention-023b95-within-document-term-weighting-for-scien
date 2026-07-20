# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 12:34:36 UTC

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

--- Item 4 ---
id: art_n8Uc3vygMnZU
type: research
title: 'Within-Document Term Weighting in Scientific Paper Retrieval: Prior Work Survey'
summary: |-
  This research surveys the prior work landscape for TF-ISF (Term Frequency-Inverse Section Frequency), a within-document reweighting approach for scientific paper retrieval. The investigation covered six major research phases: (1) foundational IDF theory and within-document variants, (2) field-weighted retrieval (BM25F), (3) modern section-aware systems (IntrAgent, SCITREERAG, SF-RAG, Disco-RAG), (4) vocabulary stratification in IMRaD scientific papers, (5) query-evidence vocabulary mismatch in scientific QA, and (6) comparative analysis positioning TF-ISF within the landscape.

  Key findings:

  **Novelty:** TF-ISF represents a novel direct application of inverse frequency weighting at the section level. While BM25F (2004) provides precedent for field-weighted retrieval in structured documents, BM25F operates on flat field structures and typically uses global IDF rather than per-field ISF. No prior work explicitly proposes section-frequency-based reweighting for scientific papers [1-5].

  **Modern Alternatives:** Contemporary section-aware systems have diverged from static term reweighting toward three approaches: (1) hierarchical structural indexing with path-guided retrieval (SF-RAG, SCITREERAG), (2) discourse-aware generation with rhetorical graphs (Disco-RAG), and (3) LLM-guided iterative section ranking (IntrAgent, SemRank). IntrAgent achieves 13.2% higher accuracy than RAG baselines through structural knowledge-enabled reasoning [6], suggesting the bottleneck is not ranking function design but iterative refinement and reasoning.

  **Vocabulary Stratification:** The assumption that Methods/Results sections use unique vocabulary lacks empirical validation. QASPER data [7] shows answer distribution is uniform across sections (no majority-holding section), contradicting the premise. Embedding quality studies show methods-only embeddings underperform abstract embeddings [8], further invalidating the stratification hypothesis. Vocabulary stratification is theoretically motivated but empirically unvalidated [9, 10].

  **Retrieval Bottleneck Analysis:** QASPER shows models underperform humans by ≥27 F1 points [7], indicating reading comprehension (not ranking) is the primary bottleneck. TF-ISF's null result (F1=0.187, p>0.37, d<0.10) aligns with evidence that: (1) section-level granularity is too coarse (proposition-level retrieval outperforms it [11, 12]), (2) embedding domain gap is marginal (fine-tuning yields only 1–5% improvements [13]), and (3) discourse structure matters more than term weights (Disco-RAG achieves SOTA without fine-tuning [14]).

  **Vocabulary Mismatch Solutions:** Standard approaches to the 30–80% historical vocabulary mismatch problem [15, 16] include query expansion, probabilistic language models, dense embeddings, domain fine-tuning, and HyDE (hypothetical document generation). Notably, static within-document term reweighting is not proposed as a solution in the prior work literature [15, 16, 17], suggesting the community converged on embedding-based or generation-based approaches as more effective.

  **Future Directions:** Rather than additional term-weighting variants, the field should pursue: (1) discourse-aware retrieval (Disco-RAG's rhetorical structure), (2) fine-grained retrieval units (paragraph/proposition-level), (3) fine-tuned embeddings with ontological supervision, and (4) iterative LLM-guided ranking. These directly address the identified bottlenecks (reading comprehension, granularity, embedding quality) rather than optimizing for ranking, which appears to be the least-important bottleneck.

  **Quantified Context:** QASPER contains 1,585 papers and 5,049 questions [7]. Answer types: 4,142 extractive, 1,931 abstractive, 1,110 yes/no, 810 unanswerable [7]. Human-model F1 gap: ≥27 points [7]. Fine-tuning gains on scientific tasks: 1–5% [13]. IntrAgent improvement: 13.2% over baselines [6]. Vocabulary mismatch affects 30–80% of queries historically [15, 16].
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 5 ---
id: art_6XiK_3KhqRM0
type: evaluation
in_dependencies:
- id: art_E7rG9mK6gbrb
  label: earlier experiment
- id: art_HHk7NUDMfOf5
  label: dataset context
title: TF-ISF vs BM25 vs Cosine Retrieval Evaluation
summary: |-
  Comprehensive evaluation of the iter_1 experiment results (n=180, tencent/hy3:free LLM, QASPER scientific QA dataset). All three retrieval methods — TF-ISF (F1=0.221), BM25 (F1=0.213), Cosine (F1=0.206) — were evaluated with:

  1. **Pairwise F1 bootstrap CIs**: TF-ISF vs Cosine diff=+0.015 95%CI=[-0.018,+0.047]; TF-ISF vs BM25 diff=+0.007; BM25 vs Cosine diff=+0.008. All Holm-Bonferroni corrected p-values = 1.0 (not significant).

  2. **Effect sizes**: Hedges' g = 0.097 (TF-ISF vs Cosine), 0.047 (TF-ISF vs BM25), 0.050 (BM25 vs Cosine) — all negligible (<0.2).

  3. **Per-example F1 statistics**: High variance (std≈0.155 for all methods), consistent with LLM-quality bottleneck.

  4. **Subgroup analysis by section type**: TF-ISF best on Result (0.197) and Unknown (0.226); BM25 best on Method (0.270); Cosine best on Related (0.269). No subgroup differences reach significance.

  5. **Hallucination rate**: cosine=62.2%, bm25=70.0%, tf_isf=71.7% — the LLM generates F1>0 answers with zero retrieval recall in 62-72% of cases, indicating widespread confabulation.

  6. **Kruskal-Wallis variance decomposition**: H=0.753, p=0.686, eta²≈0 — method choice explains essentially zero variance in F1.

  7. **Reliability assessment**: LOW — no significant differences after multiple-comparison correction, negligible effect sizes, wide CIs (≈0.045 width), and 68% average hallucination rate from free-tier LLM. The earlier claim of 'TF-ISF CONFIRMED' is not supported by rigorous statistics.

  8. **Root cause**: The dominant source of F1 variance is LLM quality (confabulation), not retrieval method. Upgrading the reader LLM is the highest-leverage intervention.

  Note: The artifact plan references a second experiment (n=200) for comparison, but only iter_1 (n=180) exists with results.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 2 artifacts were created THIS iteration.

id: art_n8Uc3vygMnZU
type: research
title: 'Within-Document Term Weighting in Scientific Paper Retrieval: Prior Work Survey'
summary: |-
  This research surveys the prior work landscape for TF-ISF (Term Frequency-Inverse Section Frequency), a within-document reweighting approach for scientific paper retrieval. The investigation covered six major research phases: (1) foundational IDF theory and within-document variants, (2) field-weighted retrieval (BM25F), (3) modern section-aware systems (IntrAgent, SCITREERAG, SF-RAG, Disco-RAG), (4) vocabulary stratification in IMRaD scientific papers, (5) query-evidence vocabulary mismatch in scientific QA, and (6) comparative analysis positioning TF-ISF within the landscape.

  Key findings:

  **Novelty:** TF-ISF represents a novel direct application of inverse frequency weighting at the section level. While BM25F (2004) provides precedent for field-weighted retrieval in structured documents, BM25F operates on flat field structures and typically uses global IDF rather than per-field ISF. No prior work explicitly proposes section-frequency-based reweighting for scientific papers [1-5].

  **Modern Alternatives:** Contemporary section-aware systems have diverged from static term reweighting toward three approaches: (1) hierarchical structural indexing with path-guided retrieval (SF-RAG, SCITREERAG), (2) discourse-aware generation with rhetorical graphs (Disco-RAG), and (3) LLM-guided iterative section ranking (IntrAgent, SemRank). IntrAgent achieves 13.2% higher accuracy than RAG baselines through structural knowledge-enabled reasoning [6], suggesting the bottleneck is not ranking function design but iterative refinement and reasoning.

  **Vocabulary Stratification:** The assumption that Methods/Results sections use unique vocabulary lacks empirical validation. QASPER data [7] shows answer distribution is uniform across sections (no majority-holding section), contradicting the premise. Embedding quality studies show methods-only embeddings underperform abstract embeddings [8], further invalidating the stratification hypothesis. Vocabulary stratification is theoretically motivated but empirically unvalidated [9, 10].

  **Retrieval Bottleneck Analysis:** QASPER shows models underperform humans by ≥27 F1 points [7], indicating reading comprehension (not ranking) is the primary bottleneck. TF-ISF's null result (F1=0.187, p>0.37, d<0.10) aligns with evidence that: (1) section-level granularity is too coarse (proposition-level retrieval outperforms it [11, 12]), (2) embedding domain gap is marginal (fine-tuning yields only 1–5% improvements [13]), and (3) discourse structure matters more than term weights (Disco-RAG achieves SOTA without fine-tuning [14]).

  **Vocabulary Mismatch Solutions:** Standard approaches to the 30–80% historical vocabulary mismatch problem [15, 16] include query expansion, probabilistic language models, dense embeddings, domain fine-tuning, and HyDE (hypothetical document generation). Notably, static within-document term reweighting is not proposed as a solution in the prior work literature [15, 16, 17], suggesting the community converged on embedding-based or generation-based approaches as more effective.

  **Future Directions:** Rather than additional term-weighting variants, the field should pursue: (1) discourse-aware retrieval (Disco-RAG's rhetorical structure), (2) fine-grained retrieval units (paragraph/proposition-level), (3) fine-tuned embeddings with ontological supervision, and (4) iterative LLM-guided ranking. These directly address the identified bottlenecks (reading comprehension, granularity, embedding quality) rather than optimizing for ranking, which appears to be the least-important bottleneck.

  **Quantified Context:** QASPER contains 1,585 papers and 5,049 questions [7]. Answer types: 4,142 extractive, 1,931 abstractive, 1,110 yes/no, 810 unanswerable [7]. Human-model F1 gap: ≥27 points [7]. Fine-tuning gains on scientific tasks: 1–5% [13]. IntrAgent improvement: 13.2% over baselines [6]. Vocabulary mismatch affects 30–80% of queries historically [15, 16].
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

id: art_6XiK_3KhqRM0
type: evaluation
in_dependencies:
- id: art_E7rG9mK6gbrb
  label: earlier experiment
- id: art_HHk7NUDMfOf5
  label: dataset context
title: TF-ISF vs BM25 vs Cosine Retrieval Evaluation
summary: |-
  Comprehensive evaluation of the iter_1 experiment results (n=180, tencent/hy3:free LLM, QASPER scientific QA dataset). All three retrieval methods — TF-ISF (F1=0.221), BM25 (F1=0.213), Cosine (F1=0.206) — were evaluated with:

  1. **Pairwise F1 bootstrap CIs**: TF-ISF vs Cosine diff=+0.015 95%CI=[-0.018,+0.047]; TF-ISF vs BM25 diff=+0.007; BM25 vs Cosine diff=+0.008. All Holm-Bonferroni corrected p-values = 1.0 (not significant).

  2. **Effect sizes**: Hedges' g = 0.097 (TF-ISF vs Cosine), 0.047 (TF-ISF vs BM25), 0.050 (BM25 vs Cosine) — all negligible (<0.2).

  3. **Per-example F1 statistics**: High variance (std≈0.155 for all methods), consistent with LLM-quality bottleneck.

  4. **Subgroup analysis by section type**: TF-ISF best on Result (0.197) and Unknown (0.226); BM25 best on Method (0.270); Cosine best on Related (0.269). No subgroup differences reach significance.

  5. **Hallucination rate**: cosine=62.2%, bm25=70.0%, tf_isf=71.7% — the LLM generates F1>0 answers with zero retrieval recall in 62-72% of cases, indicating widespread confabulation.

  6. **Kruskal-Wallis variance decomposition**: H=0.753, p=0.686, eta²≈0 — method choice explains essentially zero variance in F1.

  7. **Reliability assessment**: LOW — no significant differences after multiple-comparison correction, negligible effect sizes, wide CIs (≈0.045 width), and 68% average hallucination rate from free-tier LLM. The earlier claim of 'TF-ISF CONFIRMED' is not supported by rigorous statistics.

  8. **Root cause**: The dominant source of F1 variance is LLM quality (confabulation), not retrieval method. Upgrading the reader LLM is the highest-leverage intervention.

  Note: The artifact plan references a second experiment (n=200) for comparison, but only iter_1 (n=180) exists with results.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Scientific question answering over long research papers is a critical task for automated literature review, clinical evidence synthesis, and research acceleration. Despite advances in dense retrieval methods and large language models, a systematic failure mode remains poorly understood: when a reader queries a paper for specific evidence, standard dense retrievers often return sections that are high in rhetorical clarity (Abstract, Introduction, Conclusion) while ranking evidence-bearing sections (Methods, Results) lower. This is not random error—it reflects a structural property of scientific writing itself. The IMRaD (Introduction, Methods, Results, and Discussion) convention, by design, separates claims and their accessible restatement in early and concluding sections from the detailed, specialized evidence in Methods and Results.

The problem is acute in modern retrieval-augmented generation (RAG) systems. Dense passage retrievers like DPR [1] score text similarity using neural embeddings trained on general-domain data (web text, semantic similarity tasks). These embeddings excel at semantic matching but may be biased toward sections that paraphrase the paper's topic in accessible language—precisely what Abstract and Introduction are designed to do. Meanwhile, the technical vocabulary, specific parameter values, and precise experimental conditions in Methods and Results are sparse, section-unique, and may not score highly under cosine similarity with natural-language queries [2].

We hypothesize that this bias reflects a classical vocabulary problem in information retrieval: the vocabulary gap between query and document, which term-weighting methods like TF-IDF have long addressed by down-weighting high-frequency (document-theme) terms and up-weighting rare (discriminative) terms [3]. Applying this principle within a single document—replacing cross-corpus IDF with within-document Inverse Section Frequency (ISF)—could correct the retrieval bias. The intuition is straightforward: if a term appears in nearly every section of a paper, it provides little discriminative signal for ranking sections; if a term appears in only one or two sections, it strongly indicates those sections. A training-free, self-contained scoring function requires no external discourse models, citation graphs, or LLM inference at retrieval time.

We conducted a controlled evaluation on 200 examples from QASPER [4], a benchmark of information-seeking questions over NLP papers. Three retrieval methods were compared: (1) cosine similarity with sentence-transformers embeddings, (2) BM25 with within-document term weighting, and (3) TF-ISF using within-document section frequency. For each method, the top-3 sections were retrieved and fed to a small LLM reader to generate answers, scored against gold answers using token-level F1 [5].

**Key findings:** TF-ISF achieved F1=0.187, performing no better than cosine (F1=0.198) or BM25 (F1=0.179). All pairwise differences were non-significant (p > 0.37, Holm-corrected). Critically, the postulated mechanism is inverted: Methods and Results sections had lower mean ISF (1.23–1.24) than Introduction sections (1.34), falsifying the hypothesis that evidence sections use more section-unique vocabulary. All three methods achieved modest section recall (~0.48), indicating that the bottleneck is not ranking function choice but likely dense embedding quality, document granularity, or fundamental query-evidence vocabulary mismatch.

We also report a contradictory earlier experiment (n=180 questions, free-tier LLM: tencent/hy3) showing TF-ISF F1=0.221 (positive result, outperforming cosine F1=0.206). This discrepancy motivates a detailed comparison of the two runs, examining differences in LLM model, data loading, evidence matching, and tokenization. We argue that the larger, more rigorous n=200 evaluation (llama-3.2-3b-instruct, paired statistics, higher LLM quality) is more trustworthy, but the contradiction highlights a critical methodological vulnerability: within-document term statistics are fragile proxies for ranking when downstream LLM quality dominates variance.

[FIGURE:fig_method_overview]

This paper contributes a well-characterized negative result: naive within-document term reweighting does not rescue section retrieval in scientific QA, and the assumed vocabulary stratification between IMRaD sections is not supported empirically. We discuss likely true bottlenecks (dense embedding quality for scientific text, section granularity, query-evidence vocabulary mismatch) and point toward future directions in scientific document understanding (discourse parsing, fine-tuned embeddings, iterative LLM-based ranking).

# Related Work

**Term Weighting and IDF Variants.** The principle of inverse document frequency was introduced by Spärck Jones [3], establishing that high-frequency terms in a corpus are poor discriminators while rare terms are informative. This foundation has inspired decades of variants: BM25 [6], probabilistic language models [7], and field-weighted extensions like BM25F [8], which extends IDF to structured documents with multiple typed fields. BM25F computes per-field term weights and combines them, though it typically uses global (corpus-level) IDF rather than field-local IDF. Within-document IDF has been explored in language modeling contexts (e.g., Hiemstra's work on document priors) but has not been systematically applied to the section-ranking problem in scientific QA.

**Dense Retrieval for Question Answering.** Dense passage retrieval (DPR) [1] and related methods like ColBERT [9] have become standard for open-domain QA by learning dual encoders for queries and documents. These methods have been extended to long documents through hierarchical retrieval (e.g., retrieving paragraphs before sentences). However, most work focuses on short passages or web documents where vocabulary structure is less stratified than in scientific papers. Recent critiques [10] argue that dense embeddings can be brittle and fail to capture fine-grained term relevance, especially in domain-specific settings.

**Scientific Document Understanding.** QASPER [4] is the first large-scale QA dataset anchored to full research papers, measuring the difficulty of complex reasoning across paper sections. Section classification and rhetorical role labeling have been explored (e.g., [11]), but less work has isolated the effect of term frequency on within-document section ranking for evidence retrieval. Cohan et al. [12] developed hierarchical document-level representations using citation-aware transformers (SPECTER), but this focused on document-level embeddings rather than intra-document section ranking. More recent work on discourse-aware retrieval (e.g., Disco-RAG [13]) constructs rhetorical graphs but requires an external discourse parser.

**Vocabulary Mismatch in QA.** The vocabulary gap between queries and documents has been a longstanding problem in IR [14], typically addressed through query expansion [15], dense embeddings [1], or hypothetical document generation (HyDE) [16]. However, static within-document term reweighting is notably absent from standard vocabulary-mismatch solutions in the literature, suggesting the community has largely converged on embedding-based or generation-based approaches as more effective.

# Methods

## Dataset and Task Setup

We used QASPER [4], a dataset of 5,049 information-seeking questions over 1,585 NLP research papers. Our sample consisted of 200 examples drawn sequentially from the training and validation splits. Each example contains: (1) a natural-language question posed by an NLP practitioner after reading only the paper's title and abstract, (2) a full research paper parsed into typed sections (Abstract, Introduction, Methods, Results, Discussion, Conclusion, Other), (3) gold evidence section names identifying which sections contain the answer, and (4) a gold answer string. The 200 questions span 150+ unique papers.

**Sampling note:** Examples were selected in order without stratification, representing 7.7% of the full QASPER validation split. While stratified sampling would be preferable, the sequential selection was practical for budget-constrained evaluation. Subgroup sizes range from n=12 (Discussion/Conclusion) to n=137 (Methods/Results), limiting power for small groups.

## Retrieval Methods

**Method 1: Cosine Similarity (Dense Embedding).** For each question-section pair, we encoded the question and section text (truncated to 512 characters) using all-MiniLM-L6-v2, a lightweight sentence-transformers model [17]. Cosine similarity between L2-normalized embeddings was computed, and the top-3 sections were ranked by score.

**Method 2: BM25 (Within-Document Sparse Ranking).** We implemented BM25Okapi [6] using the rank_bm25 library. Crucially, BM25 was instantiated per question using only the sections of the target paper, not corpus-level IDF. This means BM25 operates under the same within-document locality constraint as TF-ISF, differing only in how term weights are computed (probabilistic term frequency model vs. simple linear TF). The reviewer correctly identified this [18], and we clarify here that both BM25 and TF-ISF are within-document methods; they differ in their term-weighting functions, not in their scope.

**Method 3: TF-ISF (Within-Document Inverse Section Frequency).** For each section within a target paper, we computed a TF-ISF score as:

$$\text{TF-ISF}(q, s) = \sum_{t \in q} \text{TF}(t, s) \times \log\left(\frac{N_\text{sections}}{1 + \text{SF}(t)}\right)$$

where $q$ is the query, $s$ is the section, $\text{TF}(t, s) = \frac{\text{count}(t, s)}{|s|}$ is the length-normalized term frequency (count of term $t$ in section $s$ divided by the total number of tokens in $s$), $N_\text{sections}$ is the total number of sections in the paper, and $\text{SF}(t)$ is the number of sections containing term $t$ (section frequency, computed as binary presence, not raw count). The within-document ISF score is $\log(N_\text{sections} / (1 + \text{SF}(t)))$, analogous to corpus-level IDF but scoped to a single document.

Terms were lowercased and English stopwords were removed using a standard list. The resulting TF-ISF score reflects the intuition that terms appearing in most sections (high SF, low ISF) are document-theme terms and provide little discriminative signal; terms appearing in few sections (low SF, high ISF) are section-specific and strongly indicate those sections.

## Answer Generation and Evaluation

For each question, the top-3 retrieved sections were concatenated and fed with the original question to a small LLM reader for answer generation. We used meta-llama/llama-3.2-3b-instruct via OpenRouter, a freely available model selected for cost efficiency within a \$10 budget.

Answers were evaluated using token-level F1 against gold answers (QASPER's standard metric), computed as the harmonic mean of precision and recall of token overlaps after lowercasing and punctuation removal. We also computed section-level recall: the fraction of gold evidence sections appearing in the top-3 retrieved by each method. This diagnostic metric isolates retrieval quality from LLM answer quality.

## Statistical Analysis

We conducted paired t-tests with Holm-Bonferroni correction for multiple comparisons. Cohen's d was computed to estimate effect size. Bootstrap confidence intervals (95%, 10,000 resamples) were computed for mean F1 and recall per method. All comparisons are two-tailed. For subgroups with n < 20, we report confidence intervals but avoid claims of statistical significance due to insufficient power.

# Results

## Primary Evaluation (n=200, llama-3.2-3b-instruct)

[FIGURE:fig_main_results]

On 200 questions, the three methods achieved the following token F1 scores and section recall@3:

- **Cosine Similarity**: F1 = 0.198 (95% CI: [0.174, 0.223]), Recall@3 = 0.467 (95% CI: [0.403, 0.531])
- **BM25**: F1 = 0.179 (95% CI: [0.157, 0.202]), Recall@3 = 0.525 (95% CI: [0.462, 0.589])
- **TF-ISF**: F1 = 0.187 (95% CI: [0.163, 0.213]), Recall@3 = 0.484 (95% CI: [0.418, 0.548])

None of the pairwise differences reached statistical significance after Holm-Bonferroni correction:
- TF-ISF vs. Cosine: Δ = −0.011 (p = 0.419, d = −0.060, not significant)
- TF-ISF vs. BM25: Δ = +0.008 (p = 0.373, d = +0.045, not significant)
- Cosine vs. BM25: Δ = +0.018 (p = 0.153, d = +0.053, not significant)

All 95% confidence intervals overlap substantially, and all effect sizes are negligible (|d| < 0.1).

## Subgroup Analysis by Section Type

We stratified results by the type of gold evidence section to test whether TF-ISF specifically rescues questions whose answers are in Methods or Results sections [19].

[FIGURE:fig_subgroup_analysis]

**Abstract/Introduction (n=31):** Cosine F1=0.192 CI[0.136,0.253], TF-ISF F1=0.158 CI[0.111,0.209], BM25 F1=0.170 CI[0.118,0.228]. TF-ISF underperforms cosine.

**Methods/Results (n=137, adequately powered):** Cosine F1=0.208 CI[0.178,0.239], TF-ISF F1=0.201 CI[0.171,0.233], BM25 F1=0.185 CI[0.157,0.214]. TF-ISF is marginally closer to cosine but does not exceed it. Recall: TF-ISF 0.493 vs. Cosine 0.490 (negligible difference).

**Discussion/Conclusion (n=12):** Cosine F1=0.192 CI[0.116,0.279], TF-ISF F1=0.134 CI[0.081,0.190], BM25 F1=0.156 CI[0.102,0.211]. TF-ISF underperforms on this small group. Given n=12, we interpret this as directional observation without sufficient power to draw strong conclusions.

**Other (n=53):** Cosine F1=0.193 CI[0.152,0.235], TF-ISF F1=0.172 CI[0.132,0.218], BM25 F1=0.181 CI[0.140,0.228]. No advantage for TF-ISF.

Across all subgroups, TF-ISF never significantly outperforms the baselines, and the intended mechanism—boosting Methods/Results retrieval—is not observed.

## Mechanism Diagnostic: ISF by Section Type

To diagnose why TF-ISF underperformed, we computed mean ISF scores for all terms in each section type across the corpus [ARTIFACT:art_r9whYzfM2OVO]. A critical caveat: the ISF diagnostic was computed on records where the gold evidence section was Methods or Results (139 records), not all 200 records, which may introduce selection bias. We report this filtering transparently.

[FIGURE:fig_isf_analysis]

**Mean ISF by Section Type:**
- **Introduction**: Mean ISF = 1.335 (median = 1.415, SD = 0.275, n=149 section instances)
- **Methods**: Mean ISF = 1.227 (median = 1.237, SD = 0.224, n=839 section instances)
- **Results**: Mean ISF = 1.243 (median = 1.234, SD = 0.208, n=161 section instances)
- **Related Work**: Mean ISF = 1.327 (median = 1.361, SD = 0.260, n=147 section instances)
- **Conclusion**: Mean ISF = 1.127 (median = 1.154, SD = 0.235, n=130 section instances)
- **Discussion**: Mean ISF = 1.247 (median = 1.314, SD = 0.161, n=33 section instances)
- **Other**: Mean ISF = 1.326 (median = 1.324, SD = 0.265, n=531 section instances)

**Key Finding:** Methods (1.227) and Results (1.243) have *lower* mean ISF than Introduction (1.335), directly contradicting the hypothesis that evidence sections contain more rare, section-specific terms. Instead, the data suggest that either: (1) Methods and Results use vocabulary that is common across sections (technical terms like "model," "dataset," "experiment" appear in multiple sections), (2) the within-document scope is too narrow to reveal meaningful vocabulary differences, or (3) the mechanism operates at a finer granularity than section boundaries.

## Contradictory Earlier Experiment: n=180, tencent/hy3:free LLM

[FIGURE:fig_contradiction_summary]

An earlier experiment on 180 QASPER examples using the free-tier tencent/hy3 model reported different results [ARTIFACT:art_E7rG9mK6gbrb]:

**Earlier Run (n=180, tencent/hy3:free):**
- TF-ISF F1 = 0.221 (best)
- BM25 F1 = 0.213
- Cosine F1 = 0.206
- **Conclusion:** TF-ISF outperforms cosine by +0.015 F1, hypothesis CONFIRMED

**Current Run (n=200, llama-3.2-3b-instruct):**
- TF-ISF F1 = 0.187 (worst)
- Cosine F1 = 0.198
- BM25 F1 = 0.179
- **Conclusion:** TF-ISF underperforms cosine, hypothesis DISCONFIRMED

This contradiction is a serious methodological issue and requires transparent explanation. Key differences between the two runs:

| Aspect | Earlier Run (Experiment) | Current Run (Evaluation) |
|--------|-----------|-------|
| **Sample size** | n=180 | n=200 |
| **LLM model** | tencent/hy3:free | llama-3.2-3b-instruct |
| **LLM cost** | $0 (free) | $0.014 (paid) |
| **Data loading** | Local raw JSON files | HuggingFace dataset API |
| **Tokenization** | Manual stopword list | Simple regex, manual stopwords |
| **Evidence matching** | Fuzzy section name matching | Paragraph-to-section mapping |
| **Retrieval granularity** | Section names | Full section text + metadata |

**Analysis of the Discrepancy:** The most likely explanations are: (1) **LLM quality dominates:** The tencent/hy3 model may confabulate answers more frequently, inflating F1 variance and making small ranking differences appear large. The current run's higher-quality LLM (llama-3.2-3b-instruct) may more accurately reflect answer generation quality, revealing that retrieval method differences are negligible. (2) **Data loading artifacts:** The earlier run loaded local JSON files with potentially different section parsing or evidence matching logic than the HuggingFace dataset, leading to systematic differences in which sections are considered "gold." (3) **Sample composition:** n=180 vs n=200 introduces different question distributions.

We argue that the **current evaluation run (n=200, llama-3.2-3b-instruct) is more trustworthy** because it: (i) uses a larger sample for better statistical power, (ii) employs a higher-quality LLM for more reliable answer generation, (iii) implements rigorous statistical testing with multiple-comparison correction, and (iv) applies more transparent evidence matching. However, this discrepancy demonstrates a critical vulnerability: ISF is a fragile proxy for ranking when downstream LLM quality is the dominant source of F1 variance. We recommend the current evaluation as the primary result but acknowledge the contradiction as a limitation.

## Retrieval Quality: Absolute Performance

All three methods achieved modest section recall (~0.48 mean). Only 46–53% of gold evidence sections appeared in the top-3 retrieved. This suggests that the core bottleneck is not the choice of ranking function but rather: (1) the retrieval space itself (dense embeddings may not capture query-evidence section relationships well for scientific text), (2) section granularity (QASPER sections are often hundreds of words, and gold evidence may be concentrated in a small subsection), or (3) fundamental vocabulary mismatch that neither sparse nor dense local reweighting resolves.

# Discussion

## Disconfirmation of the Hypothesis

The TF-ISF method was motivated by a clear intuition: vocabulary in scientific papers is stratified by section, with evidence-bearing sections using rare, section-specific terminology. Under this assumption, within-document term reweighting should rescue evidence sections from being outranked by claim-dense sections. However, the empirical data show that this stratification, if it exists, is either not strong enough to influence ranking or is orthogonal to the information density of dense embeddings.

The ISF diagnostic is particularly revealing. If Methods and Results sections used more unique vocabulary, we would expect higher ISF scores (rarer terms). Instead, they have lower ISF—suggesting that technical terminology is *shared* across multiple sections (e.g., hyperparameter names appear in both Methods and Results) or that the sections are not sufficiently differentiated in vocabulary profile. This falsifies the core assumption underlying TF-ISF.

## Why All Methods Underperform

The fact that cosine similarity, BM25, and TF-ISF all achieve similar (low) retrieval recall (~0.48) indicates that the bottleneck is not ranking function selection but something deeper:

1. **Dense Embedding Quality for Scientific Domain.** Sentence-transformers models are trained on general-domain data (web text, semantic textual similarity benchmarks). They may not capture domain-specific relationships between queries and evidence in scientific papers. A query like "What is the seed lexicon?" may not embed similarly to the Methods section where the seed lexicon is defined, because the embedding space conflates different senses of common terms [2].

2. **Section Granularity.** QASPER sections are subsections (e.g., "Experiments ::: Results and Discussion"). A gold evidence section might be very specific, while retrieved sections are broader siblings. Top-3 retrieval may miss the exact subsection.

3. **Query-Evidence Vocabulary Mismatch.** Queries are phrased in plain natural language ("What is...?"), while Methods and Results sections use dense technical exposition. Even with TF-ISF reweighting, the vocabulary gap may be too wide for token-level matching or shallow embedding models to bridge.

4. **Small Sample and LLM Bottleneck.** With n=200 and a modest LLM reader (3B parameters, free tier in some models), statistical power is limited. More critically, the LLM itself appears to be a dominant bottleneck: 62–72% of predictions in prior experiments had F1 > 0 despite zero retrieval recall (pure hallucination), indicating that the LLM reader dominates F1 variance over retrieval quality.

## Implications for Term-Weighting Approaches

Our findings suggest that while term-weighting strategies (TF-IDF, BM25) remain effective for keyword search and sparse retrieval, their naive within-document application does not rescue dense retrieval in scientific QA. The challenge may lie in the fundamental assumption: that term frequency is the right statistic to optimize for ranking. In scientific papers, what matters may not be how often a term appears in a section, but whether the section contains the specific *claim* or *finding* the query seeks—a semantic and structural property that term statistics cannot capture.

Recent work on discourse-aware retrieval (e.g., Disco-RAG [13]) suggests that rhetorical structure (identifying which sections contain claims vs. evidence vs. methodology) may be more informative than term frequency. However, such approaches require external discourse parsers and lose the training-free simplicity of TF-ISF.

## Limitations

1. **Sample Size:** n=200 is modest; confidence intervals are wide (≈ ±0.025 for F1). Larger n would improve power but was constrained by LLM budget.

2. **Single Reader LLM:** We used one small model. Different readers (or different prompts) might yield different relative rankings.

3. **Single Dataset:** QASPER is NLP-focused. Results may not generalize to biomedical or physics papers with different vocabulary and section conventions.

4. **Retrieval Granularity:** QASPER sections are coarse (hundreds of words). Finer-grained retrieval (sentences or propositions) might reveal vocabulary gaps that section-level retrieval obscures.

5. **ISF Diagnostic Filtering:** The ISF diagnostic was computed only on records where gold sections are Methods/Results (139 records), not all 200, potentially introducing selection bias. A full diagnostic across all records would be more conclusive.

6. **Contradictory Earlier Experiment:** The n=180 experiment with tencent/hy3 reported positive results. While we argue the n=200 evaluation is more reliable, this contradiction remains a limitation and highlights fragility in the approach.

# Conclusion

We investigated the hypothesis that within-document Inverse Section Frequency (TF-ISF) could improve section retrieval in scientific papers by down-weighting document-theme vocabulary and up-weighting section-specific terms. Evaluation on 200 QASPER questions found no significant advantage of TF-ISF over cosine similarity or BM25 retrieval (all p > 0.37, Holm-corrected). Moreover, the hypothesized mechanism—lower term frequency in evidence sections—was not supported: Methods and Results sections had lower (not higher) ISF than Introduction sections, falsifying the core assumption.

We also transparently report a contradictory earlier experiment (n=180, different LLM) showing TF-ISF F1=0.221 (positive result). We argue the n=200 evaluation is more trustworthy based on sample size, LLM quality, and statistical rigor, but the discrepancy demonstrates a critical vulnerability: ISF is fragile when LLM quality dominates variance.

For practitioners building scientific QA systems, our findings suggest that simple term-weighting alone is insufficient to rescue dense retrieval. The core retrieval bottleneck lies elsewhere—likely in dense embedding quality for scientific text, document granularity, or fundamental query-evidence vocabulary mismatch. More sophisticated approaches (discourse-aware parsing, fine-tuned embeddings, iterative LLM-based ranking) are necessary to achieve high recall on evidence sections.

This negative result contributes a rigorous, well-characterized boundary condition: within-document term reweighting does not fix section retrieval in scientific QA, and the assumed vocabulary stratification between IMRaD sections is not empirically supported at the section-frequency level in NLP papers. Future work should investigate whether vocabulary stratification exists at finer granularity (paragraph or sentence level) or whether the bottleneck is fundamentally orthogonal to term statistics.

# Acknowledgments

We thank the QASPER authors for the public dataset and the OpenRouter team for free-tier and paid-tier LLM access. All code and results are available in the project repository.

# References

[1] V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Schwenk, A. Schwab, and J. Perez. Dense Passage Retrieval for Open-Domain Question Answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2020.

[2] B. Z. Reichman and L. Heck. Dense Passage Retrieval: Is it Retrieving? In Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2024.

[3] K. Spärck Jones. A statistical interpretation of term specificity and its application in retrieval. Journal of Documentation, 28(1):11–21, 1972.

[4] P. Dasigi, K. Lo, I. Beltagy, A. Cohan, N. A. Smith, and M. Gardner. A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), pages 2335–2345, 2021.

[5] R. Rajpurkar, R. Jia, and P. Liang. Know What You Don't Know: Unanswerable Questions for SQuAD. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL), pages 784–789, 2018.

[6] S. Robertson and H. Zaragoza. The Probabilistic Relevance Framework: BM25 and Beyond. Foundations and Trends in Information Retrieval, 3(4):333–389, 2009.

[7] D. Hiemstra. Using Language Models for Information Retrieval. PhD thesis, University of Twente, 2000.

[8] S. Robertson, H. Zaragoza, and M. Taylor. Simple BM25 Extension to Multiple Weighted Fields. In Proceedings of the 13th ACM International Conference on Information and Knowledge Management (CIKM), 2004.

[9] O. Khattab and M. Potts. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR), pages 1713–1716, 2020.

[10] N. Thawani, R. Weller, and D. Weiss. What do Models Learn from Question Answering Datasets? In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 2780–2795, 2021.

[11] A. Cohan and N. A. Smith. Discourse Structure and Coherence of Scientific Documents. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL), pages 2181–2190, 2019.

[12] A. Cohan, S. Feldman, I. Beltagy, D. Downey, and D. S. Weld. SPECTER: Document-level Representation Learning using Citation-informed Transformers. In Findings of the Association for Computational Linguistics: ACL 2020, pages 3750–3764, 2020.

[13] S. Wang, Y. Jiang, J. Kasai, Z. Liu, H. Mostafazadeh, G. Zhang, and Y. Fang. Disco-RAG: Improving Document Consistency in Retrieval-Augmented Generation with Discourse Relationships. arXiv preprint arXiv:2601.04377, 2025.

[14] W. B. Croft, D. Metzler, and T. Strohman. Search Engines: Information Retrieval in Practice. Pearson Education, 2015.

[15] G. Grefenstette. Explorations in Automatic Thesaurus Discovery. Kluwer Academic Publishers, 1994.

[16] L. Gao, X. Ma, J. Lin, and J. Callan. Precise Zero-Shot Dense Retrieval without Relevance Labels. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), 2023.

[17] N. Reimers and I. Gurevych. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2019.

[18] [ARTIFACT:art_r9whYzfM2OVO] Evaluation code confirms BM25 instantiation per paper (within-document), not corpus-level.

[19] [ARTIFACT:art_r9whYzfM2OVO] Full subgroup analysis with 95% bootstrap CIs for all subgroups.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) Section text is truncated to 512 characters before embedding (eval.py line 174: `texts = [s['text'][:512] for s in sections]`). At approximately 4–5 characters per character including spaces, 512 characters corresponds to roughly 80–100 words—the first paragraph or two of a section. Scientific paper Methods and Results sections routinely run 300–1500 words. This truncation systematically discards most section content before both the cosine similarity and the TF-ISF computation, meaning: (1) the cosine baseline is not representative of dense retrieval over full sections, (2) the TF-ISF term statistics are computed over truncated text, and (3) the conclusion that 'dense embedding quality is a bottleneck' is confounded by an implementation artifact that mimics a quality failure. This is not mentioned anywhere in the paper's Methods section.
  Action: Remove the 512-character truncation for the embedding step, or replace it with a 512-token truncation (which is ~2000 characters and much more appropriate for sentence-transformers). For TF-ISF and BM25, use the full section text for term statistics. Report the mean and distribution of section lengths in the dataset to contextualize the impact. Re-run the evaluation and check whether results change. If the truncation was necessary for computational efficiency, discuss it explicitly and justify it.
- [MINOR] (rigor) The ISF diagnostic is disclosed as being filtered to 139 records (Methods/Results gold sections) but is not corrected. The paper now acknowledges this as a limitation but continues to present the ISF values (Introduction ISF=1.335, Methods=1.227, Results=1.243) as if they characterize the full corpus. If the ISF ordering reverses on the full 200-record corpus, the mechanistic falsification argument collapses. Since the filter is in a single line of code (eval.py line 412), re-running on all records is a trivial fix.
  Action: Remove the gold-section-type filter in compute_isf_diagnostics (eval.py line 412) and re-run. Report the ISF values for all 200 records. If the ordering (Introduction > Methods/Results) holds on the full corpus, the mechanistic argument is strengthened; if it does not, revise the conclusion accordingly.
- [MINOR] (scope) Sequential (non-stratified) sampling is retained. The paper acknowledges this but does not address the consequence: the first 200 QASPER questions in split order may skew toward certain papers or question types. The subgroup label 'Methods/Results (n=137, adequately powered)' is correct for that group, but the overall sample representativeness is not established.
  Action: Either (a) sample with stratification by paper (to avoid overrepresentation of prolific-question papers) and by gold-section type (to ensure ~proportional coverage of section types), or (b) use the full validation split (~890 examples), which would also increase statistical power for all subgroups. If neither is feasible due to cost, at minimum report the distribution of papers (questions per paper) in the sample to assess whether any single paper dominates.
- [MINOR] (evidence) The recall numbers differ dramatically between the two experimental runs in a way that is not adequately explained. The n=180 run reports cosine recall of 0.154 and TF-ISF recall of 0.098. The n=200 run reports cosine recall of 0.467 and TF-ISF recall of 0.484. This is a 3x difference in absolute recall that cannot plausibly be explained by a 20-example difference in sample size or LLM model choice. The paper attributes the overall discrepancy to 'LLM quality' and 'data loading artifacts' but does not explain why recall—a purely retrieval-side metric independent of the LLM—differs by 3x.
  Action: Investigate and explain the 3x recall discrepancy between the two runs. Check whether the evidence matching logic differs (does the n=180 run use fuzzy matching with a higher threshold? Does it use different section IDs?). This discrepancy is a stronger signal than the F1 difference that the two runs measured fundamentally different things, and understanding it would significantly sharpen the methodological integrity analysis in Section 4.5.
- [MINOR] (clarity) The Disco-RAG citation ([13]: Wang et al. arXiv:2601.04377, 2025) appears in the Related Work and Discussion sections as an authoritative reference for a SOTA discourse-aware retrieval system. An arXiv preprint from January 2025 with a URL of the form 2601.xxxxx has not been peer-reviewed, and its results may not be reproducible. The paper treats it as an established baseline ('Disco-RAG achieves SOTA without fine-tuning') without appropriate caveat.
  Action: Add a caveat when citing arXiv preprints that have not appeared at a peer-reviewed venue. If Disco-RAG's results are central to the Discussion, either cite a peer-reviewed version or soften the claim to 'preliminary evidence from an arXiv preprint.'
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

### [2] HUMAN-USER prompt · 2026-07-20 12:34:36 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [3] SYSTEM-USER prompt · 2026-07-20 12:35:14 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same conceptual frame retained; key change is identifying 512-char truncation as confound that invalidates strong disconfirmation claim.' is too long (at most 120 characters, got 136)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
