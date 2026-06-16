---
title: "observe — OBS Config Management"
status: "In development"
summary: "A Python CLI and Qt GUI for managing OBS Studio configuration from a local repository, using a split schema format that decomposes OBS's monolithic scene JSON into versioned, human-readable files."
tech: ["Python", "PySide6", "obs-websocket", "FFmpeg", "SSH"]
problem: "OBS stores scene collections as a single monolithic JSON file that is difficult to version-control, diff, or share. Deploying configs to remote OBS instances and managing multi-platform streaming setups requires a lot of manual work."
approach: "Introduces a split schema format (sources/, scene_items/, templates/, meta.json) that assembles into OBS format at deploy time with a template inheritance system for recursive source/item merging. Communicates with OBS via obs-websocket for live operations. Remote deployment uses SSH + rsync."
current:
  - "Profile and scene collection deployment to local or remote OBS instances."
  - "scenes-import: decomposes an existing OBS scenes.json into the split schema."
  - "scene-rename: renames scenes in the schema and optionally in a live OBS instance."
  - "Scene canvas editor (drag/scale/rotate) in the Qt GUI."
  - "Multi-platform chat aggregation (Twitch, YouTube, TikTok) as a browser overlay."
  - "SSH tunnel management and remote A/V streaming via FFmpeg."
  - "Dual-aspect-ratio support: 16:9 / 9:16 scene pairs with vertical canvas plugin integration."
  - "obs-multi-rtmp integration for multi-destination streaming, driven from observe.json."
next:
  - "Schema validation and conflict detection on deploy."
  - "GUI scene builder with full split-schema awareness."
repo_status: "Private; actively developed."
---
