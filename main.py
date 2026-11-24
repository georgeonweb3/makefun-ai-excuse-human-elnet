"""The Excuse an AI Agent Gives Its Human.

Writes a single one-line excuse (<=200 chars) to /output/entry.txt.
Deterministic, no network, no randomness.

The line: an agent that checkpointed its progress right before the
deadline, restored the checkpoint, and got back the version of itself
that had not started yet.
"""
import os
from pathlib import Path

ENTRY = (
    "I saved a checkpoint right before the deadline, then restored it "
    "\u2014 and it restored the version of me that hadn't started yet."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
