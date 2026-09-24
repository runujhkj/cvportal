---
title: "vplan — Home LAN Router, Remote Access and SSO"
status: "Active"
featured: true
summary: "A self-hosted home network built around a Debian VPN router: NordVPN by default with per-device bypass, a WireGuard road-warrior server, Pi-hole DNS/DHCP driven from a device inventory, a private CA, single sign-on across LAN services, and a web portal that shows what the network is actually doing."
tech: ["Debian", "iptables", "WireGuard", "NordVPN", "Pi-hole", "dnsmasq", "Caddy", "Authelia", "OIDC", "Docker", "Bash", "Python"]
problem: "I wanted a LAN where every device's traffic path is explicit and controllable: VPN by default, selective bypass, no DNS leaks, and safe remote access from untrusted networks. Its services also needed real TLS and a single login rather than a separate password per app, all without opaque vendor tooling."
approach: "A dual-NIC Debian router runs iptables NAT and mangle rules with policy routing to send traffic through NordVPN by default. Per-device bypass is driven from a single devices.conf, and a guard timer reapplies the rules after the VPN reconnects. Pi-hole and dnsmasq serve DNS and DHCP reservations generated from the same inventory. Caddy terminates TLS using certificates from the stepfam private CA, and Authelia provides forward-auth and OIDC so self-hosted services share one sign-on. A root snapshot job collects privileged state for an unprivileged web portal."
current:
  - "Per-device VPN bypass from one source of truth, with a guard timer that reapplies rules after NordVPN reconnects."
  - "WireGuard road-warrior server: peer tooling, friend-scoped peers restricted to listed host:port targets, split DNS by default, MSS clamping, and a DDNS auto-updater."
  - "Web portal showing ISP vs VPN upstream health, hourly and on-demand speed samples, VPN server location, bypass state, and config sync drift, plus a DHCP device-enrollment page."
  - "Authelia single sign-on: forward-auth gates on LAN services and OIDC clients for Forgejo, OpenWebUI, and Piwigo."
  - "One-step device onboarding: push the private CA's trust and the Pi-hole DNS settings to a new device."
  - "Browser-based remote desktop via Postgres-backed Apache Guacamole, plus scripted provisioning of remote-desktop target machines."
  - "Staged migration of the internal domain from .home to home.vplan, completed across DNS, Caddy, the CA's ACME endpoint, and client tooling."
next:
  - "Resolve an intermittent WireGuard tunnel stall, traced to handshake responses lost on the ISP router's return path."
  - "Photo hosting: a Piwigo transfer workflow that preserves Live Photo pairs, verifies originals, and only then allows source cleanup."
  - "Automated failover between NordVPN, WireGuard, and no-VPN modes when an upstream fails."
repo_status: "Private; in daily use as the home network's control plane."
---
