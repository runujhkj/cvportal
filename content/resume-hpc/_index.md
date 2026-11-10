---
title: "Resume (HPC Systems)"
---

# Jeffrey "Jack" Hannon Jr.

HPC Hardware and Systems Technician

{{% contact "location,phone,email,website" %}}

## Summary

Hardware and systems technician at Mississippi State University's HPC Center since 2022. I keep the compute nodes on four Slurm clusters running, which mostly means finding the failed part, replacing it, and getting Dell to send the right replacement. I also wrote the Python tool I use for every repair.

## Experience

### Computer Specialist I, HPC Center *2022–Present* {.job}

Mississippi State University, Starkville, MS

- Diagnose and repair 10–20 failed nodes a month across four Slurm clusters (96 to 1,800 nodes) used by about 5,000 researchers and staff.
- Swap memory, CPUs and drives between nodes to find the bad part, then replace whatever failed, from a single DIMM up to a system board or a whole chassis. Every node gets a recorded failure cause and dated notes.
- Run Dell support cases start to finish, including the long ones where the first replacement doesn't fix it or arrives dead.
- Track down InfiniBand link flaps by swapping DAC cables, HCAs and switch ports.
- Update firmware through OpenManage Enterprise when a node falls behind baseline, and run a regression test before it goes back into service. Compare BIOS settings against a known-good node when something looks off.
- Bring nodes back after cooling and power failures, and restart LNet when a node drops its Lustre mounts.
- Wrote `bad`, a Python terminal tool I use for every repair. It pulls Slurm drain state, NHC results, iDRAC logs and InfiniBand checks into one place, keeps per-node notes, and generates the monthly unplanned-outage report. Coworkers get its output when they're tracing a failure.

### Research Computing Administrator (Contract) *2023–2024* {.job}

Fox Chase Cancer Center, remote

- Set up and maintained about 40 bioinformatics packages for a genomics research group, mostly with Spack and by hand where Spack couldn't build something.
- Worked directly with the lead researcher, wrote down how every build was done, and kept older versions around for workflows that still needed them.

## Skills

**HPC and hardware:** Slurm, Lustre clients, NHC, Dell PowerEdge, iDRAC/RACADM, OpenManage Enterprise, InfiniBand cabling, BIOS and firmware  
**Linux:** Rocky, Debian, Ubuntu  
**Scripting:** Python, Bash, Ansible, Git, pytest, ReFrame  
**Home lab:** DNS/DHCP, iptables, WireGuard, step-ca, Docker, QEMU/KVM

## Projects

### Home network *Personal* {.job}

- vplan manages my home network's DNS and DHCP from one config file, along with WireGuard remote access and single sign-on.
- stepfam runs a private certificate authority (step-ca) that issues and deploys TLS certificates to my self-hosted services.

## Education

**B.S. Computer Science**, Mississippi State University, 2021  
**CompTIA A+**, 2025
