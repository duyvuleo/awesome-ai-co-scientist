"""Versioned full-text appraisals and their public reading index."""
import json
import re
from collections import Counter
from datetime import date
from html import escape
from catalog import ROOT, canonical_identity, ordered


def load_reviews():
    return json.loads((ROOT / "data/full-text-reviews.json").read_text(encoding="utf-8"))


def review_index(data):
    """One catalog record can link to several distinct companion papers."""
    index = {}
    for review in data["reviews"]:
        for ident in review["record_ids"]:
            index.setdefault(ident, []).append(review)
    return index


def validate_reviews(data, entries, public_url):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["full-text reviews: unsupported schema"]
    if not isinstance(data.get("reviews"), list):
        return ["full-text reviews: expected a review array"]
    for field in ("scope", "boundary"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"full-text reviews: missing {field}")
    by_id = {entry["id"]: entry for entry in entries}
    ids, identities, represented = set(), set(), set()
    associated_identities, by_review = {}, {}
    required = {"id", "title", "record_ids", "primary_source", "reading_status", "version",
                "coverage", "reviewed", "methods", "evaluation", "limitations", "sources"}
    for review in data["reviews"]:
        if not isinstance(review, dict) or required - review.keys():
            errors.append("full-text reviews: missing required fields")
            continue
        ident = review["id"]
        label = f"full-text review {ident}"
        if not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident):
            errors.append(f"{label}: invalid id")
            continue
        if ident in ids:
            errors.append(f"{label}: invalid or duplicate id")
        ids.add(ident)
        by_review[ident] = review
        paper_identities = set()
        if not public_url(review["primary_source"]):
            errors.append(f"{label}: invalid primary source")
        else:
            paper_identities.add(canonical_identity(review["primary_source"]))
        aliases = review.get("identity_aliases", [])
        if not isinstance(aliases, list) or not all(public_url(alias) for alias in aliases):
            errors.append(f"{label}: invalid verified identity aliases")
        else:
            paper_identities.update(canonical_identity(alias) for alias in aliases)
        if identities & paper_identities:
            errors.append(f"{label}: duplicate paper identity")
        identities.update(paper_identities)
        records = review["record_ids"]
        if (not isinstance(records, list) or not records
                or not all(isinstance(record, str) for record in records)
                or len(set(records)) != len(records)
                or any(record not in by_id for record in records)):
            errors.append(f"{label}: invalid catalog associations")
        else:
            represented.update(records)
            for record in records:
                associated_identities.setdefault(record, set()).update(paper_identities)
        if not isinstance(review["reading_status"], str) or review["reading_status"] not in {"full-text", "partial", "incomplete"}:
            errors.append(f"{label}: invalid reading status")
        for field in ("title", "version", "coverage", "methods", "evaluation", "limitations"):
            if not isinstance(review[field], str) or not review[field].strip():
                errors.append(f"{label}: missing {field}")
        if "reviewer_check" in review and (not isinstance(review["reviewer_check"], str)
                                           or not review["reviewer_check"].strip()):
            errors.append(f"{label}: reviewer_check must be a nonempty string")
        try:
            if (date.fromisoformat(review["reviewed"]) - date.today()).days > 1:
                raise ValueError("future date")
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid review date")
        sources = review["sources"]
        if not isinstance(sources, list) or not sources:
            errors.append(f"{label}: missing inspected sources")
            continue
        for source in sources:
            if (not isinstance(source, dict) or not public_url(source.get("url"))
                    or not isinstance(source.get("label"), str) or not source["label"].strip()
                    or not isinstance(source.get("locator"), str) or not source["locator"].strip()):
                errors.append(f"{label}: source needs a public URL, label, and locator")
    # A collection-wide appraisal must account for every core paper, including gaps.
    for entry in entries:
        if entry["kind"] == "paper" and entry["id"] not in represented:
            errors.append(f"full-text reviews: unaccounted paper {entry['id']}")
        elif entry["kind"] == "paper" and canonical_identity(entry.get("url", "")) not in associated_identities.get(entry["id"], set()):
            errors.append(f"full-text reviews: missing primary appraisal for {entry['id']}")
    # Preserve the explicit audit inventory, including linked-only publications.
    targets = data.get("coverage_targets")
    if not isinstance(targets, list) or not targets:
        errors.append("full-text reviews: missing coverage inventory")
        targets = []
    target_ids = set()
    for target in targets:
        if (not isinstance(target, dict) or not isinstance(target.get("id"), str)
                or not public_url(target.get("primary_source"))
                or not isinstance(target.get("record_ids"), list)
                or not target["record_ids"]
                or not all(isinstance(record, str) and record in by_id for record in target["record_ids"])):
            errors.append("full-text reviews: invalid coverage target")
            continue
        ident = target["id"]
        if ident in target_ids:
            errors.append(f"full-text reviews: duplicate coverage target {ident}")
        target_ids.add(ident)
        review = by_review.get(ident)
        if review is None:
            errors.append(f"full-text reviews: unaccounted target {ident}")
        elif (not public_url(review["primary_source"])
              or not isinstance(review["record_ids"], list)
              or not all(isinstance(record, str) for record in review["record_ids"])
              or canonical_identity(target["primary_source"]) != canonical_identity(review["primary_source"])
              or set(target["record_ids"]) != set(review["record_ids"])):
            errors.append(f"full-text reviews: coverage target mismatch {ident}")
    for ident in ids - target_ids:
        errors.append(f"full-text reviews: review outside declared inventory {ident}")
    return errors


def render_reviews(data, entries):
    by_id = {entry["id"]: entry for entry in entries}
    reviews = data["reviews"]
    counts = Counter(review["reading_status"] for review in reviews)
    text = "<!-- Generated by scripts/render.py from data/full-text-reviews.json. -->\n"
    text += "# Full-text reading notes\n\n[← Overview](../README.md) · [Papers](papers.md) · [Capability matrix](capability-matrix.md)\n\n"
    text += data["scope"] + "\n\n" + data["boundary"] + "\n\n"
    text += "| Reading coverage | Papers |\n| --- | ---: |\n"
    for status, label in (("full-text", "Full text appraised"), ("partial", "Partial appraisal; access gaps"), ("incomplete", "Appraisal incomplete")):
        text += f"| {label} | {counts[status]} |\n"
    text += "\n**Full text** covers the stated version’s methods, results, tables, figures, and substantive attached appendices. Coverage notes identify unavailable supplements, publication-version differences, and excluded raw artifacts. Reading is not execution or independent reproduction.\n\n"
    text += "The following notes separate the proposed mechanism, reported evaluation, and limits of interpretation. Findings are author-reported unless a reviewer calculation is explicitly identified.\n\n"
    # Use catalog dates, preserving date precision and newest-first ordering.
    dated = []
    for review in reviews:
        entry = by_id[review["record_ids"][0]]
        dated.append({**entry, "id": review["id"], "name": review["title"], "review": review})
    text += "## Index\n\nOrder follows associated catalog dates; these are not inferred publication dates for companion papers.\n\n| Catalog date | Work | Reading coverage |\n| --- | --- | --- |\n"
    labels = {"full-text": "Full text", "partial": "Partial", "incomplete": "Incomplete"}
    for entry in ordered(dated):
        review = entry["review"]
        title = escape(entry["name"], quote=False).replace("|", "&#124;").replace("\n", "<br>")
        text += f"| {entry['date']} | [{title}](#{review['id']}) | {labels[review['reading_status']]} |\n"
    for entry in ordered(dated):
        review = entry["review"]
        heading = escape(entry["name"], quote=False).replace("\n", " ")
        text += f"\n<a id=\"{review['id']}\"></a>\n\n## {heading}\n\n"
        text += (f"**Version:** {escape(review['version'])}. "
                 f"**Reading status:** {labels[review['reading_status']]}. "
                 f"**Recorded:** {review['reviewed']}. **Coverage:** {escape(review['coverage'])}\n\n")
        text += "| Aspect | Appraisal |\n| --- | --- |\n"
        for key, label in (("methods", "Method"), ("evaluation", "Evaluation"), ("limitations", "Interpretation and limits")):
            value = escape(review[key], quote=False).replace("|", "&#124;").replace("\n", "<br>")
            text += f"| {label} | {value} |\n"
        if review.get("reviewer_check"):
            text += "\n**Reviewer mathematical check.** " + escape(review["reviewer_check"], quote=False) + "\n"
        text += "\nSources: " + " · ".join(f"[{escape(s['label'])}]({s['url']}) — {escape(s['locator'])}" for s in review["sources"]) + ".\n"
        links = []
        for ident in review["record_ids"]:
            record = by_id[ident]
            page = {"paper": "papers", "system": "systems", "tool": "tools", "benchmark": "benchmarks"}[record["kind"]]
            links.append(f"[{escape(record['name'])}]({page}.md#{ident})")
        text += "\nCatalog: " + " · ".join(links) + ".\n"
    return text
