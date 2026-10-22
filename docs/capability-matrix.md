# Capability and evidence matrix

[← Overview](../README.md) · [Research synthesis](research-synthesis.md) · [Local reproducibility reports](reproducibility.md)

**14 systems · Sources reviewed 2026-10-22.** Source-based comparison of the cataloged systems. Cells describe inspected public documentation or author-reported methods and evaluation, not independent execution or reproduction. Memory means explicit research state, not knowledge encoded in model weights. Not established means the examined source does not establish the capability; it does not prove absence.

Each cell cites a paper, project document, or inspected code section. Numbered sources and evidence notes appear below each system. The matrix does not assign an overall ranking.

Paper reports and static code inspection are distinct from independent execution. **Not established** indicates insufficient evidence in the examined sources, not absence of a capability. See [local reports](reproducibility.md) for executed checks.

Rows follow release dates, newest first; year-only records follow dated records within each year. Memory refers to stored research state. Verification distinguishes execution checks from scientific validation.

## Research workflow

| System | Human involvement | Hypothesis generation | Experiment execution | Memory |
| --- | --- | --- | --- | --- |
| [Agentic Scientist](#agentic-scientist-system)<br>2026-10-13 | Researchers define tasks and rubrics; the conference case included human result verification and manuscript editing. [1](#agentic-scientist-system-sources) | Ideation agents propose falsifiable hypotheses with implementation plans and explicit rubric targets. [1](#agentic-scientist-system-sources) | Coding agents run bounded experiments, followed by baselines, ablations, and separate final evaluation. [1,2](#agentic-scientist-system-sources) | Worker histories and distilled shared conclusions persist across research cycles; optional pruning archives earlier context. [1](#agentic-scientist-system-sources) |
| [ScientistTwo](#scientisttwo-system)<br>2026-09-17 | Starts from human-defined research problems and existing baselines; subsequent research cycles are described as autonomous. [1](#scientisttwo-system-sources) | Extracts baseline limitations, checks candidate novelty, and evolves ideas from successful and failed experiments. [1](#scientisttwo-system-sources) | Screens on subsets, escalates to full benchmarks, and adds ablation and rebuttal experiments. [1](#scientisttwo-system-sources) | Aggregates historical execution traces, including unsuccessful attempts, to guide subsequent idea evolution. [1](#scientisttwo-system-sources) |
| [ScienceBuddy](#sciencebuddy-system)<br>2026-09-15 | Researchers supply materials and steer workspace conversations; released training experiments instead use bounded simulated feedback. [1](#sciencebuddy-system-sources) | Supports evidence exploration and analysis refinement; autonomous novel-hypothesis quality is not established by the workspace demonstration. [1](#sciencebuddy-system-sources) | Workspace exposes tool execution; released RSI experiments alternate harness selection and task-model training. [1](#sciencebuddy-system-sources) | Retains task conversations, trajectories, and artifacts; harness revisions and model-weight updates are distinct mechanisms. [1](#sciencebuddy-system-sources) |
| [Eureka Machine](#recursive-eureka-machine-system)<br>2026-06-11 | Flint was developed by people and agents; earlier research included manual and AI-assisted inspection. [2,1](#recursive-eureka-machine-system-sources) | Proposes research ideas and combines promising directions across experiment branches. [1](#recursive-eureka-machine-system-sources) | Implements and tests training changes and GPU kernels; Flint extends the reported use to model development. [1,2](#recursive-eureka-machine-system-sources) | Retains useful context from earlier experiments across long-running parallel research threads. [1](#recursive-eureka-machine-system-sources) |
| [ScientistOne](#scientistone-system)<br>2026-05-25 | Seed papers and task-specific evaluators frame the automated investigation, solver search, and writing pipeline. [1](#scientistone-system-sources) | Ranks literature-grounded candidate approaches by novelty and feasibility before parallel exploration. [1](#scientistone-system-sources) | Solver branches submit executable candidates to task evaluators; selected solutions receive ablation experiments. [1](#scientistone-system-sources) | Preserves retrieved references, execution logs, evaluator scores, and evidence tags connecting pipeline stages. [1](#scientistone-system-sources) |
| [OpenResearch](#openresearch-system)<br>2026 | Researchers choose coding agents, projects, and compute; the workspace supports interactive or automated investigation. [1](#openresearch-system-sources) | Project documents literature-grounded hypothesis development using alphaXiv, bioRxiv, and PubMed integrations. [1](#openresearch-system-sources) | Documents local execution and remote backends including SSH, Slurm, Kubernetes, and managed compute. [1](#openresearch-system-sources) | A local SQL experiment database links logs, code, and artifacts for later agent and researcher inspection. [1](#openresearch-system-sources) |
| [Kosmos](#kosmos-system)<br>2025-11-04 | Scientists curate datasets and objectives, then interpret and critically assess resulting discoveries. [1](#kosmos-system-sources) | Iterates literature search, data analysis, and hypothesis generation around the supplied research objective. [1](#kosmos-system-sources) | Executes computational analyses on supplied datasets; physical experiment execution is not established as a system capability. [1](#kosmos-system-sources) | A structured world model consolidates agent outputs and guides later research cycles. [1](#kosmos-system-sources) |
| [AI Scientist v2](#ai-scientist-v2-system)<br>2025-04-10 | Researchers supply topics; the workshop study selected initial ideas and best completed manuscripts across multiple runs. [1](#ai-scientist-v2-system-sources) | Generates and refines ideas from a topic brief with literature-based novelty checking. [1,2](#ai-scientist-v2-system-sources) | Progressive tree search develops prototypes, tunes hyperparameters, executes research agendas, and runs ablations. [1](#ai-scientist-v2-system-sources) | Search nodes retain code and error information; stage checkpoints and selected nodes carry progress forward. [1](#ai-scientist-v2-system-sources) |
| [Google Co-Scientist](#google-co-scientist-system)<br>2025-02-19 | Scientists set objectives, constraints, and feedback; all three biomedical validation campaigns used expert involvement. [1,2](#google-co-scientist-system-sources) | Generates, critiques, ranks, and evolves hypotheses through multi-agent debate and tournaments. [1,2](#google-co-scientist-system-sources) | Proposes experimental protocols; collaborating researchers conduct the reported wet-lab validation. [2](#google-co-scientist-system-sources) | Persistent context memory stores agent/system state and tournament progress; feedback updates prompts rather than model weights. [1,2](#google-co-scientist-system-sources) |
| [Agent Laboratory](#agent-laboratory-system)<br>2025-01-08 | Humans supply the research idea; optional co-pilot checkpoints approve or redirect each subtask. [1](#agent-laboratory-system-sources) | Develops experiment plans around researcher-supplied ideas after literature review. [1](#agent-laboratory-system-sources) | Prepares datasets, iteratively writes and repairs Python experiments, and interprets outputs before report writing. [1](#agent-laboratory-system-sources) | Retains bounded code/error histories and paper summaries; documented checkpoints restore workflow state. [1,2](#agent-laboratory-system-sources) |
| [Biomni](#biomni-system)<br>2025 | Researchers issue biomedical requests and supply data; the agent plans tool use and executes generated analysis code. [1](#biomni-system-sources) | Documents hypothesis generation from analyses, including a single-cell annotation example. [1](#biomni-system-sources) | Runs code against a biomedical tool/software environment; this does not establish autonomous physical laboratory operation. [1](#biomni-system-sources) | Exposes conversation traces and retrieves curated know-how; adaptive memory across research projects is not established here. [1](#biomni-system-sources) |
| [Virtual Lab](#virtual-lab-system)<br>2025 | A human researcher sets meeting agendas and provides high-level feedback to specialist agents. [1,3](#virtual-lab-system-sources) | Team and individual discussions develop research approaches; the demonstrated campaign designed a nanobody pipeline. [1,3](#virtual-lab-system-sources) | Agents produced computational design workflows; the paper reports separate experimental testing of resulting nanobodies. [1,3](#virtual-lab-system-sources) | Meeting code accepts prior summaries and context, accumulates messages, and saves discussions as JSON and Markdown. [2](#virtual-lab-system-sources) |
| [AI Scientist v1](#ai-scientist-system)<br>2024 | Humans provide executable starting templates, baseline experiments, and the research domain. [1,2](#ai-scientist-system-sources) | Proposes template-conditioned ideas and filters similarity through literature search. [1](#ai-scientist-system-sources) | Edits template code, runs computational experiments, repairs failures, and produces plots and manuscripts. [1](#ai-scientist-system-sources) | Maintains an idea archive and experimental notes; reported parallel experiments omitted waiting for review feedback before new ideation. [1](#ai-scientist-system-sources) |
| [Coscientist](#coscientist-system)<br>2023 | Users specify tasks and supply hardware/materials; the integrated chemistry experiment still required manual plate movement. [1](#coscientist-system-sources) | Plans syntheses and selects reaction conditions; unrestricted novel-hypothesis discovery is not established by these tasks. [1](#coscientist-system-sources) | Uses code execution and laboratory APIs, demonstrated with Opentrons and Emerald Cloud Lab. [1](#coscientist-system-sources) | Planner receives tool outputs as conversational messages; durable research memory across independent runs is not established. [1](#coscientist-system-sources) |

## Evidence and access

| System | Verification | Available code | Evaluation setting |
| --- | --- | --- | --- |
| [Agentic Scientist](#agentic-scientist-system)<br>2026-10-13 | Evaluator checks, rubric gates, evidence maps, and model audits; human audits still found evaluation-protocol violations. [1](#agentic-scientist-system-sources) | Public orchestration implementation, example evaluators, presets, and run-inspection interface. [2](#agentic-scientist-system-sources) | Author-run computational task and model comparisons, plus a separately human-supervised ALIFE research case. [1](#agentic-scientist-system-sources) |
| [ScientistTwo](#scientisttwo-system)<br>2026-09-17 | Combines experimental comparisons, artifact integrity audits, and simulated peer review; the paper also reports human manuscript evaluation. [1,2](#scientisttwo-system-sources) | Generated research artifacts are presented; a release of the complete orchestration framework is not established by the project page. [2](#scientisttwo-system-sources) | 107 publication-derived AI problems; automated reviewers and a human study of 33 papers by nine reviewers. [1](#scientisttwo-system-sources) |
| [ScienceBuddy](#sciencebuddy-system)<br>2026-09-15 | Users inspect tool records; the simplified experiment uses verifier-assisted feedback and fixed validation-task selection. [1](#sciencebuddy-system-sources) | Simple-SciBuddy experiment source is public; hosted frontend, accounts, and product API source are excluded. [1](#sciencebuddy-system-sources) | Frozen train/validation/test tasks with sequential harness/RL stages; separate recorded biomedical workspace demonstrations. [1](#sciencebuddy-system-sources) |
| [Eureka Machine](#recursive-eureka-machine-system)<br>2026-06-11 | Checks reward hacking and variance; human feedback helped improve detectors. These are creator-reported safeguards. [1](#recursive-eureka-machine-system-sources) | Selected training scripts and kernels are public outputs; complete Eureka Machine framework source is not established. [3](#recursive-eureka-machine-system-sources) | NanoChat Autoresearch, NanoGPT Speedrun, and SOL-ExecBench; later Flint development is a separate product case. [3,2](#recursive-eureka-machine-system-sources) |
| [ScientistOne](#scientistone-system)<br>2026-05-25 | Claim verification plus author-run audits of scores, specification compliance, references, and method–code agreement. [1](#scientistone-system-sources) | Generated papers and solver code are public; full framework source availability is not established by the project page. [2](#scientistone-system-sources) | ADRS systems tasks, selected MLE-Bench tasks, and Parameter Golf; author-conducted integrity and automated-review evaluations. [1](#scientistone-system-sources) |
| [OpenResearch](#openresearch-system)<br>2026 | Inspectability is documented; an independent scientific-validity verification protocol is not established by the README. [1](#openresearch-system-sources) | Public workspace and harness source, desktop releases, and standalone CLI. [1](#openresearch-system-sources) | A controlled discovery evaluation is not established by the examined README; it describes product workflows. [1](#openresearch-system-sources) |
| [Kosmos](#kosmos-system)<br>2025-11-04 | Reports link claims to papers or notebooks; authors report expert checks of sampled statements and corroboration of case-study findings. [1](#kosmos-system-sources) | Hosted access is documented; a complete public framework source release is not established by the examined announcement. [2](#kosmos-system-sources) | Seven discovery case studies across data-rich fields; statement accuracy assessed on 102 statements from three reports. [1](#kosmos-system-sources) |
| [AI Scientist v2](#ai-scientist-v2-system)<br>2025-04-10 | Repeated runs, ablations, model-based experiment assessment, and visual review; selected manuscripts also received external workshop reviews. [1](#ai-scientist-v2-system-sources) | Public tree-search workflow, configuration, ideation, and manuscript-generation source. [2](#ai-scientist-v2-system-sources) | Machine-learning experiments and three human-selected workshop submissions; one exceeded the reported acceptance threshold. [1](#ai-scientist-v2-system-sources) |
| [Google Co-Scientist](#google-co-scientist-system)<br>2025-02-19 | Combines model tournaments, expert assessment, and specific biomedical experiments; model ranking alone is not empirical validation. [1,2](#google-co-scientist-system-sources) | Nature explicitly states full source is unavailable; pseudocode, prompts, and experimental access are provided. [1,3](#google-co-scientist-system-sources) | Biomedical case studies in drug repurposing, liver fibrosis, and antimicrobial resistance, with automated and human hypothesis assessment. [1,2](#google-co-scientist-system-sources) |
| [Agent Laboratory](#agent-laboratory-system)<br>2025-01-08 | Execution feedback and simulated reviewer refinement; authors separately collect human ratings of generated research. [1](#agent-laboratory-system-sources) | Public multi-agent workflow, solvers, and configurations under MIT licensing. [2](#agent-laboratory-system-sources) | Five selected research questions, co-pilot studies, and separate mle-solver evaluation on MLE-Bench. [1](#agent-laboratory-system-sources) |
| [Biomni](#biomni-system)<br>2025 | Provides trace inspection and a task-scoring benchmark interface; a universal scientific-claim verifier is not established. [1](#biomni-system-sources) | Public agent and environment source; the README distinguishes the frozen release from the hosted platform. [1](#biomni-system-sources) | README documents Biomni-Eval1 with 433 instances across ten biological reasoning tasks, plus usage examples. [1](#biomni-system-sources) |
| [Virtual Lab](#virtual-lab-system)<br>2025 | Reported wet-lab binding measurements complement computational design scores; released discussions and experimental data permit inspection. [3](#virtual-lab-system-sources) | Public agent-meeting implementation and nanobody-design notebooks, discussions, and computational results. [1,3](#virtual-lab-system-sources) | A SARS-CoV-2 nanobody-design campaign with 92 designed candidates and experimental binding evaluation. [3](#virtual-lab-system-sources) |
| [AI Scientist v1](#ai-scientist-system)<br>2024 | Uses execution feedback, literature novelty checks, and an LLM reviewer; reviewer ratings do not establish claim correctness. [1](#ai-scientist-system-sources) | Public pipeline, templates, and example outputs; external model and compute dependencies remain. [2](#ai-scientist-system-sources) | Author-run diffusion, language-modeling, and grokking experiments with automated manuscript assessment. [1](#ai-scientist-system-sources) |
| [Coscientist](#coscientist-system)<br>2023 | Reports measured reaction products, lookup-table yield optimization, and cloud-lab quality-control failures. [1](#coscientist-system-sources) | Supporting data and simplified implementation are public; Apache 2.0 with Commons Clause restricts commercial use. [2](#coscientist-system-sources) | Six chemistry and automation tasks, including physical synthesis and optimization over previously measured reaction datasets. [1](#coscientist-system-sources) |

## Evidence notes

<a id="agentic-scientist-system"></a>

### Agentic Scientist

[Catalog entry](systems.md#agentic-scientist-system) · Source check: 2026-10-22.

Rubrics protect only stated constraints. A conference acceptance with human verification and edits does not measure acceptance of unaltered autonomous outputs.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2610.18933v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2610.18933v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2610.18933v1) · [2](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/README.md) |
| Memory | Paper report | [1](https://arxiv.org/html/2610.18933v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2610.18933v1) |
| Available code | Project documentation | [2](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/README.md) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2610.18933v1) |

<a id="agentic-scientist-system-sources"></a>

1. [Agentic Scientist paper, v1](https://arxiv.org/html/2610.18933v1) — Sections 3.1–3.5, 4.1–4.3, 5, and 6.3 (Rubric-specification sensitivity).
2. [Repository README at df8313889a00](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/README.md) — Quickstart; What you get; How it works; Resume a run or run only some phases.

<a id="scientisttwo-system"></a>

### ScientistTwo

[Catalog entry](systems.md#scientisttwo-system) · Source check: 2026-10-22.

Automated acceptance is a reviewer-model outcome. ScholarPeer also guides refinement; the held-out reviewer and human study broaden evidence without proving unrestricted research autonomy.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2609.19644v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2609.19644v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2609.19644v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2609.19644v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2609.19644v1) · [2](https://scientist-two.github.io/) |
| Available code | Not established | [2](https://scientist-two.github.io/) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2609.19644v1) |

<a id="scientisttwo-system-sources"></a>

1. [ScientistTwo paper, v1](https://arxiv.org/html/2609.19644v1) — Sections 3.1–3.6, 4 Common Setup, and 4.3 (Human Evaluation; Table 10).
2. [ScientistTwo project](https://scientist-two.github.io/) — Read What ScientistTwo Wrote; A Closed Loop from Idea to Accepted Paper; Every Claim Backed by Its Artifacts.

<a id="sciencebuddy-system"></a>

### ScienceBuddy

[Catalog entry](systems.md#sciencebuddy-system) · Source check: 2026-10-22.

Released experiment evidence does not establish continual improvement of the hosted product during researcher use. Simulation and human collaboration are separate settings.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Hypothesis generation | Not established | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Experiment execution | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Memory | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Verification | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Available code | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |
| Evaluation setting | Project documentation | [1](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) |

<a id="sciencebuddy-system-sources"></a>

1. [Repository README at 53177995fd54](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/README.md) — ScienceBuddy: work with your scientific material; Use the workspace; Double-recursive RSI; Experiment code in this repository.

<a id="recursive-eureka-machine-system"></a>

### Eureka Machine

[Catalog entry](systems.md#recursive-eureka-machine-system) · Source check: 2026-10-22.

Released outputs and creator-run benchmarks do not isolate the automated system’s causal contribution, total human effort, or full search cost. Inspectable artifacts are not a complete research-loop release.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Project documentation | [2](https://recursive.com/updates/introducing-recursive-flint) · [1](https://recursive.com/updates/first-steps-toward-automated-ai-research) |
| Hypothesis generation | Project documentation | [1](https://recursive.com/updates/first-steps-toward-automated-ai-research) |
| Experiment execution | Project documentation | [1](https://recursive.com/updates/first-steps-toward-automated-ai-research) · [2](https://recursive.com/updates/introducing-recursive-flint) |
| Memory | Project documentation | [1](https://recursive.com/updates/first-steps-toward-automated-ai-research) |
| Verification | Project documentation | [1](https://recursive.com/updates/first-steps-toward-automated-ai-research) |
| Available code | Not established | [3](https://github.com/recursive-org/first-steps-toward-automated-ai-research) |
| Evaluation setting | Project documentation | [3](https://github.com/recursive-org/first-steps-toward-automated-ai-research) · [2](https://recursive.com/updates/introducing-recursive-flint) |

<a id="recursive-eureka-machine-system-sources"></a>

1. [First Steps Toward Automated AI Research](https://recursive.com/updates/first-steps-toward-automated-ai-research) — Research loop, benchmark experiments, reward-hacking checks, and limitations.
2. [Introducing Flint](https://recursive.com/updates/introducing-recursive-flint) — A four-month experiment in automated research; architecture, quantization, and inference sections.
3. [Released research outcomes repository](https://github.com/recursive-org/first-steps-toward-automated-ai-research) — README: nanoGPT_speedrun, SOL-ExecBench, and nanochat_autoresearch artifact descriptions.

<a id="scientistone-system"></a>

### ScientistOne

[Catalog entry](systems.md#scientistone-system) · Source check: 2026-10-22.

Auditability is narrower than scientific truth or novelty. The authors flag artifact-interface incompatibility in some baseline audit comparisons, limiting direct rankings.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2605.26340v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2605.26340v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2605.26340v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2605.26340v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2605.26340v1) |
| Available code | Not established | [2](https://scientist-one.github.io/) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2605.26340v1) |

<a id="scientistone-system-sources"></a>

1. [ScientistOne paper, v1](https://arxiv.org/html/2605.26340v1) — Sections 4.1–4.3, 5, 6, 7, and 9.
2. [ScientistOne project](https://scientist-one.github.io/) — Generated Papers & Code; System Overview; CoE Audit; integrity-comparison footnote.

<a id="openresearch-system"></a>

### OpenResearch

[Catalog entry](systems.md#openresearch-system) · Source check: 2026-10-22.

This comparison captures documented product capabilities. No scientific discovery benchmark or general reliability estimate is established by the examined source.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Project documentation | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Hypothesis generation | Project documentation | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Experiment execution | Project documentation | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Memory | Project documentation | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Verification | Not established | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Available code | Project documentation | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |
| Evaluation setting | Not established | [1](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) |

<a id="openresearch-system-sources"></a>

1. [Repository README at a3a640ca068b](https://github.com/alphaXiv/OpenResearch/blob/a3a640ca068b8f371f2f9bce26da5530f2f2aebf/README.md) — Introduction; Get started; How it works.

<a id="kosmos-system"></a>

### Kosmos

[Catalog entry](systems.md#kosmos-system) · Source check: 2026-10-22.

Productivity equivalents rely on assumptions and user estimates. Traceable reports can still contain unsupported interpretations; sampled accuracy is not a universal reliability rate.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2511.02824v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2511.02824v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2511.02824v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2511.02824v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2511.02824v1) |
| Available code | Not established | [2](https://edisonscientific.com/news/announcing-kosmos) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2511.02824v1) |

<a id="kosmos-system-sources"></a>

1. [Kosmos paper, v1](https://arxiv.org/html/2511.02824v1) — Sections 2.1, 2.2–2.5, 3.1–3.2, and 4.1.1.
2. [Official Kosmos announcement](https://edisonscientific.com/news/announcing-kosmos) — Kosmos; The discoveries.

<a id="ai-scientist-v2-system"></a>

### AI Scientist v2

[Catalog entry](systems.md#ai-scientist-v2-system) · Source check: 2026-10-22.

The workshop experiment asked whether any selected output could pass review; it did not estimate the success rate of arbitrary autonomous runs.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2504.08066v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2504.08066v1) · [2](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/README.md) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2504.08066v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2504.08066v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2504.08066v1) |
| Available code | Project documentation | [2](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/README.md) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2504.08066v1) |

<a id="ai-scientist-v2-system-sources"></a>

1. [AI Scientist-v2 paper, v1](https://arxiv.org/html/2504.08066v1) — Sections 3.1–3.4 and 4.2 (idea and manuscript selection).
2. [Repository README at 96bd51617cfd](https://github.com/SakanaAI/AI-Scientist-v2/blob/96bd51617cfdbb494a9fc283af00fe090edfae48/README.md) — Generate Research Ideas; Run AI Scientist-v2 Paper Generation Experiments; Frequently Asked Questions.

<a id="google-co-scientist-system"></a>

### Google Co-Scientist

[Catalog entry](systems.md#google-co-scientist-system) · Source check: 2026-10-22.

Evidence is concentrated in selected biomedical investigations. Empirical validation of particular hypotheses does not establish clinical utility or broad discovery reliability.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [2](https://arxiv.org/html/2502.18864v1) |
| Hypothesis generation | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [2](https://arxiv.org/html/2502.18864v1) |
| Experiment execution | Paper report | [2](https://arxiv.org/html/2502.18864v1) |
| Memory | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [2](https://arxiv.org/html/2502.18864v1) |
| Verification | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [2](https://arxiv.org/html/2502.18864v1) |
| Available code | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [3](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/) |
| Evaluation setting | Paper report | [1](https://www.nature.com/articles/s41586-026-10644-y) · [2](https://arxiv.org/html/2502.18864v1) |

<a id="google-co-scientist-system-sources"></a>

1. [Co-Scientist Nature paper](https://www.nature.com/articles/s41586-026-10644-y) — Co-Scientist overview; System analysis and evaluation; Methods: context memory; Code availability.
2. [Original co-scientist paper, v1](https://arxiv.org/html/2502.18864v1) — Sections 3.1–3.5, 4.5–4.7, and 5.
3. [Official access announcement](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/) — Developing agentic tools with the scientific community.

<a id="agent-laboratory-system"></a>

### Agent Laboratory

[Catalog entry](systems.md#agent-laboratory-system) · Source check: 2026-10-22.

Human ratings, autonomous experiments, and an isolated solver benchmark measure different capabilities; co-pilot results include researcher intervention.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2501.04227v1) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2501.04227v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2501.04227v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2501.04227v1) · [2](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md) |
| Verification | Paper report | [1](https://arxiv.org/html/2501.04227v1) |
| Available code | Project documentation | [2](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2501.04227v1) |

<a id="agent-laboratory-system-sources"></a>

1. [Agent Laboratory paper, v1](https://arxiv.org/html/2501.04227v1) — Sections 3.2, 3.3.1, 4.1–4.4, and Appendix A.1.
2. [Repository README at d9017d90e329](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md) — Overview; Co-Pilot mode; Tip 3: load previous saves from checkpoints; License.

<a id="biomni-system"></a>

### Biomni

[Catalog entry](systems.md#biomni-system) · Source check: 2026-10-22.

This row describes the inspected public implementation and documented evaluation interface, not an independent biomedical validation. Hosted and released versions can differ.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Hypothesis generation | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Experiment execution | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Memory | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Verification | Not established | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Available code | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |
| Evaluation setting | Project documentation | [1](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) |

<a id="biomni-system-sources"></a>

1. [Repository README at 400c1f366b96](https://github.com/snap-stanford/Biomni/blob/400c1f366b96a35ca253e13c9b06c5076af41d65/README.md) — Overview; Basic Usage; PDF Generation; Biomni-Eval1; Know-How Library; Important Note.

<a id="virtual-lab-system"></a>

### Virtual Lab

[Catalog entry](systems.md#virtual-lab-system) · Source check: 2026-10-22.

The evidence concerns one human-guided biological campaign. Source inspection and paper-reported experimental validation do not establish general autonomous laboratory capability.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/README.md) · [3](https://www.nature.com/articles/s41586-025-09442-9) |
| Hypothesis generation | Paper report | [1](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/README.md) · [3](https://www.nature.com/articles/s41586-025-09442-9) |
| Experiment execution | Paper report | [1](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/README.md) · [3](https://www.nature.com/articles/s41586-025-09442-9) |
| Memory | Code inspection | [2](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/src/virtual_lab/run_meeting.py) |
| Verification | Paper report | [3](https://www.nature.com/articles/s41586-025-09442-9) |
| Available code | Project documentation | [1](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/README.md) · [3](https://www.nature.com/articles/s41586-025-09442-9) |
| Evaluation setting | Paper report | [3](https://www.nature.com/articles/s41586-025-09442-9) |

<a id="virtual-lab-system-sources"></a>

1. [Repository README at 8a3a4fd9ccc0](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/README.md) — Virtual Lab; Virtual Lab for nanobody design.
2. [Meeting implementation at 8a3a4fd9ccc0](https://github.com/zou-group/virtual-lab/blob/8a3a4fd9ccc0cd297bd523751e03bc9527c91832/src/virtual_lab/run_meeting.py) — run_meeting: summaries/contexts arguments, message accumulation, save_meeting, and return_summary.
3. [Virtual Lab Nature paper](https://www.nature.com/articles/s41586-025-09442-9) — Abstract; Data availability; Code availability; Figure 4 caption.

<a id="ai-scientist-system"></a>

### AI Scientist v1

[Catalog entry](systems.md#ai-scientist-system) · Source check: 2026-10-22.

The study tests small computational templates. Proposed open-ended improvement and automated review thresholds should not be treated as independently demonstrated scientific discovery or venue acceptance.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://arxiv.org/html/2408.06292v1) · [2](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md) |
| Hypothesis generation | Paper report | [1](https://arxiv.org/html/2408.06292v1) |
| Experiment execution | Paper report | [1](https://arxiv.org/html/2408.06292v1) |
| Memory | Paper report | [1](https://arxiv.org/html/2408.06292v1) |
| Verification | Paper report | [1](https://arxiv.org/html/2408.06292v1) |
| Available code | Project documentation | [2](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md) |
| Evaluation setting | Paper report | [1](https://arxiv.org/html/2408.06292v1) |

<a id="ai-scientist-system-sources"></a>

1. [AI Scientist paper, v1](https://arxiv.org/html/2408.06292v1) — Sections 3, 4, 6, and 8; Section 6 archive-feedback implementation departure.
2. [Repository README at 1de1dbc1f4ee](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md) — Introduction; Setting Up the Templates; Run AI Scientist Paper Generation Experiments.

<a id="coscientist-system"></a>

### Coscientist

[Catalog entry](systems.md#coscientist-system) · Source check: 2026-10-22.

Successful configured chemistry tasks do not establish unrestricted chemistry research. The public simplified implementation is not a complete release of the original experimental system.

| Dimension | Evidence basis | Sources |
| --- | --- | --- |
| Human involvement | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |
| Hypothesis generation | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |
| Experiment execution | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |
| Memory | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |
| Verification | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |
| Available code | Project documentation | [2](https://github.com/gomesgroup/coscientist/blob/417e82b85743f88719ba7cf8838220fcb872e2ae/README.md) |
| Evaluation setting | Paper report | [1](https://www.nature.com/articles/s41586-023-06792-0) |

<a id="coscientist-system-sources"></a>

1. [Coscientist Nature paper](https://www.nature.com/articles/s41586-023-06792-0) — Main; Coscientist system architecture; Documentation search module; Integrated chemical experiment design; Chemical reasoning capabilities.
2. [Repository README at 417e82b85743](https://github.com/gomesgroup/coscientist/blob/417e82b85743f88719ba7cf8838220fcb872e2ae/README.md) — Supporting information; Directories; License.
