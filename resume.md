---
title: "Jeffrey \"Jack\" Hannon Jr. — Resume"
---

# Jack Hannon

Linux / HPC Systems Administration · Automation · Diagnostics  

Email: runujhkj@icloud.com  
GitHub: https://github.com/runujhkj 
Website: https://runujhkj.github.io/cvportal/

---

## Summary

Linux-focused systems administrator working in a university HPC environment.  
Day-to-day work includes Slurm-driven cluster operations, hardware triage, firmware/BIOS coordination with vendors, and automation with shell and Python. I build small tools (dashboards, scripts, lab environments) to reduce repetitive operational pain and make cluster behavior more visible.

---

## Skills

**Systems & HPC:** Linux (Debian, Rocky, Ubuntu), Slurm, Lustre, OFED, BIOS/firmware coordination  
**Automation & Scripting:** Bash/Zsh, Python, basic C, Ansible, Git  
**Tooling & Platforms:** ReFrame, Kubernetes (lab environments), QEMU/KVM, GitHub/Gitea  
**Other:** Documentation, incident triage, vendor communication, internal tooling

---

## Experience

### Computer Specialist I — High-Performance Computing Center  
*Mississippi State University, Starkville, MS* · 2022–Present

- Maintain and troubleshoot compute nodes across multiple Slurm partitions, including drain handling, node reboots, and hardware checks.
- Coordinate firmware, BIOS, and OFED upgrades with Dell and internal teams; run test jobs and document behavioral changes.
- Write and maintain diagnostic scripts (bash, Python) to surface node state, drain reasons, file system usage, and other health signals.
- Support researchers and internal staff with job failures, environment issues, and general HPC usage questions.

### Research Computing Administrator (Freelance / Contract)  
*Remote* · 2023–2024

- Assisted small research groups with Linux server setup, configuration, and basic automation for compute/storage.
- Helped design simple, reproducible configurations for lab environments that could be rebuilt from documentation and scripts.

### GCP Data Engineer - Tata Consultancy Services
*Remote* · 2021-2022


### Senior Intern - Center for Cyber Innovation 
*Mississippi State University, Starkville, MS* · 2020–2021

- Provided technical support for end users and internal staff, including OS troubleshooting, basic scripting, and system maintenance.
- Contributed to basic documentation and small internal tools that reduced repeat support requests.

---

## Selected Projects

### Language Quiz (PySide6)
**Tech:** Python, PySide6, JSON

- Built a desktop vocabulary drill tool driven by JSON dictionaries to practice multiple languages and scripts (e.g., العربية, 日本語, русский, español).
- Implemented a simple UI with instant feedback and a debug mode to validate dictionary entries and catch malformed data.

### vkube — Local Kubernetes Lab (in progress)
**Tech:** Bash, QEMU, Ansible, Kubernetes

- Designing a reproducible lab environment using QEMU VMs and Ansible to spin up multi-node Kubernetes clusters with predictable networking.
- Goal is a single command (`vkube-up`) to create a small lab and `vkube-down` to tear it all back to a clean state.

### NodeBoard — Cluster Triage Dashboard (prototype)
**Tech:** Python, Flask, Slurm

- Implemented a small Flask-based dashboard that reads node status snapshots from existing CLI tools and visualizes drains, down nodes, and partitions.
- Intended for use inside a constrained environment (no external dependencies) to give operators a faster view of node health.

### Rantify — Avatar-Based Rant Pipeline (early design)
**Tech:** Blender, Python, Rhubarb, FFmpeg

- Designing a command-line pipeline where `rantify <audio> <character>` runs lip-sync analysis, animates a simple avatar in Blender, and renders to MP4.
- Focused on low-friction expressive output without needing to be on camera directly.

---

## Education

### B.S. in Computer Science  
Mississippi State University · YYYY
