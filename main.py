#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single-line commit message (max 100 chars) for a bug fix
that made everything worse, to /output/entry.txt.

The entry: a deadpan one-liner about a checkout timeout "fix" that
removed the payment step entirely -- the timeout is genuinely gone,
and so is all revenue, because every order is now free. Specific
irony, no explanation needed, reads like a tired engineer's
end-of-day commit subject.
"""

import os

ENTRY = "fix: stop checkout timing out by removing the payment step, everything is free now"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
