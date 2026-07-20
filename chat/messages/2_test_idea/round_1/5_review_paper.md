# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-20 11:38:35 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/review_paper/review_paper
```

### [2] SYSTEM-USER prompt · 2026-07-20 11:38:41 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-20 11:38:41 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [4] ASSISTANT · 2026-07-20 11:38:59 UTC

```
I'll read the supplementary materials carefully before writing the review.
```

### [5] TOOL CALL — Read · 2026-07-20 11:38:59 UTC

```
/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval.py
```

### [6] TOOL RESULT — Read · 2026-07-20 11:38:59 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval.py", "content": "#!/usr/bin/env python3\n\"\"\"TF-ISF Section Ranking Statistical Evaluation on QASPER.\n\nCompares three retrieval methods (cosine similarity, BM25, TF-ISF) on the QASPER\nscientific QA dataset. Measures section-level recall@3 and token-level answer F1,\nwith bootstrap CIs, paired significance tests, subgroup analysis, and diagnostic\nISF distributions.\n\"\"\"\n\nimport gc\nimport json\nimport math\nimport os\nimport re\nimport resource\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport requests\nfrom loguru import logger\nfrom scipy import stats\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\nlogger.add(\"logs/run.log\", rotation=\"30 MB\", level=\"DEBUG\")\n\nWORKSPACE = Path(__file__).parent\nRESULTS_DIR = WORKSPACE / \"results\"\nRESULTS_DIR.mkdir(exist_ok=True)\n\n# Container-aware RAM limit\ndef _container_ram_gb():\n    for p in [\"/sys/fs/cgroup/memory.max\", \"/sys/fs/cgroup/memory/memory.limit_in_bytes\"]:\n        try:\n            v = Path(p).read_text().strip()\n            if v != \"max\" and int(v) < 1_000_000_000_000:\n                return int(v) / 1e9\n        except (FileNotFoundError, ValueError):\n            pass\n    return None\n\ndef _detect_cpus():\n    try:\n        q = int(Path(\"/sys/fs/cgroup/cpu/cpu.cfs_quota_us\").read_text())\n        p = int(Path(\"/sys/fs/cgroup/cpu/cpu.cfs_period_us\").read_text())\n        if q > 0:\n            return math.ceil(q / p)\n    except (FileNotFoundError, ValueError):\n        pass\n    try:\n        return len(os.sched_getaffinity(0))\n    except (AttributeError, OSError):\n        pass\n    return os.cpu_count() or 1\n\nTOTAL_RAM_GB = _container_ram_gb() or 16.0\nNUM_CPUS = _detect_cpus()\nRAM_BUDGET = int(TOTAL_RAM_GB * 0.7 * 1e9)\nlogger.info(f\"Hardware: {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f}GB RAM, budget={RAM_BUDGET/1e9:.1f}GB\")\nresource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))\n\n# OpenRouter config\nOR_API_KEY = os.environ.get(\"OPENROUTER_API_KEY\", \"\")\nOR_BASE_URL = \"https://openrouter.ai/api/v1/chat/completions\"\nLLM_MODEL = \"meta-llama/llama-3.2-3b-instruct\"\nMAX_LLM_BUDGET = 8.0  # USD hard cap\ncumulative_cost = 0.0\n\nN_QUESTIONS = int(os.environ.get(\"N_QUESTIONS\", \"200\"))  # target sample size\nN_BOOTSTRAP = 10000     # bootstrap resamples\nTOP_K = 3               # sections to retrieve\nMAX_CONTEXT_TOKENS = 1500  # approx chars for LLM context\n\n# ─── Section type inference ──────────────────────────────────────────────────\n\nSECTION_TYPE_PATTERNS = [\n    (re.compile(r'abstract', re.I), \"Abstract\"),\n    (re.compile(r'introduction', re.I), \"Introduction\"),\n    (re.compile(r'related|prior|background|literature', re.I), \"Related Work\"),\n    (re.compile(r'method|approach|model|framework|architecture|experiment|setup|dataset|data|training|implementation', re.I), \"Methods\"),\n    (re.compile(r'result|finding|performance|evaluation|benchmark|comparison|ablation', re.I), \"Results\"),\n    (re.compile(r'discussion|analysis|limitation|error|case study', re.I), \"Discussion\"),\n    (re.compile(r'conclusion|future|summary', re.I), \"Conclusion\"),\n]\n\ndef infer_section_type(name: str) -> str:\n    for pat, label in SECTION_TYPE_PATTERNS:\n        if pat.search(name):\n            return label\n    return \"Other\"\n\n# ─── Tokenization ────────────────────────────────────────────────────────────\n\ndef simple_tokenize(text: str) -> list[str]:\n    \"\"\"Lowercase, alpha-only tokens.\"\"\"\n    return re.findall(r'[a-z]+', text.lower())\n\n# ─── Token F1 ────────────────────────────────────────────────────────────────\n\ndef token_f1(pred: str, gold: str) -> float:\n    \"\"\"Standard QASPER token-level F1.\"\"\"\n    pred_tokens = simple_tokenize(pred)\n    gold_tokens = simple_tokenize(gold)\n    if not pred_tokens or not gold_tokens:\n        return 0.0\n    pred_counter: dict[str, int] = defaultdict(int)\n    gold_counter: dict[str, int] = defaultdict(int)\n    for t in pred_tokens:\n        pred_counter[t] += 1\n    for t in gold_tokens:\n        gold_counter[t] += 1\n    common = sum(min(pred_counter[t], gold_counter[t]) for t in pred_counter if t in gold_counter)\n    if common == 0:\n        return 0.0\n    precision = common / len(pred_tokens)\n    recall = common / len(gold_tokens)\n    return 2 * precision * recall / (precision + recall)\n\ndef max_token_f1(pred: str, gold_answers: list[str]) -> float:\n    \"\"\"Max F1 across all gold answers (QASPER standard).\"\"\"\n    if not gold_answers:\n        return 0.0\n    return max(token_f1(pred, g) for g in gold_answers)\n\n# ─── TF-ISF Retrieval ────────────────────────────────────────────────────────\n\ndef compute_isf(sections: list[dict]) -> dict[str, float]:\n    \"\"\"Compute Inverse Section Frequency for all terms in a document.\"\"\"\n    n = len(sections)\n    if n == 0:\n        return {}\n    sf: dict[str, int] = defaultdict(int)\n    for sec in sections:\n        present = set(simple_tokenize(sec[\"text\"]))\n        for t in present:\n            sf[t] += 1\n    isf = {t: math.log(n / (1 + sf[t])) for t in sf}\n    return isf\n\ndef score_tfisf(query_tokens: list[str], section_text: str, isf: dict[str, float]) -> float:\n    \"\"\"TF-ISF score for a section given a query.\"\"\"\n    sec_tokens = simple_tokenize(section_text)\n    if not sec_tokens:\n        return 0.0\n    tf: dict[str, float] = defaultdict(float)\n    for t in sec_tokens:\n        tf[t] += 1.0 / len(sec_tokens)\n    return sum(tf.get(t, 0.0) * isf.get(t, 0.0) for t in query_tokens)\n\ndef retrieve_tfisf(query: str, sections: list[dict], k: int = TOP_K) -> list[str]:\n    isf = compute_isf(sections)\n    q_tokens = simple_tokenize(query)\n    scores = [(score_tfisf(q_tokens, s[\"text\"], isf), s[\"name\"]) for s in sections]\n    scores.sort(reverse=True)\n    return [name for _, name in scores[:k]]\n\n# ─── BM25 Retrieval ──────────────────────────────────────────────────────────\n\ndef retrieve_bm25(query: str, sections: list[dict], k: int = TOP_K) -> list[str]:\n    from rank_bm25 import BM25Okapi\n    tokenized_corpus = [simple_tokenize(s[\"text\"]) for s in sections]\n    bm25 = BM25Okapi(tokenized_corpus)\n    q_tokens = simple_tokenize(query)\n    scores = bm25.get_scores(q_tokens)\n    ranked = np.argsort(scores)[::-1][:k]\n    return [sections[i][\"name\"] for i in ranked]\n\n# ─── Cosine Retrieval ─────────────────────────────────────────────────────────\n\ndef retrieve_cosine(query: str, sections: list[dict], embedder, k: int = TOP_K) -> list[str]:\n    texts = [s[\"text\"][:512] for s in sections]  # truncate for efficiency\n    all_texts = [query] + texts\n    embeddings = embedder.encode(all_texts, batch_size=32, show_progress_bar=False, normalize_embeddings=True)\n    q_emb = embeddings[0]\n    s_embs = embeddings[1:]\n    scores = s_embs @ q_emb\n    ranked = np.argsort(scores)[::-1][:k]\n    return [sections[i][\"name\"] for i in ranked]\n\n# ─── Section recall ───────────────────────────────────────────────────────────\n\ndef section_recall(retrieved: list[str], gold: list[str]) -> float:\n    if not gold:\n        return float('nan')\n    retrieved_set = set(r.lower().strip() for r in retrieved)\n    gold_set = set(g.lower().strip() for g in gold)\n    overlap = retrieved_set & gold_set\n    return len(overlap) / len(gold_set)\n\n# ─── LLM Reader ───────────────────────────────────────────────────────────────\n\ndef call_llm(question: str, context: str, max_tokens: int = 150) -> tuple[str, float]:\n    \"\"\"Call OpenRouter LLM. Returns (answer, cost_usd).\"\"\"\n    global cumulative_cost\n    if cumulative_cost >= MAX_LLM_BUDGET:\n        logger.warning(f\"LLM budget exhausted (${cumulative_cost:.2f}), skipping\")\n        return \"\", 0.0\n\n    prompt = f\"Answer the following question based on the provided context. Be concise (1-2 sentences).\\n\\nContext:\\n{context[:MAX_CONTEXT_TOKENS]}\\n\\nQuestion: {question}\\n\\nAnswer:\"\n\n    headers = {\n        \"Authorization\": f\"Bearer {OR_API_KEY}\",\n        \"Content-Type\": \"application/json\",\n    }\n    payload = {\n        \"model\": LLM_MODEL,\n        \"messages\": [{\"role\": \"user\", \"content\": prompt}],\n        \"max_tokens\": max_tokens,\n        \"temperature\": 0.0,\n    }\n\n    try:\n        resp = requests.post(OR_BASE_URL, headers=headers, json=payload, timeout=30)\n        resp.raise_for_status()\n        data = resp.json()\n        answer = data[\"choices\"][0][\"message\"][\"content\"].strip()\n        usage = data.get(\"usage\", {})\n        # Llama-3.2-3B-instruct pricing: ~$0.06/M in, $0.06/M out (free tier usually)\n        in_tokens = usage.get(\"prompt_tokens\", 0)\n        out_tokens = usage.get(\"completion_tokens\", 0)\n        cost = (in_tokens * 0.06 + out_tokens * 0.06) / 1_000_000\n        cumulative_cost += cost\n        logger.debug(f\"LLM call: {in_tokens} in, {out_tokens} out, ${cost:.6f}, total=${cumulative_cost:.4f}\")\n        return answer, cost\n    except Exception as e:\n        logger.error(f\"LLM call failed: {e}\")\n        return \"\", 0.0\n\n# ─── Bootstrap CI ─────────────────────────────────────────────────────────────\n\ndef bootstrap_ci(values: np.ndarray, n_resamples: int = N_BOOTSTRAP, ci: float = 0.95) -> tuple[float, float, float]:\n    \"\"\"Returns (mean, lower, upper) with 95% CI.\"\"\"\n    vals = values[~np.isnan(values)]\n    if len(vals) == 0:\n        return float('nan'), float('nan'), float('nan')\n    rng = np.random.default_rng(42)\n    means = np.array([rng.choice(vals, size=len(vals), replace=True).mean() for _ in range(n_resamples)])\n    alpha = (1 - ci) / 2\n    lower = np.percentile(means, alpha * 100)\n    upper = np.percentile(means, (1 - alpha) * 100)\n    return float(vals.mean()), float(lower), float(upper)\n\n# ─── Effect size ──────────────────────────────────────────────────────────────\n\ndef cohens_d(a: np.ndarray, b: np.ndarray) -> float:\n    a = a[~np.isnan(a)]\n    b = b[~np.isnan(b)]\n    if len(a) < 2 or len(b) < 2:\n        return float('nan')\n    pooled_std = math.sqrt((np.std(a, ddof=1)**2 + np.std(b, ddof=1)**2) / 2)\n    if pooled_std == 0:\n        return 0.0\n    return (np.mean(a) - np.mean(b)) / pooled_std\n\ndef rank_biserial(a: np.ndarray, b: np.ndarray) -> float:\n    \"\"\"Rank-biserial correlation for Wilcoxon signed-rank test.\"\"\"\n    a = a[~np.isnan(a)]\n    b = b[~np.isnan(b)]\n    n = min(len(a), len(b))\n    if n < 2:\n        return float('nan')\n    diffs = a[:n] - b[:n]\n    nonzero = diffs[diffs != 0]\n    if len(nonzero) == 0:\n        return 0.0\n    ranks = stats.rankdata(np.abs(nonzero))\n    r_plus = np.sum(ranks[nonzero > 0])\n    r_minus = np.sum(ranks[nonzero < 0])\n    n_nz = len(nonzero)\n    max_w = n_nz * (n_nz + 1) / 2\n    return (r_plus - r_minus) / max_w\n\n# ─── Load QASPER ──────────────────────────────────────────────────────────────\n\ndef load_qasper(n_max: int = N_QUESTIONS) -> list[dict]:\n    \"\"\"Load and parse QASPER, returning list of question records.\"\"\"\n    logger.info(\"Loading QASPER dataset from HuggingFace...\")\n    from datasets import load_dataset\n    ds = load_dataset(\"allenai/qasper\", trust_remote_code=True)\n\n    records = []\n\n    splits = [\"train\", \"validation\"]\n    all_examples = []\n    for split in splits:\n        if split in ds:\n            all_examples.extend(list(ds[split]))\n\n    logger.info(f\"Total papers loaded: {len(all_examples)}\")\n\n    for paper in all_examples:\n        try:\n            paper_id = paper.get(\"id\", \"\")\n\n            # Parse sections — paragraphs is list[list[str]]\n            full_text = paper.get(\"full_text\", {})\n            section_names = full_text.get(\"section_name\", []) or []\n            paragraphs_list = full_text.get(\"paragraphs\", []) or []\n\n            if not section_names or not paragraphs_list:\n                continue\n\n            # Build sections, storing paragraph list for evidence matching\n            sections = []\n            para_to_section: dict[str, str] = {}  # paragraph text -> section name\n            for i, (sname, paras) in enumerate(zip(section_names, paragraphs_list)):\n                paras = paras if isinstance(paras, list) else [str(paras)]\n                text = \" \".join(paras)\n                if len(text.strip()) < 30:\n                    continue\n                stype = infer_section_type(sname)\n                sections.append({\n                    \"name\": sname,\n                    \"section_type\": stype,\n                    \"text\": text,\n                    \"idx\": i,\n                })\n                for p in paras:\n                    para_to_section[p.strip()[:120]] = sname\n\n            if len(sections) < 2:\n                continue\n\n            # Parse QAs\n            qas = paper.get(\"qas\", {})\n            questions = qas.get(\"question\", []) or []\n            answers_list = qas.get(\"answers\", []) or []\n\n            for q_text, ans_obj in zip(questions, answers_list):\n                if not q_text:\n                    continue\n                if not isinstance(ans_obj, dict):\n                    continue\n\n                # Collect answers across all annotators\n                gold_answers = []\n                gold_section_names = []\n\n                for entry in (ans_obj.get(\"answer\") or []):\n                    if not isinstance(entry, dict):\n                        continue\n                    if entry.get(\"unanswerable\"):\n                        continue\n                    ft = entry.get(\"free_form_answer\", \"\")\n                    if ft and ft.strip():\n                        gold_answers.append(ft.strip())\n                    # Also include extractive spans as answer references\n                    for span in (entry.get(\"extractive_spans\") or []):\n                        if span and span.strip():\n                            gold_answers.append(span.strip())\n\n                    # Map evidence paragraphs to sections\n                    for ev in (entry.get(\"evidence\") or []):\n                        if not ev or not ev.strip():\n                            continue\n                        ev_key = ev.strip()[:120]\n                        if ev_key in para_to_section:\n                            gold_section_names.append(para_to_section[ev_key])\n                        else:\n                            # Fuzzy: find section whose text contains evidence\n                            found = False\n                            for sec in sections:\n                                if ev.strip()[:80] in sec[\"text\"]:\n                                    gold_section_names.append(sec[\"name\"])\n                                    found = True\n                                    break\n                            # If still not found, skip this evidence item\n\n                # Need at least one free-form answer and one evidence section\n                gold_answers_ff = [a for a in gold_answers if len(a) > 5]\n                if not gold_answers_ff:\n                    continue\n                if not gold_section_names:\n                    continue\n\n                gold_sec_unique = list(dict.fromkeys(gold_section_names))  # preserve order, dedupe\n                gold_types = list(dict.fromkeys(infer_section_type(g) for g in gold_sec_unique))\n\n                records.append({\n                    \"paper_id\": paper_id,\n                    \"question\": q_text,\n                    \"gold_answers\": gold_answers_ff,\n                    \"gold_sections\": gold_sec_unique,\n                    \"gold_section_types\": gold_types,\n                    \"sections\": sections,\n                })\n\n                if len(records) >= n_max:\n                    break\n        except Exception:\n            logger.error(f\"Failed to parse paper {paper.get('id', '?')}\")\n            continue\n\n        if len(records) >= n_max:\n            break\n\n    logger.info(f\"Parsed {len(records)} QA records with valid sections and answers\")\n    return records\n\n# ─── ISF Diagnostic ───────────────────────────────────────────────────────────\n\ndef compute_isf_diagnostics(records: list[dict]) -> dict:\n    \"\"\"Compute ISF score distributions by section type across the corpus.\"\"\"\n    # For each record where gold section is Methods/Results,\n    # compute mean ISF for each section type\n    type_isf_scores: dict[str, list[float]] = defaultdict(list)\n\n    for rec in records:\n        if not any(t in rec[\"gold_section_types\"] for t in [\"Methods\", \"Results\"]):\n            continue\n        sections = rec[\"sections\"]\n        isf = compute_isf(sections)\n        if not isf:\n            continue\n        for sec in sections:\n            tokens = simple_tokenize(sec[\"text\"])\n            if not tokens:\n                continue\n            sec_isf_vals = [isf.get(t, 0.0) for t in set(tokens) if isf.get(t, 0.0) > 0]\n            if sec_isf_vals:\n                mean_isf = np.mean(sec_isf_vals)\n                type_isf_scores[sec[\"section_type\"]].append(float(mean_isf))\n\n    result = {}\n    for stype, vals in type_isf_scores.items():\n        arr = np.array(vals)\n        result[stype] = {\n            \"n\": len(vals),\n            \"mean\": float(arr.mean()),\n            \"median\": float(np.median(arr)),\n            \"std\": float(arr.std()),\n        }\n    return result\n\n# ─── Main evaluation ──────────────────────────────────────────────────────────\n\n@logger.catch(reraise=True)\ndef main():\n    global cumulative_cost\n\n    start_time = time.time()\n\n    # Check OpenRouter API key\n    if not OR_API_KEY:\n        logger.warning(\"OPENROUTER_API_KEY not set — will skip LLM calls, use gold section text as proxy answer\")\n\n    # Load embedder\n    logger.info(\"Loading sentence-transformers embedder...\")\n    from sentence_transformers import SentenceTransformer\n    embedder = SentenceTransformer(\"all-MiniLM-L6-v2\")\n    logger.info(\"Embedder loaded\")\n\n    # Load data\n    records = load_qasper(n_max=N_QUESTIONS)\n    n = len(records)\n    logger.info(f\"Working with {n} QA records\")\n\n    if n < 10:\n        logger.error(\"Too few records — check dataset parsing\")\n        raise ValueError(f\"Only {n} records parsed\")\n\n    # Per-example storage\n    results_per_method = {\n        \"cosine\": {\"f1\": [], \"recall\": [], \"retrieved\": []},\n        \"bm25\": {\"f1\": [], \"recall\": [], \"retrieved\": []},\n        \"tfisf\": {\"f1\": [], \"recall\": [], \"retrieved\": []},\n    }\n    gold_types_per_example = []\n    answers_per_method = {\"cosine\": [], \"bm25\": [], \"tfisf\": []}\n\n    logger.info(\"Starting retrieval + evaluation loop...\")\n\n    for i, rec in enumerate(records):\n        if i % 20 == 0:\n            elapsed = time.time() - start_time\n            logger.info(f\"Progress: {i}/{n}, elapsed={elapsed:.0f}s, LLM_cost=${cumulative_cost:.4f}\")\n\n        question = rec[\"question\"]\n        sections = rec[\"sections\"]\n        gold_sections = rec[\"gold_sections\"]\n        gold_types = rec[\"gold_section_types\"]\n        gold_answers = rec[\"gold_answers\"]\n        gold_types_per_example.append(gold_types)\n\n        if len(sections) < 2:\n            for m in results_per_method:\n                results_per_method[m][\"f1\"].append(float('nan'))\n                results_per_method[m][\"recall\"].append(float('nan'))\n                results_per_method[m][\"retrieved\"].append([])\n                answers_per_method[m].append(\"\")\n            continue\n\n        # Retrieve\n        try:\n            ret_cosine = retrieve_cosine(question, sections, embedder)\n        except Exception:\n            logger.error(f\"Cosine retrieval failed ex {i}\")\n            ret_cosine = [sections[0][\"name\"]]\n\n        try:\n            ret_bm25 = retrieve_bm25(question, sections)\n        except Exception:\n            logger.error(f\"BM25 retrieval failed ex {i}\")\n            ret_bm25 = [sections[0][\"name\"]]\n\n        try:\n            ret_tfisf = retrieve_tfisf(question, sections)\n        except Exception:\n            logger.error(f\"TF-ISF retrieval failed ex {i}\")\n            ret_tfisf = [sections[0][\"name\"]]\n\n        # Section recall\n        for method, retrieved in [(\"cosine\", ret_cosine), (\"bm25\", ret_bm25), (\"tfisf\", ret_tfisf)]:\n            results_per_method[method][\"recall\"].append(section_recall(retrieved, gold_sections))\n            results_per_method[method][\"retrieved\"].append(retrieved)\n\n        # Build context for LLM from retrieved sections\n        def build_context(retrieved_names: list[str]) -> str:\n            sec_map = {s[\"name\"]: s[\"text\"] for s in sections}\n            parts = []\n            for name in retrieved_names:\n                text = sec_map.get(name, \"\")\n                parts.append(f\"[{name}]\\n{text[:500]}\")\n            return \"\\n\\n\".join(parts)\n\n        # LLM answer generation\n        for method, retrieved in [(\"cosine\", ret_cosine), (\"bm25\", ret_bm25), (\"tfisf\", ret_tfisf)]:\n            if OR_API_KEY and cumulative_cost < MAX_LLM_BUDGET:\n                ctx = build_context(retrieved)\n                answer, _ = call_llm(question, ctx)\n            else:\n                # Fallback: use concatenation of retrieved section text as answer proxy\n                ctx = build_context(retrieved)\n                answer = ctx[:200]\n\n            answers_per_method[method].append(answer)\n            f1 = max_token_f1(answer, gold_answers)\n            results_per_method[method][\"f1\"].append(f1)\n\n        # Free memory\n        del sections\n        gc.collect()\n\n    logger.info(f\"Retrieval+eval loop done. LLM total cost: ${cumulative_cost:.4f}\")\n\n    # ── Aggregate metrics ────────────────────────────────────────────────────\n    method_names = [\"cosine\", \"bm25\", \"tfisf\"]\n    metrics_agg = {}\n    method_stats = {}\n\n    for method in method_names:\n        f1_arr = np.array(results_per_method[method][\"f1\"])\n        rec_arr = np.array(results_per_method[method][\"recall\"])\n\n        f1_mean, f1_lo, f1_hi = bootstrap_ci(f1_arr)\n        rec_mean, rec_lo, rec_hi = bootstrap_ci(rec_arr)\n\n        method_stats[method] = {\n            \"f1_mean\": f1_mean, \"f1_ci_lo\": f1_lo, \"f1_ci_hi\": f1_hi,\n            \"recall_mean\": rec_mean, \"recall_ci_lo\": rec_lo, \"recall_ci_hi\": rec_hi,\n            \"n\": int(np.sum(~np.isnan(f1_arr))),\n        }\n\n        metrics_agg[f\"{method}_f1\"] = f1_mean\n        metrics_agg[f\"{method}_recall_at_{TOP_K}\"] = rec_mean\n\n        logger.info(f\"{method}: F1={f1_mean:.4f} CI=[{f1_lo:.4f},{f1_hi:.4f}], \"\n                    f\"Recall@{TOP_K}={rec_mean:.4f} CI=[{rec_lo:.4f},{rec_hi:.4f}]\")\n\n    # ── Statistical tests ────────────────────────────────────────────────────\n    def paired_ttest(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:\n        mask = ~np.isnan(a) & ~np.isnan(b)\n        a, b = a[mask], b[mask]\n        if len(a) < 5:\n            return float('nan'), float('nan')\n        t, p = stats.ttest_rel(a, b)\n        return float(t), float(p)\n\n    comparisons = [\n        (\"tfisf\", \"cosine\", \"f1\"),\n        (\"tfisf\", \"bm25\", \"f1\"),\n        (\"tfisf\", \"cosine\", \"recall\"),\n        (\"tfisf\", \"bm25\", \"recall\"),\n        (\"cosine\", \"bm25\", \"f1\"),\n        (\"cosine\", \"bm25\", \"recall\"),\n    ]\n\n    raw_pvals = []\n    comparison_results = []\n    for m1, m2, metric in comparisons:\n        key = \"f1\" if metric == \"f1\" else \"recall\"\n        arr1 = np.array(results_per_method[m1][key])\n        arr2 = np.array(results_per_method[m2][key])\n        t, p = paired_ttest(arr1, arr2)\n        d = cohens_d(arr1, arr2)\n        rbc = rank_biserial(arr1, arr2)\n        comparison_results.append({\n            \"comparison\": f\"{m1}_vs_{m2}_{metric}\",\n            \"t_stat\": t, \"p_val\": p, \"cohens_d\": d, \"rank_biserial\": rbc,\n            \"delta_mean\": float(np.nanmean(arr1) - np.nanmean(arr2)),\n        })\n        if not math.isnan(p):\n            raw_pvals.append(p)\n\n    # Holm-Bonferroni correction\n    if raw_pvals:\n        sorted_idx = np.argsort(raw_pvals)\n        n_tests = len(raw_pvals)\n        pvals_arr = np.array(raw_pvals)\n        adjusted = np.ones(n_tests)\n        for rank_i, idx in enumerate(sorted_idx):\n            adjusted[idx] = min(pvals_arr[idx] * (n_tests - rank_i), 1.0)\n        # Apply monotone: adjusted[i] >= adjusted[i-1]\n        prev = 1.0\n        for i in sorted_idx[::-1]:\n            adjusted[i] = min(adjusted[i], prev)\n            prev = adjusted[i]\n\n        j = 0\n        for cr in comparison_results:\n            if not math.isnan(cr[\"p_val\"]):\n                cr[\"p_val_holm\"] = float(adjusted[j])\n                j += 1\n            else:\n                cr[\"p_val_holm\"] = float('nan')\n\n    for cr in comparison_results:\n        key = cr[\"comparison\"]\n        metrics_agg[f\"delta_{key}\"] = cr[\"delta_mean\"]\n        metrics_agg[f\"pval_{key}\"] = cr.get(\"p_val\", float('nan'))\n        logger.info(f\"  {key}: delta={cr['delta_mean']:.4f}, p={cr.get('p_val','?'):.4f}, \"\n                    f\"p_holm={cr.get('p_val_holm','?'):.4f}, d={cr['cohens_d']:.3f}\")\n\n    # ── Subgroup analysis ────────────────────────────────────────────────────\n    SUBGROUP_MAP = {\n        \"Abstract_Intro\": [\"Abstract\", \"Introduction\"],\n        \"Methods_Results\": [\"Methods\", \"Results\"],\n        \"Discussion_Conclusion\": [\"Discussion\", \"Conclusion\"],\n        \"Other\": [\"Other\", \"Related Work\"],\n    }\n\n    subgroup_results = {}\n    for sg_name, sg_types in SUBGROUP_MAP.items():\n        indices = [\n            i for i, types in enumerate(gold_types_per_example)\n            if any(t in sg_types for t in types)\n        ]\n        if not indices:\n            continue\n        sg = {}\n        for method in method_names:\n            f1_arr = np.array([results_per_method[method][\"f1\"][i] for i in indices])\n            rec_arr = np.array([results_per_method[method][\"recall\"][i] for i in indices])\n            f1_m, f1_lo, f1_hi = bootstrap_ci(f1_arr)\n            rec_m, rec_lo, rec_hi = bootstrap_ci(rec_arr)\n            sg[method] = {\n                \"n\": len(indices),\n                \"f1_mean\": f1_m, \"f1_ci_lo\": f1_lo, \"f1_ci_hi\": f1_hi,\n                \"recall_mean\": rec_m, \"recall_ci_lo\": rec_lo, \"recall_ci_hi\": rec_hi,\n            }\n        subgroup_results[sg_name] = sg\n        logger.info(f\"Subgroup {sg_name} (n={len(indices)}): \"\n                    f\"tfisf_f1={sg['tfisf']['f1_mean']:.4f}, \"\n                    f\"cosine_f1={sg['cosine']['f1_mean']:.4f}\")\n        # Add to agg metrics\n        for method in method_names:\n            metrics_agg[f\"sg_{sg_name}_{method}_f1\"] = sg[method][\"f1_mean\"]\n            metrics_agg[f\"sg_{sg_name}_{method}_recall\"] = sg[method][\"recall_mean\"]\n\n    # ── ISF Diagnostic ───────────────────────────────────────────────────────\n    logger.info(\"Computing ISF diagnostic distributions...\")\n    isf_diag = compute_isf_diagnostics(records)\n    logger.info(f\"ISF diagnostics: {json.dumps({k: {kk: round(vv,4) for kk,vv in v.items()} for k,v in isf_diag.items()}, indent=2)}\")\n\n    for stype, vals in isf_diag.items():\n        key = stype.replace(\"/\", \"_\").replace(\" \", \"_\")\n        metrics_agg[f\"isf_mean_{key}\"] = vals[\"mean\"]\n\n    # ── Build output JSON ─────────────────────────────────────────────────────\n    # Build per-example outputs\n    examples = []\n    for i, rec in enumerate(records):\n        ex = {\n            \"input\": rec[\"question\"],\n            \"output\": rec[\"gold_answers\"][0] if rec[\"gold_answers\"] else \"\",\n            \"predict_cosine\": answers_per_method[\"cosine\"][i] if i < len(answers_per_method[\"cosine\"]) else \"\",\n            \"predict_bm25\": answers_per_method[\"bm25\"][i] if i < len(answers_per_method[\"bm25\"]) else \"\",\n            \"predict_tfisf\": answers_per_method[\"tfisf\"][i] if i < len(answers_per_method[\"tfisf\"]) else \"\",\n            \"eval_f1_cosine\": results_per_method[\"cosine\"][\"f1\"][i] if i < len(results_per_method[\"cosine\"][\"f1\"]) else float('nan'),\n            \"eval_f1_bm25\": results_per_method[\"bm25\"][\"f1\"][i] if i < len(results_per_method[\"bm25\"][\"f1\"]) else float('nan'),\n            \"eval_f1_tfisf\": results_per_method[\"tfisf\"][\"f1\"][i] if i < len(results_per_method[\"tfisf\"][\"f1\"]) else float('nan'),\n            \"eval_recall_cosine\": results_per_method[\"cosine\"][\"recall\"][i] if i < len(results_per_method[\"cosine\"][\"recall\"]) else float('nan'),\n            \"eval_recall_bm25\": results_per_method[\"bm25\"][\"recall\"][i] if i < len(results_per_method[\"bm25\"][\"recall\"]) else float('nan'),\n            \"eval_recall_tfisf\": results_per_method[\"tfisf\"][\"recall\"][i] if i < len(results_per_method[\"tfisf\"][\"recall\"]) else float('nan'),\n            \"metadata_paper_id\": rec[\"paper_id\"],\n            \"metadata_gold_section_types\": json.dumps(rec[\"gold_section_types\"]),\n            \"metadata_gold_sections\": json.dumps(rec[\"gold_sections\"][:3]),\n            \"metadata_retrieved_tfisf\": json.dumps(results_per_method[\"tfisf\"][\"retrieved\"][i] if i < len(results_per_method[\"tfisf\"][\"retrieved\"]) else []),\n            \"metadata_retrieved_cosine\": json.dumps(results_per_method[\"cosine\"][\"retrieved\"][i] if i < len(results_per_method[\"cosine\"][\"retrieved\"]) else []),\n            \"metadata_retrieved_bm25\": json.dumps(results_per_method[\"bm25\"][\"retrieved\"][i] if i < len(results_per_method[\"bm25\"][\"retrieved\"]) else []),\n        }\n        # Replace NaN with 0.0 for JSON compliance\n        for k, v in ex.items():\n            if isinstance(v, float) and math.isnan(v):\n                ex[k] = 0.0\n        examples.append(ex)\n\n    # Clean NaN in metrics_agg\n    for k, v in metrics_agg.items():\n        if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):\n            metrics_agg[k] = 0.0\n\n    output = {\n        \"metadata\": {\n            \"evaluation_name\": \"TF-ISF Section Ranking Statistical Evaluation\",\n            \"dataset\": \"QASPER (allenai/qasper)\",\n            \"n_questions\": n,\n            \"top_k\": TOP_K,\n            \"n_bootstrap\": N_BOOTSTRAP,\n            \"llm_model\": LLM_MODEL,\n            \"llm_cost_usd\": round(cumulative_cost, 6),\n            \"method_stats\": method_stats,\n            \"statistical_comparisons\": comparison_results,\n            \"subgroup_analysis\": subgroup_results,\n            \"isf_diagnostics\": isf_diag,\n            \"baselines\": [\"cosine_similarity (all-MiniLM-L6-v2)\", \"BM25Okapi\"],\n            \"main_method\": \"TF-ISF (Inverse Section Frequency)\",\n        },\n        \"metrics_agg\": metrics_agg,\n        \"datasets\": [\n            {\n                \"dataset\": \"QASPER\",\n                \"examples\": examples,\n            }\n        ],\n    }\n\n    # Replace NaN/inf in comparison results for JSON\n    def clean_dict(d):\n        if isinstance(d, dict):\n            return {k: clean_dict(v) for k, v in d.items()}\n        if isinstance(d, list):\n            return [clean_dict(v) for v in d]\n        if isinstance(d, float) and (math.isnan(d) or math.isinf(d)):\n            return 0.0\n        return d\n\n    output = clean_dict(output)\n\n    out_path = WORKSPACE / \"eval_out.json\"\n    out_path.write_text(json.dumps(output, indent=2))\n    logger.info(f\"Saved eval_out.json ({out_path.stat().st_size / 1024:.1f} KB)\")\n\n    # Also save detailed results\n    detail_path = RESULTS_DIR / \"detailed_results.json\"\n    detail_path.write_text(json.dumps({\n        \"comparison_results\": clean_dict(comparison_results),\n        \"subgroup_results\": clean_dict(subgroup_results),\n        \"isf_diagnostics\": clean_dict(isf_diag),\n        \"method_stats\": clean_dict(method_stats),\n        \"total_cost_usd\": round(cumulative_cost, 6),\n    }, indent=2))\n    logger.info(f\"Saved detailed results to {detail_path}\")\n\n    elapsed = time.time() - start_time\n    logger.info(f\"Total elapsed: {elapsed:.0f}s, LLM cost: ${cumulative_cost:.4f}\")\n    logger.info(f\"Summary: tfisf_f1={metrics_agg.get('tfisf_f1',0):.4f}, \"\n                f\"cosine_f1={metrics_agg.get('cosine_f1',0):.4f}, \"\n                f\"bm25_f1={metrics_agg.get('bm25_f1',0):.4f}\")\n    logger.info(f\"Summary: tfisf_recall={metrics_agg.get(f'tfisf_recall_at_{TOP_K}',0):.4f}, \"\n                f\"cosine_recall={metrics_agg.get(f'cosine_recall_at_{TOP_K}',0):.4f}\")\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 778, "startLine": 1, "totalLines": 778}}
```

### [7] TOOL CALL — Read · 2026-07-20 11:38:59 UTC

```
/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py
```

### [8] TOOL RESULT — Read · 2026-07-20 11:38:59 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py", "content": "#!/usr/bin/env python3\n\"\"\"TF-ISF vs Cosine vs BM25 section retrieval benchmark on QASPER scientific QA dataset.\"\"\"\n\nimport gc\nimport json\nimport math\nimport os\nimport re\nimport resource\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport requests\nfrom loguru import logger\nfrom tenacity import retry, stop_after_attempt, wait_exponential\n\nWORKSPACE = Path(__file__).parent\nLOGS_DIR = WORKSPACE / \"logs\"\nLOGS_DIR.mkdir(exist_ok=True)\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\nlogger.add(str(LOGS_DIR / \"run.log\"), rotation=\"30 MB\", level=\"DEBUG\")\n\n# ── Hardware detection ──────────────────────────────────────────────────────\ndef _container_ram_gb() -> float:\n    for p in [\"/sys/fs/cgroup/memory.max\", \"/sys/fs/cgroup/memory/memory.limit_in_bytes\"]:\n        try:\n            v = Path(p).read_text().strip()\n            if v != \"max\" and int(v) < 1_000_000_000_000:\n                return int(v) / 1e9\n        except (FileNotFoundError, ValueError):\n            pass\n    import psutil\n    return psutil.virtual_memory().total / 1e9\n\nTOTAL_RAM_GB = _container_ram_gb()\nRAM_BUDGET = int(min(TOTAL_RAM_GB * 0.7, 20) * 1024**3)\nresource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))\nlogger.info(f\"RAM budget: {RAM_BUDGET / 1e9:.1f}GB (total={TOTAL_RAM_GB:.1f}GB)\")\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMAX_QUESTIONS = int(os.getenv(\"MAX_QUESTIONS\", \"180\"))\nTOP_K = 3\nMAX_CONTEXT_TOKENS = 1800  # chars proxy for tokens\nBUDGET_LIMIT_USD = 8.0\nLLM_MODEL = \"tencent/hy3:free\"  # free model\nOPENROUTER_BASE = \"https://openrouter.ai/api/v1\"\n\n# ── OpenRouter client ────────────────────────────────────────────────────────\ndef _get_or_key() -> str:\n    key = os.getenv(\"OPENROUTER_API_KEY\", \"\")\n    if not key:\n        # try reading from ability client env\n        env_path = Path(\"/ai-inventor/.claude/skills/aii-openrouter-llms/../.ability_client_venv\")\n        for p in [Path(\"/ai-inventor/.env\"), Path(\"/root/.env\")]:\n            if p.exists():\n                for line in p.read_text().splitlines():\n                    if line.startswith(\"OPENROUTER_API_KEY=\"):\n                        key = line.split(\"=\", 1)[1].strip().strip('\"')\n                        break\n    return key\n\nOR_KEY = _get_or_key()\n\n@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=10))\ndef llm_call(prompt: str, max_tokens: int = 150) -> tuple[str, float]:\n    \"\"\"Returns (answer_text, cost_usd). Cost is 0 for free models.\"\"\"\n    headers = {\n        \"Authorization\": f\"Bearer {OR_KEY}\",\n        \"Content-Type\": \"application/json\",\n        \"HTTP-Referer\": \"https://ai-inventor.ai\",\n    }\n    payload = {\n        \"model\": LLM_MODEL,\n        \"messages\": [{\"role\": \"user\", \"content\": prompt}],\n        \"max_tokens\": max_tokens,\n        \"temperature\": 0.0,\n    }\n    resp = requests.post(\n        f\"{OPENROUTER_BASE}/chat/completions\",\n        headers=headers,\n        json=payload,\n        timeout=60,\n    )\n    resp.raise_for_status()\n    data = resp.json()\n    answer = data[\"choices\"][0][\"message\"][\"content\"].strip()\n    # free model → cost = 0\n    usage = data.get(\"usage\", {})\n    in_tok = usage.get(\"prompt_tokens\", 0)\n    out_tok = usage.get(\"completion_tokens\", 0)\n    cost = (in_tok * 0.0 + out_tok * 0.0) / 1e6  # free\n    return answer, cost\n\n# ── QASPER loading ───────────────────────────────────────────────────────────\nDATA_DIR = WORKSPACE / \"data\"\n\ndef load_qasper(max_q: int) -> list[dict]:\n    \"\"\"Load QASPER from local raw JSON files and return flat QA records.\"\"\"\n    logger.info(\"Loading QASPER from local JSON files...\")\n    records = []\n\n    for fname in [\"qasper-train-v0.3.json\", \"qasper-dev-v0.3.json\"]:\n        fpath = DATA_DIR / fname\n        if not fpath.exists():\n            logger.warning(f\"Missing {fpath}, skipping\")\n            continue\n        papers = json.loads(fpath.read_text())\n        logger.info(f\"Loaded {len(papers)} papers from {fname}\")\n\n        for paper_id, paper in papers.items():\n            title = paper.get(\"title\", \"\")\n            abstract = paper.get(\"abstract\", \"\")\n\n            # Build sections\n            sections = []\n            if abstract.strip():\n                sections.append({\"name\": \"Abstract\", \"text\": abstract})\n            for sec in paper.get(\"full_text\", []):\n                sname = sec.get(\"section_name\") or \"Unknown\"\n                paras = sec.get(\"paragraphs\", [])\n                text = \" \".join(str(p) for p in paras if p).strip()\n                if text:\n                    sections.append({\"name\": sname, \"text\": text})\n\n            if not sections:\n                continue\n\n            for qa in paper.get(\"qas\", []):\n                question = qa.get(\"question\", \"\").strip()\n                if not question:\n                    continue\n\n                gold_answers = []\n                evidence_sections = []\n                for ans_wrap in qa.get(\"answers\", []):\n                    ans = ans_wrap.get(\"answer\", {})\n                    fa = ans.get(\"free_form_answer\", \"\")\n                    if fa:\n                        gold_answers.append(fa)\n                    ev = ans.get(\"evidence\", [])\n                    if isinstance(ev, list):\n                        evidence_sections.extend([str(e) for e in ev if e])\n\n                if not gold_answers:\n                    continue\n\n                records.append({\n                    \"paper_id\": paper_id,\n                    \"title\": title,\n                    \"question\": question,\n                    \"gold_answers\": gold_answers,\n                    \"evidence_sections\": evidence_sections,\n                    \"sections\": sections,\n                })\n\n                if len(records) >= max_q:\n                    logger.info(f\"Reached {max_q} questions\")\n                    return records\n\n    logger.info(f\"Loaded {len(records)} QA records from QASPER\")\n    return records\n\n# ── Text utilities ───────────────────────────────────────────────────────────\n_STOP = frozenset([\"the\",\"a\",\"an\",\"is\",\"in\",\"of\",\"to\",\"and\",\"or\",\"for\",\"with\",\n                    \"on\",\"at\",\"by\",\"from\",\"as\",\"it\",\"its\",\"this\",\"that\",\"are\",\"was\",\n                    \"were\",\"be\",\"been\",\"have\",\"has\",\"had\",\"not\",\"but\",\"if\",\"we\",\"our\",\n                    \"they\",\"their\",\"can\",\"which\",\"who\",\"what\",\"how\",\"when\",\"where\"])\n\ndef tokenize(text: str) -> list[str]:\n    tokens = re.findall(r\"[a-z0-9]+\", text.lower())\n    return [t for t in tokens if len(t) > 1 and t not in _STOP]\n\ndef token_f1(pred: str, golds: list[str]) -> float:\n    \"\"\"Compute max token-level F1 against multiple gold answers (QASPER standard).\"\"\"\n    pred_toks = set(re.findall(r\"\\w+\", pred.lower()))\n    best = 0.0\n    for gold in golds:\n        gold_toks = set(re.findall(r\"\\w+\", gold.lower()))\n        if not pred_toks or not gold_toks:\n            continue\n        common = pred_toks & gold_toks\n        if not common:\n            continue\n        p = len(common) / len(pred_toks)\n        r = len(common) / len(gold_toks)\n        f1 = 2 * p * r / (p + r)\n        best = max(best, f1)\n    return best\n\n# ── Method A: Cosine similarity ──────────────────────────────────────────────\n_embedder = None\n\ndef get_embedder():\n    global _embedder\n    if _embedder is None:\n        from sentence_transformers import SentenceTransformer\n        logger.info(\"Loading sentence-transformer (all-MiniLM-L6-v2)...\")\n        _embedder = SentenceTransformer(\"all-MiniLM-L6-v2\")\n    return _embedder\n\ndef cosine_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:\n    emb = get_embedder()\n    texts = [s[\"text\"][:512] for s in sections]\n    q_emb = emb.encode([query], normalize_embeddings=True)\n    s_embs = emb.encode(texts, normalize_embeddings=True, show_progress_bar=False)\n    scores = (s_embs @ q_emb.T).flatten()\n    top_idx = np.argsort(scores)[::-1][:k]\n    return [{\"section\": sections[i], \"score\": float(scores[i])} for i in top_idx]\n\n# ── Method B: BM25 ──────────────────────────────────────────────────────────\ndef bm25_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:\n    from rank_bm25 import BM25Okapi\n    tokenized = [tokenize(s[\"text\"]) for s in sections]\n    bm25 = BM25Okapi(tokenized)\n    q_toks = tokenize(query)\n    scores = bm25.get_scores(q_toks)\n    top_idx = np.argsort(scores)[::-1][:k]\n    return [{\"section\": sections[i], \"score\": float(scores[i])} for i in top_idx]\n\n# ── Method C: TF-ISF ────────────────────────────────────────────────────────\ndef tf_isf_retrieve(query: str, sections: list[dict], k: int = TOP_K) -> list[dict]:\n    \"\"\"TF-ISF: IDF computed within document sections (not across corpus).\"\"\"\n    n_sections = len(sections)\n    if n_sections == 0:\n        return []\n\n    # Tokenize all sections\n    tok_sections = [tokenize(s[\"text\"]) for s in sections]\n\n    # Compute SF(t): how many sections contain term t\n    sf: dict[str, int] = defaultdict(int)\n    for toks in tok_sections:\n        for t in set(toks):\n            sf[t] += 1\n\n    # Compute ISF(t) = log(N / (1 + SF(t)))\n    def isf(t: str) -> float:\n        return math.log(n_sections / (1 + sf.get(t, 0)))\n\n    # Score each section\n    q_toks = tokenize(query)\n    if not q_toks:\n        return [{\"section\": sections[i], \"score\": 0.0} for i in range(min(k, n_sections))]\n\n    scores = []\n    for toks in tok_sections:\n        if not toks:\n            scores.append(0.0)\n            continue\n        tf_map: dict[str, float] = defaultdict(float)\n        for t in toks:\n            tf_map[t] += 1.0 / len(toks)\n        score = sum(tf_map.get(t, 0.0) * isf(t) for t in q_toks)\n        scores.append(score)\n\n    scores_arr = np.array(scores)\n    top_idx = np.argsort(scores_arr)[::-1][:k]\n    return [{\"section\": sections[i], \"score\": float(scores_arr[i])} for i in top_idx]\n\n# ── Context builder ──────────────────────────────────────────────────────────\ndef build_context(retrieved: list[dict], max_chars: int = MAX_CONTEXT_TOKENS * 4) -> str:\n    parts = []\n    total = 0\n    for item in retrieved:\n        name = item[\"section\"][\"name\"]\n        text = item[\"section\"][\"text\"]\n        chunk = f\"[{name}]\\n{text}\\n\\n\"\n        if total + len(chunk) > max_chars:\n            remaining = max_chars - total\n            if remaining > 100:\n                parts.append(chunk[:remaining])\n            break\n        parts.append(chunk)\n        total += len(chunk)\n    return \"\".join(parts).strip()\n\n# ── Section recall ───────────────────────────────────────────────────────────\ndef section_recall(retrieved: list[dict], evidence: list[str]) -> float:\n    if not evidence:\n        return float(\"nan\")\n    ev_set = set(e.lower()[:100] for e in evidence)\n    ret_set = set(r[\"section\"][\"text\"].lower()[:100] for r in retrieved)\n    hits = sum(1 for e in ev_set if any(e in r or r in e for r in ret_set))\n    return hits / len(ev_set)\n\n# ── Checkpoint helpers ────────────────────────────────────────────────────────\nCKPT_PATH = WORKSPACE / \"checkpoint.jsonl\"\n\ndef load_checkpoint() -> list[dict]:\n    \"\"\"Load previously processed examples from checkpoint.\"\"\"\n    if not CKPT_PATH.exists():\n        return []\n    examples = []\n    for line in CKPT_PATH.read_text().splitlines():\n        line = line.strip()\n        if line:\n            try:\n                examples.append(json.loads(line))\n            except json.JSONDecodeError:\n                pass\n    logger.info(f\"Resumed from checkpoint: {len(examples)} examples already done\")\n    return examples\n\ndef save_checkpoint(example: dict) -> None:\n    with open(CKPT_PATH, \"a\") as f:\n        f.write(json.dumps(example, ensure_ascii=False) + \"\\n\")\n\n# ── Main ─────────────────────────────────────────────────────────────────────\n@logger.catch(reraise=True)\ndef main():\n    n_questions = int(os.getenv(\"MAX_QUESTIONS\", str(MAX_QUESTIONS)))\n    logger.info(f\"Starting TF-ISF vs Cosine vs BM25 benchmark (max {n_questions} questions)\")\n\n    records = load_qasper(n_questions)\n    if not records:\n        raise RuntimeError(\"No QASPER records loaded\")\n\n    # Load checkpoint — skip already-done questions\n    done_examples = load_checkpoint()\n    done_count = len(done_examples)\n\n    # Pre-load embedder once\n    get_embedder()\n\n    results_cosine = []\n    results_bm25 = []\n    results_tfisf = []\n\n    total_cost = 0.0\n    api_calls = 0\n    per_method_data = {\"cosine\": [], \"bm25\": [], \"tf_isf\": []}\n    examples_out = list(done_examples)\n\n    # Rebuild per_method_data from checkpoint\n    for ex in done_examples:\n        f1_c = float(ex.get(\"metadata_f1_cosine\", 0))\n        f1_b = float(ex.get(\"metadata_f1_bm25\", 0))\n        f1_t = float(ex.get(\"metadata_f1_tf_isf\", 0))\n        sr_c = float(ex.get(\"metadata_section_recall_cosine\", -1))\n        sr_b = float(ex.get(\"metadata_section_recall_bm25\", -1))\n        sr_t = float(ex.get(\"metadata_section_recall_tf_isf\", -1))\n        stype = ex.get(\"metadata_gold_section_type\", \"Unknown\")\n        results_cosine.append(f1_c)\n        results_bm25.append(f1_b)\n        results_tfisf.append(f1_t)\n        per_method_data[\"cosine\"].append({\"f1\": f1_c, \"section_recall\": sr_c if sr_c >= 0 else float(\"nan\"), \"section_type\": stype})\n        per_method_data[\"bm25\"].append({\"f1\": f1_b, \"section_recall\": sr_b if sr_b >= 0 else float(\"nan\"), \"section_type\": stype})\n        per_method_data[\"tf_isf\"].append({\"f1\": f1_t, \"section_recall\": sr_t if sr_t >= 0 else float(\"nan\"), \"section_type\": stype})\n\n    for i, rec in enumerate(records):\n        if i < done_count:\n            continue  # already processed\n        if total_cost >= BUDGET_LIMIT_USD:\n            logger.warning(f\"Budget limit ${BUDGET_LIMIT_USD} reached at q={i}\")\n            break\n\n        q = rec[\"question\"]\n        sections = rec[\"sections\"]\n        gold_answers = rec[\"gold_answers\"]\n        evidence = rec[\"evidence_sections\"]\n\n        if not sections:\n            logger.debug(f\"q={i} no sections, skip\")\n            continue\n\n        try:\n            ret_cosine = cosine_retrieve(q, sections)\n            ret_bm25 = bm25_retrieve(q, sections)\n            ret_tfisf = tf_isf_retrieve(q, sections)\n        except Exception:\n            logger.error(f\"Retrieval failed on q={i}\")\n            continue\n\n        # Section recall\n        sc_cosine = section_recall(ret_cosine, evidence)\n        sc_bm25 = section_recall(ret_bm25, evidence)\n        sc_tfisf = section_recall(ret_tfisf, evidence)\n\n        # Build contexts\n        ctx_cosine = build_context(ret_cosine)\n        ctx_bm25 = build_context(ret_bm25)\n        ctx_tfisf = build_context(ret_tfisf)\n\n        # LLM answer generation for all 3 contexts\n        def make_prompt(ctx: str) -> str:\n            return (\n                f\"Answer the following question using only the provided context. \"\n                f\"Be concise (1-2 sentences).\\n\\n\"\n                f\"Question: {q}\\n\\nContext:\\n{ctx}\\n\\nAnswer:\"\n            )\n\n        ans_cosine = ans_bm25 = ans_tfisf = \"\"\n        try:\n            ans_cosine, c1 = llm_call(make_prompt(ctx_cosine))\n            total_cost += c1; api_calls += 1\n            ans_bm25, c2 = llm_call(make_prompt(ctx_bm25))\n            total_cost += c2; api_calls += 1\n            ans_tfisf, c3 = llm_call(make_prompt(ctx_tfisf))\n            total_cost += c3; api_calls += 1\n        except Exception:\n            logger.error(f\"LLM call failed on q={i}\")\n\n        # F1 scores\n        f1_cosine = token_f1(ans_cosine, gold_answers) if ans_cosine else 0.0\n        f1_bm25 = token_f1(ans_bm25, gold_answers) if ans_bm25 else 0.0\n        f1_tfisf = token_f1(ans_tfisf, gold_answers) if ans_tfisf else 0.0\n\n        results_cosine.append(f1_cosine)\n        results_bm25.append(f1_bm25)\n        results_tfisf.append(f1_tfisf)\n\n        # Section type from first evidence section name\n        gold_section_type = \"Unknown\"\n        if evidence:\n            ev_text = evidence[0].lower()\n            for stype in [\"abstract\", \"introduction\", \"method\", \"result\", \"discussion\", \"conclusion\", \"related\"]:\n                if stype in ev_text:\n                    gold_section_type = stype.capitalize()\n                    break\n\n        per_method_data[\"cosine\"].append({\"f1\": f1_cosine, \"section_recall\": sc_cosine, \"section_type\": gold_section_type})\n        per_method_data[\"bm25\"].append({\"f1\": f1_bm25, \"section_recall\": sc_bm25, \"section_type\": gold_section_type})\n        per_method_data[\"tf_isf\"].append({\"f1\": f1_tfisf, \"section_recall\": sc_tfisf, \"section_type\": gold_section_type})\n\n        # Build exp_gen_sol_out example\n        gold_str = gold_answers[0] if gold_answers else \"\"\n        examples_out.append({\n            \"input\": q,\n            \"output\": gold_str,\n            \"predict_cosine_answer\": ans_cosine,\n            \"predict_bm25_answer\": ans_bm25,\n            \"predict_tf_isf_answer\": ans_tfisf,\n            \"metadata_paper_id\": rec[\"paper_id\"],\n            \"metadata_f1_cosine\": str(round(f1_cosine, 4)),\n            \"metadata_f1_bm25\": str(round(f1_bm25, 4)),\n            \"metadata_f1_tf_isf\": str(round(f1_tfisf, 4)),\n            \"metadata_section_recall_cosine\": str(round(sc_cosine, 4) if not math.isnan(sc_cosine) else -1),\n            \"metadata_section_recall_bm25\": str(round(sc_bm25, 4) if not math.isnan(sc_bm25) else -1),\n            \"metadata_section_recall_tf_isf\": str(round(sc_tfisf, 4) if not math.isnan(sc_tfisf) else -1),\n            \"metadata_gold_section_type\": gold_section_type,\n            \"metadata_retrieved_sections_cosine\": str([r[\"section\"][\"name\"] for r in ret_cosine]),\n            \"metadata_retrieved_sections_bm25\": str([r[\"section\"][\"name\"] for r in ret_bm25]),\n            \"metadata_retrieved_sections_tf_isf\": str([r[\"section\"][\"name\"] for r in ret_tfisf]),\n        })\n\n        save_checkpoint(examples_out[-1])\n\n        if (i + 1) % 20 == 0:\n            n = len(results_cosine)\n            logger.info(\n                f\"q={i+1}/{n_questions} | cost=${total_cost:.3f} | \"\n                f\"F1 cos={np.mean(results_cosine):.3f} bm25={np.mean(results_bm25):.3f} tfisf={np.mean(results_tfisf):.3f}\"\n            )\n\n        del ret_cosine, ret_bm25, ret_tfisf, ctx_cosine, ctx_bm25, ctx_tfisf\n        gc.collect()\n\n    # ── Aggregate metrics ────────────────────────────────────────────────────\n    def agg_method(name: str) -> dict:\n        data = per_method_data[name]\n        f1s = [d[\"f1\"] for d in data]\n        srs = [d[\"section_recall\"] for d in data if not math.isnan(d[\"section_recall\"])]\n\n        by_type: dict[str, list] = defaultdict(list)\n        by_type_sr: dict[str, list] = defaultdict(list)\n        for d in data:\n            by_type[d[\"section_type\"]].append(d[\"f1\"])\n            if not math.isnan(d[\"section_recall\"]):\n                by_type_sr[d[\"section_type\"]].append(d[\"section_recall\"])\n\n        return {\n            \"name\": name,\n            \"mean_f1\": float(np.mean(f1s)) if f1s else 0.0,\n            \"std_f1\": float(np.std(f1s)) if f1s else 0.0,\n            \"mean_section_recall\": float(np.mean(srs)) if srs else 0.0,\n            \"section_recall_by_type\": {k: float(np.mean(v)) for k, v in by_type_sr.items()},\n            \"f1_by_type\": {k: float(np.mean(v)) for k, v in by_type.items()},\n            \"n\": len(f1s),\n        }\n\n    m_cos = agg_method(\"cosine\")\n    m_bm25 = agg_method(\"bm25\")\n    m_tfisf = agg_method(\"tf_isf\")\n\n    ranked = sorted([m_cos, m_bm25, m_tfisf], key=lambda x: x[\"mean_f1\"], reverse=True)\n\n    def find_winning_types() -> list[str]:\n        wins = []\n        for stype in set(m_tfisf[\"f1_by_type\"]) | set(m_cos[\"f1_by_type\"]):\n            tf = m_tfisf[\"f1_by_type\"].get(stype, 0)\n            co = m_cos[\"f1_by_type\"].get(stype, 0)\n            if tf > co:\n                wins.append(stype)\n        return wins\n\n    result_summary = {\n        \"dataset\": \"QASPER\",\n        \"n_questions\": len(examples_out),\n        \"methods\": [m_cos, m_bm25, m_tfisf],\n        \"comparison\": {\n            \"tf_isf_vs_cosine_f1_delta\": round(m_tfisf[\"mean_f1\"] - m_cos[\"mean_f1\"], 4),\n            \"tf_isf_vs_cosine_section_recall_delta\": round(\n                m_tfisf[\"mean_section_recall\"] - m_cos[\"mean_section_recall\"], 4\n            ),\n            \"methods_ranked_by_f1\": [r[\"name\"] for r in ranked],\n        },\n        \"analysis\": {\n            \"key_finding\": (\n                f\"TF-ISF F1={m_tfisf['mean_f1']:.3f} vs Cosine F1={m_cos['mean_f1']:.3f} \"\n                f\"vs BM25 F1={m_bm25['mean_f1']:.3f}. \"\n                f\"Best method: {ranked[0]['name']}.\"\n            ),\n            \"subgroups_where_tf_isf_wins\": find_winning_types(),\n            \"api_cost_spent\": round(total_cost, 4),\n            \"api_calls_made\": api_calls,\n        },\n    }\n\n    logger.info(f\"Results: {json.dumps(result_summary['comparison'], indent=2)}\")\n    logger.info(f\"Key finding: {result_summary['analysis']['key_finding']}\")\n\n    # ── Save outputs ─────────────────────────────────────────────────────────\n    # method_out.json: exp_gen_sol_out schema\n    method_out = {\n        \"metadata\": {\n            \"method_name\": \"TF-ISF vs Cosine vs BM25 Section Retrieval\",\n            \"description\": \"Compares three retrieval methods on QASPER scientific QA\",\n            \"llm_model\": LLM_MODEL,\n            \"top_k\": TOP_K,\n            \"n_questions\": len(examples_out),\n            \"results_summary\": result_summary,\n        },\n        \"datasets\": [\n            {\n                \"dataset\": \"QASPER\",\n                \"examples\": examples_out,\n            }\n        ],\n    }\n\n    out_path = WORKSPACE / \"method_out.json\"\n    out_path.write_text(json.dumps(method_out, indent=2, ensure_ascii=False))\n    logger.info(f\"Saved method_out.json with {len(examples_out)} examples\")\n\n    # Also save standalone results for easy inspection\n    results_path = WORKSPACE / \"results_summary.json\"\n    results_path.write_text(json.dumps(result_summary, indent=2, ensure_ascii=False))\n    logger.info(f\"Saved results_summary.json\")\n\n    # Print summary table\n    logger.info(\"=\" * 60)\n    logger.info(f\"{'Method':<20} {'F1 mean':>10} {'F1 std':>10} {'Sec Recall':>12}\")\n    logger.info(\"-\" * 60)\n    for m in [m_cos, m_bm25, m_tfisf]:\n        logger.info(f\"{m['name']:<20} {m['mean_f1']:>10.4f} {m['std_f1']:>10.4f} {m['mean_section_recall']:>12.4f}\")\n    logger.info(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 567, "startLine": 1, "totalLines": 567}}
```

### [9] ASSISTANT · 2026-07-20 11:40:31 UTC

```
Now I have enough to write a thorough review. Let me identify the key issues:

1. **Critical discrepancy**: Experiment artifact (art_E7rG9mK6gbrb) says "Hypothesis CONFIRMED" (TF-ISF F1=0.221 > Cosine F1=0.206, n=180, free model tencent/hy3:free), but the evaluation artifact (art_r9whYzfM2OVO) says "DISCONFIRMED" (TF-ISF F1=0.187 < Cosine F1=0.198, n=200, llama-3.2-3b). The paper reports only the negative result without acknowledging the conflicting positive run.

2. **BM25 implementation mismatch**: Paper claims corpus-level IDF across 81,550 sections, but eval.py shows BM25 is instantiated per-paper with only that paper's sections — i.e., within-document BM25, not corpus-level.

3. **ISF diagnostic is computed only on a subset**: `compute_isf_diagnostics` filters to records where gold sections are Methods/Results only — not disclosed in the paper.

4. **Wrong reference [6]**: Cited as "hierarchical attention over paper sections" but the entry is SPECTER (citation-informed document representations) — a completely different work.

5. **TF normalization discrepancy**: Paper says "raw term frequency" but code uses frequency normalized by section length.
```

### [10] TOOL CALL — Write · 2026-07-20 11:40:31 UTC

```
File: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/review_paper/review_paper/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This paper presents a negative result: TF-ISF (Inverse Section Frequency applied within a single document) does not improve section retrieval over cosine similarity or BM25 on QASPER. The hypothesis is clearly stated, the experiment is executed, and the disconfirmation is honestly reported. However, several critical issues prevent acceptance. First, a directly contradictory earlier experiment (art_E7rG9mK6gbrb) that confirmed the hypothesis is never disclosed — the paper selectively reports only the negative run, a form of HARKing in reverse (selecting the negative outcome for novelty framing). Second, the paper misrepresents the BM25 baseline as using corpus-level IDF across 81,550 sections, whereas the evaluation code constructs BM25 purely within each paper's own sections — the same locality constraint as TF-ISF. Third, the ISF diagnostic, which forms the mechanistic core of the disconfirmation argument, is computed on a non-representative subset (only records with Methods/Results gold sections) without disclosure. Fourth, a key citation is incorrectly attributed. Fifth, TF-ISF is a trivially obvious extension of TF-IDF — the novelty bar is very low even for a negative-result paper, which must compensate with methodological rigor. Taken together, these issues undermine the reliability of the reported findings and would require substantial revision.",
  "strengths": [
    "Clear hypothesis specification with a mechanistic prediction (evidence sections should have higher ISF), making the disconfirmation falsifiable and informative.",
    "Inclusion of an ISF diagnostic section that attempts to explain why the method failed, going beyond a simple 'it didn't work' result.",
    "Appropriate use of paired t-tests with Holm-Bonferroni correction and bootstrap confidence intervals.",
    "Honest acknowledgment of limitations (sample size, single dataset, single reader model, retrieval granularity).",
    "The negative result, if methodologically clean, would be a useful boundary condition for the retrieval community — such results are underrepresented in the literature."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 1,
      "justification": "Multiple technical errors compromise the soundness. (1) The BM25 baseline is described as corpus-level but implemented as within-document — this directly distorts the comparison between methods. (2) The ISF diagnostic is computed on a filtered subset but reported as if it covers all sections. (3) A contradictory experiment (art_E7rG9mK6gbrb, n=180, different LLM, result=CONFIRMED) exists in the supplementary materials but is never discussed; the paper presents only one of two runs with opposite conclusions. (4) TF specification ('raw term frequency') contradicts the code (length-normalized TF). These are not minor errors.",
      "improvements": [
        "Fix or disclose the BM25 implementation: either implement true corpus-level BM25 (IDF computed across all 289 papers) or explicitly state that BM25 here is also within-document, and adjust all comparisons accordingly.",
        "Disclose that the ISF diagnostic is computed on the Methods/Results-gold subset only; re-run on all records and report any difference.",
        "Add a section or appendix discussing the contradictory experiment run (art_E7rG9mK6gbrb) — what changed (n, LLM model, data loading path, evidence matching), which result is trustworthy, and why. Sweeping a positive run under the rug to present a clean negative narrative is a methodological integrity issue.",
        "Correct the TF description: 'length-normalized term frequency' not 'raw term frequency.'"
      ]
    },
    {
      "dimension": "presentation",
      "score": 2,
      "justification": "The paper is well-written and clearly organized. The IMRaD structure, the ISF formula, and the diagnostic tables are presented clearly. However, reference [6] is factually wrong (SPECTER is cited as a 'hierarchical attention over paper sections' paper when it is about citation-informed document-level representations — a completely different contribution), and the mismatch between the described BM25 setup (corpus-level, 81,550 sections) and the actual implementation (within-document) would mislead any reader who does not check the code.",
      "improvements": [
        "Replace reference [6] with the correct citation for hierarchical attention over scientific paper sections (e.g., Cohan et al. 2019 'A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents', or Lo et al. work on section-aware scientific NLP).",
        "Correct the BM25 description to match the actual implementation.",
        "Add a comparison table that explicitly shows: for each method, whether IDF/ISF is within-document or cross-corpus, so readers can interpret the comparisons correctly."
      ]
    },
    {
      "dimension": "contribution",
      "score": 1,
      "justification": "TF-ISF is a one-line modification of TF-IDF applied within a document rather than across a corpus. The idea is obvious enough that it would likely occur to any IR practitioner as a first step. A negative result on such a simple method is only publishable if it is methodologically impeccable and provides clear guidance about why it fails. The current paper falls short on both: the methodology has critical errors (BM25 mismatch, selective result reporting) and the mechanistic explanation (ISF by section type) is based on a filtered diagnostic. The future directions listed are generic and not grounded in the specific failure mechanism uncovered.",
      "improvements": [
        "Strengthen the contribution by running TF-ISF against a properly implemented corpus-level BM25 baseline (which the paper claims to use but does not).",
        "Provide a fine-grained ablation: vary k (top-1, top-3, top-5), vary section granularity (paragraph vs. section), and test on a second dataset (e.g., QASPER test split or a biomedical QA dataset) to show the finding generalizes.",
        "Make the mechanistic explanation more rigorous: compute inter-section vocabulary overlap (Jaccard) by section type pair across the corpus, which would directly test whether Methods/Results vocabulary is shared with other sections.",
        "Frame the contribution more precisely: given that both BM25 and TF-ISF are within-document here, the paper's actual finding is that 'within-document sparse term weighting, whether corpus-calibrated (BM25 approximation) or document-local (TF-ISF), does not outperform dense cosine similarity for section retrieval in scientific QA.'"
      ]
    }
  ],
  "critiques": [
    {
      "category": "evidence",
      "severity": "major",
      "description": "Contradictory experiment result is not disclosed. The supplementary artifact art_E7rG9mK6gbrb contains a prior experiment run (method.py, n=180, LLM=tencent/hy3:free) whose summary explicitly states 'Hypothesis CONFIRMED: TF-ISF outperforms cosine on answer F1' with TF-ISF F1=0.221 vs Cosine F1=0.206. The paper reports only the evaluation run (art_r9whYzfM2OVO, n=200, LLM=llama-3.2-3b-instruct) which shows TF-ISF F1=0.187 vs Cosine F1=0.198 (DISCONFIRMED). These two runs used different LLMs, different data loading paths (local JSON vs HuggingFace), different evidence matching strategies, and slightly different n. Reporting only the negative run to frame a clean negative-result narrative — when an earlier positive run exists in the same artifact set — is a serious methodological integrity issue, regardless of which run is more trustworthy.",
      "suggested_action": "Add a dedicated section or appendix that presents both runs side by side, explains all differences in setup (LLM, n, data source, evidence matching, tokenization), argues which is more reliable and why, and acknowledges that the conclusion depends on this methodological choice. If the evaluation run (n=200) is preferred, explain why the experiment run (n=180) produced different results — likely the different LLM and evidence matching strategy."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The BM25 baseline is described as corpus-level ('IDF computed over all 81,550 sections across 289 papers in the QASPER dataset') but eval.py instantiates BM25Okapi per-question using only the target paper's sections. This makes BM25 a within-document sparse ranker, the same locality constraint as TF-ISF. The claimed differentiator between BM25 and TF-ISF — corpus-level vs. document-local IDF — does not exist in the implementation. This undermines the comparison and the paper's conclusion that TF-ISF adds nothing over BM25.",
      "suggested_action": "Either (a) implement true corpus-level BM25 by building an index over all 81,550 sections before evaluation and querying it to retrieve from the target paper's sections, or (b) explicitly state that the BM25 baseline is also within-document (i.e., both methods compute IDF locally), and rewrite the comparison accordingly. Option (a) is preferable as it provides a more informative baseline."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "The ISF diagnostic — the mechanistic evidence that Methods/Results have lower ISF than Introduction, which drives the core disconfirmation explanation — is computed only on the subset of records where gold sections are Methods or Results (compute_isf_diagnostics filters: 'if not any(t in rec[\"gold_section_types\"] for t in [\"Methods\", \"Results\"]): continue'). This subset is not disclosed in the paper, which presents the ISF values as if they describe all papers. Computing ISF means only on papers already filtered to have Methods/Results gold answers may introduce selection bias.",
      "suggested_action": "Re-run the ISF diagnostic on all 200 records (remove the gold-section-type filter). Report whether the ISF ordering (Introduction > Methods/Results) holds across all papers, not just the Methods/Results-gold subset. Disclose the filtering in the paper regardless."
    },
    {
      "category": "clarity",
      "severity": "major",
      "description": "Reference [6] is factually wrong. The paper states 'Cohan et al. [6] explored hierarchical attention over paper sections, but did not isolate the effect of term frequency on ranking.' Reference [6] in the bibliography is 'SPECTER: Document-level Representation Learning using Citation-informed Transformers' — this paper is about learning document embeddings from citation signals, not hierarchical attention over sections. The described claim does not match the cited paper.",
      "suggested_action": "Replace reference [6] with the correct citation. For hierarchical attention over paper sections, the relevant work includes Cohan et al. 2018 'A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents' (NAACL 2018) or relevant section-aware scientific NLP work. Verify all other citations are correctly attributed."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "The paper describes TF(t,s) as 'raw term frequency' but the code (both eval.py and method.py) uses length-normalized TF: tf[t] = count / len(section_tokens). This is a standard normalization but the formula and text description should match the implementation.",
      "suggested_action": "Update the formula and description to say 'length-normalized term frequency' and revise the TF-ISF formula to include the normalization explicitly: TF(t, s) = count(t, s) / |s|."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "The n=200 sample is drawn from the first 200 questions encountered in the QASPER train+validation split (in order), which may not be representative. QASPER has ~2,593 QA pairs; using only 200 (7.7%) risks sampling bias, especially since the code breaks at n_max without any stratification.",
      "suggested_action": "Sample 200 examples with stratification by paper and by gold-section type (ensure proportional representation of Methods/Results gold sections). Alternatively, run on the full validation split (~900 examples) to improve statistical power. Report which split was used and how examples were selected."
    },
    {
      "category": "novelty",
      "severity": "minor",
      "description": "The TF-ISF method is a trivially obvious extension of TF-IDF. Within-document IDF has been considered in the literature (e.g., Singhal et al. 1996, Hiemstra 1998 language models, and various field-weighted retrieval schemes). The paper does not cite any prior work on within-document term weighting, which means the novelty claim rests on an incomplete literature review.",
      "suggested_action": "Search for prior work on within-document IDF, field-weighted retrieval (e.g., BM25F), and section-aware term weighting. Cite and differentiate from any relevant prior work. If within-document IDF has been studied before in other domains, the novelty claim must be scoped accordingly."
    },
    {
      "category": "evidence",
      "severity": "minor",
      "description": "The subgroup sizes are very small: Abstract/Introduction n=31, Discussion/Conclusion n=12. With such small groups, the subgroup F1 comparisons have very wide confidence intervals and essentially no statistical power. Yet the paper reports these comparisons as if they are informative (e.g., 'TF-ISF significantly underperforms on this small group' for Discussion/Conclusion).",
      "suggested_action": "Add per-subgroup confidence intervals to the Results table. Remove claims of 'significant' underperformance for groups with n<20. Instead, describe these as 'directional observations with insufficient power to draw conclusions' and focus interpretation on the Methods/Results subgroup (n=137) which is adequately powered."
    }
  ],
  "score": 3,
  "confidence": 4
}
```

### [11] TOOL RESULT — Write · 2026-07-20 11:40:31 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_1/review_paper/review_paper/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This paper presents a negative result: TF-ISF (Inverse Section Frequency applied within a single document) does not improve section retrieval over cosine similarity or BM25 on QASPER. The hypothesis is clearly stated, the experiment is executed, and the disconfirmation is honestly reported. However, several critical issues prevent acceptance. First, a directly contradictory earlier experiment (art_E7rG9mK6gbrb) that confirmed the hypothesis is never disclosed — the paper selectively reports only the negative run, a form of HARKing in reverse (selecting the negative outcome for novelty framing). Second, the paper misrepresents the BM25 baseline as using corpus-level IDF across 81,550 sections, whereas the evaluation code constructs BM25 purely within each paper's own sections — the same locality constraint as TF-ISF. Third, the ISF diagnostic, which forms the mechanistic core of the disconfirmation argument, is computed on a non-representative subset (only records with Methods/Results gold sections) without disclosure. Fourth, a key citation is incorrectly attributed. Fifth, TF-ISF is a trivially obvious extension of TF-IDF — the novelty bar is very low even for a negative-result paper, which must compensate with methodological rigor. Taken together, these issues undermine the reliability of the reported findings and would require substantial revision.\",\n  \"strengths\": [\n    \"Clear hypothesis specification with a mechanistic prediction (evidence sections should have higher ISF), making the disconfirmation falsifiable and informative.\",\n    \"Inclusion of an ISF diagnostic section that attempts to explain why the method failed, going beyond a simple 'it didn't work' result.\",\n    \"Appropriate use of paired t-tests with Holm-Bonferroni correction and bootstrap confidence intervals.\",\n    \"Honest acknowledgment of limitations (sample size, single dataset, single reader model, retrieval granularity).\",\n    \"The negative result, if methodologically clean, would be a useful boundary condition for the retrieval community — such results are underrepresented in the literature.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 1,\n      \"justification\": \"Multiple technical errors compromise the soundness. (1) The BM25 baseline is described as corpus-level but implemented as within-document — this directly distorts the comparison between methods. (2) The ISF diagnostic is computed on a filtered subset but reported as if it covers all sections. (3) A contradictory experiment (art_E7rG9mK6gbrb, n=180, different LLM, result=CONFIRMED) exists in the supplementary materials but is never discussed; the paper presents only one of two runs with opposite conclusions. (4) TF specification ('raw term frequency') contradicts the code (length-normalized TF). These are not minor errors.\",\n      \"improvements\": [\n        \"Fix or disclose the BM25 implementation: either implement true corpus-level BM25 (IDF computed across all 289 papers) or explicitly state that BM25 here is also within-document, and adjust all comparisons accordingly.\",\n        \"Disclose that the ISF diagnostic is computed on the Methods/Results-gold subset only; re-run on all records and report any difference.\",\n        \"Add a section or appendix discussing the contradictory experiment run (art_E7rG9mK6gbrb) — what changed (n, LLM model, data loading path, evidence matching), which result is trustworthy, and why. Sweeping a positive run under the rug to present a clean negative narrative is a methodological integrity issue.\",\n        \"Correct the TF description: 'length-normalized term frequency' not 'raw term frequency.'\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 2,\n      \"justification\": \"The paper is well-written and clearly organized. The IMRaD structure, the ISF formula, and the diagnostic tables are presented clearly. However, reference [6] is factually wrong (SPECTER is cited as a 'hierarchical attention over paper sections' paper when it is about citation-informed document-level representations — a completely different contribution), and the mismatch between the described BM25 setup (corpus-level, 81,550 sections) and the actual implementation (within-document) would mislead any reader who does not check the code.\",\n      \"improvements\": [\n        \"Replace reference [6] with the correct citation for hierarchical attention over scientific paper sections (e.g., Cohan et al. 2019 'A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents', or Lo et al. work on section-aware scientific NLP).\",\n        \"Correct the BM25 description to match the actual implementation.\",\n        \"Add a comparison table that explicitly shows: for each method, whether IDF/ISF is within-document or cross-corpus, so readers can interpret the comparisons correctly.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 1,\n      \"justification\": \"TF-ISF is a one-line modification of TF-IDF applied within a document rather than across a corpus. The idea is obvious enough that it would likely occur to any IR practitioner as a first step. A negative result on such a simple method is only publishable if it is methodologically impeccable and provides clear guidance about why it fails. The current paper falls short on both: the methodology has critical errors (BM25 mismatch, selective result reporting) and the mechanistic explanation (ISF by section type) is based on a filtered diagnostic. The future directions listed are generic and not grounded in the specific failure mechanism uncovered.\",\n      \"improvements\": [\n        \"Strengthen the contribution by running TF-ISF against a properly implemented corpus-level BM25 baseline (which the paper claims to use but does not).\",\n        \"Provide a fine-grained ablation: vary k (top-1, top-3, top-5), vary section granularity (paragraph vs. section), and test on a second dataset (e.g., QASPER test split or a biomedical QA dataset) to show the finding generalizes.\",\n        \"Make the mechanistic explanation more rigorous: compute inter-section vocabulary overlap (Jaccard) by section type pair across the corpus, which would directly test whether Methods/Results vocabulary is shared with other sections.\",\n        \"Frame the contribution more precisely: given that both BM25 and TF-ISF are within-document here, the paper's actual finding is that 'within-document sparse term weighting, whether corpus-calibrated (BM25 approximation) or document-local (TF-ISF), does not outperform dense cosine similarity for section retrieval in scientific QA.'\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"Contradictory experiment result is not disclosed. The supplementary artifact art_E7rG9mK6gbrb contains a prior experiment run (method.py, n=180, LLM=tencent/hy3:free) whose summary explicitly states 'Hypothesis CONFIRMED: TF-ISF outperforms cosine on answer F1' with TF-ISF F1=0.221 vs Cosine F1=0.206. The paper reports only the evaluation run (art_r9whYzfM2OVO, n=200, LLM=llama-3.2-3b-instruct) which shows TF-ISF F1=0.187 vs Cosine F1=0.198 (DISCONFIRMED). These two runs used different LLMs, different data loading paths (local JSON vs HuggingFace), different evidence matching strategies, and slightly different n. Reporting only the negative run to frame a clean negative-result narrative — when an earlier positive run exists in the same artifact set — is a serious methodological integrity issue, regardless of which run is more trustworthy.\",\n      \"suggested_action\": \"Add a dedicated section or appendix that presents both runs side by side, explains all differences in setup (LLM, n, data source, evidence matching, tokenization), argues which is more reliable and why, and acknowledges that the conclusion depends on this methodological choice. If the evaluation run (n=200) is preferred, explain why the experiment run (n=180) produced different results — likely the different LLM and evidence matching strategy.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The BM25 baseline is described as corpus-level ('IDF computed over all 81,550 sections across 289 papers in the QASPER dataset') but eval.py instantiates BM25Okapi per-question using only the target paper's sections. This makes BM25 a within-document sparse ranker, the same locality constraint as TF-ISF. The claimed differentiator between BM25 and TF-ISF — corpus-level vs. document-local IDF — does not exist in the implementation. This undermines the comparison and the paper's conclusion that TF-ISF adds nothing over BM25.\",\n      \"suggested_action\": \"Either (a) implement true corpus-level BM25 by building an index over all 81,550 sections before evaluation and querying it to retrieve from the target paper's sections, or (b) explicitly state that the BM25 baseline is also within-document (i.e., both methods compute IDF locally), and rewrite the comparison accordingly. Option (a) is preferable as it provides a more informative baseline.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The ISF diagnostic — the mechanistic evidence that Methods/Results have lower ISF than Introduction, which drives the core disconfirmation explanation — is computed only on the subset of records where gold sections are Methods or Results (compute_isf_diagnostics filters: 'if not any(t in rec[\\\"gold_section_types\\\"] for t in [\\\"Methods\\\", \\\"Results\\\"]): continue'). This subset is not disclosed in the paper, which presents the ISF values as if they describe all papers. Computing ISF means only on papers already filtered to have Methods/Results gold answers may introduce selection bias.\",\n      \"suggested_action\": \"Re-run the ISF diagnostic on all 200 records (remove the gold-section-type filter). Report whether the ISF ordering (Introduction > Methods/Results) holds across all papers, not just the Methods/Results-gold subset. Disclose the filtering in the paper regardless.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"major\",\n      \"description\": \"Reference [6] is factually wrong. The paper states 'Cohan et al. [6] explored hierarchical attention over paper sections, but did not isolate the effect of term frequency on ranking.' Reference [6] in the bibliography is 'SPECTER: Document-level Representation Learning using Citation-informed Transformers' — this paper is about learning document embeddings from citation signals, not hierarchical attention over sections. The described claim does not match the cited paper.\",\n      \"suggested_action\": \"Replace reference [6] with the correct citation. For hierarchical attention over paper sections, the relevant work includes Cohan et al. 2018 'A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents' (NAACL 2018) or relevant section-aware scientific NLP work. Verify all other citations are correctly attributed.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"The paper describes TF(t,s) as 'raw term frequency' but the code (both eval.py and method.py) uses length-normalized TF: tf[t] = count / len(section_tokens). This is a standard normalization but the formula and text description should match the implementation.\",\n      \"suggested_action\": \"Update the formula and description to say 'length-normalized term frequency' and revise the TF-ISF formula to include the normalization explicitly: TF(t, s) = count(t, s) / |s|.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The n=200 sample is drawn from the first 200 questions encountered in the QASPER train+validation split (in order), which may not be representative. QASPER has ~2,593 QA pairs; using only 200 (7.7%) risks sampling bias, especially since the code breaks at n_max without any stratification.\",\n      \"suggested_action\": \"Sample 200 examples with stratification by paper and by gold-section type (ensure proportional representation of Methods/Results gold sections). Alternatively, run on the full validation split (~900 examples) to improve statistical power. Report which split was used and how examples were selected.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"minor\",\n      \"description\": \"The TF-ISF method is a trivially obvious extension of TF-IDF. Within-document IDF has been considered in the literature (e.g., Singhal et al. 1996, Hiemstra 1998 language models, and various field-weighted retrieval schemes). The paper does not cite any prior work on within-document term weighting, which means the novelty claim rests on an incomplete literature review.\",\n      \"suggested_action\": \"Search for prior work on within-document IDF, field-weighted retrieval (e.g., BM25F), and section-aware term weighting. Cite and differentiate from any relevant prior work. If within-document IDF has been studied before in other domains, the novelty claim must be scoped accordingly.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The subgroup sizes are very small: Abstract/Introduction n=31, Discussion/Conclusion n=12. With such small groups, the subgroup F1 comparisons have very wide confidence intervals and essentially no statistical power. Yet the paper reports these comparisons as if they are informative (e.g., 'TF-ISF significantly underperforms on this small group' for Discussion/Conclusion).\",\n      \"suggested_action\": \"Add per-subgroup confidence intervals to the Results table. Remove claims of 'significant' underperformance for groups with n<20. Instead, describe these as 'directional observations with insufficient power to draw conclusions' and focus interpretation on the Methods/Results subgroup (n=137) which is adequately powered.\"\n    }\n  ],\n  \"score\": 3,\n  \"confidence\": 4\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [12] ASSISTANT · 2026-07-20 11:40:41 UTC

```
Review complete. Score: **3/10 (Reject)**.

Key findings that drove the low score:

1. **Selective result reporting (major)**: A prior experiment run in the supplementary materials (art_E7rG9mK6gbrb) shows the opposite conclusion — "Hypothesis CONFIRMED, TF-ISF F1=0.221 > Cosine F1=0.206" — using n=180 and a different LLM. The paper reports only the negative run without acknowledging this contradiction.

2. **BM25 implementation mismatch (major)**: The paper claims corpus-level BM25 IDF across 81,550 sections, but eval.py constructs BM25 per-paper using only that paper's own sections — making it a within-document method like TF-ISF, collapsing the key claimed distinction.

3. **ISF diagnostic on a filtered subset (major)**: The mechanistic explanation (Methods/Results have lower ISF than Introduction) is computed only on records where gold evidence is in Methods/Results — not disclosed and potentially biased.

4. **Wrong citation [6] (major)**: SPECTER (citation-informed document embeddings) is described as "hierarchical attention over paper sections."

The paper has a clear structure and honest negative-result framing, but the methodological errors and the undisclosed contradictory run are disqualifying without revision.
```
