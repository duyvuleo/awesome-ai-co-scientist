# Getting started

[← Repository overview](../README.md) · [Evaluation guide](evaluation-guide.md) · [Workflow recipes](workflows/README.md) · [Local catalog CLI](cli.md)

Use the catalogs to select a system, examine its evidence, and define an evaluation.

## Choose your starting point

| Question | Reading | Suggested output |
| --- | --- | --- |
| Understand the field for a reading group | [Cross-paper synthesis](research-synthesis.md), then two linked primary studies | A one-page comparison of their question, human roles, evaluation, and unresolved gap. |
| Choose a system to inspect or extend | [Capability and evidence matrix](capability-matrix.md) and [Systems](systems.md) | A two-system shortlist with one required capability, its source, and one unresolved dependency per system. |
| Test whether an apparent improvement is valid | [Evaluator-integrity recipe](workflows/evaluator-integrity.md) | A fixture table that separates accepted valid outputs, rejected invalid outputs, and evaluator failures. |
| Study whether good proposals become good research | [Idea-to-experiment recipe](workflows/idea-to-experiment.md) | A protocol linking every selected idea to its baseline, executed outcome, modifications, and failures. |
| Measure the value of human guidance | [Human–AI collaboration recipe](workflows/human-ai-collaboration.md) | A matched-budget comparison plan with a complete human-effort ledger. |
| Contribute without running an agent | [Contribution guide](../CONTRIBUTING.md) and [community roadmap](community-roadmap.md) | A sourced correction, missing comparison cell, or carefully scoped report of a failed attempt. |

## A local example

Run these commands from a repository checkout using Python 3.10+. They search local data and create a study plan without downloading systems or calling model APIs.

**1. Define the question.** For example: can the evaluator distinguish feasible solutions from invalid outputs with high scores?

```bash
python3 scripts/explore.py search verification --kind system --format markdown
```

**2. Compare candidates.** Check capabilities, sources, code availability, and limitations:

```bash
python3 scripts/explore.py show agentic-scientist-system
python3 scripts/explore.py compare agentic-scientist-system scientistone-system --format markdown
```

This comparison describes documented capabilities, not relative performance. See the [CLI guide](cli.md) for filters and exports.

**3. Examine a recorded failure.** In the [circle-packing report](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md), the evaluator accepted a nonfinite coordinate. A separate invalid packing returned a score with `correct=false`. These component observations motivate checking validity before comparing scores; they do not characterize every system run.

**4. Prepare a study plan.**

```bash
python3 scripts/study_pack.py create --recipe evaluator-integrity --resources agentic-scientist-system --output .local/my-first-study
python3 scripts/study_pack.py validate .local/my-first-study
```

Complete the task, acceptance criteria, resource limits, and independent check in the generated files. The [study-pack guide](study-packs.md) describes required fields and validation limits.

The output is a protocol, not an executed experiment.

## Run a component check

The [component reports](reproducibility.md) provide source pins, inputs, commands, and limitations. Citation-F1 requires only the standard library; circle packing also requires the documented NumPy version. Follow each report’s acquisition and execution steps, and save new outputs separately from the dated records.

Both investigations used no model/API calls; local hardware and energy costs were unmeasured. A full research campaign requires a separate protocol and budget covering model access, compute, and human effort.

Report the executed component, failures, independent checks, and untested claims using the [evaluation guide](evaluation-guide.md).
