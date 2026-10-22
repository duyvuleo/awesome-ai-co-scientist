"""Conservative identity matching and negative cases for recent-addition grouping."""
from contextlib import redirect_stdout
from copy import deepcopy
import io
from itertools import permutations
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import canonical_identity, load, recent_groups
from render import reading_table
import validate


def record(ident, url, kind="paper", **extra):
    return {"id": ident, "name": ident, "kind": kind, "url": url,
            "date": "2026-10-01", "added_on": "2026-10-22",
            "checked": "2026-10-23", "evidence": "preprint",
            "summary": "An evidence-scoped test record.", **extra}


def membership(entries):
    return [[entry["id"] for entry in group] for group in recent_groups(entries)]


class IdentityTests(unittest.TestCase):
    def test_arxiv_routes_versions_hosts_and_doi_alias(self):
        urls = [
            "https://arxiv.org/abs/2610.18933",
            "https://arxiv.org/html/2610.18933v12#S3",
            "https://arxiv.org/pdf/2610.18933v2.pdf",
            "https://arxiv.org/abs/2610.18933v1/",
            "https://export.arxiv.org/pdf/2610.18933?download=1",
            "http://www.arxiv.org/abs/2610.18933v3?utm_source=feed",
            "https://ARXIV.ORG:443/abs/2610.18933",
            "https://doi.org/10.48550/arXiv.2610.18933",
            "https://dx.doi.org/10.48550%2FarXiv.2610.18933v2",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(canonical_identity(url), "arxiv:2610.18933")

    def test_legacy_arxiv_identifiers(self):
        for url in ["https://arxiv.org/abs/hep-th/9901001v2",
                    "https://export.arxiv.org/pdf/hep-th/9901001.pdf",
                    "https://doi.org/10.48550/arXiv.hep-th/9901001"]:
            self.assertEqual(canonical_identity(url), "arxiv:hep-th/9901001")
        self.assertEqual(canonical_identity("https://arxiv.org/abs/math.GT/0301001v2"),
                         "arxiv:math.gt/0301001")

    def test_doi_case_resolver_and_encoding(self):
        for url in ["https://doi.org/10.1000/ABC.DEF", "http://dx.doi.org/10.1000/abc.def",
                    "https://www.doi.org/10.1000%2Fabc.def?utm_source=feed#abstract"]:
            self.assertEqual(canonical_identity(url), "doi:10.1000/abc.def")
        # A DOI suffix can itself contain slashes, punctuation, or non-ASCII text.
        self.assertNotEqual(canonical_identity("https://doi.org/10.1000/a/"),
                            canonical_identity("https://doi.org/10.1000/a"))
        self.assertNotEqual(canonical_identity("https://doi.org/10.1000/Ä"),
                            canonical_identity("https://doi.org/10.1000/ä"))

    def test_github_root_case_git_suffix_and_tracking(self):
        for url in ["https://github.com/Owner/Repo", "https://www.github.com/owner/repo.git/",
                    "http://github.com/OWNER/REPO#readme",
                    "https://github.com/owner/repo?utm_source=x&fbclid=y"]:
            self.assertEqual(canonical_identity(url), "github:owner/repo")

    def test_branches_forks_releases_and_files_stay_distinct(self):
        urls = ["https://github.com/owner/repo", "https://github.com/fork/repo",
                "https://github.com/owner/repo/tree/v1", "https://github.com/owner/repo/tree/v2",
                "https://github.com/owner/repo/releases/tag/v1",
                "https://github.com/owner/repo/releases/tag/v2",
                "https://github.com/owner/repo/blob/main/A.md",
                "https://github.com/owner/repo/blob/main/a.md",
                "https://github.com/owner/repo?ref=v1", "https://github.com/owner/repo?ref=v2"]
        self.assertEqual(len({canonical_identity(url) for url in urls}), len(urls))

    def test_unrecognized_urls_preserve_semantic_differences(self):
        urls = ["https://example.org/Paper", "https://example.org/paper",
                "https://example.org/paper/", "https://example.org/paper?id=1",
                "https://example.org/paper?id=2", "https://example.org/#/work-a",
                "https://example.org/#/work-b", "https://example.org:444/paper"]
        self.assertEqual(len({canonical_identity(url) for url in urls}), len(urls))
        self.assertEqual(canonical_identity("https://EXAMPLE.org:443/paper?id=1&utm_source=x"),
                         canonical_identity("https://example.org/paper?id=1"))

    def test_unrelated_arxiv_paths_and_lookalike_hosts_do_not_alias(self):
        urls = ["https://arxiv.org/abs/2610.18933", "https://arxiv.org/abs/2610.18934",
                "https://arxiv.org/abs/2610.18933v0", "https://arxiv.org/abs/not-an-idv2",
                "https://arxiv.org/list/2610.18933", "https://arxiv.org.evil.example/abs/2610.18933",
                "https://arxiv.org:444/abs/2610.18933", "https://arxiv.org/abs/2610.18933/supplement"]
        self.assertEqual(len({canonical_identity(url) for url in urls}), len(urls))

    def test_validator_rejects_same_kind_url_alias(self):
        entries = deepcopy(load())
        duplicate = deepcopy(next(e for e in entries if e["id"] == "agentic-scientist"))
        duplicate.update(id="duplicate-paper", url="https://arxiv.org/pdf/2610.18933v2.pdf")
        duplicate["sources"].append(duplicate["url"])
        entries.append(duplicate)
        with patch.object(validate, "load", return_value=entries), self.assertRaisesRegex(
                SystemExit, "duplicate canonical URL within kind"):
            validate.main()

    def test_validator_preserves_case_sensitive_paths(self):
        entries = deepcopy(load())
        base = deepcopy(next(e for e in entries if e["kind"] == "paper"))
        for ident in ["A", "a"]:
            copy = deepcopy(base)
            copy.update(id="case-" + ("upper" if ident == "A" else "lower"),
                        url="https://example.org/" + ident, related=[],
                        sources=["https://example.org/" + ident])
            entries.append(copy)
        with patch.object(validate, "load", return_value=entries), redirect_stdout(io.StringIO()):
            validate.main()


class GroupingTests(unittest.TestCase):
    def test_shared_citations_names_and_related_links_are_not_identity(self):
        shared = "https://arxiv.org/abs/2610.18933"
        entries = [record("a", "https://example.org/a", name="Same", sources=[shared], related=["b"]),
                   record("b", "https://example.org/b", name="Same", sources=[shared], related=["a"])]
        self.assertEqual(len(recent_groups(entries)), 2)

    def test_distinct_systems_citing_one_paper_are_not_collapsed(self):
        url = "https://arxiv.org/abs/2610.18933"
        entries = [record("paper", url),
                   record("system-v1", "https://github.com/lab/system-v1", "system", paper_url=url),
                   record("system-v2", "https://github.com/lab/system-v2", "system", paper_url=url)]
        self.assertEqual({tuple(group) for group in membership(entries)},
                         {("paper",), ("system-v1",), ("system-v2",)})

    def test_order_and_representative_are_input_order_independent(self):
        url = "https://arxiv.org/abs/2610.18933"
        entries = [record("paper", url),
                   record("system", "https://github.com/lab/system", "system", paper_url=url,
                          added_on="2026-10-24"),
                   record("other", "https://example.org/other", added_on="2026-10-23")]
        for permutation in permutations(entries):
            self.assertEqual(membership(permutation), [["paper", "system"], ["other"]])

    def test_ambiguous_buckets_do_not_promote_old_records(self):
        url = "https://arxiv.org/abs/2610.18933"
        entries = [record("old", "https://example.org/v1", "system", paper_url=url),
                   record("new", "https://example.org/v2", "system", paper_url=url,
                          added_on="2026-10-24"),
                   record("middle", "https://example.org/middle", added_on="2026-10-23")]
        self.assertEqual(membership(entries), [["new"], ["middle"], ["old"]])

    def test_grouping_precedes_limit_and_rendering_retains_all_details(self):
        entries = []
        for i in range(10):
            url = f"https://arxiv.org/abs/2610.{10000+i}"
            entries.extend([record(f"paper-{i}", url),
                            record(f"system-{i}", f"https://github.com/lab/system-{i}", "system", paper_url=url)])
        original = deepcopy(entries)
        groups = recent_groups(entries)[:8]
        self.assertEqual(len(groups), 8)
        self.assertTrue(all(len(group) == 2 for group in groups))
        text = reading_table([g[0] for g in groups], show_added=True,
                             groups={g[0]["id"]: g for g in groups})
        for group in groups:
            for e in group:
                self.assertEqual(text.count("#"+e["id"]+")"), 1)
        self.assertEqual(entries, original)

    def test_real_catalog_partitions_without_record_loss(self):
        entries = load()
        flattened = [entry["id"] for group in recent_groups(entries) for entry in group]
        self.assertEqual(sorted(flattened), sorted(e["id"] for e in entries))
        self.assertEqual(len(flattened), len(set(flattened)))
        groups = membership(entries)
        for distinct in ["recursive-flint-tool", "recursive-eureka-machine-system",
                         "ai-scientist-system", "ai-scientist-v2-system"]:
            self.assertEqual(sum(distinct in group for group in groups), 1)
        self.assertFalse(any("ai-scientist-system" in g and "ai-scientist-v2-system" in g for g in groups))
        self.assertFalse(any("recursive-flint-tool" in g and "recursive-eureka-machine-system" in g for g in groups))


if __name__ == "__main__":
    unittest.main()
