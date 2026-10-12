---
title: "simptemp — Terminal Temperature and Load Graph"
status: "Active"
summary: "A small Rust terminal tool that graphs CPU and GPU temperature alongside CPU, GPU, and RAM utilization for the last 30 seconds. I keep it open while running GPU-heavy local model tests."
tech: ["Rust", "NVML", "Linux"]
problem: "While testing local models I wanted one glanceable view of whether the GPU or the CPU was the part working, and how hot each was running, without a full monitoring stack."
approach: "A single binary samples once a second and draws a live graph sized to the terminal. CPU temperature comes from the k10temp hwmon sensor on AMD, GPU metrics from NVML on NVIDIA, and the rest from the sysinfo crate. A sensor that cannot be read is shown as an error instead of a made-up value."
current:
  - "Live graph of CPU/GPU temperature and CPU/GPU/RAM utilization, with a configurable window and sampling interval."
  - "A --once mode that prints a single snapshot and exits, for scripts."
repo_status: "Private; about 300 lines of Rust, used daily."
---
