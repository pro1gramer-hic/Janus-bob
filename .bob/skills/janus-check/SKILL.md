---
name: janus-check
description: >-
  Scan a project for config, docs and secret drift, then fix it with parallel
  subagents
metadata:
  user-invocable: true
  disable-model-invocation: true
  argument-hint: '<project path, default example_app>'
---

Use the Janus workflow for a check on the project path given after the command.
If no path is given, use example_app.
Follow the budget and safety rules of the Janus mode strictly.
