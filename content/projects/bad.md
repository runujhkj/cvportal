---
title: "bad — HPC Node Failure Workflow Tool"
status: "Active"
featured: true
summary: "A command-line tool and curses TUI for HPC cluster administrators: diagnose down nodes, drain them with documented reasons, and record hardware changes the same way on every cluster, with each command logged."
tech: ["Python", "curses", "PTY", "Bash", "pdsh", "SLURM", "NHC", "iDRAC/RACADM", "pytest"]
problem: "Day-to-day HPC administration means dozens of repeated operations across large node sets: drain tracking, health checks, event-log pulls, BIOS queries, reboots, and service restarts. They were previously done with separate site-specific scripts that share no state, differ from cluster to cluster, and leave no consistent record of what was run."
approach: "A command runner wraps the cluster's management scripts behind one stable interface. Commands are defined in per-cluster catalogs rather than hardcoded tool paths, every command accepts --dry-run and a one-line description, and each run goes to an audit log. Parallel execution uses pdsh and falls back to a sequential ssh loop when pdsh is missing. Management-interface actions go through a selectable backend: Dell iDRAC is implemented, and an HPE iLO stub fails with a clear message instead of guessing. On top sits a persistent curses TUI that runs each command in a PTY, streams normalized output to a tray, and caches sudo credentials for the session so privileged workflows prompt once."
current:
  - "Task-list workflow: add nodes, run checks and NHC, pull the system event log, reboot through the management interface, restart lnet, filesystems, and slurmd in order, then drain with a formatted reason."
  - "Boot-stage watch that only reads state, so it is safe to run on any node at any time."
  - "BIOS inspection and configuration through iDRAC, plus a BIOS firmware baseline update workflow."
  - "Drainlist views with diff snapshots across sessions, and YAML-backed per-node notes rendered as a table."
  - "Per-cluster configuration through environment variables and command catalogs, including a configurable pdsh invocation."
  - "About 20,400 lines of Python across 115 modules, with 69 pytest files, and written docs: a design spec, a roadmap, a catalog map, and a guide to adding a command."
next:
  - "Independent scrolling for the output tray, and stable tray height when the terminal resizes mid-command."
  - "The guided wizard workflow described in the design spec."
repo_status: "Private; used daily for node triage at work. A personal tool rather than a team one, but its output (drainlists, failure summaries, node notes) is regularly handed to coworkers for analysis and tracing."
---
