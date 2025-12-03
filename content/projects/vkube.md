---
title: "vkube — Local Kubernetes Lab"
status: "In active development"
summary: "A scripted local Kubernetes environment using QEMU and Ansible, tuned for repeatable HPC-style experiments."
tech: ["QEMU", "Kubernetes", "Ansible", "Linux"]
problem: "I need a reproducible lab where I can spin up and tear down multi-node Kubernetes clusters that resemble real HPC/network constraints, without depending on cloud credits or external services."
approach: "Shell scripts and Ansible roles that provision QEMU VMs, configure networking, and bring up a K8s control plane and workers using consistent CIDR ranges and DNS. The goal is `vkube-up` to create a full lab and `vkube-down` to tear it all back to a clean state."
current:
  - "Base VM images and QEMU invocation scripts for multi-node setups."
  - "Ansible roles that configure OS, networking, and basic K8s prerequisites."
  - "Configuration variables for domains, pod CIDRs, and storage paths."
next:
  - "Full end-to-end `vkube-up` / `vkube-down` pipeline."
  - "Automated TLS / CA integration for internal services."
  - "Documentation for running vkube on both Linux and macOS hosts."
repo_status: "Under construction; not public yet."
---
