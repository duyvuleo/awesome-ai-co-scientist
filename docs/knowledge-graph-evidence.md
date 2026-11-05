# Knowledge graph pilot: evidence

[Guide](knowledge-graph.md) · [Standalone pilot](https://duyvuleo.github.io/awesome-ai-co-scientist/knowledge-graph/) · [Canonical records](../data/knowledge-graph/pilot.json)

Generated source-scoped answers. Review records identify the actual reviewer role. Source review does not establish scientific truth or independent reproduction.

<a id="benchmark-lineage"></a>

## Can ScienceBoard scores be compared directly across revisions?

Task inventories, evaluator repairs and split roles differ; a common name is insufficient.

| Assertion | Scope | Evidence |
| --- | --- | --- |
| <a id="sb-evolution-count-r1"></a>ScienceBoard-VE adds 108 tasks used exclusively for skill evolution. | Task inventory reported in ScienceCUA v1; original task IDs/evaluator hashes are not transcribed here. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-original-count-r1"></a>The ScienceCUA audit covers 169 original ScienceBoard tasks. | Task inventory reported in ScienceCUA v1; original task IDs/evaluator hashes are not transcribed here. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-revised-count-r1"></a>ScienceCUA substantively revises 37 tasks and removes one additional task. | Task inventory reported in ScienceCUA v1; original task IDs/evaluator hashes are not transcribed here. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-total-count-r1"></a>ScienceBoard-VE contains 276 executable tasks across evolution and final evaluation. | Task inventory reported in ScienceCUA v1; original task IDs/evaluator hashes are not transcribed here. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-ve-includes-evolution-r1"></a>ScienceBoard-VE contains a disjoint evolution-task split. | Evolution examples are not final test tasks. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-ve-includes-verified-r1"></a>ScienceBoard-VE contains the Verified final-evaluation split. | Final evaluation remains separate from evolution. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-verified-count-r1"></a>ScienceBoard-Verified retains 168 executable tasks for final evaluation. | Task inventory reported in ScienceCUA v1; original task IDs/evaluator hashes are not transcribed here. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sb-verified-revises-original-r1"></a>ScienceBoard-Verified revises the original ScienceBoard inventory audited in ScienceCUA v1. | Task changes and evaluator/environment repairs prevent assuming identical score meaning. | [Sections 4.1–4.3: 169 audited tasks, 37 revisions, one removal, 168 test tasks and 108 disjoint evolution tasks](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sc-model-evaluated-on-r1"></a>The ScienceCUA model-based panel evaluates frozen libraries on ScienceBoard-Verified. | The API-based and native-agent history/resource-access rules differ. | [Sections 4.3 and 5.1, Table 1: model-based versus native-agent protocols, resource/history access, unweighted application means](https://arxiv.org/html/2611.03238v1) (author-report) |
| <a id="sc-native-evaluated-on-r1"></a>The ScienceCUA native-agent panel evaluates frozen libraries on ScienceBoard-Verified. | The API-based and native-agent history/resource-access rules differ. | [Sections 4.3 and 5.1, Table 1: model-based versus native-agent protocols, resource/history access, unweighted application means](https://arxiv.org/html/2611.03238v1) (author-report) |

<a id="human-involvement"></a>

## Where does human work enter Cloudra’s evaluation?

Offline organization, runtime delivery and scientific target correctness remain distinct.

| Assertion | Scope | Evidence |
| --- | --- | --- |
| <a id="cl-guided-human-role-r1"></a>Human curators organize the guided run records before formal scoring. | Offline recovery uses existing evidence and conclusions; it is distinct from original runtime graph delivery. | [Section 2.6.4 and SI S1/S2: human reconstruction from each run before scoring; one run per task/configuration](https://arxiv.org/html/2611.02909v1) (author-report) |
| <a id="cl-standard-human-role-r1"></a>Human curators organize the standard run records before formal scoring. | Offline recovery uses existing evidence and conclusions; it is distinct from original runtime graph delivery. | [Section 2.6.4 and SI S1/S2: human reconstruction from each run before scoring; one run per task/configuration](https://arxiv.org/html/2611.02909v1) (author-report) |
| <a id="cl-support-vs-target-r1"></a>Across all four configurations, ten of 40 Impossible runs have self-consistency 1 and accuracy 0. | The outcome concerns the full P2 Impossible-task panel. Method-limited target correctness is separate from local calculation support. | [Section 3.2.8 and SI S2.6: ten of 40 Impossible runs combine full self-consistency with zero task accuracy](https://arxiv.org/html/2611.02909v1) (author-report) |

<a id="local-reproduction"></a>

## What has this collection actually reproduced?

These are two pre-existing component records, not new runs or end-to-end scientific reproduction.

| Assertion | Scope | Evidence |
| --- | --- | --- |
| <a id="circle-baseline-r1"></a>The recorded baseline radius sum agrees with the independent check at 0.9597642169962064. | Only the pinned component, synthetic inputs and recorded protocol. This does not establish an effect on published results. | [control_cases / independent_baseline_check](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/results.json) (local-component)<br>[What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) (local-component) |
| <a id="circle-nan-r1"></a>The pinned circle-packing evaluator accepted the recorded NaN-center control. | Only the pinned component, synthetic inputs and recorded protocol. This does not establish an effect on published results. | [control_cases / independent_baseline_check](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/results.json) (local-component)<br>[What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) (local-component) |
| <a id="circle-scope-r1"></a>Agentic Scientist circle-packing component was executed as a bounded local component check. | Executed 22 October 2026; indexed on 5 November, not rerun. No full-system or scientific-result reproduction. | [What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) (local-component) |
| <a id="circle-untested-r1"></a>The Agentic Scientist circle-packing component report leaves the end-to-end workflow untested. | Preserve source pins, original execution date, configuration, outcomes and cost. Source inspection is not a rerun. | [What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) (local-component) |
| <a id="scorer-arithmetic-r1"></a>The isolated scorer agrees with independent formulas on all 32 enumerated valid-identifier cases. | Only the pinned component, synthetic inputs and recorded protocol. This does not establish an effect on published results. | [exhaustive_valid_identifier_check; cases; not_tested](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/results.json) (local-component)<br>[What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) (local-component) |
| <a id="scorer-malformed-r1"></a>The recorded malformed-cache case with non-iterable identifiers raises TypeError. | Only the pinned component, synthetic inputs and recorded protocol. This does not establish an effect on published results. | [exhaustive_valid_identifier_check; cases; not_tested](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/results.json) (local-component)<br>[What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) (local-component) |
| <a id="scorer-scope-r1"></a>PaperOrchestra citation scorer was executed as a bounded local component check. | Executed 22 October 2026; indexed on 5 November, not rerun. No full-system or scientific-result reproduction. | [What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) (local-component) |
| <a id="scorer-untested-r1"></a>The PaperOrchestra citation scorer report leaves the end-to-end workflow untested. | Preserve source pins, original execution date, configuration, outcomes and cost. Source inspection is not a rerun. | [What ran; Evidence and limits](https://github.com/duyvuleo/awesome-ai-co-scientist/blob/577c73155c6e61d46ba6eeca67ca56aa27d7e31b/reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) (local-component) |

<a id="memory-outcomes"></a>

## Does persistent research state improve the final result?

Keep initialization, subsequent search and final selection separate; conclusions are bounded by the matched study.

| Assertion | Scope | Evidence |
| --- | --- | --- |
| <a id="car-controls-r1"></a>After aligning first-solution timing and subtracting its reward, no tested agent retains an advantage in subsequent search. | Author study, short task streams, fixed weights and native scaffolds; mostly single matched runs. No general scientific-learning claim. | [Sections 5.2–5.3 and 6.1, Table 2, Appendix B.1: initialization, efficiency, final outcomes and stricter controls](https://arxiv.org/html/2611.05108v1) (author-report)<br>[Sections 3–5.1: matched persistent/reset task streams, fixed weights, hidden test scoring, five agents and nine families](https://arxiv.org/html/2611.05108v1) (author-report) |
| <a id="car-final-outcomes-r1"></a>Final selected-solution gains vary across agents and do not consistently match the search-efficiency gains. | Author study, short task streams, fixed weights and native scaffolds; mostly single matched runs. No general scientific-learning claim. | [Sections 5.2–5.3 and 6.1, Table 2, Appendix B.1: initialization, efficiency, final outcomes and stricter controls](https://arxiv.org/html/2611.05108v1) (author-report)<br>[Sections 3–5.1: matched persistent/reset task streams, fixed weights, hidden test scoring, five agents and nine families](https://arxiv.org/html/2611.05108v1) (author-report) |
| <a id="car-initialization-r1"></a>Persistent state improves mean fixed-budget research efficiency across the five tested agents by helping them reach useful solutions sooner. | Author study, short task streams, fixed weights and native scaffolds; mostly single matched runs. No general scientific-learning claim. | [Sections 5.2–5.3 and 6.1, Table 2, Appendix B.1: initialization, efficiency, final outcomes and stricter controls](https://arxiv.org/html/2611.05108v1) (author-report)<br>[Sections 3–5.1: matched persistent/reset task streams, fixed weights, hidden test scoring, five agents and nine families](https://arxiv.org/html/2611.05108v1) (author-report) |

<a id="release-scope"></a>

## Does the inspected ScienceCUA release contain the full evaluated method?

Distinguish the paper-described method from the pinned construction-only release.

| Assertion | Scope | Evidence |
| --- | --- | --- |
| <a id="sc-code-benchmark-planned-r1"></a>The inspected release lists the benchmark components as planned for a future release. | An environment link does not establish a complete released evaluator. | [Release Scope: construction included; execution-guided self-evolution and benchmark components planned](https://github.com/HSZD-Team/ScienceCUA/blob/4d6b3779883b75280b5d5b228b0e26a8b0871e22/README.md) (project-documentation) |
| <a id="sc-code-construction-r1"></a>The inspected release includes Resource-to-Skill construction and export. | Release README at 4d6b3779883b; source inspection, no local execution. | [Release Scope: construction included; execution-guided self-evolution and benchmark components planned](https://github.com/HSZD-Team/ScienceCUA/blob/4d6b3779883b75280b5d5b228b0e26a8b0871e22/README.md) (project-documentation) |
| <a id="sc-code-evolution-planned-r1"></a>The inspected release lists execution-guided skill evolution as planned for a future release. | This pin only; not a claim about later releases or absence of the method. | [Release Scope: construction included; execution-guided self-evolution and benchmark components planned](https://github.com/HSZD-Team/ScienceCUA/blob/4d6b3779883b75280b5d5b228b0e26a8b0871e22/README.md) (project-documentation) |
| <a id="sc-full-method-r1"></a>ScienceCUA v1 describes construction followed by execution-guided skill evolution and a frozen final library. | A described and author-evaluated method; not a claim that every component was released. | [Sections 3.1–3.2: construction, execution-guided evolution, consolidation and frozen final library](https://arxiv.org/html/2611.03238v1) (author-report) |
