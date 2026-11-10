---
title: "Resume"
---

# Jeffrey "Jack" Hannon Jr.

Systems Automation · Python Tooling · Self-Hosted AI Infrastructure

{{% contact "location,phone,email,website" %}}

## Summary

HPC systems technician at a university computing center since 2022 (four Slurm clusters, about 5,000 users) who builds the automation around the work: Python and Bash tooling for repair triage and outage reporting, config-driven deployment, and API integrations across a self-hosted LLM stack. Works from specs and tests, documents what gets built, and directs LLM coding agents routinely.

## Skills

**Automation & Development:** Python, Bash, pytest, Git, Flask, SQLite (FTS5), REST/SSE APIs, Docker, Ansible  
**AI & LLM Tooling:** Ollama, OpenWebUI, ComfyUI, Faster-Whisper, WhisperKit, aider, Claude Code  
**Systems & Networking:** Linux (Rocky, Debian, Ubuntu), Slurm, Lustre clients (LNet), iptables, WireGuard, DNS/DHCP (Pi-hole), Caddy, PKI/TLS (step-ca), SSO/OIDC  
**Platforms:** Forgejo/GitHub Actions, cloud-init, QEMU/KVM, NVIDIA Container Toolkit

## Experience

### Computer Specialist I — HPC Center · *Mississippi State University · 2022–Present*

- Keep compute nodes in service across 4 Slurm clusters of 96 to 1,800 nodes (including 16 GPU and 16 bigmem nodes): diagnose and repair 10–20 hardware failures a month, from Slurm drain to Dell RMA closure, recording each node's failure cause and dated notes.
- Built `bad`, a Python terminal tool (~20,400 lines, 69 pytest files) used for every repair: Slurm drain state, NHC, iDRAC/RACADM, InfiniBand fabric checks and per-node notes. It also generates the monthly unplanned-outage reports (incidents, node-minutes down, which outages were worked).
- Bring nodes behind the firmware baseline up to date through OpenManage Enterprise, then run a regression test before returning them to service; diff BIOS settings against a known-good node.

### Research Computing Administrator (Contract) · *Remote · 2023–2024*

- Sole technical owner of a ~40-package bioinformatics stack for a genomics research group at Fox Chase Cancer Center, built with Spack and source builds despite incomplete upstream documentation.
- Worked directly with the lead researcher on installs and troubleshooting; documented build procedures so environments could be rebuilt, and maintained legacy versions that existing workflows depended on.

## Selected Projects

### locallm — Self-Hosted LLM and GenAI Stack · *Python, Docker, Ollama, ComfyUI, aider*

- Control plane that generates the Docker Compose stack from one config file through a service registry: adding a service is a single module, which also provides a typed API client for health checks, status, and scripting.
- Hardware-aware tuning and benchmarking; image, music, and LoRA-training workflows.
- Benchmark harness for local coding agents: a model on the GPU host builds iOS and Python apps via aider while another machine builds and tests over SSH, scored against specs and acceptance tests it cannot edit.

### what — Local Live Transcription Service · *Python, Faster-Whisper (CUDA), WhisperKit, Electron, OBS*

- Engine-independent transcription schema streamed over SSE to OBS captions and a live avatar pipeline; per-stream ASR workers, word-level replay and corrections. Preparing a GPL-3.0 release.

### vplan — Home Network Automation and SSO · *Bash, Python, iptables, WireGuard, Authelia*

- Inventory-driven DNS/DHCP, per-device VPN bypass, WireGuard remote access, and Authelia SSO (forward-auth and OIDC) across self-hosted services, with TLS from a private ACME CA.

### langquiz — Multilingual Vocabulary Web App · *Python, Flask, SQLite (FTS5), Docker*

20 languages from Wiktionary and Tatoeba data, SM-2 spaced repetition, self-hosted PWA.

## Education / Certifications

**B.S. Computer Science**, Mississippi State University, 2021 · **CompTIA A+**, 2025
