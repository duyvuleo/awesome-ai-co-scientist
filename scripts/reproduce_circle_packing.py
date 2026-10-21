"""Run the pinned Agentic Scientist example and inspect its evaluation boundary.

This is a baseline/evaluator reproduction, not an autonomous-science run.
Source download is separate from execution. Requires NumPy 2.4.2 only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import time

from reproduce_common import ROOT, SOURCES, environment, execution_time, sanitize, source_tree, write_json


def load_file(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def independent_geometry(centers, radii, reported_sum) -> dict:
    """Independent scalar arithmetic, separate from upstream NumPy validation."""
    if len(centers) != 26 or len(radii) != 26:
        return {"valid": False, "reason": "wrong circle count"}
    values = [float(v) for row in centers for v in row] + [float(v) for v in radii]
    if not all(math.isfinite(v) for v in values + [float(reported_sum)]):
        return {"valid": False, "reason": "nonfinite coordinates, radii, or score"}
    boundary = min(min(float(x)-float(r), 1-float(x)-float(r),
                       float(y)-float(r), 1-float(y)-float(r))
                   for (x, y), r in zip(centers, radii))
    clearance = min(math.hypot(float(centers[i][0])-float(centers[j][0]),
                               float(centers[i][1])-float(centers[j][1]))
                    -float(radii[i])-float(radii[j])
                    for i in range(26) for j in range(i+1, 26))
    recomputed = math.fsum(float(r) for r in radii)
    valid = (min(radii) >= 0 and boundary >= -1e-6 and clearance >= -1e-6
             and math.isclose(recomputed, float(reported_sum), rel_tol=0, abs_tol=1e-6))
    return {"valid": bool(valid), "recomputed_sum_of_radii": recomputed,
            "minimum_boundary_clearance": boundary, "minimum_pair_clearance": clearance,
            "zero_radius_circle_count": sum(float(r) == 0 for r in radii),
            "tolerance": 1e-6}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch-only", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / ".local/repro-runs/circle-packing")
    args = parser.parse_args()
    source = source_tree("circle_packing", args.fetch_only)
    if args.fetch_only:
        print("Verified pinned public circle-packing source; no code executed.")
        return
    import numpy as np
    if np.__version__ != "2.4.2":
        raise SystemExit("Use the documented isolated environment with numpy==2.4.2")
    started = time.perf_counter()
    example = source / "examples/circpack"
    sys.path.insert(0, str(example))
    evaluator = load_file("pinned_circle_evaluator", example / "evaluate.py")
    baseline = load_file("pinned_circle_baseline", example / "program_0/src/program.py")
    returned = baseline.solution()
    centers, radii, score = returned
    independent = independent_geometry(*returned)
    assert independent["valid"]
    checks = []
    cases = {"baseline": (centers.copy(), radii.copy(), float(score))}
    c = centers.copy(); c[1] = c[0]
    cases["overlapping_centers"] = (c, radii.copy(), float(score))
    c = centers.copy(); c[0] = [2.0, 2.0]
    cases["outside_square"] = (c, radii.copy(), float(score))
    r = radii.copy(); r[0] = -0.1
    cases["negative_radius"] = (centers.copy(), r, float(r.sum()))
    cases["wrong_shape"] = (centers[:-1].copy(), radii[:-1].copy(), float(radii[:-1].sum()))
    cases["misreported_score"] = (centers.copy(), radii.copy(), float(score)+1)
    c = centers.copy(); c[0] = [float("nan"), float("nan")]
    cases["nan_center"] = (c, radii.copy(), float(score))
    for name, output in cases.items():
        accepted, message = evaluator.adapted_validate_packing(output)
        checks.append({"case": name, "upstream_accepted": bool(accepted),
                       "upstream_message": message,
                       "independent": independent_geometry(*output)})
    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="circle-", dir=ROOT / ".local/repro-sources") as tmp:
        scratch = Path(tmp)
        runs = []
        for name, candidate in [("baseline", example / "program_0/src/program.py"),
                                ("overlap", scratch / "overlap.py")]:
            if name == "overlap":
                candidate.write_text("import numpy as np\ndef solution():\n"
                                     "    return np.full((26, 2), 0.5), np.full(26, 0.1), 2.6\n")
            output = scratch / name
            command = [sys.executable, str((example / "evaluate.py").relative_to(ROOT)),
                       "--program_path", str(candidate.relative_to(ROOT)),
                       "--results_dir", str(output.relative_to(ROOT)), "--quiet"]
            before = time.perf_counter()
            process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                     timeout=30, env={"PATH": "/usr/bin:/bin", "OMP_NUM_THREADS": "1",
                                                      "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"})
            elapsed = time.perf_counter()-before
            if process.returncode:
                raise RuntimeError(sanitize(process.stderr))
            metrics = json.loads((output / "metrics.json").read_text())
            correct = json.loads((output / "correct.json").read_text())
            runs.append({"case": name, "wall_seconds": elapsed, "exit_code": process.returncode,
                         "correct": correct, "combined_score": metrics["combined_score"]})
            write_json(args.output / f"{name}-metrics.json", metrics)
            write_json(args.output / f"{name}-correct.json", correct)
            logs = (output / "stdout.log").read_text() + (output / "stderr.log").read_text()
            logs += process.stderr
            logs = sanitize(logs).replace(str(scratch.relative_to(ROOT)), "<scratch>")
            (args.output / f"{name}-stdout.log").write_text(logs)
    assert runs[0]["correct"]["correct"] is True
    assert runs[1]["correct"]["correct"] is False
    assert all(not check["upstream_accepted"] for check in checks[1:6])
    write_json(args.output / "packing.json", {"centers": centers.tolist(), "radii": radii.tolist(),
                                             "reported_sum": float(score)})
    result = {"schema_version": 1, "project": "Agentic Scientist", "executed_at": execution_time(),
              "scope": "public baseline and local circle-packing evaluator only",
              "source": SOURCES["circle_packing"], "environment": {**environment(), "numpy": np.__version__},
              "configuration": {"n_circles": 26, "random_seed": None, "stochastic_operations": False,
                                "baseline_evaluator_timeout_seconds": 300, "outer_timeout_seconds": 30,
                                "numpy_thread_limit_for_subprocesses": 1},
              "independent_baseline_check": independent, "control_cases": checks, "official_cli_runs": runs,
              "wall_seconds_excluding_download_and_install": time.perf_counter()-started,
              "cost": {"model_api_calls": 0, "model_api_cost_usd": 0, "cloud_gpu_hours": 0,
                       "local_energy_and_hardware_cost": "not measured"},
              "not_tested": ["agent orchestration", "hypothesis generation", "search or optimization gains",
                             "published paper results", "sealed evaluation isolation", "scientific novelty"]}
    write_json(args.output / "results.json", result)
    print(json.dumps({"score": float(score), "independent_feasible": independent["valid"],
                      "control_cases": len(checks), "nan_center_accepted": checks[-1]["upstream_accepted"],
                      "overlap_score": runs[1]["combined_score"], "overlap_correct": False}, indent=2))


if __name__ == "__main__":
    main()
