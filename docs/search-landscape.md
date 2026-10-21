# Search landscape and curation design

Checked on **22 October 2026**. This document records the initial comparison with existing lists and the benchmark search. It supports a living curated resource, not a claim that every relevant work has been found.

## What established awesome lists teach

The official [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) emphasizes selection and useful descriptions. Its [contribution guide](https://github.com/sindresorhus/awesome/blob/main/contributing.md) routes contributors through explicit guidelines. Adopt a concise scope, readable contents, consistent annotations, contribution criteria, and a clear license. Search broadly, then distinguish foundational work, strong current resources, and candidates needing verification.

The current [Awesome checklist](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) requires descriptive entries, consistent formatting, contribution guidance, a suitable content license, and a mature list; it also excludes AI-generated lists and pull requests. The [creation guide](https://github.com/sindresorhus/awesome/blob/main/create-list.md) asks maintainers to check for duplicates and wait at least 30 days before proposing inclusion. This AI-assisted repository adopts useful curation conventions but does **not** claim acceptance into, endorsement by, or compliance with every submission rule of the central Awesome index.

Six relevant lists were inspected directly. Observations describe their visible organization, not a comprehensive audit of their entries.

| Existing list | Useful pattern | Complementary emphasis here |
| --- | --- | --- |
| [Awesome-Agent-Scientists](https://github.com/AgenticScience/Awesome-Agent-Scientists) | Survey-linked taxonomy connects autonomous pipelines, research stages, and scientific domains. | Add a concise original explanation and an evidence boundary to each selected item. |
| [Awesome Science Agents](https://github.com/zoedsy/awesome-science-agents) | Bilingual timeline atlas, detailed reading guides, source provenance, review dates, evidence caveats, and generated-data validation. | Keep concise comparisons and bounded execution evidence directly readable in GitHub Markdown; its interactive and bilingual presentation is richer than ours. |
| [Awesome AI Scientists / Awesome AI Research](https://github.com/Research-Equality/awesome-ai-scientists) | Separates autonomous systems, infrastructure, workflow modules, and evaluation resources; explicitly tracks stage, loop, domain, and openness. | Retain these distinctions while explaining paper-to-system relationships and separating claims from measured evidence. |
| [Awesome AI4Sci](https://github.com/huang-sh/awesome-ai4sci) | Practical comparison tables expose interfaces, runtime strategies, and licenses; hosted services are separate from open implementations. | Make adoption details inspectable without equating repository availability with reproducibility or scientific validation. |
| [Awesome Research Agents](https://github.com/chrisliu298/awesome-research-agents) | A starter path and research-stage map connect literature, experiments, manuscript preparation, review, and project memory. | Offer multiple reading paths for researchers, system builders, and evaluators, without centering one coding-agent vendor. |
| [Awesome AI for Science](https://github.com/ai4s-research/awesome-ai-for-science) | Broad coverage includes scientific domains, paper-to-code, documentation, workbenches, datasets, and communities. | Keep the core scope on agents that participate in research; list general scientific ML only when it clarifies a specific co-scientist capability. |

## Implemented research contributions

Timelines, summaries, provenance, benchmark coverage, and automated validation are shared practices. The [Science Agents atlas documentation](https://github.com/zoedsy/awesome-science-agents/blob/main/docs/DASHBOARD.md) describes several of them explicitly. This collection's identity rests on the following connected research outputs, without claiming that their individual features are exclusive:

- A [capability-and-evidence matrix](capability-matrix.md) compares all 13 cataloged systems across seven dimensions, with primary sources and a stated evidence basis for every cell. It separates human roles, memory mechanisms, verification, code access, and evaluation settings rather than producing a universal score.
- Two [local reproducibility reports](reproducibility.md) record executed behavior from pinned public components, including independent checks, observed failures, configuration, cost accounting, and untested claims. They provide component-level evidence; end-to-end scientist performance remains untested here.
- A [cross-paper synthesis](research-synthesis.md) examines six recurring problems, explains tensions between study findings, and proposes concrete experiments to resolve uncertainty. Reported observations are distinguished from editorial interpretation.

The reports give this initial release original execution evidence. Their coverage is deliberately narrow, and the matrix and synthesis remain dependent on the scope and quality of the cited primary sources. Daily curation is a maintenance commitment whose sustained quality must be demonstrated over time.

## Recommended presentation

1. **A short front page.** State the scope, provide a contents list and a starting reading path, then link to full annotated catalogs. A visitor should quickly distinguish papers, runnable systems, tools, and evaluation resources.
2. **Annotations that answer three questions.** What does it do, why is it useful, and what was actually demonstrated? Use approximately 35–65 words per item, with direct paper and official-code links. Avoid copying abstracts or promotional claims.
3. **Stable records with multiple views.** Store identifiers, canonical URLs, dates, source provenance, tags, concise summaries, and verification dates once. Generate the catalogs deterministically, so daily curation cannot silently diverge across Markdown pages.
4. **Two complementary navigation axes.** Browse by artifact type and filter conceptually by research stage: literature, ideation, planning, execution, analysis, validation, and communication. Domain and autonomy tags should supplement these axes.
5. **Explicit evaluation boundaries.** Distinguish implementation, benchmark performance, reproducibility, expert assessment, and prospective experimental validation. A paper, a system release, and its benchmark can have separate records connected through links.
6. **A maintenance trail.** Keep a search log, contribution template, candidate queue, and dated changes. Record substantive updates and corrections, not daily timestamp-only commits or volatile star counts.

Suggested files are `README.md`, `CONTRIBUTING.md`, `LICENSE`, structured records under `data/`, generated catalogs under `docs/`, validation and rendering scripts under `scripts/`, and narrow repository checks under `.github/`. The exact names should follow the repository's implementation conventions.

## Initial benchmark search

The search covered primary papers on arXiv and conference proceedings; official author and organization repositories; linked project pages; and citation trails from the six lists above. Secondary aggregators were used only as discovery leads. Each accepted benchmark record links to an opened primary source. Peer-reviewed status requires a linked journal or proceedings record. Author-reported acceptance without a located venue record is retained as a note under a preprint label.

Search families included:

- `AI scientist benchmark`, `scientific agents evaluation`, `Scientist-Bench`, and `ScienceAgentBench`.
- `machine learning research engineering benchmark`, `MLAgentBench`, `MLE-bench`, `RE-Bench`, and `MLRC-Bench`.
- `paper replication agents`, `computational reproducibility benchmark`, `PaperBench`, `CORE-Bench`, and `SciReplicate-Bench`.
- `scientific coding benchmark`, `SciCode`, `scientific software computer-use`, and `ScienceBoard`.
- `research idea generation evaluation`, `novelty judgment benchmark`, `research forecasting`, `AI Idea Bench`, and date-focused 2026 searches.
- `biology research agent benchmark`, `bioinformatics analysis benchmark`, `LAB-Bench`, `BixBench`, and `FrontierScience`.

The initial set contains **18 benchmark records**. It covers coding and ML engineering; computational reproduction and replication; dataset-grounded discovery; biological analysis; scientific computer use; research ideation and novelty judgment; forecasting; and expert scientific reasoning. These measurements are complementary and should not be combined into a single implied ranking of scientific intelligence.

## Concrete coverage gaps and follow-ups

- **Version-aware evaluation.** The [CORE-Bench follow-up](https://arxiv.org/abs/2606.26158) introduces v1.1 and out-of-distribution tasks after studying shortcuts, efficiency, reliability, and human collaboration. [SciCode-Verified](https://arxiv.org/abs/2608.04975) audits benchmark defects. Keep version and evaluation-setting information when adding score comparisons; an early paper's headline score is not a current leaderboard.
- **Validity of idea evaluation.** [RINoBench](https://arxiv.org/abs/2603.10303) distinguishes plausible explanations from accurate novelty judgments. [IdeaForecastBench](https://arxiv.org/abs/2609.00747) distinguishes later realization from precise anticipation. Track human agreement, judge sensitivity, temporal leakage, feasibility, and execution separately.
- **Prospective science.** This benchmark set is concentrated on prepared digital tasks. Expand systematic coverage of wet-lab execution, materials experiments, causal interventions, negative results, and discoveries validated after an agent proposed them. Do not infer this evidence from an end-to-end workflow diagram.
- **Human partnership.** Add studies measuring scientist time, correction burden, hypothesis quality, reproducibility, and longitudinal benefit under explicit human-agent interaction protocols. Pure autonomy scores leave these outcomes unresolved.
- **Operational maturity.** Project documentation can verify supported interfaces and stated dependencies; it does not establish that installation or end-to-end workflows were tested here. Future hands-on evaluations should record environment, date, inputs, costs, and failures.
- **Search coverage.** Follow citation chains and domain-specific venues beyond general ML, especially chemistry, biology, medicine, materials, and social science. Maintain a candidate queue for ambiguous names, unavailable artifacts, and sources that cannot yet support an accurate summary.

Daily curation should revisit recent publication and release sources, deduplicate by canonical identifiers, check changed evidence, and record meaningful additions or corrections. A quiet day is a valid outcome; coverage should grow through verified contributions rather than a quota.
