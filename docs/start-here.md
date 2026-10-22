# Start with a question, leave with a research artifact

[← Repository overview](../README.md) · [Evaluation guide](evaluation-guide.md) · [Workflow recipes](workflows/README.md) · [Local catalog CLI](cli.md)

Use this repository to choose a research workflow, inspect its supporting evidence, and design a bounded test. The useful output is a defensible decision or an inspectable experiment—not a longer reading list.

## Choose your starting point

| You want to… | Start with | Produce a small, useful artifact |
| --- | --- | --- |
| Understand the field for a reading group | [Cross-paper synthesis](research-synthesis.md), then two linked primary studies | A one-page comparison of their question, human roles, evaluation, and unresolved gap. |
| Choose a system to inspect or extend | [Capability and evidence matrix](capability-matrix.md) and [Systems](systems.md) | A two-system shortlist with one required capability, its source, and one unresolved dependency per system. |
| Test whether an apparent improvement is valid | [Evaluator-integrity recipe](workflows/evaluator-integrity.md) | A fixture table that separates accepted valid outputs, rejected invalid outputs, and evaluator failures. |
| Study whether good proposals become good research | [Idea-to-experiment recipe](workflows/idea-to-experiment.md) | A protocol linking every selected idea to its baseline, executed outcome, modifications, and failures. |
| Measure the value of human guidance | [Human–AI collaboration recipe](workflows/human-ai-collaboration.md) | A matched-budget comparison plan with a complete human-effort ledger. |
| Contribute without running an agent | [Contribution guide](../CONTRIBUTING.md) and [community roadmap](community-roadmap.md) | A sourced correction, missing comparison cell, or carefully scoped report of a failed attempt. |

## A ten-minute local path

The commands below use Python 3.10+ and the standard library. Run them from a checkout of this repository. They read local catalogs and create a local study plan; they do not download or execute research systems or call model APIs. The time allocation is a suggested reading exercise, not a measured completion time.

**Minutes 0–2: state the question.** For example: “Before I compare optimization agents, can I distinguish feasible solutions from high scores on invalid outputs?” Search the collection:

```bash
python3 scripts/explore.py search verification --kind system --format markdown
```

**Minutes 2–5: inspect a candidate and an alternative.** Read the evidence basis, code availability, and unresolved limits—not only the capability description:

```bash
python3 scripts/explore.py show agentic-scientist-system
python3 scripts/explore.py compare agentic-scientist-system scientistone-system --format markdown
```

The comparison is source-based. It does not establish that either system performs better on your task. Full command options and export formats are in the [CLI guide](cli.md).

**Minutes 5–8: inspect an observed failure.** Read the [circle-packing report](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md). Its pinned evaluator accepted a nonfinite coordinate; a separate invalid packing emitted a score while declaring `correct=false`. Write down the implication for your proposed test: validity must be checked before scoring. These observations concern the example evaluator, not every run of the complete system.

**Minutes 8–10: create the plan you would review before execution.**

```bash
python3 scripts/study_pack.py create --recipe evaluator-integrity --resources agentic-scientist-system --output .local/my-first-study
python3 scripts/study_pack.py validate .local/my-first-study
```

Open the generated files and replace planning placeholders with a specific task, acceptance criteria, resource limits, and independent check. See [study packs](study-packs.md) for the file contract and validation limits. A structurally valid plan is not evidence that an experiment ran or that its science is valid.

**Your result:** a sourced candidate, one concrete failure mode, and a local protocol to refine. No result should be marked “reproduced” at this stage.

## Take the next step at the right cost

For a first execution, the [recorded component reports](reproducibility.md) provide pinned sources, inspected runners, fixtures, commands, and observed limitations. The citation-F1 investigation needs only the standard library; the circle-packing investigation also needs the documented NumPy version. Their acquisition and execution steps are separate. Review those steps before running them and save fresh outputs separately from the dated records.

Both recorded investigations used zero model/API calls. Local compute, setup effort, and energy are still resources; their hardware and energy costs were not measured. A complete model-driven research campaign is a different experiment requiring its own model access, compute allowance, evaluation plan, and approved budget. It is not part of this local starting path.

When sharing a result, state exactly which component ran, what failed, what the independent check established, and what remains untested. The [evaluation guide](evaluation-guide.md) turns those distinctions into a reusable reporting protocol.
