## Recipe: idea to experiment

**Question to adapt:** Under a fixed resource budget, which proposed ideas reach independently checked experimental outcomes?

1. Choose a bounded task with public inputs, a meaningful baseline, a held-out evaluation, and an independently specified success criterion. Record data provenance and permitted external information. Freeze the task and evaluator before evaluating ideas.
2. Declare the source of ideas. For the zero paid API budget, use manually authored ideas, existing public artifacts, or a separately installed local model within declared hardware limits. A replay of published ideas does not test a system's ability to generate new ideas.
3. Register all candidate ideas before implementation, their falsifiable claims, available evidence, and selection rules. Define the unit of analysis: idea, implementation attempt, completed experiment, or system run. Preserve ideas that fail selection or implementation.
4. Declare comparisons such as the original baseline and a simple manual change. Match data, evaluator, hardware, search attempts, time, and human intervention as closely as possible; record unavoidable differences. Separate development feedback from held-out evaluation.
5. Execute the declared number of attempts and seeds, applying the same stopping rule. Record transitions from proposed to selected, implemented, executable, valid, and supported. Report implementation failures and evaluator failures separately from negative experimental findings.
6. Check every claimed improvement with independent metrics and a baseline rerun. Report individual trials and uncertainty appropriate to the sample size. Test the most plausible alternative explanation with a declared ablation when resources permit; otherwise record it as unresolved.

**Suggested artifacts:** task specification, frozen idea ledger and evaluator, baseline configuration, per-attempt records, seeds, implementation revisions, sanitized outputs, independent metric calculations, and selection decisions. Record whether the complete upstream workflow or only a manual replay was executed.

**Completion boundary:** a successful local implementation is not proof of scientific novelty. Compare experimental outcomes only when tasks, budgets, selection, human help, and evaluation conditions permit it; a single demonstration cannot estimate a general success rate.
