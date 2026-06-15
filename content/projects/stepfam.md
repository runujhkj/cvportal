---
title: "stepfam — Private PKI Toolkit"
status: "Active"
summary: "A two-part shell toolkit for running and operating a private ACME/mTLS certificate authority on a home LAN — stepmom manages the CA host, stepchild handles cert issuance, deployment, and renewal from any machine."
tech: ["bash", "step-ca", "Docker", "ACME", "mTLS", "nftables", "Caddy", "Python"]
problem: "Self-hosting services with real TLS — without browser warnings, without exposing anything to the public internet, and without letting the CA provisioner password travel outside the CA host — requires a private PKI that is easy to bootstrap, operate, and rotate. Most DIY PKI setups are brittle one-time setups with no clean teardown or renewal story."
approach: "Two halves with a clean split: stepmom runs on the CA host and manages the step-ca Docker container, CA initialization (JWK + ACME provisioners), a stable CA IP via a NetworkManager secondary /32 address, nftables firewall rules, and a symlink-based install so edits take effect immediately. stepchild runs anywhere, drives cert issuance via a Docker stepper container, maintains an inventory.json as single source of truth for what certs exist and where they go, and handles SSH-based deployment and trust-chain distribution. ACME renewal feeds Caddy; mTLS renewal handles everything else. CA rotation is a single stepmom rootate command."
current:
  - "stepmom: CA container lifecycle, JWK + ACME provisioner init, stable LAN IP, nftables rules, repo-symlink install."
  - "stepchild: inventory-driven leaf cert issuance, SSH-based deployment, trust-chain distribution to LAN hosts."
  - "ACME renewal path for Caddy; mTLS renewal for internal services — provisioner password never leaves the CA host."
  - "Bootstrap sequence respects CA → DNS → TLS dependency ordering."
  - "Idempotent Makefile-driven install with pre-flight guards and environment templating."
  - "CA state lives in the repo (gitignored); full teardown is rm -rf."
next:
  - "Automated cert expiry monitoring with alerting."
  - "Inventory diff tooling for auditing deployed vs. expected certs."
repo_status: "Private; git submodule of home network monorepo."
---
