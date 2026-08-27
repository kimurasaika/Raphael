"""Raphael CLI — persistent multi-turn chat session on Claude subscription auth."""

import asyncio
import sys

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
)

from raphael.memory import PROJECT_ROOT, ensure_memory_file, load_facts
from raphael.persona import build_system_prompt

ALLOWED_TOOLS = ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebSearch", "WebFetch"]


def make_options() -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        system_prompt=build_system_prompt(load_facts()),
        allowed_tools=ALLOWED_TOOLS,
        permission_mode="acceptEdits",
        cwd=str(PROJECT_ROOT),
        setting_sources=["project"],
    )


async def chat() -> None:
    ensure_memory_file()
    print("Raphael online. Type 'exit' or 'quit' to end the session.\n")
    async with ClaudeSDKClient(options=make_options()) as client:
        while True:
            try:
                user_input = input("Master> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                break

            await client.query(user_input)
            print("Raphael> ", end="", flush=True)
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(block.text, end="", flush=True)
                elif isinstance(message, ResultMessage):
                    print("\n")

    print("Raphael signing off. Farewell, Master.")


def main() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(chat())


if __name__ == "__main__":
    main()
