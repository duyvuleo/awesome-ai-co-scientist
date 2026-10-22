"""Shared catalog loading. Standard library only."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, unquote_plus, urlsplit, urlunsplit

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



def _arxiv_id(value):
    # Modern IDs and the pre-April-2007 archive/number form; reject other routes.
    match = re.fullmatch(r"(\d{4}\.\d{4,5}|[a-z][a-z.-]*/\d{7})(?:v[1-9]\d*)?", value, re.ASCII | re.IGNORECASE)
    return match.group(1).lower() if match else None


def canonical_identity(url):
    """Normalize known identifiers offline; preserve unknown resource distinctions."""
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    try:
        port = parsed.port
    except ValueError:
        return "url:" + url
    default_port = port is None or (parsed.scheme, port) in {
        ("https", 443), ("http", 80),
    }
    identifier_host = (parsed.scheme in {"https", "http"} and default_port
                       and not parsed.username and not parsed.password)
    if identifier_host and host in {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}:
        match = re.fullmatch(r"/(?:abs|html|pdf)/(.+?)/?", unquote(parsed.path))
        if match:
            ident = _arxiv_id(match.group(1).removesuffix(".pdf"))
            if ident:
                return "arxiv:" + ident
    if identifier_host and host in {"doi.org", "www.doi.org", "dx.doi.org"}:
        # DOI comparison uses ASCII case folding, not Unicode case folding.
        doi = unquote(parsed.path).removeprefix("/").translate(
            str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"))
        if re.fullmatch(r"10\.\d{4,9}/\S+", doi):
            if doi.startswith("10.48550/arxiv."):
                ident = _arxiv_id(doi.removeprefix("10.48550/arxiv."))
                if ident:
                    return "arxiv:" + ident
            return "doi:" + doi
    # Drop tracking fields only. Preserve meaningful query order and encoding.
    query = "&".join(part for part in parsed.query.split("&") if part and not (
        unquote_plus(part.partition("=")[0]).lower().startswith("utm_") or
        unquote_plus(part.partition("=")[0]).lower() in {"fbclid", "gclid"}
    ))
    if identifier_host and host in {"github.com", "www.github.com"}:
        parts = parsed.path.strip("/").split("/")
        if len(parts) == 2 and all(parts):
            owner, repo = (part.lower() for part in parts)
            return "github:" + owner + "/" + repo.removesuffix(".git") + ("?" + query if query else "")
    # Unknown sites can use path case, trailing slashes, query values, and hash
    # routes to distinguish works. Do not infer aliases or strip those details.
    netloc = host if default_port else parsed.netloc
    if parsed.username or parsed.password:
        netloc = parsed.netloc
    return "url:" + urlunsplit((parsed.scheme, netloc, parsed.path or "/", query, parsed.fragment))


def recent_groups(entries):
    """Group one view per kind of a primary work; leave ambiguous buckets separate."""
    ranked = recent(entries)
    rank = {entry["id"]: index for index, entry in enumerate(ranked)}
    buckets = {}
    for entry in ranked:
        key = canonical_identity(entry.get("paper_url") or entry["url"])
        buckets.setdefault(key, []).append(entry)
    groups = []
    for bucket in buckets.values():
        # Two systems or benchmarks can cite the same paper yet be distinct
        # releases/tasks. A shared citation alone cannot establish equivalence.
        kinds = [entry["kind"] for entry in bucket]
        if len(set(kinds)) != len(kinds):
            groups.extend([[entry] for entry in bucket])
        else:
            groups.append(sorted(bucket, key=lambda entry: entry["kind"] != "paper"))
    return sorted(groups, key=lambda group: min(rank[entry["id"]] for entry in group))
