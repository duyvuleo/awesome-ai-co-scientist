# Systems and tools search notes

Search and source-check date: **2026-10-22** (Australia/Sydney).

The initial search produced **28 entries: 13 systems and 15 tools**, stored in [systems-tools.json](../data/systems-tools.json). It complements the paper search; it is a documented coverage pass, not a claim that every scientific agent or commercial research tool has been found.

## Search approach

1. Resolve the requested names against primary sources: Agentic Scientist, OpenResearch, ScientistOne, ScientistTwo, ScienceBuddy, ResearchStudio, and PaperOrchestra.
2. Expand across the research workflow: literature search and screening; ideation; experiment execution and algorithm search; writing and illustration; scientific tool and document infrastructure.
3. Search by exact project name plus GitHub, official, authors, or paper; follow author/project links to repositories.
4. Open the canonical repository or official project page and, where applicable, its publication record. Use owner identity, paper links, and repository descriptions to separate originals from forks or community implementations.
5. Write original summaries of 35–65 words, recording primary sources and an explicit check date. Avoid copying README prose, popularity counts, unsupported superlatives, and productivity numbers without study context.

Representative search strings included:

- `"Agentic Scientist" github`
- `"ScienceBuddy" AI research`
- `"ResearchStudio" AI research github`
- `"PaperOrchestra" github`
- `ScientistTwo official github 2609.19644`
- `ScientistOne Google official project website`
- `Virtual Lab AI scientists github Stanford`
- `Biomni github official 2025`
- `Coscientist github Boiko 2023 official`
- `OpenScholar github allenai.org`
- `ASReview github systematic reviews Nature Machine Intelligence`
- `RD-Agent microsoft github research development agent`
- `ShinkaEvolve github SakanaAI paper`

## Resolved identities

| Requested name | Canonical source | Resolution |
| --- | --- | --- |
| Agentic Scientist | [SakanaAI/AI-Scientist-v3](https://github.com/SakanaAI/AI-Scientist-v3) | Official implementation; distinct from AI Scientist v1 and v2. |
| OpenResearch | [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) | alphaXiv's local research workspace and agent harness. |
| ResearchStudio | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | Resolved to Microsoft's Idea and Reel skill collection. Unrelated similarly named qualitative-research products were excluded. |
| PaperOrchestra | [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | Official repository, linked to the [author project page](https://yiwen-song.github.io/paper_orchestra/) and [paper](https://arxiv.org/abs/2604.05018). Search results also surfaced third-party skill implementations; these were not substituted for the original. |
| ScienceBuddy | [Gen-Verse/ScienceBuddy](https://github.com/Gen-Verse/ScienceBuddy) | Official research repository linked from [PhAI Labs](https://phai-labs.com/en/papers/sciencebuddy/). |
| ScientistOne | [Project](https://scientist-one.github.io/) | Public generated papers and solver code are distinguished from complete framework source. |
| ScientistTwo | [Project](https://scientist-two.github.io/) | Public project and generated research artifacts; complete framework source was not confirmed. |

## Evidence and availability boundaries

- **Source inspection is not runtime validation.** None of these systems or tools was installed, executed, benchmarked, or independently reproduced as part of this curation pass.
- **Paper, system, and tool entries have different purposes.** A publication explains a contribution and its evaluation; a system entry explains the research workflow and access route; a tool entry explains a reusable component. Cross-listing an underlying work in those categories is intentional when the descriptions add different information.
- **Evidence labels describe the source supporting an entry.** `project` denotes repository/product documentation; `preprint` denotes an associated preprint; `peer-reviewed` is used when a venue or publisher record was confirmed. A source's peer-review status is not independent validation of the current software release.
- **Dates are not freshness scores.** The year/date refers to the cited paper, documented release, or project origin where verified. Year-only values retain uncertainty about the precise day. The separate `checked` field records this curation pass.
- **Code availability has several meanings.** Tags distinguish complete public implementations, research experiment code, supporting code, generated artifacts, hosted access, and unconfirmed framework source. A public repository does not imply all hosted-product functionality is public.
- **ScienceBuddy:** the [README](https://github.com/Gen-Verse/ScienceBuddy) explicitly separates its hosted workspace demonstration from open harness/RL experiments on frozen tasks with simulated feedback. The latter does not by itself establish deployed continual learning.
- **Coscientist:** the [repository](https://github.com/gomesgroup/coscientist) supplies a simplified implementation and supporting data under Apache 2.0 with a Commons Clause restriction; it is not labeled an unrestricted complete system release.
- **Google Co-Scientist:** the [May 2026 announcement](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/) and [Nature article](https://www.nature.com/articles/s41586-026-10644-y) support the peer-reviewed tag; the 2025 year records the earlier system introduction.
- **OpenScholar:** the [Ai2 publication update](https://allenai.org/blog/nature-openscilm) confirms the later Nature publication. The origin remains 2024.
- **AI Scientist v1/v2:** the [March 2026 Nature article](https://www.nature.com/articles/s41586-026-10265-5) explicitly connects its template-based and template-free systems to both official repositories. Their system records therefore carry a peer-reviewed source label while retaining their 2024/2025 origin years. The workshop evaluation included human selection, and submissions were withdrawn following review.
- **STORM:** the [NAACL 2024 proceedings record](https://aclanthology.org/2024.naacl-long.347/) confirms its peer-reviewed status.
- **PaperQA2:** the [arXiv submission history](https://arxiv.org/abs/2409.13740) explicitly records its first submission on 2024-09-10; the numerical identifier alone must not be used to infer a different submission day.
- **ShinkaEvolve:** the [official repository](https://github.com/SakanaAI/ShinkaEvolve) and [ICLR record](https://openreview.net/forum?id=lKEdGCoDNC) support the peer-reviewed tag; the original preprint is from 2025.
- **Kosmos:** advertised equivalents to months of human research involve user estimates and modeling assumptions, not a controlled universal productivity measure.
- **OpenEvolve:** an independent community implementation inspired by AlphaEvolve, not a release of Google's original framework.

## Coverage and next passes

The seed emphasizes public implementations and clearly identifiable research systems. It includes adjacent components only when their role in a co-scientist pipeline is concrete. Generic coding agents and broad commercial tool directories were not added merely to increase the count.

Further curation should expand specialized chemistry/materials agents, self-driving laboratories, social-science workflows, scientific memory and provenance infrastructure, evaluation harnesses, and negative or independent replication studies. Daily additions should follow primary sources, check for rebranding or official releases, and retain uncertainty when identity, code provenance, or evidence status remains unresolved.

All per-entry source URLs are stored in the JSON. Repository reachability and README inspection establish identity and documented functionality; they do not establish package safety, licensing suitability for a particular use, scientific correctness, or operational readiness.

## 2026-10-22 addition: Recursive research outputs

Added Eureka Machine and Flint as linked system and tool records, bringing this catalog to **30 entries: 14 systems and 16 tools**. The [official update index](https://recursive.com/updates) dates the initial automated-research announcement to 2026-06-11 and Flint to 2026-10-21. The [research-output case](research-outputs.md#recursive-flint) records the model, its development context, and public artifacts. Source inspection only; no model download, execution, or benchmark reproduction was performed.
