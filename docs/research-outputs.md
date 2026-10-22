# Research outputs and evidence

[← Overview](../README.md) · [Capability matrix](capability-matrix.md) · [Reproducibility reports](reproducibility.md)

These cases connect released artifacts to their reported research process, human contributions, and validation. They are ordered by release date, newest first. Artifact availability alone does not establish autonomous discovery.

## Recursive Flint

**Released 2026-10-21 · Sources checked 2026-10-22 · Creator-reported development case · Not reproduced here.** The release date comes from Recursive’s [update index](https://recursive.com/updates).

Recursive’s [documentation](https://docs.recursive.com/) identifies **Eureka Machine** as the autoresearch system used to build Flint. The [announcement](https://recursive.com/updates/introducing-recursive-flint) describes a small team of people and agents working for under four months, with contributions across:

| Development stage | Reported automated contribution |
| --- | --- |
| Architecture | Search over expert configurations and model widths. |
| Quantization | Low-bit output-head quantization with self-distillation and selected training examples. |
| Inference | Specialized kernels for low-bit computation, mixtures of experts, and attention. |

### Released artifacts

| Artifact | What is available | Evidence boundary |
| --- | --- | --- |
| [Flint model card and weights](https://huggingface.co/RecursiveSI/flint) | Apache-2.0 BF16 checkpoint, configuration, tokenizer, chat template, and SGLang serving kit; 39.8B total parameters, approximately 2.5B active including the output head. | Documents the released model; does not reproduce its research trajectory. |
| [rec inference engine](https://github.com/recursive-oss/rec/blob/e53663b262af4cb1ca498e596ca8b1a2d79e0800/README.md) | Apache-2.0 runtime for local inference, with supported Apple hardware and memory requirements. | Inference code is distinct from the Eureka Machine research framework. |
| [Earlier automated-research outputs](https://github.com/recursive-org/first-steps-toward-automated-ai-research) | Training scripts, experiment logs, and selected kernel implementations from earlier benchmark investigations. | Separate precursor experiments; not Flint training provenance or a complete framework release. |

### Evidence limits

We inspected documentation and artifact listings without downloading weights or executing Flint. Performance and development claims remain creator-reported.

Independent assessment would require proposal-to-experiment traces, matched ablations, and accounting for human interventions, failed experiments, and total compute. These checks remain proposed. Local inference would test deployment, not reproduce model development.

Explore the linked [Flint tool record](tools.md#recursive-flint-tool), [Eureka Machine system record](systems.md#recursive-eureka-machine-system), and [seven-dimension evidence map](capability-matrix.md#recursive-eureka-machine-system-sources). To plan a contribution, use the [idea-to-experiment workflow](workflows/idea-to-experiment.md).
