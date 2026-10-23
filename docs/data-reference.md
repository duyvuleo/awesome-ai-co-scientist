# Reuse the catalog and comparison data

[← Overview](../README.md) · [CLI and exports](cli.md) · [Study packs](study-packs.md)

The JSON catalogs record primary-source observations. Preserve dates, citations, and limitations when reusing them for search or comparative analysis.

## Files and identifiers

| File | Contents | Identifier |
| --- | --- | --- |
| [papers.json](../data/papers.json) | Research publications and surveys | `id` |
| [systems-tools.json](../data/systems-tools.json) | Integrated systems and supporting tools | `id` |
| [benchmarks.json](../data/benchmarks.json) | Evaluation resources | `id` |
| [comparisons.json](../data/comparisons.json) | Seven source-backed dimensions for every cataloged system | `systems[].system_id` joins to a system's `id` |
| [explorer-taxonomy.json](../data/explorer-taxonomy.json) | Theme aliases, labels, and excluded administrative tags for the visual explorer | Catalog tag strings |
| [featured.txt](../data/featured.txt) | Selected reading entry points | Catalog IDs, one per line; comments start with `#` |

The first three files are JSON arrays with globally unique IDs. `related` links papers and software from the same research family; record counts therefore differ from counts of research programs.

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
| `added_on` | Date first added to this collection (Australia/Sydney); preserved across source checks and corrections. Drives the README’s recent additions. Existing values were recovered from catalog Git history. |
| Optional `related`, `status` | Linked catalog IDs and a source-supported availability or status note. |

The README’s recent additions group records by `paper_url`, falling back to `url`. Groups use the latest member’s `added_on` date, prefer the paper summary, and retain every catalog detail link. Grouping occurs before the eight-work limit.

| Identity | Matching rule |
| --- | --- |
| arXiv | Abstract, HTML, PDF, version, export-host, and arXiv DOI forms match the same identifier. Original citations retain their versions. |
| DOI | Resolver aliases and encoded identifiers use ASCII case-insensitive comparison; distinct DOI suffixes remain separate. |
| GitHub | Repository roots normalize owner/repository case and `.git`. Forks, branches, release paths, and files remain distinct. |
| Other URLs | Remove known tracking parameters; preserve path case, trailing slashes, meaningful queries, and fragment routes. |

Repeated record kinds within a group are ambiguous: all remain separate rather than collapsing distinct systems or benchmarks that cite one paper. Names, `related` links, and shared `sources` do not establish identity. Preprint–journal equivalence and repository renames require verified metadata; they are not inferred. Catalog validation uses the same identity rules to reject duplicates within a kind.

Identifier conventions follow the [arXiv identifier guide](https://info.arxiv.org/help/arxiv_identifier.html), [DOI Handbook](https://www.doi.org/doi-handbook/html/), and [GitHub repository API](https://docs.github.com/en/rest/repos/repos).

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
