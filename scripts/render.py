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
    text += 'Entries with only a known year appear separately after the dated entries for that year; their position within the year is unknown. Same-date ties are ordered by name. '
    text += 'Source status describes publication provenance. Catalog inclusion does not imply end-to-end replication; [local reproducibility reports](reproducibility.md) document the exact scope of selected execution checks.\n\n'
    if kind == "paper":
        text += 'Full summaries remain visible. Expand **Sources & metadata** for source links, topics, tags, related entries, and content-check dates.\n\n'
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
    text += "\n## Browse by topic\n\nJump to an entry above; links within each topic follow the same date order.\n"
    cats = [c for c in CATEGORIES if any(e["category"] == c for e in selected)]
    for cat in cats:
        text += f'\n<a id="topic-{cat}"></a>\n\n### {CATEGORIES[cat]}\n\n'
        text += "\n".join(f'- **{e["date"]}** — [{e["name"]}](#{e["id"]}).' for e in selected if e["category"] == cat) + "\n"
    return text


def readme(entries):
    counts = Counter(e["kind"] for e in entries)
    date = max(e["checked"] for e in entries)
    text = '''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="AI Co-Scientist: a research toolkit to compare systems, evaluate evidence, and reproduce results" src="assets/banner-light.svg" width="1280" height="360">
</picture>

# Awesome AI Co-Scientist

Find suitable AI co-scientist systems, design fair evaluations, and share evidence others can inspect.

[![Validate catalog](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml/badge.svg)](https://github.com/duyvuleo/awesome-ai-co-scientist/actions/workflows/validate.yml)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

A practical research resource combining **source-backed comparisons, offline discovery tools, evaluation recipes, and reproducibility reports**. The annotated literature remains available in newest-first order. Use the collection to produce a shortlist, a study plan, or an inspectable observation.

## Contents

- [Start here](#start-here)
- [Quick start](#quick-start)
- [Research workflows](#research-workflows)
- [Explore the collection](#explore-the-collection)
- [Compare, reproduce, and synthesize](#compare-reproduce-and-synthesize)
- [Selected reading](#selected-reading)
- [Choose a reading path](#choose-a-reading-path)
- [How to read the evidence](#how-to-read-the-evidence)
- [Curation and daily updates](#curation-and-daily-updates)
- [Repository layout](#repository-layout)
- [Contribute](#contribute)
- [Acknowledgements and license](#acknowledgements-and-license)

## Start here

| Your task | Use | Leave with |
| --- | --- | --- |
| Understand the field | [Guided starting path](docs/start-here.md) and [research synthesis](docs/research-synthesis.md) | A concrete question and a reading plan. |
| Choose systems to investigate | [Offline search and comparison CLI](docs/cli.md) and [capability matrix](docs/capability-matrix.md) | A shortlist with sources, capabilities, and unresolved constraints. |
| Plan a defensible evaluation | [Evaluation guide](docs/evaluation-guide.md) and [study packs](docs/study-packs.md) | A declared protocol with controls, budgets, and an empty run record. |
| Inspect or repeat an executed check | [Local reproducibility reports](docs/reproducibility.md) | Pinned code, commands, configurations, observations, and limitations. |
| Contribute a useful finding | [Community contribution opportunities](docs/community-roadmap.md) | A correction, replication attempt, workflow lesson, or testable proposal. |
| Build on the catalog | [Data reference and exports](docs/data-reference.md) | Source-preserving JSON, CSV, or Markdown for your own tools. |

## Quick start

Python 3.10+ is sufficient for discovery and planning; no API keys or third-party packages are needed for these commands.

```bash
git clone https://github.com/duyvuleo/awesome-ai-co-scientist.git
cd awesome-ai-co-scientist
python3 scripts/explore.py search --kind system --tag human-ai-collaboration
python3 scripts/explore.py compare \\
  agentic-scientist-system sciencebuddy-system --format markdown
python3 scripts/study_pack.py create \\
  --recipe evaluator-integrity \\
  --resources agentic-scientist-system \\
  --output .local/my-study
python3 scripts/study_pack.py validate .local/my-study
```

After cloning, these commands work offline. They search local evidence and create a **planned** study; they do not run research systems, contact model APIs, or produce scientific results. Use a fresh output directory for each study. Completed records require execution details and hash-checked artifacts, while scientific validity still requires evidence review.

## Research workflows

| Recipe | Main question | Useful output |
| --- | --- | --- |
| [Evaluator integrity](docs/workflows/evaluator-integrity.md) | Does the evaluator distinguish valid results from misleading scores? | Valid/invalid fixtures and an independent calculation. |
| [Idea to experiment](docs/workflows/idea-to-experiment.md) | Which proposed ideas survive implementation and controlled evaluation? | A complete idea-to-artifact ledger, including failures. |
| [Human–AI collaboration](docs/workflows/human-ai-collaboration.md) | How do assistance, quality, and total researcher effort interact? | A matched-condition protocol and human-effort ledger. |

See the [workflow index](docs/workflows/README.md) for scope and prerequisites. These are proposed study designs; the separately dated [execution reports](docs/reproducibility.md) record what has actually run.

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
## Compare, reproduce, and synthesize

| Research question | Read | What the evidence establishes |
| --- | --- | --- |
| How do these systems differ? | [Capability and evidence matrix](docs/capability-matrix.md) | Human roles, hypothesis generation, execution, memory, verification, code access, and evaluation settings, with a source for every comparison cell. |
| What has automated research produced? | [Research outputs and evidence](docs/research-outputs.md) | Released artifacts, the system and human roles behind them, and the boundary between creator claims and independent reproduction. |
| What behavior can we reproduce locally? | [Reproducibility reports](docs/reproducibility.md) | Pinned public sources, runnable commands, recorded configurations, observed results and failures, and explicit limits on reproduced claims. |
| Which findings agree, conflict, or leave gaps? | [Cross-paper research synthesis](docs/research-synthesis.md) | Recurring limitations, tensions between studies, and testable open questions, separating reported findings from editorial interpretation. |

The matrix compares evidence rather than assigning a universal ranking. The initial execution reports are local component investigations with no paid model calls; they do not reproduce a complete scientist-agent discovery campaign.

## Selected reading

These selected entry points are ordered by publication/release date, newest first. Entries with only a known year follow dated entries from that year. The full catalogs use the same ordering and retain topic indexes.

<details>
<summary>Expand selected papers, systems, tools, and benchmarks</summary>

'''
    # Selection is by explicit editorial flags in the small, versioned ID list.
    featured = (ROOT / "data" / "featured.txt").read_text().splitlines()
    by_id = {e["id"]: e for e in entries}
    featured_entries = [by_id[ident] for ident in featured if ident.strip() and not ident.startswith("#")]
    for e in ordered(featured_entries):
        page = TITLES[e["kind"]].lower()
        text += f'- **{e["date"]} — [{e["name"]}](docs/{page}.md#{e["id"]})** ({e["evidence"]}). {e["summary"]}\n\n'
    text += '''</details>

## Choose a reading path

| Your question | Suggested route |
| --- | --- |
| What does an AI co-scientist actually automate? | Start with Google AI co-scientist, Sakana's AI Scientist lineage, ScientistOne/Two, and ScienceBuddy in [Papers](docs/papers.md). Compare human input, experiment access, memory, and validation. |
| What can I inspect or build on? | Use [Systems](docs/systems.md) to find official implementations and identify projects that expose only demos or artifacts. Then choose supporting [Tools](docs/tools.md). |
| How should I evaluate one? | Start with [Benchmarks](docs/benchmarks.md): distinguish ML engineering, code execution, replication, idea evaluation, and long-horizon research. |
| What has actually been run for this collection? | Read the [reproducibility reports](docs/reproducibility.md) for exact commands, observed behavior, costs, and untested claims. |
| Which research problems remain open? | Use the [cross-paper synthesis](docs/research-synthesis.md) to connect evidence gaps to concrete evaluation designs. |
| How do research agents extend beyond ML? | Read the [domain-science papers](docs/papers.md#topic-domain-science) and examine their laboratory access, data, experimental controls, and human roles. |
| How do I improve one research stage? | Browse [Tools](docs/tools.md) by literature, ideation, experimentation, writing, or infrastructure. |

## How to read the evidence

- **Preprint**: a public research manuscript; peer review is not established by this label.
- **Peer-reviewed**: a linked journal or proceedings record supports that status. Peer review is not independent replication.
- **Project**: claims are grounded in official project documentation or a release. An implementation, demo, or hosted service is not proof of research effectiveness.
- **Content checked**: the listed primary source was inspected on that date. This is distinct from a recorded execution date in a reproducibility report.

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
docs/capability-matrix.md Comparison of system capabilities and evidence (generated)
docs/reproducibility.md   Index of bounded local execution reports
docs/research-synthesis.md Cross-paper findings and open questions
docs/start-here.md        Guided entry points and an offline first task
docs/workflows/           Worked evaluation recipes
docs/study-packs.md       Planning and evidence-record format
docs/cli.md               Search, inspect, compare, and export commands
docs/data-reference.md    Public data fields, joins, and reuse guidance
reports/reproducibility/ Pinned-source reports and observed run artifacts
templates/study/          Procedural study templates
tests/                    Offline behavior and artifact-integrity checks
docs/search-*.md          Search protocol, source trails, and coverage limits
scripts/                  Standard-library renderer, validator, and link checker
.github/                  Contribution templates and validation workflow
CHANGELOG.md              Substantive additions and corrections
```

## Contribute

Choose a [contribution opportunity](docs/community-roadmap.md) and read [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include failed attempts and unresolved observations when their evidence and limits are clear.

- [Suggest a resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=resource.yml).
- [Report a reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml).
- [Share practical experience or a proposed investigation](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml).

For reuse, see the [data reference](docs/data-reference.md) and [citation metadata](CITATION.cff). Cite the underlying papers for scientific claims and record the repository commit used for comparative analysis.

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
