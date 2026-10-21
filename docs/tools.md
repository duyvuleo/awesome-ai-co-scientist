# Tools

[← Overview](../README.md) · [Search coverage](search-protocol.md)

15 annotated records, ordered **newest first by publication/release date**, grouped by year. Entries with only a known year appear separately after the dated entries for that year; their position within the year is unknown. Same-date ties are ordered by name. Source status describes publication provenance. Catalog inclusion does not imply end-to-end replication; [local reproducibility reports](reproducibility.md) document the exact scope of selected execution checks.

## Contents

- [2026](#year-2026)
- [2025](#year-2025)
- [2024](#year-2024)
- [2023](#year-2023)
- [2021](#year-2021)
- [Browse by topic](#browse-by-topic)

<a id="year-2026"></a>

## 2026

<a id="researchstudio-tool"></a>

### [ResearchStudio](https://github.com/microsoft/ResearchStudio) · [Paper](https://arxiv.org/abs/2607.04439)

**2026-07-03 · preprint** · Ideation and planning · code-available, coding-agent-skills, research-ideas, research-communication

Microsoft's research skill collection includes Idea for developing literature-grounded research proposals and Reel for turning completed papers into posters, narrated videos, blogs, and interactive presentations. The code exposes editable workflows for coding agents. Its two modules support different stages of research and communication; their presence does not establish an autonomous experimental discovery pipeline.

Sources: [1](https://github.com/microsoft/ResearchStudio) · [2](https://arxiv.org/abs/2607.04439) · [3](https://arxiv.org/abs/2607.04438) · Content checked: 2026-10-22.

<a id="paperorchestra-tool"></a>

### [PaperOrchestra](https://github.com/google-research/paper-orchestra) · [Paper](https://arxiv.org/abs/2604.05018)

**2026-04-06 · preprint** · Writing and scientific communication · code-available, latex, multi-agent, paper-writing

Transforms research ideas, experimental records, and formatting requirements into LaTeX manuscripts through specialized planning, literature, plotting, writing, and refinement agents. The official Google Research repository accompanies the paper and evaluation resources. It addresses synthesis of existing research materials; manuscript quality ratings do not verify that the underlying experiments or scientific conclusions are correct.

Sources: [1](https://github.com/google-research/paper-orchestra) · [2](https://arxiv.org/abs/2604.05018) · Content checked: 2026-10-22.

### Year-only dates

Month and day have not been established.

<a id="autoillustrate-tool"></a>

#### [AutoIllustrate](https://github.com/SakanaAI/AutoIllustrate)

**2026 · project** · Writing and scientific communication · code-available, academic-figures, editable-diagrams, visual-verification

Converts a method description into an editable draw.io diagram, then optionally applies an image-generation restyling pass. The public command-line workflow includes figure generation and visual auditing and was used with Agentic Scientist. Retaining the vector source supports manual correction, but generated visual polish should not be taken as evidence of methodological fidelity.

Sources: [1](https://github.com/SakanaAI/AutoIllustrate) · Content checked: 2026-10-22.

<a id="paperbanana-tool"></a>

#### [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) · [Paper](https://arxiv.org/abs/2601.23265)

**2026 · preprint** · Writing and scientific communication · code-available, academic-figures, multi-agent, benchmark

Uses retrieval, planning, styling, visualization, and critique agents to generate academic diagrams and plots from scientific content. Its repository includes execution interfaces and a benchmark of reference illustrations. It is a useful study of iterative visual communication, with semantic accuracy and faithful representation of experimental data still requiring inspection beyond aesthetic judgments.

Sources: [1](https://github.com/dwzhu-pku/PaperBanana) · [2](https://arxiv.org/abs/2601.23265) · Content checked: 2026-10-22.

<a id="year-2025"></a>

## 2025


### Year-only dates

Month and day have not been established.

<a id="aide-tool"></a>

#### [AIDE](https://github.com/WecoAI/aideml) · [Paper](https://arxiv.org/abs/2502.13138)

**2025 · preprint** · Experimentation and implementation · code-available, tree-search, machine-learning, code-optimization

Searches over executable machine-learning solutions by repeatedly drafting, debugging, evaluating, and improving code against a specified metric. The public reference implementation includes configuration and search-tree inspection utilities. It is a reusable experiment-search component and benchmark baseline, with results bounded by evaluator quality, data access, and safeguards against exploiting the evaluation setup.

Sources: [1](https://github.com/WecoAI/aideml) · [2](https://arxiv.org/abs/2502.13138) · Content checked: 2026-10-22.

<a id="openevolve-tool"></a>

#### [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve)

**2025 · project** · Experimentation and implementation · code-available, community-implementation, program-evolution, algorithm-discovery

An open community implementation inspired by AlphaEvolve that evolves programs using language models, evaluator feedback, and population-based search. It includes examples for mathematical optimization, scientific computing, and kernel improvement. The repository is independently maintained rather than Google's original system, and its reported improvements should be checked against the corresponding evaluator and hardware conditions.

Sources: [1](https://github.com/algorithmicsuperintelligence/openevolve) · Content checked: 2026-10-22.

<a id="rd-agent-tool"></a>

#### [R&D-Agent](https://github.com/microsoft/RD-Agent) · [Paper](https://arxiv.org/abs/2505.14738)

**2025 · preprint** · Experimentation and implementation · code-available, data-science, feedback-loop, model-development

Separates research proposal generation from development and evaluation, then iterates using experimental feedback. Microsoft's public project includes data-science, model-development, and quantitative-finance scenarios. It offers a practical architecture for automating repeated implementation work; success in an included scenario does not establish broad scientific discovery ability or transfer to unrelated domains.

Sources: [1](https://github.com/microsoft/RD-Agent) · [2](https://arxiv.org/abs/2505.14738) · Content checked: 2026-10-22.

<a id="shinkaevolve-tool"></a>

#### [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) · [Paper](https://arxiv.org/abs/2509.19349)

**2025 · peer-reviewed** · Experimentation and implementation · code-available, program-evolution, algorithm-discovery, verifiers

Combines language-model program mutations with evolutionary search, solution archives, and evaluation feedback to improve algorithms. The public framework supports local or cluster evaluation and tasks with executable verifiers. It is suited to measurable algorithm discovery, with scientific conclusions limited by what the verifier and optimization objective actually test.

Sources: [1](https://github.com/SakanaAI/ShinkaEvolve) · [2](https://arxiv.org/abs/2509.19349) · [3](https://openreview.net/forum?id=lKEdGCoDNC) · Content checked: 2026-10-22.

<a id="tooluniverse-tool"></a>

#### [ToolUniverse](https://github.com/mims-harvard/ToolUniverse) · [Paper](https://arxiv.org/abs/2509.23426)

**2025 · preprint** · Research infrastructure · code-available, scientific-tools, mcp, tool-use

Provides a common interface for scientific tools, datasets, models, and APIs so language-model agents can discover and invoke external capabilities. The public project offers a Python SDK and agent integrations. It supplies infrastructure for building scientific assistants; available tool connectors do not by themselves establish reliable tool selection, valid analyses, or experimental reproducibility.

Sources: [1](https://github.com/mims-harvard/ToolUniverse) · [2](https://arxiv.org/abs/2509.23426) · Content checked: 2026-10-22.

<a id="year-2024"></a>

## 2024

<a id="paperqa2-tool"></a>

### [PaperQA2](https://github.com/Future-House/paper-qa) · [Paper](https://arxiv.org/abs/2409.13740)

**2024-09-10 · preprint** · Literature discovery and synthesis · code-available, agentic-rag, citations, scientific-question-answering

An agentic retrieval system for answering scientific questions with cited evidence from documents. It combines paper search, metadata collection, contextual evidence summaries, and iterative answer generation, with a public Python package and command-line interface. The research reports strong literature-task performance; those results concern particular evaluations rather than guaranteed factual correctness for every answer.

Sources: [1](https://github.com/Future-House/paper-qa) · [2](https://arxiv.org/abs/2409.13740) · Content checked: 2026-10-22.

### Year-only dates

Month and day have not been established.

<a id="docling-tool"></a>

#### [Docling](https://github.com/docling-project/docling) · [Paper](https://arxiv.org/abs/2408.09869)

**2024 · preprint** · Research infrastructure · code-available, document-parsing, pdf, research-ingestion

Converts PDFs and other documents into structured representations for retrieval and downstream analysis, including layout-aware extraction and handling of tables and figures. Its open implementation supports research-document ingestion. It is an enabling component rather than a scientist agent; extraction quality should be checked before treating parsed tables, formulas, or reading order as reliable evidence.

Sources: [1](https://github.com/docling-project/docling) · [2](https://arxiv.org/abs/2408.09869) · Content checked: 2026-10-22.

<a id="openscholar-tool"></a>

#### [OpenScholar](https://github.com/AkariAsai/OpenScholar) · [Paper](https://www.nature.com/articles/s41586-025-10072-4)

**2024 · peer-reviewed** · Literature discovery and synthesis · code-available, open-models, scientific-synthesis, citations

Pairs scientific retrieval with a language model trained to synthesize evidence and attach supporting citations. The authors provide implementation resources, models, data, and scientific question-answering evaluations, with a later Nature publication. It is a foundation for literature-grounded assistants; retrieval coverage and citation quality remain properties to evaluate for each downstream corpus and task.

Sources: [1](https://github.com/AkariAsai/OpenScholar) · [2](https://www.nature.com/articles/s41586-025-10072-4) · [3](https://allenai.org/blog/nature-openscilm) · Content checked: 2026-10-22.

<a id="storm-tool"></a>

#### [STORM / Co-STORM](https://github.com/stanford-oval/storm) · [Paper](https://arxiv.org/abs/2402.14207)

**2024 · peer-reviewed** · Literature discovery and synthesis · code-available, knowledge-curation, human-ai-collaboration, report-writing

Builds sourced topic outlines and long-form articles by combining retrieval with questions from multiple perspectives. Co-STORM adds collaborative discussion and a shared concept map so users can steer exploration. The official implementation is useful for research preparation and knowledge curation; its authors explicitly note that generated articles often require substantial editing.

Sources: [1](https://github.com/stanford-oval/storm) · [2](https://arxiv.org/abs/2402.14207) · [3](https://aclanthology.org/2024.naacl-long.347/) · Content checked: 2026-10-22.

<a id="year-2023"></a>

## 2023

<a id="gpt-researcher-tool"></a>

### [GPT Researcher](https://github.com/assafelovic/gpt-researcher)

**2023-07-23 · project** · Literature discovery and synthesis · code-available, web-research, report-writing, multi-agent

A configurable research agent that decomposes questions, gathers evidence from web or local sources, and assembles cited reports. It exposes a package, interfaces, and multi-agent or recursive research workflows. It is useful as a general research component, but its project-level claims should not be confused with scientific novelty or independently validated literature-review completeness.

Sources: [1](https://github.com/assafelovic/gpt-researcher) · [2](https://github.com/assafelovic/gpt-researcher/blob/master/citation.cff) · Content checked: 2026-10-22.

<a id="year-2021"></a>

## 2021


### Year-only dates

Month and day have not been established.

<a id="asreview-tool"></a>

#### [ASReview LAB](https://github.com/asreview/asreview) · [Paper](https://www.nature.com/articles/s42256-020-00287-7)

**2021 · peer-reviewed** · Literature discovery and synthesis · code-available, active-learning, systematic-review, human-screening

Uses active learning to prioritize records during systematic literature screening while preserving human inclusion decisions. It provides a screening interface, simulation tools, label management, and exportable review state. This is a complementary evidence-selection tool rather than a generative scientist; screening completeness depends on the review protocol, labels, and stopping decision.

Sources: [1](https://github.com/asreview/asreview) · [2](https://www.nature.com/articles/s42256-020-00287-7) · Content checked: 2026-10-22.

## Browse by topic

Jump to an entry above; links within each topic follow the same date order.

<a id="topic-literature"></a>

### Literature discovery and synthesis

- **2024-09-10** — [PaperQA2](#paperqa2-tool).
- **2024** — [OpenScholar](#openscholar-tool).
- **2024** — [STORM / Co-STORM](#storm-tool).
- **2023-07-23** — [GPT Researcher](#gpt-researcher-tool).
- **2021** — [ASReview LAB](#asreview-tool).

<a id="topic-ideation"></a>

### Ideation and planning

- **2026-07-03** — [ResearchStudio](#researchstudio-tool).

<a id="topic-experimentation"></a>

### Experimentation and implementation

- **2025** — [AIDE](#aide-tool).
- **2025** — [OpenEvolve](#openevolve-tool).
- **2025** — [R&D-Agent](#rd-agent-tool).
- **2025** — [ShinkaEvolve](#shinkaevolve-tool).

<a id="topic-writing"></a>

### Writing and scientific communication

- **2026-04-06** — [PaperOrchestra](#paperorchestra-tool).
- **2026** — [AutoIllustrate](#autoillustrate-tool).
- **2026** — [PaperBanana](#paperbanana-tool).

<a id="topic-infrastructure"></a>

### Research infrastructure

- **2025** — [ToolUniverse](#tooluniverse-tool).
- **2024** — [Docling](#docling-tool).
