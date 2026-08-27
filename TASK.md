# TASK.md — Current Task

## Task Name
Task 4 — Global /raphael slash command (Claude Code, all projects)

## What This Task Requires
Create a user-level Claude Code slash command `/raphael` so Master can invoke
Raphael's persona in any Claude Code session, in any project, without cloning
the repo per-project. This is a separate invocation mode from the standalone
raphael/main.py SDK app (which remains for a fully isolated session with its
own tool permissions). The slash command runs inside the current Claude Code
session and uses its already-available tools (Bash, Read, Write, WebSearch).

Memory for this mode is global (not per-project): ~/.claude/raphael/facts.md.

## Files In Scope
- ~/.claude/commands/raphael.md (new, outside repo — directed by Master)
- C:\Users\ACM-DEV-PHATRAPOL\agent\commands\raphael.md (repo copy, for distribution)
- C:\Users\ACM-DEV-PHATRAPOL\.claude\raphael\facts.md (global memory file, created empty)
- README.md (document the new usage mode)

## Files Out Of Scope
- raphael/ package, tests/ — untouched, standalone app still works as-is.

## Acceptance Criteria
1. `~/.claude/commands/raphael.md` exists, well-formed (frontmatter + body),
   non-empty persona instructions.
2. Master can type `/raphael` in any Claude Code session and get a Raphael-
   persona reply. (Structural verification here; live test happens in Master's
   next session since slash commands can't be invoked from Bash.)
3. Repo pushed with distribution copy + README update.

## Approach
1. Create global memory dir + empty facts.md.
2. Write ~/.claude/commands/raphael.md: frontmatter (description) + persona
   body (identity, token-economy rules, memory protocol pointing at the
   global facts.md path).
3. Copy same content into repo under commands/raphael.md with install note.
4. Update README: new "Quick usage — /raphael slash command" section above
   the existing standalone-app instructions.
5. Verify file structurally (exists, non-empty, correct frontmatter).
6. Commit + push; log in PROGRESS.md, including the directed exception to
   the ~/.claude off-limits rule.

## Known Risks
- Slash command frontmatter format could be wrong → verify against Claude
  Code docs conventions (description field); low risk, degrades gracefully
  (worst case: command shows with no description, still works).
- Two personas/memories (global vs standalone app) could drift apart →
  document clearly in README which mode does what.
