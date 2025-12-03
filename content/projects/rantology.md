---
title: "Rantology — Avatar-Based Rant Pipeline"
status: "In design / early prototype"
summary: "A Blender-based pipeline that maps audio and phoneme data onto a simple character avatar to record semi-anonymous rants."
tech: ["Blender", "Python", "Rhubarb Lip Sync", "FFmpeg"]
problem: "I wanted a low-friction way to record and share spoken thoughts without putting my actual face on camera or overproducing video."
approach: "CLI-driven pipeline where `rantology <audio> <character>` runs Rhubarb to generate phonemes, loads a prepared Blender scene with a viseme grid, animates a simple avatar, and renders to an MP4 file."
current:
  - "Character concepts and viseme grid design."
  - "Command-line Blender invocation and basic scripting."
  - "Rhubarb integration for generating phoneme JSON."
next:
  - "End-to-end automation from raw audio to final video."
  - "Reusable character definitions and camera presets."
  - "Lightweight configuration files for different output formats."
repo_status: "Not yet public."
---
