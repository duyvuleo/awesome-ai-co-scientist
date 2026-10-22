<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="AI Co-Scientist: a research toolkit to compare systems, evaluate evidence, and reproduce results" src="assets/banner-light.svg" width="1280" height="360">
</picture>

# Awesome AI Co-Scientist

Find suitable AI co-scientist systems, design fair evaluations, and share evidence others can inspect.

[![Validate catalog](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml/badge.svg)](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

A collection of papers, systems, tools, and benchmarks on AI co-scientists and automated research. Each entry includes a short summary. You’ll also find system comparisons, evaluation guides, and reports on what we’ve tested locally.

## Contents

- [Start here](#start-here)
- [Quick start](#quick-start)
- [Research workflows](#research-workflows)
- [Explore the collection](#explore-the-collection)
- [Compare, reproduce, and synthesize](#compare-reproduce-and-synthesize)
- [Selected reading](#selected-reading)
- [Choose a reading path](#choose-a-reading-path)
- [How to read the evidence](#how-to-read-the-evidence)
- [Curation and daily updates](#curation-and-daily-updates)
- [Repository layout](#repository-layout)
- [Contribute](#contribute)
- [Acknowledgements and license](#acknowledgements-and-license)

## Start here

| Your task | Use | Leave with |
| --- | --- | --- |
| Understand the field | [Guided starting path](docs/start-here.md) and [research synthesis](docs/research-synthesis.md) | A concrete question and a reading plan. |
| Choose systems to investigate | [Offline search and comparison CLI](docs/cli.md) and [capability matrix](docs/capability-matrix.md) | A shortlist with sources, capabilities, and unresolved constraints. |
| Plan a defensible evaluation | [Evaluation guide](docs/evaluation-guide.md) and [study packs](docs/study-packs.md) | A declared protocol with controls, budgets, and an empty run record. |
| Inspect or repeat an executed check | [Local reproducibility reports](docs/reproducibility.md) | Pinned code, commands, configurations, observations, and limitations. |
| Contribute a useful finding | [Community contribution opportunities](docs/community-roadmap.md) | A correction, replication attempt, workflow lesson, or testable proposal. |
| Build on the catalog | [Data reference and exports](docs/data-reference.md) | Source-preserving JSON, CSV, or Markdown for your own tools. |

## Quick start

Python 3.10+ is sufficient for discovery and planning; no API keys or third-party packages are needed for these commands.

```bash
git clone https://github.com/duyvuleo/awesome-ai-co-scientist.git
cd awesome-ai-co-scientist
python3 scripts/explore.py search --kind system --tag human-ai-collaboration
python3 scripts/explore.py compare \
  agentic-scientist-system sciencebuddy-system --format markdown
python3 scripts/study_pack.py create \
  --recipe evaluator-integrity \
  --resources agentic-scientist-system \
  --output .local/my-study
python3 scripts/study_pack.py validate .local/my-study
```

After cloning, these commands work offline. They search local evidence and create a **planned** study; they do not run research systems, contact model APIs, or produce scientific results. Use a fresh output directory for each study. Completed records require execution details and hash-checked artifacts, while scientific validity still requires evidence review.

## Research workflows

| Recipe | Main question | Useful output |
| --- | --- | --- |
| [Evaluator integrity](docs/workflows/evaluator-integrity.md) | Does the evaluator distinguish valid results from misleading scores? | Valid/invalid fixtures and an independent calculation. |
| [Idea to experiment](docs/workflows/idea-to-experiment.md) | Which proposed ideas survive implementation and controlled evaluation? | A complete idea-to-artifact ledger, including failures. |
| [Human–AI collaboration](docs/workflows/human-ai-collaboration.md) | How do assistance, quality, and total researcher effort interact? | A matched-condition protocol and human-effort ledger. |

See the [workflow index](docs/workflows/README.md) for scope and prerequisites. These are proposed study designs; the separately dated [execution reports](docs/reproducibility.md) record what has actually run.

## Explore the collection

**87 records** · Latest source-check date: **2026-10-22**. Counts distinguish papers from software; a research family may appear in both.

| Collection | Records | What you will find |
| --- | ---: | --- |
| [Papers](docs/papers.md) | 39 | Mechanisms, research findings, surveys, and scientific limitations. |
| [Systems](docs/systems.md) | 14 | Integrated research agents and end-to-end research environments. |
| [Tools](docs/tools.md) | 16 | Literature, experiments, writing, figures, and reusable infrastructure. |
| [Benchmarks](docs/benchmarks.md) | 18 | Task definitions, evaluation protocols, and what scores do—and do not—measure. |

## Compare, reproduce, and synthesize

| Research question | Read | What the evidence establishes |
| --- | --- | --- |
| How do these systems differ? | [Capability and evidence matrix](docs/capability-matrix.md) | Human roles, hypothesis generation, execution, memory, verification, code access, and evaluation settings, with a source for every comparison cell. |
| What has automated research produced? | [Research outputs and evidence](docs/research-outputs.md) | Released artifacts, the system and human roles behind them, and the boundary between creator claims and independent reproduction. |
| What behavior can we reproduce locally? | [Reproducibility reports](docs/reproducibility.md) | Pinned public sources, runnable commands, recorded configurations, observed results and failures, and explicit limits on reproduced claims. |
| Which findings agree, conflict, or leave gaps? | [Cross-paper research synthesis](docs/research-synthesis.md) | Recurring limitations, tensions between studies, and testable open questions, separating reported findings from editorial interpretation. |

The matrix compares evidence rather than assigning a universal ranking. The initial execution reports are local component investigations with no paid model calls; they do not reproduce a complete scientist-agent discovery campaign.

## Selected reading

These selected entry points are ordered by publication/release date, newest first. Entries with only a known year follow dated entries from that year. The full catalogs use the same ordering and retain topic indexes.

<details>
<summary>Expand selected papers, systems, tools, and benchmarks</summary>

- **2026-10-13 — [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](docs/papers.md#agentic-scientist)** (preprint). Coordinates coding agents through task drafting, ideas, sandboxed experiments, baselines, ablations, analysis, and manuscript writing. A meta-controller enforces stage-specific rubrics. The paper reports computational discovery studies and an ALIFE 2026 paper produced in a co-scientist setting; that human collaboration should be distinguished from its separate autonomous evaluations.

- **2026-09-17 — [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](docs/papers.md#scientist-two)** (preprint). Starts from a research problem, establishes baselines, proposes hypotheses, runs experiments and ablations, and iterates through simulated reviews. Evaluation includes publication-derived machine-learning tasks, integrity audits, automated reviewers, and a human study of generated papers. These complementary author-reported assessments remain bounded by the selected tasks; simulated acceptance is distinct from actual venue acceptance.

- **2026-09-15 — [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](docs/papers.md#sciencebuddy)** (preprint). Turns researcher requests, feedback, and execution traces into learning tasks and evaluation rubrics. An inner loop adapts the agent harness while an outer loop trains the model under the improved harness. Case studies cover four scientific task families; they demonstrate the proposed learning workflow rather than universal autonomous discovery.

- **2026-07-03 — [ResearchStudio](docs/tools.md#researchstudio-tool)** (preprint). Microsoft's research skill collection includes Idea for developing literature-grounded research proposals and Reel for turning completed papers into posters, narrated videos, blogs, and interactive presentations. The code exposes editable workflows for coding agents. Its two modules support different stages of research and communication; their presence does not establish an autonomous experimental discovery pipeline.

- **2026-05-25 — [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](docs/papers.md#scientist-one)** (preprint). Maintains explicit evidence chains from literature and experiments to manuscript claims, with audits for score reproduction, specification violations, references, and method-code agreement. The authors compare generated papers across research tasks and report improved integrity. These are task-specific audits, so the title's human-level claim should not be generalized to all research.

- **2026-05-19 — [Accelerating scientific discovery with Co-Scientist](docs/papers.md#google-co-scientist)** (peer-reviewed). Uses specialized agents to generate, criticize, rank, and evolve hypotheses through tournaments, with scientists setting goals and steering exploration. The Nature paper includes biomedical applications and laboratory validation of selected hypotheses. The system supports scientific reasoning; experimental validation remains a distinct process rather than an automatically closed physical loop.

- **2026-04-06 — [PaperOrchestra](docs/tools.md#paperorchestra-tool)** (preprint). Transforms research ideas, experimental records, and formatting requirements into LaTeX manuscripts through specialized planning, literature, plotting, writing, and refinement agents. The official Google Research repository accompanies the paper and evaluation resources. It addresses synthesis of existing research materials; manuscript quality ratings do not verify that the underlying experiments or scientific conclusions are correct.

- **2026 — [OpenResearch](docs/systems.md#openresearch-system)** (project). A local research workspace and harness from alphaXiv that connects coding agents to literature discovery, experiment execution, and artifact inspection. It records experiments in a local database and supports multiple compute backends. The repository documents a usable product; these capabilities are project claims rather than an independently established discovery benchmark.

- **2025-04-02 — [PaperBench](docs/benchmarks.md#paperbench)** (peer-reviewed). Asks agents to implement and execute replications of 20 ICML 2024 papers from scratch. Author-developed hierarchical rubrics divide the work into 8,316 gradable items, with a separately assessed model-based grader. Scores indicate progress toward specified replication requirements; code-only variants, partial rubric credit, and successful empirical replication must be distinguished.

- **2024-10-07 — [ScienceAgentBench](docs/benchmarks.md#scienceagentbench)** (peer-reviewed). Contains 102 expert-validated tasks derived from 44 publications across four disciplines. Each task requires a self-contained Python program, assessed through code, execution outputs, and costs. The benchmark deliberately tests individual data-driven research steps, providing a stronger basis for bounded capability claims than treating generated manuscripts as evidence of complete scientific discovery.

</details>

## Choose a reading path

| Your question | Suggested route |
| --- | --- |
| What does an AI co-scientist actually automate? | Start with Google AI co-scientist, Sakana's AI Scientist lineage, ScientistOne/Two, and ScienceBuddy in [Papers](docs/papers.md). Compare human input, experiment access, memory, and validation. |
| What can I inspect or build on? | Use [Systems](docs/systems.md) to find official implementations and identify projects that expose only demos or artifacts. Then choose supporting [Tools](docs/tools.md). |
| How should I evaluate one? | Start with [Benchmarks](docs/benchmarks.md): distinguish ML engineering, code execution, replication, idea evaluation, and long-horizon research. |
| What has actually been run for this collection? | Read the [reproducibility reports](docs/reproducibility.md) for exact commands, observed behavior, costs, and untested claims. |
| Which research problems remain open? | Use the [cross-paper synthesis](docs/research-synthesis.md) to connect evidence gaps to concrete evaluation designs. |
| How do research agents extend beyond ML? | Read the [domain-science papers](docs/papers.md#topic-domain-science) and examine their laboratory access, data, experimental controls, and human roles. |
| How do I improve one research stage? | Browse [Tools](docs/tools.md) by literature, ideation, experimentation, writing, or infrastructure. |

## How to read the evidence

- **Preprint**: a public research manuscript; peer review is not established by this label.
- **Peer-reviewed**: a linked journal or proceedings record supports that status. Peer review is not independent replication.
- **Project**: claims are grounded in official project documentation or a release. An implementation, demo, or hosted service is not proof of research effectiveness.
- **Content checked**: the listed primary source was inspected on that date. This is distinct from a recorded execution date in a reproducibility report.

Reported evaluations remain specific to their tasks, datasets, budgets, human involvement, and evaluation methods. Automated judging, execution success, paper acceptance, and validated scientific discovery are different outcomes. Missing code links mean availability is unconfirmed here, not necessarily that no code exists.

## Curation and daily updates

We search broadly and curate selectively. See the [search protocol and coverage gaps](docs/search-protocol.md) and [dated changes](CHANGELOG.md). The initial search spans multiple query families, reference trails, existing lists, papers, and official projects; it is **not a claim of exhaustive literature coverage**.

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
docs/capability-matrix.md Comparison of system capabilities and evidence (generated)
docs/reproducibility.md   Index of bounded local execution reports
docs/research-synthesis.md Cross-paper findings and open questions
docs/start-here.md        Guided entry points and an offline first task
docs/workflows/           Worked evaluation recipes
docs/study-packs.md       Planning and evidence-record format
docs/cli.md               Search, inspect, compare, and export commands
docs/data-reference.md    Public data fields, joins, and reuse guidance
reports/reproducibility/ Pinned-source reports and observed run artifacts
templates/study/          Procedural study templates
tests/                    Offline behavior and artifact-integrity checks
docs/search-*.md          Search protocol, source trails, and coverage limits
scripts/                  Standard-library renderer, validator, and link checker
.github/                  Contribution templates and validation workflow
CHANGELOG.md              Substantive additions and corrections
```

## Contribute

Choose a [contribution opportunity](docs/community-roadmap.md) and read [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include failed attempts and unresolved observations when their evidence and limits are clear.

- [Suggest a resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=resource.yml).
- [Report a reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml).
- [Share practical experience or a proposed investigation](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml).

For reuse, see the [data reference](docs/data-reference.md) and [citation metadata](CITATION.cff). Cite the underlying papers for scientific claims and record the repository commit used for comparative analysis.

## Acknowledgements and license

The organization follows useful conventions from the [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): focused scope, descriptive annotations, navigable categories, and clear contribution rules. [Related lists and design lessons](docs/search-landscape.md) explain the sources consulted and how this collection differs.

This is an independent collection, with no claim of inclusion in or endorsement by the main Awesome index. That index's [current contribution rules](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) exclude AI-generated lists.

Original catalog content and scripts are dedicated under [CC0 1.0](LICENSE). Linked papers, software, data, and trademarks retain their respective terms.
