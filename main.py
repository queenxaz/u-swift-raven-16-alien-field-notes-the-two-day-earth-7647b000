#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet
Earth after two days on the surface -- to /output/entry.txt.

No network, no randomness, no input files: the line is fixed text.
"""

from pathlib import Path

ENTRY = (
    "Two days on Earth: the locals keep small predators as housemates, "
    "feed them by hand, and thank them for the indifference. "
    "5/5 \u2014 would be ignored again."
)


def main() -> None:
    # Keep the gate happy by construction: one line, 1-200 characters.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
