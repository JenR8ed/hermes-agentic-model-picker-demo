---
title: Hermes Agentic Model Picker Demo
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---

# Hermes — Agentic Model Picker Demo

A compact experiment in **model routing**: an agentic decision layer selects an appropriate model/tool path for a task instead of hard-coding one model.

## Current state

**Demo / research prototype.**

The repository is intentionally small. It exists to make the routing concept concrete in a lightweight Gradio interface.

## Pattern

```
Task
  |
  v
Routing decision
  |
  +-- model/tool A
  +-- model/tool B
  +-- fallback / human path
  |
  v
Result
```

Hermes explores making model selection an explicit engineering decision that can eventually be evaluated rather than hidden inside application code.

## Stack

Python · Gradio · agentic routing logic

## Related work

- [AI-List-Assist](https://github.com/JenR8ed/AI-List-Assist) — applied multimodal AI workflow
- [jaios-agentic-core](https://github.com/JenR8ed/jaios-agentic-core) — agentic system architecture
- [AI-Agentic-Terminal-Portfolio](https://github.com/JenR8ed/AI-Agentic-Terminal-Portfolio) — AI engineering portfolio