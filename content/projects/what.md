---
title: "what — Real-Time Speech-to-Text"
status: "In development"
summary: "A streaming speech-to-text tool built around Faster-Whisper (CUDA-accelerated). Transcribes mic, file, or stdin audio and streams text output with configurable latency/accuracy tradeoffs."
tech: ["Python", "Electron", "C++", "CUDA", "Faster-Whisper"]
problem: "Real-time transcription tools are either cloud-dependent, high-latency, or require heavy integration work. I needed a local, low-latency pipeline that could handle multiplexed audio sources and serve captions to downstream consumers without restarting on reconfiguration."
approach: "A client/service architecture: the Python transcription service runs GPU inference via Faster-Whisper with VAD and exposes an SSE-based API. A stable controller sidecar (what control) intermediates between the service and GUI so reconfiguration doesn't drop connection state. The Electron GUI handles mic + desktop audio capture and live transcript display. An OBS plugin skeleton provides a native caption source as an alternative to Browser Source."
current:
  - "Python transcription service with Faster-Whisper, VAD, and SSE output."
  - "Controller sidecar for stable service lifecycle management."
  - "Electron GUI with live audio metering, mic + desktop audio capture, and transcript panel."
  - "Output modes: captions, paragraph, and JSONL logging."
  - "C++ OBS plugin skeleton for native caption source integration."
  - "Cross-platform setup scripts (Linux, macOS, Windows)."
next:
  - "v0.1 stabilization: API surface freeze, end-to-end reliability pass."
  - "OBS plugin: full caption rendering from SSE stream."
  - "Refinement loop for low-confidence segments."
repo_status: "Private; pre-release (v0.1 stabilization)."
---
