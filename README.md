# Raphael

Personal CLI assistant with the persona of Raphael (Tensei Shitara Slime Datta Ken),
built on the Claude Agent SDK. Runs on a Claude Pro subscription via Claude Code
login — no API key required.

## Capabilities
- Multi-turn chat with a fixed persona
- Runs local shell commands, reads/writes/edits files
- Web search and fetch
- Long-term memory across sessions (`memory/facts.md`, not committed)
- Ayanokoji strategic execution protocol loaded as a project skill
  (`.claude/skills/ayanokoji/`)

## Setup
```
pip install -r requirements.txt
claude login   # once, with your Claude subscription
```

## Run
```
python -m raphael.main
```

## Test
```
python tests/smoke_test.py
```
