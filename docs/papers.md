# Papers

[← Overview](../README.md) · [Search coverage](search-protocol.md)

39 annotated records, ordered **newest first by publication/release date**, grouped by year. Entries with only a known year appear separately after the dated entries for that year; their position within the year is unknown. Same-date ties are ordered by name. Source status describes publication provenance. Catalog inclusion does not imply end-to-end replication; [local reproducibility reports](reproducibility.md) document the exact scope of selected execution checks.

## Contents

- [2026](#year-2026)
- [2025](#year-2025)
- [2024](#year-2024)
- [2023](#year-2023)
- [2009](#year-2009)
- [Browse by topic](#browse-by-topic)

<a id="year-2026"></a>

## 2026

<a id="agentic-scientist"></a>

### [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933)

**2026-10-13 · preprint** · End-to-end research · orchestration, computational-science, verification

Coordinates coding agents through task drafting, ideas, sandboxed experiments, baselines, ablations, analysis, and manuscript writing. A meta-controller enforces stage-specific rubrics. The paper reports computational discovery studies and an ALIFE 2026 paper produced in a co-scientist setting; that human collaboration should be distinguished from its separate autonomous evaluations.

Related entries: [Agentic Scientist](systems.md#agentic-scientist-system).

Sources: [1](https://arxiv.org/abs/2610.18933) · Content checked: 2026-10-22.

<a id="runtime-agent-coordination"></a>

### [Can AI Scientists Coordinate at Runtime?](https://arxiv.org/abs/2610.00980) · [Code](https://github.com/systemind-team/Runtime-AI-Scientist)

**2026-10-01 · preprint** · End-to-end research · orchestration, verification, coordination

Adds runtime agent selection, scoped work contracts, and artifact-based verification to existing scientist frameworks. A single-seed exploratory study compares cumulative coordination variants under host-calibrated budgets. Runtime selection gives the strongest observed means, while additional contracts and verification can reduce scores, exposing tradeoffs that larger replicated evaluations should investigate.

Sources: [1](https://arxiv.org/abs/2610.00980) · Content checked: 2026-10-22.

<a id="denario"></a>

### [Denario Project: Deep Knowledge Artificial Intelligence Agents for Scientific Discovery](https://journals.aps.org/prxintelligence/abstract/10.1103/kk55-gc95) · [Code](https://github.com/Denario-AI/Denario)

**2026-10-01 · peer-reviewed** · End-to-end research · modular-workflow, cross-domain, human-evaluation

Provides modular agents for ideation, literature checking, planning, code execution, plotting, writing, and reviewing, using Cmbagent for analysis. Demonstrations span multiple scientific disciplines and include domain-expert reviews of generated drafts. The authors position it as a research assistant, with case-study quality and limitations requiring inspection of each output.

Sources: [1](https://arxiv.org/abs/2510.26887) · [2](https://journals.aps.org/prxintelligence/abstract/10.1103/kk55-gc95) · Content checked: 2026-10-22.

<a id="scientist-two"></a>

### [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644)

**2026-09-17 · preprint** · End-to-end research · multi-agent, ablations, machine-learning

Starts from a research problem, establishes baselines, proposes hypotheses, runs experiments and ablations, and iterates through simulated reviews. Evaluation includes publication-derived machine-learning tasks, integrity audits, automated reviewers, and a human study of generated papers. These complementary author-reported assessments remain bounded by the selected tasks; simulated acceptance is distinct from actual venue acceptance.

Related entries: [ScientistTwo](systems.md#scientisttwo-system).

Sources: [1](https://arxiv.org/abs/2609.19644) · Content checked: 2026-10-22.

<a id="sciencebuddy"></a>

### [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523)

**2026-09-15 · preprint** · End-to-end research · human-ai-collaboration, self-improvement, reinforcement-learning

Turns researcher requests, feedback, and execution traces into learning tasks and evaluation rubrics. An inner loop adapts the agent harness while an outer loop trains the model under the improved harness. Case studies cover four scientific task families; they demonstrate the proposed learning workflow rather than universal autonomous discovery.

Related entries: [ScienceBuddy](systems.md#sciencebuddy-system).

Sources: [1](https://arxiv.org/abs/2609.17523) · Content checked: 2026-10-22.

<a id="scientist-one"></a>

### [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](https://arxiv.org/abs/2605.26340)

**2026-05-25 · preprint** · End-to-end research · provenance, verification, machine-learning

Maintains explicit evidence chains from literature and experiments to manuscript claims, with audits for score reproduction, specification violations, references, and method-code agreement. The authors compare generated papers across research tasks and report improved integrity. These are task-specific audits, so the title's human-level claim should not be generalized to all research.

Related entries: [ScientistOne](systems.md#scientistone-system).

Sources: [1](https://arxiv.org/abs/2605.26340) · Content checked: 2026-10-22.

<a id="google-co-scientist"></a>

### [Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)

**2026-05-19 · peer-reviewed** · Hypothesis and idea generation · hypothesis-ranking, biomedicine, human-ai-collaboration

Uses specialized agents to generate, criticize, rank, and evolve hypotheses through tournaments, with scientists setting goals and steering exploration. The Nature paper includes biomedical applications and laboratory validation of selected hypotheses. The system supports scientific reasoning; experimental validation remains a distinct process rather than an automatically closed physical loop.

Related entries: [Google Co-Scientist](systems.md#google-co-scientist-system).

Sources: [1](https://www.nature.com/articles/s41586-026-10644-y) · Content checked: 2026-10-22.

<a id="empirical-research-assistance"></a>

### [Empirical Research Assistance: An AI system to help scientists write expert-level empirical software](https://www.nature.com/articles/s41586-026-10658-6)

**2026-05-19 · peer-reviewed** · Experimentation and implementation · tree-search, scientific-software, executable-evaluation

Uses language-model code mutations and tree search to improve a specified empirical quality metric, incorporating research ideas from external sources. The Nature paper evaluates diverse scientific software tasks, including bioinformatics and forecasting. Its strength is experimentally scored implementation search; results depend on the supplied objectives, evaluation data, and task design.

Sources: [1](https://www.nature.com/articles/s41586-026-10658-6) · Content checked: 2026-10-22.

<a id="robin"></a>

### [Robin: A multi-agent system for automating scientific discovery](https://www.nature.com/articles/s41586-026-10652-y) · [Code](https://github.com/Future-House/robin)

**2026-05-19 · peer-reviewed** · Domain science and laboratories · biomedicine, lab-in-the-loop, hypothesis

Combines literature agents and data-analysis agents in an iterative hypothesis, experiment, and interpretation cycle. The Nature study reports in-vitro evidence for candidate interventions affecting retinal-cell phagocytosis. Human researchers perform the physical experiments, and these preclinical findings do not establish treatment effectiveness in patients.

Sources: [1](https://www.nature.com/articles/s41586-026-10652-y) · [2](https://arxiv.org/abs/2505.13400) · Content checked: 2026-10-22.

<a id="ai-scientist-nature"></a>

### [Towards end-to-end automation of AI research](https://www.nature.com/articles/s41586-026-10265-5)

**2026-03-25 · peer-reviewed** · End-to-end research · machine-learning, research-lifecycle, automated-review

Integrates the AI Scientist lineage into a journal study of template-based and template-free research workflows, including idea generation, experiments, writing, and reviewing. A generated manuscript passed an initial workshop review round. This peer-reviewed system paper should be distinguished from the separate question of whether generated findings are independently replicated.

Related entries: [The AI Scientist](systems.md#ai-scientist-system), [The AI Scientist-v2](systems.md#ai-scientist-v2-system).

Sources: [1](https://www.nature.com/articles/s41586-026-10265-5) · Content checked: 2026-10-22.

<a id="evoscientist"></a>

### [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://arxiv.org/abs/2603.08127) · [Code](https://github.com/EvoScientist/EvoScientist)

**2026-03-09 · preprint** · End-to-end research · persistent-memory, self-improvement, multi-agent

Separates research, engineering, and evolution-management roles, storing both ideation history and experiment lessons in persistent memory. The October 2026 revision reports gains in idea assessment and code-execution success. These evaluations support reuse of research experience, while broader discovery quality still requires inspection beyond successful code execution.

Sources: [1](https://arxiv.org/abs/2603.08127) · Content checked: 2026-10-22.

<a id="moose-star"></a>

### [MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier](https://arxiv.org/abs/2603.03756)

**2026-03-04 · peer-reviewed** · Hypothesis and idea generation · training, hierarchical-search, hypothesis

Trains hypothesis generation through decomposed discovery subtasks, motivation-guided hierarchical retrieval, and bounded composition. It releases TOMATO-Star and studies scaling with training data and inference budget. The claimed complexity reduction depends on the paper's assumptions and best-case analysis; benchmark scaling is distinct from prospective experimental validation.

Sources: [1](https://arxiv.org/abs/2603.03756) · [2](https://proceedings.mlr.press/v306/yang26d.html) · Content checked: 2026-10-22.

### Year-only dates

Month and day have not been established.

<a id="verification-gap-survey"></a>

#### [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](https://arxiv.org/abs/2608.05179)

**2026 · preprint** · Surveys and perspectives · verification, reproducibility, evaluation

Examines computational research agents through autonomy, evaluation, released artifacts, human intervention, novelty checks, and result-selection disclosure. Its coded corpus distinguishes runnable code from evidence that supports scientific claims. The conclusions are bounded by the screened AI/ML systems and coding rules, rather than a census of all scientific domains.

Sources: [1](https://arxiv.org/abs/2608.05179) · Content checked: 2026-10-22.

<a id="year-2025"></a>

## 2025

<a id="kosmos"></a>

### [Kosmos: An AI Scientist for Autonomous Discovery](https://arxiv.org/abs/2511.02824)

**2025-11-04 · preprint** · End-to-end research · world-model, data-analysis, literature

Uses a structured world model to coordinate repeated literature search and data-analysis trajectories from an objective and dataset. Reports link claims to code or literature, and the paper presents seven discovery case studies with external scientist assessments. Human-equivalent time estimates are collaborator judgments rather than controlled productivity measurements.

Related entries: [Kosmos](systems.md#kosmos-system).

Sources: [1](https://arxiv.org/abs/2511.02824) · Content checked: 2026-10-22.

<a id="ai-scientists-survey"></a>

### [A Survey of AI Scientists](https://arxiv.org/abs/2510.23045)

**2025-10-27 · preprint** · Surveys and perspectives · taxonomy, research-lifecycle, governance

Synthesizes AI-scientist systems through six stages covering literature, ideas, preparation, execution, writing, and paper generation. The revised survey traces the shift from individual components to integrated workflows and discusses robustness and governance. Its stage-based organization is useful for comparing coverage, but does not make unlike evaluation settings directly comparable.

Sources: [1](https://arxiv.org/abs/2510.23045) · Content checked: 2026-10-22.

<a id="agentic-science-survey"></a>

### [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](https://arxiv.org/abs/2508.14111)

**2025-08-18 · preprint** · Surveys and perspectives · taxonomy, cross-domain, autonomy

Organizes agentic science across life sciences, chemistry, materials, and physics, connecting capability, workflow, and domain perspectives. It provides a useful map of hypothesis generation, experimentation, analysis, and refinement. As a survey, its taxonomy helps navigate reported systems rather than independently reproducing their discovery or autonomy claims.

Sources: [1](https://arxiv.org/abs/2508.14111) · Content checked: 2026-10-22.

<a id="virtual-lab"></a>

### [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9) · [Code](https://github.com/zou-group/virtual-lab)

**2025-07-29 · peer-reviewed** · Domain science and laboratories · biology, human-ai-collaboration, wet-lab-validation

Organizes a principal-investigator agent and scientific specialists into meetings with high-level human guidance. The agents develop a computational nanobody-design workflow, with selected designs tested experimentally. This demonstrates a specific human-AI research collaboration; human laboratory work and biological validation are central parts of the evidence.

Related entries: [Virtual Lab](systems.md#virtual-lab-system).

Sources: [1](https://www.nature.com/articles/s41586-025-09442-9) · [2](https://github.com/zou-group/virtual-lab) · Content checked: 2026-10-22.

<a id="ideation-execution-gap"></a>

### [The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas](https://arxiv.org/abs/2506.20803)

**2025-06-25 · preprint** · Hypothesis and idea generation · human-evaluation, ideation, experimental-validation

Recruits researchers to execute randomly assigned human- or model-generated ideas and obtains blinded reviews of the resulting projects. The apparent advantage of AI ideas at the ideation stage declines after implementation. This follow-up study shows why proposal ratings are insufficient proxies for completed research quality in its NLP setting.

Sources: [1](https://arxiv.org/abs/2506.20803) · Content checked: 2026-10-22.

<a id="alphaevolve"></a>

### [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)

**2025-06-16 · preprint** · Domain science and laboratories · evolutionary-search, mathematics, code-optimization

Evolves candidate programs using language-model edits and feedback from executable evaluators. Applications include mathematical constructions, algorithm discovery, and infrastructure optimization. The white paper illustrates breadth when a reliable scoring procedure exists; reported improvements are tied to those tasks and do not imply autonomous formulation of every scientific objective.

Sources: [1](https://arxiv.org/abs/2506.13131) · Content checked: 2026-10-22.

<a id="biomni"></a>

### [Biomni: A General-Purpose Biomedical AI Agent](https://doi.org/10.1101/2025.05.30.656746) · [Code](https://github.com/snap-stanford/Biomni)

**2025-06-02 · preprint** · Domain science and laboratories · biomedicine, code-execution, tool-use

Combines retrieval-guided planning and executable code with an environment of biomedical tools, software, and databases. Evaluations span heterogeneous tasks, multimodal data analysis, and experimental protocol design. The reported breadth supports biomedical research assistance; benchmark performance and protocol case studies should not be treated as general clinical validation.

Related entries: [Biomni](systems.md#biomni-system).

Sources: [1](https://doi.org/10.1101/2025.05.30.656746) · [2](https://biomni.stanford.edu/paper.pdf) · Content checked: 2026-10-22.

<a id="moose-chem2"></a>

### [MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery via Hierarchical Search](https://arxiv.org/abs/2505.19209)

**2025-05-25 · peer-reviewed** · Hypothesis and idea generation · chemistry, hierarchical-search, hypothesis

Expands coarse research directions into increasingly detailed hypotheses through hierarchical search, comparing different language-model scoring ensembles. Evaluation uses expert-annotated fine-grained hypotheses from recent literature. The study tests alignment with known hypotheses and model-defined rewards; a detailed, high-scoring proposal still needs independent checks and experimental testing.

Sources: [1](https://arxiv.org/abs/2505.19209) · [2](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8066ae1446b2bbccb5159587cc3b3bcc-Abstract-Conference.html) · Content checked: 2026-10-22.

<a id="ai-researcher"></a>

### [AI-Researcher: Autonomous Scientific Innovation](https://arxiv.org/abs/2505.18705) · [Code](https://github.com/HKUDS/AI-Researcher)

**2025-05-24 · peer-reviewed** · End-to-end research · multi-agent, machine-learning, scientist-bench

Orchestrates literature review, hypothesis formation, algorithm implementation, experiments, and manuscript preparation. It also introduces Scientist-Bench, with guided innovation and open-ended tasks derived from existing AI research. Its implementation and paper-quality evaluations help compare research pipelines; claims about innovation remain conditioned on the benchmark and evaluation protocol.

Related entries: [Scientist-Bench](benchmarks.md#scientist-bench).

Sources: [1](https://arxiv.org/abs/2505.18705) · [2](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d904d300a105809a2114d727851e759-Abstract-Conference.html) · [3](https://github.com/HKUDS/AI-Researcher) · Content checked: 2026-10-22.

<a id="ai-scientist-v2"></a>

### [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066) · [Code](https://github.com/SakanaAI/AI-Scientist-v2)

**2025-04-10 · preprint** · End-to-end research · tree-search, machine-learning, paper-generation

Replaces fixed experiment templates with progressive agentic tree search managed by an experiment agent, and uses visual feedback to refine figures. Three generated manuscripts were submitted to an ICLR workshop, with one meeting its acceptance threshold. This provides a bounded peer-review case study rather than broad evidence of researcher replacement.

Related entries: [The AI Scientist-v2](systems.md#ai-scientist-v2-system).

Sources: [1](https://arxiv.org/abs/2504.08066) · Content checked: 2026-10-22.

<a id="agentrxiv"></a>

### [AgentRxiv: Towards Collaborative Autonomous Research](https://arxiv.org/abs/2503.18102)

**2025-03-23 · preprint** · End-to-end research · research-memory, collaboration, shared-artifacts

Lets agent laboratories publish and retrieve reports through a shared preprint server, allowing later research runs to build on earlier findings. Experiments on reasoning and prompting methods compare shared research against isolated agents. The measured gains concern benchmark-solving strategies, not a demonstrated open scientific community across disciplines.

Sources: [1](https://arxiv.org/abs/2503.18102) · Content checked: 2026-10-22.

<a id="agent-laboratory"></a>

### [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)

**2025-01-08 · peer-reviewed** · End-to-end research · human-ai-collaboration, experimentation, paper-generation

Takes a human research idea through literature review, experimentation, and report writing, producing code and a manuscript while allowing feedback at each stage. Comparisons across models and a researcher study report benefits from human guidance. The results support supervised research assistance within the tested machine-learning workflows.

Related entries: [Agent Laboratory](systems.md#agent-laboratory-system).

Sources: [1](https://arxiv.org/abs/2501.04227) · [2](https://aclanthology.org/2025.findings-emnlp.320/) · Content checked: 2026-10-22.

<a id="year-2024"></a>

## 2024

<a id="data-to-paper"></a>

### [Autonomous LLM-driven research from data to human-verifiable research papers](https://doi.org/10.1056/AIoa2400555) · [Code](https://github.com/Technion-Kishony-lab/data-to-paper)

**2024-12-03 · peer-reviewed** · End-to-end research · provenance, data-analysis, human-oversight

Guides agents from annotated data through hypotheses, analysis code, results, and a manuscript while tracing information backward to its sources. The study reports stronger reliability for simpler goals and limited novelty, with human co-piloting increasingly important as complexity rises. Traceability is a central design feature rather than an afterthought.

Sources: [1](https://arxiv.org/abs/2404.17605) · [2](https://doi.org/10.1056/AIoa2400555) · Content checked: 2026-10-22.

<a id="cycleresearcher"></a>

### [CycleResearcher: Improving Automated Research via Automated Review](https://arxiv.org/abs/2411.00816) · [Code](https://github.com/ktwu01/CycleResearcher)

**2024-10-28 · peer-reviewed** · End-to-end research · research-review, preference-training, open-models

Trains research-writing and reviewing models in a feedback cycle using research and peer-review datasets. Generated papers are refined through simulated review, with evaluations of score prediction and manuscript ratings. Those simulated ratings measure an important writing-and-review capability, but should not be interpreted as independently executed experiments or scientific discoveries.

Sources: [1](https://arxiv.org/abs/2411.00816) · [2](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf) · Content checked: 2026-10-22.

<a id="moose-chem"></a>

### [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://arxiv.org/abs/2410.07076)

**2024-10-09 · peer-reviewed** · Hypothesis and idea generation · chemistry, rediscovery, inspiration-retrieval

Decomposes hypothesis discovery into retrieving inspirations, composing hypotheses, and ranking them. A chemist-annotated benchmark uses papers published after the evaluated model's stated training cutoff to test rediscovery. Similarity to withheld published hypotheses measures a useful capability, but does not establish prospective novelty or successful laboratory realization.

Sources: [1](https://arxiv.org/abs/2410.07076) · [2](https://proceedings.iclr.cc/paper_files/paper/2025/hash/51fd9a7d1706023cb9f8210cc6ac357c-Abstract-Conference.html) · Content checked: 2026-10-22.

<a id="scideator-paper"></a>

### [Scideator: Human-LLM Compound System for Scientific Ideation through Facet Recombination and Novelty Evaluation](https://arxiv.org/abs/2409.14634)

**2024-09-23 · peer-reviewed** · Hypothesis and idea generation · human-ai-collaboration, facet-recombination, novelty

Extracts purpose, mechanism, and evaluation facets from papers, lets researchers recombine them, and retrieves related work to assess originality. The updated paper reports creativity-support benefits and novelty-checking ablations. Its contribution is an interactive ideation process, with user judgments and retrieval quality distinct from validating a finished scientific result.

Sources: [1](https://arxiv.org/abs/2409.14634) · [2](https://cris.huji.ac.il/en/publications/scideator-human-llm-compound-system-for-scientific-ideation-throu/) · [3](https://doi.org/10.1145/3786335.3813161) · Content checked: 2026-10-22.

<a id="sciagents"></a>

### [SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning](https://arxiv.org/abs/2409.05556)

**2024-09-09 · preprint** · Hypothesis and idea generation · knowledge-graphs, materials, multi-agent

Combines ontological knowledge graphs, retrieval tools, and collaborating language-model agents to propose and critique interdisciplinary hypotheses. Biologically inspired materials case studies illustrate connections between concepts and proposed mechanisms. The primary evidence is hypothesis-generation and reasoning case studies, which should be separated from laboratory verification of resulting material designs.

Sources: [1](https://arxiv.org/abs/2409.05556) · Content checked: 2026-10-22.

<a id="novel-research-ideas-human-study"></a>

### [Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://arxiv.org/abs/2409.04109)

**2024-09-06 · peer-reviewed** · Hypothesis and idea generation · human-evaluation, novelty, ideation

Uses blinded comparisons between researcher-written and agent-generated NLP ideas, involving more than one hundred researchers. AI ideas receive higher novelty judgments but weaker feasibility judgments, while self-evaluation and diversity remain problematic. The experiment evaluates perceived idea quality, not whether executing those ideas yields stronger scientific discoveries.

Sources: [1](https://arxiv.org/abs/2409.04109) · [2](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html) · Content checked: 2026-10-22.

<a id="ai-scientist"></a>

### [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) · [Code](https://github.com/SakanaAI/AI-Scientist)

**2024-08-12 · preprint** · End-to-end research · machine-learning, paper-generation, automated-review

Connects idea generation, code editing, experiments, visualization, manuscript drafting, and automated reviewing around human-provided research templates. Demonstrations cover diffusion models, language models, and learning dynamics. Paper-quality claims rely substantially on an automated reviewer, and the template dependence bounds the extent of open-ended autonomy demonstrated.

Related entries: [The AI Scientist](systems.md#ai-scientist-system).

Sources: [1](https://arxiv.org/abs/2408.06292) · Content checked: 2026-10-22.

<a id="biodiscoveryagent"></a>

### [BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments](https://arxiv.org/abs/2405.17631) · [Code](https://github.com/snap-stanford/BioDiscoveryAgent)

**2024-05-27 · peer-reviewed** · Experimentation and implementation · biology, experimental-design, genetic-perturbation

Selects genetic perturbations using language-model knowledge, literature search, code analysis, and critique, then updates proposals from experimental outcomes. Evaluation across perturbation datasets compares it with Bayesian optimization and random selection. The evidence concerns efficient experiment selection in the tested settings rather than autonomous validation of arbitrary biological mechanisms.

Sources: [1](https://arxiv.org/abs/2405.17631) · [2](https://proceedings.iclr.cc/paper_files/paper/2025/file/4252dc94531833029000f85dc5fac792-Paper-Conference.pdf) · Content checked: 2026-10-22.

<a id="chemcrow"></a>

### [ChemCrow: Augmenting large language models with chemistry tools](https://www.nature.com/articles/s42256-024-00832-8)

**2024-05-08 · peer-reviewed** · Experimentation and implementation · chemistry, tool-use, synthesis

Augments a language model with expert-designed chemistry tools for synthesis, molecular tasks, and materials design. The work includes executed synthesis examples and expert assessment. Its preprint also highlights weaknesses in using a language model to judge chemical correctness, underscoring why tool execution and independent expert evaluation matter.

Sources: [1](https://www.nature.com/articles/s42256-024-00832-8) · [2](https://arxiv.org/abs/2304.05376) · [3](https://research.ibm.com/publications/augmenting-large-language-models-with-chemistry-tools) · Content checked: 2026-10-22.

<a id="researchagent"></a>

### [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://arxiv.org/abs/2404.07738)

**2024-04-11 · peer-reviewed** · Hypothesis and idea generation · citation-graphs, ideation, review-agents

Expands a seed paper through an academic graph and a concept store, then iteratively refines proposed problems, methods, and experimental designs using reviewing agents. Human and model evaluations cover multiple disciplines. The demonstrated output is a research proposal; executing the experiments and validating its scientific claims remain separate tasks.

Sources: [1](https://arxiv.org/abs/2404.07738) · [2](https://aclanthology.org/2025.naacl-long.342/) · Content checked: 2026-10-22.

<a id="year-2023"></a>

## 2023

<a id="coscientist"></a>

### [Coscientist: Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0)

**2023-12-20 · peer-reviewed** · Experimentation and implementation · chemistry, laboratory-automation, tool-use

Connects language-model planning to web and documentation search, code execution, and experimental equipment. Demonstrations include chemical synthesis planning and reaction optimization, illustrating how tool access can turn reasoning into physical experiments. The work operates within a configured laboratory and selected tasks, with human setup and oversight remaining important.

Related entries: [Coscientist](systems.md#coscientist-system).

Sources: [1](https://www.nature.com/articles/s41586-023-06792-0) · [2](https://arxiv.org/abs/2304.05332) · [3](https://pubmed.ncbi.nlm.nih.gov/38123806/) · Content checked: 2026-10-22.

<a id="funsearch"></a>

### [FunSearch: Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) · [Code](https://github.com/google-deepmind/funsearch)

**2023-12-14 · peer-reviewed** · Domain science and laboratories · mathematics, evolutionary-search, executable-evaluation

Pairs a language model with an evaluator and an evolving database of programs, searching for code that constructs strong solutions. The paper reports new cap-set constructions and improved bin-packing heuristics. Its successes depend on explicit evaluators and problem specifications, making the verification mechanism central to its scientific relevance.

Sources: [1](https://www.nature.com/articles/s41586-023-06924-6) · Content checked: 2026-10-22.

<a id="scimon"></a>

### [SciMON: Scientific Inspiration Machines Optimized for Novelty](https://arxiv.org/abs/2305.14259)

**2023-05-23 · peer-reviewed** · Hypothesis and idea generation · literature-based-discovery, novelty, retrieval

Retrieves scientific inspirations and iteratively revises proposed ideas by comparing them with prior literature. Its contextual idea-generation setting goes beyond predicting links between concepts. Human-oriented evaluations show improvements over baseline generation while also exposing limited technical depth and novelty, making it useful for studying ideation quality rather than experimental discovery.

Sources: [1](https://arxiv.org/abs/2305.14259) · [2](https://aclanthology.org/2024.acl-long.18/) · Content checked: 2026-10-22.

<a id="year-2009"></a>

## 2009

<a id="robot-scientist-adam"></a>

### [The Automation of Science (Robot Scientist Adam)](https://doi.org/10.1126/science.1165620)

**2009-04-03 · peer-reviewed** · Experimentation and implementation · historical-foundation, robot-scientist, provenance

Combines hypothesis generation, automated laboratory experiments, and a logical record of the research process to study yeast functional genomics. The authors report manual confirmation of Adam's conclusions. This pre-LLM example grounds modern autonomy discussions in a closed experimental loop and explicit provenance within a constrained biological problem.

Sources: [1](https://doi.org/10.1126/science.1165620) · [2](https://pubmed.ncbi.nlm.nih.gov/19342587/) · Content checked: 2026-10-22.

## Browse by topic

Jump to an entry above; links within each topic follow the same date order.

<a id="topic-end-to-end"></a>

### End-to-end research

- **2026-10-13** — [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](#agentic-scientist).
- **2026-10-01** — [Can AI Scientists Coordinate at Runtime?](#runtime-agent-coordination).
- **2026-10-01** — [Denario Project: Deep Knowledge Artificial Intelligence Agents for Scientific Discovery](#denario).
- **2026-09-17** — [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](#scientist-two).
- **2026-09-15** — [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](#sciencebuddy).
- **2026-05-25** — [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](#scientist-one).
- **2026-03-25** — [Towards end-to-end automation of AI research](#ai-scientist-nature).
- **2026-03-09** — [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](#evoscientist).
- **2025-11-04** — [Kosmos: An AI Scientist for Autonomous Discovery](#kosmos).
- **2025-05-24** — [AI-Researcher: Autonomous Scientific Innovation](#ai-researcher).
- **2025-04-10** — [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](#ai-scientist-v2).
- **2025-03-23** — [AgentRxiv: Towards Collaborative Autonomous Research](#agentrxiv).
- **2025-01-08** — [Agent Laboratory: Using LLM Agents as Research Assistants](#agent-laboratory).
- **2024-12-03** — [Autonomous LLM-driven research from data to human-verifiable research papers](#data-to-paper).
- **2024-10-28** — [CycleResearcher: Improving Automated Research via Automated Review](#cycleresearcher).
- **2024-08-12** — [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](#ai-scientist).

<a id="topic-hypothesis"></a>

### Hypothesis and idea generation

- **2026-05-19** — [Accelerating scientific discovery with Co-Scientist](#google-co-scientist).
- **2026-03-04** — [MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier](#moose-star).
- **2025-06-25** — [The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas](#ideation-execution-gap).
- **2025-05-25** — [MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery via Hierarchical Search](#moose-chem2).
- **2024-10-09** — [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](#moose-chem).
- **2024-09-23** — [Scideator: Human-LLM Compound System for Scientific Ideation through Facet Recombination and Novelty Evaluation](#scideator-paper).
- **2024-09-09** — [SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning](#sciagents).
- **2024-09-06** — [Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](#novel-research-ideas-human-study).
- **2024-04-11** — [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](#researchagent).
- **2023-05-23** — [SciMON: Scientific Inspiration Machines Optimized for Novelty](#scimon).

<a id="topic-domain-science"></a>

### Domain science and laboratories

- **2026-05-19** — [Robin: A multi-agent system for automating scientific discovery](#robin).
- **2025-07-29** — [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](#virtual-lab).
- **2025-06-16** — [AlphaEvolve: A coding agent for scientific and algorithmic discovery](#alphaevolve).
- **2025-06-02** — [Biomni: A General-Purpose Biomedical AI Agent](#biomni).
- **2023-12-14** — [FunSearch: Mathematical discoveries from program search with large language models](#funsearch).

<a id="topic-survey"></a>

### Surveys and perspectives

- **2026** — [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](#verification-gap-survey).
- **2025-10-27** — [A Survey of AI Scientists](#ai-scientists-survey).
- **2025-08-18** — [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](#agentic-science-survey).

<a id="topic-experimentation"></a>

### Experimentation and implementation

- **2026-05-19** — [Empirical Research Assistance: An AI system to help scientists write expert-level empirical software](#empirical-research-assistance).
- **2024-05-27** — [BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments](#biodiscoveryagent).
- **2024-05-08** — [ChemCrow: Augmenting large language models with chemistry tools](#chemcrow).
- **2023-12-20** — [Coscientist: Autonomous chemical research with large language models](#coscientist).
- **2009-04-03** — [The Automation of Science (Robot Scientist Adam)](#robot-scientist-adam).
