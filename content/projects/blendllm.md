---
title: "blendllm — LLM-Driven Blender Pose Tool"
status: "In development"
summary: "A CLI pipeline that translates natural-language pose and animation descriptions into Blender rig operations via an LLM — distilling a 1000+ bone armature down to what the model needs to know, then applying the result as a versioned JSON patch."
tech: ["Python", "Blender", "Anthropic SDK", "Ollama"]
problem: "Manually posing 3D characters in Blender is slow and requires detailed knowledge of rig structure. I wanted to drive poses and animation keyframes from plain text descriptions, using an LLM as the intermediary."
approach: "The tool snapshots a .blend file's armature state, classifies bones into CONTROL / DEFORM / MECHANISM categories via naming heuristics, and builds a structured prompt from the ~250 control bones the model needs. The LLM returns a versioned JSON patch (blendllm-patch/v0.2) with a defined op vocabulary (set_pose, add_rotation_euler, keyframe, etc.) which is applied back into Blender via bpy in background mode. Optionally renders a multi-angle preview of the current pose and sends it as visual context before generating the patch."
current:
  - "Working end-to-end pipeline: snapshot → classify → prompt → patch → apply."
  - "Supports Anthropic Claude (default: claude-opus-4-5) and any Ollama model (default: llama3.2-vision) via --provider flag or env vars."
  - "Versioned patch format with validation, per-character rig profiles, and lineage tracking across iterations."
  - "Vision-grounded mode: multi-angle render sent to model before patch generation."
  - "Tkinter preview GUI."
next:
  - "Refinement loop: re-render after patch and allow model to self-correct."
  - "Bone classification improvements beyond naming heuristics."
  - "Broader rig support beyond Rigify."
repo_status: "Private; functional but early-stage."
---
