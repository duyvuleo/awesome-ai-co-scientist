# Evaluation protocols

[← Start here](../start-here.md) · [Repository overview](../../README.md) · [Evaluation guide](../evaluation-guide.md) · [Local catalog CLI](../cli.md)

These proposed protocols specify inputs, controls, outputs, and interpretation limits. Executed results are documented separately in the [component reports](../reproducibility.md).

| Protocol | Question | Output | Execution scope |
| --- | --- | --- | --- |
| [Evaluator integrity](evaluator-integrity.md) | Does a score remain meaningful when candidate outputs are invalid? | A control-fixture ledger with independent validity decisions. | Starts from existing local component reports; an extended isolation study requires additional implementation. |
| [Idea to experiment](idea-to-experiment.md) | Do promising proposals lead to valid executed outcomes? | A frozen idea-to-outcome protocol that retains unsuccessful attempts. | Planning can be local; a prospective model study needs its own resources and budget. |
| [Human–AI collaboration](human-ai-collaboration.md) | Where does human intervention improve results at a matched total budget? | A comparison protocol with task assignment and human-effort accounting. | Planning can be local; recruitment and model execution are separate study activities. |

Choose a recipe, inspect candidate systems with the [CLI](../cli.md), then create a [study pack](../study-packs.md). For example, from the repository root:

```bash
python3 scripts/study_pack.py create --recipe evaluator-integrity --resources agentic-scientist-system --output .local/my-first-study
python3 scripts/study_pack.py validate .local/my-first-study
```

Recipe IDs are `evaluator-integrity`, `idea-to-experiment`, and `human-ai-collaboration`. Pack creation and validation are offline planning steps. Complete and review the protocol before execution.

Preserve dated reports. Document each new attempt’s inputs, source revision, environment, costs, failures, and conclusions following the [contribution guide](../../CONTRIBUTING.md).
