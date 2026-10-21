# Initial verification

Performed on **22 October 2026** for the initial 85-record catalog.

| Check | Result | Boundary |
| --- | --- | --- |
| Catalog metadata, unique IDs, dates, source URLs, and relationships | Passed for all 85 records | Structural validation does not judge scientific accuracy. |
| Generated Markdown consistency and local file/anchor links | Passed | Checks the committed views against their JSON source. |
| Validator negative cases in a temporary copy | Passed | Duplicate arXiv versions and invalid related IDs, featured IDs, local files, and local anchors were rejected; distinct v2/v3 repositories remained distinct. |
| Python source compilation | Passed | No external packages or scientific systems were executed. |
| Public source URL probes | 152 of 161 returned successful responses; 9 returned HTTP 403 | Restricted automated access is not evidence of a missing resource. See below. |
| Official software repository metadata | All 24 GitHub software destinations existed and were neither archived nor disabled | This does not establish maintenance quality, software safety, or license suitability. |

The nine HTTP 403 responses were three publisher DOI destinations (NEJM AI, Science, ACM), five OpenReview PDF destinations, and OpenAI's FrontierScience announcement. The catalog retains alternate accessible primary sources where available; source-access limitations are documented in the [paper](search-papers.md) and [benchmark](search-landscape.md) search logs. FrontierScience's official announcement was inspected through web retrieval. No source was removed or claimed dead solely because of these probe results.

Publication status was cross-checked across related records; Scientist-Bench and AI-Researcher share the verified NeurIPS publication. Paper and software dates can differ because an initial release and a later journal paper are different events.

GitHub Actions reruns structural validation and generated-file checks on every push and pull request; its current status is linked from the README. This report records the initial verification, not perpetual assurance about future edits or external sites.

No software installation, benchmark execution, independent scientific replication, or unattended scheduled curation run is claimed by these checks.
