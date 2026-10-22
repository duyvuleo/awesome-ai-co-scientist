# Contribution topics

[← Start here](start-here.md) · [Contribution guide](../CONTRIBUTING.md) · [Study packs](study-packs.md)

We welcome source corrections, component replications, and documented failures. Include the inputs, methods, and limitations needed to assess the contribution.

## Open topics

| Contribution | Starting point | Output | Scope |
| --- | --- | --- | --- |
| Correct an evidence claim | Pick one cell in the [capability matrix](capability-matrix.md), read its cited section, and check the statement against that source version. | A precise correction with a primary URL and section/file locator, preserving uncertainty where needed. | Source review; no system execution required. |
| Re-run a component on another environment | Use one of the [recorded reports](reproducibility.md), retaining its source pins and fixtures. | A separately dated report with configuration differences, all outcomes, costs, and any portability failure. | Component reproduction; the recorded initial runs were on macOS ARM64. |
| Extend evaluator controls | Start with the [circle-packing report](../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) and [integrity recipe](workflows/evaluator-integrity.md). | Additional finite/nonfinite, boundary, shape, and score-consistency fixtures with an independent check. | Test the specified evaluator revision; do not infer an effect on published experiments. |
| Examine citation-resolution coverage | Start with the [citation-F1 report](../reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md). | A small public reference sample with manually checked identifiers, resolution outcomes, and explicit raw-versus-resolved denominators. | Separate resolution quality from overlap arithmetic and citation support. |
| Compare ideas with executed outcomes | Follow the [idea-to-experiment recipe](workflows/idea-to-experiment.md), using a small, declared task and budget. | A complete idea-to-artifact ledger including rejected, modified, invalid, and unsuccessful attempts. | A pilot can establish feasibility; it does not establish general superiority. |
| Document the human work | Follow the [collaboration recipe](workflows/human-ai-collaboration.md). | A task-level ledger of preparation, intervention, selection, verification time, and outcomes. | Distinguish an experience report from a controlled productivity study. |
| Improve access to the evidence | Try the [CLI](cli.md), exported data, or guides from a fresh checkout. | A reproducible bug report, accessible presentation improvement, or tested documentation correction. | Preserve citations and the difference between source checks and executions. |

These topics are proposed studies. Check existing issues and pull requests for overlap; discuss substantial experimental protocols before execution.

## Submit a contribution

- [Resource or correction](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=resource.yml): a primary-source addition, metadata fix, or evidence correction.
- [Reproduction attempt](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=reproduction.yml): work actually executed, including failures, with a specific revision, inputs, configuration, and inspectable evidence.
- [Practical experience or proposed investigation](https://github.com/duyvuleo/awesome-ai-co-scientist/issues/new?template=experience.yml): setup problems, workflow lessons, source inspection, or a plan that has not run.
- Pull request: a focused change following [CONTRIBUTING.md](../CONTRIBUTING.md). If reporting a study, distinguish original observations from copied or author-reported findings.

Include only public evidence relevant to the claim. Submitted observations remain unverified until reviewed.

## Priorities

Priorities are independent replications, failed attempts, measurements of human effort, and comparisons under declared budgets. Broader domain and language coverage should support these investigations.

Current evidence comprises documented system comparisons and two local component investigations. Cross-system performance comparisons, prospective validation, and community replications remain open work.
