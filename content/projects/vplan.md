---
title: "vplan — Home LAN Router, Remote Access and SSO"
status: "Active"
featured: true
summary: "A self-hosted home network built around a Debian VPN router: NordVPN by default with per-device bypass, a WireGuard road-warrior server, Pi-hole DNS/DHCP driven from a device inventory, a private CA, single sign-on across LAN services, browser remote desktop, and a verified photo-backup pipeline."
tech: ["Debian", "iptables", "WireGuard", "NordVPN", "Pi-hole", "dnsmasq", "Caddy", "Authelia", "OIDC", "Docker", "Ansible", "Bash", "Python"]
problem: "I wanted a LAN where every device's traffic path is explicit and controllable: VPN by default, selective bypass, no DNS leaks, and safe remote access from untrusted networks. Its services also needed real TLS and a single login rather than a separate password per app, and my photo library needed somewhere to live that I could prove was a complete copy."
approach: "A dual-NIC Debian router runs iptables NAT and mangle rules with policy routing to send traffic through NordVPN by default. Per-device bypass is driven from a single devices.conf, and a guard timer reapplies the rules after the VPN reconnects. Pi-hole and dnsmasq serve DNS and DHCP reservations generated from the same inventory. Caddy terminates TLS using certificates from the stepfam private CA, and Authelia provides forward-auth and OIDC so self-hosted services share one sign-on. A root snapshot job collects privileged state for an unprivileged web portal. Changes are tracked in the repo alongside a runbook and a topology document."
current:
  - "Per-device VPN bypass from one source of truth, with a guard timer that reapplies rules after NordVPN reconnects."
  - "WireGuard road-warrior server: peer tooling, friend-scoped peers restricted to listed host:port targets, split DNS, MSS clamping, a DDNS auto-updater, and a client watchdog that recovers a stalled tunnel, and an all-day handshake trace with a correlation tool that explains each stall."
  - "Web portal showing ISP vs VPN upstream health, speed samples, VPN server location, bypass state, tunnel reliability, and config sync drift, plus a DHCP device-enrollment page and a one-tab workspace that keeps the self-hosted apps open side by side."
  - "Authelia single sign-on: forward-auth gates on LAN services, with OIDC as the preferred pattern for Forgejo, OpenWebUI, Guacamole, and Immich."
  - "Browser remote desktop through Apache Guacamole 1.6 with Postgres-backed connections, a small extension for edge panning and touch scrolling, and an Ansible role that provisions remote-desktop targets."
  - "Photo offload pipeline: staged export from phones and a Mac library into two independent stores, verified by content hash (21,486 of 21,551 items confirmed in the first full run), with a ledger, a filtered view served to Immich (which replaced an earlier Piwigo gallery), and hourly replication of new uploads checked against Immich's own checksums."
  - "One-step device onboarding that pushes the private CA's trust and DNS settings, and a completed migration of the internal domain across DNS, Caddy, the CA, and client tooling."
  - "Backups: a self-hosted Kopia server behind single sign-on, a Linux client installer with nightly snapshots, and Time Machine for Macs on the home network."
  - "Configuration as code: domain names, host addresses, NAS mounts, and Pi-hole settings come from one site file instead of being hardcoded or written up as runbook steps."
  - "A hardware watchdog on the gateway, added after its init process froze for four days, and proxies that retry refused connections while a service restarts."
next:
  - "Per-user remote-desktop connections in Guacamole."
  - "Finish the release preparation: the remaining hardcoded values moved into the site file, an allowlist of what can be published, and a fictitious network map to stand in for the real one."
  - "Automated failover between NordVPN, WireGuard, and no-VPN modes when an upstream fails."
repo_status: "Private; in daily use as the home network's control plane."
---
