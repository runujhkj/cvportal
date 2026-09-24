---
title: "Resume"
---

# Jeffrey "Jack" Hannon Jr.

Systems Automation · Python Tooling · Self-Hosted AI Infrastructure

+1 (251)-753-1915 · runujhkj@icloud.com · github.com/runujhkj · runujhkj.github.io/cvportal

## Summary

Linux systems administrator with four years in university HPC operations (about 5,000 users) who builds the automation around the work: Python and Bash tooling for fleet triage, config-driven deployment, and API integrations across a self-hosted LLM stack. Works from specs and tests, documents what gets built, and directs LLM coding agents routinely.

## Skills

**Automation & Development:** Python, Bash, pytest, Git, Flask, SQLite (FTS5), REST/SSE APIs, Docker, Ansible  
**AI & LLM Tooling:** Ollama, OpenWebUI, ComfyUI, Faster-Whisper, WhisperKit, aider, Claude Code  
**Systems & Networking:** Linux (Rocky, Debian, Ubuntu), Slurm, Lustre, iptables, WireGuard, DNS/DHCP (Pi-hole), Caddy, PKI/TLS (step-ca), SSO/OIDC  
**Platforms:** Forgejo/GitHub Actions, cloud-init, QEMU/KVM, NVIDIA Container Toolkit

## Experience

### Computer Specialist I — HPC Center · *Mississippi State University · 2022–Present*

- Operate 4 Slurm clusters of 96 to 1,800 nodes (including 16 GPU and 16 bigmem nodes): node triage, drain handling, hardware diagnosis, and vendor RMA coordination across 10–20 hardware failures per month.
- Write and maintain Python and Bash tooling that surfaces node state, drain reasons, Lustre usage, and health signals; built `bad`, a Python terminal UI (~8,500 lines, 100+ pytest files) used daily for triage.
- Coordinate firmware, BIOS, and OFED upgrades with Dell and internal teams, including IB adapter firmware through OpenManage Enterprise; run validation jobs and document behavioral changes.

### Research Computing Administrator (Freelance / Contract) · *Remote · 2023–2024*

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
