---
title: "what — Local Live Transcription and Captions"
status: "In development"
summary: "Local live transcription with OBS captions and an editable transcript linked to the recorded audio: listen, transcribe, revisit, correct. Runs on WhisperKit on Apple Silicon and Faster-Whisper with CUDA on Linux, behind one engine-independent transcription schema."
tech: ["Python", "Electron", "Swift", "WhisperKit", "Faster-Whisper", "CUDA", "C++", "OBS"]
problem: "Real-time transcription tools are either cloud-dependent, high-latency, or throw away the audio once the text is produced. I wanted captions that run locally, show up cleanly in OBS, and keep a transcript I can scroll back through, replay word by word, and correct."
approach: "A Python service runs per-stream ASR workers (mic and desktop no longer share one serialized worker) and publishes a single transcription schema, so captions, viseme consumers such as Rantology, and other clients never branch on which engine is running. The engine resolves to WhisperKit, driven through a native Swift worker, on Apple Silicon and to Faster-Whisper on CUDA elsewhere, with a startup decode that verifies the engine before any stream uses it. An Electron GUI handles capture and review. Captions reach OBS through a browser caption box or a native plugin source."
current:
  - "Mic and desktop capture on macOS (Core Audio tap helper) and Linux (PulseAudio monitor), with input and replay devices switchable while running."
  - "Transcript scrollback with Return to live, Cmd/Ctrl-click word replay from the session recording, and in-place corrections saved with provenance."
  - "OBS caption box with drag-to-reflow at a fixed font size and frozen completed lines, verified on both the main and Aitum vertical canvases."
  - "VAD on by default; microphones delivering digital silence are detected and reported instead of producing hallucinated text."
  - "Linux NVIDIA runtime dependencies prepared automatically at startup, with a non-interactive CUDA-to-CPU fallback."
  - "Append-safe session recordings and transcript offsets that survive reconnects."
  - "Prepared for source publication under GPL-3.0-or-later, with privacy cleanup and third-party license notes."
next:
  - "v0.1 release certification: hardware acceptance checks for device switching and a full platform pass."
  - "v0.2: using saved corrections to improve recognition."
  - "Reopening past sessions in the GUI, and a packaged app instead of running from source."
repo_status: "Private for now; being prepared for public source release under GPL-3.0."
---
