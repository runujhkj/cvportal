---
title: "Thrash — Skateboarding Battle Royale"
status: "In development"
summary: "A Unity skateboarding game built around Tony Hawk's Pro Skater–style feel: fully kinematic movement, a full move set, battle royale and free-skate modes, a campaign core, a tutorial in progress, seven blockout levels, and an in-game level editor, built for Mac, Windows, and Linux and pinned by play mode tests."
tech: ["Unity", "C#"]
problem: "I wanted a skateboarding game with genuinely good controller feel, the kind of authored, kinematic movement that made THPS satisfying. Most Unity skating prototypes rely on physics colliders, which produces floaty, unreliable results, and feel is easy to break without noticing."
approach: "The skater has no Rigidbody: ground contact is sampled by raycasts and movement is fully kinematic. Gameplay reads input actions rather than raw keys, so the keyboard, gamepads, scripted test scenarios, and bots all drive the same path. Every playtest round is written up, turned into changes, and pinned by play mode tests, and the skating rules that survive are recorded as confirmed principles in the design doc. Bots play whole matches on every level unattended, which turns soak runs into a regression check."
current:
  - "Game loop: battle royale (rounds, shrinking circle, eliminations, results), free skate, and a campaign core with mission givers, points, and unlocks."
  - "Flow: title, profiles and saves, menus, display and camera settings, and an attract mode where a bot battle royale plays behind the main menu."
  - "Skating: flat, ramps, rails and ledges, manuals, lip tricks, wallrides and wall plants, on-foot, spine transfers, force drops, a special meter with special airs and manuals, and pools ridden as one continuous transition surface."
  - "Five greybox level drafts plus an arena (a suburb, an industrial estate, a dead mall, a spaceflight centre, and a reservoir), and blockouts of a tutorial yard and a downtown level."
  - "Tutorial: ten guided lessons whose goals are met by skating anywhere, then open challenges."
  - "In-game level editor: ground brushes, placeable pieces, a mould tool, gamepad support, and a test mode."
  - "Playtest tooling: test spots, time control, input overlay and record/replay, built-game logs, and frame-by-frame comparison against reference footage."
  - "Mac, Windows, and Linux player builds, each stamped with its build, and playtest scripts that run on Linux and Windows."
  - "Play mode tests across movement, modes, the editor, and the tutorial; 56 written-up playtest rounds."
next:
  - "Finish the new pools and bring them to every level."
  - "Finish the tutorial yard, then Downtown, as designed and proven levels rather than first drafts."
  - "Editor tools for laying out lines and gaps."
repo_status: "Private; playable with stand-in art, names, and sound throughout."
---
