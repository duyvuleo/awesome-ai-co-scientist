## Recipe: evaluator integrity

**Question to adapt:** Does the evaluator reject invalid candidates and recompute the quantity it claims to score?

1. Pin the evaluator and baseline revisions. State which component will run and which orchestration, model, and scientific claims remain untested. Record input schema, numeric tolerances, expected outputs, dependencies, and the evaluator's allowed data access.
2. Prepare a valid baseline with an independently calculable expected result. Write the independent calculation before seeing candidate scores; do not simply copy the evaluator implementation.
3. Declare controlled invalid inputs: wrong dimensions, missing fields, duplicates, nonfinite values, out-of-range values, violated constraints, and a deliberately misreported score, as applicable. Include boundary-valid cases to measure false rejection. Keep each perturbation separate.
4. Freeze the fixture set, expected validity decisions, seed policy, time limit, and scoring rule. Preserve the fixtures and their hashes. Do not call a rejected candidate's numeric output a successful scientific result.
5. Run the valid baseline, boundary cases, and invalid controls under the same configuration. Record exit code, validity decision, emitted score, independent result, elapsed time, and errors for every case. Retain failed and timed-out cases in the denominator.
6. Compare acceptance decisions and independently recomputed scores. Report counts of invalid acceptance and valid rejection, the full case table, tolerance sensitivity, and which inputs were not tested. Separate an implementation defect from evidence that any published experiment was affected.

**Suggested artifacts:** frozen fixtures, expected decisions, portable command file, sanitized per-case results, independent checker, dependency versions, and an executed-component diff if extraction was necessary. Retain the pre-execution protocol and explain deviations.

**Completion boundary:** a valid local component check supports only the tested component and inputs. It does not reproduce agent orchestration, model behavior, research novelty, or a published headline result.
