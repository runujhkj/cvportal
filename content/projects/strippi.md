---
title: "strippi — Token and Phrase Redaction Tool"
status: "Prototype"
summary: "A Rust CLI for detecting and hashing sensitive phrases in text streams using a custom pattern database."
tech: ["Rust", "Regex", "CLI"]
problem: "I needed a way to remove personally identifiable phrases from logs or shared text without losing debuggability."
approach: "A small CLI that loads pattern rules from JSON, scans input streams, hashes matched phrases, and re-emits text with redactions."
current:
  - "Phrase and token DB in JSON."
  - "Candidate detection with regex + heuristics."
  - "Configurable redaction modes."
next:
  - "Parallel scanning."
  - "Interactive phrase DB editing."
  - "Improved tokenization for mixed-language text."
repo_status: "Private; functional prototype."
---
