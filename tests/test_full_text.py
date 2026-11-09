"""Guard the reading coverage and paper/resource distinction."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from full_text import validate_reviews, review_index, render_reviews
from validate import public_url


class ReadingCoverageTests(unittest.TestCase):
    def setUp(self):
        self.entries = [dict(id="sample", name="Sample paper", kind="paper", date="2025-01-01"),
                        dict(id="sample-code", name="Sample system", kind="system", date="2025-01-01")]
        self.entries[0]["url"] = "https://arxiv.org/abs/2501.01234"
        self.review = dict(id="sample", title="Sample paper", record_ids=["sample", "sample-code"],
                           primary_source="https://arxiv.org/abs/2501.01234",
                           reading_status="partial", version="arXiv:2501.01234v2",
                           coverage="Main text read; scientific supplement unavailable.",
                           reviewed="2026-11-09", methods="Method description.",
                           evaluation="Reported evaluation.", limitations="Supplement access gap.",
                           sources=[dict(url="https://arxiv.org/html/2501.01234v2",
                                         label="Author version", locator="Sections 2–4")])
        self.data = dict(schema_version=1, scope="Two records, one paper.",
                         boundary="Reading is not reproduction.", reviews=[self.review],
                         coverage_targets=[self.target(self.review)])

    @staticmethod
    def target(review):
        return {key: copy.deepcopy(review[key]) for key in ("id", "record_ids", "primary_source")}

    def test_one_paper_can_support_multiple_catalog_records(self):
        self.assertEqual(validate_reviews(self.data, self.entries, public_url), [])
        self.assertEqual(set(review_index(self.data)), {"sample", "sample-code"})
        rendered = render_reviews(self.data, self.entries)
        self.assertIn("Partial appraisal; access gaps | 1", rendered)
        self.assertIn("scientific supplement unavailable", rendered)
        self.assertIn("systems.md#sample-code", rendered)

    def test_version_alias_is_not_a_second_paper(self):
        other = copy.deepcopy(self.review)
        other.update(id="duplicate", primary_source="https://arxiv.org/pdf/2501.01234v3")
        self.data["reviews"].append(other)
        self.data["coverage_targets"].append(self.target(other))
        self.assertTrue(any("duplicate paper identity" in error
                            for error in validate_reviews(self.data, self.entries, public_url)))

    def test_distinct_companion_can_share_a_resource(self):
        other = copy.deepcopy(self.review)
        other.update(id="companion", primary_source="https://arxiv.org/abs/2502.01234",
                     record_ids=["sample-code"])
        self.data["reviews"].append(other)
        self.data["coverage_targets"].append(self.target(other))
        self.assertEqual(validate_reviews(self.data, self.entries, public_url), [])
        self.assertEqual(len(review_index(self.data)["sample-code"]), 2)

    def test_missing_core_paper_cannot_disappear_from_coverage(self):
        self.entries.append(dict(id="unread", kind="paper"))
        self.assertIn("full-text reviews: unaccounted paper unread",
                      validate_reviews(self.data, self.entries, public_url))

    def test_missing_source_locator_and_unknown_association_fail(self):
        self.review["record_ids"].append("missing")
        del self.review["sources"][0]["locator"]
        errors = validate_reviews(self.data, self.entries, public_url)
        self.assertTrue(any("invalid catalog associations" in error for error in errors))
        self.assertTrue(any("locator" in error for error in errors))

    def test_companion_cannot_stand_in_for_the_core_paper(self):
        self.review["primary_source"] = "https://arxiv.org/abs/2502.09999"
        self.data["coverage_targets"] = [self.target(self.review)]
        self.assertIn("full-text reviews: missing primary appraisal for sample",
                      validate_reviews(self.data, self.entries, public_url))

    def test_verified_publication_alias_preserves_primary_coverage(self):
        self.entries[0]["url"] = "https://doi.org/10.1234/example"
        self.review["identity_aliases"] = [self.entries[0]["url"]]
        self.assertEqual(validate_reviews(self.data, self.entries, public_url), [])

    def test_linked_only_primary_cannot_disappear_from_the_inventory(self):
        self.entries[0]["kind"] = "tool"
        self.data["reviews"] = []
        self.assertIn("full-text reviews: unaccounted target sample",
                      validate_reviews(self.data, self.entries, public_url))

    def test_malformed_reviewer_check_is_rejected_before_rendering(self):
        self.review["reviewer_check"] = ["not a string"]
        self.assertTrue(any("reviewer_check" in error for error in
                            validate_reviews(self.data, self.entries, public_url)))

    def test_index_title_cannot_add_a_table_column_or_row(self):
        self.review["title"] = "Sample | second column\nsecond row"
        rendered = render_reviews(self.data, self.entries)
        rows = [line for line in rendered.splitlines() if line.startswith("| 2025-01-01")]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].count("|"), 4)
        self.assertIn("&#124;", rows[0])
        self.assertIn("<br>", rows[0])


if __name__ == "__main__":
    unittest.main()
