# CONTEXT.md — Architecture Reference

## Project Overview
Personal Jarvis-style CLI assistant for a single user on Windows 11. Chat agent
with a fixed persona that answers questions, runs local shell commands, reads
and writes files, searches the web, and remembers user facts across sessions.
Runs entirely on the user's Claude Pro subscription via Claude Code login —
no API key, no pay-per-use billing.

## Tech Stack
Runtime:           Python 3.12.10 (Windows 11)
Framework:         claude-agent-sdk 0.2.145 (drives Claude Code 2.1.201)
Database:          None — filesystem memory (memory/facts.md)
External Services: None beyond Claude subscription; web via SDK WebSearch/WebFetch
Deployment:        Local machine, launched from terminal

## Core Modules

**jarvis/persona.py**
- Purpose: JARVIS identity and system prompt text.
- Depends on: nothing.
- Danger zones: single source of persona truth — edits change agent character.

**jarvis/memory.py**
- Purpose: load memory/facts.md into system prompt; append new facts.
- Depends on: filesystem only.
- Danger zones: memory file holds personal user data; never delete blindly.

**jarvis/main.py**
- Purpose: CLI loop; persistent ClaudeSDKClient session; streams replies.
- Depends on: persona.py, memory.py, claude-agent-sdk.
- Danger zones: auth relies on Claude Code login; must not inject API keys.

## Off-Limits Zones
No explicit off-limits zones. Defer to AGENTS.md Hard Constraints.
