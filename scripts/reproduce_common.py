"""Shared provenance and output helpers for explicitly invoked local reproductions.

No third-party source is redistributed. Fetches are restricted to pinned public
GitHub archives; every executed source file is checked against an inspected hash.
"""

from __future__ import annotations

import hashlib
from datetime import datetime
import io
import json
import os
from pathlib import Path
import platform
import urllib.request
import zipfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / ".local/repro-sources"
SOURCES = {
    "circle_packing": {
        "repository": "https://github.com/SakanaAI/AI-Scientist-v3",
        "commit": "df8313889a004f8a44a472e19a833cd547bb828a",
        "archive_sha256": "3eb52673b48e6fafab8eafef33d5f1867655238d1b472ef498a68f3395560eea",
        "files": {
            "examples/circpack/evaluate.py": "11187fcb39331efccc1c23aa2761d6eaefce200d2d81df660f32e5595d18a4fa",
            "examples/circpack/capture.py": "cc7a660d33180d61479bbf0df59fae815d0119dd19d9e5290e0d2126096804d5",
            "examples/circpack/program_0/src/program.py": "72aaca25037f1cdc9f71257eb325ec456b888de55d9328f62eea488335d5101a",
            "examples/circpack/task.md": "226af1f6d9d74f0dd3373abc03af9bdeab86dbd1578ee6f5d6909f575d93df80",
            "examples/circpack/requirements.txt": "8a1ff7c87e0b624415213e3652b974cfe92ac989b17c6cbec17a08d62afe5f72",
        },
    },
    "citation_f1": {
        "repository": "https://github.com/google-research/paper-orchestra",
        "commit": "ca1b3fa01c2970fc7cda32d16245db38d57b3f56",
        "archive_sha256": "693f59a764d0a7c0b5371f7655274e0cfc907de31baa11ff307e97986a70ffb8",
        "files": {
            "autoraters/citation_f1.py": "099af7c3ade2c7488e2794e193390df2115b411cfc2e6868341e91e1c070f766",
        },
    },
}


def source_tree(key: str, fetch: bool = False) -> Path:
    source = SOURCES[key]
    repo = source["repository"].removeprefix("https://github.com/")
    directory = SOURCE_ROOT / f"{repo.split('/')[-1]}-{source['commit']}"
    if fetch:
        SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
        archive = SOURCE_ROOT / f"{directory.name}.zip"
        if not archive.exists():
            url = f"https://codeload.github.com/{repo}/zip/{source['commit']}"
            payload = urllib.request.urlopen(url, timeout=60).read()
            if hashlib.sha256(payload).hexdigest() != source["archive_sha256"]:
                raise ValueError("Pinned archive hash mismatch; inspect before updating pins")
            archive.write_bytes(payload)
        payload = archive.read_bytes()
        if hashlib.sha256(payload).hexdigest() != source["archive_sha256"]:
            raise ValueError("Pinned archive hash mismatch")
        with zipfile.ZipFile(io.BytesIO(payload)) as zipped:
            # Extract only the reviewed files; never unpack executables or links.
            for relative in source["files"]:
                target = directory / relative
                content = zipped.read(f"{directory.name}/{relative}")
                if hashlib.sha256(content).hexdigest() != source["files"][relative]:
                    raise ValueError(f"Source hash mismatch: {relative}")
                if target.exists() and target.read_bytes() != content:
                    raise ValueError(f"Refusing to overwrite locally modified source: {relative}")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    for relative, expected in source["files"].items():
        target = directory / relative
        if not target.is_file():
            raise SystemExit("Pinned source missing; first run this script with --fetch-only")
        if hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Inspected source hash mismatch: {relative}")
    return directory


def environment() -> dict:
    return {
        "python": platform.python_version(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "machine_architecture": platform.machine(),
        "logical_cpu_count": os.cpu_count(),
    }


def execution_time() -> str:
    return datetime.now(ZoneInfo("Australia/Sydney")).isoformat(timespec="seconds")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def sanitize(text: str) -> str:
    return text.replace(str(ROOT), "<checkout>")
