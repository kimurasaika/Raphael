# Raphael

Personal CLI assistant with the persona of Raphael (Tensei Shitara Slime Datta Ken),
built on the Claude Agent SDK. Runs on a Claude Pro/Max subscription via Claude Code
login — no API key, no pay-per-use billing. Replies are tuned for low output-token
usage (lean-answer rules built into the persona).

## Capabilities
- Multi-turn chat with a fixed persona
- Runs local shell commands, reads/writes/edits files
- Web search and fetch
- Long-term memory across sessions
- Ayanokoji strategic execution protocol loaded as a project skill
  (`.claude/skills/ayanokoji/`)

## Why Raphael (strengths, trade-offs, use cases)

Raphael is two layers stacked: a **roleplay persona** (identity, tone, terse
"Answer."/"Report." style) plus the **Ayanokoji strategic execution protocol**
(structured intake, four scaffold files, verification gates) for real project
work. Neither layer alone is that special — combined, they make Raphael good
at *sustained, disciplined project work across sessions*, not casual chat.

### Strengths
- **Decisive, low-noise answers.** Token-economy rules built into the persona
  cut preamble, restating, and filler — good when you want the conclusion,
  not a essay.
- **Cross-session project memory.** Ayanokoji's PROGRESS.md/TASK.md/CONTEXT.md
  mean a new session picks up exactly where the last one left off — what was
  tried, what failed, what's still open — instead of re-deriving context.
- **Discipline on scope.** Ayanokoji forces "files in scope" before writing
  code, and a verification gate before marking anything done. Fewer silent
  half-finished changes.
- **Two invocation modes for two needs.** `/raphael` for quick cross-project
  convenience; the standalone app when you want an isolated session with its
  own tool permissions.
- **Subscription-based, not pay-per-use.** Runs on Claude Pro/Max login — cost
  is quota, not per-token billing.
- **Full local tool access.** Bash, file read/write, web search/fetch — it
  can actually execute work, not just describe it.

### Trade-offs
- **Persona can feel rigid for casual chat.** "Answer."/"Master" framing is
  built for decisive work, not open-ended brainstorming or small talk — say
  so explicitly if you want plain, unstyled replies.
- **Ayanokoji overhead isn't worth it for trivial asks.** The intake →
  scaffold → verify flow is for multi-session projects; a one-line question
  doesn't need four files.
- **Memory is a flat markdown file, not a knowledge base.** Fine for a
  handful of facts and decisions; it won't scale to large structured
  knowledge or fast lookup across hundreds of entries.
- **`/raphael` isn't isolated.** It runs inside your current Claude Code
  session and inherits its tool permissions — for a hard permission boundary,
  use the standalone app instead.
- **Single-user by design.** No multi-tenant memory separation; everything
  under one Master.

### Use cases where it shines
- Ongoing personal coding projects spanning many sessions — refactors,
  feature builds, anything where "what did we already try and why did it
  fail" matters.
- Repeated project bootstrapping — Ayanokoji's intake-then-scaffold flow is
  built exactly for "start a new thing correctly the first time."
- Quick technical Q&A where you want the answer first, reasoning only if
  asked.
- Research/synthesis tasks combining web search with local file work, with a
  consistent, trustworthy tone across the session.

### Where a plain assistant is a better fit
- Casual conversation, exploratory brainstorming, or creative writing — the
  terse "Answer." style actively fights against open-ended ideation.
- One-off questions with no follow-up — the scaffold/memory machinery adds
  nothing there.
- Multi-user or team settings — Raphael's memory and persona assume one
  Master.

## Two ways to use Raphael

| Mode | How | Runs where | Memory |
|---|---|---|---|
| **`/raphael` slash command** (recommended, quick) | Install once, then type `/raphael` in any Claude Code session, in any project | Inside your current Claude Code session, reuses its tools | Global: `~/.claude/raphael/facts.md` (all projects share it) |
| **Standalone app** | `python -m raphael.main` from this repo | Its own dedicated SDK session, isolated tool permissions | Project-local: `memory/facts.md` (this repo only) |

Pick `/raphael` for everyday convenience across every project. Pick the
standalone app when you want Raphael fully isolated with its own permission
scope.

Activation is manual by design — Raphael does not auto-load on every Claude
Code session start (no SessionStart hook). Invoke it explicitly.

### `/raphael*` commands
| Command | Does |
|---|---|
| `/raphael` | Activate Raphael's persona for the rest of the conversation |
| `/raphael-status` | Quick "Report." — memory fact count + this project's Ayanokoji task/blockers, no full persona takeover |
| `/raphael-off` | Drop the persona, resume normal Claude Code voice |
| `/raphael-research` | Deep-research playbook (web, X, Reddit, YouTube transcripts, GitHub) — load before multi-source research |

### Install (one time, works everywhere after)
```bash
# after cloning this repo (see Setup below), copy the commands into your
# global Claude Code config:
mkdir -p ~/.claude/commands
cp commands/raphael.md commands/raphael-status.md commands/raphael-off.md commands/raphael-research.md ~/.claude/commands/
```
Windows PowerShell:
```powershell
New-Item -ItemType Directory -Force ~/.claude/commands
Copy-Item commands/raphael.md, commands/raphael-status.md, commands/raphael-off.md, commands/raphael-research.md ~/.claude/commands/
```
Then, in any Claude Code session, in any project, type `/raphael` — no clone
needed per-project once this is installed.

## Requirements
| Requirement | Version | Check with |
|---|---|---|
| Python | 3.12+ | `python --version` |
| Claude Code CLI | 2.x | `claude --version` |
| git | any recent | `git --version` |
| Claude subscription | Pro or Max | login step below |

Python package (installed in step 3): `claude-agent-sdk`.

## Setup — from a fresh terminal

**1. Install prerequisites (skip any you already have)**

Windows (PowerShell):
```powershell
winget install Python.Python.3.12
winget install Git.Git
# Claude Code CLI:
irm https://claude.ai/install.ps1 | iex
```
macOS/Linux:
```bash
# Python 3.12+ and git via your package manager, then:
curl -fsSL https://claude.ai/install.sh | bash
```
Close and reopen the terminal after installing so PATH updates.

**2. Get the code**
```bash
git clone git@github.com:kimurasaika/Raphael.git
cd Raphael
```
(No SSH key? Use `git clone https://github.com/kimurasaika/Raphael.git`.)

**3. Install the Python dependency**
```bash
pip install -r requirements.txt
```

**4. Log in with your Claude subscription (one time)**
```bash
claude login
```
Browser opens — sign in with the account that has your Pro/Max plan.
Do NOT set `ANTHROPIC_API_KEY`; if it is set, unset it, or the SDK will
bill pay-per-use instead of using your subscription.

**5. Run Raphael**

Standalone app:
```bash
python -m raphael.main
```
Type your message at the `Master>` prompt. `exit` or `quit` to leave.

Or, if you installed the slash command above, just type `/raphael` in any
Claude Code session.

**6. Verify (optional)**
```bash
python tests/smoke_test.py
```
Expect `SMOKE TEST PASS` and exit code 0.

## Troubleshooting
- `claude: command not found` → reopen terminal, or re-run the installer in step 1.
- Auth errors from the SDK → run `claude login` again; make sure
  `ANTHROPIC_API_KEY` is not set in your environment.
- Garbled characters on Windows → run `chcp 65001` or use Windows Terminal.

## Memory
- Standalone app: `memory/facts.md` in this repo (gitignored, project-local).
- `/raphael` slash command: `~/.claude/raphael/facts.md` (global, shared
  across every project on your machine).

Tell Raphael "remember ..." in either mode to add facts. Data never leaves
your machine.

Every fact is re-loaded into context at every session start, so a growing
file is a recurring token cost — Raphael self-compresses facts.md once it
passes ~30 lines (keeps the last ~10 facts verbatim, condenses older ones),
same pattern as Ayanokoji's PROGRESS.md.
