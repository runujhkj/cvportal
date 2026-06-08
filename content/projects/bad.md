---
title: "bad — HPC Administration Terminal UI"
status: "In active use"
summary: "A persistent interactive TUI for day-to-day SLURM cluster administration — replacing ad-hoc shell one-liners with a stateful session that keeps context across repeated operations on the same node sets."
tech: ["Python", "curses", "PTY", "SLURM", "NHC", "iDRAC/RACADM", "pytest"]
problem: "Day-to-day HPC sysadmin involves dozens of repeated operations across large node sets — drain tracking, health checks, BIOS queries, fix dispatch, boot watching — all previously done with separate shell one-liners that share no state and produce inconsistent output."
approach: "A persistent curses session that owns a PTY-based output capture pipeline. Every command runs inside a PTY, raw output is read via select/os.read, normalized (ANSI strip, CR handling, cluster alias substitution), and streamed live to an output tray. Named views (drainlist, failures, task nodes, notes, history, settings) are navigable by keybinding. A SudoCredentialManager caches credentials per-session via a temp FIFO and mtime-validated askpass helper, persisting them for 14 minutes across commands."
current:
  - "Node drain/enable tracking with drainlist diff snapshots across sessions."
  - "Remote NHC health check execution with normalized output capture."
  - "Batch BIOS GET/SET via Dell iDRAC RACADM."
  - "Fix command dispatch, boot watch with regex-matched stage monitoring."
  - "Physical dependency chain resolution and ticket creation."
  - "YAML-backed per-node notes and weekly drainlist summary generation."
  - "Fully interactive settings menu with live output feedback."
  - "~8,500 lines across ~90 source modules; 100+ pytest files with PTY simulation helpers for integration-level testing."
next:
  - "Structured session export for post-shift handoff notes."
  - "Plugin interface for additional fix command categories."
repo_status: "Private; in daily production use."
---
