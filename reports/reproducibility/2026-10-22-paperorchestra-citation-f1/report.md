# PaperOrchestra: citation-F1 scoring boundary

**Executed 2026-10-22 · Isolated scoring-method reproduction · Formula agreement confirmed; input assumptions exposed.**

PaperOrchestra's inspected citation-scoring method agreed with independent precision, recall, F1, and priority-recall calculations for all **32 subsets** of a five-identifier generated-reference universe. Ten additional named scenarios exercised duplicates, unresolved references, legacy caches, empty input, and malformed caches. This reproduces one deterministic scorer's behavior. The complete module and paper-generation pipeline were not imported, installed, or run.

## Source and question

We used [google-research/paper-orchestra at `ca1b3fa01c2970fc7cda32d16245db38d57b3f56`](https://github.com/google-research/paper-orchestra/tree/ca1b3fa01c2970fc7cda32d16245db38d57b3f56), specifically [`ReferenceF1V1Evaluator.evaluate_from_data`](https://github.com/google-research/paper-orchestra/blob/ca1b3fa01c2970fc7cda32d16245db38d57b3f56/autoraters/citation_f1.py#L262). The surrounding source resolves reference titles to Semantic Scholar identifiers and uses a model to classify ground-truth citations as P0 or P1. The selected method consumes the resulting cached identifiers and computes set-overlap metrics.

We asked whether the arithmetic matches an independent formulation and what its denominator includes. An overlap score can be correct for resolved identifiers while leaving reference extraction, identifier matching, priority classification, and citation validity untested.

## What ran

We verified the public archive and the source file by SHA-256. We parsed the file into Python's abstract syntax tree and selected the exact `evaluate_from_data` method without changing its body. We then compiled that unchanged method node with only its standard-library dependencies (`os`, `json`, and the `Dict` type annotation) and supplied a temporary log directory as `self.log_folder`. No replacement was made inside the metric computation. The [results](results.json) record the source-file hash, exact method-source hash, method-AST hash, and source line range.

**Module initialization was bypassed.** The full module imports model/PDF utilities, loads environment configuration, and prints an API-key variable on import. We neither imported that module nor executed those initialization statements. This separation allows scoring-only execution without reading credentials or calling external services; it does not establish whole-module or full-pipeline compatibility.

Inputs were explicitly synthetic identifiers `A`, `B`, `C`, `D`, and `X`. The main ground truth was `{A, B, C, D}`, with P0 `{A, B}` and P1 `{C, D}`. We enumerated every subset of `{A, B, C, D, X}` as generated output and compared all five returned metrics to a separately written count formula. Eight well-formed or legacy named scenarios also had explicit independent expected values. The remaining two named scenarios examined invalid cache handling.

The local runtime was Python **3.14.7**, Darwin **25.6.0**, ARM64, with 11 logical CPUs available. The scorer uses the Python standard library; no third-party dependency was imported by this runner. All inputs were deterministic.

## Observed results

| Scenario | Precision | Recall | F1 | P0 recall | P1 recall |
|---|---:|---:|---:|---:|---:|
| Exact match: `A, B, C, D` | 1 | 1 | 1 | 1 | 1 |
| P0 only: `A, B` | 1 | 0.5 | 0.6667 | 1 | 0 |
| Partial plus extra: `A, C, X` | 0.6667 | 0.5 | 0.5714 | 0.5 | 0.5 |
| Duplicates: `A, A, B, A` | 1 | 0.5 | 0.6667 | 1 | 0 |
| `A, B` plus `gen_NA`, empty string, and null | 1 | 0.5 | 0.6667 | 1 | 0 |
| Empty generated identifiers | 0 | 0 | 0 | 0 | 0 |
| Both inputs empty | 0 | 0 | 0 | 0 | 0 |

All **32/32** enumerated valid-identifier cases agreed with the independent formulas within absolute tolerance `1e-12`. The legacy-cache scenario confirmed that duplicate references are collapsed, P0 takes precedence over P1 for the same identifier, and the `gt_NA` unresolved placeholder is excluded. These are expected behaviors of a scorer defined over resolved unique identifiers.

The denominator sensitivity matters when interpreting results: the named unresolved-reference scenario had exactly the same metrics as `A, B` alone. The scorer therefore measures overlap among included resolved identifiers; it does not penalize every raw unresolved citation in these cached inputs. This result does **not** measure the real pipeline's resolution failure rate, demonstrate fabricated citations, or establish bias in a published benchmark. Resolution coverage would need to be reported separately to evaluate those questions.

Two invalid-cache controls exposed additional assumptions:

- **Inconsistent priority membership:** ground truth `all_ids=[A]` with `p0_ids=[A, X]` and generated `all_ids=[X]` returned overall F1 `0` and P0 recall `0.5`. The method accepted the contradictory cache; it is not a schema validator. We did not establish whether upstream cache generation can produce this inconsistency.
- **Non-iterable identifiers:** generated `all_ids=null` raised `TypeError: 'NoneType' object is not iterable`. This malformed-input outcome was observed and recorded; it is not a successful score or evidence of graceful input validation.

## Runtime and cost

The scoring investigation took **0.048 seconds**, excluding source download, for 42 invocations: 32 enumerated cases and 10 named scenarios. This single wall-time measurement includes local parsing and temporary-file work, and is not a pipeline performance benchmark.

**Model/API cost: USD 0**, because neither a model API nor Semantic Scholar was called. Cloud GPU usage was zero. Local hardware and energy costs were not measured. These figures do not estimate PaperOrchestra paper-generation cost or the effort required to prepare the report.

## Reproduce

Run from this collection's repository root. An isolated environment is recommended; the scorer itself needs no installed third-party packages.

```bash
python3 -m venv .local/repro-sources/venv
.local/repro-sources/venv/bin/python scripts/reproduce_citation_f1.py --fetch-only
.local/repro-sources/venv/bin/python scripts/reproduce_citation_f1.py
```

The first command that invokes the runner acquires and verifies the pinned public source without executing it. The second executes only the selected scoring method and writes to `.local/repro-runs/citation-f1/`. The recorded run used:

```bash
.local/repro-sources/venv/bin/python scripts/reproduce_citation_f1.py --output reports/reproducibility/2026-10-22-paperorchestra-citation-f1
```

Inspect [the runner](../../../scripts/reproduce_citation_f1.py) and [acquisition helper](../../../scripts/reproduce_common.py) before execution. The helper refuses source or archive hash changes. The source pin is mandatory; the AST selection is not a general-purpose safe executor for arbitrary source files.

## Evidence and limits

- [Results, extraction hashes, environment, costs, and named outcomes](results.json)
- [Ten named synthetic input fixtures](fixtures.json)
- [All 32 enumerated valid-identifier outputs](exhaustive-valid-id-cases.json)
- [Sanitized scorer stdout](stdout.log)

Reproduced: the selected method's set-based arithmetic, duplicate handling, legacy-cache behavior, and the listed malformed-input outcomes. **Untested:** PDF reference extraction, title matching, Semantic Scholar identifier accuracy, model-assigned priority correctness, citation support for manuscript claims, manuscript generation, and published benchmark results. Scorer-only execution cannot establish paper quality or end-to-end reproducibility.

[Back to reproducibility reports](../../../docs/reproducibility.md)
