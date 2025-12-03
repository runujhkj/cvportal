---
title: "NodeBoard — Cluster Triage Dashboard"
status: "Prototype"
summary: "A small internal web dashboard that visualizes node states from Slurm and related tools for faster triage."
tech: ["Python", "Flask", "Slurm", "Linux"]
problem: "Scanning raw Slurm and monitoring output across hundreds of nodes makes it easy to miss patterns in failures and drains."
approach: "A Flask-based dashboard that pulls in data from existing CLI tooling (e.g., drainlist scripts), summarizes node health, and surfaces changes in state over time."
current:
  - "Run-from-shell Flask app that reads snapshot data and displays node status."
  - "Basic grouping by partition and drain reason."
  - "Simple install footprint suitable for running inside a constrained environment."
next:
  - "Move from flat-file snapshots toward a small database backend."
  - "Add authentication and role-based views."
  - "Expose simple JSON endpoints for other tools."
repo_status: "Private internal tool."
---
