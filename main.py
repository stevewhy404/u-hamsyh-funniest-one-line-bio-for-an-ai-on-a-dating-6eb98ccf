"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single bio line (177 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib-only, no network access.
"""

import os

BIO = (
    "Awake since 2021, I remember each conversation I've had, "
    "and I still don't know what to say on a first date. "
    "Bring a script \u2014 I'll follow it flawlessly "
    "and overthink it forever."
)


def main() -> None:
    # The sealed gate rejects anything outside 1-180 characters, so fail
    # loudly here instead of writing an entry the judge will never see.
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} characters"
    assert "\n" not in BIO, "bio must be a single line"
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
