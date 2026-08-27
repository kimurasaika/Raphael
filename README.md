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

## Two ways to use Raphael

| Mode | How | Runs where | Memory |
|---|---|---|---|
| **`/raphael` slash command** (recommended, quick) | Install once, then type `/raphael` in any Claude Code session, in any project | Inside your current Claude Code session, reuses its tools | Global: `~/.claude/raphael/facts.md` (all projects share it) |
| **Standalone app** | `python -m raphael.main` from this repo | Its own dedicated SDK session, isolated tool permissions | Project-local: `memory/facts.md` (this repo only) |

Pick `/raphael` for everyday convenience across every project. Pick the
standalone app when you want Raphael fully isolated with its own permission
scope.

### Install `/raphael` (one time, works everywhere after)
```bash
# after cloning this repo (see Setup below), copy the command into your
# global Claude Code config:
mkdir -p ~/.claude/commands
cp commands/raphael.md ~/.claude/commands/raphael.md
```
Windows PowerShell:
```powershell
New-Item -ItemType Directory -Force ~/.claude/commands
Copy-Item commands/raphael.md ~/.claude/commands/raphael.md
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
