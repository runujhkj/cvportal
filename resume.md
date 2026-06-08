---
title: "Jeffrey \"Jack\" Hannon Jr. — Resume"
---

# Jack Hannon

Linux / HPC Systems Administration · Automation · Diagnostics  

Phone: +1 (251)-753-1915
Email: runujhkj@icloud.com  
GitHub: https://github.com/runujhkj 
Website: https://runujhkj.github.io/cvportal/

---

## Summary

Linux-focused systems administrator working in a university HPC environment.  
Day-to-day work includes Slurm-driven cluster operations, hardware triage, firmware/BIOS coordination with vendors, and automation with shell and Python. I build tools to reduce repetitive operational pain and make cluster behavior more visible.

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

- Maintain and troubleshoot compute nodes across clusters ranging from 200 to 1,800 nodes, including drain handling, node reboots, hardware diagnosis, and vendor RMA coordination.
- Coordinate firmware, BIOS, and OFED upgrades with Dell and internal teams; run test jobs and document behavioral changes.
- Write and maintain diagnostic scripts (bash, Python) to surface node state, drain reasons, file system usage, and other health signals.
- Support researchers and internal staff with job failures, environment issues, and general HPC usage questions.

### Research Computing Administrator (Freelance / Contract)  
*Remote* · 2023–2024

- Assisted small research groups with Linux server setup, configuration, and basic automation for compute/storage.
- Designed simple, reproducible configurations for lab environments that could be rebuilt from documentation and scripts.
- Operated independently with full responsibility for uptime, environment consistency, and recovery.

### GCP Data Engineer — Tata Consultancy Services  
*Remote* · 2021–2022

- Short-term contract role; gained practical exposure to GCP compute/storage and Hadoop-based data pipelines.

### Senior Intern — Center for Cyber Innovation  
*Mississippi State University, Starkville, MS* · 2020–2021

- Provided technical support for end users and internal staff, including OS troubleshooting, basic scripting, and system maintenance.
- Contributed to basic documentation and small internal tools that reduced repeat support requests.

---

## Selected Projects

### bad — HPC Administration Terminal UI
**Tech:** Python, curses, PTY, SLURM, NHC, iDRAC/RACADM, pytest

- Built a persistent interactive TUI replacing ad-hoc shell workflows for day-to-day cluster administration across large node sets
- Integrates SLURM, NHC, and Dell iDRAC RACADM into a single stateful session with live output capture, drainlist diff tracking, and cached sudo credentials
- ~8,500 lines across ~90 modules with 100+ pytest files including PTY simulation for integration-level testing

### Home Network Lab — vplan & stepfam
**Tech:** Linux, WireGuard/NordVPN, iptables, Pi-hole, step-ca, Docker, Caddy, bash, Python

- Designed and maintain a multi-segment home network with a dual-NIC Debian Linux router providing LAN-wide VPN tunneling with selective per-device bypass via iptables mangle and policy routing tables
- Built vplan: a device-management toolkit generating Pi-hole DHCP reservations and DNS records idempotently from a single source-of-truth config, with full DNS postcheck validation
- Built stepfam: a two-part PKI toolkit managing a private ACME CA (step-ca in Docker) with inventory-driven cert issuance, SSH-based deployment, trust-chain distribution, and CA rotation — integrated with Caddy for automatic TLS on self-hosted services

### netcon — iOS Network Coverage Mapper
**Tech:** Swift, SwiftUI, CoreLocation, CoreMotion, CoreData, MapKit, CoreGraphics

- Built a self-contained iOS app that passively measures Wi-Fi and cellular quality (latency, loss, throughput) as the user moves and renders results as a zoomable heatmap overlay
- Implemented a custom MapKit tile rasteriser with manual Web-Mercator projection, zoom-adaptive power-of-2 grid snapping, and confidence-based opacity blending
- Zero third-party dependencies; covers background location scheduling, Core Data persistence, and multi-format export (zip, CSV, GeoJSON)

### myvm — Apple Silicon VM Manager
**Tech:** Python, PySide6, QEMU, QMP, HVF, cloud-init

- Desktop GUI for full VM lifecycle management on Apple Silicon using QEMU with HVF acceleration and macosvm for macOS guests
- Drives QEMU over QMP Unix socket for graceful ACPI shutdown; auto-manages SSH config blocks so VMs are immediately reachable by name after first boot
- Generates cloud-init NoCloud seed ISOs with Jinja-templated user-data for reproducible guest provisioning

---

## Certifications/Awards

### CompTIA A+
**Awarded:** 11/2025

---

## Education

### B.S. in Computer Science  
Mississippi State University · 2021