"""Render and validate source-backed system comparisons."""
import json
from datetime import date
from urllib.parse import urlsplit
from catalog import ROOT, ordered

DIMENSIONS = {
    "human_involvement": "Human involvement",
    "hypothesis_generation": "Hypothesis generation",
    "experiment_execution": "Experiment execution",
    "memory": "Memory",
    "verification": "Verification",
    "available_code": "Available code",
    "evaluation_setting": "Evaluation setting",
}
BASES = {
    "paper-report": "Paper report",
    "project-documentation": "Project documentation",
    "code-inspection": "Code inspection",
    "not-established": "Not established",
}


def load_comparisons():
    return json.loads((ROOT / "data/comparisons.json").read_text(encoding="utf-8"))


def validate_comparisons(data, entries):
    errors = []
    systems = {e["id"] for e in entries if e["kind"] == "system"}
    seen = set()
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["comparisons: expected schema_version 1 object"]
    if not isinstance(data.get("scope"), str) or not data["scope"].strip():
        errors.append("comparisons: scope is required")
    records = data.get("systems")
    if not isinstance(records, list) or not records:
        return errors + ["comparisons: systems must be a nonempty list"]
    for value, label in [(data.get("reviewed"), "reviewed")] + [
        (r.get("checked"), r.get("system_id", "record")) for r in records if isinstance(r, dict)
    ]:
        try:
            if (date.fromisoformat(value) - date.today()).days > 1:
                raise ValueError("future date")
        except (ValueError, TypeError):
            errors.append(f"comparisons: invalid date for {label}")
    for record in records:
        if not isinstance(record, dict):
            errors.append("comparisons: each system must be an object")
            continue
        ident = record.get("system_id")
        if ident not in systems or ident in seen:
            errors.append(f"comparisons: unknown or duplicate system {ident}")
        seen.add(ident)
        for field in ("short_name", "limitations"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f"{ident}: {field} is required")
        source_records = record.get("sources", [])
        if not isinstance(source_records, list) or not source_records:
            errors.append(f"{ident}: sources must be nonempty")
            source_records = []
        urls = set()
        for source in source_records:
            if not isinstance(source, dict):
                errors.append(f"{ident}: invalid source")
                continue
            url = source.get("url", "")
            parsed = urlsplit(url)
            if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
                errors.append(f"{ident}: source must be a public HTTPS URL")
            if url in urls:
                errors.append(f"{ident}: duplicate source URL")
            urls.add(url)
            if not source.get("label") or not source.get("locator"):
                errors.append(f"{ident}: source needs a label and a section/file locator")
        dims = record.get("dimensions", {})
        if not isinstance(dims, dict) or set(dims) != set(DIMENSIONS):
            errors.append(f"{ident}: all seven comparison dimensions are required")
            continue
        for dimension, cell in dims.items():
            if not isinstance(cell, dict):
                errors.append(f"{ident}/{dimension}: cell must be an object")
                continue
            if not isinstance(cell.get("text"), str) or not 1 <= len(cell["text"].split()) <= 40:
                errors.append(f"{ident}/{dimension}: concise text is required")
            if cell.get("basis") not in BASES:
                errors.append(f"{ident}/{dimension}: invalid evidence basis")
            citations = cell.get("sources")
            if not isinstance(citations, list) or not citations or any(u not in urls for u in citations):
                errors.append(f"{ident}/{dimension}: cite a source registered for this system")
    missing = systems - seen
    if missing:
        errors.append("comparisons: missing catalog systems: " + ", ".join(sorted(missing)))
    return errors


def cell_text(cell, refs, ident):
    text = cell["text"].replace("|", "\\|").replace("\n", " ")
    numbers = ",".join(str(refs[url]) for url in cell["sources"])
    return f'{text} [{numbers}](#{ident}-sources)'


def render_comparisons(data, entries):
    catalog = {e["id"]: e for e in entries}
    records = {r["system_id"]: r for r in data["systems"]}
    ordered_entries = ordered([catalog[ident] for ident in records])
    text = "# Capability and evidence matrix\n\n"
    text += "[← Overview](../README.md) · [Research synthesis](research-synthesis.md) · [Local reproducibility reports](reproducibility.md)\n\n"
    text += f'**{len(records)} systems · Sources reviewed {data["reviewed"]}.** {data["scope"]}\n\n'
    text += "The tables describe reported or inspected behavior. They do not assign an overall score or establish that one system is scientifically superior. Source numbers resolve to the section/file references below each system. The detailed evidence map records whether each cell comes from a paper, project documentation, code inspection, or an unresolved question.\n\n"
    text += "A code inspection is a static check. A paper report is an author-reported result. Neither means that we reproduced the complete system. **Not established** means the examined sources did not support a stronger statement; it does not prove a capability is absent. See the separate reports for the exact scope of local execution.\n\n"
    text += "Rows follow the recorded publication/release dates, newest first. Year-only records follow precisely dated records in the same year. Memory here distinguishes stored research state from model training; verification distinguishes checks on execution, evidence, and scientific validity.\n\n"
    for heading, keys in [
        ("Research workflow", ["human_involvement", "hypothesis_generation", "experiment_execution", "memory"]),
        ("Evidence and access", ["verification", "available_code", "evaluation_setting"]),
    ]:
        text += f"## {heading}\n\n| System | " + " | ".join(DIMENSIONS[k] for k in keys) + " |\n"
        text += "| " + " | ".join("---" for _ in range(len(keys) + 1)) + " |\n"
        for entry in ordered_entries:
            ident = entry["id"]
            record = records[ident]
            refs = {s["url"]: n for n, s in enumerate(record["sources"], 1)}
            text += f'| [{record["short_name"]}](#{ident})<br>{entry["date"]} | '
            text += " | ".join(cell_text(record["dimensions"][k], refs, ident) for k in keys) + " |\n"
        text += "\n"
    text += "## Evidence notes\n\n"
    for entry in ordered_entries:
        ident = entry["id"]
        record = records[ident]
        refs = {s["url"]: n for n, s in enumerate(record["sources"], 1)}
        text += f'<a id="{ident}"></a>\n\n### {record["short_name"]}\n\n'
        text += f'[Catalog entry](systems.md#{ident}) · Source check: {record["checked"]}.\n\n'
        text += record["limitations"] + "\n\n"
        text += "| Dimension | Evidence basis | Sources |\n| --- | --- | --- |\n"
        for dimension, label in DIMENSIONS.items():
            cell = record["dimensions"][dimension]
            links = " · ".join(f'[{refs[url]}]({url})' for url in cell["sources"])
            text += f'| {label} | {BASES[cell["basis"]]} | {links} |\n'
        text += f'\n<a id="{ident}-sources"></a>\n\n'
        for number, source in enumerate(record["sources"], 1):
            text += f'{number}. [{source["label"]}]({source["url"]}) — {source["locator"]}.\n'
        text += "\n"
    return text.rstrip() + "\n"
