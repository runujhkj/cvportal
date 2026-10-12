---
title: "mutter — Mumble Client for iOS"
built_by: "locallm"
status: "Prototype"
summary: "A deliberately simple iOS Mumble client for text chat and two-way voice, written by a local language model through the locallm build pipeline and held to acceptance tests that run against a real Mumble server."
tech: ["Swift", "SwiftUI", "AVAudioEngine", "Opus", "Protocol Buffers", "XCTest"]
problem: "I wanted an as-simple-as-possible iOS app that connects to reachable Mumble servers, particularly ones on my own network. It was also the test case for a harder question: can a small local model build a working networked app, not just code that compiles?"
approach: "I wrote the request and the spec; the code was written by a local model running on my own GPU, one unit at a time, with a Mac building and testing each change. The spec is a contract of units, and the tests hold the app to what a real server shows: a throwaway Murmur server runs in Docker for each check, and a second client connected to it reports whether the app's user is really listed and whether its messages really arrived. Nothing about the server can be faked inside the app. Later passes with other coding agents added voice and reworked the interface."
current:
  - "Connect over TLS, see channels and users, join a channel, and send and receive text."
  - "Two-way voice: mono 48 kHz Opus in 10 ms frames over the TLS tunnel, with each speaker decoded independently and played through AVAudioEngine."
  - "Microphone capture stops on disconnect, backgrounding, and audio interruptions; permission and audio errors are shown, not swallowed."
  - "About 4,900 lines of Swift with 28 test files, including UI tests against the live fixture server."
  - "One consolidated history that keeps seven earlier build attempts as archived refs."
next:
  - "Voice testing on real hardware beyond the simulator."
  - "Another interface pass against the iOS Human Interface Guidelines."
repo_status: "Private. Commit history records which commits were authored by the locallm pipeline and which by me."
---
