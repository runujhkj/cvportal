---
title: "Drum Controls — Generative Music Engine"
forgejo_repo: "drumcontrols"
status: "In development"
summary: "A Python app that turns drum-pad or keyboard input into stochastic music via MIDI and FluidSynth, producing structured-random melody rather than literal drum sounds. Its core now runs headless, separate from the PySide6 GUI."
tech: ["Python", "PySide6", "MIDI", "FluidSynth", "TOML"]
problem: "I wanted generative background music that responds to input without being rigidly sequenced: within 30 seconds of setup, typing or drumming should start music that ranges from structured to deliberately discordant."
approach: "Input events feed a rhythm engine that fits generated notes into measures using chord progressions, scale-based note remapping, and configurable timing and rest probability. Each pad maps to a note and an instrument program, so a drum hit triggers a melodic voice, and each orchestration instrument has its own MIDI channel. The engine, sound sets, MIDI output, and TOML configuration have been pulled out into a headless drumcore package (drumcore.Session), with the PySide6 GUI becoming one client of it."
current:
  - "Headless drumcore package: rhythm engine, sound sets, MIDI output, and a Session that wires them together."
  - "TOML configuration layer with migration from the older JSON layouts."
  - "Multi-instrument orchestration, each instrument routed to its own MIDI channel and program."
  - "Visual drum-pad view with customizable pad-to-note mappings and named sound sets."
  - "FluidSynth integration for local audio output."
next:
  - "A single authoritative clock for the rhythm engine, fixing missed metronome beats and preview drift."
  - "GUI redesign on top of drumcore: an Orchestra tab for global BPM, key, and chord progression, and an Instruments tab for per-slot overrides."
  - "Preset save/load for full session state."
repo_status: "Private; core extracted, GUI redesign planned."
---
