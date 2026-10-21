# Awesome AI Co-Scientist

AI systems that help researchers develop hypotheses, run experiments, evaluate evidence, and communicate discoveries.

[![Validate catalog](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml/badge.svg)](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

A curated, annotated guide to **papers, systems, tools, and benchmarks**, presented **newest first**. Each entry explains the contribution and its evidence boundary, with primary sources and a content-check date. The collection includes autonomous systems and human-guided research workflows.

## Contents

- [Explore the collection](#explore-the-collection)
- [Start here](#start-here)
- [Choose a reading path](#choose-a-reading-path)
- [How to read the evidence](#how-to-read-the-evidence)
- [Curation and daily updates](#curation-and-daily-updates)
- [Repository layout](#repository-layout)
- [Contribute](#contribute)
- [Acknowledgements and license](#acknowledgements-and-license)

## Explore the collection

**85 records** · Latest source-check date: **2026-10-22**. Counts distinguish papers from software; a research family may appear in both.

| Collection | Records | What you will find |
| --- | ---: | --- |
| [Papers](docs/papers.md) | 39 | Mechanisms, research findings, surveys, and scientific limitations. |
| [Systems](docs/systems.md) | 13 | Integrated research agents and end-to-end research environments. |
| [Tools](docs/tools.md) | 15 | Literature, experiments, writing, figures, and reusable infrastructure. |
| [Benchmarks](docs/benchmarks.md) | 18 | Task definitions, evaluation protocols, and what scores do—and do not—measure. |

## Start here

These selected entry points are ordered by publication/release date, newest first. Entries with only a known year follow dated entries from that year. The full catalogs use the same ordering and retain topic indexes.

- **2026-10-13 — [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](docs/papers.md#agentic-scientist)** (preprint). Coordinates coding agents through task drafting, ideas, sandboxed experiments, baselines, ablations, analysis, and manuscript writing. A meta-controller enforces stage-specific rubrics. The paper reports computational discovery studies and an ALIFE 2026 paper produced in a co-scientist setting; that human collaboration should be distinguished from its separate autonomous evaluations.

- **2026-09-17 — [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](docs/papers.md#scientist-two)** (preprint). Starts from a research problem, establishes baselines, proposes hypotheses, runs experiments and ablations, and iterates through simulated reviews and rebuttals. Evaluation uses tasks derived from major machine-learning conference papers. Reported performance and automated reviewer preferences are promising research evidence, but simulated acceptance is not independent peer review.

- **2026-09-15 — [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](docs/papers.md#sciencebuddy)** (preprint). Turns researcher requests, feedback, and execution traces into learning tasks and evaluation rubrics. An inner loop adapts the agent harness while an outer loop trains the model under the improved harness. Case studies cover four scientific task families; they demonstrate the proposed learning workflow rather than universal autonomous discovery.

- **2026-07-03 — [ResearchStudio](docs/tools.md#researchstudio-tool)** (preprint). Microsoft's research skill collection includes Idea for developing literature-grounded research proposals and Reel for turning completed papers into posters, narrated videos, blogs, and interactive presentations. The code exposes editable workflows for coding agents. Its two modules support different stages of research and communication; their presence does not establish an autonomous experimental discovery pipeline.

- **2026-05-25 — [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](docs/papers.md#scientist-one)** (preprint). Maintains explicit evidence chains from literature and experiments to manuscript claims, with audits for score reproduction, specification violations, references, and method-code agreement. The authors compare generated papers across research tasks and report improved integrity. These are task-specific audits, so the title's human-level claim should not be generalized to all research.

- **2026-05-19 — [Accelerating scientific discovery with Co-Scientist](docs/papers.md#google-co-scientist)** (peer-reviewed). Uses specialized agents to generate, criticize, rank, and evolve hypotheses through tournaments, with scientists setting goals and steering exploration. The Nature paper includes biomedical applications and laboratory validation of selected hypotheses. The system supports scientific reasoning; experimental validation remains a distinct process rather than an automatically closed physical loop.

- **2026-04-06 — [PaperOrchestra](docs/tools.md#paperorchestra-tool)** (preprint). Transforms research ideas, experimental records, and formatting requirements into LaTeX manuscripts through specialized planning, literature, plotting, writing, and refinement agents. The official Google Research repository accompanies the paper and evaluation resources. It addresses synthesis of existing research materials; manuscript quality ratings do not verify that the underlying experiments or scientific conclusions are correct.

- **2026 — [OpenResearch](docs/systems.md#openresearch-system)** (project). A local research workspace and harness from alphaXiv that connects coding agents to literature discovery, experiment execution, and artifact inspection. It records experiments in a local database and supports multiple compute backends. The repository documents a usable product; these capabilities are project claims rather than an independently established discovery benchmark.

- **2025-04-02 — [PaperBench](docs/benchmarks.md#paperbench)** (peer-reviewed). Asks agents to implement and execute replications of 20 ICML 2024 papers from scratch. Author-developed hierarchical rubrics divide the work into 8,316 gradable items, with a separately assessed model-based grader. Scores indicate progress toward specified replication requirements; code-only variants, partial rubric credit, and successful empirical replication must be distinguished.

- **2024-10-07 — [ScienceAgentBench](docs/benchmarks.md#scienceagentbench)** (peer-reviewed). Contains 102 expert-validated tasks derived from 44 publications across four disciplines. Each task requires a self-contained Python program, assessed through code, execution outputs, and costs. The benchmark deliberately tests individual data-driven research steps, providing a stronger basis for bounded capability claims than treating generated manuscripts as evidence of complete scientific discovery.

## Choose a reading path

| Your question | Suggested route |
| --- | --- |
| What does an AI co-scientist actually automate? | Start with Google AI co-scientist, Sakana's AI Scientist lineage, ScientistOne/Two, and ScienceBuddy in [Papers](docs/papers.md). Compare human input, experiment access, memory, and validation. |
| What can I inspect or build on? | Use [Systems](docs/systems.md) to find official implementations and identify projects that expose only demos or artifacts. Then choose supporting [Tools](docs/tools.md). |
| How should I evaluate one? | Start with [Benchmarks](docs/benchmarks.md): distinguish ML engineering, code execution, replication, idea evaluation, and long-horizon research. |
| How do research agents extend beyond ML? | Read the [domain-science papers](docs/papers.md#topic-domain-science) and examine their laboratory access, data, experimental controls, and human roles. |
| How do I improve one research stage? | Browse [Tools](docs/tools.md) by literature, ideation, experimentation, writing, or infrastructure. |

## How to read the evidence

- **Preprint**: a public research manuscript; peer review is not established by this label.
- **Peer-reviewed**: a linked journal or proceedings record supports that status. Peer review is not independent replication.
- **Project**: claims are grounded in official project documentation or a release. An implementation, demo, or hosted service is not proof of research effectiveness.
- **Content checked**: the listed primary source was inspected on that date. We have not installed or independently reproduced every system.

Reported evaluations remain specific to their tasks, datasets, budgets, human involvement, and evaluation methods. Automated judging, execution success, paper acceptance, and validated scientific discovery are different outcomes. Missing code links mean availability is unconfirmed here, not necessarily that no code exists.

## Curation and daily updates

We search broadly and curate selectively. See the [search protocol and coverage gaps](docs/search-protocol.md), [dated changes](CHANGELOG.md), and [maintenance policy](docs/curation.md). The initial search spans multiple query families, reference trails, existing lists, papers, and official projects; it is **not a claim of exhaustive literature coverage**.

Daily curation is intended to check new research and project changes, read primary evidence, deduplicate entries, run validation, and publish substantive updates. GitHub Actions checks catalog structure and generated-file consistency. No-change searches do not create cosmetic commits.

This repository is **AI-assisted and maintainer-owned**. Source-backed annotations remain open to correction; neither AI generation nor automated checks substitute for expert review.

## Repository layout

```text
README.md                 Overview and selected starting points (generated)
data/                     Canonical JSON catalogs and featured entry IDs
docs/papers.md            Annotated paper catalog (generated)
docs/systems.md           Annotated system catalog (generated)
docs/tools.md             Annotated tool catalog (generated)
docs/benchmarks.md        Annotated evaluation catalog (generated)
docs/search-*.md          Search protocol, source trails, and coverage limits
docs/curation.md          Inclusion rules, evidence labels, and daily process
scripts/                  Standard-library renderer, validator, and link checker
.github/                  Contribution templates and validation workflow
CHANGELOG.md              Substantive additions and corrections
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md), then [suggest a resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new/choose). Explain its contribution, provide primary evidence, and preserve the distinction between an author claim and an independently verified result.

## Acknowledgements and license

The organization follows useful conventions from the [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): focused scope, descriptive annotations, navigable categories, and clear contribution rules. [Related lists and design lessons](docs/search-landscape.md) explain the sources consulted and how this collection differs.

This is an independent collection, with no claim of inclusion in or endorsement by the main Awesome index. That index's [current contribution rules](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) exclude AI-generated lists.

Original catalog content and scripts are dedicated under [CC0 1.0](LICENSE). Linked papers, software, data, and trademarks retain their respective terms.
