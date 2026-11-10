---
title: "Resume (HPC Systems)"
---

# Jeffrey "Jack" Hannon Jr.

HPC Systems & Hardware · Slurm · Dell PowerEdge · InfiniBand · Python

{{% contact "location,phone,email,website" %}}

## Summary

HPC systems technician at Mississippi State University's HPC Center since 2022, keeping the compute nodes of four Slurm clusters (96 to 1,800 nodes, about 5,000 users) in service. Takes each failed node from report back to production: isolates the fault, replaces the part, works the Dell case to closure, and brings firmware up to baseline. Built the Python tool used for every repair.

## Skills

**HPC & Hardware:** Slurm, Lustre clients (LNet), NHC, Dell PowerEdge, iDRAC/RACADM, OpenManage Enterprise, BIOS/firmware baselines, InfiniBand cabling (HCAs, DAC, switch ports), Dell support cases and TSR logs, Linux (Rocky, Debian, Ubuntu)  
**Automation:** Python, Bash, Ansible, Git, pytest, ReFrame  
**Networking:** DNS/DHCP (dnsmasq, Pi-hole), iptables, WireGuard, policy routing, PKI/TLS (step-ca, ACME, mTLS)  
**Other:** QEMU/KVM, Docker, cloud-init

## Experience

### Computer Specialist I — HPC Center · *Mississippi State University · 2022–Present*

- Repair 10–20 hardware failures a month across four clusters: isolate the fault by moving DIMMs, CPUs and drives between nodes, then replace memory, CPUs, system boards, boot SSDs or full chassis internals and return the node to the compute pool, with its failure cause and dated notes on record.
- Open and close Dell support cases: collect TSR logs, ship failed parts back, and carry cases through repeat failures and dead-on-arrival replacements.
- Trace InfiniBand link flaps to the physical layer by swapping DAC cables, HCAs and switch ports.
- Bring nodes that fall behind the firmware baseline up to date through OpenManage Enterprise, then run a regression test before returning them to service; diff BIOS settings against a known-good node.
- Recover nodes after facility events such as a cooling-unit failure and chassis power faults, using power drains and sled-by-sled testing; restart Lustre LNet on nodes that drop off the filesystem.
- Built `bad`, a Python terminal tool (~20,400 lines, 69 test files) that runs each step of a repair in one session: Slurm drain state, NHC, iDRAC event logs and reboots, InfiniBand fabric checks, and per-node repair notes. It also generates the monthly unplanned-outage reports (incidents, node-minutes down, which outages were worked); its output goes to coworkers for failure tracing.

### Research Computing Administrator (Contract) · *Remote · 2023–2024*

- Sole administrator of the software environment for a genomics research group at Fox Chase Cancer Center, working directly with the lead researcher.
- Built and kept current a ~40-package bioinformatics stack with Spack, plus source builds where Spack fell short; documented every build so the environment could be rebuilt, and kept legacy versions for existing workflows.

## Selected Projects

### Home Network / Infrastructure Automation · *Linux, WireGuard, iptables, Pi-hole, step-ca, Docker*

- Built vplan: a device-management toolkit generating Pi-hole DHCP reservations and DNS records idempotently from a single source-of-truth config, with full DNS postcheck validation.
- Built stepfam: a PKI toolkit managing a private ACME CA (step-ca) with inventory-driven cert issuance, SSH-based deployment, trust-chain distribution, and CA rotation, integrated with Caddy for automatic TLS on self-hosted services.

## Education / Certifications

**B.S. Computer Science**, Mississippi State University, 2021 · **CompTIA A+**, 2025
