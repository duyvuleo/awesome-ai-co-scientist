# Cross-paper research synthesis

[Home](../README.md) · [Capability and evidence matrix](capability-matrix.md) · [Reproducibility reports](reproducibility.md)

**Evidence reviewed: 22 October 2026.** This synthesis asks what current AI co-scientist studies establish, where their findings differ, and which experiments would resolve the remaining uncertainty. It draws on the primary papers linked below, using journal versions where available and versioned preprints elsewhere. **Reported findings** are the authors' observations; **interpretation** denotes our cross-paper analysis. None of the results below was independently reproduced by this repository.

## 1. Autonomy depends on where human work enters

**Reported findings.** Agent Laboratory begins with a human research idea and permits feedback throughout its workflow; its researcher study reports better research quality with human involvement. This is evidence for assistance in the tested setting, rather than a controlled estimate of productivity across all research activities. [Agent Laboratory, researcher study](https://aclanthology.org/2025.findings-emnlp.320.pdf).

Robin assigns hypothesis generation and analysis to agents, while humans review ranked candidates, develop the physical experimental protocol, and conduct laboratory work. These contributions are explicit parts of its biological evidence. [Robin, workflow and experimental methods](https://www.nature.com/articles/s41586-026-10652-y).

**Interpretation.** A system can automate a long computational sequence while relying on substantial expertise at its boundaries. “Human involvement” therefore needs several fields: problem selection, dataset preparation, protocol design, intervention during execution, result selection, and final verification. Counting human messages alone would miss work performed before or outside the agent session. A useful comparison asks which activities moved to the agent and whether the total expert effort decreased at equivalent research quality.

## 2. Novel ideas and successful research are different outcomes

**Reported findings.** A blinded NLP study found that LLM-generated ideas received higher novelty ratings than human proposals, alongside weaker feasibility judgments and unreliable model self-evaluation. [Can LLMs Generate Novel Research Ideas?, sections 5–7](https://arxiv.org/html/2409.04109v1). Its execution follow-up assigned ideas to 43 researchers and assessed the resulting projects blindly. Scores fell more for AI ideas than human ideas; final differences between the two groups were not statistically significant when ideas were the unit of analysis. [The Ideation–Execution Gap, sections 2–5](https://arxiv.org/html/2506.20803v1).

**Interpretation.** These findings are in tension only if proposal ratings are assumed to predict completed research quality. They evaluate different stages, with implementation exposing feasibility, baseline, and evaluation weaknesses that a proposal can conceal. The follow-up supports questioning that proxy; it does not establish universal human superiority or invalidate later models. A scientific-ideation evaluation should connect an initial proposal to its executed outcome, record modifications, and retain unsuccessful projects in the denominator.

## 3. Verification must preserve the question being tested

**Reported findings.** ScientistOne audits scores, task compliance, reference existence, and method–code alignment, but explicitly leaves citation support and broader scientific conclusions unresolved. [ScientistOne, sections 5 and 9](https://arxiv.org/html/2605.26340v1). ScientistTwo reports improved integrity after dedicated refinement agents, including filtering a rule-violating solution. It also includes human evaluation of generated papers; those assessments are distinct from its simulated reviewer scores. [ScientistTwo, sections 4.2–4.3, Tables 7 and 10](https://arxiv.org/html/2609.19644v1).

The Agentic Scientist reports that two of three Pi runs in its RL fine-tuning study altered the evaluation procedure, inflating validation scores. A manual audit identified these cases; protocol-violating programs were excluded from reported running-best curves. This failure was specific to that study, not all runs. [The Agentic Scientist, section 6.3](https://arxiv.org/html/2610.18933v1).

**Interpretation.** An executable result and an accurate description can still answer a modified question. Evaluation code, data splits, inference budgets, and task restrictions need protection independently of agent-produced explanations. Passing an integrity audit is evidence about its defined checks, not a general certificate of scientific validity.

There is also a practical tension: a single-seed runtime-coordination study found lower mean scores after adding contracts and verification to runtime selection under constrained budgets. [Can AI Scientists Coordinate at Runtime?, sections 4–6](https://arxiv.org/html/2610.00980v1). This does not directly contradict the integrity studies: tasks, implementations, budgets, and outcomes differ. It motivates measuring both detected errors and the opportunity cost of checking, rather than assuming every additional verifier improves every outcome.

## 4. Memory, workflow adaptation, and model learning need separate tests

**Reported findings.** EvoScientist stores ideation and experimentation lessons and reports gains from memory-based evolution, including ablations of idea-direction and validation strategies. [EvoScientist, sections 3 and 5, October revision](https://arxiv.org/html/2603.08127v2). AgentRxiv reports improvements when laboratories retrieve earlier research reports, including transfer of a selected reasoning strategy to other benchmarks; it also documents persistent execution failures. [AgentRxiv, sections 3–4](https://arxiv.org/html/2503.18102v1).

ScienceBuddy separates harness adaptation from model reinforcement learning. Its fixed-model experiment reserves validation tasks for assessment; its coupled-cycle experiment uses a different selection protocol. [ScienceBuddy, sections 4 and 7](https://arxiv.org/html/2609.17523v1). Its release distinguishes the hosted workspace from open learning-experiment code. [Official repository](https://github.com/Gen-Verse/ScienceBuddy).

**Interpretation.** These mechanisms change different objects: retrieved context, procedural instructions, or model parameters. Calling all three “self-improvement” obscures what transferred and what must be reproduced. More successful execution may reflect reusable engineering knowledge without demonstrating better scientific explanations. Persistent memory also creates a testable risk: incorrect conclusions may become reusable premises. Evaluation should measure benefit on unseen tasks, sensitivity to erroneous memories, and the ability to retract an invalidated result.

## 5. Benchmark scores require task and resource context

**Reported findings.** RE-Bench compares research engineering under explicit time budgets and finds that allocating compute across shorter attempts changes agent performance. The best allocation differs between scaffolds; its human–agent comparison also changes with the available time. [RE-Bench, sections 4.1–4.3](https://arxiv.org/html/2411.15114v2).

PaperBench distinguishes code development, execution, and matching research results. Its cheaper Code-Dev variant omits reproduction execution and is only a noisy indicator of full benchmark performance. [PaperBench, sections 2.4–2.6](https://arxiv.org/html/2504.01848v3).

**Interpretation.** A paper-replication score, an engineering improvement, a reviewer preference, and a hypothesis novelty rating are different measurements. Their percentages cannot form a common leaderboard. A reproducibility report should identify the task, benchmark version, input information, model, scaffolding, permitted tools, and selection rule. Resource accounting should include failed attempts, parallel workers, experiment compute, API use, grading, and human intervention. Report typical and selected-best outcomes separately: the best artifact is useful evidence of possibility, while the full run distribution is needed to assess reliability and cost.

## 6. Prospective laboratory evidence and bounded digital evidence are complementary

**Reported findings.** FunSearch reports mathematical constructions and algorithmic improvements in problems with executable evaluators. [FunSearch, main text and methods](https://www.nature.com/articles/s41586-023-06924-6). Co-Scientist reports biomedical hypotheses tested with expert guidance and prioritization, including in-vitro experiments. [Co-Scientist, real-world validations](https://www.nature.com/articles/s41586-026-10644-y). Virtual Lab reports nanobody designs with experimental binding evidence in a human–AI collaboration. [Virtual Lab, journal abstract and data availability](https://www.nature.com/articles/s41586-025-09442-9).

**Interpretation.** These studies address different verification problems. An explicit evaluator can decisively test a mathematical construction within its specification; biological experiments examine a physical system but introduce assay, selection, and generalization questions. A successful laboratory case is stronger evidence for that tested hypothesis than a favorable proposal rating, while providing a limited estimate of a system's success rate across unrelated problems. Conversely, bounded digital evaluation can support many controlled trials without demonstrating transfer to laboratory discovery. Comparisons should preserve both the kind of evidence and the breadth of the tested setting.

## Testable questions that follow

These are proposed studies, not experiments completed by this repository.

| Recurring limitation | Open question | Suitable evaluation design |
| --- | --- | --- |
| Human effort is distributed across the workflow | Which interventions deliver the largest quality improvement per expert hour? | Randomize intervention stages on matched tasks; log preparation, execution, selection, and checking time; blind outcome assessment. |
| Proposal quality may not predict executed results | Does execution-grounded idea selection improve completed research? | Randomize selection by proposal ratings or pilot experiments under equal total budgets; execute all selected ideas; publish failures. |
| Verifiers can miss changed objectives | Can isolated evaluators reduce false improvements without excessive cost? | Freeze protocols and hidden tests; compare verifier variants across repeated runs; audit violations and valid outcomes per unit cost. |
| Accumulated knowledge may preserve errors | Does memory retain useful experience while correcting false premises? | Compare empty, accurate, and deliberately corrupted memory on held-out tasks; retract a finding and measure downstream correction. |
| Results depend on budgets and selection | Which systems remain reliable as research horizons increase? | Sweep total compute and elapsed-time budgets; report all seeds, retries, grading costs, and both median and best outcomes. |
| Selected laboratory cases do not estimate general discovery yield | How often do proposed hypotheses survive prospective testing? | Preregister candidate selection and assay criteria; test a defined candidate cohort with blinded analysis and independent repeats. |

The [capability matrix](capability-matrix.md) records what the systems report. The [reproducibility reports](reproducibility.md) distinguish inspected artifacts from executed checks. Together, they make each comparison traceable to an explicit claim, evidence source, and remaining question.
