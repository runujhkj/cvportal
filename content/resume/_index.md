---
title: "Resume"
---

# Jeffrey "Jack" Hannon Jr.

Systems Automation and Python Tooling

{{% contact "location,phone,email,website" %}}

## Summary

HPC systems technician at Mississippi State University since 2022, and the one who writes the tooling around that work. Outside of work I build and run a self-hosted AI stack, mostly by directing LLM coding agents against specs and tests I write.

## Experience

### Computer Specialist I, HPC Center *Nov 2022 – Present* {.job}

Mississippi State University, Starkville, MS

- Diagnose and repair 10–20 failed nodes a month across four Slurm clusters (96 to 1,800 nodes), from draining the node to closing the Dell RMA, with notes on each one.
- Wrote `bad`, a Python terminal tool I use for every repair. It pulls Slurm drain state, NHC results, iDRAC logs and InfiniBand checks into one place, and it generates the monthly unplanned-outage report.
- Update firmware through OpenManage Enterprise when a node falls behind baseline, and run a regression test before it goes back into service.

### Research Computing Administrator (Contract) *May 2023 – Mar 2024* {.job}

Fox Chase Cancer Center, remote

- Set up and maintained about 40 bioinformatics packages for a genomics research group, mostly with Spack and by hand where Spack couldn't build something.
- Worked directly with the lead researcher, wrote down how every build was done, and kept older versions around for workflows that still needed them.

## Projects

### locallm (self-hosted AI stack)

- Generates the whole Docker Compose stack from one config file. Each service is a single module that also gives it a typed API client for health checks and scripting.
- Includes hardware-aware tuning and benchmarking, plus image, music and LoRA-training workflows.
- Has a benchmark where local models build iOS and Python apps through aider, scored against specs and acceptance tests the model can't edit.

### what (live transcription)

- Transcribes live audio locally with Faster-Whisper and WhisperKit and streams it to OBS captions and a live avatar, with word-level replay and corrections. Being prepared for a GPL-3.0 release.

### vplan (home network)

- Manages my home network's DNS, DHCP, per-device VPN bypass, WireGuard remote access and Authelia single sign-on, with TLS from a private certificate authority.

### langquiz (vocabulary app)

- Self-hosted Flask app for vocabulary practice in 20 languages, with spaced repetition.

## Skills

**Languages and tools:** Python, Bash, Git, pytest, Flask, SQLite, REST and SSE APIs, Docker, Ansible  
**AI tooling:** Ollama, OpenWebUI, ComfyUI, Faster-Whisper, WhisperKit, aider, Claude Code  
**Systems:** Linux (Rocky, Debian, Ubuntu), Slurm, Lustre clients, iptables, WireGuard, Pi-hole, Caddy, step-ca  
**Platforms:** Forgejo and GitHub Actions, cloud-init, QEMU/KVM, NVIDIA Container Toolkit

## Education

**B.S. Computer Science**, Mississippi State University, 2021  
**CompTIA A+**, 2025
