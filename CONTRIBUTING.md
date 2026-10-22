# Contributing

Suggest a resource through an issue or a focused pull request. Explain what a researcher can learn or do with it and provide the primary paper or official project URL. Disclose your connection to the project when relevant.

You can also contribute a [reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml), [practical experience or investigation plan](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml), or a tested improvement to the offline tools. The [community roadmap](docs/community-roadmap.md) lists concrete starting points; the [evaluation guide](docs/evaluation-guide.md) and [study packs](docs/study-packs.md) help prepare an inspectable report.

## What belongs here

Include work that helps formulate, investigate, execute, evaluate, or communicate scientific research: integrated scientist agents, hypothesis generation, experiment orchestration, domain-specific research agents, research workflow tools, and benchmarks. Include foundational work when it explains a current design choice. Generic agent frameworks and general chatbots need a concrete scientific workflow to qualify.

We prioritize useful, inspectable contributions over popularity. A preprint or new repository can qualify, but its maturity and evidence must remain clear. A historical research artifact can stay even if its software is no longer maintained; mark that condition instead of implying active support.

## Entry requirements

1. Search the catalog for the title, arXiv identifier, DOI, and repository. Update an existing record when it is a new version of the same work.
2. Read the primary source. Use an official repository for software and an author paper, proceedings record, or journal for research claims.
3. Add an original 25–85 word summary: what it does, how it does it, and the relevant evidence boundary. Avoid copied abstracts, promotional claims, unsupported comparisons, and benchmark numbers without their exact setting.
4. Include the source URLs, source-status label, date precision actually available, useful tags, and the date on which the sources were read. A source check is not an independent reproduction.
5. Set `added_on` to the date an entry first enters this collection (Australia/Sydney), and preserve it on later edits. The README automatically displays the eight latest additions. Keep source dates separate from `checked`. Do not replace an unknown publication date with the discovery date. The `year` field means the represented paper or project release year, not necessarily the project's founding year.
6. Add a short dated entry to CHANGELOG.md for substantive additions or corrections. Record search coverage and unresolved questions when expanding a topic.

## Editing and checks

The source of truth is `data/*.json`. The four catalogs and the README selection are generated; edit the JSON or renderer as appropriate.

The system matrix is generated from `data/comparisons.json`. Every comparison cell needs a primary source and an evidence basis: paper report, project documentation, code inspection, or not established. Include the section or file inspected. A missing capability statement is not evidence of absence, and static inspection is not an execution result.

Reproducibility reports belong under `reports/reproducibility/` and must distinguish the exact executed component from broader system claims. Include the pinned public revision, source hashes, input fixtures, portable commands, environment, observed outcomes and failures, wall time, cost basis, and untested claims. Preserve completed reports as dated observations; a new run or upstream revision needs separately recorded evidence. Scientific reproduction claims require matching the relevant experimental protocol, not merely a successful component check.

Cross-paper synthesis should cite primary findings, label interpretation, and explain differences in tasks, budgets, human roles, and evaluation before describing results as conflicting.

Presentation is newest first by publication/release date, grouped by year in each catalog. Year-only records appear in a labeled group within their year; do not invent a month or day to force a chronological position. All four catalogs use the same table columns: date, resource/status, summary/evidence, and links. Keep summaries and status notes visible, with detailed sources in expandable metadata. Topic indexes use date/resource tables.

```bash
python3 scripts/validate.py
python3 scripts/render.py
python3 scripts/render.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_links.py --output .local/link-report.json
```

Python 3.10 or newer is sufficient; no third-party packages are needed. HTTP status checks complement source reading and do not establish that a URL contains the correct paper. Rate limits, bot protection, and temporary outages need manual review.

Use the [pull request template](.github/pull_request_template.md). Human review is welcome for every AI-assisted entry. Contributions use the repository's [CC0 dedication](LICENSE); linked papers, code, and trademarks retain their owners' terms.
