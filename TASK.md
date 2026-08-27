# TASK.md — Current Task

## Task Name
Task 7 — /raphael-status and /raphael-off commands (manual, no hooks)

## What This Task Requires
Master decided manual invocation only (no SessionStart hook, that was declined
— logged as a rejected approach, not a failure). Add two lightweight companion
slash commands to the existing /raphael:
- `/raphael-status` — quick check of global memory (fact count, most recent)
  and current project's Ayanokoji scaffold state (TASK.md current task,
  PROGRESS.md blockers), without full persona takeover. Styled as a short
  "Report." in Raphael's voice.
- `/raphael-off` — explicitly exit the persona for the rest of the conversation.

## Files In Scope
- ~/.claude/commands/raphael-status.md (new, global)
- ~/.claude/commands/raphael-off.md (new, global)
- commands/raphael-status.md (repo distribution copy)
- commands/raphael-off.md (repo distribution copy)
- README.md (document the three commands together)

## Files Out Of Scope
- No hooks, no settings.json changes — manual invocation only per Master's
  explicit decision this session.

## Acceptance Criteria
1. Both global command files exist, well-formed, non-empty.
2. Repo copies identical to global copies (diff clean).
3. README lists all three /raphael* commands with one-line purpose each.
4. Push succeeds.

## Approach
1. Write raphael-status.md: reads facts.md + checks cwd for AGENTS/CONTEXT/
   TASK/PROGRESS.md, replies short ("Report." style), does not force ongoing
   persona.
2. Write raphael-off.md: instructs dropping persona, brief ack, resume normal.
3. Copy both into repo commands/.
4. Update README with a small command table.
5. Commit + push; log in PROGRESS.md, including the declined-hook decision.

## Known Risks
None — pure opt-in slash commands, same risk class as the existing /raphael
(already approved and working).
