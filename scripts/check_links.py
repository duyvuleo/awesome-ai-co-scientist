"""Check public catalog links. Failures need review; no entries are modified."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from catalog import load
from comparison import load_comparisons


def check(url):
    try:
        request = Request(url, headers={"User-Agent": "awesome-ai-co-scientist-link-check/1.0"})
        with urlopen(request, timeout=25) as response:
            return {"url": url, "status": response.status, "final_url": response.url, "result": "reachable"}
    except HTTPError as exc:
        return {"url": url, "status": exc.code, "result": "review"}
    except (URLError, TimeoutError, OSError) as exc:
        return {"url": url, "status": None, "result": "review", "detail": str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=".local/link-report.json")
    parser.add_argument("--ids", nargs="*", help="Only check these catalog IDs")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero for any URL needing review")
    args = parser.parse_args()
    entries = load()
    if args.ids:
        unknown = set(args.ids) - {e["id"] for e in entries}
        if unknown:
            parser.error("Unknown IDs: " + ", ".join(sorted(unknown)))
        entries = [e for e in entries if e["id"] in args.ids]
    urls = {u for e in entries for u in e["sources"] + [e[k] for k in ("url", "code_url", "paper_url") if e.get(k)]}
    for record in load_comparisons()["systems"]:
        if not args.ids or record["system_id"] in args.ids:
            urls.update(s["url"] for s in record["sources"])
    urls = sorted(urls)
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(check, urls))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "results": results}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n")
    failed = [r for r in results if r["result"] != "reachable"]
    print(f"Checked {len(urls)} URLs: {len(urls) - len(failed)} reachable; {len(failed)} need review. Report: {path}")
    for r in failed:
        print(f'{r["status"] or "network"}: {r["url"]}')
    if args.strict and failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
