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

## 2026-10-23: judgment, physics evaluation, and analytical robustness

The rolling search targeted 16–23 October 2026, with older work retained when surfaced by recent indexing. Publication dates below come from primary records, not search-engine recency labels.

| Addition | Primary evidence inspected | Scope |
| --- | --- | --- |
| [SEER-Repro study](https://arxiv.org/abs/2610.23845) | Version 1, sections 3–4 and Appendix F | One paper and one benchmark record; report grading and expert review limits retained. Public package release unverified. |
| [SciPIvot](https://arxiv.org/abs/2610.21082) | Version 1, benchmark construction and limitations; [official repository](https://github.com/AutoResearch-Factory/SciPIvot) | Recognition of corrective decisions; does not estimate failure prevalence or test autonomous execution. First submitted 15 October. |
| [PhysClosureBench](https://arxiv.org/abs/2610.21767) | Version 1, section 3 and Appendix B; [repository](https://github.com/uncertainty2019/PhysClosureBench) and [dataset page](https://huggingface.co/datasets/Tauben/PhysClosureBench) | Separate partial accomplishment and closure criteria; distinguish execution framework from scientific grading. First submitted 15 October. |
| [AInsteinBench](https://arxiv.org/abs/2512.21373) | Primary abstract, submission history, and [official README](https://github.com/ByteDance-Seed/AInsteinBench) | Older coverage addition dated 24 December 2025; some environment images require a request. |

Queries included `site:arxiv.org "scientific discovery" after:2026-10-15 before:2026-10-24`, `site:arxiv.org "research agent" after:2026-10-15 before:2026-10-24`, and exact-title searches for the selected studies. Recent search results surfaced AInsteinBench under an October discovery date; the original submission date was retained. None of the added resources was executed, and no research datasets were downloaded.

The inspected arXiv records for Agentic Scientist, ScientistOne, ScientistTwo, ScienceBuddy, and PaperOrchestra still identify version 1. Official OpenResearch, ResearchStudio, and PaperOrchestra documentation was also reviewed; no new catalog claim was warranted by this pass. ResearchStudio's tool date remains its documented 3 July release, distinct from the 5 July paper submission.

Further leads include AutoSciBench, Gan Jiang, and recent methodological critiques. These require a separate inclusion review; discovery alone does not establish their claims or release status.

## 2026-10-23: audit of two missed papers

[DiscoveryRSI](https://arxiv.org/abs/2610.23839) was first submitted on 16 October and revised on 20 October; [Agent4Sci](https://arxiv.org/abs/2610.28763) was submitted on 20 October. Both fell inside the prior search window and were absent from the catalog and exclusion queue. This was a retrieval/coverage miss, not a duplicate-removal decision.

| Check | Observed result |
| --- | --- |
| Repeat `site:arxiv.org "scientific discovery" after:2026-10-15 before:2026-10-24` | DiscoveryRSI was not returned. |
| Exact-name queries `site:arxiv.org "DiscoveryRSI"` and `site:arxiv.org "Agent4Sci"` | No results from the web-search service, despite readable primary arXiv pages. |
| Unrestricted DiscoveryRSI search and official-lab search | Retrieved the [official repository](https://github.com/Gen-Verse/DiscoveryRSI) and [PhAI Labs release announcement](https://phai-labs.com/news/discoveryrsi/). |
| Direct arXiv submission query using the expanded family in the [search protocol](search-protocol.md#retrieval-cross-checks), 16–23 October | Retrieved 89 of 89 metadata records and included both papers. Other returned candidates still require relevance screening; the count is not 89 accepted additions. |

A separate revision pass paged 200 metadata records in descending update order, crossed the 16 October boundary, and retained 139 records updated within the window, including both requested papers. This is retrieval coverage for the stated query family, not completed relevance screening. Tests with DiscoveryRSI confirmed that `submittedDate` is a range filter, while `lastUpdatedDate` must be used for sorting and followed by timestamp filtering.

The earlier pass depended on ranked results and did not complete an independent metadata or lab-release cross-check. The observations establish a failure of that retrieval route; they do not isolate the search provider’s internal indexing or ranking cause. The revised protocol adds complementary retrieval paths, pagination checks, and fixed known-paper probes.

DiscoveryRSI is annotated from **v2**, with the original submission date retained. Sources inspected include sections 3–7 and Appendices C–F, the public harness, DFM-Bench, and the model card. The implemented model objective is offline weighted supervision; proposal review, retrospective literature correspondence, computational readiness, and independently confirmed discovery remain distinct.

Agent4Sci is annotated from **v1**, including the evaluation protocol and Appendix A limitations, plus its [runner](https://github.com/maszhongming/agent4sci) and [dataset card](https://huggingface.co/datasets/MingZhong/agent4sci). The arXiv NeurIPS 2026 E&D comment was not promoted to a peer-reviewed label without a verified venue record. No models, upstream programs, or datasets were executed or downloaded.

## 2026-10-24: integrity, proposal judgment, and constrained scientific workflows

The direct arXiv pass covered 17–24 October in UTC: **83 submission-window records** and **140 update-window records**. Submission retrieval exhausted its result set; revision retrieval crossed the start-date boundary. The merged ledger retained 140 unique versioned records: two already cataloged, four selected after primary-source review, and 134 awaiting further relevance review. These are retrieval counts, not claims of exhaustive literature screening. DiscoveryRSI v2 and Agent4Sci v1 remained retrievable as fixed probes.

| Selected work | Primary evidence inspected | Inclusion boundary |
| --- | --- | --- |
| [RIDAR](https://arxiv.org/abs/2610.31372) | v1, sections 3–6, limitations, and [official release](https://github.com/THU-KEG/RIDAR) | Paper, auditor tool, and RIV-Gold benchmark views; model-detected violations under deliberately exposed constraints are not universal failure rates. |
| [ADAPT for Science](https://arxiv.org/abs/2610.30851) | v1, sections 3.6, 4, and 5 | Gravitational-wave detector optimization in simulation; broader scientific transfer remains untested. |
| [GeoAgent](https://arxiv.org/abs/2610.31096) | v1, sections 6–10 | Fixed seismic workflow with one-dataset engineering evidence; no controlled multi-domain evaluation. |
| [SoundnessBench](https://arxiv.org/abs/2605.30329) | v2, sections 2–3, [code](https://github.com/hosytuyen/SoundnessBench), and [dataset card](https://huggingface.co/datasets/hosytuyen/SoundnessBench) | Paper and benchmark views; full-paper proxy labels and proposal-only expert judgments remain distinct. The first-submission date stays 28 May despite the 22 October revision. |

RIDAR’s arXiv abstract promises a future release, but the official repository documents a **23 October code release** and exposes implementation and result files. Complete raw trajectories and annotation-package availability were not established from the inspected tree. An [earlier ICLR submission](https://openreview.net/forum?id=842NHIqIg4) is marked withdrawn in OpenReview’s public metadata and reports different results; annotations follow the current October arXiv preprint, without mixing versions or claiming peer-reviewed acceptance.

The named seed papers (Agentic Scientist, ScientistOne/Two, ScienceBuddy, ResearchStudio-Idea, and PaperOrchestra) retained the versions already represented in the catalog. The [PhAI Labs release page](https://phai-labs.com/news/) still led with DiscoveryRSI. [OpenResearch v0.2.21](https://github.com/alphaXiv/OpenResearch/releases/tag/v0.2.21) was inspected, but its maintenance and tracking changes did not warrant a new scientific-capability claim. Repository release checks also covered ResearchStudio and PaperOrchestra.

Follow-up candidates retained for review include SplatLab (`2610.30468`), GAV (`2610.30292`), Astro2Method (`2610.30282`), ExpEvolve (`2610.29303`), Magnolia (`2610.27230`), and SwarmRSI (`2610.20431`). No candidate is treated as excluded merely because it remains unreviewed. No upstream programs, model weights, or research datasets were executed or downloaded.


## 2026-10-25: reusable experience and domain-specific evaluation

The rolling search covered **18–24 October UTC**, through 23:04 UTC on 24 October (25 October in Sydney). The protocol query retrieved all **79 submission-window records**. Two revision pages of 100 records crossed the start-date boundary; **131 records** remained within the update window. A supplementary submission query using `persistent-memory`, `method selection` with `astronomy`, plural `scientific agents`, and `self-driving laboratory` retrieved all **41 results**, adding ten records to the merged set. The combined ledger contains **141 unique versioned records**: six already cataloged, four selected after primary-source review, and 131 awaiting further relevance review. These counts describe retrieval, not exhaustive screening. All four selected works were also present in the main query family.

| Selected work | Primary evidence inspected | Catalog treatment and boundary |
| --- | --- | --- |
| [ExpEvolve](https://arxiv.org/abs/2610.29303) | v1, sections 4–5 and Appendix A | Paper on idea-factor extraction and evolutionary search; small executable tasks and assumption-dependent theory. The manuscript identifies an earlier CausalEvolve version; no separate duplicate was added. |
| [GAV](https://arxiv.org/abs/2610.30292) | v1, sections 2–4 and 6; [official implementation](https://github.com/PotatoJnny/PDE-GAV) | Paper plus experimentation tool. Manufactured references support controlled PDE feedback; the public repository does not contain all historical experiment assets. |
| [Magnolia](https://arxiv.org/abs/2610.27230) | v1, sections 2, 4.4, 5, and 8; [official repository and limitations](https://github.com/HolobiomicsLab/Magnolia-AI) | Paper plus supporting infrastructure tool. The authors disclaim autonomy; project-internal replay checks and supervised campaign observations remain distinct. |
| [Astro2Method](https://arxiv.org/abs/2610.30282) | v1, sections 2–4 and source-exposure analysis; [dataset card](https://huggingface.co/datasets/Xingzhongfan/Astro2Method) | Benchmark for retrospective method selection, with source-paper exposure separated from reasoning over historical literature. |

Exact-ID probes confirmed the currently cataloged versions of Agentic Scientist, ScientistOne, ScientistTwo, ScienceBuddy, ResearchStudio-Idea, and PaperOrchestra. DiscoveryRSI v2 and Agent4Sci v1 remained retrievable. Official release checks found OpenResearch still at [v0.2.21](https://github.com/alphaXiv/OpenResearch/releases/tag/v0.2.21); ResearchStudio and PaperOrchestra exposed no GitHub releases. These checks did not justify changes to existing capability claims.

Pending primary review includes SplatLab (`2610.30468`), MLEvolve v2 (`2606.06473`), OptScientist (`2610.28562`), scientific research-team discovery (`2610.28887`), research-trajectory modeling (`2610.27337`), and Bayesian model discovery (`2610.25747`). Broader web discovery also surfaced AgentDiscover (`2610.05334`) and Station (`2610.08927`), outside this submission window; neither was added from a search snippet. No pending item is treated as excluded. No upstream programs or research experiments were run, and no datasets or model weights were downloaded.
