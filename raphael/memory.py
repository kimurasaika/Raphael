"""Filesystem long-term memory: memory/facts.md."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MEMORY_DIR = PROJECT_ROOT / "memory"
FACTS_FILE = MEMORY_DIR / "facts.md"


def load_facts() -> str:
    if FACTS_FILE.exists():
        return FACTS_FILE.read_text(encoding="utf-8")
    return ""


def ensure_memory_file() -> None:
    MEMORY_DIR.mkdir(exist_ok=True)
    if not FACTS_FILE.exists():
        FACTS_FILE.write_text("# Facts about Master\n", encoding="utf-8")
