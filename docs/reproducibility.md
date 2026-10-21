# Local reproducibility reports

[← Overview](../README.md) · [Capability and evidence matrix](capability-matrix.md) · [Research synthesis](research-synthesis.md)

These reports record **what we executed**, using pinned public source revisions and local inputs. The first two investigations cover deterministic components: a released baseline/evaluator and an isolated scoring method. They do not reproduce a complete autonomous research campaign or the papers' headline results.

## Executed investigations

| Executed | Component and report | Reproduced behavior | Observed limitations |
| --- | --- | --- | --- |
| 2026-10-22 | [Agentic Scientist: circle-packing baseline and evaluator](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) | Baseline radius sum **0.9597642169962064** agrees with an independent geometry and score check. | A NaN coordinate was accepted. An invalid overlap run emitted score **2.6** with `correct=false`; the score alone is not a valid result. |
| 2026-10-22 | [PaperOrchestra: citation-F1 scorer](../reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) | The unchanged scoring-method body agrees with independent formulas on **32/32** enumerated cases; ten further scenarios inspect input assumptions. | Unresolved IDs are excluded in the tested caches; inconsistent priority membership is accepted; non-iterable IDs raise `TypeError`. |

Both runs used **zero model/API calls and zero cloud GPU hours**. Model/API charges were **USD 0**; local hardware and energy costs were not measured. Their recorded wall times are individual component measurements, excluding acquisition and installation, and do not estimate complete research-system costs.

## How to interpret the reports

- **Source inspection:** establishes what a particular paper or implementation says. It is not execution evidence.
- **Component reproduction:** executes a specified public component with recorded inputs and independent checks. The baseline/evaluator and isolated-scorer reports above are in this category.
- **End-to-end execution:** would require the complete workflow, its external services, environment, and artifacts. Neither report makes this claim.
- **Scientific-result reproduction:** would require a comparable experimental protocol, data, evaluation, and selection procedure. Neither report claims to reproduce a published scientific finding.

PaperOrchestra's scorer was extracted as an unchanged Python method from its verified source file. Module initialization, PDF extraction, identifier resolution, model-based prioritization, and paper generation were bypassed. The report records that extraction and its hashes explicitly. Agentic Scientist's report ran the released baseline and example evaluator, including its command-line interface, while leaving the agent orchestration untested.

Each report provides the upstream commit, inspected-file hashes, commands, environment, configuration, runtime, cost basis, observed failures, and explicit untested claims. Linked JSON, fixtures, and sanitized logs let readers inspect the recorded observations. Rerun scripts write to an ignored local directory by default, preserving these dated records.

## Connection to the broader evidence

The [comparison matrix](capability-matrix.md) describes system capabilities from primary sources. These reports add narrow execution evidence for selected components. The [synthesis](research-synthesis.md#3-verification-must-preserve-the-question-being-tested) explains why validation results, metric values, and scientific claims must remain distinct. An invalid-input result here does not establish that a published experiment was affected or that the full system lacks additional protections.
