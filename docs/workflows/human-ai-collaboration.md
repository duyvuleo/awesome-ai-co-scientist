# Recipe: measure the value of human collaboration

[← Workflow recipes](README.md) · [Study packs](../study-packs.md) · [Catalog CLI](../cli.md)

**Question:** Which human interventions improve valid research outcomes under a matched total budget and elapsed-time limit?

**Status and scope:** Proposed study, not an executed comparison. Local task selection and protocol preparation incur no model/API charges. Recruiting participants or running research agents requires separately specified resources and a budget; neither is triggered by a study pack.

## Motivation and task choice

Agent Laboratory permits human guidance and reports improved research quality with involvement in its tested setting. RE-Bench shows that time allowances and attempt allocation affect human–agent comparisons. Neither finding determines the value of a particular intervention on a new task. [Agent Laboratory](https://aclanthology.org/2025.findings-emnlp.320/), [RE-Bench, sections 4.1–4.3](https://arxiv.org/html/2411.15114v2).

For a worked planning example, choose a frozen subset of [ScienceAgentBench](https://arxiv.org/abs/2410.05080) tasks: each condition receives the same task data and must return a self-contained Python program and required analysis outputs. Record selected task IDs and environment versions. Use the [capability matrix](../capability-matrix.md) to find supported intervention points. Test one intervention: human review of the analysis plan before execution. Keep the model, memory policy, and tools fixed across agent conditions.

## Conditions and fair resource matching

Compare human-only, agent-only, and human–agent conditions if resources permit. Define allowed assistance for the human-only condition and all setup shared by the other conditions. Use identical task information, datasets, evaluator access, and compute environment. Record differences that cannot be controlled.

Set the same elapsed-time cap and total monetary resource cap per task. Prespecify conversion rates for human hours, compute, and model use; report the underlying quantities as well, since monetary equivalence depends on those rates. Count preparation, interventions, retries, parallel workers, output selection, and verification. Unused resources remain unused. A second resource cap may become binding first; report which one rather than quietly extending a condition's allowance.

## Procedure

1. Freeze the task set, baseline, success criterion, stopping rules, and permitted intervention stage. Include the no-agent baseline even if its result is uncompetitive.
2. Randomize task assignment within difficulty groups. Balance participant expertise and condition order; do not let someone solve the same task in one condition and bring its solution into another. Use equivalent disjoint tasks where necessary.
3. Log every human action with stage, duration, purpose, and resulting change. Record expert work performed before the session. Count independent outcome assessment separately and provide the same assessment protocol to all conditions.
4. Retain all assigned attempts, including timeouts, invalid artifacts, failed setup, and incomplete research. Distinguish protocol violations from incorrect scientific conclusions.
5. Blind assessors to condition where feasible and document remaining cues. Apply an executable validity gate before scoring quality; independently inspect whether the artifact supports its claims.

## Expected artifact and success criterion

Produce an assignment table, complete effort-and-cost ledger, intervention log, and task-level outcomes linked to inspectable artifacts. Report valid-completion rate, task-specific quality, total expert time, elapsed time, and cost separately. Compare paired or grouped observations according to the assignment design; repeated ratings of one output do not increase the number of independent tasks.

Declare success as a prespecified improvement in valid outcomes at the matched limits, or reduced total cost at a prespecified equivalent-quality threshold. A favorable survey rating alone satisfies neither criterion. Small pilots can reveal intervention overhead and logging problems without establishing population-wide benefits. The [existing local reports](../reproducibility.md) demonstrate bounded artifact reporting; they contain no human–agent productivity experiment.
