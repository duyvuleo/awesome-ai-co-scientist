# Reuse the catalog and comparison data

[← Overview](../README.md) · [CLI and exports](cli.md) · [Study packs](study-packs.md)

The public JSON records can support a reading-group shortlist, a local search interface, or a comparative research analysis. They contain curated observations about primary sources, not an execution log or a universal ranking. Preserve their dates, citations, and evidence limitations when reusing them.

## Files and identifiers

| File | Contents | Identifier |
| --- | --- | --- |
| [papers.json](../data/papers.json) | Research publications and surveys | `id` |
| [systems-tools.json](../data/systems-tools.json) | Integrated systems and supporting tools | `id` |
| [benchmarks.json](../data/benchmarks.json) | Evaluation resources | `id` |
| [comparisons.json](../data/comparisons.json) | Seven source-backed dimensions for every cataloged system | `systems[].system_id` joins to a system's `id` |
| [featured.txt](../data/featured.txt) | Selected reading entry points | Catalog IDs, one per line; comments start with `#` |

The first three files are JSON arrays. IDs are unique across those arrays. Paper and software records can describe the same research family; `related` contains explicit catalog IDs linking them. Counting records does not count independent scientific discoveries or unique research programs.

## Catalog field meanings

| Field | Meaning |
| --- | --- |
| `id`, `name` | Stable lookup ID and displayed resource name. |
| `kind`, `category`, `tags` | Artifact type, broad workflow category, and descriptive tags. Tags are a curated vocabulary, not standardized capability scores. |
| `year`, `date` | The represented publication/release date. `date` has either year or day precision; do not manufacture a month/day for a year-only record. |
| `url`, optional `code_url` / `paper_url` | Canonical resource and explicitly recorded supporting links. Link presence does not certify runnable or complete code. |
| `summary` | Original concise annotation with its contribution and evidence boundary. |
| `evidence` | Source status: `preprint`, `peer-reviewed`, or `project`. This is distinct from the basis of a comparison cell and from independent reproduction. |
| `sources` | Primary URLs used to support the record. |
| `checked` | Date of source inspection; not the publication date, execution date, or proof of current link availability. |
| Optional `related`, `status` | Linked catalog IDs and a source-supported availability or status note. |

Sort by recorded date, newest first. Within a year, fully dated records precede year-only records; the latter are explicitly uncertain, not assumed to have been released earlier. Names and IDs resolve ties.

## Comparison field meanings

`comparisons.json` is a versioned object with `schema_version`, `reviewed`, `scope`, and `systems`. Each system has seven dimensions: `human_involvement`, `hypothesis_generation`, `experiment_execution`, `memory`, `verification`, `available_code`, and `evaluation_setting`.

Each cell contains `text`, `sources`, and `basis`. The basis is `paper-report`, `project-documentation`, `code-inspection`, or `not-established`. Source URLs map to that system's source records, which include a human-readable `label` and section/file `locator`. Keep these source records with exported cells. `limitations` and `checked` belong to the system comparison as a whole.

“Not established” means the examined sources do not support a stronger claim. Static code inspection is not execution. A paper's empirical result remains bounded by its study setting, and a later implementation can differ from that setting.

## Export without writing a parser

The [offline CLI](cli.md) preserves source metadata in JSON and encodes list-valued CSV cells as JSON, allowing source locators and commas to survive round trips.

```bash
python3 scripts/explore.py search --kind paper --format json
python3 scripts/explore.py search --kind tool --format csv
python3 scripts/explore.py compare agentic-scientist-system sciencebuddy-system --format json
```

For direct use in Python, this reads only local files:

```python
import json
from pathlib import Path

root = Path(".")  # Run from the repository root.
records = [
    record
    for name in ("papers.json", "systems-tools.json", "benchmarks.json")
    for record in json.loads((root / "data" / name).read_text())
]
by_id = {record["id"]: record for record in records}
print(by_id["agentic-scientist"]["sources"])
```

Run `python3 scripts/validate.py` and `python3 scripts/render.py --check` to check catalog structure, relationships, local navigation, and generated views. They do not independently verify scientific statements. The [study-pack validator](study-packs.md) checks a different record format and local artifact integrity; the original dated reproducibility reports retain their own recorded JSON format.

## Attribution and versioning

Original catalog content and scripts use [CC0 1.0](../LICENSE). Linked papers, software, and datasets retain their own licenses. Cite primary papers for scientific claims. When citing this collection or reusing its comparative analysis, use [CITATION.cff](../CITATION.cff) and record the Git commit you used, since the catalog evolves. No DOI or archived release is claimed.
