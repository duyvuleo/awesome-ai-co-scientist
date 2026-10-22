"""Shared catalog loading. Standard library only."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ("papers.json", "systems-tools.json", "benchmarks.json")
CATEGORIES = {
    "end-to-end": "End-to-end research",
    "hypothesis": "Hypothesis and idea generation",
    "domain-science": "Domain science and laboratories",
    "survey": "Surveys and perspectives",
    "literature": "Literature discovery and synthesis",
    "ideation": "Ideation and planning",
    "experimentation": "Experimentation and implementation",
    "writing": "Writing and scientific communication",
    "infrastructure": "Research infrastructure",
    "benchmark": "Benchmarks and evaluation",
}


def load():
    entries = []
    for name in CATALOGS:
        value = json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
        if not isinstance(value, list):
            raise ValueError(f"{name}: expected a JSON array")
        entries.extend(value)
    return entries


def ordered(entries):
    """Newest source dates first; year-only dates follow dated items in that year."""
    def key(entry):
        parts = [int(part) for part in entry["date"].split("-")]
        year, month, day = (parts + [0, 0])[:3]
        return (-year, -month, -day, entry["name"].casefold(), entry["id"])

    return sorted(entries, key=key)


def recent(entries):
    """Newest catalog additions first; retain source-date order within each day."""
    return sorted(ordered(entries), key=lambda entry: entry["added_on"], reverse=True)


def recent_groups(entries):
    """Group catalog views of the same primary work, not merely related projects."""
    groups = {}
    for entry in recent(entries):
        url = entry.get("paper_url") or entry["url"]
        parsed = urlsplit(url)
        key = url.rstrip("/")
        if parsed.hostname in {"arxiv.org", "www.arxiv.org"}:
            path = re.sub(r"^/(?:abs|html|pdf)/", "", parsed.path)
            key = "arxiv:" + re.sub(r"v\d+$", "", path.removesuffix(".pdf"))
        groups.setdefault(key, []).append(entry)
    # A paper provides the summary; links retain each system/tool/benchmark view.
    return [sorted(group, key=lambda entry: entry["kind"] != "paper")
            for group in groups.values()]
