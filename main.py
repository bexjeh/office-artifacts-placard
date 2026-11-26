#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Deterministic: the text is a fixed constant; no clock, no randomness,
no network, no environment reads beyond the output directory.
"""

import os

PLACARD = (
    "Stapler, c. 2019, pressed steel. "
    "Binding tool of the Covenant of Two Sheets; "
    "its jams were read as omens. "
    "Gift of Facilities."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
