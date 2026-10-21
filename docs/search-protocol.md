# Search protocol and coverage

Initial search date: **22 October 2026**. Coverage target: the scientific research workflow, from literature and hypothesis development to experimentation, evaluation, and communication.

This is a broad, iterative search rather than a registered systematic review. Search engines, repository discovery, and citation trails have coverage and indexing limits. The catalog should not be described as an exhaustive census. A resource's absence is not evidence that it is unimportant or nonexistent.

## Search families

| Area | Example query families | Primary-source destinations |
| --- | --- | --- |
| Integrated discovery | `AI co-scientist`, `autonomous scientist`, `agentic scientist`, `automated scientific discovery`, `AI Scientist v2 v3` | arXiv, author project pages, official research repositories |
| Named systems | `ScientistOne`, `ScientistTwo`, `ScienceBuddy`, `OpenResearch` | Canonical papers and author-linked code |
| Hypothesis and ideas | `LLM scientific hypothesis generation`, `research ideation agents`, `literature based discovery agents` | Papers, proceedings, domain journals |
| Experiments | `autonomous research agents experiment`, `self-driving laboratory`, `LLM laboratory automation`, `machine learning research agent` | System papers, official lab/project releases |
| Domain breadth | `AI scientist biology chemistry materials physics`, `virtual lab scientific agents`, `scientific code discovery` | Domain papers and research institution releases |
| Research tools | `ResearchStudio`, `PaperOrchestra`, `research literature assistant`, `paper writing agents`, `scientific figure generation` | Official repositories and documentation |
| Evaluation | `scientific discovery agent benchmark`, `research replication benchmark`, `hypothesis benchmark`, `ML research agent evaluation` | Benchmark papers, task repositories, evaluation specifications |
| Synthesis and critique | `scientific discovery agents survey`, `AI scientist evaluation limitations`, `LLM research novelty evaluation` | Surveys, methodological papers, peer-reviewed critiques |

## Search procedure

1. Resolve the requested seed names and their official links.
2. Search alternate spellings, research lineages, and adjacent workflow stages.
3. Inspect established curated lists and recent surveys for additional candidates.
4. Follow references and project links from selected primary sources.
5. Read the primary source, deduplicate paper versions and project aliases, and write a bounded annotation.
6. Separate identifiable paper, software, and benchmark contributions. Multiple records for one research family are intentional when the paper and implementation answer different reader needs; counts are records, not unique research programs.
7. Record unresolved identities and gaps; revisit them during daily curation.

## Search records

- [Papers: queries, source trail, and coverage limits](search-papers.md).
- [Systems and tools: identity checks and source trail](search-systems-tools.md).
- [Existing lists, design lessons, and benchmarks](search-landscape.md).

## Remaining coverage risks

The initial corpus is English-language and weighted toward public LLM-agent research. Non-English literature, commercial systems without technical disclosures, inaccessible publisher material, negative findings, earlier robotics and laboratory-automation literature, and specialist disciplinary work can be underrepresented. A source check confirms what a public page says; it does not independently validate an experiment or software release.

Daily search uses a seven-day overlap. Weekly passes should rotate disciplines and include older work surfaced by new citations. Monthly passes should revisit paper versions, proceedings status, renamed repositories, archived projects, and retractions or corrections.
