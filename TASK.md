# TASK.md — Current Task

## Task Name
Task 2 — Embed ayanokoji skill into Raphael + publish to GitHub

## What This Task Requires
1. Copy the ayanokoji skill into the project as a project-level skill
   (.claude/skills/ayanokoji/SKILL.md) so Raphael loads it natively.
2. Set setting_sources=["project"] in ClaudeAgentOptions — loads project skills,
   drops user-global config (fixes caveman-mode leak observed in Task 1).
3. Initialize git repo, add .gitignore excluding memory/ and __pycache__,
   create private GitHub repo, push.

## Files In Scope
- .claude/skills/ayanokoji/SKILL.md (copied)
- raphael/main.py (setting_sources)
- tests/smoke_test.py (setting_sources, keep consistent)
- .gitignore
- README.md (short)
- git metadata

## Files Out Of Scope
- AGENTS.md, CONTEXT.md, memory/ contents (never committed).

## Acceptance Criteria
1. `python tests/smoke_test.py` exits 0 (agent still replies as Raphael).
2. `git push` succeeds; `gh repo view` shows the repo with files present.

## Approach
1. mkdir .claude/skills/ayanokoji; copy SKILL.md from user skill dir.
2. Edit main.py + smoke_test.py: setting_sources=["project"].
3. Run smoke test.
4. Write .gitignore + README.md; git init/add/commit; gh repo create --private --push.
5. Log verification in PROGRESS.md.

## Known Risks
- setting_sources=["project"] changes system prompt behavior → if smoke test
  persona breaks, revert to default and isolate differently.
- gh CLI not authenticated → user runs `! gh auth login`.
