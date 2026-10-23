# Tools

[← Overview](../README.md) · [Search coverage](search-protocol.md)

17 annotated records, ordered **newest first by publication/release date**, grouped by year. Year-only entries follow dated entries within each year; ties are alphabetical. Source status identifies publication provenance. See [local reports](reproducibility.md) for executed component checks.

Expand **Sources & metadata** for citations, topics, related entries, and inspection dates.

## Contents

- [2026](#year-2026)
- [2025](#year-2025)
- [2024](#year-2024)
- [2023](#year-2023)
- [2021](#year-2021)
- [Browse by topic](#browse-by-topic)

<a id="year-2026"></a>

## 2026

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2026&#8209;10&#8209;23</code> | <a id="ridar-tool"></a>**[RIDAR](https://github.com/THU-KEG/RIDAR)**<br>*preprint* | Provides trajectory collectors, post-hoc integrity detection, runtime intervention, and a monitoring interface for research agents. Findings link to evidence in recorded runs, with public result files accompanying the implementation. It supports investigation of agent research behavior; detector output requires contextual review and does not certify scientific validity.<br><br><strong>Status:</strong> Official repository announces the code release on 23 October. No installation or runtime validation was performed here.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Research infrastructure<br><strong>Tags:</strong> code-available, research-integrity, trajectory-audit, runtime-intervention<br><strong>Sources:</strong> <a href="https://github.com/THU-KEG/RIDAR">1</a> · <a href="https://arxiv.org/abs/2610.31372">2</a><br><strong>Content checked:</strong> 2026-10-24<br><strong>Related entries:</strong> <a href="papers.md#ridar">RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention</a>, <a href="benchmarks.md#riv-gold">RIV-Gold</a></details> | [Paper](https://arxiv.org/abs/2610.31372) |
| <code>2026&#8209;10&#8209;21</code> | <a id="recursive-flint-tool"></a>**[Recursive Flint](https://recursive.com/updates/introducing-recursive-flint)**<br>*project* | An open-weight mixture-of-experts coding model built with Recursive’s Eureka Machine and a human team. The model card specifies 39.8B total parameters and approximately 2.5B active per token, including the output head. Included as a concrete automated-research output and reusable coding component; released weights and inference code do not independently validate the development process or reported performance.<br><br><strong>Status:</strong> Apache-2.0 weights and inference engine; no local execution or independent performance reproduction in this collection.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Research infrastructure<br><strong>Tags:</strong> research-output, open-weights, local-coding, machine-learning, inference-code<br><strong>Sources:</strong> <a href="https://recursive.com/updates/introducing-recursive-flint">1</a> · <a href="https://huggingface.co/RecursiveSI/flint">2</a> · <a href="https://github.com/recursive-oss/rec">3</a> · <a href="https://docs.recursive.com/">4</a> · <a href="https://recursive.com/updates">5</a><br><strong>Content checked:</strong> 2026-10-22<br><strong>Related entries:</strong> <a href="systems.md#recursive-eureka-machine-system">Recursive Eureka Machine</a></details> | [Code](https://github.com/recursive-oss/rec) |
| <code>2026&#8209;07&#8209;03</code> | <a id="researchstudio-tool"></a>**[ResearchStudio](https://github.com/microsoft/ResearchStudio)**<br>*preprint* | Microsoft's research skill collection includes Idea for developing literature-grounded research proposals and Reel for turning completed papers into posters, narrated videos, blogs, and interactive presentations. The code exposes editable workflows for coding agents. Its two modules support different stages of research and communication; their presence does not establish an autonomous experimental discovery pipeline.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Ideation and planning<br><strong>Tags:</strong> code-available, coding-agent-skills, research-ideas, research-communication<br><strong>Sources:</strong> <a href="https://github.com/microsoft/ResearchStudio">1</a> · <a href="https://arxiv.org/abs/2607.04439">2</a> · <a href="https://arxiv.org/abs/2607.04438">3</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2607.04439) |
| <code>2026&#8209;04&#8209;06</code> | <a id="paperorchestra-tool"></a>**[PaperOrchestra](https://github.com/google-research/paper-orchestra)**<br>*preprint* | Transforms research ideas, experimental records, and formatting requirements into LaTeX manuscripts through specialized planning, literature, plotting, writing, and refinement agents. The official Google Research repository accompanies the paper and evaluation resources. It addresses synthesis of existing research materials; manuscript quality ratings do not verify that the underlying experiments or scientific conclusions are correct.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Writing and scientific communication<br><strong>Tags:</strong> code-available, latex, multi-agent, paper-writing<br><strong>Sources:</strong> <a href="https://github.com/google-research/paper-orchestra">1</a> · <a href="https://arxiv.org/abs/2604.05018">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2604.05018) |

### Year-only dates

Month and day have not been established.

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2026</code> | <a id="autoillustrate-tool"></a>**[AutoIllustrate](https://github.com/SakanaAI/AutoIllustrate)**<br>*project* | Converts a method description into an editable draw.io diagram, then optionally applies an image-generation restyling pass. The public command-line workflow includes figure generation and visual auditing and was used with Agentic Scientist. Retaining the vector source supports manual correction, but generated visual polish should not be taken as evidence of methodological fidelity.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Writing and scientific communication<br><strong>Tags:</strong> code-available, academic-figures, editable-diagrams, visual-verification<br><strong>Sources:</strong> <a href="https://github.com/SakanaAI/AutoIllustrate">1</a><br><strong>Content checked:</strong> 2026-10-22</details> | — |
| <code>2026</code> | <a id="paperbanana-tool"></a>**[PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**<br>*preprint* | Uses retrieval, planning, styling, visualization, and critique agents to generate academic diagrams and plots from scientific content. Its repository includes execution interfaces and a benchmark of reference illustrations. It is a useful study of iterative visual communication, with semantic accuracy and faithful representation of experimental data still requiring inspection beyond aesthetic judgments.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Writing and scientific communication<br><strong>Tags:</strong> code-available, academic-figures, multi-agent, benchmark<br><strong>Sources:</strong> <a href="https://github.com/dwzhu-pku/PaperBanana">1</a> · <a href="https://arxiv.org/abs/2601.23265">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2601.23265) |

<a id="year-2025"></a>

## 2025


### Year-only dates

Month and day have not been established.

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2025</code> | <a id="aide-tool"></a>**[AIDE](https://github.com/WecoAI/aideml)**<br>*preprint* | Searches over executable machine-learning solutions by repeatedly drafting, debugging, evaluating, and improving code against a specified metric. The public reference implementation includes configuration and search-tree inspection utilities. It is a reusable experiment-search component and benchmark baseline, with results bounded by evaluator quality, data access, and safeguards against exploiting the evaluation setup.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Experimentation and implementation<br><strong>Tags:</strong> code-available, tree-search, machine-learning, code-optimization<br><strong>Sources:</strong> <a href="https://github.com/WecoAI/aideml">1</a> · <a href="https://arxiv.org/abs/2502.13138">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2502.13138) |
| <code>2025</code> | <a id="openevolve-tool"></a>**[OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve)**<br>*project* | An open community implementation inspired by AlphaEvolve that evolves programs using language models, evaluator feedback, and population-based search. It includes examples for mathematical optimization, scientific computing, and kernel improvement. The repository is independently maintained rather than Google's original system, and its reported improvements should be checked against the corresponding evaluator and hardware conditions.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Experimentation and implementation<br><strong>Tags:</strong> code-available, community-implementation, program-evolution, algorithm-discovery<br><strong>Sources:</strong> <a href="https://github.com/algorithmicsuperintelligence/openevolve">1</a><br><strong>Content checked:</strong> 2026-10-22</details> | — |
| <code>2025</code> | <a id="rd-agent-tool"></a>**[R&amp;D-Agent](https://github.com/microsoft/RD-Agent)**<br>*preprint* | Separates research proposal generation from development and evaluation, then iterates using experimental feedback. Microsoft's public project includes data-science, model-development, and quantitative-finance scenarios. It offers a practical architecture for automating repeated implementation work; success in an included scenario does not establish broad scientific discovery ability or transfer to unrelated domains.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Experimentation and implementation<br><strong>Tags:</strong> code-available, data-science, feedback-loop, model-development<br><strong>Sources:</strong> <a href="https://github.com/microsoft/RD-Agent">1</a> · <a href="https://arxiv.org/abs/2505.14738">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2505.14738) |
| <code>2025</code> | <a id="shinkaevolve-tool"></a>**[ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve)**<br>*peer reviewed* | Combines language-model program mutations with evolutionary search, solution archives, and evaluation feedback to improve algorithms. The public framework supports local or cluster evaluation and tasks with executable verifiers. It is suited to measurable algorithm discovery, with scientific conclusions limited by what the verifier and optimization objective actually test.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Experimentation and implementation<br><strong>Tags:</strong> code-available, program-evolution, algorithm-discovery, verifiers<br><strong>Sources:</strong> <a href="https://github.com/SakanaAI/ShinkaEvolve">1</a> · <a href="https://arxiv.org/abs/2509.19349">2</a> · <a href="https://openreview.net/forum?id=lKEdGCoDNC">3</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2509.19349) |
| <code>2025</code> | <a id="tooluniverse-tool"></a>**[ToolUniverse](https://github.com/mims-harvard/ToolUniverse)**<br>*preprint* | Provides a common interface for scientific tools, datasets, models, and APIs so language-model agents can discover and invoke external capabilities. The public project offers a Python SDK and agent integrations. It supplies infrastructure for building scientific assistants; available tool connectors do not by themselves establish reliable tool selection, valid analyses, or experimental reproducibility.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Research infrastructure<br><strong>Tags:</strong> code-available, scientific-tools, mcp, tool-use<br><strong>Sources:</strong> <a href="https://github.com/mims-harvard/ToolUniverse">1</a> · <a href="https://arxiv.org/abs/2509.23426">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2509.23426) |

<a id="year-2024"></a>

## 2024

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2024&#8209;09&#8209;10</code> | <a id="paperqa2-tool"></a>**[PaperQA2](https://github.com/Future-House/paper-qa)**<br>*preprint* | An agentic retrieval system for answering scientific questions with cited evidence from documents. It combines paper search, metadata collection, contextual evidence summaries, and iterative answer generation, with a public Python package and command-line interface. The research reports strong literature-task performance; those results concern particular evaluations rather than guaranteed factual correctness for every answer.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Literature discovery and synthesis<br><strong>Tags:</strong> code-available, agentic-rag, citations, scientific-question-answering<br><strong>Sources:</strong> <a href="https://github.com/Future-House/paper-qa">1</a> · <a href="https://arxiv.org/abs/2409.13740">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2409.13740) |

### Year-only dates

Month and day have not been established.

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2024</code> | <a id="docling-tool"></a>**[Docling](https://github.com/docling-project/docling)**<br>*preprint* | Converts PDFs and other documents into structured representations for retrieval and downstream analysis, including layout-aware extraction and handling of tables and figures. Its open implementation supports research-document ingestion. It is an enabling component rather than a scientist agent; extraction quality should be checked before treating parsed tables, formulas, or reading order as reliable evidence.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Research infrastructure<br><strong>Tags:</strong> code-available, document-parsing, pdf, research-ingestion<br><strong>Sources:</strong> <a href="https://github.com/docling-project/docling">1</a> · <a href="https://arxiv.org/abs/2408.09869">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2408.09869) |
| <code>2024</code> | <a id="openscholar-tool"></a>**[OpenScholar](https://github.com/AkariAsai/OpenScholar)**<br>*peer reviewed* | Pairs scientific retrieval with a language model trained to synthesize evidence and attach supporting citations. The authors provide implementation resources, models, data, and scientific question-answering evaluations, with a later Nature publication. It is a foundation for literature-grounded assistants; retrieval coverage and citation quality remain properties to evaluate for each downstream corpus and task.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Literature discovery and synthesis<br><strong>Tags:</strong> code-available, open-models, scientific-synthesis, citations<br><strong>Sources:</strong> <a href="https://github.com/AkariAsai/OpenScholar">1</a> · <a href="https://www.nature.com/articles/s41586-025-10072-4">2</a> · <a href="https://allenai.org/blog/nature-openscilm">3</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://www.nature.com/articles/s41586-025-10072-4) |
| <code>2024</code> | <a id="storm-tool"></a>**[STORM / Co-STORM](https://github.com/stanford-oval/storm)**<br>*peer reviewed* | Builds sourced topic outlines and long-form articles by combining retrieval with questions from multiple perspectives. Co-STORM adds collaborative discussion and a shared concept map so users can steer exploration. The official implementation is useful for research preparation and knowledge curation; its authors explicitly note that generated articles often require substantial editing.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Literature discovery and synthesis<br><strong>Tags:</strong> code-available, knowledge-curation, human-ai-collaboration, report-writing<br><strong>Sources:</strong> <a href="https://github.com/stanford-oval/storm">1</a> · <a href="https://arxiv.org/abs/2402.14207">2</a> · <a href="https://aclanthology.org/2024.naacl-long.347/">3</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://arxiv.org/abs/2402.14207) |

<a id="year-2023"></a>

## 2023

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2023&#8209;07&#8209;23</code> | <a id="gpt-researcher-tool"></a>**[GPT Researcher](https://github.com/assafelovic/gpt-researcher)**<br>*project* | A configurable research agent that decomposes questions, gathers evidence from web or local sources, and assembles cited reports. It exposes a package, interfaces, and multi-agent or recursive research workflows. It is useful as a general research component, but its project-level claims should not be confused with scientific novelty or independently validated literature-review completeness.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Literature discovery and synthesis<br><strong>Tags:</strong> code-available, web-research, report-writing, multi-agent<br><strong>Sources:</strong> <a href="https://github.com/assafelovic/gpt-researcher">1</a> · <a href="https://github.com/assafelovic/gpt-researcher/blob/master/citation.cff">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | — |

<a id="year-2021"></a>

## 2021


### Year-only dates

Month and day have not been established.

| Date | Resource / status | Summary & evidence | Links |
| --- | --- | --- | --- |
| <code>2021</code> | <a id="asreview-tool"></a>**[ASReview LAB](https://github.com/asreview/asreview)**<br>*peer reviewed* | Uses active learning to prioritize records during systematic literature screening while preserving human inclusion decisions. It provides a screening interface, simulation tools, label management, and exportable review state. This is a complementary evidence-selection tool rather than a generative scientist; screening completeness depends on the review protocol, labels, and stopping decision.<details><summary>Sources &amp; metadata</summary><strong>Topic:</strong> Literature discovery and synthesis<br><strong>Tags:</strong> code-available, active-learning, systematic-review, human-screening<br><strong>Sources:</strong> <a href="https://github.com/asreview/asreview">1</a> · <a href="https://www.nature.com/articles/s42256-020-00287-7">2</a><br><strong>Content checked:</strong> 2026-10-22</details> | [Paper](https://www.nature.com/articles/s42256-020-00287-7) |

## Browse by topic

Entries within each topic follow the same date order.

<a id="topic-literature"></a>

### Literature discovery and synthesis

| Date | Resource |
| --- | --- |
| <code>2024&#8209;09&#8209;10</code> | [PaperQA2](#paperqa2-tool) |
| <code>2024</code> | [OpenScholar](#openscholar-tool) |
| <code>2024</code> | [STORM / Co-STORM](#storm-tool) |
| <code>2023&#8209;07&#8209;23</code> | [GPT Researcher](#gpt-researcher-tool) |
| <code>2021</code> | [ASReview LAB](#asreview-tool) |

<a id="topic-ideation"></a>

### Ideation and planning

| Date | Resource |
| --- | --- |
| <code>2026&#8209;07&#8209;03</code> | [ResearchStudio](#researchstudio-tool) |

<a id="topic-experimentation"></a>

### Experimentation and implementation

| Date | Resource |
| --- | --- |
| <code>2025</code> | [AIDE](#aide-tool) |
| <code>2025</code> | [OpenEvolve](#openevolve-tool) |
| <code>2025</code> | [R&amp;D-Agent](#rd-agent-tool) |
| <code>2025</code> | [ShinkaEvolve](#shinkaevolve-tool) |

<a id="topic-writing"></a>

### Writing and scientific communication

| Date | Resource |
| --- | --- |
| <code>2026&#8209;04&#8209;06</code> | [PaperOrchestra](#paperorchestra-tool) |
| <code>2026</code> | [AutoIllustrate](#autoillustrate-tool) |
| <code>2026</code> | [PaperBanana](#paperbanana-tool) |

<a id="topic-infrastructure"></a>

### Research infrastructure

| Date | Resource |
| --- | --- |
| <code>2026&#8209;10&#8209;23</code> | [RIDAR](#ridar-tool) |
| <code>2026&#8209;10&#8209;21</code> | [Recursive Flint](#recursive-flint-tool) |
| <code>2025</code> | [ToolUniverse](#tooluniverse-tool) |
| <code>2024</code> | [Docling](#docling-tool) |
