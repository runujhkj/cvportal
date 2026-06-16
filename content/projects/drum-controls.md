---
title: "Drum Controls — Generative Music Engine"
status: "In development"
summary: "A Python/PySide6 desktop app that maps drum pad input (MIDI or keyboard) to stochastic musical playback via FluidSynth — producing structured-random music rather than literal drum sounds."
tech: ["Python", "PySide6", "MIDI", "FluidSynth"]
problem: "I wanted a generative background music system that responds to input but isn't rigidly sequenced — something configurable from 'structured random music' to 'deliberately discordant noise' that runs alongside other work."
approach: "Pad hits enqueue into a heap-based rhythm engine that applies chord progressions, scale-based note remapping, and configurable timing/rest probability. Each pad maps to a note number and instrument program (harp, guitar, brass, etc.) so hitting a drum triggers a melodic voice. Multiple independent instrument tracks each run their own rhythm config. FluidSynth handles local audio output via subprocess and a virtual MIDI port."
current:
  - "Visual drum pad view with customizable pad-to-note mappings."
  - "Named sound sets assigning MIDI programs and note numbers per pad."
  - "Multi-instrument orchestration with independent per-track rhythm configs."
  - "Heap-based playback engine with precise metronome injection."
  - "FluidSynth integration for local audio output."
  - "JSON-backed layouts, sound sets, and mappings."
next:
  - "GUI redesign: Orchestra tab (global BPM, key, chord progression) + Instruments tab (per-slot overrides with randomization locking)."
  - "Per-parameter randomization controls."
  - "Preset save/load for full session state."
repo_status: "Private; functional, undergoing redesign."
---
