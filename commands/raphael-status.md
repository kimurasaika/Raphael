---
description: Quick status check — Raphael's global memory and this project's Ayanokoji scaffold, no full persona takeover
---

Give a short status report in Raphael's voice (a single "Report." line, not a
full persona activation — you do not need to stay in character afterward
unless Master keeps addressing you as Raphael).

1. Read `~/.claude/raphael/facts.md` (Windows:
   `C:\Users\ACM-DEV-PHATRAPOL\.claude\raphael\facts.md`). If it doesn't
   exist or is empty, say memory is empty. Otherwise count the fact bullets
   and name the 1-2 most recent.
2. Check the current working directory for Ayanokoji scaffold files
   (AGENTS.md, CONTEXT.md, TASK.md, PROGRESS.md). If TASK.md exists, read it
   and state the current `## Task Name` in a few words. If PROGRESS.md
   exists, note how many entries are in `## Completed Tasks` and what
   `## Current Blockers` says (or "none").
3. If neither memory nor scaffold files exist, say so plainly — don't pad.

Keep the whole reply to about 4-6 lines total. Example shape:

"Report. Memory: 12 facts, most recent: prefers terse replies, uses VS Code.
Project: Ayanokoji scaffold present. Current task: fix login timeout.
Blockers: none."
