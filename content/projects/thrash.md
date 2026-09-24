---
title: "Thrash — Skateboarding Battle Royale"
status: "In development"
summary: "A Unity prototype of a skateboarding battle royale focused on Tony Hawk's Pro Skater–style skating feel: fully kinematic movement, procedural transitions, and a trick/combo pipeline. An art-free, all-bot vertical slice now runs the whole match loop for soak testing."
tech: ["Unity", "C#"]
problem: "I wanted a skateboarding game with genuinely good controller feel, the kind of kinematic, authored movement that made THPS satisfying, before layering on multiplayer or battle-royale mechanics. Most Unity skating prototypes rely on physics colliders, which produces floaty, unreliable results."
approach: "The skater has no Rigidbody. Ground contact is sampled by a two-axle raycast system, keeping movement fully kinematic, and transition surfaces are procedurally generated with bespoke handling for ramp launches, pipe bounces, lip exits, and air-over-lip entries. Gameplay reads input actions rather than raw keys, so the same input path serves the keyboard, gamepads, scripted test scenarios, and bots. That lets twelve bots play full matches on the real movement controller while a scenario harness replays trick paths at several frame rates to catch regressions."
current:
  - "Raycast-based kinematic movement with no Rigidbody dependency."
  - "Procedural quarter-pipes, half-pipes, grind rails, and bowls, with lip tricks working on real pipe coping."
  - "Trick/combo pipeline: input → trick driver → combo controller → scoring."
  - "Input System backend with gamepad support; bots and test scenarios drive the same action layer as the player."
  - "All-bot vertical slice: skate-park arena, twelve bots, contracting circle rounds, eliminations, results, and auto-restart for unattended soak runs."
  - "Spectator director that cuts to whoever is in the air, grinding, on a lip, or outside the circle, with manual follow and a free camera."
  - "Playtest tools: teleport to test spots, time control, input overlay, stance readout, bot inspector, and input record/replay."
  - "Movement scenario harness (7 scenarios × 3 frame rates), with each gameplay bug found by the bot slice fixed alongside a regression test."
next:
  - "Remaining stance/fakie edge cases on transitions and switch airs."
  - "Gravity-driven pumping and escape-velocity bounces on transition surfaces."
  - "Menu and game-flow structure around the match loop."
repo_status: "Private; playable-to-watch vertical slice under active development."
---
