---
title: "locallm — Self-Hosted LLM and GenAI Stack"
status: "Active"
featured: true
summary: "A control plane for a self-hosted LLM and generative-AI stack (Ollama, OpenWebUI, ComfyUI) that runs across several machines. It includes a coding agent that works inside chat, a pipeline that has local models build and test real applications from a spec, image, music, 3D and LoRA workflows, and measured benchmarks of what a 9–10B local model can and cannot do."
tech: ["Python", "Docker", "Ollama", "OpenWebUI", "ComfyUI", "Blender", "NVIDIA Container Toolkit", "aider", "OpenCode", "Whisper", "ACE-Step", "MediaPipe", "Prometheus", "Grafana", "SwiftUI", "Unity", "pytest"]
problem: "Running a local model stack by hand means hand-edited compose files, guessed context windows, and settings that don't match the GPU they run on. It also leaves no reliable way to judge whether a small local model can actually write working software rather than just code that compiles, or whether a change to a prompt or pipeline helped."
approach: "A service registry generates the Docker Compose file from stack.yaml and the host's .env, so adding a service is a single Python module, and the same definitions provide typed API clients for status, health checks, and scripting. Hardware-aware commands derive or measure settings from the GPU in the machine. For building software, a conversation becomes a spec, the spec becomes a contract of units with tests, and a local model builds one unit at a time in a small context, frozen once its tests pass. The model runs on the GPU host while the machine that can build the target (a Mac for iOS, Unity for games) builds and tests over SSH. The agent can read the spec and acceptance tests but not edit them, and every run leaves a record beside the project. Claims about what helps are tested as controlled comparisons with repeated runs, not single results."
current:
  - "Stack lifecycle: render, up, status, doctor, update, logs, and discover/adopt for hosts already running parts of the stack, across NVIDIA Linux, Windows/WSL, and Apple Silicon machines, kept on the same code and settings by one sync command."
  - "A gateway that serves every machine's models at one OpenAI-compatible address and sends each request to a named machine or one with a free GPU."
  - "A coding mode in chat: the agent works in a chosen repository on its own branch, cannot change tests, must write a real commit message for every change, tries scripts on a sandboxed copy, and reports whether the code still builds. It is also served over MCP to OpenCode. On a ten-task benchmark run five times per task, it went from 11 of 18 attempts solved on the first run to 49 of 50 as these rules were added."
  - "GPU readiness checks with toolkit install; tune and bench commands that separate hardware limits from configuration limits."
  - "App pipeline for any platform: start a project, build it by units, check it, preview it, and consolidate earlier attempts into one history. Used so far for iOS (SwiftUI), Python, and Unity (C# with play mode tests)."
  - "Chat-to-spec: a requirements conversation turned into a spec and a test suite a build can be held to."
  - "A local, cached index of platform documentation the coding model can look things up in, with no live web search."
  - "Image workflows on ComfyUI: seeded batches with contact sheets, promotion of a pick to full quality, inpainting, variations from a chosen image, a prompt expander composed from rule files, and an image judge that names the next edit."
  - "LoRA training from a folder of photos, with checkpoint comparison sheets; music generation batches with the same record-keeping, and music written around a spoken recording, with its stressed words landing on beats."
  - "OpenWebUI chat filters for token counts and context usage, and chat compaction. Memory changes are switched on only after A/B runs: structured summaries kept 49–53 of 57 test facts, against 38–48 without them."
  - "A read-only shell tool for models, run in a fenced account, that held all 57 scripted attacks."
  - "GPU leases on every machine: chat models, image runs, Blender renders, LoRA training, and benchmarks wait their turn for the card instead of colliding."
  - "Long jobs started from a chat run elsewhere and are watched on a LAN portal that shows each machine's queue (with cancel and pause), its outputs, and its free GPU, memory, and disk, and exports metrics to Prometheus and Grafana."
  - "3D assets a language model can use: each character gets a readable card, and a Blender tool poses, animates, and renders shots from written stage directions, with checks for feet that slide, hands that pass through bodies, and joints bent past what a joint does."
  - "A comic-reading pipeline that stresses consumer hardware: scanned pages are cut into panels, lettering is found by one model and read by another in order, and the book is written up as a record of its events and characters. Nothing from any book is stored in the repository."
  - "190 test modules covering the registry, renderer, clients, pipelines, and workflows."
next:
  - "One front end for every machine through the gateway, with tools that take a machine name."
  - "A 3D section of the portal, starting with an in-browser shot player."
  - "When a local model can't finish a task, a handoff small enough to settle in one exchange with a larger hosted model."
  - "Toward one self-hosted place for writing, drawing, music, 3D modelling, and other generative tools, paced by the hardware already on hand."
repo_status: "Private; in daily use at home behind vplan's single sign-on."
---

### Capability ladder

One 9.7B model (qwen3.5, 4-bit, 32k context) was given graded tasks in six areas, from easy rungs to hard ones. Expected results were written down before the run.

| Area | Apple Silicon Mac, 32 GB shared | RTX 3080, 10 GB |
|---|---|---|
| Text: formats, word problems, reading, multi-step reasoning | 14 of 14 | 14 of 14 |
| Code written in the reply and run against tests | 11 of 12 | 11 of 12 |
| Reading pictures drawn for the test | 6 of 6 | 6 of 6 |
| Making pictures, judged by a picture-reading model | 3 of 3 | 3 of 3 |
| Speech to text | 4 of 4 | 4 of 4 |
| Working in a real repository through the coding chat | 12 of 12 | 12 of 12 |

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
