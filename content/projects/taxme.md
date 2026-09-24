---
title: "Taxme — Tax-Prep Training Game"
status: "Prototype"
summary: "A game-like training app for entry-level U.S. tax preparers, aimed at decision accuracy and long-term retention: short case missions with immediate feedback, fix cards generated from mistakes, and confidence-weighted scoring."
tech: ["TypeScript", "React", "Vite", "Node.js", "Docker"]
problem: "Newer tax preparers (1–3 years in) need rule recall, speed, and confidence, but most training material is reading, not practice. I wanted short, repeatable drills that feel like a game while keeping the explanations professionally accurate."
approach: "A React and Vite web UI served by a small Node server. Each mission is a case dossier with a handful of discrete decisions, each scored immediately and weighted by the confidence the player reports: overconfident wrong answers count against unlocking the next tier. Errors spawn fix cards for later review. Content is JSON-defined so missions can grow into versioned, per-tax-year content packs. Pushes to Forgejo deploy the app automatically through a runner and a webhook."
current:
  - "Case Simulator loop: mission brief → decisions → immediate feedback → fix cards."
  - "One sample mission, with confidence-based scoring and speed recorded alongside."
  - "Weather mood system (auto-rotating every 30 minutes, or fixed)."
  - "Design brief and v0.1 spec: Career mode with tiered missions and unlock gates, plus an Endless mode."
  - "Forgejo Actions workflow and webhook deploy, with the build's version and commit ID shown on the site."
next:
  - "Implement the v0.1 spec: tiered Career missions, unlock rules, and Endless mode."
  - "Fix-card spaced-repetition queue and the rule-card library."
  - "Mission content built from public IRS materials for the latest tax year."
repo_status: "Private; early prototype, self-hosted on the home LAN."
---
