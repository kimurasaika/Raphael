# Raphael

Personal CLI assistant with the persona of Raphael (Tensei Shitara Slime Datta Ken),
built on the Claude Agent SDK. Runs on a Claude Pro/Max subscription via Claude Code
login — no API key, no pay-per-use billing. Replies are tuned for low output-token
usage (lean-answer rules built into the persona).

## Capabilities
- Multi-turn chat with a fixed persona
- Runs local shell commands, reads/writes/edits files
- Web search and fetch
- Long-term memory across sessions (`memory/facts.md`, kept local, never committed)
- Ayanokoji strategic execution protocol loaded as a project skill
  (`.claude/skills/ayanokoji/`)

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
```bash
python -m raphael.main
```
Type your message at the `Master>` prompt. `exit` or `quit` to leave.

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
Raphael stores facts about you in `memory/facts.md` (created on first run).
Tell it "remember ..." to add facts. The folder is gitignored — personal data
never leaves your machine.
