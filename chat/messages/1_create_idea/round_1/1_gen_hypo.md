# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 1 · `gen_hypo`
> Run: `run_gjLlrqQuoUxT` — Within-Document Term Weighting for Scientific Section Retrieval: A Negative Result
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-20 10:00:56 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/iter_1/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-07-20 10:01:02 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-20 10:01:02 UTC

```
A compact retrieval-augmented summarizer for long scientific PDFs that ranks sections by query relevance, benchmarked on a small QA set for answer F1 against a fixed top-k baseline.
```

### [4] ASSISTANT · 2026-07-20 10:01:58 UTC

```
I'll load the web tools skill and brainstorm directions before searching.
```

### [5] TOOL CALL — Skill · 2026-07-20 10:01:58 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-20 10:01:58 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-07-20 10:02:04 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-07-20 10:02:04 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [9] ASSISTANT · 2026-07-20 10:02:10 UTC

```
Now I'll search in parallel across several promising directions.
```

### [10] TOOL CALL — WebSearch · 2026-07-20 10:02:10 UTC

```
rhetorical role aware retrieval scientific papers RAG section ranking 2024 2025
```

### [11] TOOL CALL — WebSearch · 2026-07-20 10:02:10 UTC

```
citation graph based document section retrieval scientific QA reranking
```

### [12] TOOL CALL — WebSearch · 2026-07-20 10:02:10 UTC

```
argument structure scientific paper RAG query relevance section retrieval 2024
```

### [13] TOOL CALL — WebSearch · 2026-07-20 10:02:10 UTC

```
iterative retrieval augmented generation state estimation control theory scientific papers
```

### [14] TOOL RESULT — WebSearch · 2026-07-20 10:02:16 UTC

```
{"query": "rhetorical role aware retrieval scientific papers RAG section ranking 2024 2025", "results": [{"tool_use_id": "srvtoolu_01X6s9pP9DbNPNkn6qmrJG5T", "content": [{"title": "Discourse-Aware Retrieval-Augmented Generation via Rhetorical Structure Modeling | OpenReview", "url": "https://openreview.net/forum?id=AWv0mlCeUk"}, {"title": "Retrieval-Augmented Generation (RAG): 2025 Definitive Guide", "url": "https://www.chitika.com/retrieval-augmented-generation-rag-the-definitive-guide-2025/"}, {"title": "Embedding-Based Context-Aware Reranker", "url": "https://arxiv.org/pdf/2510.13329"}, {"title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow", "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"}, {"title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers", "url": "https://arxiv.org/html/2506.00054v1"}, {"title": "Retrieval-Augmented Generation (RAG)", "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-b2f527f9-ed5b-4d55-bf40-48c4e873c676"}, {"title": "Disco-RAG: Discourse-Aware Retrieval-Augmented Generation", "url": "https://arxiv.org/html/2601.04377v5"}, {"title": "Rank4Gen: RAG-Preference-Aligned Document Set Selection and Ranking", "url": "https://arxiv.org/pdf/2601.11273"}, {"title": "Enhancing RAG and Knowledge Graphs with Discourse Boris Galitsky", "url": "https://dialogue-conf.org/wp-content/uploads/2025/04/GalitskyBIlvovskyDMorkovkinA.110.pdf"}]}, "Based on the search results, I found several relevant recent developments in rhetorical role-aware retrieval and RAG systems for scientific papers:\n\n## Key Recent Work (2024-2025):\n\n**Discourse-Aware RAG Approaches:**\n\nDiscourse-RAG is a structure-aware framework that explicitly injects discourse signals into the generation process by constructing intra-chunk rhetorical structure theory (RST) trees to capture local coherence hierarchies and building inter-chunk rhetorical graphs to model cross-passage discourse flow. Discourse-RAG achieves a new state-of-the-art ROUGE-L score of 42.4 on ASQA dataset and improves LLM Score by 12.79 points over standard RAG on Loong benchmark.\n\n**Disco-RAG:**\n\nDisco-RAG leverages intra-chunk discourse trees and inter-chunk rhetorical graphs to plan and orchestrate generation, vastly improving coherence on long/semi-structured inputs. Disco-RAG outperforms more sophisticated prompting systems, such as MAIN-RAG and Tree of Clarifications, achieving an RL score of 42.3.\n\n**Discourse-Aware Self-Reflection:**\n\nSystems incorporating discourse-aware self-reflection enable models to not only evaluate semantic grounding but also analyze the rhetorical relation between the question and candidate answers.\n\nThese approaches represent a shift toward incorporating rhetorical structure and discourse analysis into RAG systems, particularly for handling scientific papers and complex structured documents."], "durationSeconds": 9.313022421000001, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-07-20 10:02:18 UTC

```
{"query": "citation graph based document section retrieval scientific QA reranking", "results": [{"tool_use_id": "srvtoolu_01D4NzASijxw5pLV83WVcy9Q", "content": [{"title": "SciRerankBench: Benchmarking Rerankers Towards Scientific Retrieval-Augmented Generated LLMs", "url": "https://arxiv.org/html/2508.08742v1"}, {"title": "SciRAG: Adaptive, Citation-Aware, and Outline-Guided Retrieval and Synthesis for Scientific Literature", "url": "https://arxiv.org/html/2511.14362"}, {"title": "CoRank: LLM-Based Compact Reranking with Document Features for Scientific Retrieval", "url": "https://arxiv.org/pdf/2505.13757"}, {"title": "CG-RAG: Research Question Answering by Citation Graph Retrieval-Augmented LLMs", "url": "https://arxiv.org/pdf/2501.15067"}, {"title": "Beyond Case Law: Evaluating Structure-Aware Retrieval and Safety in Statute-Centric Legal QA", "url": "https://arxiv.org/pdf/2604.06173"}, {"title": "DeepEra: A Deep Evidence Reranking Agent for Scientific Retrieval-Augmented Generated Question Answering", "url": "https://arxiv.org/pdf/2601.16478"}, {"title": "Unified Multimodal Interleaved Document Representation for Retrieval", "url": "https://arxiv.org/pdf/2410.02729"}, {"title": "Discourse-Aware Scientific Paper Recommendation via QA-Style Summarization and Multi-Level Contrastive Learning", "url": "https://arxiv.org/pdf/2511.03330"}, {"title": "SurveyGen-I: Consistent Scientific Survey Generation with Evolving Plans and Memory-Guided Writing", "url": "https://arxiv.org/pdf/2508.14317"}]}, "I found several relevant research papers on citation graph-based document section retrieval for scientific QA and reranking. Here's what the search revealed:\n\n## Citation Graph-Based Approaches\n\nCG-RAG is a novel framework for research question answering that constructs a citation graph at the chunk level, where each chunk represents a semantically meaningful module of the paper. These chunks form a graph structure with intra-paper and inter-paper connections, capturing both internal coherence and external relationships.\n\nSciRAG is another retrieval and synthesis framework for scientific literature that pioneers an adaptive architecture that dynamically integrates citation-driven reasoning over the literature graph, symbolic logic, and structured knowledge aggregation. Each retrieval node searches documents, decides whether to expand along the citation graph, builds contribution chains, and applies reasoning-based reranking.\n\n## Section-Level Retrieval and Reranking\n\nSection-level reranking mechanisms have been introduced to enable fine-grained retrieval within documents, where the objective is to pinpoint the specific sections within the document that best match the query.\n\nG-RAG is a graph-based reranker that models semantic and relational connections between retrieved documents using graph neural networks (GNNs).\n\nThese approaches address the challenge that research paper content is highly heterogeneous—information in related work, methodology, and experimental sections serve different purposes, so effective modeling requires breaking down documents into semantic chunks."], "durationSeconds": 10.362327397000001, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-07-20 10:02:20 UTC

```
{"query": "argument structure scientific paper RAG query relevance section retrieval 2024", "results": [{"tool_use_id": "srvtoolu_01PfHg7vQaanubAzS47JTRiW", "content": [{"title": "IntrAgent: An LLM Agent for Content-Grounded Information Retrieval through Literature Review", "url": "https://arxiv.org/pdf/2604.22861"}, {"title": "Retrieval Augmented Generation Evaluation in the Era of Large Language Models: A Comprehensive Survey", "url": "https://arxiv.org/html/2504.14891v1"}, {"title": "SF-RAG: Structure-Fidelity Retrieval-Augmented Generation for Academic Question Answering", "url": "https://arxiv.org/pdf/2602.13647"}, {"title": "Enhancing Retrieval-Augmented Generation: A Study of ...", "url": "https://aclanthology.org/2025.coling-main.449.pdf"}, {"title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers", "url": "https://arxiv.org/html/2506.00054v1"}, {"title": "Citation Recommendation based on Argumentative Zoning of User Queries", "url": "https://arxiv.org/pdf/2501.18292"}, {"title": "ArgRAG: Explainable Retrieval Augmented Generation using Quantitative Bipolar Argumentation", "url": "https://arxiv.org/html/2508.20131v1"}, {"title": "Research on the construction and application of retrieval enhanced generation (RAG) model based on knowledge graph | Scientific Reports", "url": "https://www.nature.com/articles/s41598-025-21222-z"}]}, "Based on the search results, here's what I found on this topic:\n\n## Key Findings\n\n**RAG and Section Retrieval in Scientific Papers**\n\nUnlike flat, semantic-similarity-based RAG that overlooks document structure and often fails to align a scientific question with the relevant sections, some approaches leverage structural knowledge for reasoning-based ranking, prioritizing sections relevant to the question. Scientific research literature typically follow a well-defined section hierarchy where parent-level headings convey broader topics, while sub-level headings provide more specific details.\n\n**Structure-Fidelity Approaches**\n\nCurrent RAG methods flatten documents into unordered chunks, losing section signals and leading to fragmented, inaccurate retrieval, whereas humans naturally navigate papers via section hierarchies to localize evidence efficiently. Structure-fidelity approaches construct a structure-fidelity index that preserves the native outline and performs path-guided retrieval, enabling precise, low-entropy context assembly under token budgets.\n\n**Query Relevance and Retrieval**\n\nA prominent strategy focuses on refining and structuring user intent before retrieval to maximize alignment with relevant corpus segments, including decomposition, rewriting, generative reformulation, and the incorporation of structured priors to guide retrieval.\n\n**Argument Structure in Scientific Texts**\n\nCitation recommendation has arisen researchers' attention, which aims to help people find appropriate and necessary work to cite based on the given user queries, with research aiming to improve citation recommendation by considering the argumentative zoning of the citing sentence."], "durationSeconds": 10.867135041999994, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-07-20 10:02:20 UTC

```
{"query": "iterative retrieval augmented generation state estimation control theory scientific papers", "results": [{"tool_use_id": "srvtoolu_01HnKRkhwUtiKZ8FCAqMtYFh", "content": [{"title": "Adaptive iterative retrieval for enhanced retrieval-augmented generation - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/pii/S0925231225029443"}, {"title": "Iterative Retrieval-Augmented Generation", "url": "https://www.emergentmind.com/topics/iterative-retrieval-augmented-generation-rag"}, {"title": "IRAGKR:Iterative retrieval augmented generation with fine-grained knowledge refinement - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S092523122501954X"}, {"title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers", "url": "https://arxiv.org/html/2506.00054v1"}, {"title": "Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation", "url": "https://arxiv.org/pdf/2605.01284"}, {"title": "SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions", "url": "https://arxiv.org/pdf/2603.07379"}, {"title": "Retrieval Augmented Generation (RAG) and Beyond: A Comprehensive Survey   on How to Make your LLMs use External Data More Wisely", "url": "https://arxiv.org/pdf/2409.14924"}, {"title": "S2G-RAG: Structured Sufficiency and Gap Judging for Iterative Retrieval-Augmented QA", "url": "https://arxiv.org/pdf/2604.23783"}]}, "I've performed the web search for your query. Here are the key findings about iterative retrieval-augmented generation, state estimation, and control theory:\n\n## Overview of Iterative RAG\n\nIterative Retrieval-Augmented Generation (RAG) is a class of architectures and procedures that augment LLM generation by dynamically alternating between the LLM's reasoning steps and external document retrieval in multiple rounds. Unlike standard RAG, iterative RAG repeatedly reformulates queries, accumulates and prunes evidence, and re-invokes retrieval, thereby adapting the context and information exposed to the generator across multiple iterations.\n\n## State-Dependent Control\n\nThe search results reveal a connection to control theory concepts. Agentic systems increasingly treat retrieval as a repeated, state-dependent action rather than an upfront preprocessing step. Iterative RAG faces a retrieval control bottleneck where at each turn, the system must assess whether the accumulated evidence supports answering, and if not, specify what to retrieve next.\n\n## Advanced Techniques\n\nState-of-the-art iterative RAG systems employ agentic reasoning, explicit evidence gap analysis, adaptive termination policies, structured knowledge representations, and reinforcement learning. One approach uses a multi-dimensional dynamic retrieval decision mechanism controlled by evaluating uncertainty via a combination of entropy, attention fusion, and part-of-speech filtering.\n\n## Broader Framework\n\nThe most effective frameworks tightly couple retrieval, generation, and verification in iterative loops, ensuring that generation is guided by critique and alignment rather than treated as a terminal step.\n\nThe search results show active research in this area with papers from 2025 and 2026 exploring optimal control and state estimation principles in iterative RAG systems."], "durationSeconds": 10.831231423999998, "searchCount": 1}
```

### [18] ASSISTANT · 2026-07-20 10:03:15 UTC

```
The rhetorical/discourse-aware and citation-graph RAG space is crowded (Disco-RAG, CG-RAG, SF-RAG). Let me search for several more specific directions.
```

### [19] TOOL CALL — WebSearch · 2026-07-20 10:03:15 UTC

```
abstract bias scientific paper retrieval RAG answers claims vs evidence 2024 2025
```

### [20] TOOL CALL — WebSearch · 2026-07-20 10:03:15 UTC

```
value of information section selection document question answering marginal utility
```

### [21] TOOL CALL — WebSearch · 2026-07-20 10:03:15 UTC

```
optimal transport Wasserstein distance text retrieval document sections ranking 2024
```

### [22] TOOL RESULT — WebSearch · 2026-07-20 10:03:20 UTC

```
{"query": "value of information section selection document question answering marginal utility", "results": [{"tool_use_id": "srvtoolu_01Sa7evDwwWV6ESG5EPQHGKj", "content": [{"title": "ESC1501 - Assessment 8 & 9 questions and answers (docx) - CliffsNotes", "url": "https://www.cliffsnotes.com/study-notes/23154845"}, {"title": "An Information-Theoretic Formalism for Multiscale Structure in Complex   Systems", "url": "https://arxiv.org/pdf/1409.4708"}, {"title": "Section -B Theory Instruction: Answer all question in this section Explai..", "url": "https://askfilo.com/user-question-answers-smart-solutions/section-b-theory-instruction-answer-all-question-in-this-3331303131353232"}, {"title": "Payoffs-Beliefs Duality and the Value of Information", "url": "https://arxiv.org/pdf/1908.01633"}, {"title": "Marginal Utility Multiple Choice Quiz | PDF", "url": "https://www.scribd.com/document/809120983/Chap-07-22e-Economics-Algo"}, {"title": "Marginal Analysis and Consumer Choice AP Micro | Topic 1.6 | Fiveable", "url": "https://fiveable.me/ap-micro/unit-1/marginal-analysis-consumer-choice/study-guide/QBFQvkWXhvx4wSHnR6dr"}, {"title": "Utility Theory Practice Questions-1 (pdf) - CliffsNotes", "url": "https://www.cliffsnotes.com/study-notes/12905643"}, {"title": "The Cost of Informing Decision-Makers in Multi-Agent Maximum Coverage   Problems with Random Resource Values", "url": "https://arxiv.org/pdf/2306.12603"}, {"title": "EC 200 - Answers to Practice Problems on Consumer Behavior", "url": "https://www.washburn.edu/sobu/dnizovtsev/200P02_Uans.html"}, {"title": "The Marginal Utility of Information: Its Effects upon Decision-Making: The Sociological Quarterly: Vol 21, No 2", "url": "https://www.tandfonline.com/doi/abs/10.1111/j.1533-8525.1980.tb00607.x"}]}, "I've completed the web search for your query. The results cover several relevant topics:\n\n**Key findings:**\n\n1. **Marginal Utility of Information (General Concept)**: The marginal utility of information is an alternative measure that quantifies how well a system can be characterized using a limited amount of information.\n\n2. **Information and Decision-Making**: Research specifies how the importance or marginal utility of information can change as a function of both its amount and evaluation, with mathematical models describing different relations between decision-making and the amount and evaluation of information available to actors.\n\n3. **Value of Information in Economics**: The marginal value of information has been studied with conditions on parameterized information structures and decision problems showing when the marginal value of information is null when the agent receives little information.\n\n4. **Information Utility Variation**: Research suggests that information of the same type does not necessarily have the same weight or utility for actors' decision-making.\n\nThe search results include academic papers on information theory, economics papers on marginal utility, and theoretical work on how information affects decision-making and utility maximization."], "durationSeconds": 7.553422841000021, "searchCount": 1}
```

### [23] TOOL RESULT — WebSearch · 2026-07-20 10:03:24 UTC

```
{"query": "optimal transport Wasserstein distance text retrieval document sections ranking 2024", "results": [{"tool_use_id": "srvtoolu_01Q29kp17HpXWxvGzQCp57hn", "content": [{"title": "Kd-tree Based Wasserstein Distance Approximation for High-Dimensional Data", "url": "https://arxiv.org/pdf/2601.12975"}, {"title": "Optimal transport for cross-ligual document retrieval - Georgios Balikas: Personal website!", "url": "https://balikasg.github.io/machine%20learning/information%20retrieval/word%20embeddings/Wasserstein-distances-for-document-retrieval/"}, {"title": "Large-scale similarity search with Optimal Transport - ACL Anthology", "url": "https://aclanthology.org/2023.emnlp-main.730/"}, {"title": "Fast Optimal Transport through Sliced Wasserstein Generalized Geodesics", "url": "https://arxiv.org/pdf/2307.01770"}, {"title": "Cross-lingual Document Retrieval using Regularized Wasserstein Distance", "url": "https://arxiv.org/pdf/1805.04437"}, {"title": "WassRank: Listwise Document Ranking Using Optimal ...", "url": "https://dl.acm.org/doi/10.1145/3289600.3291006"}, {"title": "Document-Level Text Generation with Minimum Bayes Risk Decoding using Optimal Transport", "url": "https://arxiv.org/pdf/2505.23078"}, {"title": "Improving Cross-lingual Information Retrieval on Low-Resource Languages via Optimal Transport Distillation | Request PDF", "url": "https://www.researchgate.net/publication/368838794_Improving_Cross-lingual_Information_Retrieval_on_Low-Resource_Languages_via_Optimal_Transport_Distillation"}, {"title": "(PDF) Cross-lingual Document Retrieval using Regularized Wasserstein Distance", "url": "https://www.researchgate.net/publication/325118403_Cross-lingual_Document_Retrieval_using_Regularized_Wasserstein_Distance"}, {"title": "Wasserstein-Fisher-Rao Document Distance", "url": "https://arxiv.org/pdf/1904.10294"}]}, "Here are the search results for your query on optimal transport, Wasserstein distance, text retrieval, document ranking, and related 2024 research:\n\n## Key Findings\n\n**Applications in Text Retrieval:**\n\nWasserstein distance has been applied widely, with one of its most prominent applications being the retrieval of similar items in data such as images and text. For document retrieval, the Word Mover's Distance—defined as the optimal transport cost between distributions in a word embedding space—has been shown to evaluate semantic similarity with high accuracy even for documents with no overlapping vocabulary.\n\n**Large-Scale Applications:**\n\nWasserstein distance is a powerful tool for comparing probability distributions and is widely used for document classification and retrieval tasks in NLP, known as the word mover's distance (WMD) in the NLP community. However, WMD exhibits excellent performance for various NLP tasks; however, one of its limitations is its computational cost and thus is not useful for large-scale distribution comparisons. One solution employs the L1 embedding method based on tree-based Wasserstein approximation and nearest neighbor search to efficiently find k-nearest neighbors, demonstrating comparable performance to vanilla Wasserstein distance while being computed three orders of magnitude faster.\n\n**Document Ranking:**\n\nThe listwise ranking loss is formulated as the minimum cost (the Wasserstein distance) of transporting (or reshaping) the pile of predicted relevance mass so that it matches the pile of ground-truth relevance.\n\n**Recent Work:**\n\nThe search results include recent papers from 2023 onward exploring these topics, including work on large-scale similarity search with optimal transport and document-level text generation applications published in 2024 and 2025."], "durationSeconds": 10.397936531999992, "searchCount": 1}
```

### [24] TOOL RESULT — WebSearch · 2026-07-20 10:03:24 UTC

```
{"query": "abstract bias scientific paper retrieval RAG answers claims vs evidence 2024 2025", "results": [{"tool_use_id": "srvtoolu_01GT3J8kWf3sizRsPTFQLqJ6", "content": [{"title": "A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges", "url": "https://www.mdpi.com/2504-2289/9/12/320"}, {"title": "From Data to Decisions: Leveraging Retrieval-Augmented Generation to Balance Citation Bias in Burn Management Literature - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12191722/"}, {"title": "Dead Science Walking: Publication Bias and the AI Scientist Pipeline", "url": "https://arxiv.org/pdf/2606.04220"}, {"title": "Retrieval-Augmented Generation with Conflicting Evidence", "url": "https://arxiv.org/pdf/2504.13079"}, {"title": "DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation", "url": "https://arxiv.org/pdf/2605.27710"}, {"title": "The Impact of Ideological Discourses in RAG: A Case Study with COVID-19 Treatments", "url": "https://arxiv.org/pdf/2603.14838"}, {"title": "VERIRAG: A Post-Retrieval Auditing of Scientific Study Summaries", "url": "https://arxiv.org/pdf/2507.17948"}, {"title": "A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution,", "url": "https://arxiv.org/pdf/2410.12837"}, {"title": "Rationale-Guided Retrieval Augmented Generation for ...", "url": "https://aclanthology.org/2025.naacl-long.635.pdf"}, {"title": "Retrieval-Augmented Generation Must Move Beyond Factual Grounding to Represent Diverse Opinions", "url": "https://arxiv.org/html/2604.12138v3"}]}, "I found several relevant research papers and studies addressing the intersection of abstract bias, scientific paper retrieval, RAG systems, and the challenges of claims versus evidence. Here are the key findings:\n\n## Key Research Areas\n\n**RAG and Evidence Bias in Scientific Retrieval:**\n\nQueries framed around a hypothesis are often more similar to supporting abstracts than to null-result records, and this selection step can push positive evidence into the context window more often than negative evidence. The issue is that standard retrieval optimises relevance to the query, while governance requires relevance to the evidential state of the claim.\n\n**Citation Bias in RAG:**\n\nCitation bias in sourcing for RAG often prioritizes highly cited studies, overlooking less-cited but valuable research.\n\n**Claim Verification and Scientific Evidence:**\n\nScientific claim verification focuses on determining whether scientific evidence supports, contradicts, or is insufficient to verify a claim, with SciFact adapting this to the scientific domain by pairing expert-written claims with evidence abstracts.\n\n**Generation Issues:**\n\nLLMs trained to produce helpful and coherent text can turn mixed evidence into a confident synthesis, which is useful when the evidence is strong but risky when the retrieved set is already biased, with prior work reporting omissions of caveats and null results in LLM-generated reviews.\n\n**Broader RAG Bias Concerns:**\n\nWhile RAG has the potential to reduce biases by retrieving more balanced information, there is still the risk of amplifying biases present in the retrieved sources.\n\nThe research from 2024-2025 reveals that RAG systems face significant challenges in accurately representing the full evidential landscape when handling scientific claims."], "durationSeconds": 11.310214730000007, "searchCount": 1}
```

### [25] ASSISTANT · 2026-07-20 10:04:20 UTC

```
The discourse/citation/structure-fidelity RAG space is heavily explored. Let me search for the more novel angle of proof-minimal retrieval.
```

### [26] TOOL CALL — WebSearch · 2026-07-20 10:04:20 UTC

```
minimal sufficient section set document retrieval proof search backward chaining scientific QA 2024 2025
```

### [27] TOOL CALL — WebSearch · 2026-07-20 10:04:20 UTC

```
necessity sufficiency retrieval RAG minimum evidence set answer 2025
```

### [28] TOOL RESULT — WebSearch · 2026-07-20 10:04:28 UTC

```
{"query": "minimal sufficient section set document retrieval proof search backward chaining scientific QA 2024 2025", "results": [{"tool_use_id": "srvtoolu_01R1Bsi6nqvntAA2Xf4KvpBE", "content": [{"title": "Improving Scientific Document Retrieval with Concept Coverage-based Query Set Generation", "url": "https://arxiv.org/html/2502.11181"}, {"title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers", "url": "https://arxiv.org/html/2506.00054v1"}, {"title": "SUFFICIENT CONTEXT:ANEW LENS ON RETRIEVAL ...", "url": "https://openreview.net/pdf?id=Jjr2Odj8DJ"}, {"title": "Inter-Passage Verification for Multi-evidence Multi-answer QA", "url": "https://aclanthology.org/2025.findings-acl.354.pdf"}, {"title": "sufficient context:anew lens on retrieval augmented ...", "url": "https://arxiv.org/pdf/2411.06037"}, {"title": "Towards evidence-aware retrieval-augmented generation via self-corrective chain-of-thought - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0306457325003103"}, {"title": "Perspectives on neural proof nets", "url": "https://arxiv.org/pdf/2211.04141"}, {"title": "A Survey of RAG-Reasoning Systems in LLMs", "url": "https://aclanthology.org/2025.findings-emnlp.648.pdf"}]}, "I found several relevant research papers and resources related to your search query. Here's a summary of the key findings:\n\n## Recent Research on Document Retrieval and QA (2024-2025)\n\n**Scientific Document Retrieval:**\nA dedicated method for scientific document retrieval hasn't been well-studied in the literature, with recent work proposing frameworks to generate query sets that comprehensively cover document concepts.\n\n**Retrieval-Augmented Generation (RAG) Systems:**\nMultiHop-RAG (2024) targets multi-hop challenges through linked question-answer pairs, bridge entities, and explicit multi-hop query types, enabling systematic assessment of retrieval chaining, evidence linking, and document-level reasoning.\n\n**Sufficient Context in QA:**\nResearch on \"sufficient context\" as a framework where open-book QA cannot be solved by improving retrieval alone has been explored, with findings showing that when given instances without sufficient context, models tend to hallucinate more than they abstain, especially for multi-hop questions.\n\n**Multi-evidence QA Approaches:**\nRecent work searches broadly for a large pool of passages to cover sufficient evidence, with reader models processing retrieved passages to generate answer candidates, then employing verification pipelines to verify each answer.\n\n**Proof Search and Backward Chaining:**\nBackward chaining proof net generation can be used for graph generation, functioning similarly to sequent calculus proof search, contrasting with forward chaining proof search which resembles natural deduction proof search.\n\nThe search results indicate active research in RAG systems, multi-hop reasoning, and retrieval verification methods for scientific QA in 2024-2025."], "durationSeconds": 10.028698013000016, "searchCount": 1}
```

### [29] TOOL RESULT — WebSearch · 2026-07-20 10:04:30 UTC

```
{"query": "necessity sufficiency retrieval RAG minimum evidence set answer 2025", "results": [{"tool_use_id": "srvtoolu_0125RTXrsDkKooj3VaUZEvD1", "content": [{"title": "From Retrieval to Evidence Sufficiency: Why RAG Needs a Judge Before It Answers | by Fanghua (Joshua) Yu | Jun, 2026 | Medium", "url": "https://medium.com/@yu-joshua/from-retrieval-to-evidence-sufficiency-why-rag-needs-a-judge-before-it-answers-8719596bea75"}, {"title": "[2605.03534] SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation", "url": "https://arxiv.org/abs/2605.03534"}, {"title": "Proceedings - Retrieval Augmented Generation (RAG) 2025 - TREC Browser", "url": "https://pages.nist.gov/trec-browser/trec34/rag/proceedings/"}, {"title": "S2G-RAG: Structured Sufficiency and Gap Judging for Iterative Retrieval-Augmented QA", "url": "https://arxiv.org/html/2604.23783"}, {"title": "[2605.03534v1] SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation", "url": "https://arxiv.org/abs/2605.03534v1"}, {"title": "Deeper insights into retrieval augmented generation: The role of sufficient context", "url": "https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/"}, {"title": "SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation", "url": "https://arxiv.org/html/2605.03534"}, {"title": "When Confidence Takes the Wrong Path: Diagnosing Retrieval-State Lock-In in RAG", "url": "https://arxiv.org/pdf/2606.22728"}]}, "The search results reveal several important recent developments in RAG systems focused on necessity, sufficiency, and minimum evidence sets for generating answers:\n\n## Key Findings from 2025-2026\n\n**Evidence Sufficiency as a Core Problem**\n\nRAG systems often mistake topical relevance for answerability—retrieved evidence may be close to the answer, but not enough to support the final claim. Even after retrieval, reranking, and traversal, systems need to know whether evidence is sufficient. A better architecture adds sufficiency judgment—retrieval finds candidate evidence, and sufficiency judgment decides whether the evidence deserves an answer.\n\n**ICLR 2025: \"Sufficient Context\"**\n\nThe ICLR 2025 paper \"Sufficient Context: A New Lens on Retrieval Augmented Generation Systems\" defines a method to classify whether retrieved context has enough information to answer a query. An autorater judges whether a diligent reader could infer the answer using only that context, and this label is combined with model confidence to guide selective generation.\n\n**SURE-RAG Approach (2026)**\n\nSURE-RAG is built on the observation that evidence sufficiency is a set-level property: missing hops and unresolved conflicts cannot be detected by independent passage scoring. It produces local relation distributions that are aggregated into interpretable answer-level signals—coverage, relation strength, disagreement, conflict, and retrieval uncertainty.\n\n**Minimum Evidence Design**\n\nSome approaches redefine RAG to select a small but high-quality set of evidence, with a paradigm of \"providing necessary and sufficient context in a readable format.\""], "durationSeconds": 12.08336043999999, "searchCount": 1}
```

### [30] ASSISTANT · 2026-07-20 10:06:00 UTC

```
Let me search for the most specific novel angle I've identified — using within-document inverse section frequency and internal cross-references.
```

### [31] TOOL CALL — WebSearch · 2026-07-20 10:06:00 UTC

```
within-document inverse section frequency TF-IDF section ranking query retrieval intra-document
```

### [32] TOOL CALL — WebSearch · 2026-07-20 10:06:00 UTC

```
internal cross-reference forward reference scientific paper retrieval section dependency graph 2024 2025
```

### [33] TOOL CALL — WebSearch · 2026-07-20 10:06:00 UTC

```
compressed sensing sparse recovery RAG section selection document retrieval information theoretic 2024
```

### [34] TOOL RESULT — WebSearch · 2026-07-20 10:06:08 UTC

```
{"query": "within-document inverse section frequency TF-IDF section ranking query retrieval intra-document", "results": [{"tool_use_id": "srvtoolu_01DPYNqfSbfEKrv7kHVLVxMc", "content": [{"title": "Document retrieval and ranking - IBM Documentation", "url": "https://www.ibm.com/docs/en/filenet-p8-platform/5.7.0?topic=domain-document-retrieval-ranking"}, {"title": "TF–IDF Search Mechanism", "url": "https://www.emergentmind.com/topics/tf-idf-based-search-mechanism"}, {"title": "What Is TF-IDF? Search Intent and Inverse Document Frequency", "url": "https://loganix.com/what-is-tf-idf/"}, {"title": "Fine-Tuning Large Language Models and Evaluating Retrieval Methods for   Improved Question Answering on Building Codes", "url": "https://arxiv.org/pdf/2505.04666"}, {"title": "Personalized Search", "url": "https://arxiv.org/pdf/1509.02207"}, {"title": "Targeted banner advertisements", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8275661"}, {"title": "tf-idf Model for Page Ranking - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/nlp/tf-idf-model-for-page-ranking/"}, {"title": "Intelligent chat channel processor", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11374882"}, {"title": "tf–idf - Wikipedia", "url": "https://en.wikipedia.org/wiki/Tf%E2%80%93idf"}, {"title": "An Introduction to TF-IDF: What It Is & How to Use It", "url": "https://www.semrush.com/blog/tf-idf/"}]}, "I've performed a web search on your query about within-document inverse section frequency, TF-IDF section ranking, query retrieval, and intra-document methods.\n\nThe search results provide information about TF-IDF fundamentals and its applications in document retrieval and ranking:\n\n**TF-IDF Overview:**\nTF-IDF is a measure of importance of a word to a document in a collection or corpus, adjusted for the fact that some words appear more frequently in general. TF-IDF is calculated by multiplying TF by IDF, and the calculated value gives higher scores to terms that are frequent in a specific document but rare in the overall corpus, making them more useful for distinguishing relevant documents.\n\n**Section-Based Retrieval:**\nThe results include a reference to treating documents as chunks for retrieval purposes. A document can be treated as a collection of chunks, each chunk representing a distinct retrieval unit, where TF measures how often a query term appears within a particular chunk, normalized by the total number of terms in that chunk.\n\n**Applications:**\nIn the context of search results, TF-IDF helps rank web pages based on their relevance to a specific query, ensuring that search engines deliver the most pertinent results to users' queries.\n\nHowever, the search results don't contain specific information about \"within-document inverse section frequency\" or specialized intra-document section ranking techniques. For more detailed academic papers on these specific advanced topics, you may want to search academic databases like arXiv or Google Scholar directly."], "durationSeconds": 9.312003619999974, "searchCount": 1}
```

### [35] TOOL RESULT — WebSearch · 2026-07-20 10:06:10 UTC

```
{"query": "internal cross-reference forward reference scientific paper retrieval section dependency graph 2024 2025", "results": [{"tool_use_id": "srvtoolu_01Fb2TNxqfsgUGdqdjnugdPG", "content": [{"title": "AGH IR at LongEval: Improving Scientific Information ...", "url": "https://ceur-ws.org/Vol-4038/paper_276.pdf"}, {"title": "Deep Retrieval at CheckThat! 2025: Identifying Scientific Papers from Implicit Social Media Mentions via Hybrid Retrieval and Re-Ranking", "url": "https://arxiv.org/html/2505.23250v1"}, {"title": "The Reciprocal Impact of Science and Software: A Cross-Corpus Analysis of How Research Shapes Software and Software Enables Research", "url": "https://arxiv.org/pdf/2606.28120"}, {"title": "Enhance Multimodal Retrieval-Augmented Generation ...", "url": "https://www.ijournalse.org/index.php/ESJ/article/download/3369/958/11312"}, {"title": "Knowledge Graph-Guided Retrieval Augmented Generation", "url": "https://aclanthology.org/2025.naacl-long.449.pdf"}, {"title": "Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework", "url": "https://arxiv.org/pdf/2604.06170"}, {"title": "A Systematic Review of Key Retrieval-Augmented Generation (RAG) Systems: Progress, Gaps, and Future Directions", "url": "https://arxiv.org/html/2507.18910v1"}, {"title": "Article Not peer-reviewed version Retrieval Augmented Generation (RAG)", "url": "https://www.preprints.org/frontend/manuscript/84594ac4303eab08678a86675fef3405/download_pub"}, {"title": "CHLA 2025 CONFERENCE CONTRIBUTED PAPERS / ABSC CONGRÈS 2025 COMMUNICATIONS LIBRES", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12352438/"}]}, "I've completed the web search for your query about internal cross-references, forward references, scientific paper retrieval, section dependency graphs in 2024-2025. Here's what the search revealed:\n\n## Key Findings:\n\n**Scientific Paper Retrieval and Structure (2024-2025):**\n\nRecent work in 2025 has focused on dense retrieval and cross-encoder reranking approaches for scientific information retrieval, with comprehensive investigations into document retrieval strategies for evolving scholarly corpora.\n\n**Knowledge Graph and Dependency Modeling:**\n\nA notable framework uses a typed schema with nodes for papers, sections, concepts, methods, experiments, datasets, and visual elements, with edges encoding structural and semantic relations including hierarchy, definition, proposal, usage, evaluation, illustration, and dependency. All nodes and edges carry provenance metadata including source chunk IDs, page numbers, verification status, and confidence scores.\n\n**RAG and Retrieval Advances:**\n\n2024 work taught models to decide when and how much to retrieve, with systems like SAM-RAG dynamically filtering documents and verifying both evidence and answers.\n\n**Cross-Reference and Citation Searching:**\n\nRecent research has examined backward and forward citation searching tools, measuring time needed to complete citation searching, total references retrieved, and relevant references found.\n\nThe search results show active research in scientific paper analysis with emphasis on structured representations of paper components and their dependencies, particularly relevant to understanding cross-references and forward/backward citation patterns."], "durationSeconds": 10.382661161000026, "searchCount": 1}
```

### [36] TOOL RESULT — WebSearch · 2026-07-20 10:06:10 UTC

```
{"query": "compressed sensing sparse recovery RAG section selection document retrieval information theoretic 2024", "results": [{"tool_use_id": "srvtoolu_01Pvtud36z8qymVLHewrerkH", "content": [{"title": "A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution,", "url": "https://arxiv.org/pdf/2410.12837"}, {"title": "Compressive Sensing in Image/Video Compression: Sampling, Coding, Reconstruction, and Codec Optimization", "url": "https://www.mdpi.com/2078-2489/15/2/75"}, {"title": "(1+eps)-approximate Sparse Recovery", "url": "https://arxiv.org/pdf/1110.4414"}, {"title": "Information-theoretic limits on sparse signal recovery: Dense versus   sparse measurement matrices", "url": "https://arxiv.org/pdf/0806.0604"}, {"title": "Sparse Recovery with Linear and Nonlinear Observations: Dependent and   Noisy Data", "url": "https://arxiv.org/pdf/1403.3109"}, {"title": "Support Recovery with Sparsely Sampled Free Random Matrices", "url": "https://arxiv.org/pdf/1208.5269"}, {"title": "Sub-linear Time Support Recovery for Compressed Sensing using   Sparse-Graph Codes", "url": "https://arxiv.org/pdf/1412.7646"}, {"title": "arXiv:2408.16166v1 [cs.IT] 28 Aug 2024", "url": "https://arxiv.org/pdf/2408.16166"}, {"title": "The All-or-Nothing Phenomenon in Sparse Linear Regression", "url": "https://arxiv.org/pdf/1903.05046"}, {"title": "Optimal Phase Transitions in Compressed Sensing", "url": "https://arxiv.org/pdf/1111.6822"}]}, "I've performed the web search for your query. Here's what the results show:\n\nThe search returned several relevant sources across multiple topics related to your query:\n\n**Retrieval-Augmented Generation (RAG) and Document Selection:**\nInformation-theoretic approaches are used to identify useful context and filter retrieved contexts in RAG systems. Hybrid retrieval approaches that combine dense and sparse retrieval could enhance the effectiveness of RAG systems.\n\n**Compressed Sensing and Sparse Recovery:**\nCompressed Sensing has emerged as a transformative technique in image compression, offering solutions for efficient signal representation and acquisition. Compressed Sensing can efficiently capture and represent sparse signals.\n\n**Information-Theoretic Perspectives:**\nThe search results included several papers on information-theoretic bounds for compressed sensing and sparse recovery, indicating active research in understanding fundamental limits of recovery algorithms through information theory approaches.\n\n**2024 Work:**\nIn the last two decades, the problem of recovering structured signals from significantly under-sampled linear measurements, referred to as compressed sensing, has been extensively studied by applied mathematicians, signal processing researchers, information theorists and statisticians (from a 2024 paper).\n\nThe search results show intersection between RAG/document retrieval methods and information-theoretic principles, though a specific paper directly combining all these topics (compressed sensing, sparse recovery, RAG, section selection, and information theory) in 2024 wasn't prominently featured in these results."], "durationSeconds": 10.43536486099998, "searchCount": 1}
```

### [37] ASSISTANT · 2026-07-20 10:06:50 UTC

```
Let me check the most specific novel angle — contrastive answer-hypothesis scoring for retrieval.
```

### [38] TOOL CALL — WebSearch · 2026-07-20 10:06:50 UTC

```
contrastive answer hypothesis retrieval scoring document sections multiple answers discriminative 2024 2025
```

### [39] TOOL CALL — WebSearch · 2026-07-20 10:06:50 UTC

```
QASPER scientific paper QA dataset section retrieval benchmark 2024
```

### [40] TOOL RESULT — WebSearch · 2026-07-20 10:06:56 UTC

```
{"query": "QASPER scientific paper QA dataset section retrieval benchmark 2024", "results": [{"tool_use_id": "srvtoolu_014p1Fw98zW5igpvVFxp74j2", "content": [{"title": "Synthesizing Scientific Literature with Retrieval-augmented ...", "url": "https://kyleclo.com/assets/pdf/openscholar-synthesizing-scientific-literature-with-retrieval-augmented-lms.pdf"}, {"title": "SciDQA: A Deep Reading Comprehension Dataset over Scientific Papers", "url": "https://arxiv.org/pdf/2411.05338"}, {"title": "ISQA: Informative Factuality Feedback for Scientific Summarization", "url": "https://arxiv.org/pdf/2404.13246"}, {"title": "LMEB: Long-horizon Memory Embedding Benchmark", "url": "https://arxiv.org/pdf/2603.12572"}, {"title": "A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers | Request PDF", "url": "https://www.researchgate.net/publication/352364140_A_Dataset_of_Information-Seeking_Questions_and_Answers_Anchored_in_Research_Papers"}, {"title": "Qasper Leaderboard", "url": "https://llm-stats.com/benchmarks/qasper"}, {"title": "SciVer: Evaluating Foundation Models for Multimodal Scientific Claim Verification", "url": "https://arxiv.org/pdf/2506.15569"}, {"title": "QASA: Advanced Question Answering on Scientific Articles", "url": "https://proceedings.mlr.press/v202/lee23n/lee23n.pdf"}, {"title": "SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding", "url": "https://arxiv.org/pdf/2408.15545"}]}, "Based on the search results, here's what I found about QASPER:\n\nQASPER is a dataset comprised of 5,049 questions over 1,585 Natural Language Processing (NLP) papers, where questions are provided by NLP practitioners while answers are extracted by another set of practitioners who also provide corresponding supporting facts. Questions are written from the title and abstract and answered using evidence from the full text.\n\nQASPER uses single NLP papers as input context with expert annotation and includes evidence rationale annotations. This makes it a valuable benchmark for evaluating scientific question answering and section retrieval capabilities on academic papers.\n\nThe dataset has been actively used in benchmarking efforts. The Qasper paper is available at https://arxiv.org/abs/2105.03011. Recent work continues to evaluate models on this benchmark, with Phi-3.5-mini-instruct from Microsoft currently leading the Qasper leaderboard with a score of 0.419."], "durationSeconds": 7.440483814999985, "searchCount": 1}
```

### [41] TOOL RESULT — WebSearch · 2026-07-20 10:06:58 UTC

```
{"query": "contrastive answer hypothesis retrieval scoring document sections multiple answers discriminative 2024 2025", "results": [{"tool_use_id": "srvtoolu_01T6h2RtJjzroK9sLiGHgKRL", "content": [{"title": "CONTRASTIVE RETRIEVAL HEADS IMPROVE ATTENTION-BASED RE-RANKING Linh Tran1", "url": "https://arxiv.org/pdf/2510.02219"}, {"title": "Contrastive Learning to Improve Retrieval for Real-world ...", "url": "https://aclanthology.org/2024.fever-1.28.pdf"}, {"title": "Contrastive Retrieval-Augmented Generation on Experience", "url": "https://aclanthology.org/2025.findings-acl.1224.pdf"}, {"title": "Accepted Findings Papers - ACL 2025", "url": "https://2025.aclweb.org/program/find_papers/"}, {"title": "Ruling Out to Rule In: Contrastive Hypothesis Retrieval for Medical Question Answering", "url": "https://arxiv.org/pdf/2604.04593"}, {"title": "Beyond Topical Similarity: Contrastive Evidence Retrieval with Interpretable Attention Alignment in RAG", "url": "https://arxiv.org/pdf/2606.01482"}, {"title": "Dual-Confidence Contrastive Decoding for Retrieval-Augmented Generation", "url": "https://arxiv.org/pdf/2607.00570"}, {"title": "Multi-level Relevance Document Identifier Learning for ...", "url": "https://aclanthology.org/2025.acl-long.497.pdf"}, {"title": "[2410.04657] Contrastive Learning to Improve Retrieval for Real-world Fact Checking", "url": "https://arxiv.org/abs/2410.04657"}]}, "I found several relevant research papers on this topic. Here are the key results:\n\n## Contrastive Hypothesis Retrieval\n\nA contrastive scoring function scores candidate documents using: S(d) = Sim(d, H⁺) - λ · Sim(d, H⁻), where Sim denotes cosine similarity between document and hypothesis embeddings, and λ ≥ 0 controls the penalty weight for mimic-aligned documents. The first term promotes documents relevant to the target diagnosis, while the second term penalizes documents that align with the mimic, and documents similar to H⁺ but dissimilar to H⁻ receive the highest scores, effectively filtering out hard negatives.\n\n## Contrastive Retrieval Heads for Document Re-ranking\n\nCoRe heads (Contrastive Retrieval heads) are a subset of attention heads specialized for document re-ranking. This approach proposes a contrastive scoring metric that identifies CoRe heads by rewarding attention directed towards relevant documents while penalizing attention to irrelevant ones.\n\n## Multi-level Relevance Learning\n\nMulti-level relevance learning uses outer-level relevance contrastive learning to differentiate between relevant and irrelevant documents, and inner-level multi-level relevance learning to distinguish between varying levels of relevance among documents.\n\n## Contrastive Learning for Fact Checking\n\nContrastive Fact-Checking Reranker fine-tunes Contriever with a contrastive objective based on multiple training signals, including distillation from GPT-4, evaluating subquestion answers, and gold labels."], "durationSeconds": 10.08478088799998, "searchCount": 1}
```

### [42] ASSISTANT · 2026-07-20 10:08:38 UTC

```
I found a very close match: "Ruling Out to Rule In: Contrastive Hypothesis Retrieval" for medical QA covers contrastive answer scoring. Let me now verify my clearest candidate — within-document inverse section frequency — and check one more angle.
```

### [43] TOOL CALL — WebFetch · 2026-07-20 10:08:38 UTC

```
URL: https://arxiv.org/abs/2604.04593
Prompt: What is the core mechanism of this paper? Does it use within-document term frequency, or is it about contrastive scoring between hypotheses in medical QA?
```

### [44] TOOL CALL — WebSearch · 2026-07-20 10:08:38 UTC

```
"within-document" "inverse section frequency" OR "intra-document IDF" section retrieval scoring 2024 2025
```

### [45] TOOL RESULT — WebFetch · 2026-07-20 10:08:40 UTC

```
{"bytes": 43595, "code": 200, "codeText": "OK", "result": "# Core Mechanism of CHR\n\nThe paper employs **contrastive scoring between hypotheses**, not term frequency analysis.\n\nThe framework generates two competing hypotheses: a target hypothesis (H+) for the correct answer and a mimic hypothesis (H−) for the most plausible incorrect alternative. Documents are then ranked by \"promoting H+-aligned evidence while penalizing H−-aligned content.\"\n\nThis approach is explicitly inspired by clinical reasoning. As the abstract states, CHR \"bridges clinical reasoning with retrieval mechanism design\" by modeling \"what to avoid alongside what to find,\" deliberately suppressing hard negatives that are semantically similar but clinically distinct from the correct diagnosis.", "durationMs": 4328, "url": "https://arxiv.org/abs/2604.04593"}
```

### [46] TOOL RESULT — WebSearch · 2026-07-20 10:08:44 UTC

```
{"query": "\"within-document\" \"inverse section frequency\" OR \"intra-document IDF\" section retrieval scoring 2024 2025", "results": [{"tool_use_id": "srvtoolu_01TYvXo42RECggmzNSeBjMdn", "content": [{"title": "Document retrieval and ranking - IBM Documentation", "url": "https://www.ibm.com/docs/en/filenet-p8-platform/5.7.0?topic=domain-document-retrieval-ranking"}, {"title": "TF–IDF Search Mechanism", "url": "https://www.emergentmind.com/topics/tf-idf-based-search-mechanism"}, {"title": "Inverse Document Frequency - an overview | ScienceDirect Topics", "url": "https://www.sciencedirect.com/topics/mathematics/inverse-document-frequency"}, {"title": "An Introduction to TF-IDF: What It Is & How to Use It", "url": "https://www.semrush.com/blog/tf-idf/"}, {"title": "TF-IDF — Term Frequency-Inverse Document Frequency – LearnDataSci", "url": "https://www.learndatasci.com/glossary/tf-idf-term-frequency-inverse-document-frequency/"}, {"title": "tf–idf - Wikipedia", "url": "https://en.wikipedia.org/wiki/Tf%E2%80%93idf"}, {"title": "A Survey on Why-Type Question Answering Systems", "url": "https://arxiv.org/pdf/1911.04879"}, {"title": "Semantic-Sensitive Web Information Retrieval Model for HTML Documents", "url": "https://arxiv.org/pdf/1204.0186"}, {"title": "IDF revisited: A simple new derivation within the Robertson-Sp\\\"arck   Jones probabilistic model", "url": "https://arxiv.org/pdf/0705.1161"}, {"title": "Detecting Cyber-Related Discussions in Online Social Platforms", "url": "https://arxiv.org/pdf/1907.02383"}]}, "Based on the search results, I found general information about TF-IDF and document retrieval scoring, but the results do not contain specific content about \"within-document inverse section frequency,\" \"intra-document IDF,\" or section-level retrieval scoring from 2024-2025.\n\nThe search results primarily cover:\n\n- TF-IDF as a measure of importance of a word to a document in a collection or corpus\n- Modern scoring improvements like term frequency saturation and document length normalization in BM25\n- Recent work on multilingual and cross-domain retrieval with subword vectorization (dated September 2025)\n\nHowever, none of the results specifically address the specialized techniques you're searching for regarding within-document section frequency or intra-document IDF for section-level retrieval scoring. These appear to be more specialized research topics that may not have substantial web coverage, or they might be discussed under different terminology in recent academic literature."], "durationSeconds": 8.377233259, "searchCount": 1}
```

### [47] ASSISTANT · 2026-07-20 10:10:07 UTC

```
No prior work found on within-document inverse section frequency (TF-ISF) for section retrieval. The CHR paper is about cross-document medical QA, not intra-document section scoring. I now have a clear, novel, feasible hypothesis. Let me write the output.
```

### [48] TOOL CALL — Write · 2026-07-20 10:10:07 UTC

```
File: /ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Within-Doc Term Rarity Fixes Section Retrieval",
  "hypothesis": "Standard dense retrieval systematically mis-ranks sections within scientific PDFs because it treats query-term matches uniformly, regardless of how many sections in the same document share that term. We hypothesize that replacing cross-corpus IDF with an Intra-Document Inverse Section Frequency (ISF) — ISF(t) = log(N_sections / (1 + SF(t))), where SF(t) is the count of sections in the target paper containing term t — produces a TF-ISF score that better identifies the evidence-bearing sections. Specifically, 'document theme terms' (e.g., the paper's topic words) appear in nearly every section, providing no discriminative signal; meanwhile, section-specific terms (precise technique names, numeric variable identifiers, unique experimental conditions) appear in only one or two sections and are the true discriminative signal for locating evidence. TF-ISF up-weights section-specific terms and down-weights document theme terms, thereby counteracting the retrieval bias toward claim-dense sections (Abstract, Introduction, Conclusion) that repeat theme terms in query-friendly language while directing retrieval toward evidence-dense sections (Methods, Results) that contain section-unique terms. We predict this training-free, self-contained score improves section recall and downstream answer F1 on QASPER relative to a fixed-k cosine-similarity baseline.",
  "motivation": "Scientific question answering over long PDFs is increasingly important for automated literature review, clinical evidence synthesis, and research acceleration. Despite significant RAG advances, a structural failure mode in scientific documents remains unstudied: claim-dense sections (Abstract, Introduction, Conclusion) paraphrase findings in accessible language that closely mirrors natural-language queries, inflating their cosine similarity scores. Evidence-dense sections (Results, Methods) contain the verifiable, specific information needed for accurate answers but use specialized, low-frequency vocabulary that under-scores under standard retrieval. This claim/evidence vocabulary gap is not random noise — it is an artifact of how scientific papers are written (IMRaD convention mandates separating claims from evidence). TF-ISF directly corrects this bias using only the document itself, requiring no external training data, no rhetorical parser, no citation graph, and no LLM inference at retrieval time. The approach is also interpretable: the ISF score for each query term is directly readable from the document's own statistics.",
  "assumptions": [
    "Scientific papers written in IMRaD (Introduction, Methods, Results, and Discussion) format create a systematic vocabulary split: claim-summarizing sections repeat topic terms while evidence sections contain section-unique terms.",
    "QASPER (or a similar dataset) contains enough examples where the gold evidence is in Methods/Results sections (not Abstract/Introduction) to detect the difference between TF-ISF and cosine similarity.",
    "Within-document section frequency can be computed from simple tokenization and section boundary detection, which is reliable for structured scientific PDFs.",
    "The improvement in section retrieval (higher recall of gold evidence sections) translates to measurable gains in downstream answer F1 when a fixed-size context window is used.",
    "A cheap LLM reader (available via OpenRouter within the $10 budget) can generate answers from retrieved sections consistently enough that retrieval quality differences are reflected in answer F1."
  ],
  "investigation_approach": "1) Load QASPER from HuggingFace; parse each paper's sections and their text. 2) Implement three retrieval methods: (a) top-k cosine similarity with sentence-transformers embeddings (baseline), (b) BM25 over sections using standard corpus-level IDF (strong baseline), and (c) TF-ISF using within-document section frequency for ISF computation. 3) For each query, retrieve the top-k=3 sections under each method. 4) Feed retrieved sections + query to a cheap LLM via OpenRouter (e.g., Llama-3.2-3B-Instruct) and generate an answer. 5) Evaluate with token-level F1 against gold answers (QASPER's standard metric). 6) Also compute section-level recall (fraction of gold evidence sections retrieved in top-k) as an intermediate diagnostic. 7) Run a subgroup analysis: split queries by gold evidence section type (Abstract vs. Methods vs. Results) and compare retrieval performance per subtype across methods. This reveals whether TF-ISF specifically rescues cases where cosine fails to retrieve Methods/Results sections. Target: ~150–200 examples to stay within $10 LLM budget at approximately $0.01–0.05 per query.",
  "success_criteria": "CONFIRM: TF-ISF achieves ≥3 F1 points higher than top-k cosine baseline on QASPER answer F1, AND section-level recall of gold evidence sections is higher for TF-ISF than cosine (especially for questions with evidence in Results/Methods sections). An intermediate confirmation would be showing that Abstract/Introduction sections have systematically lower ISF scores (more document-theme terms) while Methods/Results sections have higher ISF scores (more section-unique terms) for the same queries. DISCONFIRM: If cosine or BM25 already retrieves gold sections with high recall (≥0.80), suggesting the vocabulary gap between claim and evidence sections is not large enough in practice to create a retrieval failure. PARTIAL: If TF-ISF improves section recall but not F1 (suggesting the bottleneck is reader quality, not retrieval), or if improvement is only visible on a specific subtype (e.g., numerical questions).",
  "related_works": [
    "Disco-RAG (2025, arxiv 2601.04377): Builds intra-chunk RST discourse trees and inter-chunk rhetorical graphs to improve RAG coherence. Key difference: Disco-RAG requires an external discourse parser and focuses on discourse coherence for generation, while TF-ISF is a simple term-weighting formula computed purely from within-document statistics, requiring no external model and targeting retrieval rather than generation coherence.",
    "SF-RAG (2026, arxiv 2602.13647): Structure-Fidelity RAG preserves section hierarchy as a routing index and uses path-guided retrieval along the outline. Key difference: SF-RAG routes queries through a pre-built structural index; TF-ISF reweights term-section matches using within-document statistics, with no routing or indexing infrastructure required.",
    "CG-RAG (2025, arxiv 2501.15067): Citation-graph RAG builds intra- and inter-paper citation graphs for retrieval. Key difference: CG-RAG requires an external citation graph and focuses on inter-paper relationships. TF-ISF operates within a single document with no external resources.",
    "HyDE (Hypothetical Document Embeddings, 2022): Generates a hypothetical answer document and retrieves by its embedding. Key difference: HyDE requires LLM generation at retrieval time and targets query-document mismatch via generation; TF-ISF targets the within-document claim/evidence vocabulary split via statistical term weighting, requiring zero LLM calls during retrieval.",
    "Ruling Out to Rule In — Contrastive Hypothesis Retrieval (2026, arxiv 2604.04593): Scores documents by Sim(doc, H+) - lambda*Sim(doc, H-) where H+/H- are target and mimic hypotheses. Key difference: CHR retrieves across a document corpus for medical QA; TF-ISF ranks sections within a single document using no competing hypotheses, only within-document term statistics.",
    "SURE-RAG (2026, arxiv 2605.03534): Sufficiency and uncertainty-aware evidence verification using set-level sufficiency judgments. Key difference: SURE-RAG is a post-retrieval verification step that assesses if retrieved evidence is sufficient; TF-ISF is a retrieval scoring function that changes which sections are retrieved in the first place."
  ],
  "inspiration": "The core insight is TF-IDF applied at a finer granularity: just as cross-corpus IDF down-weights terms that appear in many documents (making them poor discriminators), within-document ISF down-weights terms that appear in many sections of the same paper. The mathematical framework is 50 years old (Sparck Jones 1972), but its application to the intra-document section-ranking problem in scientific RAG is new. The additional biological analogy is indicator species from ecology: just as ecologists use rare species whose presence precisely signals a particular habitat, TF-ISF identifies rare intra-document terms (section-specific vocabulary) as the most reliable indicators of a section's unique content. The hypothesis that this specifically corrects a systematic failure in scientific RAG is motivated by the IMRaD writing convention, which by design separates claim language (intro/conclusion) from evidence language (methods/results) — a structural feature absent in general-purpose documents.",
  "terms": [
    {
      "term": "TF-ISF",
      "definition": "Term Frequency × Inverse Section Frequency: a within-document term-weighting score where ISF(t) = log(N_sections / (1 + SF(t))), SF(t) is the number of sections in the same document containing term t, and N_sections is the total number of sections. Analogous to TF-IDF but using per-document section counts as the 'document frequency'."
    },
    {
      "term": "Inverse Section Frequency (ISF)",
      "definition": "The within-document analogue of IDF: a weight for term t in a given document computed as log(N_sections / (1 + SF(t))). Terms appearing in many sections of the same document receive low ISF (they are document theme terms); terms appearing in few sections receive high ISF (they are section-specific)."
    },
    {
      "term": "Claim-dense section",
      "definition": "A section of a scientific paper (typically Abstract, Introduction, or Conclusion) that summarizes findings and claims in accessible language, reusing the paper's main topic vocabulary. These sections score high under standard cosine similarity for typical queries but contain little verifiable evidence."
    },
    {
      "term": "Evidence-dense section",
      "definition": "A section of a scientific paper (typically Methods or Results) that contains specific experimental procedures, quantitative outcomes, and precise technical terms unique to that section. These sections are the true answer source for most factual questions but score lower under cosine similarity due to specialized vocabulary."
    },
    {
      "term": "Document theme term",
      "definition": "A term that appears in nearly every section of a given scientific paper (e.g., the paper's central topic noun). Theme terms have near-zero ISF and are uninformative for discriminating between sections."
    },
    {
      "term": "Section-specific term",
      "definition": "A term that appears in only one or two sections of a document (e.g., a specific dataset name, model hyperparameter, or experimental condition). Section-specific terms have high ISF and strongly indicate the section's unique content."
    },
    {
      "term": "QASPER",
      "definition": "A public benchmark dataset of 5,049 information-seeking questions over 1,585 NLP research papers, where each question is paired with gold answers and evidence annotations identifying the exact paper sections containing the answer."
    }
  ],
  "summary": "We hypothesize that standard cosine-similarity retrieval systematically mis-ranks sections in scientific PDFs by treating theme terms (shared across many sections) equally with section-specific terms, biasing retrieval toward claim-dense sections like Abstracts. Replacing cross-corpus IDF with a within-document Inverse Section Frequency (ISF) computed solely from the target paper's own section statistics corrects this bias without any training, discourse parsing, or LLM inference at retrieval time, and should improve answer F1 on QASPER over a fixed-k cosine baseline."
}
```

### [49] TOOL RESULT — Write · 2026-07-20 10:10:07 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Within-Doc Term Rarity Fixes Section Retrieval\",\n  \"hypothesis\": \"Standard dense retrieval systematically mis-ranks sections within scientific PDFs because it treats query-term matches uniformly, regardless of how many sections in the same document share that term. We hypothesize that replacing cross-corpus IDF with an Intra-Document Inverse Section Frequency (ISF) — ISF(t) = log(N_sections / (1 + SF(t))), where SF(t) is the count of sections in the target paper containing term t — produces a TF-ISF score that better identifies the evidence-bearing sections. Specifically, 'document theme terms' (e.g., the paper's topic words) appear in nearly every section, providing no discriminative signal; meanwhile, section-specific terms (precise technique names, numeric variable identifiers, unique experimental conditions) appear in only one or two sections and are the true discriminative signal for locating evidence. TF-ISF up-weights section-specific terms and down-weights document theme terms, thereby counteracting the retrieval bias toward claim-dense sections (Abstract, Introduction, Conclusion) that repeat theme terms in query-friendly language while directing retrieval toward evidence-dense sections (Methods, Results) that contain section-unique terms. We predict this training-free, self-contained score improves section recall and downstream answer F1 on QASPER relative to a fixed-k cosine-similarity baseline.\",\n  \"motivation\": \"Scientific question answering over long PDFs is increasingly important for automated literature review, clinical evidence synthesis, and research acceleration. Despite significant RAG advances, a structural failure mode in scientific documents remains unstudied: claim-dense sections (Abstract, Introduction, Conclusion) paraphrase findings in accessible language that closely mirrors natural-language queries, inflating their cosine similarity scores. Evidence-dense sections (Results, Methods) contain the verifiable, specific information needed for accurate answers but use specialized, low-frequency vocabulary that under-scores under standard retrieval. This claim/evidence vocabulary gap is not random noise — it is an artifact of how scientific papers are written (IMRaD convention mandates separating claims from evidence). TF-ISF directly corrects this bias using only the document itself, requiring no external training data, no rhetorical parser, no citation graph, and no LLM inference at retrieval time. The approach is also interpretable: the ISF score for each query term is directly readable from the document's own statistics.\",\n  \"assumptions\": [\n    \"Scientific papers written in IMRaD (Introduction, Methods, Results, and Discussion) format create a systematic vocabulary split: claim-summarizing sections repeat topic terms while evidence sections contain section-unique terms.\",\n    \"QASPER (or a similar dataset) contains enough examples where the gold evidence is in Methods/Results sections (not Abstract/Introduction) to detect the difference between TF-ISF and cosine similarity.\",\n    \"Within-document section frequency can be computed from simple tokenization and section boundary detection, which is reliable for structured scientific PDFs.\",\n    \"The improvement in section retrieval (higher recall of gold evidence sections) translates to measurable gains in downstream answer F1 when a fixed-size context window is used.\",\n    \"A cheap LLM reader (available via OpenRouter within the $10 budget) can generate answers from retrieved sections consistently enough that retrieval quality differences are reflected in answer F1.\"\n  ],\n  \"investigation_approach\": \"1) Load QASPER from HuggingFace; parse each paper's sections and their text. 2) Implement three retrieval methods: (a) top-k cosine similarity with sentence-transformers embeddings (baseline), (b) BM25 over sections using standard corpus-level IDF (strong baseline), and (c) TF-ISF using within-document section frequency for ISF computation. 3) For each query, retrieve the top-k=3 sections under each method. 4) Feed retrieved sections + query to a cheap LLM via OpenRouter (e.g., Llama-3.2-3B-Instruct) and generate an answer. 5) Evaluate with token-level F1 against gold answers (QASPER's standard metric). 6) Also compute section-level recall (fraction of gold evidence sections retrieved in top-k) as an intermediate diagnostic. 7) Run a subgroup analysis: split queries by gold evidence section type (Abstract vs. Methods vs. Results) and compare retrieval performance per subtype across methods. This reveals whether TF-ISF specifically rescues cases where cosine fails to retrieve Methods/Results sections. Target: ~150–200 examples to stay within $10 LLM budget at approximately $0.01–0.05 per query.\",\n  \"success_criteria\": \"CONFIRM: TF-ISF achieves ≥3 F1 points higher than top-k cosine baseline on QASPER answer F1, AND section-level recall of gold evidence sections is higher for TF-ISF than cosine (especially for questions with evidence in Results/Methods sections). An intermediate confirmation would be showing that Abstract/Introduction sections have systematically lower ISF scores (more document-theme terms) while Methods/Results sections have higher ISF scores (more section-unique terms) for the same queries. DISCONFIRM: If cosine or BM25 already retrieves gold sections with high recall (≥0.80), suggesting the vocabulary gap between claim and evidence sections is not large enough in practice to create a retrieval failure. PARTIAL: If TF-ISF improves section recall but not F1 (suggesting the bottleneck is reader quality, not retrieval), or if improvement is only visible on a specific subtype (e.g., numerical questions).\",\n  \"related_works\": [\n    \"Disco-RAG (2025, arxiv 2601.04377): Builds intra-chunk RST discourse trees and inter-chunk rhetorical graphs to improve RAG coherence. Key difference: Disco-RAG requires an external discourse parser and focuses on discourse coherence for generation, while TF-ISF is a simple term-weighting formula computed purely from within-document statistics, requiring no external model and targeting retrieval rather than generation coherence.\",\n    \"SF-RAG (2026, arxiv 2602.13647): Structure-Fidelity RAG preserves section hierarchy as a routing index and uses path-guided retrieval along the outline. Key difference: SF-RAG routes queries through a pre-built structural index; TF-ISF reweights term-section matches using within-document statistics, with no routing or indexing infrastructure required.\",\n    \"CG-RAG (2025, arxiv 2501.15067): Citation-graph RAG builds intra- and inter-paper citation graphs for retrieval. Key difference: CG-RAG requires an external citation graph and focuses on inter-paper relationships. TF-ISF operates within a single document with no external resources.\",\n    \"HyDE (Hypothetical Document Embeddings, 2022): Generates a hypothetical answer document and retrieves by its embedding. Key difference: HyDE requires LLM generation at retrieval time and targets query-document mismatch via generation; TF-ISF targets the within-document claim/evidence vocabulary split via statistical term weighting, requiring zero LLM calls during retrieval.\",\n    \"Ruling Out to Rule In — Contrastive Hypothesis Retrieval (2026, arxiv 2604.04593): Scores documents by Sim(doc, H+) - lambda*Sim(doc, H-) where H+/H- are target and mimic hypotheses. Key difference: CHR retrieves across a document corpus for medical QA; TF-ISF ranks sections within a single document using no competing hypotheses, only within-document term statistics.\",\n    \"SURE-RAG (2026, arxiv 2605.03534): Sufficiency and uncertainty-aware evidence verification using set-level sufficiency judgments. Key difference: SURE-RAG is a post-retrieval verification step that assesses if retrieved evidence is sufficient; TF-ISF is a retrieval scoring function that changes which sections are retrieved in the first place.\"\n  ],\n  \"inspiration\": \"The core insight is TF-IDF applied at a finer granularity: just as cross-corpus IDF down-weights terms that appear in many documents (making them poor discriminators), within-document ISF down-weights terms that appear in many sections of the same paper. The mathematical framework is 50 years old (Sparck Jones 1972), but its application to the intra-document section-ranking problem in scientific RAG is new. The additional biological analogy is indicator species from ecology: just as ecologists use rare species whose presence precisely signals a particular habitat, TF-ISF identifies rare intra-document terms (section-specific vocabulary) as the most reliable indicators of a section's unique content. The hypothesis that this specifically corrects a systematic failure in scientific RAG is motivated by the IMRaD writing convention, which by design separates claim language (intro/conclusion) from evidence language (methods/results) — a structural feature absent in general-purpose documents.\",\n  \"terms\": [\n    {\n      \"term\": \"TF-ISF\",\n      \"definition\": \"Term Frequency × Inverse Section Frequency: a within-document term-weighting score where ISF(t) = log(N_sections / (1 + SF(t))), SF(t) is the number of sections in the same document containing term t, and N_sections is the total number of sections. Analogous to TF-IDF but using per-document section counts as the 'document frequency'.\"\n    },\n    {\n      \"term\": \"Inverse Section Frequency (ISF)\",\n      \"definition\": \"The within-document analogue of IDF: a weight for term t in a given document computed as log(N_sections / (1 + SF(t))). Terms appearing in many sections of the same document receive low ISF (they are document theme terms); terms appearing in few sections receive high ISF (they are section-specific).\"\n    },\n    {\n      \"term\": \"Claim-dense section\",\n      \"definition\": \"A section of a scientific paper (typically Abstract, Introduction, or Conclusion) that summarizes findings and claims in accessible language, reusing the paper's main topic vocabulary. These sections score high under standard cosine similarity for typical queries but contain little verifiable evidence.\"\n    },\n    {\n      \"term\": \"Evidence-dense section\",\n      \"definition\": \"A section of a scientific paper (typically Methods or Results) that contains specific experimental procedures, quantitative outcomes, and precise technical terms unique to that section. These sections are the true answer source for most factual questions but score lower under cosine similarity due to specialized vocabulary.\"\n    },\n    {\n      \"term\": \"Document theme term\",\n      \"definition\": \"A term that appears in nearly every section of a given scientific paper (e.g., the paper's central topic noun). Theme terms have near-zero ISF and are uninformative for discriminating between sections.\"\n    },\n    {\n      \"term\": \"Section-specific term\",\n      \"definition\": \"A term that appears in only one or two sections of a document (e.g., a specific dataset name, model hyperparameter, or experimental condition). Section-specific terms have high ISF and strongly indicate the section's unique content.\"\n    },\n    {\n      \"term\": \"QASPER\",\n      \"definition\": \"A public benchmark dataset of 5,049 information-seeking questions over 1,585 NLP research papers, where each question is paired with gold answers and evidence annotations identifying the exact paper sections containing the answer.\"\n    }\n  ],\n  \"summary\": \"We hypothesize that standard cosine-similarity retrieval systematically mis-ranks sections in scientific PDFs by treating theme terms (shared across many sections) equally with section-specific terms, biasing retrieval toward claim-dense sections like Abstracts. Replacing cross-corpus IDF with a within-document Inverse Section Frequency (ISF) computed solely from the target paper's own section statistics corrects this bias without any training, discourse parsing, or LLM inference at retrieval time, and should improve answer F1 on QASPER over a fixed-k cosine baseline.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [50] ASSISTANT · 2026-07-20 10:10:16 UTC

```
The hypothesis has been written to `.terminal_claude_agent_struct_out.json`.

**Summary of the hypothesis:**

**Within-Document Inverse Section Frequency (TF-ISF) for Scientific Section Retrieval**

Standard cosine/BM25 retrieval over scientific PDFs is systematically biased toward Abstract/Introduction/Conclusion sections because these "claim-dense" sections repeat the paper's topic vocabulary in accessible language that closely resembles natural-language queries. Meanwhile, the actual evidence (Methods, Results) uses specialized, section-unique vocabulary that scores poorly under standard retrieval.

**The fix**: Replace cross-corpus IDF with an *Intra-Document* Inverse Section Frequency (ISF = log(N_sections / (1 + SF(t)))) computed from the target paper's own section statistics. This down-weights "document theme terms" that appear in many sections (low discriminative value) and up-weights section-specific terms that appear in only 1–2 sections (high discriminative value for locating evidence).

**What's novel**: The specific application of within-document section frequency as a retrieval signal has not been proposed. All existing structure-aware RAG approaches (Disco-RAG, SF-RAG, CG-RAG) require external parsers, citation graphs, or LLM inference at retrieval time. TF-ISF requires only the document itself and is computed from simple tokenization.

**Test**: Evaluate on QASPER with top-k=3 section retrieval, comparing cosine baseline vs. BM25 vs. TF-ISF, measured by section recall and answer F1 using a cheap LLM reader within the $10 budget.
```
