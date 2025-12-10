---
title: "myvm — Lightweight macOS VM Launcher"
status: "In active development"
summary: "A PySide6-based GUI for launching QEMU virtual machines on macOS with YAML-defined profiles, overlay disks, logs, and QMP sockets."
tech: ["Python", "PySide6", "QEMU", "macOS"]
problem: "I needed a quick, reproducible way to launch VM profiles on macOS without maintaining dozens of shell scripts."
approach: "A GUI that loads VM definitions from YAML, creates overlay disks as needed, builds QEMU commands, and manages logs + runtime state."
current:
  - "GUI launcher with start/stop + log viewer."
  - "YAML profiles stored under `config/vms.yml`."
  - "Automatic overlay disk creation for non-destructive VM testing."
next:
  - "Cloud-init integration for automated first-boot provisioning."
  - "Improved build workflows for ARM vs x86 images."
  - "Snapshot workflows + profile editing UI."
repo_status: "Private; moderately functional."
---
