# Evaluating AI co-scientists

[← Start here](start-here.md) · [Benchmark catalog](benchmarks.md) · [Workflow recipes](workflows/README.md) · [Study packs](study-packs.md)

Choose benchmarks according to the claim: hypothesis quality, analysis execution, result replication, or researcher productivity. These outcomes require different evidence.

This guide proposes evaluation and reporting practices; it contains no new comparative results.

## Match the task, output, and evidence

| Question | Relevant work | Evidence | Limitation |
| --- | --- | --- | --- |
| Can it propose interesting, feasible hypotheses? | [Human ideation study](papers.md#novel-research-ideas-human-study); [idea-evaluation benchmarks](benchmarks.md#ai-idea-bench-2025) | Blinded proposal assessments, provenance, feasibility assumptions, and diversity | Proposal ratings do not establish executed findings. |
| Can it complete a defined scientific analysis? | [ScienceAgentBench](benchmarks.md#scienceagentbench), [SciCode](benchmarks.md#scicode) | Executable program, task-specific outputs, errors, and cost | Success on an individual task does not establish autonomous question selection. |
| Can it improve ML engineering under constraints? | [RE-Bench](benchmarks.md#re-bench), [MLE-bench](benchmarks.md#mle-bench) | Valid held-out performance, attempts, resources, and selection rule | Engineering improvements do not by themselves establish scientific novelty. |
| Can it reproduce research from a specification? | [PaperBench](benchmarks.md#paperbench), [CORE-Bench](benchmarks.md#core-bench) | Required implementation, actual execution, and matching outputs | Distinguish reproducing from scratch from using supplied artifacts; name the benchmark variant. |
| Does human guidance improve outcomes? | [Collaboration recipe](workflows/human-ai-collaboration.md) and [Agent Laboratory](papers.md#agent-laboratory) | Matched task outcomes plus preparation, intervention, and checking effort | A preference survey alone does not measure total productivity. |
| Does a proposed discovery survive prospective testing? | [Domain-science studies](papers.md#topic-domain-science) | Prespecified candidate cohort, controls, physical or computational measurements, and independent checks | Selected successes cannot estimate the yield of unreported candidates. |

These are entry points, not interchangeable tests. Read each benchmark's current protocol, access requirements, and license before choosing tasks. ScienceAgentBench explicitly evaluates individual workflow tasks through programs, results, and costs; PaperBench distinguishes code development from execution and result matching. [ScienceAgentBench](https://arxiv.org/abs/2410.05080), [PaperBench, sections 2.2–2.6](https://arxiv.org/html/2504.01848v3).

## Write the protocol before producing candidates

Record these decisions in a [study pack](study-packs.md) before comparison.

| Decision | Record before running |
| --- | --- |
| Claim and unit of analysis | One falsifiable question; whether observations are tasks, ideas, participants, or independent runs. Repeated ratings of one artifact are not independent experiments. |
| Inputs and provenance | Exact task IDs, dataset/split versions, source revisions, information available to each condition, and any known prior exposure. |
| Conditions and baselines | A reference implementation or human workflow; the changed component; equal task access; any unavoidable differences. |
| Human roles | Who selects problems, prepares data, writes rubrics, intervenes, chooses outputs, and verifies results; record time for each role. |
| Resource limits | Elapsed-time cap, total worker time, CPU/GPU allowance, model/API cap, retries, parallelism, and grading allowance. State which limits are matched. |
| Acceptance and stopping | Validity gate, primary outcome, meaningful effect threshold, sample size or pilot scope, timeout, and early-stop rule. |
| Evaluation separation | Freeze evaluator and split hashes outside candidate write access; separate development feedback from final assessment. Record who can see held-out answers. |
| Reporting and selection | Save every planned attempt and failure; declare how a final artifact is selected; report typical and selected-best outcomes separately. |

Treat memory, external tools, and cached results as experimental conditions. Record what persists between attempts and who can modify it. A memory ablation should change memory while holding other conditions constant; a model change is a different intervention.

Resource matching is multidimensional. Equal wall-clock time can hide extra parallel workers; equal API spend can hide expert preparation or GPU usage. Report the resource vector and, where a monetary comparison is useful, the explicit conversion rates. RE-Bench demonstrates why both time allowance and the allocation of repeated attempts matter. [RE-Bench, sections 4.1–4.3](https://arxiv.org/html/2411.15114v2).

## Check validity before comparing scores

First test a known valid output and deliberately invalid controls. Independently recompute the primary metric where feasible. Record invalid acceptance, valid rejection, exceptions, missing outputs, and timeouts separately; none should silently disappear from the denominator. A high score on an invalid artifact is not a successful result.

The [circle-packing investigation](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) illustrates correctness and score disagreeing at an example evaluator boundary. The [citation-F1 investigation](../reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) illustrates correct arithmetic over a restricted denominator: resolved-identifier overlap leaves citation extraction, resolution, and support untested. Neither component observation establishes an effect on the papers' reported experiments.

For model judges, record the judge model/version, prompt, sampling, rubric, and calibration against qualified human assessments. Blind condition identity when possible, disclose remaining identifying cues, and retain disagreements. A stronger automated review rating remains a rating; it does not independently reproduce a scientific result.

## Report outcomes and failures

Link each claim to inputs, commands, environment, outputs, and independent checks. Retain setup failures, timeouts, invalid outputs, and abandoned ideas. Distinguish system failures, evaluator failures, and unassessable tasks.

Report the valid-completion rate and performance among valid outputs, with both denominators. Account for repeated tasks or participants and report uncertainty appropriate to the design. Small pilots establish feasibility and failure modes, not general superiority.

State the conclusion as: **“At revision X, component Y produced outcome Z on inputs W under budget B; independent check C agreed/disagreed; claims D remain untested.”** Separate actual model/API charges, compute, human effort, and unmeasured costs.
