---
title: "Resume (HPC Systems)"
---

# Jeffrey "Jack" Hannon Jr.

Linux / HPC Systems Engineering · Slurm · Lustre · Automation

+1 (251)-753-1915 · runujhkj@icloud.com · github.com/runujhkj · runujhkj.github.io/cvportal

## Summary

Systems administrator with four years operating HPC clusters across four Slurm deployments — 96 to 1,800 nodes — on Rocky Linux, with Lustre parallel filesystems and Dell iDRAC/OFED hardware management. Day-to-day scope spans node triage, drain management, firmware and BIOS coordination, OFED and IB adapter firmware upgrades, and vendor RMA at fleet scale. Maintains Python and Bash tooling for fleet visibility, automated health assessment, and operational workflow reduction.

## Skills

**HPC & Systems:** Slurm, Lustre, OFED, NHC, Dell iDRAC/RACADM, BIOS/firmware, RMA workflow, Linux (Rocky, Debian, Ubuntu)  
**Automation:** Python, Bash, Ansible, Git, pytest, ReFrame  
**Networking:** DNS/DHCP (dnsmasq, Pi-hole), iptables, WireGuard, policy routing, PKI/TLS (step-ca, ACME, mTLS)  
**Other:** QEMU/KVM, Docker, cloud-init

## Experience

### Computer Specialist I — High-Performance Computing Center
*Mississippi State University, Starkville, MS* · 2022–Present

- Administer and triage compute nodes across 4 Slurm clusters ranging from 96 to 1,800 nodes (16 GPU nodes, 16 bigmem nodes) under Rocky Linux; routine work includes drain management, hardware diagnosis, node reboots, and vendor RMA coordination.
- Coordinate firmware, BIOS, and OFED upgrades with Dell and internal teams, including IB adapter firmware managed through OpenManage Enterprise; run validation jobs and document behavioral changes.
- Maintain Python and Bash tooling to surface Slurm state, drain reasons, Lustre filesystem usage, and node health signals across the fleet.
- Built and maintain `bad`, a Python TUI used daily for personal node triage, integrating Slurm, NHC, and iDRAC/RACADM into a single session with live output capture and drainlist tracking.
- Support approximately 5,000 researchers and staff; handle roughly 10–20 hardware failure events per month.

### Research Computing Administrator (Freelance / Contract)
*Remote* · 2023–2024

- Lead administrator and sole technical owner of the software environment for a genomics research group at Fox Chase Cancer Center, working directly with a small team of researchers.
- Built and maintained a ~40-package bioinformatics stack using Spack, with manual source builds where Spack couldn't cover a tool; resolved dependency conflicts and build failures, often from incomplete upstream documentation.
- Documented build procedures so environments could be rebuilt, and kept the stack current across upstream releases while also maintaining legacy versions of software for needed workflows.

## Selected Projects

**bad — HPC Administration Terminal UI** (Python, curses, PTY, pytest): ~8,500 lines across ~90 modules, with 100+ pytest files including PTY simulation for integration-level testing.

### Home Network / Infrastructure Automation
**Tech:** Linux, WireGuard, iptables, dnsmasq, Pi-hole, step-ca, Docker, Python, Bash

- Built vplan: a device-management toolkit generating Pi-hole DHCP reservations and DNS records idempotently from a single source-of-truth config, with full DNS postcheck validation.
- Built stepfam: a PKI toolkit managing a private ACME CA (step-ca) with inventory-driven cert issuance, SSH-based deployment, trust-chain distribution, and CA rotation, integrated with Caddy for automatic TLS on self-hosted services.

## Certifications / Education

**CompTIA A+** · Awarded 11/2025  
**B.S. Computer Science** · Mississippi State University · 2021
