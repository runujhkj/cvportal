---
title: "langquiz — Offline Language Learning App"
aliases: ["/projects/language-quiz/"]
status: "Active"
summary: "A free, offline language-learning app covering 20 languages: picture-led beginner courses, vocabulary and sentence quizzes built from Wiktionary and Tatoeba data, and SM-2 spaced repetition. It runs as a self-hosted web app and is packaged for iOS and Android from the same source."
tech: ["Python", "Flask", "JavaScript", "SQLite", "Docker", "PWA", "iOS", "Android", "pytest"]
problem: "I wanted to drill several languages and writing systems with the pacing of a spaced-repetition app, without subscriptions, accounts, or a network connection, and with a beginner path that teaches through pictures and sentences instead of dictionary glosses."
approach: "Per-language loaders stream Wiktionary (kaikki.org) dictionary dumps and Tatoeba sentence pairs into SQLite caches with full-text indexes, built in an explicit, atomic step. A Flask app generates questions, picks distractors by part of speech, frequency, and IPA similarity, and schedules reviews with SM-2. The mobile build packages the existing web source with a second, offline quiz engine in JavaScript; shared regression contracts run in CI on both engines so grading, course selection, and test-out behave the same on the server and on a phone. Learning state is saved atomically and travels between devices as a validated, portable backup."
current:
  - "20 languages, including Arabic, Chinese, Hebrew, Hindi, Japanese, Korean, Russian, Ukrainian, Urdu, and Vietnamese, with audio where the source data has it."
  - "Beginner courses that open with pictures and sentence building, authored practical lessons, phrase guides, and a test-out that restarts after three mistakes."
  - "Question types: multiple choice, fill-in-the-blank from real sentences, sentence comprehension, and typed recall that forgives one typo or missing word."
  - "SM-2 spaced repetition with a Review Due mode, missed-word practice, lesson summaries with review guidance, daily streaks, and XP."
  - "iOS and Android packaging from the web source, with offline quiz sessions that persist and recover."
  - "Portable backups covering progress, preferences, and answer history, validated before import; per-profile timezones so days roll over locally."
  - "Content quality tools: question flagging with a review page, a daily pruning queue, personal accepted translations, and course-pack validation."
  - "Cross-platform CI running the same regression contracts against the Python and offline engines."
next:
  - "More authored beginner units beyond the first Spanish lessons."
  - "Matching-pairs and word-ordering question types, which need Japanese tokenization."
  - "Replacing emoji stand-ins in picture lessons with real artwork."
repo_status: "Private; self-hosted on the home LAN."
---
