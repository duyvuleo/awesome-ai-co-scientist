## Recipe: human–AI collaboration

**Question to adapt:** Does assistance improve a specified research task after accounting for researcher effort, verification, and errors?

1. Select a bounded task and rubric with inspectable references, such as finding supporting evidence or translating a proposal into an experiment plan. Specify what correctness, completeness, and unacceptable errors mean before comparing conditions.
2. Declare conditions: an unassisted baseline and assisted work using an available local model or existing public outputs within the zero paid API budget. An offline replay evaluates interaction with those outputs, not the live hosted system. Describe participant expertise without personal identifiers.
3. Assign comparable tasks and counterbalance condition order where feasible. Avoid showing the same answer first in one condition and then treating recall as an assistance gain. Predeclare sample size, unit of analysis, timing boundaries, allowed tools, and stopping rule.
4. Log human work by stage: initial task definition, prompting or steering, verification, correction, and final decision. Record interventions and rejected suggestions. Do not report tool runtime alone as the total time required for the task.
5. Use condition-blind assessment when feasible, an independently specified rubric, and a procedure for disagreements. Measure final-task quality and consequential errors alongside time. Keep subjective usefulness separate from measured correctness and productivity.
6. Report per-task outcomes, failures, order effects, reviewer disagreement, and the limits of the sample. A self-study is descriptive; do not generalize it to a population or infer a causal productivity effect without a suitable design. Only share participant material for which you have permission.

**Suggested artifacts:** public task inputs, frozen rubrics, assignment schedule without participant identifiers, sanitized intervention summaries, timing definitions, scores with adjudication notes, and uncertainty calculations. Prefer structured observations to raw private conversations.

**Completion boundary:** positive experience, quality ratings, time saved, and scientific correctness are different outcomes. State which were measured and which remain untested; do not use an assistant's self-evaluation as the sole correctness check.
