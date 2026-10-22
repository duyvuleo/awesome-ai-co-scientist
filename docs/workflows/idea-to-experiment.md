# Recipe: connect proposals to executed outcomes

[← Workflow recipes](README.md) · [Study packs](../study-packs.md) · [Catalog CLI](../cli.md)

**Question:** Does a proposal-selection method improve completed research under an equal total resource allowance?

**Status and scope:** Proposed prospective study. Local preparation requires no paid API calls; this repository has not run the proposed idea-generation or execution comparison. A later model-driven study requires an explicit model, compute, human-effort, and grading budget.

## Why this question matters

A blinded NLP study rated LLM-generated ideas as more novel while finding weaker feasibility judgments. Its execution follow-up found that AI ideas' ratings declined more after implementation; final group differences were not statistically significant when ideas were the analysis unit. These results motivate connecting stages, not assuming that proposal preference predicts discovery. [Ideation study](https://arxiv.org/html/2409.04109v1), [execution follow-up](https://arxiv.org/html/2506.20803v1).

## Inputs and conditions

For a worked planning example, use the [recorded circle-packing task](../../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md): improve the summed radii of 26 circles in a unit square while preserving feasibility. Freeze the released baseline, independent geometric checks, held-out evaluation seeds where randomness is introduced, and a meaningful improvement threshold. Define proposal novelty separately; a higher radius sum does not establish a novel algorithm. This prospective comparison has not been run.

Use a frozen candidate pool to compare **proposal-rating selection** against **selection after a small feasibility pilot**. This isolates the selection mechanism; comparing different generators at the same time would introduce another intervention. Randomize candidate batches to the selection conditions, keep selected counts equal, and retain IDs for all candidates. Pilot execution consumes part of that condition's total budget. Give proposal review its own accounted effort; neither condition receives free screening.

## Procedure

1. Save each original proposal, assumptions, related-work sources, predicted outcome, and blinded proposal ratings. Record known source exposure and any selection exclusions.
2. Freeze the baseline, splits, evaluator, success criterion, number of selected ideas, stopping rules, and resource caps. Use a separate development split for pilot feedback.
3. Execute every selected idea, including ones that become unattractive. Log implementation changes with reasons. A materially revised hypothesis is a new or amended claim, not automatic evidence for the original proposal.
4. Give conditions comparable implementation support and operator expertise. Record human setup, debugging, interpretation, and result selection; either randomize operators or explain the assignment limitation.
5. Evaluate final artifacts under the frozen protocol, blind to selection condition where feasible. Keep proposal novelty, execution validity, metric change, and scientific interpretation as separate outcomes.

## Expected artifact and interpretation

Produce one linked record per selected idea: proposal → selection decision → baseline → attempted implementation → final artifact or failure → independent assessment. For this example, retain the returned coordinates and radii, feasibility decision, recomputed score, and resource usage. Include unselected candidates, pilot costs, failed attempts, and reasons for missing outputs. Report outcome rates over all selected ideas and distributions of valid outcomes, with both denominators explicit. Keep best-case demonstrations separate from average reliability.

The success criterion for the selection comparison is a prespecified improvement in valid completed outcomes within the matched budget, with uncertainty assessed at the idea or randomized-batch level appropriate to the design. A small pilot establishes feasibility and failure modes; it cannot support a general superiority claim.

Use the [evaluator-integrity recipe](evaluator-integrity.md) before trusting optimization results. Existing [local component reports](../reproducibility.md) show how to preserve inputs and failed controls; they provide no observation about which idea-selection strategy wins. A validated study pack is a plan, and a stronger manuscript rating remains an assessment rather than independent reproduction.
