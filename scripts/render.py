"""Generate the public Markdown views; --check detects drift without writing."""
import argparse
from collections import Counter
from catalog import ROOT, CATEGORIES, load, ordered

TITLES = {"paper": "Papers", "system": "Systems", "tool": "Tools", "benchmark": "Benchmarks"}


def entry_text(e, by_id, heading_level=3):
    links = [f'[{e["name"]}]({e["url"]})']
    for field, label in (("paper_url", "Paper"), ("code_url", "Code")):
        if e.get(field) and e[field] != e["url"]:
            links.append(f'[{label}]({e[field]})')
    text = f'<a id="{e["id"]}"></a>\n\n' + "#" * heading_level + " " + " · ".join(links)
    text += f'\n\n**{e["date"]} · {e["evidence"]}** · {CATEGORIES[e["category"]]} · ' + ", ".join(e["tags"])
    text += f'\n\n{e["summary"]}\n\n'
    if e.get("status"):
        text += f'Availability/maintenance: {e["status"]}\n\n'
    if e.get("related"):
        related = []
        for ident in e["related"]:
            other = by_id[ident]
            related.append(f'[{other["name"]}]({TITLES[other["kind"]].lower()}.md#{ident})')
        text += "Related entries: " + ", ".join(related) + ".\n\n"
    text += "Sources: " + " · ".join(f"[{i}]({u})" for i, u in enumerate(e["sources"], 1))
    return text + f' · Content checked: {e["checked"]}.\n'


def render_catalog(kind, entries, by_id):
    selected = ordered([e for e in entries if e["kind"] == kind])
    text = f'# {TITLES[kind]}\n\n[← Overview](../README.md) · [Search coverage](search-protocol.md)\n\n'
    text += f'{len(selected)} annotated records, ordered **newest first by publication/release date**, grouped by year. '
    text += 'Entries with only a known year appear separately after the dated entries for that year; their position within the year is unknown. Same-date ties are ordered by name. '
    text += 'Source status describes publication provenance; these resources have not been independently reproduced for this list.\n\n'
    years = sorted({e["year"] for e in selected}, reverse=True)
    text += "## Contents\n\n" + "\n".join(f'- [{year}](#year-{year})' for year in years) + "\n- [Browse by topic](#browse-by-topic)\n"
    for year in years:
        text += f'\n<a id="year-{year}"></a>\n\n## {year}\n\n'
        year_entries = [e for e in selected if e["year"] == year]
        text += "\n".join(entry_text(e, by_id) for e in year_entries if len(e["date"]) == 10)
        year_only = [e for e in year_entries if len(e["date"]) == 4]
        if year_only:
            text += "\n### Year-only dates\n\nMonth and day have not been established.\n\n"
            text += "\n".join(entry_text(e, by_id, heading_level=4) for e in year_only)
    text += "\n## Browse by topic\n\nJump to an entry above; links within each topic follow the same date order.\n"
    cats = [c for c in CATEGORIES if any(e["category"] == c for e in selected)]
    for cat in cats:
        text += f'\n<a id="topic-{cat}"></a>\n\n### {CATEGORIES[cat]}\n\n'
        text += "\n".join(f'- **{e["date"]}** — [{e["name"]}](#{e["id"]}).' for e in selected if e["category"] == cat) + "\n"
    return text


def readme(entries):
    counts = Counter(e["kind"] for e in entries)
    date = max(e["checked"] for e in entries)
    text = '''# Awesome AI Co-Scientist

AI systems that help researchers develop hypotheses, run experiments, evaluate evidence, and communicate discoveries.

[![Validate catalog](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml/badge.svg)](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

A curated, annotated guide to **papers, systems, tools, and benchmarks**, presented **newest first**. Each entry explains the contribution and its evidence boundary, with primary sources and a content-check date. The collection includes autonomous systems and human-guided research workflows.

## Contents

- [Explore the collection](#explore-the-collection)
- [Start here](#start-here)
- [Choose a reading path](#choose-a-reading-path)
- [How to read the evidence](#how-to-read-the-evidence)
- [Curation and daily updates](#curation-and-daily-updates)
- [Repository layout](#repository-layout)
- [Contribute](#contribute)
- [Acknowledgements and license](#acknowledgements-and-license)

## Explore the collection

'''
    text += f'**{len(entries)} records** · Latest source-check date: **{date}**. Counts distinguish papers from software; a research family may appear in both.\n\n'
    descriptions = {
        "paper": "Mechanisms, research findings, surveys, and scientific limitations.",
        "system": "Integrated research agents and end-to-end research environments.",
        "tool": "Literature, experiments, writing, figures, and reusable infrastructure.",
        "benchmark": "Task definitions, evaluation protocols, and what scores do—and do not—measure.",
    }
    text += "| Collection | Records | What you will find |\n| --- | ---: | --- |\n"
    for kind, title in TITLES.items():
        text += f'| [{title}](docs/{title.lower()}.md) | {counts[kind]} | {descriptions[kind]} |\n'
    text += '''
## Start here

These selected entry points are ordered by publication/release date, newest first. Entries with only a known year follow dated entries from that year. The full catalogs use the same ordering and retain topic indexes.

'''
    # Selection is by explicit editorial flags in the small, versioned ID list.
    featured = (ROOT / "data" / "featured.txt").read_text().splitlines()
    by_id = {e["id"]: e for e in entries}
    featured_entries = [by_id[ident] for ident in featured if ident.strip() and not ident.startswith("#")]
    for e in ordered(featured_entries):
        page = TITLES[e["kind"]].lower()
        text += f'- **{e["date"]} — [{e["name"]}](docs/{page}.md#{e["id"]})** ({e["evidence"]}). {e["summary"]}\n\n'
    text += '''## Choose a reading path

| Your question | Suggested route |
| --- | --- |
| What does an AI co-scientist actually automate? | Start with Google AI co-scientist, Sakana's AI Scientist lineage, ScientistOne/Two, and ScienceBuddy in [Papers](docs/papers.md). Compare human input, experiment access, memory, and validation. |
| What can I inspect or build on? | Use [Systems](docs/systems.md) to find official implementations and identify projects that expose only demos or artifacts. Then choose supporting [Tools](docs/tools.md). |
| How should I evaluate one? | Start with [Benchmarks](docs/benchmarks.md): distinguish ML engineering, code execution, replication, idea evaluation, and long-horizon research. |
| How do research agents extend beyond ML? | Read the [domain-science papers](docs/papers.md#topic-domain-science) and examine their laboratory access, data, experimental controls, and human roles. |
| How do I improve one research stage? | Browse [Tools](docs/tools.md) by literature, ideation, experimentation, writing, or infrastructure. |

## How to read the evidence

- **Preprint**: a public research manuscript; peer review is not established by this label.
- **Peer-reviewed**: a linked journal or proceedings record supports that status. Peer review is not independent replication.
- **Project**: claims are grounded in official project documentation or a release. An implementation, demo, or hosted service is not proof of research effectiveness.
- **Content checked**: the listed primary source was inspected on that date. We have not installed or independently reproduced every system.

Reported evaluations remain specific to their tasks, datasets, budgets, human involvement, and evaluation methods. Automated judging, execution success, paper acceptance, and validated scientific discovery are different outcomes. Missing code links mean availability is unconfirmed here, not necessarily that no code exists.

## Curation and daily updates

We search broadly and curate selectively. See the [search protocol and coverage gaps](docs/search-protocol.md) and [dated changes](CHANGELOG.md). The initial search spans multiple query families, reference trails, existing lists, papers, and official projects; it is **not a claim of exhaustive literature coverage**.

Daily curation is intended to check new research and project changes, read primary evidence, deduplicate entries, run validation, and publish substantive updates. GitHub Actions checks catalog structure and generated-file consistency. No-change searches do not create cosmetic commits.

This repository is **AI-assisted and maintainer-owned**. Source-backed annotations remain open to correction; neither AI generation nor automated checks substitute for expert review.

## Repository layout

```text
README.md                 Overview and selected starting points (generated)
data/                     Canonical JSON catalogs and featured entry IDs
docs/papers.md            Annotated paper catalog (generated)
docs/systems.md           Annotated system catalog (generated)
docs/tools.md             Annotated tool catalog (generated)
docs/benchmarks.md        Annotated evaluation catalog (generated)
docs/search-*.md          Search protocol, source trails, and coverage limits
scripts/                  Standard-library renderer, validator, and link checker
.github/                  Contribution templates and validation workflow
CHANGELOG.md              Substantive additions and corrections
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md), then [suggest a resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new/choose). Explain its contribution, provide primary evidence, and preserve the distinction between an author claim and an independently verified result.

## Acknowledgements and license

The organization follows useful conventions from the [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): focused scope, descriptive annotations, navigable categories, and clear contribution rules. [Related lists and design lessons](docs/search-landscape.md) explain the sources consulted and how this collection differs.

This is an independent collection, with no claim of inclusion in or endorsement by the main Awesome index. That index's [current contribution rules](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) exclude AI-generated lists.

Original catalog content and scripts are dedicated under [CC0 1.0](LICENSE). Linked papers, software, data, and trademarks retain their respective terms.
'''
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    entries = load()
    by_id = {e["id"]: e for e in entries}
    outputs = {ROOT / "README.md": readme(entries)}
    outputs.update({ROOT / "docs" / f"{title.lower()}.md": render_catalog(kind, entries, by_id) for kind, title in TITLES.items()})
    stale = []
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content, encoding="utf-8")
    if stale:
        parser.exit(1, "Generated files need updating: " + ", ".join(stale) + "\n")
    print(f'{"Checked" if args.check else "Rendered"} {len(outputs)} Markdown views from {len(entries)} records.')


if __name__ == "__main__":
    main()
