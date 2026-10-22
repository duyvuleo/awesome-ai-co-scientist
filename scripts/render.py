"""Generate the public Markdown views; --check detects drift without writing."""
import argparse
from collections import Counter
from html import escape
from catalog import ROOT, CATEGORIES, load, ordered
from comparison import load_comparisons, render_comparisons

TITLES = {"paper": "Papers", "system": "Systems", "tool": "Tools", "benchmark": "Benchmarks"}


def table_text(value):
    """Keep text in a single GFM table cell without losing literal characters."""
    return escape(value, quote=False).replace("|", "&#124;").replace("\n", "<br>")


def paper_table(entries, by_id):
    if not entries:
        return ""
    rows = ["| Date | Paper | Summary & evidence |", "| --- | --- | --- |"]
    for entry in entries:
        ident = entry["id"]
        paper = f'<a id="{ident}"></a>**[{table_text(entry["name"])}]({entry["url"]})**'
        paper += f'<br>*{entry["evidence"].replace("-", " ").capitalize()}*'
        if entry.get("code_url") and entry["code_url"] != entry["url"]:
            paper += f' · [Code]({entry["code_url"]})'
        metadata = [
            f'<strong>Topic:</strong> {escape(CATEGORIES[entry["category"]])}',
            f'<strong>Tags:</strong> {escape(", ".join(entry["tags"]))}',
            '<strong>Sources:</strong> ' + " · ".join(
                f'<a href="{escape(url, quote=True)}">{i}</a>'
                for i, url in enumerate(entry["sources"], 1)
            ),
            f'<strong>Content checked:</strong> {escape(entry["checked"])}',
        ]
        if entry.get("related"):
            related = []
            for related_id in entry["related"]:
                other = by_id[related_id]
                href = f'{TITLES[other["kind"]].lower()}.md#{related_id}'
                related.append(f'<a href="{escape(href, quote=True)}">{escape(other["name"])}</a>')
            metadata.append('<strong>Related entries:</strong> ' + ", ".join(related))
        if entry.get("status"):
            metadata.append('<strong>Status:</strong> ' + escape(entry["status"]))
        disclosure = '<details><summary>Sources &amp; metadata</summary>' + "<br>".join(metadata) + '</details>'
        summary = table_text(entry["summary"]) + disclosure.replace("|", "&#124;").replace("\n", "<br>")
        display_date = entry["date"].replace("-", "&#8209;")
        rows.append(f'| <code>{display_date}</code> | {paper} | {summary} |')
    return "\n".join(rows) + "\n"


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
    text += 'Year-only entries follow dated entries within each year; ties are alphabetical. '
    text += 'Source status identifies publication provenance. See [local reports](reproducibility.md) for executed component checks.\n\n'
    if kind == "paper":
        text += 'Expand **Sources & metadata** for citations, topics, related entries, and inspection dates.\n\n'
    years = sorted({e["year"] for e in selected}, reverse=True)
    text += "## Contents\n\n" + "\n".join(f'- [{year}](#year-{year})' for year in years) + "\n- [Browse by topic](#browse-by-topic)\n"
    for year in years:
        text += f'\n<a id="year-{year}"></a>\n\n## {year}\n\n'
        year_entries = [e for e in selected if e["year"] == year]
        dated = [e for e in year_entries if len(e["date"]) == 10]
        text += paper_table(dated, by_id) if kind == "paper" else "\n".join(entry_text(e, by_id) for e in dated)
        year_only = [e for e in year_entries if len(e["date"]) == 4]
        if year_only:
            text += "\n### Year-only dates\n\nMonth and day have not been established.\n\n"
            text += paper_table(year_only, by_id) if kind == "paper" else "\n".join(entry_text(e, by_id, heading_level=4) for e in year_only)
    text += "\n## Browse by topic\n\nEntries within each topic follow the same date order.\n"
    cats = [c for c in CATEGORIES if any(e["category"] == c for e in selected)]
    for cat in cats:
        text += f'\n<a id="topic-{cat}"></a>\n\n### {CATEGORIES[cat]}\n\n'
        text += "\n".join(f'- **{e["date"]}** — [{e["name"]}](#{e["id"]}).' for e in selected if e["category"] == cat) + "\n"
    return text


def readme(entries):
    counts = Counter(e["kind"] for e in entries)
    date = max(e["checked"] for e in entries)
    text = '''<!-- Generated by scripts/render.py from data/. Edit the source, then regenerate. -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="AI Co-Scientist: compare systems, evaluate evidence, and reproduce results" src="assets/banner-light.svg" width="1280" height="360">
</picture>

# Awesome AI Co-Scientist

[![Validation](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml)
[![License: CC0](https://img.shields.io/badge/license-CC0%201.0-315da7)](LICENSE)

> Curated papers, systems, tools, and benchmarks for AI-assisted scientific discovery.

Evaluating an AI co-scientist requires distinguishing hypothesis generation, experiment execution, and scientific validation. This collection compares these capabilities, the human work they require, and the evidence reported for them.

[Browse papers](docs/papers.md) · [Compare systems](docs/capability-matrix.md) · [Read local experiments](docs/reproducibility.md) · [Contribute](CONTRIBUTING.md)

<a id="explore-the-collection"></a>

'''
    text += (
        f'**{counts["paper"]} annotated papers · {counts["system"]} systems · '
        f'{counts["tool"]} tools · {counts["benchmark"]} benchmarks**\n\n'
        f'Latest source check: **{date}**. Entries include summaries, publication status, primary sources, '
        'and inspection dates. Papers and software are counted separately.\n\n'
    )
    text += '''## Contents

- [Start here](#start-here)
- [Choose a reading route](#choose-a-reading-route)
- [Papers](docs/papers.md)
- [Systems](docs/systems.md) and [tools](docs/tools.md)
- [Benchmarks](docs/benchmarks.md)
- [Capability and evidence matrix](docs/capability-matrix.md)
- [Evaluation guide](docs/evaluation-guide.md)
- [Research outputs](docs/research-outputs.md)
- [Research synthesis](docs/research-synthesis.md)
- [Local experiments and study guides](#local-experiments-and-study-guides)
- [Curation and daily updates](#curation-and-daily-updates)
- [Contributing](#contributing)
- [Related collections](#related-collections)

<a id="selected-reading"></a>

## Start here

Selected resources, newest first. Year-only entries follow dated entries within each year; all catalogs retain topic indexes.

| Date | Resource / status | Concise summary | Links |
| --- | --- | --- | --- |
'''
    featured = (ROOT / "data" / "featured.txt").read_text().splitlines()
    by_id = {e["id"]: e for e in entries}
    featured_entries = [by_id[ident] for ident in featured if ident.strip() and not ident.startswith("#")]
    for e in ordered(featured_entries):
        page = TITLES[e["kind"]].lower()
        resource = f'[{table_text(e["name"])}]({e["url"]})<br>*{e["evidence"].replace("-", " ")}*'
        links = []
        for field, label in (("paper_url", "Paper"), ("code_url", "Code")):
            if e.get(field) and e[field] != e["url"]:
                links.append(f'[{label}]({e[field]})')
        links.append(f'[Details](docs/{page}.md#{e["id"]})')
        display_date = e["date"].replace("-", "&#8209;")
        text += f'| <code>{display_date}</code> | {resource} | {table_text(e["summary"])} | {" · ".join(links)} |\n'
    text += '''
<a id="choose-a-reading-path"></a>
<a id="compare-reproduce-and-synthesize"></a>

## Choose a reading route

| Your question | Where to start |
| --- | --- |
| Which research stages can agents automate? | [Papers](docs/papers.md) and the [capability matrix](docs/capability-matrix.md) |
| What can I inspect or build on? | [Systems](docs/systems.md) and [tools](docs/tools.md), with availability notes |
| Which benchmark fits my experiment? | [Benchmarks](docs/benchmarks.md) and the [evaluation guide](docs/evaluation-guide.md) |
| What has automated research produced? | [Released research outputs](docs/research-outputs.md), including Recursive Flint |
| What has been tested locally? | [Component reproducibility reports](docs/reproducibility.md) |
| Which findings agree, and which questions remain open? | [Cross-paper synthesis](docs/research-synthesis.md) |
| How do agents support laboratory research? | [Domain-science papers](docs/papers.md#topic-domain-science) |

## Scope

We include systems that formulate hypotheses, conduct experiments, analyse results, or communicate scientific findings. Supporting tools and benchmarks are included when their role in these activities is explicit. General-purpose agents require a concrete connection to scientific research.

<a id="how-to-read-the-evidence"></a>

**Preprint**, **peer-reviewed**, and **project** identify source status. Peer review requires a linked publication record; project entries describe official documentation. **Content checked** records source inspection, not execution. Missing code links indicate unconfirmed availability.

Proposal ratings, successful execution, and validated discoveries measure different outcomes. Comparisons therefore retain the task, budget, human roles, and evaluation setting. Our local reports cover selected components; they do not reproduce complete research campaigns or published scientific findings.

<a id="quick-start"></a>
<a id="research-workflows"></a>

## Local experiments and study guides

| Resource | Purpose |
| --- | --- |
| [Getting started](docs/start-here.md) | Inspect a system, examine a recorded failure, and prepare a study. |
| [Local search and exports](docs/cli.md) | Search, compare, and export catalog records using Python 3.10+. |
| [Evaluation protocols](docs/workflows/README.md) | Study [evaluator integrity](docs/workflows/evaluator-integrity.md), [idea selection](docs/workflows/idea-to-experiment.md), or [human collaboration](docs/workflows/human-ai-collaboration.md). |
| [Study packs](docs/study-packs.md) | Record protocols, budgets, execution details, and results. |
| [Reproducibility reports](docs/reproducibility.md) | Inspect pinned sources, commands, failures, and independent checks. |

Search and planning work offline without model calls. The two recorded component investigations used no paid APIs. Proposed protocols are labelled separately from executed experiments.

## Curation and daily updates

Daily curation checks primary sources for new work and project changes. We publish substantive additions and corrections after validation. See the [search protocol](docs/search-protocol.md) for coverage limits and the [changelog](CHANGELOG.md) for updates; coverage is not exhaustive.

This collection is AI-assisted and maintainer-owned. Automated checks validate catalog structure and generated files; scientific claims require source review.

<a id="repository-layout"></a>
<a id="contribute"></a>

## Contributing

Suggest a [resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=resource.yml), report a [reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml), or share [practical experience](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml). Include sources, methods, and limitations; failed attempts are welcome. See the [contribution guide](CONTRIBUTING.md) and [open contribution topics](docs/community-roadmap.md).

The catalogs in [data/](data/) generate the indexes. The [data reference](docs/data-reference.md) explains their structure and reuse. Cite primary papers for scientific claims; use [CITATION.cff](CITATION.cff) and a commit ID when citing this collection.

<a id="acknowledgements-and-license"></a>

## Related collections

- [Awesome Reliable Text-to-SQL](https://github.com/duyvuleo/awesome-reliable-text-to-sql) — A companion collection on ambiguity, clarification, and unanswerability.
- [Related AI-science collections](docs/search-landscape.md) — Coverage and differences among existing lists.
- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) — Guidance for curated collections. This repository is independent of the central index, whose [contribution rules](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) exclude AI-generated lists.

## License

Original annotations, catalog records, and scripts use [CC0 1.0](LICENSE). Linked papers, software, data, and trademarks retain their respective terms.
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
    outputs[ROOT / "docs/capability-matrix.md"] = render_comparisons(load_comparisons(), entries)
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
