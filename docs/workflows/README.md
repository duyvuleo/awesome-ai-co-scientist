# From a research question to an evaluation protocol

[← Start here](../start-here.md) · [Repository overview](../../README.md) · [Evaluation guide](../evaluation-guide.md) · [Local catalog CLI](../cli.md)

These recipes turn recurring evidence gaps into bounded studies. Each defines inputs, controls, outputs, and interpretation limits. They are proposed protocols; only the separately linked, dated [component reports](../reproducibility.md) contain execution results from this repository.

| Recipe | Question | First useful artifact | Execution scope |
| --- | --- | --- | --- |
| [Evaluator integrity](evaluator-integrity.md) | Does a score remain meaningful when candidate outputs are invalid? | A control-fixture ledger with independent validity decisions. | Starts from existing local component reports; an extended isolation study requires additional implementation. |
| [Idea to experiment](idea-to-experiment.md) | Do promising proposals lead to valid executed outcomes? | A frozen idea-to-outcome protocol that retains unsuccessful attempts. | Planning can be local; a prospective model study needs its own resources and budget. |
| [Human–AI collaboration](human-ai-collaboration.md) | Where does human intervention improve results at a matched total budget? | A comparison protocol with task assignment and human-effort accounting. | Planning can be local; recruitment and model execution are separate study activities. |

Choose a recipe, inspect candidate systems with the [CLI](../cli.md), then create a [study pack](../study-packs.md). For example, from the repository root:

```bash
python3 scripts/study_pack.py create --recipe evaluator-integrity --resources agentic-scientist-system --output .local/my-first-study
python3 scripts/study_pack.py validate .local/my-first-study
```

The recipe IDs are `evaluator-integrity`, `idea-to-experiment`, and `human-ai-collaboration`. Creating or validating a pack does not execute a system, spend an API budget, or establish a result. Replace placeholders and review the protocol before running any experiment.

Keep the existing dated reports unchanged. A new attempt needs its own inputs, source pin, environment, costs, failure record, and conclusion. Use the [contribution guide](../../CONTRIBUTING.md) when sharing a result, including negative results or corrections.
