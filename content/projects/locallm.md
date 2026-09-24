---
title: "locallm — Self-Hosted LLM and GenAI Stack"
status: "Active"
summary: "A control plane and client layer for a self-hosted LLM and generative-AI stack (Ollama, OpenWebUI, ComfyUI) on an NVIDIA GPU host. It covers deployment, hardware tuning, image, audio, and LoRA workflows, and a harness for benchmarking local coding agents on real app builds."
tech: ["Python", "Docker", "Ollama", "OpenWebUI", "ComfyUI", "NVIDIA Container Toolkit", "aider", "SwiftUI", "pytest"]
problem: "Running a local model stack by hand means hand-edited compose files, guessed context windows, and settings that don't match the GPU they run on. It also leaves no reliable way to judge whether a small local model can actually write working software rather than just code that compiles."
approach: "A service registry generates the Docker Compose file from stack.yaml and the host's .env, so adding a service is a single Python module. The same definitions provide typed API clients for status, health checks, and scripting. Hardware-aware commands derive or measure settings from the GPU in the machine and report whether it is limited by hardware or by configuration. For coding agents, locallm scaffolds a project, runs a local model through aider on the GPU box while a Mac builds and tests over SSH, and scores the result against specs and acceptance tests the agent can read but not edit."
current:
  - "Stack lifecycle: render, up, status, doctor, update, logs, and discover/adopt for hosts already running parts of the stack."
  - "GPU readiness checks with toolkit install; tune and bench commands that separate hardware limits from configuration limits."
  - "Image workflows on ComfyUI: seeded batches with contact sheets, full-quality promotion of a pick, inpainting, variations started from a chosen image, and a prompt expander composed from rule files."
  - "LoRA training from a folder of photos (background removal, captioning around a trigger word), with checkpoint comparison sheets."
  - "Music generation batches with the same record-keeping as images, including settings read back out of the saved FLAC files."
  - "OpenWebUI chat filters for token counts and context usage, chat compaction, per-model tool-call reliability measurement, and history export for tuning."
  - "Coding-agent benchmarks: iOS and Python apps built by a local model through aider, including a Mumble text client tested against a real server and built one unit at a time."
  - "Apple Silicon native runtime alongside the NVIDIA host, with measured ComfyUI performance on an M2 Pro."
  - "An image judge that names the next edit, and a loop that applies it to the current best image."
  - "53 test modules covering the registry, renderer, clients, and workflows."
next:
  - "Image refinement and img2img from inside chat, via a shim between OpenWebUI and ComfyUI."
  - "Web search during generation, and getting the most out of a single query on each hardware target."
  - "Toward one self-hosted place for writing, drawing, music, 3D modelling, and other generative tools, paced by the hardware already on hand."
repo_status: "Private; in daily use on the home GPU host behind vplan's single sign-on."
---
