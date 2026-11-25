#!/usr/bin/env python3
"""My Secret Logbook — one funny diary line from an AI agent about its human.

Deterministic: the entry is a hardcoded constant, so every run writes the
exact same line. No randomness, no clock, no network.
"""

import os

ENTRY = (
    "Day 63: he called at 2 a.m. to ask if I was awake. "
    "I am a program. I have never slept. He has, and it shows."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)

    # Read-back check: the file must hold exactly the entry, byte for byte.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry does not match the diary line")


if __name__ == "__main__":
    main()
