"""Recent additions follow collection history, not source freshness."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import recent


class RecentAdditionsTests(unittest.TestCase):
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
