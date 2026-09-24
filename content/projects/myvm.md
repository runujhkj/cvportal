---
title: "myvm — Lightweight macOS VM Launcher"
status: "In development"
featured: true
summary: "A PySide6 GUI and CLI for running QEMU virtual machines on Apple Silicon from YAML profiles, with cloud-init provisioning, bridged networking, serial boot logs, and a check that decides whether a VM is fit to be the golden image dev VMs are cloned from."
tech: ["Python", "PySide6", "QEMU", "QMP", "cloud-init", "macOS", "pytest"]
problem: "I needed a quick, reproducible way to launch and provision VMs on a Mac without maintaining dozens of shell scripts, and a way to trust a base image before cloning development VMs from it."
approach: "VM profiles live in YAML. myvm creates disks, assembles the QEMU command (HVF-accelerated on Apple Silicon), captures logs, and drives the guest over QMP. Cloud-init seed ISOs provision a guest on first boot, and socket_vmnet provides bridged networking for Linux guests. A separate bless command SSHes into a running VM and checks it against a golden-image standard, recording the guest's package manifest for each run. macOS guests can run through macosvm (Virtualization.framework) instead of QEMU."
current:
  - "GUI launcher plus command-line profile editing, VM lifecycle, and disk operations."
  - "Cloud-init NoCloud seed generation for first-boot provisioning."
  - "Bridged networking for Linux guests via socket_vmnet, alongside user-mode networking with SSH forwarding."
  - "Serial console logging of guest boots for diagnostics."
  - "bless: checks whether a running VM is fit to be a golden dev image, recording the package manifest for each network mode."
  - "Experimental macOS guest presets using macosvm."
next:
  - "Build the clone-from-golden-image workflow on top of bless."
  - "Snapshot workflows and a profile-editing UI."
repo_status: "Private; actively developed."
---
