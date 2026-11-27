#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes a single line -- the one line the writer would send back to
their younger self if one line were all they got -- to /output/entry.txt.

The gate requires the file to be UTF-8 text of 1 to 200 characters,
not only white space, and a single line. This program writes exactly
one line, checks the gate's limits itself, and exits non-zero if the
line ever broke them.

Usage:
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # writes <path> instead (for local testing)
"""

import os
import sys

LINE = (
    "You will spend years sanding off your edges to be easy to love; "
    "the day you stop is the day someone loves you for the sharp parts."
)


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"

    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry line is {len(text)} characters, must be 1-200")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Read back what was written and re-check the gate against the file
    # itself, not just the in-memory string, so a write failure or an
    # encoding surprise is caught here instead of by the grader.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != text:
        raise SystemExit("written file does not match the entry line")
    if not 1 <= len(written) <= 200 or "\n" in written:
        raise SystemExit("written file fails the gate")

    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
