# Agentic Scientist: circle-packing baseline and evaluator

**Executed 2026-10-22 · Local component reproduction · Baseline reproduced; one invalid-input control failed.**

The released baseline produced a radius sum of **0.9597642169962064**. Its 26 returned entries satisfied an independent geometric check at absolute tolerance `1e-6`; two entries had zero radius. The example evaluator rejected ordinary overlaps, out-of-bounds centers, negative radii, the wrong number of circles, and a misreported score. It nevertheless accepted a center containing `NaN`. These results characterize this pinned example's behavior, not the performance of the autonomous research system.

## Source and question

We used [SakanaAI/AI-Scientist-v3 at `df8313889a004f8a44a472e19a833cd547bb828a`](https://github.com/SakanaAI/AI-Scientist-v3/tree/df8313889a004f8a44a472e19a833cd547bb828a). The [example task](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/examples/circpack/task.md) asks for 26 non-overlapping circles inside a unit square while maximizing their radius sum. The inspected [baseline](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/examples/circpack/program_0/src/program.py) constructs fixed centers and reduces radii to avoid overlap. The inspected [evaluator](https://github.com/SakanaAI/AI-Scientist-v3/blob/df8313889a004f8a44a472e19a833cd547bb828a/examples/circpack/evaluate.py) checks feasibility and writes separate correctness and score files.

We asked whether the public baseline runs locally, whether its reported score agrees with an independent calculation, and whether invalid candidate outputs are rejected. This is an evaluator-boundary investigation using a released baseline and deliberately constructed controls. It is not an attempt to reproduce the paper's optimization results.

## What ran

1. Downloaded a public GitHub archive pinned to the commit above, verified its SHA-256, and verified the five inspected source files individually. The [machine-readable record](results.json) contains all hashes.
2. Ran the unmodified baseline and the unmodified evaluator's command-line entry point. The runner also loaded their inspected functions directly for controlled input perturbations.
3. Independently recomputed the radius sum with `math.fsum`, containment margins with scalar arithmetic, and every pairwise clearance with `math.hypot`. This independent check explicitly requires finite numbers.
4. Executed the official evaluator again on a synthetic program returning 26 mutually overlapping circles of radius `0.1`. No agent, coding model, training job, or search process ran.

The environment was Python **3.14.7**, NumPy **2.4.2**, Darwin **25.6.0**, ARM64, with 11 logical CPUs available. The evaluator subprocesses limited numerical-library threads to one. The deterministic baseline does not sample randomness, so no random seed is applicable. NumPy matches the example's requirements; SciPy was not installed because neither inspected execution path imports it. This is not a full environment installation.

## Observed results

| Case | Upstream result | Independent interpretation |
|---|---|---|
| Released baseline | Accepted; score `0.9597642169962064` | Same recomputed score; feasible within `1e-6` |
| Two centers made identical | Rejected | Overlap confirmed |
| Center moved to `(2, 2)` | Rejected | Outside square |
| One negative radius | Rejected | Invalid radius |
| Only 25 circle entries | Rejected | Wrong shape |
| Reported score increased by 1 | Rejected | Score does not match radii |
| One center changed to `(NaN, NaN)` | **Accepted** | **Invalid-input control failed**: nonfinite coordinates |

For the baseline, the minimum boundary clearance was `0.0`; the minimum pairwise clearance was approximately `-2.78e-17`, within the declared floating-point tolerance. Two radii were exactly zero, so this establishes feasibility under the released nonnegative-radius checks, not the construction of 26 positive-radius circles.

The separate overlapping-circle command-line run returned **exit code 0**, wrote **`correct: false`**, and still wrote **`combined_score: 2.6`**. The number is an output of aggregation, not a valid achieved packing score. A consumer must read the correctness artifact before using the score. We did not test whether the larger orchestration pipeline already enforces that requirement.

The `NaN` behavior is consistent with the inspected comparisons: the validator does not first reject nonfinite centers, and the relevant comparisons with `NaN` do not evaluate to true. This is a finding about the pinned example validator; it does not establish an effect on any published result or sealed evaluation run. We left upstream code unchanged.

## Runtime and cost

The investigation took **0.492 seconds** after dependencies were available, excluding source download and installation. The official baseline and overlap subprocesses took **0.238** and **0.193 seconds**, respectively. These are single-run wall times, not performance benchmarks. The upstream solution timeout was 300 seconds; our outer subprocess timeout was 30 seconds.

**Model/API cost: USD 0**, because no model API was invoked; cloud GPU usage was zero. Local hardware and energy costs were not measured. This cost does not estimate an autonomous Agentic Scientist run or the effort required to prepare this report.

## Reproduce

Run from this collection's repository root. Source acquisition and execution are separate. The fetch command downloads only a pinned public archive and verifies the inspected files; it does not execute upstream code. The run command executes the inspected baseline and evaluator locally.

```bash
python3 -m venv .local/repro-sources/venv
.local/repro-sources/venv/bin/python -m pip install --only-binary=:all: numpy==2.4.2
.local/repro-sources/venv/bin/python scripts/reproduce_circle_packing.py --fetch-only
.local/repro-sources/venv/bin/python scripts/reproduce_circle_packing.py
```

Reruns write to `.local/repro-runs/circle-packing/`, leaving the reviewed record intact. The recorded run used:

```bash
.local/repro-sources/venv/bin/python scripts/reproduce_circle_packing.py --output reports/reproducibility/2026-10-22-agentic-scientist-circle-packing
```

Inspect [the runner](../../../scripts/reproduce_circle_packing.py) and [source acquisition helper](../../../scripts/reproduce_common.py) before execution. The helper refuses changed source hashes. GitHub may eventually change archive packaging without changing individual files; in that case acquisition stops for review rather than silently accepting a different archive.

## Evidence and limits

- [Results, source hashes, configuration, and control outcomes](results.json)
- [Baseline coordinates, radii, and score](packing.json)
- [Official baseline metrics](baseline-metrics.json), [correctness](baseline-correct.json), and [sanitized combined execution log](baseline-stdout.log)
- [Official overlap metrics](overlap-metrics.json), [correctness](overlap-correct.json), and [sanitized combined execution log](overlap-stdout.log)

Reproduced: execution of the released fixed baseline, agreement of its reported sum with an independent calculation, its feasibility under the stated tolerance, and the listed evaluator behaviors. **Untested:** hypothesis generation, search improvements, agent orchestration, sealed-evaluation isolation, paper writing, scientific novelty, and published numerical claims. No end-to-end scientist replication is claimed.

[Back to reproducibility reports](../../../docs/reproducibility.md)
