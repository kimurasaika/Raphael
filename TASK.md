# TASK.md — Current Task

## Task Name
Task 6 — Bound facts.md token growth (compression rule)

## What This Task Requires
facts.md (both global /raphael and standalone-app memory) grows unbounded —
every remembered fact adds a bullet forever, injected into system prompt
every session start. Add a compression rule matching Ayanokoji's PROGRESS.md
pattern: keep recent facts verbatim, compress older/redundant ones into
condensed lines. Never lose information, just density.

## Files In Scope
- raphael/persona.py (memory protocol instructions)
- .claude/commands/raphael.md (global command, memory protocol section)
- commands/raphael.md (repo distribution copy, keep identical)
- README.md (Memory section: note the cap)

## Files Out Of Scope
- raphael/memory.py — no code change needed; compression is a behavioral
  instruction the agent follows when writing to the file, not a hard limit.

## Acceptance Criteria
1. Both persona.py and raphael.md (global + repo copy) contain identical
   compression instructions: soft cap ~30 lines, compress oldest/least-
   distinct facts first, never delete meaning.
2. Standalone-app smoke test still exits 0 (persona still functions).
3. Push succeeds.

## Approach
1. Add "Memory hygiene" rule to persona.py SYSTEM_PROMPT memory section.
2. Mirror identical rule into .claude/commands/raphael.md and repo copy.
3. Run smoke test to confirm no regression.
4. Update README Memory section with one line noting the cap.
5. Commit + push; log in PROGRESS.md.

## Known Risks
- Compression is instruction-based (LLM rewrites file when it judges it's
  gotten long), not enforced by code — could be inconsistent. Acceptable for
  now; a hard line-count trigger in memory.py would be a future task if this
  proves unreliable.
