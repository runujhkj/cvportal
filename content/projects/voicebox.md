---
title: "Voicebox — Local Voice Conversion"
status: "Prototype"
summary: "A local browser UI for live voice changing and higher-quality conversion of full recordings, running on a Mac or an NVIDIA Linux machine, with the option to hand long conversions to a private GPU host over SSH."
tech: ["Python", "HTML", "Beatrice", "Seed-VC", "RVC", "CUDA", "SSH", "pytest"]
problem: "The packaged voice-changer I started from would not launch on a current macOS, and nothing I found handled both low-latency live conversion and slower, better-sounding conversion of a whole recording, entirely on my own machines."
approach: "One launcher starts a local web UI and picks the engine for the machine it is on: Beatrice for live audio and Seed-VC on Apple Metal for recordings on the Mac, RVC and Seed-VC on CUDA under Linux. Full-recording jobs can be sent to a private GPU host: the file is uploaded and acknowledged before processing starts, the worker then detaches from SSH so the client can disconnect, and job identifiers make retries idempotent even when an acknowledgement is lost. Uploads and working files are removed after processing, and finished output is kept privately for a limited time."
current:
  - "Live voice changing with selectable microphone, headphones, and starter voices."
  - "Full-recording conversion, locally or on the GPU host, with a progress estimate that adapts as sections finish."
  - "Remote jobs that survive the client disconnecting, with idempotent retries and bounded retention of results."
  - "Repeatable speech and listening test procedures, and 12 test files."
  - "Third-party engines, models, and their licences kept separate from the application code."
next:
  - "Listening tests for English quality: the starter voices were trained on Japanese speech."
repo_status: "Private. The bundled voice models are restricted to noncommercial use."
---
