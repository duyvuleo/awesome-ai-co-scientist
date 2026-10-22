"""Create study plans and validate recorded evidence. Python 3.10+, no execution or network."""
import argparse
import hashlib
import json
import math
import re
from datetime import date, datetime
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from catalog import ROOT, load

RECIPES = ("evaluator-integrity", "idea-to-experiment", "human-ai-collaboration")
TEXT_FIELDS = ("question", "declared_claim", "human_role", "unit_of_analysis",
               "success_criteria", "stopping_rule", "seed_policy", "exclusions")


class InvalidPack(ValueError):
    """A plan or record does not satisfy the public study-pack contract."""


def require(condition, field, message):
    if not condition:
        raise InvalidPack(f"{field}: {message}")


def text(value):
    return isinstance(value, str) and bool(value.strip())


def number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def strings(value, nonempty=False):
    return isinstance(value, list) and (bool(value) or not nonempty) and all(text(v) for v in value)


def public_url(value):
    if not text(value):
        return False
    parsed = urlsplit(value)
    host = parsed.hostname or ""
    return (parsed.scheme == "https" and "." in host and not parsed.username
            and not parsed.password and not re.search(r"\s", value)
            and host not in {"127.0.0.1", "0.0.0.0"}
            and not host.endswith((".local", ".internal")))


def fields(value, required, label):
    require(isinstance(value, dict), label, "must be an object")
    require(set(value) == set(required), label, "has missing or unsupported fields")


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def timestamp(value, label):
    require(text(value), label, "must be an ISO timestamp with timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidPack(f"{label}: invalid timestamp") from exc
    require(parsed.tzinfo is not None, label, "timezone is required")
    return parsed


def artifact_path(root, value):
    require(text(value), "artifact.path", "must be a relative POSIX file path")
    path = PurePosixPath(value)
    require(not path.is_absolute() and "\\" not in value and ":" not in value
            and all(part not in {"", ".", ".."} for part in value.split("/")),
            "artifact.path", "absolute paths, traversal, and ambiguous separators are forbidden")
    candidate = root.joinpath(*path.parts)
    require(candidate.resolve().is_relative_to(root.resolve()), "artifact.path", "must stay inside the pack")
    cursor = root
    for part in path.parts:
        cursor /= part
        require(not cursor.is_symlink(), "artifact.path", "symlinks are forbidden")
    require(candidate.is_file(), "artifact.path", "file does not exist")
    require(value != "run-record.json", "artifact.path", "the record cannot be its own evidence")
    return candidate


def make_record(recipe, resource_ids):
    require(recipe in RECIPES, "recipe", "unknown recipe")
    catalog = {item["id"]: item for item in load() if item["kind"] in {"system", "tool"}}
    require(bool(resource_ids) and len(set(resource_ids)) == len(resource_ids),
            "resources", "provide distinct system or tool IDs")
    require(all(item in catalog for item in resource_ids), "resources", "unknown system or tool ID")
    resources = []
    for resource_id in resource_ids:
        item = catalog[resource_id]
        resources.append({"id": item["id"], "name": item["name"], "kind": item["kind"],
                          "url": item["url"], "sources": item["sources"],
                          "catalog_checked": item["checked"]})
    protocol = {key: None for key in TEXT_FIELDS}
    protocol.update({"baselines": [], "controls": [], "configuration": {}, "seeds": [],
                     "sample_size": None, "budget": {"paid_api_usd": 0,
                         "max_wall_seconds": None, "max_local_compute_hours": None,
                         "max_human_hours": None}})
    return {"schema_version": 1, "status": "planned", "recipe": recipe,
            "resources": resources, "protocol": protocol, "execution": None,
            "actual": {"cost": None, "results": None, "failures": None,
                       "claim_outcomes": None, "artifacts": []}}


def create_pack(recipe, resource_ids, output):
    record = make_record(recipe, resource_ids)
    method = (ROOT / "templates" / "study" / f"{recipe}.md").read_text(encoding="utf-8")
    selected = "\n".join(f"- [{r['name']}]({r['url']}) — `{r['id']}`; catalog source check: "
                         f"{r['catalog_checked']} (copied snapshot, not a new check)."
                         for r in record["resources"])
    protocol = (f"# Study protocol: {recipe}\n\n**Planned; no experiment has been executed by this tool.**\n\n"
                f"## Selected resources\n\n{selected}\n\n"
                "## Before execution\n\nComplete the `protocol` fields in `run-record.json` before running anything. "
                "Record the question, scoped claim, human role, unit of analysis, baselines, controls, "
                "configuration, seeds, sample size, success criteria, stopping rule, exclusions, and budgets. "
                "The paid API budget defaults to USD 0. Declare any independently authorized budget before execution. "
                "Local compute and researcher time still have costs.\n\n" + method)
    readme = ("# Local study pack\n\nThis directory starts as an unexecuted plan. The generator does not install "
              "dependencies, invoke models, run upstream code, or collect logs.\n\n"
              "1. Read `protocol.md` and fill the protocol in `run-record.json`.\n"
              "2. Save the completed protocol before execution; record any later deviations.\n"
              "3. Execute only the work you have independently chosen and are authorized to run.\n"
              "4. Record observations, failures, timings, cost basis, pinned source revisions, and scoped claims. "
              "Add only deliberately selected, sanitized artifacts and their SHA-256 hashes.\n"
              "5. Mark `status` as `completed` only after execution and validate from the repository with "
              "`python3 scripts/study_pack.py validate PACK_DIRECTORY`.\n\n"
              "Use the repository's `docs/study-packs.md` for the field contract. Validation checks record "
              "structure and artifact integrity; it cannot prove execution, scientific validity, or that "
              "files contain no sensitive information. Review every file before sharing. Never include "
              "credentials, personal data, private paths, or raw logs copied automatically.\n")
    # Fail before writing anything if a target, including a broken symlink, already exists.
    output.mkdir(parents=True, exist_ok=False)
    for name, content in (("protocol.md", protocol), ("README.md", readme),
                          ("run-record.json", json.dumps(record, indent=2, ensure_ascii=False) + "\n")):
        with (output / name).open("x", encoding="utf-8") as handle:
            handle.write(content)
    return record


def validate_pack(root):
    require(root.is_dir(), "pack", "must be a directory")
    for name in ("run-record.json", "protocol.md", "README.md"):
        require((root / name).is_file() and not (root / name).is_symlink(), name, "must be a regular file")
    def invalid_constant(_):
        raise InvalidPack("record: NaN and Infinity are forbidden")
    def unique_fields(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "record", "duplicate JSON fields are forbidden")
            result[key] = value
        return result
    record = json.loads((root / "run-record.json").read_text(encoding="utf-8"),
                        parse_constant=invalid_constant, object_pairs_hook=unique_fields)
    fields(record, ("schema_version", "status", "recipe", "resources", "protocol", "execution", "actual"), "record")
    require(type(record["schema_version"]) is int and record["schema_version"] == 1, "schema_version", "must be 1")
    require(record["status"] in ("planned", "completed"), "status", "must be planned or completed")
    require(record["recipe"] in RECIPES, "recipe", "unknown recipe")
    completed = record["status"] == "completed"
    resources = record["resources"]
    require(isinstance(resources, list) and bool(resources), "resources", "must be a nonempty list")
    resource_ids = set()
    for resource in resources:
        fields(resource, ("id", "name", "kind", "url", "sources", "catalog_checked"), "resource")
        require(text(resource["id"]) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", resource["id"]), "resource.id", "invalid ID")
        require(resource["id"] not in resource_ids, "resource.id", "must be unique")
        resource_ids.add(resource["id"])
        require(text(resource["name"]) and resource["kind"] in ("system", "tool"), "resource", "invalid name or kind")
        require(public_url(resource["url"]) and strings(resource["sources"], True)
                and all(public_url(url) for url in resource["sources"])
                and resource["url"] in resource["sources"], "resource.sources", "use public HTTPS sources without embedded usernames or passwords")
        try:
            date.fromisoformat(resource["catalog_checked"])
        except (TypeError, ValueError) as exc:
            raise InvalidPack("resource.catalog_checked: invalid date") from exc
    protocol = record["protocol"]
    fields(protocol, (*TEXT_FIELDS, "baselines", "controls", "configuration", "seeds", "sample_size", "budget"), "protocol")
    for key in TEXT_FIELDS:
        require(text(protocol[key]) or (protocol[key] is None and not completed), f"protocol.{key}", "must be filled before completion")
    for key in ("baselines", "controls"):
        require(strings(protocol[key], completed), f"protocol.{key}", "must list declared comparisons; explain any inapplicable comparison")
    require(isinstance(protocol["configuration"], dict) and (bool(protocol["configuration"]) or not completed), "protocol.configuration", "must describe the planned configuration")
    require(isinstance(protocol["seeds"], list) and all(type(seed) is int and seed >= 0 for seed in protocol["seeds"]), "protocol.seeds", "must contain nonnegative integers")
    require((type(protocol["sample_size"]) is int and protocol["sample_size"] > 0)
            or (protocol["sample_size"] is None and not completed), "protocol.sample_size", "must be a positive integer before completion")
    fields(protocol["budget"], ("paid_api_usd", "max_wall_seconds", "max_local_compute_hours", "max_human_hours"), "protocol.budget")
    require(number(protocol["budget"]["paid_api_usd"]), "protocol.budget.paid_api_usd", "declare a nonnegative budget; new plans default to zero")
    for key in ("max_wall_seconds", "max_local_compute_hours", "max_human_hours"):
        require(number(protocol["budget"][key]) or (protocol["budget"][key] is None and not completed), f"protocol.budget.{key}", "declare a nonnegative limit before completion")
    actual = record["actual"]
    fields(actual, ("cost", "results", "failures", "claim_outcomes", "artifacts"), "actual")
    require(isinstance(actual["artifacts"], list), "actual.artifacts", "must be a list")
    if not completed:
        require(record["execution"] is None and all(actual[key] is None for key in ("cost", "results", "failures", "claim_outcomes"))
                and not actual["artifacts"], "planned", "unobserved execution and outcomes must remain null, with no evidence artifacts")
        return record
    execution = record["execution"]
    fields(execution, ("started_at", "ended_at", "environment", "commands", "configuration", "upstream_versions", "data_provenance", "deviations"), "execution")
    start = timestamp(execution["started_at"], "execution.started_at")
    end = timestamp(execution["ended_at"], "execution.ended_at")
    require(end >= start, "execution.ended_at", "must not precede started_at")
    fields(execution["environment"], ("os", "runtime", "hardware", "dependencies"), "execution.environment")
    require(all(text(value) for value in execution["environment"].values()), "execution.environment", "describe OS, runtime, hardware, and dependency versions without private paths")
    require(strings(execution["commands"], True), "execution.commands", "record portable commands")
    require(isinstance(execution["configuration"], dict) and bool(execution["configuration"]), "execution.configuration", "record the actual configuration")
    require(text(execution["data_provenance"]) and strings(execution["deviations"]), "execution", "record data provenance and deviations, including budget overruns")
    require(isinstance(execution["upstream_versions"], list), "execution.upstream_versions", "must be a list")
    version_ids = set()
    for version in execution["upstream_versions"]:
        fields(version, ("resource_id", "url", "revision_type", "revision", "scope"), "upstream_version")
        require(text(version["resource_id"]) and version["resource_id"] in resource_ids
                and version["resource_id"] not in version_ids, "upstream_version.resource_id", "must identify one selected resource exactly once")
        version_ids.add(version["resource_id"])
        revision_type = version["revision_type"]
        length = 40 if revision_type == "git-commit" else 64
        require(revision_type in ("git-commit", "sha256") and text(version["revision"])
                and re.fullmatch(r"[a-f0-9]{" + str(length) + r"}", version["revision"]), "upstream_version.revision", "use a full Git commit or SHA-256 content hash")
        require(public_url(version["url"]) and text(version["scope"]), "upstream_version", "record the public source and exact executed scope")
    require(version_ids == resource_ids, "execution.upstream_versions", "every selected resource requires a pinned revision")
    cost = actual["cost"]
    fields(cost, ("paid_api_usd", "wall_seconds", "local_compute_hours", "human_hours", "basis", "excluded_costs"), "actual.cost")
    require(number(cost["paid_api_usd"]), "actual.cost.paid_api_usd", "record a nonnegative observed charge")
    require(number(cost["wall_seconds"]), "actual.cost.wall_seconds", "must be nonnegative")
    for key in ("local_compute_hours", "human_hours"):
        require(cost[key] is None or number(cost[key]), f"actual.cost.{key}", "must be nonnegative or null when unmeasured")
    require(text(cost["basis"]) and text(cost["excluded_costs"]), "actual.cost", "explain measurement, zero API charges, and excluded or unmeasured costs")
    overruns = cost["paid_api_usd"] > protocol["budget"]["paid_api_usd"] or any(cost[key] is not None and cost[key] > protocol["budget"][f"max_{key}"]
                   for key in ("wall_seconds", "local_compute_hours", "human_hours"))
    require(not overruns or bool(execution["deviations"]), "execution.deviations", "explain observed budget overruns")
    require(strings(actual["failures"]), "actual.failures", "record failures, or an empty list when none were observed")
    artifact_names = set()
    require(bool(actual["artifacts"]), "actual.artifacts", "completed records require evidence files")
    for artifact in actual["artifacts"]:
        fields(artifact, ("path", "sha256", "description"), "artifact")
        path = artifact_path(root, artifact["path"])
        require(artifact["path"] not in artifact_names, "artifact.path", "must be unique")
        artifact_names.add(artifact["path"])
        require(text(artifact["sha256"]) and re.fullmatch(r"[a-f0-9]{64}", artifact["sha256"])
                and digest(path) == artifact["sha256"], "artifact.sha256", "must match the existing file")
        require(text(artifact["description"]), "artifact.description", "describe the evidence")
    def references(value, label, required=True):
        require(strings(value, required) and all(path in artifact_names for path in value), label, "reference recorded evidence artifact paths")
    require(isinstance(actual["results"], list) and bool(actual["results"]), "actual.results", "record at least one observed result, including unsuccessful execution")
    for result in actual["results"]:
        fields(result, ("observation", "artifact_paths"), "result")
        require(text(result["observation"]), "result.observation", "describe the actual observation")
        references(result["artifact_paths"], "result.artifact_paths")
    require(isinstance(actual["claim_outcomes"], list) and bool(actual["claim_outcomes"]), "actual.claim_outcomes", "record scoped outcomes")
    for claim in actual["claim_outcomes"]:
        fields(claim, ("claim", "outcome", "scope", "artifact_paths"), "claim_outcome")
        require(text(claim["claim"]) and text(claim["scope"])
                and claim["outcome"] in ("supported", "not-supported", "inconclusive", "not-tested"), "claim_outcome", "state the scoped claim and supported, not-supported, inconclusive, or not-tested outcome")
        references(claim["artifact_paths"], "claim_outcome.artifact_paths", claim["outcome"] != "not-tested")
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("create", help="create an unexecuted study plan")
    create.add_argument("--recipe", choices=RECIPES, required=True)
    create.add_argument("--resources", "--systems", dest="resources", nargs="+", required=True,
                        help="existing system or tool IDs; --systems is an alias")
    create.add_argument("--output", type=Path, required=True)
    validate = commands.add_parser("validate", help="check schema and artifact integrity")
    validate.add_argument("directory", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            create_pack(args.recipe, args.resources, args.output)
            print("Created a planned study pack. No experiment was executed.")
        else:
            record = validate_pack(args.directory)
            print(f"Valid {record['status']} study pack: structure and artifact integrity only; execution and scientific claims are not certified.")
    except (InvalidPack, OSError, ValueError) as exc:
        # Do not echo private absolute output paths from filesystem exception messages.
        message = "filesystem operation failed (check existence and permissions)" if isinstance(exc, OSError) else str(exc)
        parser.exit(1, f"Study pack error: {message}\n")


if __name__ == "__main__":
    main()
