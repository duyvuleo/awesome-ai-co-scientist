# Plan a study and record its evidence

[← Overview](../README.md) · [Executed reproducibility reports](reproducibility.md) · [Capability matrix](capability-matrix.md)

Use a study pack to turn a research question into a declared comparison, then record exactly what you observed. Each pack contains a procedural recipe, selected catalog resources, and a structured run record. It starts as **planned**, with no implied execution or results.

The generator and validator use Python 3.10+ and the standard library. They run offline. They do not install software, invoke a model, execute upstream code, collect logs, or submit anything. New plans default to an **API budget of USD 0**. Contributors can explicitly record their independently authorized budget and actual charges; changing a record never starts a paid operation. Local hardware, energy, and researcher time still matter.

## Choose a question

| Recipe | What you can investigate | Key control | What it does not establish |
| --- | --- | --- | --- |
| [`evaluator-integrity`](../templates/study/evaluator-integrity.md) | Whether a component accepts valid inputs, rejects invalid inputs, and computes its stated metric | Independent calculation, valid boundaries, deliberately invalid candidates | Full-system reliability or whether a published experiment was affected |
| [`idea-to-experiment`](../templates/study/idea-to-experiment.md) | Which declared ideas become valid experiments under a fixed budget | Baseline reruns, frozen evaluator, complete attempt ledger | Novelty or live idea-generation ability when replaying existing ideas |
| [`human-ai-collaboration`](../templates/study/human-ai-collaboration.md) | Task quality, researcher effort, verification, and errors with assistance | Comparable tasks, unassisted condition, declared rubric and order | A general or causal productivity gain from a single self-study |

These are study-design starting points. Select only methods suitable for your task. A catalog entry or recipe is not an endorsement that a system is safe, accessible, or suitable for execution.

## Create a pack

Run these commands from the repository root. `.local/` is ignored by Git so unfinished local plans do not enter a contribution accidentally.

```bash
python3 scripts/study_pack.py create \
  --recipe evaluator-integrity \
  --resources agentic-scientist-system \
  --output .local/studies/evaluator-check

python3 scripts/study_pack.py validate .local/studies/evaluator-check
```

The initial check should say **Valid planned study pack**. This means its structure is valid; the protocol can still contain unanswered fields. It is not a readiness check or execution certificate.

You can select multiple **system or tool IDs** from `data/systems-tools.json`. Paper and benchmark IDs are not execution targets in this initial format. `--systems` is an alias for `--resources`, with the same behavior.

```bash
python3 scripts/study_pack.py create \
  --recipe evaluator-integrity \
  --resources agentic-scientist-system paperorchestra-tool \
  --output .local/studies/component-comparison

python3 scripts/study_pack.py create \
  --recipe idea-to-experiment \
  --resources openresearch-system \
  --output .local/studies/idea-replay

python3 scripts/study_pack.py create \
  --recipe human-ai-collaboration \
  --resources researchstudio-tool \
  --output .local/studies/collaboration-plan
```

Selecting a resource means you intend to investigate it; it does not confirm code availability, hardware feasibility, or a local execution path. Choose fewer resources if you can only run a narrower study. Creation refuses an existing output directory, including an empty one. Use a fresh directory for a new study.

## Complete the plan before executing

Read the generated `protocol.md` and edit `run-record.json`. The JSON `protocol` object is the structured record; use the Markdown protocol for detailed rationale. Preserve your pre-execution protocol as a separate artifact if you later change it.

| Field | Record before running |
| --- | --- |
| `question`, `declared_claim` | A bounded question and the claim your observations could support or refute |
| `human_role` | Who defines tasks, selects ideas, changes code, checks evidence, and makes decisions; avoid personal identifiers |
| `unit_of_analysis`, `sample_size` | What counts as one observation and how many you intend to collect |
| `baselines`, `controls` | Named comparisons and invalid or alternative cases; explain an inapplicable comparison explicitly |
| `configuration` | Public, portable configuration, without credentials, personal data, or private filesystem paths |
| `seeds`, `seed_policy` | Declared integer seeds; for deterministic work, use an empty list and explain why |
| `success_criteria`, `stopping_rule` | Metric and validity requirements, how failures count, and when work stops |
| `exclusions` | Components, data, scientific claims, and generalizations outside the study |
| `budget` | `paid_api_usd` defaults to `0`; declare any authorized change before execution, alongside wall-time, local-compute, and human-time limits |

`resources` preserves each selected entry's name, ID, kind, canonical URL, sources, and original `catalog_checked` date. That date is copied from the catalog; creating a pack does **not** recheck those sources. Keep the snapshot as provenance even if the catalog later changes.

Until execution occurs, leave `execution`, `actual.cost`, `actual.results`, `actual.failures`, and `actual.claim_outcomes` as `null`, and `actual.artifacts` as `[]`. Unknown cost is not zero, and a planned test is not an observed result.

## Record a completed attempt

After your chosen execution, complete the record and change `status` to `completed`. This includes unsuccessful attempts: record what failed and which claims remain inconclusive or untested. The format uses `completed` to describe a finished record, not a successful scientific result.

Required execution fields are:

- `started_at`, `ended_at`: ISO timestamps with timezones, in chronological order.
- `environment`: an object with nonempty `os`, `runtime`, `hardware`, and `dependencies` descriptions, including relevant versions.
- `commands`: portable commands actually used; `configuration`: the actual configuration object.
- `upstream_versions`: one object per selected resource with `resource_id`, public `url`, `revision_type`, `revision`, and exact executed `scope`. Use `git-commit` with a full 40-character commit or `sha256` with a 64-character source-content hash. A branch name is not a pin. A hash records identity but does not prove source authenticity or execution.
- `data_provenance`: inputs, permissions, and selection procedure; `deviations`: a list describing changes to the frozen protocol, including any budget overruns, or `[]` when none occurred.

Under `actual`, fill:

- `cost`: actual nonnegative `paid_api_usd`, measured `wall_seconds`, `local_compute_hours` and `human_hours` (numeric or `null` if unmeasured), `basis`, and `excluded_costs`. Explain timing and billing boundaries, including why API charges are zero when no model API ran; do not imply unmeasured energy or hardware is free. Any recorded budget overrun requires a deviation note.
- `results`: a nonempty list of observations, each with `observation` and `artifact_paths`.
- `failures`: a list of observed failures, or `[]` when none were observed. Include invalid and unsuccessful attempts, not only retained successes.
- `claim_outcomes`: a nonempty list with `claim`, `outcome`, `scope`, and `artifact_paths`. Outcomes are `supported`, `not-supported`, `inconclusive`, or `not-tested`. Only `not-tested` can omit evidence paths.
- `artifacts`: a nonempty list with `path`, `sha256`, and `description`. Use paths relative to the pack; the files must exist and their hashes must match. Absolute paths, traversal, symlinks, duplicate paths, and the record itself as evidence are rejected.

**Synthetic schema example only:** the following fragments illustrate the shape of an observation and a scoped claim. They are not research findings or a complete valid record. Replace them with actual observations and real artifact references.

```json
{
  "results": [
    {
      "observation": "Synthetic example: an invalid candidate was rejected.",
      "artifact_paths": ["evidence/cases.json"]
    }
  ],
  "claim_outcomes": [
    {
      "claim": "Synthetic example: this specific invalid candidate is rejected.",
      "outcome": "supported",
      "scope": "One declared fixture; no full-system inference.",
      "artifact_paths": ["evidence/cases.json"]
    },
    {
      "claim": "The system produces scientifically novel findings.",
      "outcome": "not-tested",
      "scope": "Outside this component check.",
      "artifact_paths": []
    }
  ]
}
```

After deliberately adding a sanitized artifact, calculate its SHA-256 locally. This prints only the hash, reads one named file, and does not copy or upload anything:

```bash
python3 -c 'import hashlib; from pathlib import Path; print(hashlib.sha256(Path(".local/studies/evaluator-check/evidence/cases.json").read_bytes()).hexdigest())'
python3 scripts/study_pack.py validate .local/studies/evaluator-check
```

See the [executed reports](reproducibility.md) for real examples of bounded claims, independent checks, measured costs, and failures. Their existing report format predates study packs; it is not validated by this command.

## Share useful evidence

Open a [reproduction report](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml) when you executed a specified workflow or component, or an [experience report](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml) for a practical observation, installation obstacle, or unexecuted investigation. For a pull request, follow [CONTRIBUTING.md](../CONTRIBUTING.md) and share only the files necessary to inspect the claim.

Validation checks structure, pinned-revision format, internal references, and local artifact hashes. It cannot verify that commands were run, that a source revision exists upstream, that outcomes follow from the evidence, or that files are free of sensitive information. Review and sanitize every file you choose to publish. The tool never copies raw logs or submits a report automatically.
