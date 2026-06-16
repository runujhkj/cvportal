---
title: "Thrash — Skateboarding Battle Royale"
status: "In development"
summary: "A Unity prototype of a skateboarding battle royale game, focused on Tony Hawk's Pro Skater–style skating feel. Fully kinematic movement, procedural geometry, and a trick/combo pipeline — with battle-royale scaffolding present but not yet the focus."
tech: ["Unity", "C#"]
problem: "I wanted to build a skateboarding game with genuinely good controller feel — the kind of kinematic, authored movement that made THPS satisfying — before layering in multiplayer or battle-royale mechanics. Most Unity skating prototypes rely on physics colliders, which produces floaty, unreliable results."
approach: "The skater has no Rigidbody; ground contact is sampled via a two-axle raycast system (AxleGroundSampler), keeping movement fully kinematic. Transition surfaces (quarter-pipes, half-pipes, grind rails, bowls) are procedurally generated with bespoke physics handling for ramp launches, pipe bounces, lip exits, and air-over-lip entries. A travel-direction refactor separates the three conflated axes (direction of travel, board orientation, stance/fakie) into one authoritative value to eliminate a recurring class of stance/direction bugs."
current:
  - "Raycast-based kinematic movement with no Rigidbody dependency."
  - "Procedural quarter-pipes, half-pipes, grind rails, and bowls (including kidney shapes)."
  - "Trick/combo pipeline: input → trick driver → combo controller → scoring."
  - "Battle-royale scaffolding: player registry, contracting safe-zone controller, minimap HUD."
  - "Runtime mesh builders shared between editor scene builders and a scaffolded in-game park editor."
  - "Debug instrumentation: ring-buffer movement log, live travel-direction gizmo, input logging."
next:
  - "Complete travel-direction refactor and resolve stance/fakie edge cases."
  - "Gravity-driven pumping and escape-velocity bounces on transition surfaces."
  - "Drop-in and air-over-lip entry polish."
repo_status: "Private; functional skating sandbox under active development."
---
