# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 12:57:54 UTC

````
<system-prompt>
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

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
</system-prompt>

<prompt>
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
abstract: >-
  Locating evidence-bearing sections in scientific papers remains challenging for retrieval-augmented QA systems. Dense retrievers
  often rank claim-summarizing sections (Abstract, Introduction) higher than evidence-dense sections (Methods, Results), a
  bias hypothesized to stem from vocabulary stratification in the IMRaD convention. We propose TF-ISF (Term Frequency-Inverse
  Section Frequency), a document-local reweighting method that applies within-document inverse frequency to sections instead
  of cross-corpus inverse frequency. Evaluated on 200 QASPER examples, TF-ISF achieves F1=0.187, matching cosine similarity
  (F1=0.198) and BM25 (F1=0.179)—no significant differences (p > 0.37, Holm-corrected). Critically, the hypothesized mechanism
  fails: Methods and Results sections have lower ISF (1.23–1.24) than Introduction (1.34), indicating that evidence sections
  do not use more section-unique vocabulary. We also report a contradictory earlier experiment (n=180, different LLM) showing
  TF-ISF F1=0.221 (positive result), discuss methodological differences, and conclude that naive within-document term reweighting
  cannot rescue section retrieval in scientific QA. The contribution is a rigorous negative result identifying where term
  weighting approaches fail and motivating future work toward discourse-aware or embedding-based solutions.
paper_text: |
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

  To diagnose why TF-ISF underperformed, we computed mean ISF scores for all terms in each section type across the corpus \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-023b95-within-document-term-weighting-for-scien/tree/main/round-1/evaluation-1}}. A critical caveat: the ISF diagnostic was computed on records where the gold evidence section was Methods or Results (139 records), not all 200 records, which may introduce selection bias. We report this filtering transparently.

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

  An earlier experiment on 180 QASPER examples using the free-tier tencent/hy3 model reported different results \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-023b95-within-document-term-weighting-for-scien/tree/main/round-1/experiment-1}}:

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

  [18]  Evaluation code confirms BM25 instantiation per paper (within-document), not corpus-level.

  [19]  Full subgroup analysis with 95% bootstrap CIs for all subgroups.
summary: >-
  This paper investigates whether within-document Inverse Section Frequency (TF-ISF) can improve section retrieval in scientific
  papers by applying term-reweighting principles within single documents rather than across corpora. Evaluation on 200 QASPER
  examples finds TF-ISF achieves F1=0.187, matching cosine similarity (0.198) and BM25 (0.179)—no significant differences
  (p > 0.37). Critically, the hypothesized mechanism fails: Methods/Results sections have LOWER ISF (1.23–1.24) than Introduction
  (1.34), falsifying the assumption that evidence sections use more unique vocabulary. We also transparently report a contradictory
  earlier experiment (n=180, different LLM) showing positive results. The paper contributes a well-characterized negative
  result: naive within-document term reweighting cannot rescue section retrieval in scientific QA, and future work should
  target discourse-aware or embedding-based approaches rather than static reweighting heuristics.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig_method_overview
title: Retrieval Methods Compared
caption: >-
  Conceptual comparison of three retrieval methods. Cosine similarity ranks sections by embedding similarity to the query.
  BM25 applies probabilistic term weighting with within-document term statistics. TF-ISF applies inverse section frequency
  to down-weight terms shared across many sections and up-weight section-specific terms. All three operate on the same document-local
  scope.
image_gen_detailed_description: >-
  Flowchart with three parallel paths, each showing a query and paper being processed by a different method. Path 1 (Cosine):
  Query box → Embed query → Cosine similarity computation → Ranked sections. Path 2 (BM25): Query box → Tokenize → BM25 scoring
  → Ranked sections. Path 3 (TF-ISF): Query box → Tokenize → Compute per-section ISF → TF-ISF scoring → Ranked sections. All
  paths feed into a common box labeled 'Top-3G at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.

A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
</prompt> Sections' → 'LLM Reader' → 'Answer + F1'. Use clean sans-serif font, horizontal
  layout, light gray background, colored boxes (blue for cosine, orange for BM25, green for TF-ISF).
aspect_ratio: '21:9'
summary: >-
  Three retrieval methods operating on the same document: dense embeddings (cosine), probabilistic sparse ranking (BM25),
  and within-document term frequency (TF-ISF).
figure_path: figures/fig_method_overview_v0.jpg

--- Item 2 ---
id: fig_main_results
title: Retrieval Performance Comparison (n=200)
caption: >-
  Token-level F1 and section recall@3 for all three retrieval methods on 200 QASPER questions (llama-3.2-3b-instruct reader).
  Error bars show 95% bootstrap confidence intervals (10,000 resamples). All pairwise differences are non-significant (p >
  0.37, Holm-corrected). Cosine achieves the highest mean F1 (0.198) while BM25 achieves highest recall (0.525), but differences
  are within confidence interval overlap.
image_gen_detailed_description: >-
  Two side-by-side grouped bar charts. Left panel: Token F1 scores. X-axis: methods (Cosine, BM25, TF-ISF). Y-axis: F1 (0.0–0.30
  scale). Bar heights: Cosine 0.198, BM25 0.179, TF-ISF 0.187. Error bars (95% CI): Cosine [0.174, 0.223], BM25 [0.157, 0.202],
  TF-ISF [0.163, 0.213]. Right panel: Section Recall@3. X-axis: methods. Y-axis: Recall (0.0–1.0 scale). Bar heights: Cosine
  0.467, BM25 0.525, TF-ISF 0.484. Error bars: Cosine [0.403, 0.531], BM25 [0.462, 0.589], TF-ISF [0.418, 0.548]. Colors:
  Cosine blue, BM25 orange, TF-ISF green. Sans-serif font, white background, overlapping error bars indicate non-significance.
aspect_ratio: '21:9'
summary: >-
  All three methods achieve similar performance with overlapping confidence intervals, showing no significant differences
  in either F1 or recall.
figure_path: figures/fig_main_results_v0.jpg

--- Item 3 ---
id: fig_subgroup_analysis
title: Performance by Gold Evidence Section Type
caption: >-
  F1 performance stratified by the section type containing the gold answer. Methods/Results (n=137) is adequately powered;
  Abstract/Introduction (n=31) and Discussion/Conclusion (n=12) are underpowered for strong inference. TF-ISF does not outperform
  cosine in any subgroup. The Methods/Results subgroup, where TF-ISF was hypothesized to help most, shows no advantage (TF-ISF
  F1=0.201 vs. Cosine F1=0.208, overlapping CIs).
image_gen_detailed_description: >-
  Four grouped bar charts, one for each subgroup (Abstract/Intro, Methods/Results, Discussion/Conclusion, Other). Each chart
  shows three bars (Cosine, BM25, TF-ISF) with heights representing F1 and error bars showing 95% bootstrap CIs. Methods/Results
  subgroup (n=137) has narrower CIs; other subgroups have wider CIs. X-axis: methods. Y-axis: F1 (0.0–0.30 scale). Exact values:
  Abstract/Intro (Cosine 0.192 [0.136,0.253], BM25 0.170 [0.118,0.228], TF-ISF 0.158 [0.111,0.209]); Methods/Results (Cosine
  0.208 [0.178,0.239], BM25 0.185 [0.157,0.214], TF-ISF 0.201 [0.171,0.233]); Discussion/Conclusion (Cosine 0.192 [0.116,0.279],
  BM25 0.156 [0.102,0.211], TF-ISF 0.134 [0.081,0.190]); Other (Cosine 0.193 [0.152,0.235], BM25 0.181 [0.140,0.228], TF-ISF
  0.172 [0.132,0.218]). Use colors: Cosine blue, BM25 orange, TF-ISF green. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: >-
  TF-ISF does not outperform cosine in any subgroup, including Methods/Results where it was hypothesized to excel.
figure_path: figures/fig_subgroup_analysis_v0.jpg

--- Item 4 ---
id: fig_isf_analysis
title: Mean ISF by Section Type (Mechanism Diagnostic)
caption: >-
  Mean Inverse Section Frequency for all terms in each section type (computed on records where gold evidence is Methods/Results,
  n=139 records, potentially biased). Methods (1.227) and Results (1.243) have LOWER ISF than Introduction (1.335), contradicting
  the hypothesis that evidence sections contain more rare, section-specific vocabulary. This mechanism disconfirmation is
  a key finding.
image_gen_detailed_description: >-
  Horizontal bar chart. X-axis: Mean ISF (0.0–1.5 scale). Y-axis: Section types (Introduction, Methods, Results, Related Work,
  Conclusion, Discussion, Other). Bar lengths and values: Introduction 1.335, Methods 1.227, Results 1.243, Related Work 1.327,
  Conclusion 1.127, Discussion 1.247, Other 1.326. Color gradient: Introduction and Related Work (claim-dense sections) dark
  blue; Methods and Results (evidence-dense sections) red/orange to highlight the contradiction. Error bars or std dev: use
  light gray bands for std dev width. Add n-values as labels (e.g., 'n=839' for Methods). Sans-serif font, white background.
aspect_ratio: '21:9'
summary: >-
  Evidence sections (Methods/Results) have LOWER ISF than claim sections (Introduction), falsifying the hypothesis that evidence
  sections use more section-unique vocabulary.
figure_path: figures/fig_isf_analysis_v0.jpg

--- Item 5 ---
id: fig_contradiction_summary
title: Comparison of n=180 vs n=200 Runs
caption: >-
  Two runs with different LLMs and data loading strategies produced contradictory results. Earlier run (n=180, tencent/hy3:free)
  showed TF-ISF F1=0.221 > Cosine F1=0.206 (positive result); current run (n=200, llama-3.2-3b-instruct) shows TF-ISF F1=0.187
  < Cosine F1=0.198 (negative result). We argue the n=200 evaluation is more trustworthy due to larger sample, higher-quality
  LLM, and rigorous statistics, but the discrepancy highlights fragility in the approach.
image_gen_detailed_description: >-
  Side-by-side comparison table rendered as a figure. Left panel: 'Earlier Experiment (n=180, tencent/hy3:free)' with three
  bars (Cosine 0.206, BM25 0.213, TF-ISF 0.221) arranged horizontally, TF-ISF highest, highlighted in gold. Right panel: 'Current
  Evaluation (n=200, llama-3.2-3b-instruct)' with three bars (Cosine 0.198, BM25 0.179, TF-ISF 0.187), Cosine highest, highlighted.
  X-axis: F1 (0.15–0.25 scale). Y-axis: Methods. Add annotation: 'Result: CONFIRMED' for left, 'Result: DISCONFIRMED' for
  right. Use contrasting colors to emphasize contradiction. Add small text labels for LLM model and sample size. Sans-serif
  font.
aspect_ratio: '21:9'
summary: >-
  Contradictory results between two runs with different LLMs and data sources, highlighting fragility when LLM quality dominates
  variance.
figure_path: figures/fig_contradiction_summary_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PN
````

### [2] SKILL-INPUT — aii-paper-to-latex · 2026-07-20 12:58:00 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [3] SKILL-INPUT — aii-semscholar-bib · 2026-07-20 12:58:04 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
