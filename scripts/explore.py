"""Search, inspect, and compare the local catalog without network access."""
import argparse
from copy import deepcopy
import csv
import io
import json
import sys
from urllib.parse import urlsplit

from catalog import load, ordered
from comparison import BASES, DIMENSIONS, load_comparisons

KINDS = ("paper", "system", "tool", "benchmark")
EVIDENCE = ("preprint", "peer-reviewed", "project")
FORMATS = ("text", "json", "csv", "markdown")
SOURCE_NOTE = "checked is a source-review date, not an execution or reproduction date."
ORDER_NOTE = "Newest publication/release date first; year-only records follow dated records in their year."
CODE_LINK_NOTE = (
    "Code-link presence means a code_url or a repository URL in url/sources; "
    "it does not establish complete framework availability or runnable code."
)
CATALOG_FIELDS = (
    "id", "name", "kind", "category", "year", "date", "date_precision",
    "evidence", "summary", "url", "code_url", "paper_url", "tags",
    "sources", "related", "checked", "added_on", "status",
)


def code_links(entry):
    """Return recorded code links, without checking their contents or availability."""
    links = [entry["code_url"]] if entry.get("code_url") else []
    for url in [entry.get("url", ""), *entry.get("sources", [])]:
        parsed = urlsplit(url)
        parts = [part for part in parsed.path.split("/") if part]
        if (parsed.hostname in {"github.com", "gitlab.com", "bitbucket.org"}
                and len(parts) >= 2 and url not in links):
            links.append(url)
    return links


def search_entries(entries, query="", *, kind=None, tags=(), year=None,
                   since_year=None, evidence=None, has_code_link=False):
    """Match all query terms and all tags; return copies in catalog date order."""
    terms = query.casefold().split()
    wanted_tags = {tag.casefold() for tag in tags}
    results = []
    for entry in entries:
        searchable = " ".join([
            entry["id"], entry["name"], entry["summary"], entry["category"],
            *entry["tags"],
        ]).casefold()
        if not all(term in searchable for term in terms):
            continue
        if kind and entry["kind"] != kind:
            continue
        if not wanted_tags.issubset({tag.casefold() for tag in entry["tags"]}):
            continue
        if year is not None and entry["year"] != year:
            continue
        if since_year is not None and entry["year"] < since_year:
            continue
        if evidence and entry["evidence"] != evidence:
            continue
        if has_code_link and not code_links(entry):
            continue
        results.append(deepcopy(entry))
    return ordered(results)


def show_entry(entries, ident):
    for entry in entries:
        if entry["id"] == ident:
            return deepcopy(entry)
    raise ValueError(f"Unknown catalog ID: {ident}. Use search to find an ID.")


def compare_entries(entries, comparisons, ids):
    """Return source-backed records for systems, without scoring or changing data."""
    if len(ids) < 2:
        raise ValueError("compare needs at least two distinct system IDs.")
    if len(set(ids)) != len(ids):
        raise ValueError("compare needs distinct system IDs; an ID was repeated.")
    selected = [show_entry(entries, ident) for ident in ids]
    non_systems = [e["id"] for e in selected if e["kind"] != "system"]
    if non_systems:
        raise ValueError("compare accepts system IDs only: " + ", ".join(non_systems))
    records = {r["system_id"]: r for r in comparisons["systems"]}
    missing = [e["id"] for e in selected if e["id"] not in records]
    if missing:
        raise ValueError("No source-backed comparison record for: " + ", ".join(missing))
    return [
        {"catalog": entry, "comparison": deepcopy(records[entry["id"]])}
        for entry in ordered(selected)
    ]


def precision(entry):
    return "year only" if len(entry["date"]) == 4 else "day"


def display_date(entry):
    return entry["date"] + (" (year only)" if precision(entry) == "year only" else "")


def markdown(value):
    """Escape data for Markdown text and table cells."""
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(
        ">", "&gt;"
    ).replace("\\", "\\\\").replace("|", "\\|").replace(
        "[", "\\["
    ).replace("]", "\\]").replace("*", "\\*").replace("_", "\\_").replace("\n", "<br>")


def source_lines(record, prefix=""):
    return [f'{prefix}{s["label"]}: {s["url"]} — {s["locator"]}' for s in record["sources"]]


def catalog_text(entries, full=False):
    blocks = []
    for entry in entries:
        lines = [
            f'{entry["name"]} [{entry["id"]}]',
            f'  {display_date(entry)} | {entry["kind"]} | {entry["evidence"]}',
            f'  {entry["summary"]}',
            f'  URL: {entry["url"]}',
            f'  Tags: {", ".join(entry["tags"])}',
            f'  Source checked: {entry["checked"]}',
        ]
        if full:
            lines.append(f'  Category: {entry["category"]}')
            for field in ("code_url", "paper_url", "status"):
                if entry.get(field):
                    lines.append(f'  {field}: {entry[field]}')
            lines.append("  Sources:")
            lines.extend(f"    {url}" for url in entry["sources"])
            lines.append("  Related IDs: " + ", ".join(entry.get("related", [])))
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def compare_text(payload):
    lines = [payload["metadata"]["comparison_scope"], ""]
    for pair in payload["systems"]:
        entry, record = pair["catalog"], pair["comparison"]
        lines.extend([
            f'{record["short_name"]} [{entry["id"]}] — {display_date(entry)}',
            f'Comparison source checked: {record["checked"]}; catalog source checked: {entry["checked"]}',
            f'Limitations: {record["limitations"]}',
        ])
        for dimension, label in DIMENSIONS.items():
            cell = record["dimensions"][dimension]
            lines.extend([
                f'  {label} [{BASES[cell["basis"]]}]: {cell["text"]}',
                "  Sources: " + ", ".join(cell["sources"]),
            ])
        lines.append("Source locations:")
        lines.extend(source_lines(record, "  "))
        lines.append("")
    return "\n".join(lines).rstrip()


def catalog_markdown(entries):
    lines = ["| Date | Resource | Summary and evidence |", "| --- | --- | --- |"]
    for entry in entries:
        name = f'[{markdown(entry["name"])}]({entry["url"]})'
        resource = name + f'<br>ID: `{entry["id"]}`<br>{entry["kind"]} · {entry["evidence"]}'
        details = [markdown(entry["summary"]), "Category: " + markdown(entry["category"])]
        details.append("Tags: " + ", ".join(markdown(tag) for tag in entry["tags"]))
        details.append("Sources: " + " · ".join(f'[{i}]({url})' for i, url in enumerate(entry["sources"], 1)))
        for field in ("code_url", "paper_url"):
            if entry.get(field):
                details.append(f'{field}: [{field}]({entry[field]})')
        if entry.get("related"):
            details.append("Related IDs: " + ", ".join(f'`{ident}`' for ident in entry["related"]))
        if entry.get("status"):
            details.append("Status: " + markdown(entry["status"]))
        details.append(f'Source checked: {entry["checked"]}')
        lines.append(f'| {display_date(entry)} | {resource} | {"<br><br>".join(details)} |')
    return "\n".join(lines)


def compare_markdown(payload):
    systems = payload["systems"]
    lines = [markdown(payload["metadata"]["comparison_scope"]), ""]
    names = [markdown(pair["comparison"]["short_name"]) for pair in systems]
    lines.extend(["| Dimension | " + " | ".join(names) + " |", "| --- | " + " | ".join("---" for _ in systems) + " |"])
    for dimension, label in DIMENSIONS.items():
        cells = []
        for pair in systems:
            record = pair["comparison"]
            cell = record["dimensions"][dimension]
            refs = {source["url"]: i for i, source in enumerate(record["sources"], 1)}
            links = " · ".join(f'[{refs[url]}]({url})' for url in cell["sources"])
            cells.append(f'{markdown(cell["text"])}<br>**{BASES[cell["basis"]]}** · {links}')
        lines.append(f'| {label} | {" | ".join(cells)} |')
    for pair in systems:
        entry, record = pair["catalog"], pair["comparison"]
        lines.extend([
            "", f'### {markdown(record["short_name"])}', "",
            f'ID: `{entry["id"]}` · Publication/release: {display_date(entry)} · Comparison source checked: {record["checked"]} · Catalog source checked: {entry["checked"]}',
            "", markdown(record["limitations"]), "",
        ])
        for index, source in enumerate(record["sources"], 1):
            lines.append(f'{index}. [{markdown(source["label"])}]({source["url"]}) — {markdown(source["locator"])}')
    return "\n".join(lines)


def csv_output(payload):
    output = io.StringIO(newline="")
    if payload["metadata"]["command"] == "compare":
        fields = ("system_id", "name", "date", "date_precision", "catalog_checked", "comparison_checked", "comparison_reviewed", "dimension", "evidence_basis", "statement", "sources", "limitations", "scope")
        writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for pair in payload["systems"]:
            entry, record = pair["catalog"], pair["comparison"]
            sources = {source["url"]: source for source in record["sources"]}
            for dimension, cell in record["dimensions"].items():
                writer.writerow({
                    "system_id": entry["id"], "name": entry["name"],
                    "date": entry["date"], "date_precision": precision(entry),
                    "catalog_checked": entry["checked"], "comparison_checked": record["checked"],
                    "comparison_reviewed": payload["metadata"]["comparison_reviewed"],
                    "dimension": dimension, "evidence_basis": cell["basis"], "statement": cell["text"],
                    "sources": json.dumps([sources[url] for url in cell["sources"]], ensure_ascii=False),
                    "limitations": record["limitations"], "scope": payload["metadata"]["comparison_scope"],
                })
    else:
        writer = csv.DictWriter(output, fieldnames=CATALOG_FIELDS, lineterminator="\n")
        writer.writeheader()
        for entry in payload["entries"]:
            row = {key: entry.get(key, "") for key in CATALOG_FIELDS}
            row["date_precision"] = precision(entry)
            for key in ("tags", "sources", "related"):
                row[key] = json.dumps(entry.get(key, []), ensure_ascii=False)
            writer.writerow(row)
    return output.getvalue()


def render_output(payload, output_format):
    if output_format == "json":
        return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if output_format == "csv":
        return csv_output(payload)
    metadata = payload["metadata"]
    lines = [SOURCE_NOTE, ORDER_NOTE]
    if metadata["command"] == "compare":
        lines.append(f'Comparison sources reviewed: {metadata["comparison_reviewed"]}. No ranking is assigned.')
        content = compare_markdown(payload) if output_format == "markdown" else compare_text(payload)
    else:
        lines.append(f'Showing {metadata["returned"]} of {metadata["total_matches"]} matching records.')
        if metadata.get("filters", {}).get("has_code_link"):
            lines.append(CODE_LINK_NOTE)
        if not payload["entries"]:
            content = "No matching records."
        elif output_format == "markdown":
            content = catalog_markdown(payload["entries"])
        else:
            content = catalog_text(payload["entries"], full=metadata["command"] == "show")
    return "\n\n".join([*lines, content]) + "\n"


def positive_integer(value):
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def year_number(value):
    number = positive_integer(value)
    if not 1900 <= number <= 9999:
        raise argparse.ArgumentTypeError("must be a four-digit year from 1900 to 9999")
    return number


def make_parser():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    subparsers = parser.add_subparsers(dest="command", required=True)
    search = subparsers.add_parser("search", help="Find records; all filters combine with AND", allow_abbrev=False)
    search.add_argument("query", nargs="?", default="", help="Quoted text; all whitespace-separated terms must match")
    search.add_argument("--kind", choices=KINDS)
    search.add_argument("--tag", action="append", default=[], help="Exact tag, case-insensitive; repeat to require every tag")
    years = search.add_mutually_exclusive_group()
    years.add_argument("--year", type=year_number, help="Exact publication/release year")
    years.add_argument("--since-year", type=year_number, help="Inclusive minimum publication/release year")
    search.add_argument("--evidence", choices=EVIDENCE, help="Source-status label; not a quality score")
    search.add_argument("--has-code-link", action="store_true", help=CODE_LINK_NOTE)
    search.add_argument("--limit", type=positive_integer, help="Return at most this many records (default: all matches)")
    show = subparsers.add_parser("show", help="Inspect one ID, including sources and related IDs", allow_abbrev=False)
    show.add_argument("id")
    compare = subparsers.add_parser("compare", help="Compare two or more system IDs with primary-source evidence", allow_abbrev=False)
    compare.add_argument("ids", nargs="+")
    for subparser in (search, show, compare):
        subparser.add_argument("--format", choices=FORMATS, default="text")
    return parser


def main(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)
    metadata = {"command": args.command, "order": ORDER_NOTE, "source_check_note": SOURCE_NOTE}
    try:
        entries = load()
        if args.command == "compare":
            comparisons = load_comparisons()
            systems = compare_entries(entries, comparisons, args.ids)
            metadata.update(comparison_scope=comparisons["scope"], comparison_reviewed=comparisons["reviewed"])
            payload = {"metadata": metadata, "systems": systems}
        elif args.command == "show":
            metadata.update(total_matches=1, returned=1)
            payload = {"metadata": metadata, "entries": [show_entry(entries, args.id)]}
        else:
            available_tags = {tag.casefold() for entry in entries for tag in entry["tags"]}
            unknown = sorted(set(tag for tag in args.tag if tag.casefold() not in available_tags))
            if unknown:
                raise ValueError("Unknown tag(s): " + ", ".join(unknown) + ". Inspect search output for recorded tags.")
            filters = dict(query=args.query, kind=args.kind, tags=args.tag, year=args.year,
                           since_year=args.since_year, evidence=args.evidence, has_code_link=args.has_code_link)
            matches = search_entries(entries, **filters)
            selected = matches[:args.limit] if args.limit else matches
            metadata.update(filters=filters, total_matches=len(matches), returned=len(selected),
                            limit=args.limit, code_link_note=CODE_LINK_NOTE)
            payload = {"metadata": metadata, "entries": selected}
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    sys.stdout.write(render_output(payload, args.format))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
