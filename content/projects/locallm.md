---
title: "locallm — Self-Hosted LLM and GenAI Stack"
status: "Active"
summary: "A control plane for a self-hosted LLM and generative-AI stack (Ollama, OpenWebUI, ComfyUI), and a pipeline that has local models build and test real applications from a spec. It covers deployment, hardware tuning, image, audio, and LoRA workflows, and measured benchmarks of what small local models can and cannot do."
tech: ["Python", "Docker", "Ollama", "OpenWebUI", "ComfyUI", "NVIDIA Container Toolkit", "aider", "SwiftUI", "Unity", "pytest"]
problem: "Running a local model stack by hand means hand-edited compose files, guessed context windows, and settings that don't match the GPU they run on. It also leaves no reliable way to judge whether a small local model can actually write working software rather than just code that compiles, or whether a change to a prompt or pipeline helped."
approach: "A service registry generates the Docker Compose file from stack.yaml and the host's .env, so adding a service is a single Python module, and the same definitions provide typed API clients for status, health checks, and scripting. Hardware-aware commands derive or measure settings from the GPU in the machine. For building software, a conversation becomes a spec, the spec becomes a contract of units with tests, and a local model builds one unit at a time in a small context, frozen once its tests pass. The model runs on the GPU host while the machine that can build the target (a Mac for iOS, Unity for games) builds and tests over SSH. The agent can read the spec and acceptance tests but not edit them, and every run leaves a record beside the project. Claims about what helps are tested as controlled comparisons with repeated runs, not single results."
current:
  - "Stack lifecycle: render, up, status, doctor, update, logs, and discover/adopt for hosts already running parts of the stack, across an NVIDIA Linux host and an Apple Silicon Mac kept equivalent."
  - "GPU readiness checks with toolkit install; tune and bench commands that separate hardware limits from configuration limits."
  - "App pipeline for any platform: start a project, build it by units, check it, preview it, and consolidate earlier attempts into one history. Used so far for iOS (SwiftUI), Python, and Unity (C# with play mode tests)."
  - "Chat-to-spec: a requirements conversation turned into a spec and a test suite a build can be held to."
  - "A local, cached index of platform documentation the coding model can look things up in, with no live web search."
  - "Image workflows on ComfyUI: seeded batches with contact sheets, promotion of a pick to full quality, inpainting, variations from a chosen image, a prompt expander composed from rule files, and an image judge that names the next edit."
  - "LoRA training from a folder of photos, with checkpoint comparison sheets; music generation batches with the same record-keeping."
  - "OpenWebUI chat filters for token counts and context usage, chat compaction, and benchmarks of chat memory and behaviour run as marked-versus-unmarked comparisons."
  - "A LAN portal showing what each machine's stack is running."
  - "147 test files covering the registry, renderer, clients, pipelines, and workflows."
next:
  - "Sustained, unattended work: longer builds that survive a busy or restarted GPU host."
  - "Image refinement and img2img from inside chat."
  - "Toward one self-hosted place for writing, drawing, music, 3D modelling, and other generative tools, paced by the hardware already on hand."
repo_status: "Private; in daily use on the home GPU host behind vplan's single sign-on."
---

### Recorded builds

Each row is a run the pipeline recorded itself: a local model wrote the code, and the count is acceptance tests passing out of those the spec required.

| Build | Target | Result |
|---|---|---|
| Tap counter (first run) | iOS, SwiftUI | 4 of 4 tests in about two minutes, unattended, on a 10 GB RTX 3080 |
| Mumble text client | Python | 29 of 29, built unit by unit against a real Mumble server |
| Mumble client, channel-joining stage | iOS, SwiftUI | 57 of 57 in 45.3 minutes |
| Stealth-game simulation core (first build) | Unity, C# | 28 of 28 in 6.8 minutes, every unit on its first attempt |
| Stealth-game later stages | Unity, C# | 38 of 38, 49 of 49, 55 of 55, then 56 of 56 as stages were added |

The builds that became projects of their own are listed below.
