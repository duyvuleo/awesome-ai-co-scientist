# Paper-search audit

Last checked: **2026-10-22**. This search produced **39 curated paper records**, including one historical foundation and three surveys. It is a broad, source-checked seed collection, not a claim that every relevant publication has been found.

## Scope and method

The search covered systems that participate in scientific hypothesis formation, experimental design or execution, analysis, or a connected research workflow. It included computational research, biomedical collaboration, chemistry, mathematical program search, provenance, human evaluation, and surveys. General predictive models were not included solely because they are useful to science.

1. Resolve the requested names against author papers and official projects.
2. Expand through related-work terminology, named systems, surveys, and publisher searches.
3. Open primary sources and inspect the mechanism, evaluation setting, publication status, and obvious limitations.
4. Reconcile newer journal/proceedings versions and name changes.
5. Write an original short summary separating demonstrated output from broader claims.

Search engines and third-party paper aggregators were used to discover identifiers. Inclusion and summaries rely on the primary URLs in each record. At least one primary paper, venue record, author institution, or official project source was successfully opened for every included record. This is source inspection, not independent reproduction of results or a full-text methodological audit of every paper.

## Query coverage

Queries were issued in named-system and topical groups, including:

| Search group | Representative queries | Coverage |
| --- | --- | --- |
| Requested systems | `"Agentic Scientist" paper`; `"Scientist-One" arxiv chain evidence`; `"Scientist-Two" paper`; `"ScienceBuddy" paper AI` | Agentic Scientist, ScientistOne, ScientistTwo, ScienceBuddy; differentiated Google and Sakana naming. |
| Integrated computational research | `AI Scientist autonomous research papers AI-Researcher Agent Laboratory Kosmos`; `"AgentRxiv" arxiv`; `"Denario" scientific research arxiv`; `"CycleResearcher" arxiv`; `"EvoScientist" arxiv` | Whole-workflow agents, research memory, collaboration, and writing/review cycles. |
| Hypothesis formation | `"SciAgents" arxiv`; `"SciMON" arxiv scientific ideas`; `"ResearchAgent" arxiv scientific idea generation`; `"MOOSE-Chem" arxiv`; `"Scideator" arxiv` | Graph-based reasoning, retrieval, novelty checks, hierarchical search, and human interaction. |
| Scientific laboratories and biology | `"Coscientist" "Autonomous chemical research" Nature`; `"ChemCrow" nature machine intelligence paper`; `"The Virtual Lab" AI agents Nature paper 2025`; `"Biomni" arxiv general purpose biomedical AI agent`; `"BioDiscoveryAgent" arxiv`; `"Robin" "Nature" "2026" Ghareeb` | Physical-tool integration, experimental design, domain agents, and lab-in-the-loop validation. |
| Executable discovery | `"FunSearch" Nature mathematical discoveries`; `"AlphaEvolve" arxiv`; `"An AI system to help scientists write expert-level empirical software"` | Evaluator-driven program search, mathematical constructions, and scientific software. |
| Foundations and evaluation | `"The automation of science" King 2009 Science`; `"Can LLMs Generate Novel Research Ideas" arxiv`; `"data-to-paper" scientific research arxiv`; follow-up inspection of the ideation-execution study | Historical closed-loop experimentation, traceability, and the distinction between idea ratings and executed projects. |
| Surveys and 2026 developments | `AI co-scientist autonomous scientific discovery survey 2026`; `"AI scientists" "survey" 2026 arxiv` | Domain and workflow surveys, verification gaps, runtime coordination, and 2026 training/search work. |
| Publication verification | System titles restricted to `aclanthology.org`, `proceedings.iclr.cc`, `proceedings.neurips.cc`, and `proceedings.mlr.press`; publisher and DOI follow-up | Actual proceedings/journal links support peer-reviewed labels. |

Primary source families inspected include arXiv, Nature, ACL Anthology, ICLR and NeurIPS proceedings, PMLR, PRX Intelligence, NEJM AI publisher metadata, bioRxiv metadata, author-hosted papers, and official project repositories. Search snippets can lag later versions; they were not accepted as the only source for paper content when a current primary page was available.

## Naming and version decisions

- **ScientistOne and ScientistTwo** are distinct from Sakana's **The AI Scientist** and **The AI Scientist-v2**. [ScientistOne's arXiv record](https://arxiv.org/abs/2605.26340) and [a Google publication entry](https://research.google/pubs/scientist-one-verifiable-autonomous-research-via-chain-of-evidence/) expose different titles and audit totals. The seed uses the arXiv title and avoids mixing numerical results from the two descriptions.
- **The Agentic Scientist** is the current paper title for the Sakana lineage also encountered under the repository name AI-Scientist-v3. Its ALIFE 2026 co-scientist result is not described as a fully autonomous paper.
- **The AI Scientist** and **v2** retain their individual technical-report records. The subsequent [Nature study](https://www.nature.com/articles/s41586-026-10265-5) is listed separately because it jointly presents template-based and template-free modes. These are three publications, not three unrelated systems.
- Google [Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y), [Robin](https://www.nature.com/articles/s41586-026-10652-y), and [Empirical Research Assistance](https://www.nature.com/articles/s41586-026-10658-6) have 2026 Nature articles. Their summaries use the journal evidence where available.
- [Denario](https://journals.aps.org/prxintelligence/abstract/10.1103/kk55-gc95) was published in PRX Intelligence on 2026-10-01. Its current official repository is [Denario-AI/Denario](https://github.com/Denario-AI/Denario); the earlier arXiv abstract links the older organization.
- [Scideator](https://arxiv.org/abs/2409.14634) changed title and experimental reporting across revisions. The summary follows the current version. The [author institution's record](https://cris.huji.ac.il/en/publications/scideator-human-llm-compound-system-for-scientific-ideation-throu/) identifies its peer-reviewed CAIS 2026 publication and [ACM DOI](https://doi.org/10.1145/3786335.3813161).
- [Data-to-paper](https://doi.org/10.1056/AIoa2400555) appeared online on 2024-12-03 in NEJM AI, with a January 2025 issue date. The seed's date uses the online publication date.

For arXiv-linked records, `date` generally records first submission rather than the most recent revision or eventual conference year. For records linked directly to a journal version, it records that version's online publication date. The `evidence` label records verified publication status, independently of the chronology field. A year-only value is used where a precise date is not established cleanly; the verification-gap survey's displayed submission month differs from its arXiv identifier month.

## Source-access limits

Some Nature pages redirected into cookie authentication, bioRxiv blocked direct reads, and OpenReview displayed a browser challenge. Alternate author, arXiv, official proceedings, and PubMed sources were used without attempting to bypass these restrictions.

- Coscientist and ChemCrow were checked through their preprints and additional primary bibliographic/institutional sources.
- The Virtual Lab's author repository confirms the Nature article and collaboration structure.
- Biomni's author-hosted PDF was readable when its bioRxiv page returned 403.
- BioDiscoveryAgent and CycleResearcher were verified through official ICLR proceedings PDFs after OpenReview challenged the fetch.
- Data-to-paper's journal metadata and abstract were visible through primary publisher search results; a direct DOI fetch returned 403. Its arXiv source was opened successfully.
- Scideator's ACM DOI could not be opened by the tool. Publication status was corroborated by its author institution's detailed proceedings record.
- No executable code, scientific benchmark, or wet-lab result was independently rerun during this curation pass.

## Exclusions and follow-up queue

| Candidate | Decision and reason |
| --- | --- |
| [FirstResearch](https://arxiv.org/abs/2607.05682) | Excluded: the live arXiv page marks it withdrawn, with the reason “further improvement and work consolidation.” Search summaries still present its original claims, illustrating why current version checks matter. |
| [A-Lab](https://www.nature.com/articles/s41586-023-06734-w) | Follow-up: current publisher-indexed text differs from the original PDF in title and reported synthesis counts. Direct publisher, PMC, and archive fetches did not yield a usable current full record in this pass. Resolve the correction history before adding numerical claims. |
| Specialist equations, theorem provers, robot labs, and social-science agents | Extend domain coverage in later passes. Their absence here is not evidence of absence from the literature. |
| Additional 2026 training, governance, and independent-evaluation papers | Screen by the same evidence rules; search discovery is broader than the final selected set. |
| Proprietary or unreleased system implementations | Do not infer an official code release from a similarly named community reproduction. |

This initial collection is weighted toward English-language public sources and computational/biomedical systems. Search ranking, inaccessible pages, publication delays, and changing terminology limit completeness. Later curation should use overlapping date windows, citation chasing, official release updates, and explicit correction/withdrawal checks.
