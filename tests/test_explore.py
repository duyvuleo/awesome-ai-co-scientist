"""Behavioral tests for the offline discovery and comparison CLI."""
from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
import csv
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import explore
from catalog import load
from comparison import DIMENSIONS, load_comparisons


def entry(ident, date, *, kind="system", tags=None, evidence="preprint", **extra):
    return {
        "id": ident, "name": ident.title(), "kind": kind, "category": "end-to-end",
        "year": int(date[:4]), "date": date, "url": "https://example.org/" + ident,
        "summary": "Retains evidence for hypothesis verification.", "evidence": evidence,
        "tags": tags or ["verification", "memory"], "sources": ["https://example.org/" + ident],
        "checked": "2026-10-22", **extra,
    }


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.entries = [
            entry("year-only", "2026"),
            entry("newer", "2026-10-13", code_url="https://example.org/code"),
            entry("older", "2025-12-31", kind="paper", evidence="peer-reviewed"),
            entry("dated", "2026-01-01", tags=["memory"], evidence="project"),
        ]

    def ids(self, **filters):
        return [e["id"] for e in explore.search_entries(self.entries, **filters)]

    def test_newest_first_and_year_only_last_within_year(self):
        self.assertEqual(self.ids(), ["newer", "dated", "year-only", "older"])

    def test_query_matches_all_terms_across_fields_case_insensitively(self):
        self.assertEqual(self.ids(query="NEWER hypothesis"), ["newer"])
        self.assertEqual(self.ids(query="hypothesis nonexistent"), [])

    def test_repeated_tags_are_exact_and_intersection(self):
        self.assertEqual(self.ids(tags=["MEMORY", "verification"]), ["newer", "year-only", "older"])
        self.assertEqual(self.ids(tags=["mem"]), [])

    def test_filters_combine_and_since_year_is_inclusive(self):
        self.assertEqual(self.ids(kind="system", year=2026, evidence="preprint", has_code_link=True), ["newer"])
        self.assertEqual(self.ids(since_year=2026), ["newer", "dated", "year-only"])
        self.assertEqual(self.ids(since_year=2025), self.ids())
        self.assertEqual(self.ids(kind="paper", evidence="project"), [])

    def test_code_link_presence_is_not_a_tag_or_product_availability_claim(self):
        items = [
            entry("tag-only", "2026", tags=["code-available"]),
            entry("artifacts", "2026", sources=["https://github.com/example/generated-artifacts"]),
            entry("github-pages", "2026", url="https://example.github.io/project"),
            entry("repository", "2026", url="https://github.com/example/project"),
            entry("code-field", "2026", code_url="https://example.org/source.zip"),
            entry("api-only", "2026", sources=["https://api.github.com/repos/example/project"]),
        ]
        self.assertEqual({e["id"] for e in explore.search_entries(items, has_code_link=True)},
                         {"artifacts", "repository", "code-field"})

    def test_results_do_not_mutate_or_share_nested_catalog_data(self):
        original = deepcopy(self.entries)
        matches = explore.search_entries(self.entries)
        matches[0]["tags"].append("changed")
        found = explore.show_entry(self.entries, "newer")
        found["sources"].clear()
        self.assertEqual(self.entries, original)


class OutputAndCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = load()
        cls.comparisons = load_comparisons()

    def invoke(self, argv):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            try:
                result = explore.main(argv)
            except SystemExit as exc:
                result = exc.code
        return result, stdout.getvalue(), stderr.getvalue()

    def test_json_search_is_parseable_and_preserves_full_records(self):
        code, output, error = self.invoke(["search", "--kind", "system", "--limit", "2", "--format", "json"])
        self.assertEqual((code, error), (0, ""))
        payload = json.loads(output)
        self.assertEqual(payload["metadata"]["total_matches"], len([e for e in self.entries if e["kind"] == "system"]))
        self.assertEqual(payload["metadata"]["returned"], 2)
        self.assertIn("not an execution", payload["metadata"]["source_check_note"])
        by_id = {e["id"]: e for e in self.entries}
        for found in payload["entries"]:
            self.assertEqual(found, by_id[found["id"]])

    def test_show_preserves_sources_related_and_dates_in_every_format(self):
        original = explore.show_entry(self.entries, "agentic-scientist-system")
        for output_format in explore.FORMATS:
            with self.subTest(output_format=output_format):
                code, output, error = self.invoke(["show", original["id"], "--format", output_format])
                self.assertEqual((code, error), (0, ""))
                for source in original["sources"]:
                    self.assertIn(source, output)
                for related in original["related"]:
                    self.assertIn(related, output)
                self.assertIn(original["checked"], output)
                self.assertIn(original["date"], output)

    def test_csv_catalog_lists_round_trip_without_losing_commas_or_unicode(self):
        special = entry("special", "2026", summary='A "quoted", multi-line\nclaim: α | β', related=["related"])
        with patch.object(explore, "load", return_value=[special]):
            code, output, error = self.invoke(["search", "--format", "csv"])
        self.assertEqual((code, error), (0, ""))
        row = list(csv.DictReader(io.StringIO(output)))[0]
        self.assertEqual(row["summary"], special["summary"])
        self.assertEqual(row["date_precision"], "year only")
        for field in ("tags", "sources", "related"):
            self.assertEqual(json.loads(row[field]), special[field])

    def test_empty_search_has_successful_machine_readable_output(self):
        for output_format in ("json", "csv"):
            code, output, error = self.invoke(["search", "never-matching-query-12345", "--format", output_format])
            self.assertEqual((code, error), (0, ""))
            if output_format == "json":
                self.assertEqual(json.loads(output)["entries"], [])
            else:
                self.assertEqual(list(csv.DictReader(io.StringIO(output))), [])
                self.assertTrue(output.startswith("id,name,"))

    def test_errors_are_nonzero_on_stderr_without_stdout(self):
        for argv in (
            ["show", "missing-id"], ["search", "--unknown"], ["search", "--ki", "paper"],
            ["search", "--tag", "missing-tag"], ["search", "--kind", "wrong"],
            ["search", "--evidence", "wrong"], ["search", "--limit", "0"],
            ["search", "--limit", "-1"], ["search", "--year", "26"],
            ["search", "--year", "2026", "--since-year", "2025"],
            ["compare", "agentic-scientist-system"],
            ["compare", "agentic-scientist-system", "missing-id"],
            ["compare", "agentic-scientist-system", "agentic-scientist"],
            ["compare", "agentic-scientist-system", "agentic-scientist-system"],
        ):
            with self.subTest(argv=argv):
                code, output, error = self.invoke(argv)
                self.assertEqual(code, 2)
                self.assertEqual(output, "")
                self.assertIn("error:", error)

    def test_markdown_escapes_table_breaking_content(self):
        special = entry("special", "2026", summary="a | b\n<script>[x]*y*")
        with patch.object(explore, "load", return_value=[special]):
            code, output, error = self.invoke(["show", "special", "--format", "markdown"])
        self.assertEqual((code, error), (0, ""))
        self.assertIn(r"a \| b<br>&lt;script&gt;\[x\]\*y\*", output)

    def test_script_works_from_a_different_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts/explore.py"), "show", "agentic-scientist", "--format", "json"],
                cwd=directory, text=True, capture_output=True, check=False,
            )
        self.assertEqual((completed.returncode, completed.stderr), (0, ""))
        self.assertEqual(json.loads(completed.stdout)["entries"][0]["id"], "agentic-scientist")

    def test_comparison_json_preserves_all_seven_cells_and_source_locators(self):
        code, output, error = self.invoke(["compare", "openresearch-system", "agentic-scientist-system", "--format", "json"])
        self.assertEqual((code, error), (0, ""))
        payload = json.loads(output)
        self.assertEqual(payload["metadata"]["comparison_scope"], self.comparisons["scope"])
        original = {r["system_id"]: r for r in self.comparisons["systems"]}
        self.assertEqual(payload["systems"][0]["catalog"]["id"], "agentic-scientist-system")
        for pair in payload["systems"]:
            record = pair["comparison"]
            self.assertEqual(record, original[record["system_id"]])
            self.assertEqual(set(record["dimensions"]), set(DIMENSIONS))

    def test_comparison_csv_has_cell_basis_statement_and_resolved_sources(self):
        code, output, error = self.invoke(["compare", "agentic-scientist-system", "openresearch-system", "--format", "csv"])
        self.assertEqual((code, error), (0, ""))
        rows = list(csv.DictReader(io.StringIO(output)))
        self.assertEqual(len(rows), 2 * len(DIMENSIONS))
        originals = {r["system_id"]: r for r in self.comparisons["systems"]}
        for row in rows:
            original = originals[row["system_id"]]
            cell = original["dimensions"][row["dimension"]]
            self.assertEqual(row["statement"], cell["text"])
            self.assertEqual(row["evidence_basis"], cell["basis"])
            sources = json.loads(row["sources"])
            self.assertEqual([s["url"] for s in sources], cell["sources"])
            self.assertTrue(all(s["locator"] and s["label"] for s in sources))
            self.assertEqual(row["comparison_checked"], original["checked"])

    def test_comparison_readable_formats_retain_citations_and_basis(self):
        original = self.comparisons["systems"][0]
        for output_format in ("text", "markdown"):
            code, output, error = self.invoke(["compare", original["system_id"], "openresearch-system", "--format", output_format])
            self.assertEqual((code, error), (0, ""))
            for source in original["sources"]:
                self.assertIn(source["url"], output)
                self.assertIn(source["locator"], output)
            for cell in original["dimensions"].values():
                self.assertIn(explore.BASES[cell["basis"]], output)

    def test_comparison_does_not_mutate_inputs_or_share_nested_data(self):
        entries, comparisons = deepcopy(self.entries), deepcopy(self.comparisons)
        before_entries, before_comparisons = deepcopy(entries), deepcopy(comparisons)
        pairs = explore.compare_entries(entries, comparisons, ["agentic-scientist-system", "openresearch-system"])
        pairs[0]["comparison"]["dimensions"]["memory"]["sources"].clear()
        pairs[0]["catalog"]["tags"].clear()
        self.assertEqual(entries, before_entries)
        self.assertEqual(comparisons, before_comparisons)

    def test_missing_comparison_record_is_explicit(self):
        with self.assertRaisesRegex(ValueError, "No source-backed comparison record"):
            explore.compare_entries(self.entries, {"systems": []}, ["agentic-scientist-system", "openresearch-system"])


if __name__ == "__main__":
    unittest.main()
