"""Recent additions follow collection history, not source freshness."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import load, recent, recent_groups
from render import reading_table


class RecentAdditionsTests(unittest.TestCase):
    def test_paper_and_newer_system_share_one_group_without_mutating_dates(self):
        entries = [
            {"id": "paper", "name": "Paper", "kind": "paper", "date": "2025-01-01",
             "added_on": "2026-10-22", "url": "https://arxiv.org/abs/2501.00001"},
            {"id": "system", "name": "System", "kind": "system", "date": "2025-02-01",
             "added_on": "2026-10-24", "url": "https://github.com/example/system",
             "paper_url": "https://arxiv.org/html/2501.00001v2"},
            {"id": "other", "name": "Other", "kind": "paper", "date": "2026-10-20",
             "added_on": "2026-10-23", "url": "https://arxiv.org/abs/2610.00001"},
        ]
        original = deepcopy(entries)
        self.assertEqual([[e["id"] for e in group] for group in recent_groups(entries)],
                         [["paper", "system"], ["other"]])
        self.assertEqual(entries, original)

    def test_related_projects_and_distinct_papers_remain_separate(self):
        entries = [
            {"id": "first", "name": "Project", "kind": "system", "date": "2026-10-20",
             "added_on": "2026-10-23", "url": "https://example.org/first",
             "related": ["second"]},
            {"id": "second", "name": "Project", "kind": "tool", "date": "2026-10-20",
             "added_on": "2026-10-23", "url": "https://example.org/second",
             "related": ["first"]},
        ]
        self.assertEqual(len(recent_groups(entries)), 2)

    def test_recent_table_has_one_row_per_work_and_keeps_both_detail_links(self):
        ids = {"agentic-scientist", "agentic-scientist-system",
               "seer-analytical-robustness", "seer-repro"}
        groups = recent_groups([e for e in load() if e["id"] in ids])
        section = reading_table([g[0] for g in groups], show_added=True,
                                groups={g[0]["id"]: g for g in groups})
        rows = [line for line in section.splitlines() if line.startswith("| <code>")]
        self.assertEqual(len(rows), 2)
        for paper, companion in [
            ("papers.md#agentic-scientist", "systems.md#agentic-scientist-system"),
            ("papers.md#seer-analytical-robustness", "benchmarks.md#seer-repro"),
        ]:
            matched = [row for row in rows if paper in row or companion in row]
            self.assertEqual(len(matched), 1)
            self.assertIn(paper, matched[0])
            self.assertIn(companion, matched[0])

    def test_old_paper_added_today_precedes_new_paper_added_yesterday(self):
        entries = [
            {"id": "new-paper", "name": "New paper", "date": "2026-10-20",
             "added_on": "2026-10-22", "checked": "2026-10-23"},
            {"id": "old-paper", "name": "Old paper", "date": "2025-12-24",
             "added_on": "2026-10-23", "checked": "2026-10-23"},
        ]
        original = deepcopy(entries)
        self.assertEqual([e["id"] for e in recent(entries)], ["old-paper", "new-paper"])
        entries[0]["checked"] = "2026-10-24"
        self.assertEqual([e["id"] for e in recent(entries)], ["old-paper", "new-paper"])
        self.assertEqual([e["id"] for e in entries], [e["id"] for e in original])

    def test_same_day_additions_keep_source_date_precision_and_tie_order(self):
        entries = [
            {"id": "year-only", "name": "A year-only entry", "date": "2026"},
            {"id": "beta", "name": "Beta", "date": "2026-10-15"},
            {"id": "alpha", "name": "Alpha", "date": "2026-10-15"},
            {"id": "latest", "name": "Latest", "date": "2026-10-16"},
        ]
        for entry in entries:
            entry["added_on"] = "2026-10-23"
        original = deepcopy(entries)
        self.assertEqual([e["id"] for e in recent(entries)],
                         ["latest", "alpha", "beta", "year-only"])
        self.assertEqual(entries, original)


if __name__ == "__main__":
    unittest.main()
