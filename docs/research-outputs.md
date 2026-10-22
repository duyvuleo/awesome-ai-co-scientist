# Research outputs and evidence

[← Overview](../README.md) · [Capability matrix](capability-matrix.md) · [Reproducibility reports](reproducibility.md)

What has automated research produced, and what evidence connects the output to the research process? These cases distinguish released artifacts, creator-reported contributions, human involvement, and independent execution. Cases follow release dates, newest first. A released model or algorithm is an outcome to investigate; its availability alone does not establish autonomous discovery.

## Recursive Flint

**Released 2026-10-21 · Sources checked 2026-10-22 · Creator-reported development case · Not reproduced here.** The release date comes from Recursive’s [update index](https://recursive.com/updates).

Flint connects a concrete released model to an automated research workflow. Recursive’s [documentation](https://docs.recursive.com/) identifies **Eureka Machine** as the autoresearch system used to build it. The [announcement](https://recursive.com/updates/introducing-recursive-flint) describes a small team of people and agents working for under four months, with contributions across:

| Development stage | Reported automated contribution |
| --- | --- |
| Architecture | Search over expert configurations and model widths. |
| Quantization | Low-bit output-head quantization with self-distillation and selected training examples. |
| Inference | Specialized kernels for low-bit computation, mixtures of experts, and attention. |

### Inspectable artifacts

| Artifact | What is available | Evidence boundary |
| --- | --- | --- |
| [Flint model card and weights](https://huggingface.co/RecursiveSI/flint) | Apache-2.0 BF16 checkpoint, configuration, tokenizer, chat template, and SGLang serving kit; 39.8B total parameters, approximately 2.5B active including the output head. | Documents the released model; does not reproduce its research trajectory. |
| [rec inference engine](https://github.com/recursive-oss/rec/blob/e53663b262af4cb1ca498e596ca8b1a2d79e0800/README.md) | Apache-2.0 runtime for local inference, with supported Apple hardware and memory requirements. | Inference code is distinct from the Eureka Machine research framework. |
| [Earlier automated-research outputs](https://github.com/recursive-org/first-steps-toward-automated-ai-research) | Training scripts, experiment logs, and selected kernel implementations from earlier benchmark investigations. | Separate precursor experiments; not Flint training provenance or a complete framework release. |

### What remains to establish

This collection inspected primary documentation and artifact listings; **we did not download weights, run Flint, or reproduce its benchmarks**. Performance and automated-development claims remain creator-reported.

For a stronger independent assessment, we would seek experiment traces connecting proposals to accepted changes, matched ablations of research assistance, and accounting for human interventions, failed experiments, and total compute. These are proposed checks, not completed findings. Local inference would test deployment behavior; it would not reproduce the process that created the model.

Explore the linked [Flint tool record](tools.md#recursive-flint-tool), [Eureka Machine system record](systems.md#recursive-eureka-machine-system), and [seven-dimension evidence map](capability-matrix.md#recursive-eureka-machine-system-sources). To plan a contribution, use the [idea-to-experiment workflow](workflows/idea-to-experiment.md).
