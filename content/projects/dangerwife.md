---
title: "Dangerwife — Stealth Game Vertical Slice"
draft: true
built_by: "locallm"
status: "Prototype"
summary: "A Unity stealth-game vertical slice whose simulation core was written by a local language model through the locallm pipeline, starting from a design conversation that was turned into a spec and a test suite."
tech: ["Unity", "C#", "Unity Test Framework"]
problem: "A game idea needed a cheap answer to one question before any art or content: does its core loop (juggling timed tasks while a pursuer's suspicion meter rises) hold up as gameplay? It was also the first Unity target for the locallm build pipeline."
approach: "The design conversation was turned into a spec whose contract names each unit and what it provides: a danger meter, timed tasks, the pursuer's AI, and game state. A local model built the units one at a time against edit mode and play mode tests, with the spec and tests off limits to it. The first build produced the simulation core with no scene or MonoBehaviours; later stages added perception, rates, and the fail state through the same pipeline."
current:
  - "Simulation core: danger meter with recovery over time, timed tasks, pursuer AI driven by sight, and capture and chapter-complete states."
  - "Built in recorded stages: 28 of 28 tests on the first build in 6.8 minutes, then 38, 49, 55, and 56 as stages were added."
  - "About 2,500 lines of C# on Unity 6, with 17 test files."
next:
  - "A playable greybox scene around the simulation core."
repo_status: "Private; not yet pushed."
---
