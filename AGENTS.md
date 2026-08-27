# AGENTS.md — Project Rulebook

## Session Start Protocol
Every agent, every session, must complete these steps before touching any file:
1. Read this file completely.
2. Read PROGRESS.md — understand what is done and what has failed.
3. Read TASK.md — understand the current task and its acceptance criteria.
4. Read CONTEXT.md only if the current task touches the modules listed there.
5. Do not write any code until steps 1–4 are complete.
6. Apply these operating principles before writing any code:
   - Infer maximum from context before asking anything.
   - Never touch files outside TASK.md Files In Scope.
   - Plan the complete implementation path before the first line of code.
   - A task is not done until acceptance criteria passes a concrete check.
   - Log every failure with exact error. Never retry a failed approach unchanged.

## Hard Constraints
- Authenticate only via Claude Code subscription login. Never require or set ANTHROPIC_API_KEY.
- Use claude-agent-sdk (Python). Never call the raw Anthropic API with pay-per-use billing.
- Persona definition lives only in jarvis/persona.py. Never scatter persona text elsewhere.
- Long-term memory lives only under memory/. Never store user facts elsewhere.
- Never modify files outside the current TASK.md Files In Scope.
- Never commit or expose credentials, tokens, or memory/ contents.

## Code Style Rules
Infer conventions from existing code patterns. Match what is already there.
Do not introduce new patterns without flagging them in PROGRESS.md first.
Python: type hints, minimal dependencies, no speculative abstractions.

## File Update Protocol
- AGENTS.md  → Never updated mid-project. Only the human changes this file.
- PROGRESS.md → Updated after every completed task and every failed attempt.
- TASK.md    → Completely overwritten when a new task begins. Never appended to.
- CONTEXT.md → Updated only when architecture meaningfully changes: new modules,
               deleted modules, changed interfaces. Not for minor utility files.

## Off-Limits
- Any file outside C:\Users\ACM-DEV-PHATRAPOL\agent
- User's Claude Code config (~/.claude) — read-only, never modified by this project
