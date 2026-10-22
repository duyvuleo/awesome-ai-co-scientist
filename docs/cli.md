# Search and compare locally

[← Overview](../README.md) · [Capability matrix](capability-matrix.md) · [Reproducibility reports](reproducibility.md)

The CLI searches, compares, and exports the local JSON catalogs. It requires Python 3.10+, uses no network or third-party packages, and does not execute listed systems.

From the repository root:

```bash
python3 scripts/explore.py --help
python3 scripts/explore.py search --help
```

## Search the catalog

```bash
# Search titles, IDs, summaries, categories, and tags.
python3 scripts/explore.py search "evidence verification" --limit 5

# List systems with a recorded repository or code link.
python3 scripts/explore.py search --kind system --has-code-link

# Find papers carrying both tags, with publication years from 2025 onward.
python3 scripts/explore.py search --kind paper --tag verification --tag provenance --since-year 2025

# Filter by a recorded source-status label.
python3 scripts/explore.py search --kind benchmark --evidence peer-reviewed --year 2025
```

All filters combine with **AND**. Search text is case-insensitive: each whitespace-separated term must occur somewhere in the combined searchable fields. This is substring matching, not semantic search or relevance ranking. Quote a query containing spaces. Repeated `--tag` arguments require every tag, with case-insensitive exact matching. An unknown tag produces an error; inspect the tags in search output or the [JSON catalogs](../data/) to find the existing vocabulary.

`--year` selects an exact publication/release year; `--since-year` is inclusive. Use one at a time. Results follow the catalog's newest-first order. Year-only dates remain visibly labeled and appear after precisely dated entries from the same year. `--limit` takes a positive integer; the default returns all matches. An empty result is successful and means that no local record matched, not that no such research exists.

`--evidence` accepts `preprint`, `peer-reviewed`, or `project`. These are source-status labels, not quality scores. `--has-code-link` checks for a `code_url` or a GitHub, GitLab, or Bitbucket repository URL in the record's `url`/`sources`. A link can point to supporting code or generated artifacts; it does **not** establish a complete runnable framework, maintenance status, license permissions, or independent reproduction. Read the summary, sources, and system comparison before deciding what to run.

## Inspect a record and follow its relationships

```bash
python3 scripts/explore.py show agentic-scientist
python3 scripts/explore.py show agentic-scientist-system
```

`show` includes the full summary, source URLs, related catalog IDs, source status, tags, and source-check date. Paper and software records remain distinct; use the related IDs to follow the connection. Unknown IDs fail with a clear message and a nonzero exit code.

## Compare systems without assigning a score

```bash
python3 scripts/explore.py compare agentic-scientist-system openresearch-system

# Produce a portable Markdown comparison for a reading group or design review.
python3 scripts/explore.py compare agentic-scientist-system openresearch-system --format markdown
```

Supply at least two distinct **system** IDs. Comparisons retain all seven dimensions, evidence bases, source locators, and limitations. Systems appear by publication/release date, not performance.

The source is [data/comparisons.json](../data/comparisons.json), also used by the published [capability matrix](capability-matrix.md). “Paper report,” “project documentation,” and “code inspection” identify different evidence bases. “Not established” indicates a limit in the examined evidence; it does not prove that a capability is absent. A source check is not a system run. Executed component observations are documented separately in the [reproducibility reports](reproducibility.md).

## Export for your own analysis

All commands support `--format text` (default), `json`, `csv`, or `markdown`. Redirect terminal output to save a file.

```bash
python3 scripts/explore.py search --kind paper --tag verification --format json
python3 scripts/explore.py search --kind tool --format csv
python3 scripts/explore.py show sciencebuddy-system --format json
python3 scripts/explore.py compare agentic-scientist-system openresearch-system --format csv
```

JSON contains `metadata` plus either `entries` or `systems`. Catalog records and comparison records retain their existing fields and full source lists. Search metadata records the applied filters, total matches, returned count, and ordering. Comparison metadata includes the comparison scope and review date.

Catalog CSV uses one row per entry; comparison CSV uses one row per system and dimension. Lists such as `tags`, `sources`, and `related` are JSON encoded within CSV cells, so commas and source locators are preserved. Comparison source cells contain objects with `url`, `label`, and `locator`. CSV includes a header even when no records match and never includes prose before the header. Text and Markdown include contextual notes; JSON and CSV remain machine-readable. Errors go to standard error with exit status 2.

`date` and `year` describe the represented publication/release. Catalog `checked`, comparison `comparison_checked`, and comparison `comparison_reviewed` describe source-review dates. None is a local execution date, a CLI run date, or a promise of current remote availability. Running this CLI does not refresh sources. Its coverage is exactly the catalog in your checkout.

## Verify the CLI

```bash
python3 -m unittest discover -s tests -p 'test_explore.py' -v
```

The tests cover combined filtering, date precision, export round trips, retained citations and evidence bases, clear input errors, use from a different working directory, and preservation of the input records.
