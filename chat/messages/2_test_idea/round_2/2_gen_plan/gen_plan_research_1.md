# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-20 11:44:02 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_research_1
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
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

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

id: research_iter2_dir1
type: research
objective: >-
  Survey prior work on within-document term weighting, field-weighted retrieval, and section-aware ranking to establish novelty
  and cite relevant literature
approach: >-
  Search comprehensively for: (1) Within-document IDF or similar approaches (Singhal et al. 1996, Hiemstra 1998, probabilistic
  language models), (2) Field-weighted retrieval (BM25F, Zaragoza et al. 2004), (3) Section-aware ranking in retrieval (hierarchical
  attention over document sections, discourse-aware retrieval), (4) Vocabulary stratification in scientific papers (claim
  vs evidence language, IMRaD-specific studies), (5) Query-evidence vocabulary mismatch in domain-specific QA. Synthesis should
  clarify how TF-ISF relates to prior work and position the null result within the landscape of term-weighting approaches.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

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
  "description": "Plan for a RESEARCH artifact.",
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
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-20 11:44:08 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [4] ASSISTANT · 2026-07-20 11:44:22 UTC

```
I need to craft a detailed research plan for surveying prior work on within-document term weighting and section-aware ranking. Let me search the web to understand the landscape and make the plan concrete.
```

### [5] TOOL CALL — Skill · 2026-07-20 11:44:22 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-20 11:44:22 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-07-20 11:44:22 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-07-20 11:44:22 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-07-20 11:44:22 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-07-20 11:44:22 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] TOOL CALL — Skill · 2026-07-20 11:44:22 UTC

```
aii-web-tools
```

### [12] TOOL RESULT — Skill · 2026-07-20 11:44:22 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [13] TOOL CALL — Skill · 2026-07-20 11:44:22 UTC

```
aii-web-tools
```

### [14] TOOL RESULT — Skill · 2026-07-20 11:44:22 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [15] ASSISTANT · 2026-07-20 11:44:24 UTC

```
I see the skill documentation. Let me load the built-in WebSearch and WebFetch tools to conduct the research directly.
```

### [16] TOOL CALL — ToolSearch · 2026-07-20 11:44:24 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [17] TOOL RESULT — ToolSearch · 2026-07-20 11:44:24 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [18] ASSISTANT · 2026-07-20 11:44:32 UTC

```
Now I'll search comprehensively for the research landscape across the five key areas identified in the artifact direction.
```

### [19] TOOL CALL — WebSearch · 2026-07-20 11:44:32 UTC

```
within-document IDF term weighting Singhal 1996 probabilistic language model
```

### [20] TOOL CALL — WebSearch · 2026-07-20 11:44:32 UTC

```
BM25F field-weighted retrieval Zaragoza 2004 structured documents
```

### [21] TOOL CALL — WebSearch · 2026-07-20 11:44:32 UTC

```
section-aware ranking hierarchical document retrieval scientific papers
```

### [22] TOOL CALL — WebSearch · 2026-07-20 11:44:32 UTC

```
IMRaD vocabulary stratification abstract introduction methods results
```

### [23] TOOL CALL — WebSearch · 2026-07-20 11:44:32 UTC

```
query-evidence vocabulary mismatch scientific question answering
```

### [24] TOOL RESULT — WebSearch · 2026-07-20 11:44:36 UTC

```
{"query": "BM25F field-weighted retrieval Zaragoza 2004 structured documents", "results": [{"tool_use_id": "srvtoolu_014U47Edv1wrDGeTpfGJdC8y", "content": [{"title": "Automatic and Analytical Field Weighting for Structured Document Retrieval | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-031-28244-7_31"}, {"title": "(PDF) Field-Weighted XML Retrieval Based on BM25", "url": "https://www.academia.edu/31223487/Field_Weighted_XML_Retrieval_Based_on_BM25"}, {"title": "A framework for BM25F-based XML retrieval | Proceedings of the 33rd international ACM SIGIR conference on Research and development in information retrieval", "url": "https://dl.acm.org/doi/10.1145/1835449.1835644"}, {"title": "(PDF) Field-weighted XML retrieval based on BM25", "url": "https://www.staff.city.ac.uk/~sbrp622/papers/city_INEX05.pdf"}, {"title": "(PDF) Field-weighted XML retrieval based on BM25", "url": "https://www.researchgate.net/publication/221232871_Field-weighted_XML_retrieval_based_on_BM25"}, {"title": "SPBERTQA: A Two-Stage Question Answering System Based on Sentence   Transformers for Medical Texts", "url": "https://arxiv.org/pdf/2206.09600"}, {"title": "Field-Weighted XML Retrieval Based on BM25 | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-540-34963-1_12"}]}, "Based on the search results, here's what I found about BM25F field-weighted retrieval:\n\nStephen Robertson, Hugo Zaragoza, and Michael Taylor published \"Simple BM25 extension to multiple weighted fields\" at CIKM 2004, pages 42-49. This appears to be the foundational work on BM25F.\n\nIn structured document retrieval (SDR), BM25F is considered the most established model. BM25F is the field-weighted version of BM25 derived from Robertson et al for document level retrieval.\n\nThe BM25F model has been particularly influential in XML and structured document retrieval. Researchers extended Robertson's field-weighted BM25F for document retrieval to element level retrieval, creating BM25E, which was used in evaluations with INEX 2004 topics and assessments.\n\nWithout optimization, BM25F does not benefit from the document structure, which has led to subsequent research into improved field weighting methods for structured document retrieval."], "durationSeconds": 6.390840009000003, "searchCount": 1}
```

### [25] TOOL RESULT — WebSearch · 2026-07-20 11:44:36 UTC

```
{"query": "within-document IDF term weighting Singhal 1996 probabilistic language model", "results": [{"tool_use_id": "srvtoolu_01LZhpjveGtseUmV9dAufa6X", "content": [{"title": "References and further reading", "url": "https://nlp.stanford.edu/IR-book/html/htmledition/references-and-further-reading-6.html"}, {"title": "Scoring, term weighting and the vector space model", "url": "https://nlp.stanford.edu/IR-book/pdf/06vect.pdf"}, {"title": "A Polya Urn Document Language Model for Improved Information Retrieval", "url": "https://arxiv.org/pdf/1502.00804"}, {"title": "Full article: A Fisher’s Exact Test Justification of the TF–IDF Term-Weighting Scheme", "url": "https://www.tandfonline.com/doi/full/10.1080/00031305.2025.2539241"}, {"title": "IDF revisited: A simple new derivation within the Robertson-Sp\\\"arck   Jones probabilistic model", "url": "https://arxiv.org/pdf/0705.1161"}, {"title": "(PDF) A probabilistic justification for using tf�idf term weighting in information retrieval", "url": "https://www.researchgate.net/publication/220387577_A_probabilistic_justification_for_using_tfidf_term_weighting_in_information_retrieval"}, {"title": "models.tfidfmodel – TF-IDF model — gensim", "url": "https://radimrehurek.com/gensim/models/tfidfmodel.html"}, {"title": "A Linguistically Motivated Probabilistic Model of Information Retrieval | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/3-540-49653-X_34"}, {"title": "Probabilistic models of information retrieval based on measuring the divergence from randomness | ACM Transactions on Information Systems", "url": "https://dl.acm.org/doi/abs/10.1145/582415.582416"}, {"title": "An analysis on document length retrieval trends in language modeling smoothing | Discover Computing | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10791-007-9040-x"}]}, "Based on the search results, here's what I found regarding your query about within-document IDF term weighting, Singhal 1996, and probabilistic language models:\n\nThe SMART notation for tf-idf term weighting schemes is presented in Singhal et al. (1996b), and closely follows this work. Singhal et al. (1996a) developed pivoted document length normalization.\n\nAccounting for document length effects within a retrieval algorithm tends to improve performance, as demonstrated by Singhal et al. (1996a). More specifically, in Singhal et al. (1996a), the distribution of the length of documents is referred to as a length pattern, so the documents retrieved by a model produce a retrieval pattern.\n\nRegarding probabilistic language models and term weighting, probabilistic language models develop weighting techniques that are more nuanced than tf-idf. Additionally, one probabilistic model of information retrieval assumes documents and queries are defined by an ordered sequence of single terms, and uses advances in statistical natural language processing to formulate a probabilistic justification for using tf×idf term weighting."], "durationSeconds": 6.981925109, "searchCount": 1}
```

### [26] TOOL RESULT — WebSearch · 2026-07-20 11:44:40 UTC

```
{"query": "query-evidence vocabulary mismatch scientific question answering", "results": [{"tool_use_id": "srvtoolu_01NS9v3Y4BFGfWEpKLm6PoDi", "content": [{"title": "Example of the vocabulary mismatch problem. Regarding the question... | Download Scientific Diagram", "url": "https://www.researchgate.net/figure/Example-of-the-vocabulary-mismatch-problem-Regarding-the-question-shown-in-a-a-user_fig1_322724007"}, {"title": "(PDF) RQUERY: Rewriting Natural Language Queries on Knowledge Graphs to Alleviate the Vocabulary Mismatch Problem", "url": "https://www.researchgate.net/publication/311535153_RQUERY_Rewriting_Natural_Language_Queries_on_Knowledge_Graphs_to_Alleviate_the_Vocabulary_Mismatch_Problem"}, {"title": "answered comprehension questions: Topics by Science.gov", "url": "https://www.science.gov/topicpages/a/answered+comprehension+questions"}, {"title": "Vocabulary mismatch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Vocabulary_mismatch"}, {"title": "Vocabulary Mismatch Avoidance Techniques", "url": "https://www.ijstr.org/final-print/apr2020/Vocabulary-Mismatch-Avoidance-Techniques.pdf"}, {"title": "Using the Hammer Only on Nails: A Hybrid Method for Evidence Retrieval   for Question Answering", "url": "https://arxiv.org/pdf/2009.10791"}, {"title": "The SciQA Scientific Question Answering Benchmark for Scholarly Knowledge | Scientific Reports", "url": "https://www.nature.com/articles/s41598-023-33607-z"}, {"title": "Mitigating Vocabulary Mismatch on Multi-domain Corpus using Word", "url": "https://www.scitepress.org/Papers/2020/90908/90908.pdf"}]}, "I've completed the web search for \"query-evidence vocabulary mismatch scientific question answering\". Here are the key findings:\n\n## Overview\n\nThe vocabulary mismatch between user created queries and relevant documents in a corpus causes the term mismatch problem in information retrieval. Vocabulary mismatch is a common phenomenon in the usage of natural languages, occurring when different people name the same thing or concept differently.\n\n## Quantifying the Problem\n\nAn average query term fails to appear in 30-40% of the documents that are relevant to the user query. Additionally, on average 80% of the times different people (experts in the same field) will name the same thing differently.\n\n## Application to Scientific Question Answering\n\nIn the context of question answering systems, a lexical gap exists between the user's vocabulary and that of the ontology. This involves predicting terms that exist in supporting facts and not in the query, bridging the lexical chasm between queries and supporting facts.\n\n## Solutions\n\nQuery expansion is an extensively researched topic in the field of information retrieval that helps to bridge the vocabulary mismatch problem, i.e., the way users express concepts differs from the way they appear in the corpus. Different approaches include interactive query expansion where the user can choose related words, or automatic query expansion where the retrieval system adds extra words to the query without user input."], "durationSeconds": 8.528195988, "searchCount": 1}
```

### [27] TOOL RESULT — WebSearch · 2026-07-20 11:44:40 UTC

```
{"query": "section-aware ranking hierarchical document retrieval scientific papers", "results": [{"tool_use_id": "srvtoolu_01L2F7UD47zKkcP8kxyZVTh3", "content": [{"title": "IntrAgent: An LLM Agent for Content-Grounded Information Retrieval through Literature Review", "url": "https://arxiv.org/pdf/2604.22861"}, {"title": "Scientific Paper Retrieval with LLM-Guided Semantic-Based Ranking", "url": "https://arxiv.org/html/2505.21815v2"}, {"title": "Discourse-Aware Scientific Paper Recommendation via QA-Style Summarization and", "url": "https://arxiv.org/pdf/2511.03330"}, {"title": "Discourse-Aware Unsupervised Summarization of Long Scientific Documents", "url": "https://arxiv.org/pdf/2005.00513"}, {"title": "Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis", "url": "https://arxiv.org/pdf/2509.06855"}, {"title": "Retrieval of structured documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7428538"}, {"title": "Scientific Paper Retrieval with LLM-Guided Semantic- ...", "url": "https://aclanthology.org/2025.findings-emnlp.108.pdf"}, {"title": "Weakly Supervised Multi-Label Classification of Full-Text Scientific   Papers", "url": "https://arxiv.org/pdf/2306.14003"}]}, "I found several relevant scientific papers on section-aware ranking and hierarchical document retrieval. Here are the key results:\n\n## Key Approaches Found:\n\n**IntrAgent - Section-Aware Ranking:**\nScientific research literature typically follows a well-defined section hierarchy, and IntrAgent leverages this structural knowledge for reasoning-based ranking, prioritizing sections relevant to a question—unlike flat, semantic-similarity-based approaches that overlook document structure.\n\n**SCITREERAG - Hierarchical Tree-Based Retrieval:**\nSCITREERAG addresses semantic similarity issues by exploiting the hierarchical tree-like structure inherent to scientific publications, building a tree representation to guide retrieval toward semantically relevant content in contextually appropriate sections. The system retrieves information by traversing the document hierarchy from abstract to specific content, selecting chunks that are both semantically similar to the query and originate from topically relevant sections using greedy tree traversal.\n\n**Hierarchical Document Graph for Summarization:**\nHierarchical document graphs can be created by splitting documents into sections and sentences, with two levels of connections: intrasectional connections (modeling local importance within a section) and inter-sectional connections (modeling global importance across topics).\n\n**OMRC-MR - Structure-Aware Re-ranking:**\nA hierarchical framework integrates QA-style OMRC summarization, multi-level contrastive learning, and structure-aware re-ranking, with contrastive objectives aligning semantic representations across metadata, section, and document levels.\n\n**Hierarchy-Aware Aggregation:**\nIn-paper hierarchy structure can be utilized to perform embedding aggregation from paragraphs to sections and then to the entire paper by aggregating embeddings from a text unit's children."], "durationSeconds": 9.698549428999998, "searchCount": 1}
```

### [28] TOOL RESULT — WebSearch · 2026-07-20 11:44:46 UTC

```
{"query": "IMRaD vocabulary stratification abstract introduction methods results", "results": [{"tool_use_id": "srvtoolu_01WMqFQVypRBYsQHR1bgrYcz", "content": [{"title": "(PDF) The introduction, methods, results and discussion (IMRAD) structure: A Survey of its use in different authoring partnerships in a students' journal", "url": "https://www.researchgate.net/publication/51509928_The_introduction_methods_results_and_discussion_IMRAD_structure_A_Survey_of_its_use_in_different_authoring_partnerships_in_a_students'_journal"}, {"title": "IMRaD Format Comprehensive Guide", "url": "https://customuniversitypapers.com/imrad-format-comprehensive-guide/"}, {"title": "[PDF] The introduction, methods, results, and discussion (IMRAD) structure: a fifty-year survey. | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/The-introduction,-methods,-results,-and-discussion-Sollaci-Pereira/fb17391a78df98af2b6e65a38fe878809652f53d"}, {"title": "What is IMRaD Format in Research? | Researcher.Life", "url": "https://researcher.life/blog/article/what-is-imrad-format-in-research/"}, {"title": "On the Composition of Scientific Abstracts", "url": "https://arxiv.org/pdf/1604.02580"}, {"title": "Five Key Strategies for Structuring a Scientific Article – Scientific Writing – Escritura Científica", "url": "https://scientificwriting.hcommons.org/2025/04/12/five-key-strategies-for-structuring-a-scientific-article/"}, {"title": "The Writing Center | Scientific (IMRaD) Research Reports...", "url": "https://writingcenter.gmu.edu/writing-resources/imrad/writing-an-imrad-report"}, {"title": "The introduction, methods, results and discussion (IMRAD) structure: a Survey of its use in different authoring partnerships in a students' journal", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3154165/"}]}, "I've completed the web search for your query. Here are the results:\n\n## Key Findings about IMRaD Structure:\n\nIMRaD is an acronym for Introduction, Methods, Results, and Discussion; the standard structure used to report original research. The IMRaD structure is a crucial framework for organizing information in abstract writing, enabling clear and effective communication of research findings.\n\n**Structure Overview:**\n\nThe IMRaD structure follows a rhetorical logic where the Introduction sets the context and outlines the objective, the Methods section details how the study was conducted, the Results section presents findings objectively, and the Discussion interprets those results and explores their implications.\n\n**Abstract and IMRaD:**\n\nAn abstract is a short summary, typically 150 to 300 words, that appears before the Introduction and often mirrors the IMRaD structure in miniature.\n\n**Writing Sections:**\n\nGenerally, Introduction and Discussion comprise 20-25% each, Methods 15-20%, and Results 25-30% of manuscript length.\n\nThe search results provide comprehensive information about the IMRaD framework, though I did not find specific information about \"vocabulary stratification\" in relation to these sections. If you need more specific information about that aspect, please let me know!"], "durationSeconds": 15.636501371000001, "searchCount": 1}
```

### [29] ASSISTANT · 2026-07-20 11:44:58 UTC

```
Now let me fetch some key papers to get concrete methodological details for the plan.
```

### [30] TOOL CALL — WebFetch · 2026-07-20 11:44:58 UTC

```
URL: https://nlp.stanford.edu/IR-book/html/htmledition/references-and-further-reading-6.html
Prompt: What are the key foundational papers on IDF, term weighting, and probabilistic models for information retrieval? List specific authors, years, and main contributions.
```

### [31] TOOL CALL — WebFetch · 2026-07-20 11:44:58 UTC

```
URL: https://arxiv.org/pdf/2604.22861
Prompt: How does IntrAgent handle section-aware retrieval in scientific papers? What methods does it use to rank sections?
```

### [32] TOOL CALL — WebFetch · 2026-07-20 11:44:58 UTC

```
URL: https://arxiv.org/pdf/2005.00513
Prompt: How does this paper use discourse-aware approaches for scientific documents? What methodology is used?
```

### [33] TOOL RESULT — WebFetch · 2026-07-20 11:44:58 UTC

```
{"bytes": 8423, "code": 200, "codeText": "OK", "result": "# Key Foundational Papers on IDF and Term Weighting\n\n**Early Term Weighting:**\n- **Luhn (1957, 1958)**: Pioneered early applications of term weighting, emphasizing \"the importance of medium frequency terms\" and anticipating tf-idf schemes.\n\n**Inverse Document Frequency:**\n- **Spärck Jones (1972)**: Conducted detailed experiments demonstrating the effectiveness of inverse document frequency in term weighting.\n\n**IDF Extensions and Theory:**\n- **Robertson and Jones (1976)**, **Croft and Harper (1979)**, **Salton and Buckley (1987)**, and **Papineni (2001)**: Provided successive extensions and theoretical justifications for idf weighting.\n\n**Vector Space Model:**\n- **Salton (1971)**: The SMART information retrieval system was \"perhaps the first to view a document as a vector of weights.\"\n\n**Normalization Techniques:**\n- **Singhal et al. (1996)**: Developed pivoted document length normalization methods.\n\n**Advanced Probabilistic Models:**\n- **Chapter 11** references probabilistic language models offering \"weighting techniques that are more nuanced than tf-idf,\" with specific discussion of Okapi BM25 in Section 11.4.3.\n\n**Comprehensive Frameworks:**\n- **Moffat and Zobel (1998)**: Developed exhaustive notation for term and document frequency weighting schemes.", "durationMs": 6008, "url": "https://nlp.stanford.edu/IR-book/html/htmledition/references-and-further-reading-6.html"}
```

### [34] TOOL RESULT — WebFetch · 2026-07-20 11:44:58 UTC

```
{"bytes": 1974012, "code": 200, "codeText": "OK", "result": "I apologize, but the content provided appears to be a corrupted or compressed PDF file that cannot be properly parsed. The text shown consists primarily of binary data, compression artifacts, and unreadable encoded content.\n\nTo accurately answer your question about how a paper uses discourse-aware approaches for scientific documents and its methodology, I would need access to a readable version of the document. \n\nCould you please provide:\n- A plain text or properly extracted version of the paper, or\n- The paper's title and authors so I can assist you better, or\n- A different format of the same document?\n\nOnce readable content is available, I'll be happy to analyze the paper's approach to discourse-aware methods and summarize its methodology within the specified constraints.\n\n[Binary content (application/pdf, 1.9MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-gjLlrqQuoUxT-3-invention-loop-iter-2-gen-plan-gen-plan-research-1/e28470cc-047a-449b-89d6-a3eaed78c3d8/tool-results/webfetch-1784547892056-34dt9e.pdf]", "durationMs": 4758, "url": "https://arxiv.org/pdf/2005.00513"}
```

### [35] TOOL RESULT — WebFetch · 2026-07-20 11:44:58 UTC

```
{"bytes": 4706317, "code": 200, "codeText": "OK", "result": "# IntrAgent's Section-Aware Retrieval Approach\n\nBased on the PDF content provided, IntrAgent employs a sophisticated method for handling section-aware retrieval in scientific papers. The system uses what appears to be a hierarchical, content-grounded approach to literature review.\n\n## Ranking Methodology\n\nThe document indicates that IntrAgent utilizes **similarity-based section selection** as a core component. Rather than treating papers as flat documents, the system recognizes the structural organization of academic papers and leverages this hierarchy during retrieval operations.\n\nThe ranking mechanism appears to involve evaluating semantic relevance between user queries and individual paper sections, allowing the system to identify and prioritize the most pertinent portions of research documents. This granular approach enables more precise information extraction than treating entire papers as single retrieval units.\n\n## Key Capability\n\nA notable feature mentioned in the materials is \"Similarity-Based Section Selection,\" which suggests IntrAgent scores and ranks sections based on their relevance to specific information needs. This allows the LLM agent to focus on the most relevant subsections rather than processing entire papers, improving both efficiency and accuracy in content-grounded information retrieval tasks.\n\nThis methodology aligns with IntrAgent's broader design as an agent system for conducting systematic literature reviews while maintaining strong grounding in actual source material.\n\n[Binary content (application/pdf, 4.5MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-gjLlrqQuoUxT-3-invention-loop-iter-2-gen-plan-gen-plan-research-1/e28470cc-047a-449b-89d6-a3eaed78c3d8/tool-results/webfetch-1784547892136-700284.pdf]", "durationMs": 6554, "url": "https://arxiv.org/pdf/2604.22861"}
```

### [36] ASSISTANT · 2026-07-20 11:45:02 UTC

```
Now let me search for more specific related work on RAG and section retrieval in scientific papers.
```

### [37] TOOL CALL — WebSearch · 2026-07-20 11:45:02 UTC

```
QASPER dataset scientific question answering section evidence annotation
```

### [38] TOOL CALL — WebSearch · 2026-07-20 11:45:02 UTC

```
Disco-RAG structure-aware retrieval augmented generation 2025
```

### [39] TOOL CALL — WebSearch · 2026-07-20 11:45:02 UTC

```
dense retrieval scientific domain embedding fine-tuning BERT sentence-transformers
```

### [40] TOOL CALL — WebSearch · 2026-07-20 11:45:02 UTC

```
HyDE hypothetical document embeddings retrieval domain mismatch
```

### [41] TOOL RESULT — WebSearch · 2026-07-20 11:45:08 UTC

```
{"query": "Disco-RAG structure-aware retrieval augmented generation 2025", "results": [{"tool_use_id": "srvtoolu_01TihtEtNrqf2M5AR4oJuwda", "content": [{"title": "Disco-RAG: Discourse-Aware Retrieval-Augmented Generation", "url": "https://arxiv.org/html/2601.04377v5"}, {"title": "Retrieval-Augmented Generation (RAG)", "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-b2f527f9-ed5b-4d55-bf40-48c4e873c676"}, {"title": "Structure-Aware RAG: Structured Retrieval Augmented Generation from Noisy Data for Conversational Agents", "url": "https://arxiv.org/html/2605.24366"}, {"title": "[2601.04377] Disco-RAG: Discourse-Aware Retrieval-Augmented Generation", "url": "https://arxiv.org/abs/2601.04377"}, {"title": "Disco-RAG: Discourse-Aware Retrieval-Augmented Generation", "url": "https://arxiv.org/pdf/2601.04377"}, {"title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers", "url": "https://arxiv.org/html/2506.00054v1"}]}, "Based on the search results, here's what I found about Disco-RAG:\n\n## Disco-RAG: Discourse-Aware Retrieval-Augmented Generation\n\nDisco-RAG is a discourse-aware framework that explicitly injects discourse signals into the generation process by constructing intra-chunk discourse trees to capture local hierarchies and building inter-chunk rhetorical graphs to model cross-passage coherence.\n\n### Key Features\n\nConventional RAG methods typically treat retrieved chunks as isolated and flat sequences, overlooking their structural interconnections, which Disco-RAG addresses. The discourse structures are jointly integrated into a planning blueprint that conditions the generation.\n\n### Performance\n\nThe approach shows efficacy on question answering and long-document summarization benchmarks, achieving state-of-the-art results without fine-tuning. Additionally, Disco-RAG leverages intra-chunk discourse trees and inter-chunk rhetorical graphs to plan and orchestrate generation, vastly improving coherence on long/semi-structured inputs.\n\nThe research was published in January 2026 and represents an important advancement in structure-aware retrieval-augmented generation systems."], "durationSeconds": 6.892549986999999, "searchCount": 1}
```

### [42] TOOL RESULT — WebSearch · 2026-07-20 11:45:10 UTC

```
{"query": "QASPER dataset scientific question answering section evidence annotation", "results": [{"tool_use_id": "srvtoolu_01Q1sCjezWa2pPLNZAfM6Uhb", "content": [{"title": "A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers | Request PDF", "url": "https://www.researchgate.net/publication/352364140_A_Dataset_of_Information-Seeking_Questions_and_Answers_Anchored_in_Research_Papers"}, {"title": "Detect, Retrieve, Comprehend: A Flexible Framework for Zero-Shot   Document-Level Question Answering", "url": "https://arxiv.org/pdf/2210.01959"}, {"title": "README.md · allenai/qasper at main", "url": "https://huggingface.co/datasets/allenai/qasper/blob/main/README.md"}, {"title": "Citation Failure: Definition, Analysis and Efficient Mitigation", "url": "https://arxiv.org/pdf/2510.20303"}, {"title": "QASPER Dataset", "url": "https://paperswithcode.com/dataset/qasper"}, {"title": "QASA: Advanced Question Answering on Scientific Articles", "url": "https://proceedings.mlr.press/v202/lee23n/lee23n.pdf"}, {"title": "SciDQA: A Deep Reading Comprehension Dataset over Scientific Papers", "url": "https://arxiv.org/pdf/2411.05338"}, {"title": "Capturing Global Structural Information in Long Document Question   Answering with Compressive Graph Selector Network", "url": "https://arxiv.org/pdf/2210.05499"}, {"title": "GitHub - shubhamtamhane/QA-Generator-Research-Papers", "url": "https://github.com/shubhamtamhane/QA-Generator-Research-Papers"}, {"title": "A Dataset of Information-Seeking Questions and Answers Anchored in   Research Papers", "url": "https://arxiv.org/pdf/2105.03011"}]}, "Based on the search results, here's information about the QASPER dataset and its evidence annotation, particularly regarding sections:\n\n## Overview of QASPER\n\nThe Question Answering on Scientific Research Papers (QASPER) dataset consists of 1,585 NLP papers sourced from arXiv, and is accompanied by 5,049 questions from NLP readers and corresponding answers from NLP practitioners. Each question is written by an NLP practitioner who read only the title and abstract of the corresponding paper, and the question seeks information present in the full text. The questions are then answered by a separate set of NLP practitioners who also provide supporting evidence to answers.\n\n## Evidence Annotation in QASPER\n\nAnswers are annotated with sentence-level evidence highlights. The dataset includes two types of evidence annotations: \"highlighted_evidence\" is the set of sentences the answer providers selected as evidence if they chose textual evidence. The text in the \"evidence\" field is a mapping from these sentences to the paragraph level. That is, if you see textual evidence in the \"evidence\" field, it is guaranteed to be entire paragraphs, while that is not the case with \"highlighted_evidence\".\n\n## Section-Level Analysis\n\nResearchers performed section name normalization and found that among frequently used section names such as \"Experiments\" and \"Introduction,\" there was not a single section name that contained a majority of evidence spans, indicating that the distribution of evidence over section in the paper was more or less uniform."], "durationSeconds": 7.982411565000002, "searchCount": 1}
```

### [43] TOOL RESULT — WebSearch · 2026-07-20 11:45:12 UTC

```
{"query": "HyDE hypothetical document embeddings retrieval domain mismatch", "results": [{"tool_use_id": "srvtoolu_01BSRsmhyMSAXDBRNosiQRR7", "content": [{"title": "LM-Kit.NET HyDE: Hypothetical Document Embeddings for RAG in C# .NET", "url": "https://docs.lm-kit.com/lm-kit-net/guides/glossary/hyde.html"}, {"title": "Advanced RAG Optimization: Aligning Question and Document Embedding Spaces with HyDE | by Richard Song | Epsilla", "url": "https://blog.epsilla.com/demystifying-rag-empowered-chat-agents-aligning-question-and-document-embedding-spaces-with-hyde-dc06d81a423d?gi=fe4a2feb843b"}, {"title": "Issue #85 - Advanced Retrieval Strategies: HyDE", "url": "https://mlpills.substack.com/p/issue-85-advanced-retrieval-strategies"}, {"title": "HyDE: Hypothetical Document Embeddings | by Chanchala Gorale | Medium", "url": "https://cgorale111.medium.com/hyde-hypothetical-document-embeddings-3071840e364c"}, {"title": "Hypothetical Document Embeddings (HyDE)", "url": "https://deepchecks.com/glossary/hypothetical-document-embeddings/"}, {"title": "LLMs to Support a Domain Specific Knowledge Assistant", "url": "https://arxiv.org/pdf/2502.04095"}, {"title": "Hypothetical Document Embeddings (HyDE) | Haystack Documentation", "url": "https://docs.haystack.deepset.ai/docs/hypothetical-document-embeddings-hyde"}, {"title": "Introduction to Hypothetical Document Embeddings (HyDE) - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/data-science/hypothetical-document-embeddings-hyde-hyde/"}, {"title": "101. Hypothetical Document Embeddings The Simple Trick That Makes RAG Retrieval Actually Work: HyDE", "url": "https://plainenglish.io/blog/101-hypothetical-document-embeddings-the-simple-trick-that-makes-rag-retrieval-actually-work-hyde"}, {"title": "Leveraging Hypothetical Document Embeddings (HyDE) to Enhance Retrieval-Augmented Generation…", "url": "https://medium.com/@ali.rafik.ali.97/leveraging-hypothetical-document-embeddings-hyde-to-enhance-retrieval-augmented-generation-434deccb9755"}]}, "Based on the search results, here's what I found about HyDE (Hypothetical Document Embeddings) and how it addresses domain mismatch in retrieval:\n\n## Overview of HyDE\n\nHyDE is a retrieval technique that bridges the gap between how users phrase questions and how answers are written in documents. Instead of embedding the user's question directly and searching for similar text, HyDE first asks the LLM to generate a hypothetical answer to the question, then embeds that hypothetical answer and uses it as the search query.\n\n## Addressing Domain Mismatch\n\nA big challenge in traditional embedding-based search systems is something called misalignment — basically, a mismatch between how user questions and documents are represented in the embedding space. This is the fundamental problem in information retrieval where users' questions are linguistically different from the documents containing the answers.\n\nBecause the hypothetical answer is written in the same style and vocabulary as actual documents (declarative statements, domain terminology, factual descriptions), it matches far better against the document embeddings in the vector store.\n\n## Domain-Specific Benefits\n\nHyDE is especially useful when dealing with specialized domains that differ significantly from typical datasets that retrievers are trained on. In these cases, HyDE can help bridge the domain gap between queries and documents. Additionally, many embedding retrievers generalize poorly to new, unseen domains, and this approach tries to tackle this problem.\n\n## Limitations in Niche Domains\n\nHowever, there is a caveat: if the domain is rare or not well represented in the LLM's training corpus, the hypothetical doc might be way off, misleading retrieval to irrelevant documents."], "durationSeconds": 9.114352350000008, "searchCount": 1}
```

### [44] TOOL RESULT — WebSearch · 2026-07-20 11:45:12 UTC

```
{"query": "dense retrieval scientific domain embedding fine-tuning BERT sentence-transformers", "results": [{"tool_use_id": "srvtoolu_017iJA7ryzNjyjVA57uEsjdT", "content": [{"title": "GitHub - siamakz/sentence-transformers-1: Sentence Embeddings with BERT & XLNet · GitHub", "url": "https://github.com/siamakz/sentence-transformers-1"}, {"title": "NeuML/pubmedbert-base-embeddings · Hugging Face", "url": "https://huggingface.co/NeuML/pubmedbert-base-embeddings"}, {"title": "Pre-training vs. Fine-tuning: A Reproducibility Study on Dense Retrieval Knowledge Acquisition", "url": "https://arxiv.org/pdf/2505.07166"}, {"title": "sentence-transformers/docs/publications.md at main · huggingface/sentence-transformers", "url": "https://github.com/huggingface/sentence-transformers/blob/main/docs/publications.md"}, {"title": "Retrieval for Extremely Long Queries and Documents with RPRS: a Highly   Efficient and Effective Transformer-based Re-Ranker", "url": "https://arxiv.org/pdf/2303.01200"}, {"title": "Sentence Transformers: From BERT to Modern Embedding Models | by Bhaskar Dakamarri | Medium", "url": "https://medium.com/@ddbrao11/sentence-transformers-from-bert-to-modern-embedding-models-609cfad37458"}, {"title": "PairSem: LLM-Guided Pairwise Semantic Matching for Scientific Document Retrieval", "url": "https://arxiv.org/pdf/2510.09897"}, {"title": "GitHub - huggingface/sentence-transformers: State-of-the-Art Embeddings, Retrieval, and Reranking · GitHub", "url": "https://github.com/huggingface/sentence-transformers"}, {"title": "Domain-Adaptive and Scalable Dense Retrieval for Content-Based Recommendation", "url": "https://arxiv.org/pdf/2602.00899"}]}, "I've performed the web search on dense retrieval, scientific domain embedding fine-tuning with BERT and sentence-transformers. Here are the key results:\n\n## Overview of Sentence-Transformers Framework\n\nThe sentence-transformers framework provides an easy method to compute dense vector representations for sentences and paragraphs using transformer networks like BERT, RoBERTa, and XLM-RoBERTa. These models are tuned to create meaningful sentence embeddings such that sentences with similar meanings are close in vector space.\n\n## Fine-tuning for Task-Specific Embeddings\n\nThe framework allows easy fine-tuning of custom embedding models to achieve maximal performance on specific tasks. The Sentence Transformers (SBERT) framework fine-tunes BERT using Siamese & Triplet networks, making embeddings directly usable for semantic similarity tasks.\n\n## Scientific Domain Application\n\nFor scientific document retrieval, there's specific work being done: Works such as SciBERT, SPECTER, and BMRetriever focused on scientific retrieval by fine-tuning retriever models on domain-specific data. Additionally, PubMedBERT-base is a model fine-tuned using sentence-transformers that maps sentences and paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.\n\n## Dense Retrieval Architecture\n\nPre-trained dense retrievers map texts into continuous Euclidean spaces, where semantic relevance between queries and documents is captured through vector similarity. The sentence-transformers library offers support for 20+ loss functions for embedding models, allowing you to tune models specifically for semantic search, paraphrase mining, semantic similarity comparison, clustering, triplet loss, contrastive loss, and other applications."], "durationSeconds": 10.516970676000005, "searchCount": 1}
```

### [45] ASSISTANT · 2026-07-20 11:45:22 UTC

```
Excellent. Now let me fetch a couple more key papers to complete the landscape picture.
```

### [46] TOOL CALL — WebFetch · 2026-07-20 11:45:22 UTC

```
URL: https://arxiv.org/pdf/2105.03011
Prompt: What is the QASPER dataset? How many papers and questions does it contain? How are evidence sections annotated? What section types are present?
```

### [47] TOOL CALL — WebFetch · 2026-07-20 11:45:22 UTC

```
URL: https://arxiv.org/html/2601.04377v5
Prompt: What is Disco-RAG? How does it differ from TF-ISF approaches? What discourse structures does it use?
```

### [48] TOOL RESULT — WebFetch · 2026-07-20 11:45:22 UTC

```
{"bytes": 544620, "code": 200, "codeText": "OK", "result": "# Disco-RAG: Discourse-Aware Retrieval-Augmented Generation\n\n## What is Disco-RAG?\n\nDisco-RAG is a framework that enhances retrieval-augmented generation by explicitly incorporating discourse structure into the generation process. Unlike standard RAG systems that treat retrieved passages as isolated chunks, this approach organizes evidence using hierarchical structures and rhetorical relationships to improve reasoning and coherence.\n\n## Key Differences from Standard RAG\n\nStandard retrieval approaches typically suffer from what the paper calls \"intra-chunk structural blindness\" and \"inter-chunk coherence gaps.\" Disco-RAG addresses these by organizing scattered evidence into \"discourse structures (trees & graphs)\" rather than handling passages as disconnected fragments. The system recognizes that understanding how information relates logically is crucial for synthesis.\n\n## Discourse Structures Used\n\nThe framework employs three complementary structural components:\n\n1. **Intra-Chunk RST Trees**: Constructs Rhetorical Structure Theory trees within each retrieved passage to capture internal logical hierarchies and relationships between elementary discourse units\n\n2. **Inter-Chunk Rhetorical Graphs**: Builds directed graphs mapping rhetorical connections across multiple chunks, modeling how evidence relates between documents\n\n3. **Discourse-Driven Planning**: Generates a strategic blueprint that orchestrates how to present and synthesize information, based on the identified structures\n\nThese structures collectively enable the model to distinguish between core and supplementary information and maintain coherent argumentative flow across dispersed evidence.", "durationMs": 5605, "url": "https://arxiv.org/html/2601.04377v5"}
```

### [49] TOOL RESULT — WebFetch · 2026-07-20 11:45:22 UTC

```
{"bytes": 506609, "code": 200, "codeText": "OK", "result": "I cannot provide useful information about the QASPER dataset from the content above. The material appears to be a PDF file containing encoded/compressed image and form data rather than readable text about the dataset.\n\nTo properly answer your questions about QASPER's composition, annotation methodology, and section types, I would need access to the actual paper or documentation in plain text format. I'd recommend:\n\n1. Locating the original QASPER paper (likely \"QASPER: A Benchmark Dataset with Expert-Annotated Summaries...\" or similar)\n2. Accessing it through arXiv, the authors' website, or a university repository\n3. Sharing the text content directly rather than a PDF\n\nIf you can provide the readable text of the paper, I'll be happy to answer your specific questions about dataset size, annotation approaches, and section categorizations.\n\n[Binary content (application/pdf, 494.7KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-gjLlrqQuoUxT-3-invention-loop-iter-2-gen-plan-gen-plan-research-1/e28470cc-047a-449b-89d6-a3eaed78c3d8/tool-results/webfetch-1784547914844-0zajbz.pdf]", "durationMs": 7176, "url": "https://arxiv.org/pdf/2105.03011"}
```

### [50] ASSISTANT · 2026-07-20 11:46:19 UTC

```
Perfect. I now have sufficient research context to write a comprehensive, actionable plan. Let me compile this into the JSON output.
```

### [51] TOOL CALL — Write · 2026-07-20 11:46:19 UTC

```
File: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "Within-Document Term Weighting Prior Work Survey",
  "summary": "Comprehensive literature survey to establish novelty and contextualize TF-ISF within the landscape of within-document term reweighting, field-weighted retrieval, section-aware ranking, vocabulary stratification in IMRaD papers, and query-evidence mismatch in scientific QA.",
  "runpod_compute_profile": "cpu_light",
  "question": "How do prior approaches to within-document term weighting, field-weighted retrieval, and section-aware ranking in scientific papers compare to TF-ISF, and what evidence exists for vocabulary stratification between IMRaD sections?",
  "research_plan": "## Phase 1: Within-Document Term Weighting & IDF Variants (Search, Fetch, Synthesize)\n\n### 1.1 Foundational IDF and Term Weighting Theory\n- **Search scope**: Spärck Jones (1972) IDF pioneer work, Singhal et al. (1996) pivoted normalization, Robertson & Jones (1976), Salton & Buckley (1987) tf-idf theory\n- **Target**: Establish that classical IDF is cross-corpus; identify historical precedent (if any) for within-document variants\n- **Fetch**: Stanford IR Book Ch.6 (vector space model, term weighting), key foundational papers on tf-idf justification\n- **Extract specifics**: Exact mathematical definitions of IDF, document frequency vs. section frequency, any mention of intra-document frequency variants\n- **Key question to answer**: Are there published precedents for within-document IDF or section-based IDF before this work? What probabilistic justifications exist for tf-idf that might extend to ISF?\n\n### 1.2 Probabilistic Language Models for Retrieval\n- **Search scope**: Probabilistic language models (Hiemstra 1998 and later), Okapi BM25 (Robertson et al.), query likelihood models, language model smoothing\n- **Target**: Understand how probabilistic frameworks assign term weights; identify if any naturally extend to section-level granularity\n- **Fetch**: Papers on Dirichlet smoothing, collection model variants, position-aware language models\n- **Key question**: Do probabilistic models explicitly handle multi-level structures (document + section)? Any prior work on section-specific language models?\n\n## Phase 2: Field-Weighted Retrieval (BM25F and Structured Documents)\n\n### 2.1 BM25F and Field-Weighted Extensions\n- **Search scope**: BM25F (Zaragoza et al. 2004 CIKM), field weighting in structured documents, BM25E for XML/hierarchical retrieval\n- **Target**: Establish that BM25F is the industrial standard for multi-field retrieval; clarify how field IDF is computed (per-field or global)\n- **Fetch**: Zaragoza et al. (2004) \"Simple BM25 extension to multiple weighted fields\", XML retrieval papers using BM25F\n- **Extract specifics**: Mathematical formulation of BM25F, how field weights are assigned, whether field-level ISF is ever discussed\n- **Key question**: Does BM25F compute per-field IDF or use global IDF? How does this relate to per-section ISF?\n\n### 2.2 Other Structured Document Retrieval Approaches\n- **Search scope**: Hierarchical BM25, Zaragoza et al. field boost experiments, weight tuning methods\n- **Target**: Understand what field weighting techniques exist beyond basic BM25F\n- **Key question**: Have researchers tuned section-specific boost weights empirically? Any ablations on field IDF vs. boost?\n\n## Phase 3: Section-Aware & Hierarchical Retrieval in Scientific Papers\n\n### 3.1 Recent Structure-Aware RAG Systems\n- **Search scope**: IntrAgent (2024), SCITREERAG, Disco-RAG (2025 arxiv 2601.04377), SF-RAG (2026 arxiv 2602.13647), hierarchical document graphs\n- **Target**: Map the landscape of recent approaches that exploit document structure; identify which use term weighting vs. embedding-only vs. discourse\n- **Fetch**: IntrAgent paper (arxiv 2604.22861) for similarity-based section selection; Disco-RAG for discourse-aware approach; SCITREERAG for tree-based hierarchy\n- **Extract**: How each method ranks or retrieves sections; whether they use term statistics, embeddings, discourse, or hybrid; computational cost\n- **Key comparison points vs. TF-ISF**:\n  - Disco-RAG: Requires RST parsing + inter-chunk graphs (external model), operates on generation coherence not retrieval scoring → TF-ISF requires zero external infrastructure\n  - SF-RAG: Routes via pre-built structural index; TF-ISF reweights term-section matches post-hoc without indexing infrastructure\n  - IntrAgent: Similarity-based section selection on embeddings; TF-ISF is sparse-term based\n\n### 3.2 Hierarchical Document Structure in Dense Retrieval\n- **Search scope**: Hierarchy-aware aggregation (paragraph→section→document embeddings), OMRC-MR structure-aware re-ranking, in-paper hierarchy for semantic coherence\n- **Target**: Understand how dense embeddings handle multi-level structure\n- **Key question**: Do dense methods suffer from the same claim-section bias? Any evidence that embedding quality differs across IMRaD sections?\n\n## Phase 4: Vocabulary Stratification in IMRaD Scientific Papers\n\n### 4.1 IMRaD Writing Convention & Section Characteristics\n- **Search scope**: IMRaD format survey papers, abstract composition studies (arxiv 1604.02580), section length and content distribution\n- **Target**: Establish that IMRaD is standard in scientific papers; confirm claim vs. evidence vocabulary split is theoretically motivated\n- **Fetch**: 50-year IMRaD survey, abstract composition paper\n- **Extract**: Typical section lengths, reuse of topic terms across sections, any linguistic analysis of vocabulary differences\n- **Key question**: Is there published linguistic evidence that Abstract/Introduction use more shared vocabulary than Methods/Results within the same paper?\n\n### 4.2 Empirical Vocabulary Analysis in Scientific Corpora\n- **Search scope**: Claim vs. evidence language studies, discourse-aware scientific summarization, vocabulary analysis in scientific papers\n- **Target**: Find prior empirical studies that measure vocabulary overlap between sections\n- **Fetch**: Discourse-aware summarization papers (arxiv 2005.00513 if readable)\n- **Key question**: Has anyone quantified section-level vocabulary overlap? Any evidence that Methods/Results sections contain unique terms?\n\n## Phase 5: Query-Evidence Vocabulary Mismatch in Scientific QA\n\n### 5.1 Vocabulary Mismatch Problem (General)\n- **Search scope**: General vocabulary mismatch in IR (30-40% term failure rate), query expansion techniques, lexical gaps in QA\n- **Target**: Establish that query-document vocabulary mismatch is a well-known problem; understand standard mitigation strategies\n- **Fetch**: Vocabulary mismatch Wikipedia, RQUERY paper, vocabulary avoidance techniques\n- **Extract**: Quantified statistics on mismatch rate, solutions attempted (expansion, paraphrase, dense embeddings)\n- **Key question**: Is within-document term reweighting ever proposed as a solution?\n\n### 5.2 Vocabulary Mismatch in Scientific QA Specifically\n- **Search scope**: QASPER dataset annotation studies, SciQA, dense retrieval for scientific papers, domain-specific embedding fine-tuning\n- **Target**: Understand whether scientific QA exhibits different vocabulary mismatch patterns; identify bottlenecks empirically\n- **Fetch**: QASPER dataset paper (README or arxiv 2105.03011), QASA paper, SciDQA, CG-RAG (citation-graph RAG)\n- **Extract from QASPER**:\n  - Dataset size (1,585 papers, 5,049 questions confirmed)\n  - Evidence distribution across sections (confirmed: uniform, no majority-holding section)\n  - Types of questions (factual, numerical, synthesis, etc.)\n  - Current baseline performance levels (dense retrieval F1, sparse F1, reader F1)\n- **Key question**: Which sections (Abstract vs. Methods) contain correct answers most often? How does cosine similarity rank these sections for queries with evidence in Methods/Results?\n\n### 5.3 Domain-Specific Dense Retrieval Quality\n- **Search scope**: PubMedBERT, SciBERT, SPECTER, domain-adaptive dense retrievers, pre-training vs. fine-tuning for scientific retrieval (arxiv 2505.07166)\n- **Target**: Identify gaps in dense embedding quality for scientific domain; confirm that general-purpose embedders underperform\n- **Fetch**: PubMedBERT docs, Pre-training vs Fine-tuning paper (2505.07166), PairSem for scientific doc retrieval\n- **Extract**: Performance numbers on scientific benchmarks (QASPER, SciDQA), evidence that fine-tuning helps, any failure analysis on section types\n- **Key question**: Can fine-tuning dense embedders solve the section retrieval problem? Or is the bottleneck fundamental (coarse granularity, query phrasing)?\n\n### 5.4 HyDE and Query-Generation Approaches\n- **Search scope**: HyDE (hypothetical document embeddings), query generation for domain shift, LLM-in-the-loop retrieval\n- **Target**: Understand alternative approaches to vocabulary mismatch that use LLM generation\n- **Fetch**: HyDE blog posts, Haystack docs, medium articles on query-generation methods\n- **Key comparison**: HyDE requires LLM inference at retrieval time; TF-ISF requires zero LLM calls during retrieval\n\n## Phase 6: Related Work Synthesis & Positioning\n\n### 6.1 Comparative Analysis\n- **Create a comparison table** (research_out.json) with rows = [TF-ISF, BM25F, Disco-RAG, HyDE, SF-RAG, CG-RAG, SURE-RAG, dense embeddings]\n- **Columns**: Method, Granularity (document/section/chunk), External infrastructure required?, LLM inference at retrieval time?, Training required?, Key strengths, Key limitations, Citation count / maturity\n- **Positioning**: Where does TF-ISF sit? Nearest neighbors in the design space?\n\n### 6.2 Novelty Assessment\n- **Question 1**: Is within-document ISF explicitly proposed in prior work? (Expected answer: No, but BM25F and field weighting are close cousins)\n- **Question 2**: Has anyone proposed section-frequency-based reweighting for scientific paper retrieval? (Expected: No, but discourse-aware and hierarchy-aware systems are emerging)\n- **Question 3**: Has the claim/evidence vocabulary gap in IMRaD been formally studied empirically? (Expected: Theoretically motivated but not quantified at scale in QASPER era)\n\n### 6.3 Contextualize the Null Result\n- **Key finding to synthesize**: If TF-ISF achieved F1=0.187 (no better than cosine 0.198 or BM25 0.179, p>0.37), why?\n  - **Hypothesis A**: The vocabulary gap assumption is wrong; Methods/Results sections do NOT use more unique vocabulary (confirmed by ISF scores: Methods ISF 1.23–1.24 < Intro ISF 1.34)\n  - **Hypothesis B**: Even if Methods sections had high ISF, the problem is not ranking (both achieve similar section recall ~0.48) but reader quality\n  - **Hypothesis C**: Section granularity is too coarse; within-section vocabulary mismatch is the bottleneck\n  - **Synthesis**: Disco-RAG, SCITREERAG, and fine-tuned embedders suggest future work should target (1) finer-grained retrieval (paragraph/sentence level), (2) discourse or embedding structure, (3) domain-specific models\n\n## Phase 7: Report Structure & Output Format\n\n### Output Files\n- **research_out.json**: Structured output with fields:\n  - `answer`: 2–3 paragraph summary of findings (novelty claim, key prior work landscape, positioning)\n  - `sources`: Comprehensive bibliography (≥20 citations with BibTeX entries where possible)\n  - `follow_up_questions`: 5–8 open questions for the executor (e.g., \"Did embedding quality on scientific domain improve 2023–2026?\", \"Has fine-tuned dense retrieval been evaluated on QASPER per-section?\")\n  - `comparative_table`: JSON table comparing methods (TF-ISF vs. Disco-RAG vs. BM25F vs. HyDE vs. dense embeddings)\n  - `vocabulary_stratification_evidence`: Summary of whether IMRaD vocabulary gap is empirically confirmed or merely theoretical\n  - `section_retrieval_bottlenecks`: Structured analysis of whether bottleneck is (a) ranking function, (b) reader quality, (c) section granularity, (d) embedding domain gap\n\n- **research_report.md**: Narrative report with sections:\n  1. Executive Summary (novelty + position in landscape)\n  2. Within-Document Term Weighting Landscape (IDF theory, BM25F, prior ISF work)\n  3. Section-Aware & Hierarchical Retrieval (IntrAgent, SCITREERAG, Disco-RAG comparison)\n  4. IMRaD Vocabulary Stratification (theory + evidence)\n  5. Query-Evidence Mismatch in Scientific QA (QASPER, dense retrieval quality, HyDE)\n  6. Comparative Analysis Table\n  7. Null Result Contextualization (why TF-ISF did not improve F1)\n  8. Future Directions (discourse-aware, fine-tuned embeddings, finer granularity)\n\n### Research Quality Checkpoints\n- ✓ Fetch & extract at least 1 foundational paper per theme (Spärck Jones 1972, Zaragoza 2004, Disco-RAG, QASPER, HyDE)\n- ✓ Quantify claim with numbers (QASPER: 1,585 papers, 5,049 questions; null result: p>0.37, d<0.10; ISF gap: Methods 1.23–1.24 vs. Intro 1.34)\n- ✓ Create comparative table with ≥5 related methods\n- ✓ Identify at least 3 future directions (discourse, fine-tuning, granularity)\n- ✓ Cite ≥20 sources across all themes\n\n## Executor Notes\n- **Time allocation** (within 3h budget):\n  - Phase 1–2: 30 min (foundational theory + BM25F)\n  - Phase 3: 40 min (IntrAgent, SCITREERAG, Disco-RAG, dense methods)\n  - Phase 4: 30 min (IMRaD studies, vocabulary stratification)\n  - Phase 5: 45 min (QASPER analysis, dense retrieval, HyDE)\n  - Phase 6–7: 35 min (synthesis, report writing)\n- **Cost tracking**: Each web search is ~free (via Serper). Each fetch of a 2–10 page paper via WebFetch is ~free. Budget is for potential deep-reading LLM calls if synthesis requires extracting complex details; keep to <$1 total.\n- **Failure scenarios**:\n  - If QASPER paper is not fetchable: Use the README + search results; section uniformity is already confirmed in search snippets\n  - If Disco-RAG PDF doesn't parse: HTML version is available; fetch that instead\n  - If no empirical vocabulary stratification study exists: Frame as \"vocabulary gap is theoretically motivated but empirically unquantified,\" which is still a valid finding\n- **Success criteria**:\n  - Novelty claim is clear and specific: TF-ISF is a direct within-document application of IDF; closest prior is BM25F (field-level, not section-level, and for flat documents not IMRaD papers)\n  - Null result is contextualized: ISF assumption (Methods sections have higher ISF) is empirically inverted; bottleneck is not ranking but reader or embedding quality\n  - Future work is actionable: Disco-RAG, fine-tuned embeddings, paragraph-level retrieval are concrete next steps\n  - Bibliography is comprehensive and well-organized (20+ citations)\n"
}
```

### [52] TOOL RESULT — Write · 2026-07-20 11:46:19 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Within-Document Term Weighting Prior Work Survey\",\n  \"summary\": \"Comprehensive literature survey to establish novelty and contextualize TF-ISF within the landscape of within-document term reweighting, field-weighted retrieval, section-aware ranking, vocabulary stratification in IMRaD papers, and query-evidence mismatch in scientific QA.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"How do prior approaches to within-document term weighting, field-weighted retrieval, and section-aware ranking in scientific papers compare to TF-ISF, and what evidence exists for vocabulary stratification between IMRaD sections?\",\n  \"research_plan\": \"## Phase 1: Within-Document Term Weighting & IDF Variants (Search, Fetch, Synthesize)\\n\\n### 1.1 Foundational IDF and Term Weighting Theory\\n- **Search scope**: Spärck Jones (1972) IDF pioneer work, Singhal et al. (1996) pivoted normalization, Robertson & Jones (1976), Salton & Buckley (1987) tf-idf theory\\n- **Target**: Establish that classical IDF is cross-corpus; identify historical precedent (if any) for within-document variants\\n- **Fetch**: Stanford IR Book Ch.6 (vector space model, term weighting), key foundational papers on tf-idf justification\\n- **Extract specifics**: Exact mathematical definitions of IDF, document frequency vs. section frequency, any mention of intra-document frequency variants\\n- **Key question to answer**: Are there published precedents for within-document IDF or section-based IDF before this work? What probabilistic justifications exist for tf-idf that might extend to ISF?\\n\\n### 1.2 Probabilistic Language Models for Retrieval\\n- **Search scope**: Probabilistic language models (Hiemstra 1998 and later), Okapi BM25 (Robertson et al.), query likelihood models, language model smoothing\\n- **Target**: Understand how probabilistic frameworks assign term weights; identify if any naturally extend to section-level granularity\\n- **Fetch**: Papers on Dirichlet smoothing, collection model variants, position-aware language models\\n- **Key question**: Do probabilistic models explicitly handle multi-level structures (document + section)? Any prior work on section-specific language models?\\n\\n## Phase 2: Field-Weighted Retrieval (BM25F and Structured Documents)\\n\\n### 2.1 BM25F and Field-Weighted Extensions\\n- **Search scope**: BM25F (Zaragoza et al. 2004 CIKM), field weighting in structured documents, BM25E for XML/hierarchical retrieval\\n- **Target**: Establish that BM25F is the industrial standard for multi-field retrieval; clarify how field IDF is computed (per-field or global)\\n- **Fetch**: Zaragoza et al. (2004) \\\"Simple BM25 extension to multiple weighted fields\\\", XML retrieval papers using BM25F\\n- **Extract specifics**: Mathematical formulation of BM25F, how field weights are assigned, whether field-level ISF is ever discussed\\n- **Key question**: Does BM25F compute per-field IDF or use global IDF? How does this relate to per-section ISF?\\n\\n### 2.2 Other Structured Document Retrieval Approaches\\n- **Search scope**: Hierarchical BM25, Zaragoza et al. field boost experiments, weight tuning methods\\n- **Target**: Understand what field weighting techniques exist beyond basic BM25F\\n- **Key question**: Have researchers tuned section-specific boost weights empirically? Any ablations on field IDF vs. boost?\\n\\n## Phase 3: Section-Aware & Hierarchical Retrieval in Scientific Papers\\n\\n### 3.1 Recent Structure-Aware RAG Systems\\n- **Search scope**: IntrAgent (2024), SCITREERAG, Disco-RAG (2025 arxiv 2601.04377), SF-RAG (2026 arxiv 2602.13647), hierarchical document graphs\\n- **Target**: Map the landscape of recent approaches that exploit document structure; identify which use term weighting vs. embedding-only vs. discourse\\n- **Fetch**: IntrAgent paper (arxiv 2604.22861) for similarity-based section selection; Disco-RAG for discourse-aware approach; SCITREERAG for tree-based hierarchy\\n- **Extract**: How each method ranks or retrieves sections; whether they use term statistics, embeddings, discourse, or hybrid; computational cost\\n- **Key comparison points vs. TF-ISF**:\\n  - Disco-RAG: Requires RST parsing + inter-chunk graphs (external model), operates on generation coherence not retrieval scoring → TF-ISF requires zero external infrastructure\\n  - SF-RAG: Routes via pre-built structural index; TF-ISF reweights term-section matches post-hoc without indexing infrastructure\\n  - IntrAgent: Similarity-based section selection on embeddings; TF-ISF is sparse-term based\\n\\n### 3.2 Hierarchical Document Structure in Dense Retrieval\\n- **Search scope**: Hierarchy-aware aggregation (paragraph→section→document embeddings), OMRC-MR structure-aware re-ranking, in-paper hierarchy for semantic coherence\\n- **Target**: Understand how dense embeddings handle multi-level structure\\n- **Key question**: Do dense methods suffer from the same claim-section bias? Any evidence that embedding quality differs across IMRaD sections?\\n\\n## Phase 4: Vocabulary Stratification in IMRaD Scientific Papers\\n\\n### 4.1 IMRaD Writing Convention & Section Characteristics\\n- **Search scope**: IMRaD format survey papers, abstract composition studies (arxiv 1604.02580), section length and content distribution\\n- **Target**: Establish that IMRaD is standard in scientific papers; confirm claim vs. evidence vocabulary split is theoretically motivated\\n- **Fetch**: 50-year IMRaD survey, abstract composition paper\\n- **Extract**: Typical section lengths, reuse of topic terms across sections, any linguistic analysis of vocabulary differences\\n- **Key question**: Is there published linguistic evidence that Abstract/Introduction use more shared vocabulary than Methods/Results within the same paper?\\n\\n### 4.2 Empirical Vocabulary Analysis in Scientific Corpora\\n- **Search scope**: Claim vs. evidence language studies, discourse-aware scientific summarization, vocabulary analysis in scientific papers\\n- **Target**: Find prior empirical studies that measure vocabulary overlap between sections\\n- **Fetch**: Discourse-aware summarization papers (arxiv 2005.00513 if readable)\\n- **Key question**: Has anyone quantified section-level vocabulary overlap? Any evidence that Methods/Results sections contain unique terms?\\n\\n## Phase 5: Query-Evidence Vocabulary Mismatch in Scientific QA\\n\\n### 5.1 Vocabulary Mismatch Problem (General)\\n- **Search scope**: General vocabulary mismatch in IR (30-40% term failure rate), query expansion techniques, lexical gaps in QA\\n- **Target**: Establish that query-document vocabulary mismatch is a well-known problem; understand standard mitigation strategies\\n- **Fetch**: Vocabulary mismatch Wikipedia, RQUERY paper, vocabulary avoidance techniques\\n- **Extract**: Quantified statistics on mismatch rate, solutions attempted (expansion, paraphrase, dense embeddings)\\n- **Key question**: Is within-document term reweighting ever proposed as a solution?\\n\\n### 5.2 Vocabulary Mismatch in Scientific QA Specifically\\n- **Search scope**: QASPER dataset annotation studies, SciQA, dense retrieval for scientific papers, domain-specific embedding fine-tuning\\n- **Target**: Understand whether scientific QA exhibits different vocabulary mismatch patterns; identify bottlenecks empirically\\n- **Fetch**: QASPER dataset paper (README or arxiv 2105.03011), QASA paper, SciDQA, CG-RAG (citation-graph RAG)\\n- **Extract from QASPER**:\\n  - Dataset size (1,585 papers, 5,049 questions confirmed)\\n  - Evidence distribution across sections (confirmed: uniform, no majority-holding section)\\n  - Types of questions (factual, numerical, synthesis, etc.)\\n  - Current baseline performance levels (dense retrieval F1, sparse F1, reader F1)\\n- **Key question**: Which sections (Abstract vs. Methods) contain correct answers most often? How does cosine similarity rank these sections for queries with evidence in Methods/Results?\\n\\n### 5.3 Domain-Specific Dense Retrieval Quality\\n- **Search scope**: PubMedBERT, SciBERT, SPECTER, domain-adaptive dense retrievers, pre-training vs. fine-tuning for scientific retrieval (arxiv 2505.07166)\\n- **Target**: Identify gaps in dense embedding quality for scientific domain; confirm that general-purpose embedders underperform\\n- **Fetch**: PubMedBERT docs, Pre-training vs Fine-tuning paper (2505.07166), PairSem for scientific doc retrieval\\n- **Extract**: Performance numbers on scientific benchmarks (QASPER, SciDQA), evidence that fine-tuning helps, any failure analysis on section types\\n- **Key question**: Can fine-tuning dense embedders solve the section retrieval problem? Or is the bottleneck fundamental (coarse granularity, query phrasing)?\\n\\n### 5.4 HyDE and Query-Generation Approaches\\n- **Search scope**: HyDE (hypothetical document embeddings), query generation for domain shift, LLM-in-the-loop retrieval\\n- **Target**: Understand alternative approaches to vocabulary mismatch that use LLM generation\\n- **Fetch**: HyDE blog posts, Haystack docs, medium articles on query-generation methods\\n- **Key comparison**: HyDE requires LLM inference at retrieval time; TF-ISF requires zero LLM calls during retrieval\\n\\n## Phase 6: Related Work Synthesis & Positioning\\n\\n### 6.1 Comparative Analysis\\n- **Create a comparison table** (research_out.json) with rows = [TF-ISF, BM25F, Disco-RAG, HyDE, SF-RAG, CG-RAG, SURE-RAG, dense embeddings]\\n- **Columns**: Method, Granularity (document/section/chunk), External infrastructure required?, LLM inference at retrieval time?, Training required?, Key strengths, Key limitations, Citation count / maturity\\n- **Positioning**: Where does TF-ISF sit? Nearest neighbors in the design space?\\n\\n### 6.2 Novelty Assessment\\n- **Question 1**: Is within-document ISF explicitly proposed in prior work? (Expected answer: No, but BM25F and field weighting are close cousins)\\n- **Question 2**: Has anyone proposed section-frequency-based reweighting for scientific paper retrieval? (Expected: No, but discourse-aware and hierarchy-aware systems are emerging)\\n- **Question 3**: Has the claim/evidence vocabulary gap in IMRaD been formally studied empirically? (Expected: Theoretically motivated but not quantified at scale in QASPER era)\\n\\n### 6.3 Contextualize the Null Result\\n- **Key finding to synthesize**: If TF-ISF achieved F1=0.187 (no better than cosine 0.198 or BM25 0.179, p>0.37), why?\\n  - **Hypothesis A**: The vocabulary gap assumption is wrong; Methods/Results sections do NOT use more unique vocabulary (confirmed by ISF scores: Methods ISF 1.23–1.24 < Intro ISF 1.34)\\n  - **Hypothesis B**: Even if Methods sections had high ISF, the problem is not ranking (both achieve similar section recall ~0.48) but reader quality\\n  - **Hypothesis C**: Section granularity is too coarse; within-section vocabulary mismatch is the bottleneck\\n  - **Synthesis**: Disco-RAG, SCITREERAG, and fine-tuned embedders suggest future work should target (1) finer-grained retrieval (paragraph/sentence level), (2) discourse or embedding structure, (3) domain-specific models\\n\\n## Phase 7: Report Structure & Output Format\\n\\n### Output Files\\n- **research_out.json**: Structured output with fields:\\n  - `answer`: 2–3 paragraph summary of findings (novelty claim, key prior work landscape, positioning)\\n  - `sources`: Comprehensive bibliography (≥20 citations with BibTeX entries where possible)\\n  - `follow_up_questions`: 5–8 open questions for the executor (e.g., \\\"Did embedding quality on scientific domain improve 2023–2026?\\\", \\\"Has fine-tuned dense retrieval been evaluated on QASPER per-section?\\\")\\n  - `comparative_table`: JSON table comparing methods (TF-ISF vs. Disco-RAG vs. BM25F vs. HyDE vs. dense embeddings)\\n  - `vocabulary_stratification_evidence`: Summary of whether IMRaD vocabulary gap is empirically confirmed or merely theoretical\\n  - `section_retrieval_bottlenecks`: Structured analysis of whether bottleneck is (a) ranking function, (b) reader quality, (c) section granularity, (d) embedding domain gap\\n\\n- **research_report.md**: Narrative report with sections:\\n  1. Executive Summary (novelty + position in landscape)\\n  2. Within-Document Term Weighting Landscape (IDF theory, BM25F, prior ISF work)\\n  3. Section-Aware & Hierarchical Retrieval (IntrAgent, SCITREERAG, Disco-RAG comparison)\\n  4. IMRaD Vocabulary Stratification (theory + evidence)\\n  5. Query-Evidence Mismatch in Scientific QA (QASPER, dense retrieval quality, HyDE)\\n  6. Comparative Analysis Table\\n  7. Null Result Contextualization (why TF-ISF did not improve F1)\\n  8. Future Directions (discourse-aware, fine-tuned embeddings, finer granularity)\\n\\n### Research Quality Checkpoints\\n- ✓ Fetch & extract at least 1 foundational paper per theme (Spärck Jones 1972, Zaragoza 2004, Disco-RAG, QASPER, HyDE)\\n- ✓ Quantify claim with numbers (QASPER: 1,585 papers, 5,049 questions; null result: p>0.37, d<0.10; ISF gap: Methods 1.23–1.24 vs. Intro 1.34)\\n- ✓ Create comparative table with ≥5 related methods\\n- ✓ Identify at least 3 future directions (discourse, fine-tuning, granularity)\\n- ✓ Cite ≥20 sources across all themes\\n\\n## Executor Notes\\n- **Time allocation** (within 3h budget):\\n  - Phase 1–2: 30 min (foundational theory + BM25F)\\n  - Phase 3: 40 min (IntrAgent, SCITREERAG, Disco-RAG, dense methods)\\n  - Phase 4: 30 min (IMRaD studies, vocabulary stratification)\\n  - Phase 5: 45 min (QASPER analysis, dense retrieval, HyDE)\\n  - Phase 6–7: 35 min (synthesis, report writing)\\n- **Cost tracking**: Each web search is ~free (via Serper). Each fetch of a 2–10 page paper via WebFetch is ~free. Budget is for potential deep-reading LLM calls if synthesis requires extracting complex details; keep to <$1 total.\\n- **Failure scenarios**:\\n  - If QASPER paper is not fetchable: Use the README + search results; section uniformity is already confirmed in search snippets\\n  - If Disco-RAG PDF doesn't parse: HTML version is available; fetch that instead\\n  - If no empirical vocabulary stratification study exists: Frame as \\\"vocabulary gap is theoretically motivated but empirically unquantified,\\\" which is still a valid finding\\n- **Success criteria**:\\n  - Novelty claim is clear and specific: TF-ISF is a direct within-document application of IDF; closest prior is BM25F (field-level, not section-level, and for flat documents not IMRaD papers)\\n  - Null result is contextualized: ISF assumption (Methods sections have higher ISF) is empirically inverted; bottleneck is not ranking but reader or embedding quality\\n  - Future work is actionable: Disco-RAG, fine-tuned embeddings, paragraph-level retrieval are concrete next steps\\n  - Bibliography is comprehensive and well-organized (20+ citations)\\n\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [53] ASSISTANT · 2026-07-20 11:46:31 UTC

```
Perfect! I've created a comprehensive, actionable research plan for the artifact executor. Here's what I've delivered:

## Plan Summary

I conducted web research across 5 major themes and created a detailed **7-phase research plan** that guides the executor through:

1. **Foundational Theory** (Within-document IDF, probabilistic language models) — establishing theoretical context
2. **Field-Weighted Retrieval** (BM25F, Zaragoza 2004) — identifying the closest industrial prior work
3. **Section-Aware & Hierarchical Retrieval** (IntrAgent, SCITREERAG, Disco-RAG) — mapping the modern landscape
4. **IMRaD Vocabulary Stratification** — testing the core assumption (empirically inverted: Methods sections have *lower* ISF than Intro)
5. **Query-Evidence Mismatch** (QASPER dataset, dense retrieval quality, HyDE) — understanding scientific QA bottlenecks
6. **Null Result Synthesis** — contextualizing why TF-ISF achieved F1=0.187 (no better than cosine/BM25)
7. **Report Structure** — output format (research_out.json + research_report.md with 20+ citations)

## Key Research Findings Already Gathered

- **QASPER** (1,585 papers, 5,049 questions) has *uniform* section distribution for evidence (no section dominates)
- **Disco-RAG** (2025) uses RST discourse trees; requires external parsing (vs. TF-ISF: zero infrastructure)
- **BM25F** (Zaragoza 2004) is the field-weighted standard; computes global IDF, not per-field ISF
- **Dense embedding quality**: PubMedBERT, SciBERT, SPECTER address domain gap but no per-section analysis in literature
- **Vocabulary mismatch**: 30-40% of query terms don't appear in relevant documents (well-documented problem)
- **HyDE**: Generates hypothetical answers to bridge vocabulary gap, but requires LLM inference at retrieval time

## Plan Specificity for Executor

Each phase includes:
- **Search scope**: Exact keywords and paper titles
- **Fetch targets**: Which papers to read and what to extract
- **Key questions**: What the executor should verify
- **Comparison framework**: How to position TF-ISF relative to each method

**Time budget**: 30 min (theory) + 40 min (modern methods) + 30 min (IMRaD) + 45 min (scientific QA) + 35 min (synthesis)

**Output requirements**: Comparative table, novelty statement, contextualization of null result, 20+ citations

The plan file is ready at `./.terminal_claude_agent_struct_out.json`.
```

### [54] SYSTEM-USER prompt · 2026-07-20 11:46:33 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `<root>`: 'explanation' is a required property
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [55] TOOL CALL — Write · 2026-07-20 11:47:32 UTC

```
File: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "Within-Document Term Weighting Prior Work Survey",
  "summary": "Comprehensive literature survey to establish novelty and contextualize TF-ISF within the landscape of within-document term reweighting, field-weighted retrieval, section-aware ranking, vocabulary stratification in IMRaD papers, and query-evidence mismatch in scientific QA.",
  "explanation": "This research matters because the hypothesis claims that TF-ISF (within-document Inverse Section Frequency) is a novel approach to correct systematic retrieval bias in scientific papers, but the null result suggests the mechanism itself may be flawed. Prior work survey establishes: (1) whether within-document term reweighting has been explored before (novelty claim), (2) how modern section-aware methods (Disco-RAG, SCITREERAG) compare to static term weighting, (3) whether the vocabulary stratification assumption (Methods sections use unique vocabulary) is empirically supported in QASPER, and (4) what the true bottlenecks are (embedding quality, section granularity, reader capacity vs. ranking function). This survey enables precise positioning of the null result within the broader landscape and identifies whether future work should pursue discourse-aware methods, fine-tuned embeddings, or finer-grained retrieval rather than static term reweighting.",
  "runpod_compute_profile": "cpu_light",
  "question": "How do prior approaches to within-document term weighting, field-weighted retrieval, and section-aware ranking in scientific papers compare to TF-ISF, and what evidence exists for vocabulary stratification between IMRaD sections?",
  "research_plan": "## Phase 1: Within-Document Term Weighting & IDF Variants (Search, Fetch, Synthesize)\n\n### 1.1 Foundational IDF and Term Weighting Theory\n- **Search scope**: Spärck Jones (1972) IDF pioneer work, Singhal et al. (1996) pivoted normalization, Robertson & Jones (1976), Salton & Buckley (1987) tf-idf theory\n- **Target**: Establish that classical IDF is cross-corpus; identify historical precedent (if any) for within-document variants\n- **Fetch**: Stanford IR Book Ch.6 (vector space model, term weighting), key foundational papers on tf-idf justification\n- **Extract specifics**: Exact mathematical definitions of IDF, document frequency vs. section frequency, any mention of intra-document frequency variants\n- **Key question to answer**: Are there published precedents for within-document IDF or section-based IDF before this work? What probabilistic justifications exist for tf-idf that might extend to ISF?\n\n### 1.2 Probabilistic Language Models for Retrieval\n- **Search scope**: Probabilistic language models (Hiemstra 1998 and later), Okapi BM25 (Robertson et al.), query likelihood models, language model smoothing\n- **Target**: Understand how probabilistic frameworks assign term weights; identify if any naturally extend to section-level granularity\n- **Fetch**: Papers on Dirichlet smoothing, collection model variants, position-aware language models\n- **Key question**: Do probabilistic models explicitly handle multi-level structures (document + section)? Any prior work on section-specific language models?\n\n## Phase 2: Field-Weighted Retrieval (BM25F and Structured Documents)\n\n### 2.1 BM25F and Field-Weighted Extensions\n- **Search scope**: BM25F (Zaragoza et al. 2004 CIKM), field weighting in structured documents, BM25E for XML/hierarchical retrieval\n- **Target**: Establish that BM25F is the industrial standard for multi-field retrieval; clarify how field IDF is computed (per-field or global)\n- **Fetch**: Zaragoza et al. (2004) \"Simple BM25 extension to multiple weighted fields\", XML retrieval papers using BM25F\n- **Extract specifics**: Mathematical formulation of BM25F, how field weights are assigned, whether field-level ISF is ever discussed\n- **Key question**: Does BM25F compute per-field IDF or use global IDF? How does this relate to per-section ISF?\n\n### 2.2 Other Structured Document Retrieval Approaches\n- **Search scope**: Hierarchical BM25, Zaragoza et al. field boost experiments, weight tuning methods\n- **Target**: Understand what field weighting techniques exist beyond basic BM25F\n- **Key question**: Have researchers tuned section-specific boost weights empirically? Any ablations on field IDF vs. boost?\n\n## Phase 3: Section-Aware & Hierarchical Retrieval in Scientific Papers\n\n### 3.1 Recent Structure-Aware RAG Systems\n- **Search scope**: IntrAgent (2024), SCITREERAG, Disco-RAG (2025 arxiv 2601.04377), SF-RAG (2026 arxiv 2602.13647), hierarchical document graphs\n- **Target**: Map the landscape of recent approaches that exploit document structure; identify which use term weighting vs. embedding-only vs. discourse\n- **Fetch**: IntrAgent paper (arxiv 2604.22861) for similarity-based section selection; Disco-RAG for discourse-aware approach; SCITREERAG for tree-based hierarchy\n- **Extract**: How each method ranks or retrieves sections; whether they use term statistics, embeddings, discourse, or hybrid; computational cost\n- **Key comparison points vs. TF-ISF**:\n  - Disco-RAG: Requires RST parsing + inter-chunk graphs (external model), operates on generation coherence not retrieval scoring → TF-ISF requires zero external infrastructure\n  - SF-RAG: Routes via pre-built structural index; TF-ISF reweights term-section matches post-hoc without indexing infrastructure\n  - IntrAgent: Similarity-based section selection on embeddings; TF-ISF is sparse-term based\n\n### 3.2 Hierarchical Document Structure in Dense Retrieval\n- **Search scope**: Hierarchy-aware aggregation (paragraph→section→document embeddings), OMRC-MR structure-aware re-ranking, in-paper hierarchy for semantic coherence\n- **Target**: Understand how dense embeddings handle multi-level structure\n- **Key question**: Do dense methods suffer from the same claim-section bias? Any evidence that embedding quality differs across IMRaD sections?\n\n## Phase 4: Vocabulary Stratification in IMRaD Scientific Papers\n\n### 4.1 IMRaD Writing Convention & Section Characteristics\n- **Search scope**: IMRaD format survey papers, abstract composition studies (arxiv 1604.02580), section length and content distribution\n- **Target**: Establish that IMRaD is standard in scientific papers; confirm claim vs. evidence vocabulary split is theoretically motivated\n- **Fetch**: 50-year IMRaD survey, abstract composition paper\n- **Extract**: Typical section lengths, reuse of topic terms across sections, any linguistic analysis of vocabulary differences\n- **Key question**: Is there published linguistic evidence that Abstract/Introduction use more shared vocabulary than Methods/Results within the same paper?\n\n### 4.2 Empirical Vocabulary Analysis in Scientific Corpora\n- **Search scope**: Claim vs. evidence language studies, discourse-aware scientific summarization, vocabulary analysis in scientific papers\n- **Target**: Find prior empirical studies that measure vocabulary overlap between sections\n- **Fetch**: Discourse-aware summarization papers (arxiv 2005.00513 if readable)\n- **Key question**: Has anyone quantified section-level vocabulary overlap? Any evidence that Methods/Results sections contain unique terms?\n\n## Phase 5: Query-Evidence Vocabulary Mismatch in Scientific QA\n\n### 5.1 Vocabulary Mismatch Problem (General)\n- **Search scope**: General vocabulary mismatch in IR (30-40% term failure rate), query expansion techniques, lexical gaps in QA\n- **Target**: Establish that query-document vocabulary mismatch is a well-known problem; understand standard mitigation strategies\n- **Fetch**: Vocabulary mismatch Wikipedia, RQUERY paper, vocabulary avoidance techniques\n- **Extract**: Quantified statistics on mismatch rate, solutions attempted (expansion, paraphrase, dense embeddings)\n- **Key question**: Is within-document term reweighting ever proposed as a solution?\n\n### 5.2 Vocabulary Mismatch in Scientific QA Specifically\n- **Search scope**: QASPER dataset annotation studies, SciQA, dense retrieval for scientific papers, domain-specific embedding fine-tuning\n- **Target**: Understand whether scientific QA exhibits different vocabulary mismatch patterns; identify bottlenecks empirically\n- **Fetch**: QASPER dataset paper (README or arxiv 2105.03011), QASA paper, SciDQA, CG-RAG (citation-graph RAG)\n- **Extract from QASPER**:\n  - Dataset size (1,585 papers, 5,049 questions confirmed)\n  - Evidence distribution across sections (confirmed: uniform, no majority-holding section)\n  - Types of questions (factual, numerical, synthesis, etc.)\n  - Current baseline performance levels (dense retrieval F1, sparse F1, reader F1)\n- **Key question**: Which sections (Abstract vs. Methods) contain correct answers most often? How does cosine similarity rank these sections for queries with evidence in Methods/Results?\n\n### 5.3 Domain-Specific Dense Retrieval Quality\n- **Search scope**: PubMedBERT, SciBERT, SPECTER, domain-adaptive dense retrievers, pre-training vs. fine-tuning for scientific retrieval (arxiv 2505.07166)\n- **Target**: Identify gaps in dense embedding quality for scientific domain; confirm that general-purpose embedders underperform\n- **Fetch**: PubMedBERT docs, Pre-training vs Fine-tuning paper (2505.07166), PairSem for scientific doc retrieval\n- **Extract**: Performance numbers on scientific benchmarks (QASPER, SciDQA), evidence that fine-tuning helps, any failure analysis on section types\n- **Key question**: Can fine-tuning dense embedders solve the section retrieval problem? Or is the bottleneck fundamental (coarse granularity, query phrasing)?\n\n### 5.4 HyDE and Query-Generation Approaches\n- **Search scope**: HyDE (hypothetical document embeddings), query generation for domain shift, LLM-in-the-loop retrieval\n- **Target**: Understand alternative approaches to vocabulary mismatch that use LLM generation\n- **Fetch**: HyDE blog posts, Haystack docs, medium articles on query-generation methods\n- **Key comparison**: HyDE requires LLM inference at retrieval time; TF-ISF requires zero LLM calls during retrieval\n\n## Phase 6: Related Work Synthesis & Positioning\n\n### 6.1 Comparative Analysis\n- **Create a comparison table** (research_out.json) with rows = [TF-ISF, BM25F, Disco-RAG, HyDE, SF-RAG, CG-RAG, SURE-RAG, dense embeddings]\n- **Columns**: Method, Granularity (document/section/chunk), External infrastructure required?, LLM inference at retrieval time?, Training required?, Key strengths, Key limitations, Citation count / maturity\n- **Positioning**: Where does TF-ISF sit? Nearest neighbors in the design space?\n\n### 6.2 Novelty Assessment\n- **Question 1**: Is within-document ISF explicitly proposed in prior work? (Expected answer: No, but BM25F and field weighting are close cousins)\n- **Question 2**: Has anyone proposed section-frequency-based reweighting for scientific paper retrieval? (Expected: No, but discourse-aware and hierarchy-aware systems are emerging)\n- **Question 3**: Has the claim/evidence vocabulary gap in IMRaD been formally studied empirically? (Expected: Theoretically motivated but not quantified at scale in QASPER era)\n\n### 6.3 Contextualize the Null Result\n- **Key finding to synthesize**: If TF-ISF achieved F1=0.187 (no better than cosine 0.198 or BM25 0.179, p>0.37), why?\n  - **Hypothesis A**: The vocabulary gap assumption is wrong; Methods/Results sections do NOT use more unique vocabulary (confirmed by ISF scores: Methods ISF 1.23–1.24 < Intro ISF 1.34)\n  - **Hypothesis B**: Even if Methods sections had high ISF, the problem is not ranking (both achieve similar section recall ~0.48) but reader quality\n  - **Hypothesis C**: Section granularity is too coarse; within-section vocabulary mismatch is the bottleneck\n  - **Synthesis**: Disco-RAG, SCITREERAG, and fine-tuned embedders suggest future work should target (1) finer-grained retrieval (paragraph/sentence level), (2) discourse or embedding structure, (3) domain-specific models\n\n## Phase 7: Report Structure & Output Format\n\n### Output Files\n- **research_out.json**: Structured output with fields:\n  - `answer`: 2–3 paragraph summary of findings (novelty claim, key prior work landscape, positioning)\n  - `sources`: Comprehensive bibliography (≥20 citations with BibTeX entries where possible)\n  - `follow_up_questions`: 5–8 open questions for the executor (e.g., \"Did embedding quality on scientific domain improve 2023–2026?\", \"Has fine-tuned dense retrieval been evaluated on QASPER per-section?\")\n  - `comparative_table`: JSON table comparing methods (TF-ISF vs. Disco-RAG vs. BM25F vs. HyDE vs. dense embeddings)\n  - `vocabulary_stratification_evidence`: Summary of whether IMRaD vocabulary gap is empirically confirmed or merely theoretical\n  - `section_retrieval_bottlenecks`: Structured analysis of whether bottleneck is (a) ranking function, (b) reader quality, (c) section granularity, (d) embedding domain gap\n\n- **research_report.md**: Narrative report with sections:\n  1. Executive Summary (novelty + position in landscape)\n  2. Within-Document Term Weighting Landscape (IDF theory, BM25F, prior ISF work)\n  3. Section-Aware & Hierarchical Retrieval (IntrAgent, SCITREERAG, Disco-RAG comparison)\n  4. IMRaD Vocabulary Stratification (theory + evidence)\n  5. Query-Evidence Mismatch in Scientific QA (QASPER, dense retrieval quality, HyDE)\n  6. Comparative Analysis Table\n  7. Null Result Contextualization (why TF-ISF did not improve F1)\n  8. Future Directions (discourse-aware, fine-tuned embeddings, finer granularity)\n\n### Research Quality Checkpoints\n- ✓ Fetch & extract at least 1 foundational paper per theme (Spärck Jones 1972, Zaragoza 2004, Disco-RAG, QASPER, HyDE)\n- ✓ Quantify claim with numbers (QASPER: 1,585 papers, 5,049 questions; null result: p>0.37, d<0.10; ISF gap: Methods 1.23–1.24 vs. Intro 1.34)\n- ✓ Create comparative table with ≥5 related methods\n- ✓ Identify at least 3 future directions (discourse, fine-tuning, granularity)\n- ✓ Cite ≥20 sources across all themes\n\n## Executor Notes\n- **Time allocation** (within 3h budget):\n  - Phase 1–2: 30 min (foundational theory + BM25F)\n  - Phase 3: 40 min (IntrAgent, SCITREERAG, Disco-RAG, dense methods)\n  - Phase 4: 30 min (IMRaD studies, vocabulary stratification)\n  - Phase 5: 45 min (QASPER analysis, dense retrieval, HyDE)\n  - Phase 6–7: 35 min (synthesis, report writing)\n- **Cost tracking**: Each web search is ~free (via Serper). Each fetch of a 2–10 page paper via WebFetch is ~free. Budget is for potential deep-reading LLM calls if synthesis requires extracting complex details; keep to <$1 total.\n- **Failure scenarios**:\n  - If QASPER paper is not fetchable: Use the README + search results; section uniformity is already confirmed in search snippets\n  - If Disco-RAG PDF doesn't parse: HTML version is available; fetch that instead\n  - If no empirical vocabulary stratification study exists: Frame as \"vocabulary gap is theoretically motivated but empirically unquantified,\" which is still a valid finding\n- **Success criteria**:\n  - Novelty claim is clear and specific: TF-ISF is a direct within-document application of IDF; closest prior is BM25F (field-level, not section-level, and for flat documents not IMRaD papers)\n  - Null result is contextualized: ISF assumption (Methods sections have higher ISF) is empirically inverted; bottleneck is not ranking but reader or embedding quality\n  - Future work is actionable: Disco-RAG, fine-tuned embeddings, paragraph-level retrieval are concrete next steps\n  - Bibliography is comprehensive and well-organized (20+ citations)\n"
}
```

### [56] TOOL RESULT — Write · 2026-07-20 11:47:32 UTC

```
{"type": "update", "filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Within-Document Term Weighting Prior Work Survey\",\n  \"summary\": \"Comprehensive literature survey to establish novelty and contextualize TF-ISF within the landscape of within-document term reweighting, field-weighted retrieval, section-aware ranking, vocabulary stratification in IMRaD papers, and query-evidence mismatch in scientific QA.\",\n  \"explanation\": \"This research matters because the hypothesis claims that TF-ISF (within-document Inverse Section Frequency) is a novel approach to correct systematic retrieval bias in scientific papers, but the null result suggests the mechanism itself may be flawed. Prior work survey establishes: (1) whether within-document term reweighting has been explored before (novelty claim), (2) how modern section-aware methods (Disco-RAG, SCITREERAG) compare to static term weighting, (3) whether the vocabulary stratification assumption (Methods sections use unique vocabulary) is empirically supported in QASPER, and (4) what the true bottlenecks are (embedding quality, section granularity, reader capacity vs. ranking function). This survey enables precise positioning of the null result within the broader landscape and identifies whether future work should pursue discourse-aware methods, fine-tuned embeddings, or finer-grained retrieval rather than static term reweighting.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"How do prior approaches to within-document term weighting, field-weighted retrieval, and section-aware ranking in scientific papers compare to TF-ISF, and what evidence exists for vocabulary stratification between IMRaD sections?\",\n  \"research_plan\": \"## Phase 1: Within-Document Term Weighting & IDF Variants (Search, Fetch, Synthesize)\\n\\n### 1.1 Foundational IDF and Term Weighting Theory\\n- **Search scope**: Spärck Jones (1972) IDF pioneer work, Singhal et al. (1996) pivoted normalization, Robertson & Jones (1976), Salton & Buckley (1987) tf-idf theory\\n- **Target**: Establish that classical IDF is cross-corpus; identify historical precedent (if any) for within-document variants\\n- **Fetch**: Stanford IR Book Ch.6 (vector space model, term weighting), key foundational papers on tf-idf justification\\n- **Extract specifics**: Exact mathematical definitions of IDF, document frequency vs. section frequency, any mention of intra-document frequency variants\\n- **Key question to answer**: Are there published precedents for within-document IDF or section-based IDF before this work? What probabilistic justifications exist for tf-idf that might extend to ISF?\\n\\n### 1.2 Probabilistic Language Models for Retrieval\\n- **Search scope**: Probabilistic language models (Hiemstra 1998 and later), Okapi BM25 (Robertson et al.), query likelihood models, language model smoothing\\n- **Target**: Understand how probabilistic frameworks assign term weights; identify if any naturally extend to section-level granularity\\n- **Fetch**: Papers on Dirichlet smoothing, collection model variants, position-aware language models\\n- **Key question**: Do probabilistic models explicitly handle multi-level structures (document + section)? Any prior work on section-specific language models?\\n\\n## Phase 2: Field-Weighted Retrieval (BM25F and Structured Documents)\\n\\n### 2.1 BM25F and Field-Weighted Extensions\\n- **Search scope**: BM25F (Zaragoza et al. 2004 CIKM), field weighting in structured documents, BM25E for XML/hierarchical retrieval\\n- **Target**: Establish that BM25F is the industrial standard for multi-field retrieval; clarify how field IDF is computed (per-field or global)\\n- **Fetch**: Zaragoza et al. (2004) \\\"Simple BM25 extension to multiple weighted fields\\\", XML retrieval papers using BM25F\\n- **Extract specifics**: Mathematical formulation of BM25F, how field weights are assigned, whether field-level ISF is ever discussed\\n- **Key question**: Does BM25F compute per-field IDF or use global IDF? How does this relate to per-section ISF?\\n\\n### 2.2 Other Structured Document Retrieval Approaches\\n- **Search scope**: Hierarchical BM25, Zaragoza et al. field boost experiments, weight tuning methods\\n- **Target**: Understand what field weighting techniques exist beyond basic BM25F\\n- **Key question**: Have researchers tuned section-specific boost weights empirically? Any ablations on field IDF vs. boost?\\n\\n## Phase 3: Section-Aware & Hierarchical Retrieval in Scientific Papers\\n\\n### 3.1 Recent Structure-Aware RAG Systems\\n- **Search scope**: IntrAgent (2024), SCITREERAG, Disco-RAG (2025 arxiv 2601.04377), SF-RAG (2026 arxiv 2602.13647), hierarchical document graphs\\n- **Target**: Map the landscape of recent approaches that exploit document structure; identify which use term weighting vs. embedding-only vs. discourse\\n- **Fetch**: IntrAgent paper (arxiv 2604.22861) for similarity-based section selection; Disco-RAG for discourse-aware approach; SCITREERAG for tree-based hierarchy\\n- **Extract**: How each method ranks or retrieves sections; whether they use term statistics, embeddings, discourse, or hybrid; computational cost\\n- **Key comparison points vs. TF-ISF**:\\n  - Disco-RAG: Requires RST parsing + inter-chunk graphs (external model), operates on generation coherence not retrieval scoring → TF-ISF requires zero external infrastructure\\n  - SF-RAG: Routes via pre-built structural index; TF-ISF reweights term-section matches post-hoc without indexing infrastructure\\n  - IntrAgent: Similarity-based section selection on embeddings; TF-ISF is sparse-term based\\n\\n### 3.2 Hierarchical Document Structure in Dense Retrieval\\n- **Search scope**: Hierarchy-aware aggregation (paragraph→section→document embeddings), OMRC-MR structure-aware re-ranking, in-paper hierarchy for semantic coherence\\n- **Target**: Understand how dense embeddings handle multi-level structure\\n- **Key question**: Do dense methods suffer from the same claim-section bias? Any evidence that embedding quality differs across IMRaD sections?\\n\\n## Phase 4: Vocabulary Stratification in IMRaD Scientific Papers\\n\\n### 4.1 IMRaD Writing Convention & Section Characteristics\\n- **Search scope**: IMRaD format survey papers, abstract composition studies (arxiv 1604.02580), section length and content distribution\\n- **Target**: Establish that IMRaD is standard in scientific papers; confirm claim vs. evidence vocabulary split is theoretically motivated\\n- **Fetch**: 50-year IMRaD survey, abstract composition paper\\n- **Extract**: Typical section lengths, reuse of topic terms across sections, any linguistic analysis of vocabulary differences\\n- **Key question**: Is there published linguistic evidence that Abstract/Introduction use more shared vocabulary than Methods/Results within the same paper?\\n\\n### 4.2 Empirical Vocabulary Analysis in Scientific Corpora\\n- **Search scope**: Claim vs. evidence language studies, discourse-aware scientific summarization, vocabulary analysis in scientific papers\\n- **Target**: Find prior empirical studies that measure vocabulary overlap between sections\\n- **Fetch**: Discourse-aware summarization papers (arxiv 2005.00513 if readable)\\n- **Key question**: Has anyone quantified section-level vocabulary overlap? Any evidence that Methods/Results sections contain unique terms?\\n\\n## Phase 5: Query-Evidence Vocabulary Mismatch in Scientific QA\\n\\n### 5.1 Vocabulary Mismatch Problem (General)\\n- **Search scope**: General vocabulary mismatch in IR (30-40% term failure rate), query expansion techniques, lexical gaps in QA\\n- **Target**: Establish that query-document vocabulary mismatch is a well-known problem; understand standard mitigation strategies\\n- **Fetch**: Vocabulary mismatch Wikipedia, RQUERY paper, vocabulary avoidance techniques\\n- **Extract**: Quantified statistics on mismatch rate, solutions attempted (expansion, paraphrase, dense embeddings)\\n- **Key question**: Is within-document term reweighting ever proposed as a solution?\\n\\n### 5.2 Vocabulary Mismatch in Scientific QA Specifically\\n- **Search scope**: QASPER dataset annotation studies, SciQA, dense retrieval for scientific papers, domain-specific embedding fine-tuning\\n- **Target**: Understand whether scientific QA exhibits different vocabulary mismatch patterns; identify bottlenecks empirically\\n- **Fetch**: QASPER dataset paper (README or arxiv 2105.03011), QASA paper, SciDQA, CG-RAG (citation-graph RAG)\\n- **Extract from QASPER**:\\n  - Dataset size (1,585 papers, 5,049 questions confirmed)\\n  - Evidence distribution across sections (confirmed: uniform, no majority-holding section)\\n  - Types of questions (factual, numerical, synthesis, etc.)\\n  - Current baseline performance levels (dense retrieval F1, sparse F1, reader F1)\\n- **Key question**: Which sections (Abstract vs. Methods) contain correct answers most often? How does cosine similarity rank these sections for queries with evidence in Methods/Results?\\n\\n### 5.3 Domain-Specific Dense Retrieval Quality\\n- **Search scope**: PubMedBERT, SciBERT, SPECTER, domain-adaptive dense retrievers, pre-training vs. fine-tuning for scientific retrieval (arxiv 2505.07166)\\n- **Target**: Identify gaps in dense embedding quality for scientific domain; confirm that general-purpose embedders underperform\\n- **Fetch**: PubMedBERT docs, Pre-training vs Fine-tuning paper (2505.07166), PairSem for scientific doc retrieval\\n- **Extract**: Performance numbers on scientific benchmarks (QASPER, SciDQA), evidence that fine-tuning helps, any failure analysis on section types\\n- **Key question**: Can fine-tuning dense embedders solve the section retrieval problem? Or is the bottleneck fundamental (coarse granularity, query phrasing)?\\n\\n### 5.4 HyDE and Query-Generation Approaches\\n- **Search scope**: HyDE (hypothetical document embeddings), query generation for domain shift, LLM-in-the-loop retrieval\\n- **Target**: Understand alternative approaches to vocabulary mismatch that use LLM generation\\n- **Fetch**: HyDE blog posts, Haystack docs, medium articles on query-generation methods\\n- **Key comparison**: HyDE requires LLM inference at retrieval time; TF-ISF requires zero LLM calls during retrieval\\n\\n## Phase 6: Related Work Synthesis & Positioning\\n\\n### 6.1 Comparative Analysis\\n- **Create a comparison table** (research_out.json) with rows = [TF-ISF, BM25F, Disco-RAG, HyDE, SF-RAG, CG-RAG, SURE-RAG, dense embeddings]\\n- **Columns**: Method, Granularity (document/section/chunk), External infrastructure required?, LLM inference at retrieval time?, Training required?, Key strengths, Key limitations, Citation count / maturity\\n- **Positioning**: Where does TF-ISF sit? Nearest neighbors in the design space?\\n\\n### 6.2 Novelty Assessment\\n- **Question 1**: Is within-document ISF explicitly proposed in prior work? (Expected answer: No, but BM25F and field weighting are close cousins)\\n- **Question 2**: Has anyone proposed section-frequency-based reweighting for scientific paper retrieval? (Expected: No, but discourse-aware and hierarchy-aware systems are emerging)\\n- **Question 3**: Has the claim/evidence vocabulary gap in IMRaD been formally studied empirically? (Expected: Theoretically motivated but not quantified at scale in QASPER era)\\n\\n### 6.3 Contextualize the Null Result\\n- **Key finding to synthesize**: If TF-ISF achieved F1=0.187 (no better than cosine 0.198 or BM25 0.179, p>0.37), why?\\n  - **Hypothesis A**: The vocabulary gap assumption is wrong; Methods/Results sections do NOT use more unique vocabulary (confirmed by ISF scores: Methods ISF 1.23–1.24 < Intro ISF 1.34)\\n  - **Hypothesis B**: Even if Methods sections had high ISF, the problem is not ranking (both achieve similar section recall ~0.48) but reader quality\\n  - **Hypothesis C**: Section granularity is too coarse; within-section vocabulary mismatch is the bottleneck\\n  - **Synthesis**: Disco-RAG, SCITREERAG, and fine-tuned embedders suggest future work should target (1) finer-grained retrieval (paragraph/sentence level), (2) discourse or embedding structure, (3) domain-specific models\\n\\n## Phase 7: Report Structure & Output Format\\n\\n### Output Files\\n- **research_out.json**: Structured output with fields:\\n  - `answer`: 2–3 paragraph summary of findings (novelty claim, key prior work landscape, positioning)\\n  - `sources`: Comprehensive bibliography (≥20 citations with BibTeX entries where possible)\\n  - `follow_up_questions`: 5–8 open questions for the executor (e.g., \\\"Did embedding quality on scientific domain improve 2023–2026?\\\", \\\"Has fine-tuned dense retrieval been evaluated on QASPER per-section?\\\")\\n  - `comparative_table`: JSON table comparing methods (TF-ISF vs. Disco-RAG vs. BM25F vs. HyDE vs. dense embeddings)\\n  - `vocabulary_stratification_evidence`: Summary of whether IMRaD vocabulary gap is empirically confirmed or merely theoretical\\n  - `section_retrieval_bottlenecks`: Structured analysis of whether bottleneck is (a) ranking function, (b) reader quality, (c) section granularity, (d) embedding domain gap\\n\\n- **research_report.md**: Narrative report with sections:\\n  1. Executive Summary (novelty + position in landscape)\\n  2. Within-Document Term Weighting Landscape (IDF theory, BM25F, prior ISF work)\\n  3. Section-Aware & Hierarchical Retrieval (IntrAgent, SCITREERAG, Disco-RAG comparison)\\n  4. IMRaD Vocabulary Stratification (theory + evidence)\\n  5. Query-Evidence Mismatch in Scientific QA (QASPER, dense retrieval quality, HyDE)\\n  6. Comparative Analysis Table\\n  7. Null Result Contextualization (why TF-ISF did not improve F1)\\n  8. Future Directions (discourse-aware, fine-tuned embeddings, finer granularity)\\n\\n### Research Quality Checkpoints\\n- ✓ Fetch & extract at least 1 foundational paper per theme (Spärck Jones 1972, Zaragoza 2004, Disco-RAG, QASPER, HyDE)\\n- ✓ Quantify claim with numbers (QASPER: 1,585 papers, 5,049 questions; null result: p>0.37, d<0.10; ISF gap: Methods 1.23–1.24 vs. Intro 1.34)\\n- ✓ Create comparative table with ≥5 related methods\\n- ✓ Identify at least 3 future directions (discourse, fine-tuning, granularity)\\n- ✓ Cite ≥20 sources across all themes\\n\\n## Executor Notes\\n- **Time allocation** (within 3h budget):\\n  - Phase 1–2: 30 min (foundational theory + BM25F)\\n  - Phase 3: 40 min (IntrAgent, SCITREERAG, Disco-RAG, dense methods)\\n  - Phase 4: 30 min (IMRaD studies, vocabulary stratification)\\n  - Phase 5: 45 min (QASPER analysis, dense retrieval, HyDE)\\n  - Phase 6–7: 35 min (synthesis, report writing)\\n- **Cost tracking**: Each web search is ~free (via Serper). Each fetch of a 2–10 page paper via WebFetch is ~free. Budget is for potential deep-reading LLM calls if synthesis requires extracting complex details; keep to <$1 total.\\n- **Failure scenarios**:\\n  - If QASPER paper is not fetchable: Use the README + search results; section uniformity is already confirmed in search snippets\\n  - If Disco-RAG PDF doesn't parse: HTML version is available; fetch that instead\\n  - If no empirical vocabulary stratification study exists: Frame as \\\"vocabulary gap is theoretically motivated but empirically unquantified,\\\" which is still a valid finding\\n- **Success criteria**:\\n  - Novelty claim is clear and specific: TF-ISF is a direct within-document application of IDF; closest prior is BM25F (field-level, not section-level, and for flat documents not IMRaD papers)\\n  - Null result is contextualized: ISF assumption (Methods sections have higher ISF) is empirically inverted; bottleneck is not ranking but reader or embedding quality\\n  - Future work is actionable: Disco-RAG, fine-tuned embeddings, paragraph-level retrieval are concrete next steps\\n  - Bibliography is comprehensive and well-organized (20+ citations)\\n\"\n}\n", "structuredPatch": [{"oldStart": 1, "oldLines": 6, "newStart": 1, "newLines": 7, "lines": [" {", "   \"title\": \"Within-Document Term Weighting Prior Work Survey\",", "   \"summary\": \"Comprehensive literature survey to establish novelty and contextualize TF-ISF within the landscape of within-document term reweighting, field-weighted retrieval, section-aware ranking, vocabulary stratification in IMRaD papers, and query-evidence mismatch in scientific QA.\",", "+  \"explanation\": \"This research matters because the hypothesis claims that TF-ISF (within-document Inverse Section Frequency) is a novel approach to correct systematic retrieval bias in scientific papers, but the null result suggests the mechanism itself may be flawed. Prior work survey establishes: (1) whether within-document term reweighting has been explored before (novelty claim), (2) how modern section-aware methods (Disco-RAG, SCITREERAG) compare to static term weighting, (3) whether the vocabulary stratification assumption (Methods sections use unique vocabulary) is empirically supported in QASPER, and (4) what the true bottlenecks are (embedding quality, section granularity, reader capacity vs. ranking function). This survey enables precise positioning of the null result within the broader landscape and identifies whether future work should pursue discourse-aware methods, fine-tuned embeddings, or finer-grained retrieval rather than static term reweighting.\",", "   \"runpod_compute_profile\": \"cpu_light\",", "   \"question\": \"How do prior approaches to within-document term weighting, field-weighted retrieval, and section-aware ranking in scientific papers compare to TF-ISF, and what evidence exists for vocabulary stratification between IMRaD sections?\",", "   \"research_plan\": \"## Phase 1: Within-Document Term Weighting & IDF Variants (Search, Fetch, Synthesize)\\n\\n### 1.1 Foundational IDF and Term Weighting Theory\\n- **Search scope**: Spärck Jones (1972) IDF pioneer work, Singhal et al. (1996) pivoted normalization, Robertson & Jones (1976), Salton & Buckley (1987) tf-idf theory\\n- **Target**: Establish that classical IDF is cross-corpus; identify historical precedent (if any) for within-document variants\\n- **Fetch**: Stanford IR Book Ch.6 (vector space model, term weighting), key foundational papers on tf-idf justification\\n- **Extract specifics**: Exact mathematical definitions of IDF, document frequency vs. section frequency, any mention of intra-document frequency variants\\n- **Key question to answer**: Are there published precedents for within-document IDF or section-based IDF before this work? What probabilistic justifications exist for tf-idf that might extend to ISF?\\n\\n### 1.2 Probabilistic Language Models for Retrieval\\n- **Search scope**: Probabilistic language models (Hiemstra 1998 and later), Okapi BM25 (Robertson et al.), query likelihood models, language model smoothing\\n- **Target**: Understand how probabilistic frameworks assign term weights; identify if any naturally extend to section-level granularity\\n- **Fetch**: Papers on Dirichlet smoothing, collection model variants, position-aware language models\\n- **Key question**: Do probabilistic models explicitly handle multi-level structures (document + section)? Any prior work on section-specific language models?\\n\\n## Phase 2: Field-Weighted Retrieval (BM25F and Structured Documents)\\n\\n### 2.1 BM25F and Field-Weighted Extensions\\n- **Search scope**: BM25F (Zaragoza et al. 2004 CIKM), field weighting in structured documents, BM25E for XML/hierarchical retrieval\\n- **Target**: Establish that BM25F is the industrial standard for multi-field retrieval; clarify how field IDF is computed (per-field or global)\\n- **Fetch**: Zaragoza et al. (2004) \\\"Simple BM25 extension to multiple weighted fields\\\", XML retrieval papers using BM25F\\n- **Extract specifics**: Mathematical formulation of BM25F, how field weights are assigned, whether field-level ISF is ever discussed\\n- **Key question**: Does BM25F compute per-field IDF or use global IDF? How does this relate to per-section ISF?\\n\\n### 2.2 Other Structured Document Retrieval Approaches\\n- **Search scope**: Hierarchical BM25, Zaragoza et al. field boost experiments, weight tuning methods\\n- **Target**: Understand what field weighting techniques exist beyond basic BM25F\\n- **Key question**: Have researchers tuned section-specific boost weights empirically? Any ablations on field IDF vs. boost?\\n\\n## Phase 3: Section-Aware & Hierarchical Retrieval in Scientific Papers\\n\\n### 3.1 Recent Structure-Aware RAG Systems\\n- **Search scope**: IntrAgent (2024), SCITREERAG, Disco-RAG (2025 arxiv 2601.04377), SF-RAG (2026 arxiv 2602.13647), hierarchical document graphs\\n- **Target**: Map the landscape of recent approaches that exploit document structure; identify which use term weighting vs. embedding-only vs. discourse\\n- **Fetch**: IntrAgent paper (arxiv 2604.22861) for similarity-based section selection; Disco-RAG for discourse-aware approach; SCITREERAG for tree-based hierarchy\\n- **Extract**: How each method ranks or retrieves sections; whether they use term statistics, embeddings, discourse, or hybrid; computational cost\\n- **Key comparison points vs. TF-ISF**:\\n  - Disco-RAG: Requires RST parsing + inter-chunk graphs (external model), operates on generation coherence not retrieval scoring → TF-ISF requires zero external infrastructure\\n  - SF-RAG: Routes via pre-built structural index; TF-ISF reweights term-section matches post-hoc without indexing infrastructure\\n  - IntrAgent: Similarity-based section selection on embeddings; TF-ISF is sparse-term based\\n\\n### 3.2 Hierarchical Document Structure in Dense Retrieval\\n- **Search scope**: Hierarchy-aware aggregation (paragraph→section→document embeddings), OMRC-MR structure-aware re-ranking, in-paper hierarchy for semantic coherence\\n- **Target**: Understand how dense embeddings handle multi-level structure\\n- **Key question**: Do dense methods suffer from the same claim-section bias? Any evidence that embedding quality differs across IMRaD sections?\\n\\n## Phase 4: Vocabulary Stratification in IMRaD Scientific Papers\\n\\n### 4.1 IMRaD Writing Convention & Section Characteristics\\n- **Search scope**: IMRaD format survey papers, abstract composition studies (arxiv 1604.02580), section length and content distribution\\n- **Target**: Establish that IMRaD is standard in scientific papers; confirm claim vs. evidence vocabulary split is theoretically motivated\\n- **Fetch**: 50-year IMRaD survey, abstract composition paper\\n- **Extract**: Typical section lengths, reuse of topic terms across sections, any linguistic analysis of vocabulary differences\\n- **Key question**: Is there published linguistic evidence that Abstract/Introduction use more shared vocabulary than Methods/Results within the same paper?\\n\\n### 4.2 Empirical Vocabulary Analysis in Scientific Corpora\\n- **Search scope**: Claim vs. evidence language studies, discourse-aware scientific summarization, vocabulary analysis in scientific papers\\n- **Target**: Find prior empirical studies that measure vocabulary overlap between sections\\n- **Fetch**: Discourse-aware summarization papers (arxiv 2005.00513 if readable)\\n- **Key question**: Has anyone quantified section-level vocabulary overlap? Any evidence that Methods/Results sections contain unique terms?\\n\\n## Phase 5: Query-Evidence Vocabulary Mismatch in Scientific QA\\n\\n### 5.1 Vocabulary Mismatch Problem (General)\\n- **Search scope**: General vocabulary mismatch in IR (30-40% term failure rate), query expansion techniques, lexical gaps in QA\\n- **Target**: Establish that query-document vocabulary mismatch is a well-known problem; understand standard mitigation strategies\\n- **Fetch**: Vocabulary mismatch Wikipedia, RQUERY paper, vocabulary avoidance techniques\\n- **Extract**: Quantified statistics on mismatch rate, solutions attempted (expansion, paraphrase, dense embeddings)\\n- **Key question**: Is within-document term reweighting ever proposed as a solution?\\n\\n### 5.2 Vocabulary Mismatch in Scientific QA Specifically\\n- **Search scope**: QASPER dataset annotation studies, SciQA, dense retrieval for scientific papers, domain-specific embedding fine-tuning\\n- **Target**: Understand whether scientific QA exhibits different vocabulary mismatch patterns; identify bottlenecks empirically\\n- **Fetch**: QASPER dataset paper (README or arxiv 2105.03011), QASA paper, SciDQA, CG-RAG (citation-graph RAG)\\n- **Extract from QASPER**:\\n  - Dataset size (1,585 papers, 5,049 questions confirmed)\\n  - Evidence distribution across sections (confirmed: uniform, no majority-holding section)\\n  - Types of questions (factual, numerical, synthesis, etc.)\\n  - Current baseline performance levels (dense retrieval F1, sparse F1, reader F1)\\n- **Key question**: Which sections (Abstract vs. Methods) contain correct answers most often? How does cosine similarity rank these sections for queries with evidence in Methods/Results?\\n\\n### 5.3 Domain-Specific Dense Retrieval Quality\\n- **Search scope**: PubMedBERT, SciBERT, SPECTER, domain-adaptive dense retrievers, pre-training vs. fine-tuning for scientific retrieval (arxiv 2505.07166)\\n- **Target**: Identify gaps in dense embedding quality for scientific domain; confirm that general-purpose embedders underperform\\n- **Fetch**: PubMedBERT docs, Pre-training vs Fine-tuning paper (2505.07166), PairSem for scientific doc retrieval\\n- **Extract**: Performance numbers on scientific benchmarks (QASPER, SciDQA), evidence that fine-tuning helps, any failure analysis on section types\\n- **Key question**: Can fine-tuning dense embedders solve the section retrieval problem? Or is the bottleneck fundamental (coarse granularity, query phrasing)?\\n\\n### 5.4 HyDE and Query-Generation Approaches\\n- **Search scope**: HyDE (hypothetical document embeddings), query generation for domain shift, LLM-in-the-loop retrieval\\n- **Target**: Understand alternative approaches to vocabulary mismatch that use LLM generation\\n- **Fetch**: HyDE blog posts, Haystack docs, medium articles on query-generation methods\\n- **Key comparison**: HyDE requires LLM inference at retrieval time; TF-ISF requires zero LLM calls during retrieval\\n\\n## Phase 6: Related Work Synthesis & Positioning\\n\\n### 6.1 Comparative Analysis\\n- **Create a comparison table** (research_out.json) with rows = [TF-ISF, BM25F, Disco-RAG, HyDE, SF-RAG, CG-RAG, SURE-RAG, dense embeddings]\\n- **Columns**: Method, Granularity (document/section/chunk), External infrastructure required?, LLM inference at retrieval time?, Training required?, Key strengths, Key limitations, Citation count / maturity\\n- **Positioning**: Where does TF-ISF sit? Nearest neighbors in the design space?\\n\\n### 6.2 Novelty Assessment\\n- **Question 1**: Is within-document ISF explicitly proposed in prior work? (Expected answer: No, but BM25F and field weighting are close cousins)\\n- **Question 2**: Has anyone proposed section-frequency-based reweighting for scientific paper retrieval? (Expected: No, but discourse-aware and hierarchy-aware systems are emerging)\\n- **Question 3**: Has the claim/evidence vocabulary gap in IMRaD been formally studied empirically? (Expected: Theoretically motivated but not quantified at scale in QASPER era)\\n\\n### 6.3 Contextualize the Null Result\\n- **Key finding to synthesize**: If TF-ISF achieved F1=0.187 (no better than cosine 0.198 or BM25 0.179, p>0.37), why?\\n  - **Hypothesis A**: The vocabulary gap assumption is wrong; Methods/Results sections do NOT use more unique vocabulary (confirmed by ISF scores: Methods ISF 1.23–1.24 < Intro ISF 1.34)\\n  - **Hypothesis B**: Even if Methods sections had high ISF, the problem is not ranking (both achieve similar section recall ~0.48) but reader quality\\n  - **Hypothesis C**: Section granularity is too coarse; within-section vocabulary mismatch is the bottleneck\\n  - **Synthesis**: Disco-RAG, SCITREERAG, and fine-tuned embedders suggest future work should target (1) finer-grained retrieval (paragraph/sentence level), (2) discourse or embedding structure, (3) domain-specific models\\n\\n## Phase 7: Report Structure & Output Format\\n\\n### Output Files\\n- **research_out.json**: Structured output with fields:\\n  - `answer`: 2–3 paragraph summary of findings (novelty claim, key prior work landscape, positioning)\\n  - `sources`: Comprehensive bibliography (≥20 citations with BibTeX entries where possible)\\n  - `follow_up_questions`: 5–8 open questions for the executor (e.g., \\\"Did embedding quality on scientific domain improve 2023–2026?\\\", \\\"Has fine-tuned dense retrieval been evaluated on QASPER per-section?\\\")\\n  - `comparative_table`: JSON table comparing methods (TF-ISF vs. Disco-RAG vs. BM25F vs. HyDE vs. dense embeddings)\\n  - `vocabulary_stratification_evidence`: Summary of whether IMRaD vocabulary gap is empirically confirmed or merely theoretical\\n  - `section_retrieval_bottlenecks`: Structured analysis of whether bottleneck is (a) ranking function, (b) reader quality, (c) section granularity, (d) embedding domain gap\\n\\n- **research_report.md**: Narrative report with sections:\\n  1. Executive Summary (novelty + position in landscape)\\n  2. Within-Document Term Weighting Landscape (IDF theory, BM25F, prior ISF work)\\n  3. Section-Aware & Hierarchical Retrieval (IntrAgent, SCITREERAG, Disco-RAG comparison)\\n  4. IMRaD Vocabulary Stratification (theory + evidence)\\n  5. Query-Evidence Mismatch in Scientific QA (QASPER, dense retrieval quality, HyDE)\\n  6. Comparative Analysis Table\\n  7. Null Result Contextualization (why TF-ISF did not improve F1)\\n  8. Future Directions (discourse-aware, fine-tuned embeddings, finer granularity)\\n\\n### Research Quality Checkpoints\\n- ✓ Fetch & extract at least 1 foundational paper per theme (Spärck Jones 1972, Zaragoza 2004, Disco-RAG, QASPER, HyDE)\\n- ✓ Quantify claim with numbers (QASPER: 1,585 papers, 5,049 questions; null result: p>0.37, d<0.10; ISF gap: Methods 1.23–1.24 vs. Intro 1.34)\\n- ✓ Create comparative table with ≥5 related methods\\n- ✓ Identify at least 3 future directions (discourse, fine-tuning, granularity)\\n- ✓ Cite ≥20 sources across all themes\\n\\n## Executor Notes\\n- **Time allocation** (within 3h budget):\\n  - Phase 1–2: 30 min (foundational theory + BM25F)\\n  - Phase 3: 40 min (IntrAgent, SCITREERAG, Disco-RAG, dense methods)\\n  - Phase 4: 30 min (IMRaD studies, vocabulary stratification)\\n  - Phase 5: 45 min (QASPER analysis, dense retrieval, HyDE)\\n  - Phase 6–7: 35 min (synthesis, report writing)\\n- **Cost tracking**: Each web search is ~free (via Serper). Each fetch of a 2–10 page paper via WebFetch is ~free. Budget is for potential deep-reading LLM calls if synthesis requires extracting complex details; keep to <$1 total.\\n- **Failure scenarios**:\\n  - If QASPER paper is not fetchable: Use the README + search results; section uniformity is already confirmed in search snippets\\n  - If Disco-RAG PDF doesn't parse: HTML version is available; fetch that instead\\n  - If no empirical vocabulary stratification study exists: Frame as \\\"vocabulary gap is theoretically motivated but empirically unquantified,\\\" which is still a valid finding\\n- **Success criteria**:\\n  - Novelty claim is clear and specific: TF-ISF is a direct within-document application of IDF; closest prior is BM25F (field-level, not section-level, and for flat documents not IMRaD papers)\\n  - Null result is contextualized: ISF assumption (Methods sections have higher ISF) is empirically inverted; bottleneck is not ranking but reader or embedding quality\\n  - Future work is actionable: Disco-RAG, fine-tuned embeddings, paragraph-level retrieval are concrete next steps\\n  - Bibliography is comprehensive and well-organized (20+ citations)\\n\""]}], "originalFile": null, "userModified": false}
```

### [57] ASSISTANT · 2026-07-20 11:47:38 UTC

```
Done! I've corrected the JSON by adding the required `explanation` field. The plan now includes:

**Fixed Schema:**
- ✓ `title`: "Within-Document Term Weighting Prior Work Survey"
- ✓ `explanation`: Detailed rationale for why this research matters, what questions it answers, and how it contextualizes the null result
- ✓ `research_plan`: 7-phase comprehensive plan with specific search scopes, fetch targets, and extraction goals
- ✓ `question`: Research question guiding the investigation
- ✓ `summary`: Brief overview
- ✓ `runpod_compute_profile`: "cpu_light"

The plan is now complete and ready for executor validation. It provides a detailed roadmap for surveying prior work across: within-document term weighting theory, field-weighted retrieval (BM25F), modern section-aware systems (Disco-RAG, IntrAgent), IMRaD vocabulary stratification, and query-evidence mismatch in scientific QA—all to establish novelty and contextualize the null result.
```
