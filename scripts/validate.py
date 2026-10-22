"""Validate the catalog and local Markdown destinations without network access."""
import re
from datetime import date
from html import unescape
from urllib.parse import urlsplit, unquote
from catalog import ROOT, CATEGORIES, load
from comparison import load_comparisons, validate_comparisons


def public_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    host = parsed.hostname or ""
    return (parsed.scheme == "https" and "." in host and not parsed.username
            and not parsed.password and not re.search(r"\s", value)
            and host not in {"localhost", "127.0.0.1", "0.0.0.0"}
            and not host.endswith((".local", ".internal")))


def main():
    errors = []
    try:
        entries = load()
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
    ids, keys = set(), set()
    required = {"id", "name", "kind", "category", "year", "date", "url", "summary", "evidence", "tags", "sources", "checked", "added_on"}
    for i, e in enumerate(entries):
        label = e.get("id", f"record {i}") if isinstance(e, dict) else f"record {i}"
        if not isinstance(e, dict) or required - e.keys():
            errors.append(f"{label}: missing required fields or invalid record")
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", e["id"]) or e["id"] in ids:
            errors.append(f"{label}: invalid or duplicate id")
        ids.add(e["id"])
        if e["kind"] not in {"paper", "system", "tool", "benchmark"}:
            errors.append(f"{label}: invalid kind")
        if e["category"] not in CATEGORIES:
            errors.append(f"{label}: invalid category")
        if e["evidence"] not in {"preprint", "peer-reviewed", "project"}:
            errors.append(f"{label}: invalid source status")
        if not isinstance(e["year"], int) or not 1900 <= e["year"] <= date.today().year:
            errors.append(f"{label}: invalid year")
        if not isinstance(e["date"], str) or not re.fullmatch(r"\d{4}(?:-\d{2}-\d{2})?", e["date"]):
            errors.append(f"{label}: invalid date precision")
        elif not e["date"].startswith(str(e["year"])):
            errors.append(f"{label}: date and year disagree")
        for key in ("date", "checked", "added_on"):
            try:
                value = e[key]
                if key == "date" and len(value) == 4:
                    continue
                parsed = date.fromisoformat(value)
                # Client timezone can be one day ahead of a UTC CI host.
                if (parsed - date.today()).days > 1:
                    raise ValueError("future date")
            except (ValueError, TypeError):
                errors.append(f"{label}: invalid {key}")
        if not isinstance(e["summary"], str) or not 25 <= len(e["summary"].split()) <= 85:
            errors.append(f"{label}: summary must have 25–85 words")
        if not e["tags"] or not isinstance(e["tags"], list) or not all(isinstance(t, str) and t for t in e["tags"]):
            errors.append(f"{label}: tags must be nonempty strings")
        if not isinstance(e["sources"], list) or not e["sources"]:
            errors.append(f"{label}: sources must be a nonempty list")
            continue
        urls = e["sources"] + [e[k] for k in ("url", "code_url", "paper_url") if e.get(k)]
        if not all(public_url(u) for u in urls):
            errors.append(f"{label}: invalid public HTTPS URL")
        if e["url"] not in e["sources"]:
            errors.append(f"{label}: canonical URL must be in sources")
        canonical = e["url"].rstrip("/").lower()
        if urlsplit(canonical).hostname in {"arxiv.org", "www.arxiv.org"}:
            canonical = re.sub(r"v\d+$", "", canonical)
        key = (e["kind"], canonical)
        if key in keys:
            errors.append(f"{label}: duplicate canonical URL within kind")
        keys.add(key)
    for e in entries:
        if not isinstance(e, dict):
            continue
        for ident in e.get("related", []):
            if ident not in ids or ident == e.get("id"):
                errors.append(f'{e.get("id")}: invalid related id {ident}')
    featured = ROOT / "data" / "featured.txt"
    if featured.exists():
        for ident in featured.read_text().splitlines():
            if ident and not ident.startswith("#") and ident not in ids:
                errors.append(f"Unknown featured id: {ident}")
    try:
        errors.extend(validate_comparisons(load_comparisons(), entries))
    except (ValueError, OSError) as exc:
        errors.append(f"comparisons: {exc}")
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        contents = path.read_text(encoding="utf-8")
        targets = re.findall(r"\]\(([^)\s]+)\)", contents)
        targets += [unescape(value) for value in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', contents)]
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
                continue
            if parsed.fragment and resolved.suffix == ".md":
                contents = resolved.read_text(encoding="utf-8")
                anchors = set(re.findall(r'<a id="([^"]+)"', contents))
                for heading in re.findall(r"^#{1,6}\s+(.+)$", contents, re.M):
                    anchors.add(re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-"))
                if unquote(parsed.fragment) not in anchors:
                    errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(entries)} records, IDs, dates, sources, relationships, and local Markdown links.")


if __name__ == "__main__":
    main()
