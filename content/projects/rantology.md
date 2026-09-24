---
title: "Rantology — Live Avatar and Captions Pipeline"
status: "In development"
summary: "A live pipeline that captures mic and desktop audio, transcribes it on the GPU with the what service, drives a Blender character's mouth from the transcript, and hands OBS a single delayed audio/video program where voice, mouth, and captions line up."
tech: ["Python", "PySide6", "Blender", "OBS", "obs-websocket", "PulseAudio", "pytest"]
problem: "I wanted to stream and record spoken thoughts through an animated avatar instead of my face. Live captions and lip-sync can't show a word until it has been transcribed, so they always run a couple of seconds behind the audio. Anything not deliberately delayed arrives early and falls out of sync."
approach: "One command launches and supervises the whole pipeline: the what transcription service and client, a hidden Blender instance, overlay HTTP servers, a local control endpoint, and Rantbank, a PySide6 GUI where every setting can be changed while the pipeline runs. Mouth shapes are driven from the what transcript rather than a second local Whisper model. Everything reaches OBS at the same delayed program stage: mic, desktop audio, and soundboard clips go through one shared delay, and while Rantbank runs, OBS's own real-time sources get matching render-delay filters and audio sync offsets, which are removed when it exits."
current:
  - "Single-command launch that starts, supervises, and cleans up every child process on exit."
  - "Rantbank GUI with tabs for the soundboard, audio devices, scene, captions, Blender viewport preview, multi-platform chat, and remote ASR nodes."
  - "Delayed broadcast-audio passthrough with a live delay control and a Measure tool that times how far captions trail speech."
  - "Independent mic and desktop-audio caption streams, each with its own recording and a clickable transcript: Ctrl+click a word to replay from it and save corrections."
  - "OBS integration via obs-websocket: automatic source delays, a shared-memory camera feed, styled text-box overlays, and reflow-on-resize, including on the Aitum vertical canvas."
  - "Loop-test mode that animates the avatar from a canned clip to check the visual half without a microphone."
  - "pytest suite (125 passing) pinned to the project's own tests."
next:
  - "Validate the program-audio path against real OBS recordings: delay calibration, lane separation, and lifecycle cleanup."
  - "A common presentation clock linking viseme release to program audio, if recordings show a variable rather than fixed offset."
  - "Restore the full g2p phonemizer (currently falling back to a cruder grapheme speller) and resume macOS support."
repo_status: "Private; runs end to end on Linux, with OBS recording acceptance still pending."
---
