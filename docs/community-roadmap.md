# Ways to make a useful contribution

[← Start here](start-here.md) · [Contribution guide](../CONTRIBUTING.md) · [Study packs](study-packs.md)

The most useful contribution helps another researcher make a decision, inspect an observation, or reproduce a bounded result. A failed attempt can be valuable when its inputs, environment, commands, and limits are clear. You do not need a large model budget to contribute.

## Choose an achievable contribution

| Contribution | Concrete starting point | Useful deliverable | Scope |
| --- | --- | --- | --- |
| Correct an evidence claim | Pick one cell in the [capability matrix](capability-matrix.md), read its cited section, and check the statement against that source version. | A precise correction with a primary URL and section/file locator, preserving uncertainty where needed. | Source review; no system execution required. |
| Re-run a component on another environment | Use one of the [recorded reports](reproducibility.md), retaining its source pins and fixtures. | A separately dated report with configuration differences, all outcomes, costs, and any portability failure. | Component reproduction; the recorded initial runs were on macOS ARM64. |
| Extend evaluator controls | Start with the [circle-packing report](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) and [integrity recipe](workflows/evaluator-integrity.md). | Additional finite/nonfinite, boundary, shape, and score-consistency fixtures with an independent check. | Test the specified evaluator revision; do not infer an effect on published experiments. |
| Examine citation-resolution coverage | Start with the [citation-F1 report](../reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md). | A small public reference sample with manually checked identifiers, resolution outcomes, and explicit raw-versus-resolved denominators. | Separate resolution quality from overlap arithmetic and citation support. |
| Compare ideas with executed outcomes | Follow the [idea-to-experiment recipe](workflows/idea-to-experiment.md), using a small, declared task and budget. | A complete idea-to-artifact ledger including rejected, modified, invalid, and unsuccessful attempts. | A pilot can establish feasibility; it does not establish general superiority. |
| Document the human work | Follow the [collaboration recipe](workflows/human-ai-collaboration.md). | A task-level ledger of preparation, intervention, selection, verification time, and outcomes. | Distinguish an experience report from a controlled productivity study. |
| Improve access to the evidence | Try the [CLI](cli.md), exported data, or guides from a fresh checkout. | A reproducible bug report, accessible presentation improvement, or tested documentation correction. | Preserve citations and the difference between source checks and executions. |

These are open contribution ideas, not assigned work or completed studies. Check existing issues and pull requests before starting overlapping work. For a substantial experiment, sharing its proposed protocol first can reveal missing controls before resources are spent.

## Submit through the right route

- [Resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=resource.yml): a primary-source addition, metadata fix, or evidence correction.
- [Reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml): work actually executed, including failures, with a specific revision, inputs, configuration, and inspectable evidence.
- [Practical experience or proposed investigation](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml): setup problems, workflow lessons, source inspection, or a plan that has not run.
- Pull request: a focused change following [CONTRIBUTING.md](../CONTRIBUTING.md). If reporting a study, distinguish original observations from copied or author-reported findings.

The forms help contributors state what happened and what remains unknown. Opening an issue does not establish that a claim has been reviewed or reproduced. Review the material you choose to share and retain only the public evidence needed to understand it.

## What would make the resource stronger next?

The priority is accumulating useful evidence: independent component reruns, transparent failed attempts, better characterization of human effort, and comparisons under declared budgets. Interactive search, additional languages, and broader domain coverage are worthwhile when they help people use this evidence. Their presence alone would not establish research quality.

The repository currently offers source-backed comparisons and two narrow local investigations. It does not yet provide a cross-system performance leaderboard, prospective scientific validation, or a demonstrated history of community replication. Contributions should expand those boundaries through observable work and keep the limitations visible.
