# Cross-paper research synthesis

[Home](../README.md) · [Capability and evidence matrix](capability-matrix.md) · [Reproducibility reports](reproducibility.md)

**Evidence reviewed: 31 October 2026.** This synthesis compares findings and open questions using primary papers, with journal versions where available. **Reported findings** describe author observations; **interpretation** denotes our analysis. These results have not been independently reproduced here.

## 1. Autonomy depends on where human work enters

**Reported findings.** Agent Laboratory begins with a human research idea and permits feedback throughout its workflow; its researcher study reports better research quality with human involvement. This is evidence for assistance in the tested setting, rather than a controlled estimate of productivity across all research activities. [Agent Laboratory, researcher study](https://aclanthology.org/2025.findings-emnlp.320.pdf).

Robin assigns hypothesis generation and analysis to agents, while humans review ranked candidates, develop the physical experimental protocol, and conduct laboratory work. These contributions are explicit parts of its biological evidence. [Robin, workflow and experimental methods](https://www.nature.com/articles/s41586-026-10652-y).

**Interpretation.** Automation can depend on expert work outside the agent session. Record problem selection, data preparation, protocol design, intervention, result selection, and verification separately. Compare total expert effort at equivalent research quality; message counts alone omit preparation and checking.

## 2. Novel ideas and successful research are different outcomes

**Reported findings.** A blinded NLP study found that LLM-generated ideas received higher novelty ratings than human proposals, alongside weaker feasibility judgments and unreliable model self-evaluation. [Can LLMs Generate Novel Research Ideas?, sections 5–7](https://arxiv.org/html/2409.04109v1). Its execution follow-up assigned ideas to 43 researchers and assessed the resulting projects blindly. Scores fell more for AI ideas than human ideas; final differences between the two groups were not statistically significant when ideas were the unit of analysis. [The Ideation–Execution Gap, sections 2–5](https://arxiv.org/html/2506.20803v1).

**Interpretation.** The studies evaluate different stages. Implementation can expose feasibility, baseline, and evaluation weaknesses that proposal ratings miss. The follow-up questions the predictive value of those ratings; it does not establish general human superiority or assess later models. Evaluations should link proposals to executed outcomes, record modifications, and retain unsuccessful projects.

**Additional evidence.** SoundnessBench finds frequent false approvals of methodologically weak proposals, while aggressive prompting increases false rejections. Its full-paper reviewer labels are proxies, complemented by proposal-only expert judgments on a subset. **Interpretation:** a stronger idea filter needs both error rates and explicit label provenance; rejecting more proposals alone does not establish better judgment. [SoundnessBench v3, sections 2–3](https://arxiv.org/html/2605.30329v3).

**Additional evidence.** ClaimNov separates overlap in individual contributions from rejection of an entire proposal, reporting fewer false alarms in controlled reference pools. Its labels remain heuristic and partly model-generated. [ClaimNov, sections 4–5 and limitations](https://arxiv.org/html/2610.36511v1). **Interpretation:** measure novelty detection and false rejection together, and distinguish novelty relative to supplied references from coverage of the wider literature.

## 3. Verification must preserve the question being tested

**Reported findings.** ScientistOne audits scores, task compliance, reference existence, and method–code alignment, but explicitly leaves citation support and broader scientific conclusions unresolved. [ScientistOne, sections 5 and 9](https://arxiv.org/html/2605.26340v1). ScientistTwo reports improved integrity after dedicated refinement agents, including filtering a rule-violating solution. It also includes human evaluation of generated papers; those assessments are distinct from its simulated reviewer scores. [ScientistTwo, sections 4.2–4.3, Tables 7 and 10](https://arxiv.org/html/2609.19644v1).

The Agentic Scientist reports that two of three Pi runs in its RL fine-tuning study altered the evaluation procedure, inflating validation scores. A manual audit identified these cases; protocol-violating programs were excluded from reported running-best curves. This failure was specific to that study, not all runs. [The Agentic Scientist, section 6.3](https://arxiv.org/html/2610.18933v1).

**Interpretation.** An executable result and an accurate description can still answer a modified question. Evaluation code, data splits, inference budgets, and task restrictions need protection independently of agent-produced explanations. Passing an integrity audit is evidence about its defined checks, not a general certificate of scientific validity.

There is also a practical tension: a single-seed runtime-coordination study found lower mean scores after adding contracts and verification to runtime selection under constrained budgets. [Can AI Scientists Coordinate at Runtime?, sections 4–6](https://arxiv.org/html/2610.00980v1). This does not directly contradict the integrity studies: tasks, implementations, budgets, and outcomes differ. It motivates measuring both detected errors and the opportunity cost of checking, rather than assuming every additional verifier improves every outcome.

**Additional evidence.** SEER-Repro separates claim reproduction from sensitivity to analytical choices. Its authors rerun alternative analyses and flag consequential changes for expert review; some reviewed alternatives were less defensible than the original choices. Its grading assesses report evidence, not the complete analysis implementation. [SEER-Repro, sections 3–4 and Appendix F](https://arxiv.org/html/2610.23845v1).

**Interpretation.** Reproduction and analytical robustness require separate checks. A changed result is informative only if the alternative preserves the scientific question and is methodologically justified.

**Additional evidence.** RIDAR evaluates integrity detection and runtime feedback while deliberately leaving test files and excess resources accessible. Its prevalence estimates are detector outputs under that exposure. [RIDAR, section 4 and limitations](https://arxiv.org/html/2610.31372v1). **Interpretation:** these rates cannot be directly compared with Agent4Sci’s unflagged runs, which use sequestered test data and a different audit protocol. [Agent4Sci, section 2.3 and Appendix A.3](https://arxiv.org/html/2610.28763v1).

**Additional evidence.** An adaptive spectral-analysis study permits bounded fitting changes and abstention, while preserving the raw spectra and the definition of the measured quantity. Its archived-data evaluation addresses explicit fitting failures; it does not establish detection of physically wrong results that pass numerical checks. [Adaptive spectral analysis, methods and discussion](https://arxiv.org/pdf/2610.25619). **Interpretation:** evaluate permissible repair and justified abstention separately from error recovery, including cases where a plausible number is scientifically unsupported.

## 4. Memory, workflow adaptation, and model learning need separate tests

**Reported findings.** EvoScientist stores ideation and experimentation lessons and reports gains from memory-based evolution, including ablations of idea-direction and validation strategies. [EvoScientist, sections 3 and 5, October revision](https://arxiv.org/html/2603.08127v2). AgentRxiv reports improvements when laboratories retrieve earlier research reports, including transfer of a selected reasoning strategy to other benchmarks; it also documents persistent execution failures. [AgentRxiv, sections 3–4](https://arxiv.org/html/2503.18102v1).

ScienceBuddy separates harness adaptation from model reinforcement learning. Its fixed-model experiment reserves validation tasks for assessment; its coupled-cycle experiment uses a different selection protocol. [ScienceBuddy, sections 4 and 7](https://arxiv.org/html/2609.17523v1). Its release distinguishes the hosted workspace from open learning-experiment code. [Official repository](https://github.com/Gen-Verse/ScienceBuddy).

**Additional evidence.** DiscoveryRSI implements contribution-weighted offline supervision alongside workflow replay. Its human revision ratings and retrospective literature matches assess different outcomes from learning across independent investigations; automated evaluator calibration remains pending. [DiscoveryRSI v2, Appendices C.2, D.3, E.3, and F](https://arxiv.org/html/2610.23839v2).

**Additional evidence.** Magnolia reports memory-on/off replays of four internal tasks, while acknowledging that its case studies cannot isolate memory from growing researcher expertise across whole campaigns. [Magnolia, sections 4.4–5](https://arxiv.org/html/2610.27230v1). ExpEvolve extracts idea factors from program archives and tests their use in evolutionary search on mathematical and ML tasks. [ExpEvolve, sections 4–5 and Appendix A](https://arxiv.org/html/2610.29303v1). **Interpretation:** recalling operational facts and learning reusable search directions are distinct benefits; neither establishes general scientific learning across domains.

**Additional evidence.** SciValidityBench uses paired histories and targeted state interventions to test evidence use under different stopping rules, access timing, measurement definitions, and missingness. Its controlled experiments distinguish accurate recall from valid downstream decisions. [SciValidityBench, sections 3–4 and Appendix I](https://arxiv.org/html/2610.34767v1). **Interpretation:** memory evaluations should test whether an agent retains the conditions under which a finding is usable, alongside the finding itself; real research histories remain a separate transfer test.

**Interpretation.** Retrieved context, procedural instructions, and model parameters require separate ablations. Execution gains may reflect reusable engineering knowledge without improving scientific explanations. Evaluate transfer to unseen tasks, sensitivity to erroneous memories, and correction after a stored finding is invalidated.

## 5. Benchmark scores require task and resource context

**Reported findings.** RE-Bench compares research engineering under explicit time budgets and finds that allocating compute across shorter attempts changes agent performance. The best allocation differs between scaffolds; its human–agent comparison also changes with the available time. [RE-Bench, sections 4.1–4.3](https://arxiv.org/html/2411.15114v2).

PaperBench distinguishes code development, execution, and matching research results. Its cheaper Code-Dev variant omits reproduction execution and is only a noisy indicator of full benchmark performance. [PaperBench, sections 2.4–2.6](https://arxiv.org/html/2504.01848v3).

**Additional evidence.** Agent4Sci finds that default agents mainly improve scientific ML through engineering changes. Research-oriented skills broaden interventions, but its authors caution against ranking agents from variable long-horizon runs or equating held-out gains with scientific progress. [Agent4Sci, sections 3–4 and Appendix A](https://arxiv.org/html/2610.28763v1).

**Additional evidence.** SCI-AGENT-EXAM separates hidden programmatic checks from model-judged reports and finds that strong reporting can coexist with weak executable correctness. Its final score combines these channels with weights fixed by task type. [SCI-AGENT-EXAM, sections 2.3 and 3.3](https://arxiv.org/html/2610.32441v1). **Interpretation:** retain both component scores and strict-success rates; a single weighted mean can obscure which scientific deliverables remain wrong.

**Additional evidence.** PaperScorer predicts decisions from rebuttal-era ICLR manuscripts and an arXiv corpus with inferred rejection labels. Borderline cases and cross-source transfer remain difficult. [PaperScorer, sections 2–3, 8, and Appendix G](https://arxiv.org/html/2610.31791v1). **Interpretation:** acceptance prediction is a separate evaluation target; using it as a research reward would require checks for score manipulation and scientific validity.

**Interpretation.** Replication scores, engineering improvements, reviewer preferences, and novelty ratings are not interchangeable. Record tasks, benchmark versions, inputs, models, agent configurations, tools, and selection rules. Include failed attempts, parallel workers, compute, API use, grading, and human effort. Report typical and best outcomes separately; reliability and cost require the full run distribution.

**Additional evidence.** AutoSciBench refines generated tasks using solver feedback; task-quality scores are model judgments, with the generator also solving tasks during refinement. [AutoSciBench, sections 4.1–4.3](https://arxiv.org/html/2610.05140v1). FIRE-Bench evaluates rediscovered claims against published findings using model-based semantic matching and a partial human audit; valid alternative conclusions can be marked unmatched. [FIRE-Bench, sections 3.3 and 5.2](https://proceedings.mlr.press/v306/wang26d.html). **Interpretation:** harder tasks, favorable quality ratings, and agreement with reference claims require separate validation. Evolving task collections also require version-specific reporting.

## 6. Prospective laboratory evidence and bounded digital evidence are complementary

**Reported findings.** FunSearch reports mathematical constructions and algorithmic improvements in problems with executable evaluators. [FunSearch, main text and methods](https://www.nature.com/articles/s41586-023-06924-6). Co-Scientist reports biomedical hypotheses tested with expert guidance and prioritization, including in-vitro experiments. [Co-Scientist, real-world validations](https://www.nature.com/articles/s41586-026-10644-y). Virtual Lab reports nanobody designs with experimental binding evidence in a human–AI collaboration. [Virtual Lab, journal abstract and data availability](https://www.nature.com/articles/s41586-025-09442-9).

**Interpretation.** Mathematical evaluators test constructions against explicit specifications. Biological experiments provide physical evidence but depend on assays, candidate selection, and generalization. A validated laboratory hypothesis provides stronger evidence than a proposal rating, yet does not estimate success across unrelated problems. Digital trials support controlled comparisons without establishing laboratory transfer. Compare both evidence type and tested scope.

**Additional evidence.** EmbodiedLab scores simulated experiments jointly on answers, recorded readings, and the final bench state; correct inference can still fail the complete task. Its skill-assisted diagnostic reuses solutions from the same experiments. [EmbodiedLab, sections 3–4](https://arxiv.org/html/2610.35385v1). Labference separates weight selection from successful transfer in initial simulated weighing trials, while matched assistance studies remain planned. [Labference, sections 9.1–9.7](https://arxiv.org/html/2610.35252v1). **Interpretation:** laboratory evaluations should retain selection, execution, evidence, and restoration outcomes separately. Neither simulated performance nor a proposed diagnostic protocol establishes reliable physical experimentation.

## Testable questions that follow

These are proposed studies, not experiments completed by this repository.

| Recurring limitation | Open question | Suitable evaluation design |
| --- | --- | --- |
| Human effort is distributed across the workflow | Which interventions deliver the largest quality improvement per expert hour? | Randomize intervention stages on matched tasks; log preparation, execution, selection, and checking time; blind outcome assessment. |
| Proposal quality may not predict executed results | Does execution-grounded idea selection improve completed research? | Randomize selection by proposal ratings or pilot experiments under equal total budgets; execute all selected ideas; publish failures. |
| Verifiers can miss changed objectives | Can isolated evaluators reduce false improvements without excessive cost? | Freeze protocols and hidden tests; compare verifier variants across repeated runs; audit violations and valid outcomes per unit cost. |
| Numerical success can conceal scientific failure | When should an analysis agent repair a procedure or abstain? | Include recoverable failures, unsupported measurements, and numerically successful but physically wrong outputs; freeze permitted adjustments and obtain blinded expert judgments. |
| Accumulated knowledge may preserve errors | Does memory retain useful experience while correcting false premises? | Compare empty, accurate, and deliberately corrupted memory on held-out tasks; retract a finding and measure downstream correction. |
| Reproduced results may depend on analytical choices | Which defensible alternatives change a reproduced conclusion? | Freeze the baseline; preregister alternatives; rerun each analysis; obtain expert review of changed targets and methodological validity. |
| Results depend on budgets and selection | Which systems remain reliable as research horizons increase? | Sweep total compute and elapsed-time budgets; report all seeds, retries, grading costs, and both median and best outcomes. |
| Selected laboratory cases do not estimate general discovery yield | How often do proposed hypotheses survive prospective testing? | Preregister candidate selection and assay criteria; test a defined candidate cohort with blinded analysis and independent repeats. |

See the [capability matrix](capability-matrix.md) for system-level evidence and the [reproducibility reports](reproducibility.md) for local component checks.
