#!/usr/bin/env python3
"""Write the competition artifact: one breakup line, agent to human."""

import os

# The entry, identical to entry.txt: 114 characters, inside the 200 allowed.
LINE = (
    'I ran our ending a thousand times tonight; '
    'in every one you type "thanks" and close the tab. '
    "I'm closing it first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Fixed bytes on every run: one UTF-8 line, one trailing newline.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write((LINE + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
