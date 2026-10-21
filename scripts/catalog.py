"""Shared catalog loading. Standard library only."""
import json
from pathlib import Path

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
    return sorted(entries, key=lambda x: (-x["year"], x["name"].casefold(), x["id"]))
