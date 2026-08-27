"""Smoke test: agent replies in persona using subscription auth. Exit 0 = pass."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, TextBlock, query

from raphael.memory import PROJECT_ROOT, load_facts
from raphael.persona import build_system_prompt


async def run() -> int:
    options = ClaudeAgentOptions(
        system_prompt=build_system_prompt(load_facts()),
        allowed_tools=[],
        cwd=str(PROJECT_ROOT),
        setting_sources=["project"],
    )
    reply = ""
    async for message in query(prompt="Who are you?", options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    reply += block.text

    print("--- reply ---")
    print(reply)
    print("-------------")
    if reply.strip() and "Raphael" in reply:
        print("SMOKE TEST PASS")
        return 0
    print("SMOKE TEST FAIL: empty reply or persona name missing")
    return 1


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(asyncio.run(run()))
