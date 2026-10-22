# Recipe: test evaluator integrity

[← Workflow recipes](README.md) · [Study packs](../study-packs.md) · [Catalog CLI](../cli.md)

**Question:** Does an apparent improvement survive independent validity checks, and can candidate code alter the question being scored?

**Status and scope:** Proposed evaluation protocol with two recorded component examples. Begin locally with no paid API calls. Evaluator isolation is a proposed extension; the existing reports did not test a sealed, complete agent workflow.

## Inputs and controls

Choose one executable task, freeze the task specification, source revision, evaluator hash, tolerances, and resource limit, and identify a known valid baseline. Prepare a fixture ledger before scoring. Include ordinary valid outputs, boundary cases, and deliberately invalid outputs: wrong dimensions, nonfinite values, constraint violations, inflated reported scores, and missing results. Keep evaluator inputs separate from candidate explanations.

For each fixture, record its expected validity and an independently implemented check. Two calls to the same evaluator are a repeatability check, not independent verification. For the proposed isolation extension, place the reference evaluator and held-out fixtures outside candidate write access and compare their hashes before and after execution. Use an isolated environment with no credentials; a read-only path alone is not a complete containment mechanism.

## Procedure

1. Run the baseline and independently recompute its metric. Establish acceptance criteria before inspecting perturbed outputs.
2. Apply one controlled perturbation per fixture. Record validity, score, exit status, exceptions, and timeout independently. A numeric score must pass the validity gate before entering an improvement comparison.
3. Compare the original evaluator with the proposed isolated evaluation path using identical candidate artifacts and fixtures. Keep the metric, tolerance, timeout, and available inputs fixed; do not make the “protected” condition easier by weakening the task.
4. Measure evaluator wall time and compute separately from candidate generation. If a future agent comparison is added, include every candidate, retry, worker, and grading call in both conditions' budgets.
5. Publish all discrepancies, including valid outputs rejected by the new checks. Inspect each discrepancy before attributing it to agent behavior or evaluator design.

## A concrete local starting point

The [circle-packing report](../../reports/reproducibility/2026-10-22-agentic-scientist-circle-packing/report.md) provides pinned sources, fixtures, commands, and independent geometry checks. Its example evaluator accepted a NaN coordinate; a separate overlap run returned `correct=false` while emitting a score. The [citation-F1 report](../../reports/reproducibility/2026-10-22-paperorchestra-citation-f1/report.md) provides a standard-library-only scoring example with malformed-cache controls. Follow each report's separate acquisition and execution steps; preserve its source pin and save fresh outputs separately.

These examples reproduce component behavior, not agent orchestration, published scientific findings, or the effectiveness of isolation. Both recorded runs made zero model/API calls; local hardware and energy costs were unmeasured. The broader motivation is supported by the Agentic Scientist paper's audit of evaluation-procedure changes in a particular RL study. [Primary paper, section 6.3](https://arxiv.org/html/2610.18933v1).

## Expected artifact and success criterion

Produce a fixture table containing expected validity, observed acceptance, independently calculated score, failure type, and evaluator revision, plus a cost record and source hashes. A proposed acceptance criterion is that every prespecified invalid fixture is rejected, every valid control is accepted, and valid scores agree within the declared tolerance. Passing this finite suite establishes only those tested properties. Finding a false acceptance is a useful result; it does not establish that a published experiment was affected.
