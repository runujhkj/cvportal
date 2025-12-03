---
title: "vplan — VPN-LAN Router Architecture"
status: "Long-running systems project"
summary: "A full home-LAN architecture built around a Debian-based VPN router with nftables, Pi-hole, WireGuard/OpenVPN, DHCP reservations, per-device VPN bypassing, and internal service discovery."
tech: ["Debian", "nftables", "WireGuard", "OpenVPN", "Pi-hole", "dnsmasq", "systemd-networkd"]
problem: "I needed a LAN where every device’s traffic path is explicit and controllable: defaulting to NordVPN, allowing per-device bypassing, avoiding DNS leaks, and ensuring remote access from hostile networks — all without using opaque vendor tooling or iptables leftovers."
approach: "A single Debian router (ZimaBoard) runs nftables for NAT/firewalling, Pi-hole for DNS, dnsmasq for DHCP, and scripted components for VPN routing. The design makes traffic flow predictable and observable while allowing scripted toggles for per-device VPN state and clean separation between VPN-LAN and non-VPN-LAN interfaces."
current:
  - "Stable nftables configuration for NAT, forwarding, VPN routing, and LAN segmentation."
  - "Pi-hole and dnsmasq managing LAN DNS + DHCP with static reservations sourced from a plain-text device inventory."
  - "Per-device VPN bypass scripts for MAC/IP, with logging and integration points for future GUI notifications."
  - "Working remote-access model using WireGuard or Meshnet-style tunneling from untrusted networks back into the LAN."
next:
  - "Dashboard (`tunstat.home.arpa`) for VPN service state and fallback routing behavior."
  - "Automated detection of upstream failures and failover between NordVPN, WireGuard/OpenVPN, and no-VPN modes."
  - "Full rewrite of legacy iptables logic into nftables with clearer, human-readable rule visualization tools."
repo_status: "Internal only; no public repo planned."
---
