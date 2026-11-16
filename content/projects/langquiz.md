---
title: "langquiz — Offline Language Learning App"
aliases: ["/projects/language-quiz/"]
status: "Active"
summary: "A free, offline language-learning app covering 20 languages: picture-led beginner courses, alphabet and character lessons for ten writing systems, vocabulary and sentence quizzes built from Wiktionary, CC-CEDICT, JMdict, and Tatoeba data, and SM-2 spaced repetition. It runs as a self-hosted web app and is packaged for iOS and Android from the same source."
tech: ["Python", "Flask", "JavaScript", "SQLite", "Docker", "PWA", "iOS", "Android", "pytest"]
problem: "I wanted to drill several languages and writing systems with the pacing of a spaced-repetition app, without subscriptions, accounts, or a network connection, and with a beginner path that teaches through pictures and sentences instead of dictionary glosses."
approach: "Per-language loaders stream Wiktionary (kaikki.org) dictionary dumps and Tatoeba sentence pairs into SQLite caches with full-text indexes, built in an explicit, atomic step. A Flask app generates questions, picks distractors by part of speech, frequency, and IPA similarity, and schedules reviews with SM-2. The mobile build packages the existing web source with a second, offline quiz engine in JavaScript; shared regression contracts run in CI on both engines so grading, course selection, and test-out behave the same on the server and on a phone. Learning state is saved atomically and travels between devices as a validated, portable backup."
current:
  - "20 languages, including Arabic, Chinese, Hebrew, Hindi, Japanese, Korean, Russian, Ukrainian, Urdu, and Vietnamese. Lesson words in 18 of them, and the letters of every taught script, play from about 31,000 pre-recorded clips made with local system voices."
  - "Every course opens with 17 picture lessons; Spanish continues with 15 A1 units. Courses run a unit at a time, with a unit test-out and lessons marked perfect, skipped, or mastered, and mastery has to be shown again after 30 days."
  - "Alphabet, kana, and Hangul lessons a few letters at a time, plus a Characters view showing which letters or characters a learner has mastered (for Japanese, the 741 kanji its vocabulary uses)."
  - "Question types: multiple choice, fill-in-the-blank from real sentences, letter sounds, word matching, sentence building from a word bank, and typed recall that forgives one typo or missing word."
  - "Data clean-up: Japanese vocabulary from JMdict's common words, about 215 meanings in the first lessons corrected by hand, and wrong answers drawn from the 2,500 most common words."
  - "SM-2 spaced repetition with a Review Due mode, missed-word practice, lesson summaries with review guidance, daily streaks, and XP."
  - "iOS and Android packaging from the web source, with offline quiz sessions that persist and recover."
  - "Portable backups covering progress, preferences, and answer history, validated before import; per-profile timezones so days roll over locally."
  - "Content quality tools: question flagging with a review page, a daily pruning queue, personal accepted translations, and course-pack validation."
  - "Cross-platform CI running the same regression contracts against the Python and offline engines: 957 Python tests and about 180 JavaScript tests."
next:
  - "A1 units for languages beyond Spanish."
  - "Testing offline use on real devices."
  - "Replacing emoji stand-ins in picture lessons with real artwork."
repo_status: "Private; self-hosted on the home LAN."
---
