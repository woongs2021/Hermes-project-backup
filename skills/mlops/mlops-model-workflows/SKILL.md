---
name: mlops-model-workflows
description: "Use when working with ML/LLM model operations across the lifecycle: Hub discovery/download/upload, local inference, serving, quantization, benchmarking, experiment tracking, model surgery, audio/image models, and evaluation workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [mlops, llm, inference, evaluation, huggingface, vllm, llama-cpp, wandb, benchmarks, models]
    related_skills: []
---

# MLOps Model Workflows

## Overview

This umbrella covers class-level ML/LLM operations: finding models and datasets, downloading or publishing to Hugging Face, running local inference, serving APIs, quantizing, benchmarking, tracking experiments, and using specialized model families. The shared pattern is to identify the model/task/hardware boundary first, then run a reproducible command or script and return concrete metrics or artifact paths.

## When to Use

- The user asks about Hugging Face Hub models, datasets, repos, downloads, uploads, or tokens.
- The user asks to run, serve, quantize, or optimize a local LLM.
- The user asks for vLLM, llama.cpp, GGUF, OpenAI-compatible local serving, batching, or throughput.
- The user asks to benchmark LLMs, run lm-eval-harness, compare models, or log/track experiments.
- The user asks about W&B sweeps/artifacts/model registry.
- The user asks about SAM segmentation, AudioCraft/MusicGen/AudioGen, or model-surgery workflows such as abliteration.

## Core Decision Tree

1. **Identify task class.** Hub I/O, inference, serving, quantization, evaluation, experiment tracking, or specialized model execution.
2. **Check hardware and runtime.** GPU/CPU, CUDA, VRAM, Python version, disk, and whether containerized serving is expected.
3. **Pin model identity.** Record repo ID, revision, file name, quantization, license/terms, and local path.
4. **Run the smallest proof.** Smoke-test a prompt, sample batch, evaluation subset, or API health endpoint before scaling.
5. **Report reproducibly.** Include commands, paths, metrics, model IDs, and caveats about benchmark scope.

## Workflow Lanes

### Hugging Face Hub

- Use the `hf` CLI or API for search, metadata, login, download, upload, and repo management.
- Prefer exact repo IDs and revision pins for reproducibility.
- For GGUF discovery, enumerate repository files and choose quantization based on hardware, not popularity alone.

### Local inference and serving

- `llama.cpp`: best for GGUF, CPU/GPU-offloaded local inference, quantization, and lightweight servers.
- `vLLM`: best for high-throughput OpenAI-compatible serving, batching, tensor parallelism, and production-ish APIs.
- Always health-check the server endpoint and run at least one real completion before claiming success.

### Evaluation and tracking

- `lm-eval-harness`: use for standardized tasks such as MMLU/GSM8K/HellaSwag; start with a small task/sample set for smoke tests.
- W&B: log config, metrics, artifacts, sweeps, and model registry entries; never claim a run exists without returning a URL/path/run ID.
- Separate benchmark results from interpretation; include hardware, batch size, precision, and sample counts.

### Specialized model families

- SAM: choose point/box/automatic mask generation; return masks/overlays and note coordinate systems.
- AudioCraft: distinguish MusicGen, AudioGen, EnCodec, and style-conditioned generation; verify output audio file paths.
- OBLITERATUS/abliteration: treat as experimental model surgery; make backups, document diff-in-means settings, and verify safety/evaluation outcomes separately.

## Consolidated Legacy Knowledge

- `huggingface-hub`: HF CLI search/download/upload and model/dataset repo operations.
- `llama-cpp`: GGUF discovery, quant selection, llama.cpp server, optimization, and troubleshooting.
- `serving-llms-vllm`: vLLM quick starts, OpenAI API serving, hardware guidance, and common issues.
- `evaluating-llms-harness`: lm-eval-harness task setup, model adapters, and benchmark reporting.
- `weights-and-biases`: W&B runs, sweeps, artifacts, integrations, and dashboard/model registry usage.
- `segment-anything-model`: SAM prompts, automatic masks, batching, ONNX deployment, and segmentation workflows.
- `audiocraft-audio-generation`: MusicGen/AudioGen/EnCodec setup and generation patterns.
- `obliteratus`: refusal-vector abliteration, analysis modules, and YAML configuration templates.

## Common Pitfalls

1. **Skipping hardware checks.** Many MLOps failures are VRAM/CUDA/runtime mismatches.
2. **Unpinned models.** Always record repo, revision, file, quant, and local path.
3. **Benchmark theater.** Tiny smoke tests prove wiring, not model quality; label them clearly.
4. **No health check.** A launched server is not working until a request succeeds.
5. **Losing artifacts.** Return W&B URLs, output directories, model paths, generated audio/image files, or benchmark JSON.

## Verification Checklist

- [ ] Model/task/runtime boundaries identified.
- [ ] Required credentials or local files checked.
- [ ] Smoke command or API request actually ran.
- [ ] Output metric/path/URL returned.
- [ ] Caveats about scale, hardware, and reproducibility included.
