"""Execute only PaperOrchestra's pinned citation scorer on synthetic cache inputs.

The exact method AST is executed unchanged, while imports, class construction,
environment loading, PDF extraction, identifier resolution and LLM calls are
bypassed. This does not install or reproduce the PaperOrchestra pipeline.
"""

from __future__ import annotations

import argparse
import ast
import contextlib
import hashlib
import io
import itertools
import json
import math
import os
from pathlib import Path
import tempfile
import time
from types import SimpleNamespace
from typing import Dict

from reproduce_common import ROOT, SOURCES, environment, execution_time, source_tree, write_json


def load_scoring_method(path: Path):
    text = path.read_text()
    tree = ast.parse(text)
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef)
               and node.name == "ReferenceF1V1Evaluator")
    method = next(node for node in cls.body if isinstance(node, ast.FunctionDef)
                  and node.name == "evaluate_from_data")
    exact_source = ast.get_source_segment(text, method)
    ast_dump = ast.dump(method, include_attributes=False)
    module = ast.Module(body=[method], type_ignores=[])
    # The same node is used without edits, stubs or replacements in its body.
    assert ast.dump(module.body[0], include_attributes=False) == ast_dump
    namespace = {"os": os, "json": json, "Dict": Dict}
    exec(compile(module, "autoraters/citation_f1.py", "exec"), namespace)
    return namespace[method.name], {
        "class": cls.name, "method": method.name,
        "source_line_start": method.lineno, "source_line_end": method.end_lineno,
        "method_source_sha256": hashlib.sha256(exact_source.encode()).hexdigest(),
        "method_ast_sha256": hashlib.sha256(ast_dump.encode()).hexdigest(),
        "method_ast_unchanged": True, "full_module_imported": False,
    }


def oracle(gt_ids, gen_ids, p0_ids, p1_ids):
    """Independent count formula for valid resolved-ID inputs."""
    truth, generated = frozenset(gt_ids), frozenset(gen_ids)
    matches = len(truth & generated)
    return {"overall_precision": matches / len(generated) if generated else 0.0,
            "overall_recall": matches / len(truth) if truth else 0.0,
            "overall_f1": 2 * matches / (len(truth) + len(generated)) if truth or generated else 0.0,
            "p0_recall": len(frozenset(p0_ids) & generated) / len(p0_ids) if p0_ids else 0.0,
            "p1_recall": len(frozenset(p1_ids) & generated) / len(p1_ids) if p1_ids else 0.0}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch-only", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / ".local/repro-runs/citation-f1")
    args = parser.parse_args()
    source = source_tree("citation_f1", args.fetch_only)
    if args.fetch_only:
        print("Verified pinned public citation scorer source; no code executed.")
        return
    started = time.perf_counter()
    scorer, extraction = load_scoring_method(source / "autoraters/citation_f1.py")
    gt = {"all_ids": ["A", "B", "C", "D"], "p0_ids": ["A", "B"], "p1_ids": ["C", "D"]}
    fixtures = [
        {"name": "exact_match", "gt": gt, "gen": {"all_ids": ["A", "B", "C", "D"]}},
        {"name": "only_priority_zero", "gt": gt, "gen": {"all_ids": ["A", "B"]}},
        {"name": "partial_with_extra", "gt": gt, "gen": {"all_ids": ["A", "C", "X"]}},
        {"name": "duplicate_generated_ids", "gt": gt, "gen": {"all_ids": ["A", "A", "B", "A"]}},
        {"name": "unresolved_generated_ids", "gt": gt,
         "gen": {"all_ids": ["A", "B", "gen_NA", "", None]}},
        {"name": "empty_generated", "gt": gt, "gen": {"all_ids": []}},
        {"name": "empty_both", "gt": {}, "gen": {}},
        {"name": "legacy_ground_truth_cache", "gt": {"citation_info": [
            {"fetched_paper_id": "A", "priority": "P1"},
            {"fetched_paper_id": "A", "priority": "P0"},
            {"fetched_paper_id": "B", "priority": "P1"},
            {"fetched_paper_id": "gt_NA", "priority": "P0"}]}, "gen": {"all_ids": ["A"]}},
        {"name": "inconsistent_priority_membership", "gt": {"all_ids": ["A"],
            "p0_ids": ["A", "X"], "p1_ids": []}, "gen": {"all_ids": ["X"]}},
        {"name": "malformed_noniterable_ids", "gt": gt, "gen": {"all_ids": None}},
    ]
    expected = {
        "exact_match": oracle(gt["all_ids"], gt["all_ids"], gt["p0_ids"], gt["p1_ids"]),
        "only_priority_zero": oracle(gt["all_ids"], ["A", "B"], gt["p0_ids"], gt["p1_ids"]),
        "partial_with_extra": oracle(gt["all_ids"], ["A", "C", "X"], gt["p0_ids"], gt["p1_ids"]),
        "duplicate_generated_ids": oracle(gt["all_ids"], ["A", "B"], gt["p0_ids"], gt["p1_ids"]),
        "unresolved_generated_ids": oracle(gt["all_ids"], ["A", "B"], gt["p0_ids"], gt["p1_ids"]),
        "empty_generated": oracle(gt["all_ids"], [], gt["p0_ids"], gt["p1_ids"]),
        "empty_both": oracle([], [], [], []),
        "legacy_ground_truth_cache": oracle(["A", "B"], ["A"], ["A"], ["B"]),
    }
    outputs, logs, exhaustive = [], [], []
    with tempfile.TemporaryDirectory(prefix="citation-", dir=ROOT / ".local/repro-sources") as tmp:
        def run(gt_data, gen_data):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = scorer(SimpleNamespace(log_folder=tmp), gt_data, gen_data)
            logs.append(output.getvalue().replace(tmp, "<scratch>"))
            return result
        for fixture in fixtures:
            try:
                result = run(fixture["gt"], fixture["gen"])
                outcome = {"name": fixture["name"], "outcome": "returned_metrics", "metrics": result}
                if fixture["name"] in expected:
                    wanted = expected[fixture["name"]]
                    assert all(math.isclose(result[k], v, rel_tol=0, abs_tol=1e-12) for k, v in wanted.items())
                    outcome.update({"independent_expected": wanted, "independent_formula_agrees": True})
            except TypeError as error:
                if fixture["name"] != "malformed_noniterable_ids":
                    raise
                outcome = {"name": fixture["name"], "outcome": "raised_TypeError", "message": str(error)}
            outputs.append(outcome)
        universe = ["A", "B", "C", "D", "X"]
        for size in range(len(universe)+1):
            for subset in itertools.combinations(universe, size):
                observed = run(gt, {"all_ids": list(subset)})
                wanted = oracle(gt["all_ids"], subset, gt["p0_ids"], gt["p1_ids"])
                assert all(math.isclose(observed[k], v, rel_tol=0, abs_tol=1e-12) for k, v in wanted.items())
                exhaustive.append({"generated_ids": list(subset), "metrics": observed,
                                   "independent_formula_agrees": True})
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / "fixtures.json", fixtures)
    write_json(args.output / "exhaustive-valid-id-cases.json", exhaustive)
    (args.output / "stdout.log").write_text("\n".join(logs))
    results = {"schema_version": 1, "project": "PaperOrchestra", "executed_at": execution_time(),
               "scope": "isolated unchanged citation-scoring method on synthetic cached-reference inputs",
               "source": SOURCES["citation_f1"], "extraction": extraction,
               "environment": environment(), "configuration": {"synthetic_ids": True,
                   "third_party_dependencies": [], "stochastic_operations": False,
                   "executed_methods": ["ReferenceF1V1Evaluator.evaluate_from_data"]},
               "cases": outputs, "exhaustive_valid_id_case_count": len(exhaustive),
               "exhaustive_valid_id_formula_agreement_count": len(exhaustive),
               "wall_seconds_excluding_download": time.perf_counter()-started,
               "cost": {"model_api_calls": 0, "model_api_cost_usd": 0,
                        "semantic_scholar_calls": 0, "cloud_gpu_hours": 0,
                        "local_energy_and_hardware_cost": "not measured"},
               "not_tested": ["full module import or pipeline installation", "PDF reference extraction",
                   "title or identifier resolution", "LLM citation prioritization", "paper generation",
                   "citation correctness in context", "published benchmark results"]}
    write_json(args.output / "results.json", results)
    print(json.dumps({"fixture_cases": len(outputs), "valid_id_cases": len(exhaustive),
                      "valid_id_formula_agreement": len(exhaustive),
                      "malformed_cache_outcome": outputs[-1]["outcome"],
                      "whole_pipeline_executed": False}, indent=2))


if __name__ == "__main__":
    main()
