---
title: "langquiz — Multilingual Vocabulary Quiz"
aliases: ["/projects/language-quiz/"]
status: "Active"
summary: "A self-hosted, installable web app that quizzes vocabulary and sentence comprehension across 20 languages, built from Wiktionary and Tatoeba data with SM-2 spaced repetition. It runs entirely offline from data on disk."
tech: ["Python", "Flask", "SQLite", "Docker", "PWA", "pytest", "PySide6"]
problem: "I wanted a fast, offline way to drill vocabulary across many languages and writing systems, with the pacing of a spaced-repetition app, without subscription platforms or hand-built word lists."
approach: "Per-language loaders stream Wiktionary (kaikki.org) dictionary dumps and Tatoeba sentence pairs into SQLite caches with full-text indexes, built in an explicit, atomic build step. A Flask app generates multiple-choice, fill-in-the-blank, and sentence-comprehension questions, choosing distractors by part of speech, frequency, and IPA similarity, and schedules reviews with SM-2. It runs under gunicorn in Docker on the home LAN behind single sign-on, and installs on a phone as a PWA. The original PySide6 desktop quiz is still in the repo."
current:
  - "20 languages, including Arabic, Chinese, Hebrew, Hindi, Japanese, Korean, Russian, Ukrainian, Urdu, and Vietnamese, with audio playback where the source data has it."
  - "SM-2 spaced repetition with a Review Due mode, daily streaks, and an XP system with a consecutive-correct multiplier."
  - "Question types: multiple choice, Tatoeba fill-in-the-blank with sentence hints, sentence-to-English comprehension, and typed five-word recall."
  - "Correction rounds that bring missed items back before a quiz completes."
  - "Japanese romanization that prefers conventional Hepburn spelling, with click-to-reveal pronunciation."
  - "Multi-user profiles, question flagging with an admin review page, and flagged questions suppressed from generation."
  - "SQLite cache schema with SQL-side filtering and atomic builds; tests isolated from real progress data."
next:
  - "Practice-my-mistakes mode built on the per-word error counts already tracked."
  - "Daily-goal picker for the existing XP goal, and hearts/lives per session."
  - "Matching-pairs and word-ordering question types, which need Japanese tokenization."
repo_status: "Private; self-hosted on the home LAN."
---
