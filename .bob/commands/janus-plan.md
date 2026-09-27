---
description: Before a change, list what it will touch and write a change contract
argument-hint: <description of the change you want to make>
---
The user describes a change they want to make to example_app.
1. Run: python -m janus check example_app, and read example_app/.janus/report.json.
2. Using grep only (no full file reads), find the functions, routes, environment
   variables and README sections the change will touch, and their call sites.
3. Write example_app/.janus/contract.md with: files to change, call sites affected,
   tests to add or update, config keys to add, README lines to update, security risks.
4. Show the contract and ask the user to confirm before changing any code.
