---
title: "vplan — Home LAN Router, Remote Access and SSO"
status: "Active"
featured: true
summary: "A self-hosted home network and service platform built around a Debian VPN router: NordVPN by default with per-device and per-service bypass, WireGuard remote access with scoped peers, Pi-hole DNS/DHCP driven from a device inventory, a private CA, single sign-on across every site, monitoring with phone alerts, browser remote desktop, and verified backups."
tech: ["Debian", "iptables", "WireGuard", "NordVPN", "Pi-hole", "dnsmasq", "Caddy", "Authelia", "OIDC", "Docker", "Ansible", "Windows/WSL2", "Prometheus", "Grafana", "Kopia", "Go", "Bash", "Python"]
problem: "I wanted a LAN where every device's traffic path is explicit and controllable: VPN by default, selective bypass, no DNS leaks, and safe remote access from untrusted networks. Its services also needed real TLS and a single login rather than a separate password per app, and my photo library needed somewhere to live that I could prove was a complete copy."
approach: "A dual-NIC Debian router runs iptables NAT and mangle rules with policy routing to send traffic through NordVPN by default. Per-device bypass is driven from a single devices.conf, and a guard timer reapplies the rules after the VPN reconnects. Pi-hole and dnsmasq serve DNS and DHCP reservations generated from the same inventory. Services run on a Windows 11 host under WSL2 and Docker, set up with Ansible. Caddy terminates TLS using certificates from the private CA (formerly the separate stepfam project), and Authelia gates every site and provides OIDC so self-hosted services share one sign-on. Settings come from one site file, and a deploy script applies only what changed on each machine. A root snapshot job collects privileged state for an unprivileged web portal. Changes are tracked in the repo alongside a runbook and a topology document."
current:
  - "Per-device VPN bypass from one source of truth, with a guard timer that reapplies rules after NordVPN reconnects, plus named services that skip the VPN for every device."
  - "WireGuard remote access with three peer scopes (admin, web-only, and named host:port pairs), end dates, and a default-deny firewall toward the home network; split DNS, MSS clamping, and a DDNS updater."
  - "A recurring tunnel stall traced to handshake replies lost on the way back; client guards now change port when a key renewal goes unanswered. In the week of Nov 9–13 the tunnel was available 99.5% of the time, and watchdog restarts fell from about 3 an hour to under 0.5."
  - "Prometheus, Grafana, and Alertmanager with probes of every site and app, alerts to phones, and a status screen."
  - "Services moved to a new host one at a time, each with about a minute of downtime and a rollback kept."
  - "Web portal showing ISP vs VPN upstream health, speed samples, VPN server location, bypass state, tunnel reliability, and config sync drift, plus a DHCP device-enrollment page and a one-tab workspace that keeps the self-hosted apps open side by side."
  - "Authelia single sign-on: every site is gated, with OIDC for Forgejo, OpenWebUI, Guacamole, Immich, and Grafana, and password logins turned off where OIDC covers them."
  - "Browser remote desktop through Apache Guacamole 1.6 with per-user connections, a small extension for edge panning and two-finger scroll and zoom, and an Ansible role that provisions remote-desktop targets."
  - "Photo offload pipeline: staged export from phones and a Mac library into two independent stores, verified by content hash in both copies (20,772 of 21,047 items in the latest run), with a ledger, a filtered view served to Immich (which replaced an earlier Piwigo gallery), and hourly replication of new uploads checked against Immich's own checksums."
  - "One-step device onboarding that pushes the private CA's trust and DNS settings, and a completed migration of the internal domain across DNS, Caddy, the CA, and client tooling."
  - "Backups: a self-hosted Kopia server behind single sign-on, nightly snapshots with per-machine database dumps and staleness alerts, imported older history spot-checked 181 of 181, and Time Machine for Macs at home or over the tunnel."
  - "Configuration as code: domain names, host addresses, NAS mounts, and Pi-hole settings come from one site file instead of being hardcoded or written up as runbook steps."
  - "A hardware watchdog on the gateway, added after its init process froze for four days, and proxies that retry refused connections while a service restarts."
next:
  - "Publish the public snapshot: a script already rebuilds the repository with every real name swapped for a fictional network, and refuses to finish if one remains."
  - "An off-site copy of the photo library in cold cloud storage, defined in Terraform, after de-duplicating it."
  - "Machine secrets in Ansible Vault, and SSH certificates from the private CA."
repo_status: "Private; in daily use as the home network's control plane."
---

### Tunnel reliability

{{< tunnel-chart >}}Weekly figures (weeks with at least 10 hours on the tunnel) from the client watchdog, which checks the tunnel every 10 seconds while a Mac is away from home and restarts it when it stalls. Hover over a bar for that week's hours and availability. Before an ISP router change in early October, it was restarting the tunnel about 11 times an hour.{{< /tunnel-chart >}}
