# TASK.md — Current Task

## Task Name
Task 3 — Token-economy persona rules + full CLI setup README

## What This Task Requires
1. Add an output-token-economy section to raphael/persona.py: concise by
   default, no filler/preamble/repetition, short summaries, expand only when
   Master asks. Persona intact, just leaner.
2. Rewrite README.md: complete from-scratch setup on a fresh terminal
   (prerequisites: Python 3.12+, Claude Code CLI, git; clone, install, login,
   run, test) + troubleshooting basics.

## Files In Scope
- raphael/persona.py
- README.md

## Files Out Of Scope
- Everything else. No caveman skill import.

## Acceptance Criteria
`python tests/smoke_test.py` exits 0; reply is in persona and noticeably
shorter than Task 2 baseline (was ~90 words). Push to origin succeeds.

## Approach
1. Edit persona.py: add "Token economy" rules block.
2. Rewrite README.md.
3. Run smoke test, compare length.
4. Commit + push; log in PROGRESS.md.

## Known Risks
- Over-tight brevity rules could clip useful detail → rule includes
  "expand when Master asks or when accuracy demands".
