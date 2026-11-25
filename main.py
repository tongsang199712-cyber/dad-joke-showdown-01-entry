#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to
/output/entry.txt, where the sealed scorer reads it.

The joke is fixed text: no randomness, no clock, no network, no
model calls, no file reads besides this source. The program is
deterministic, so both graded runs produce the same file.
"""

import os

JOKE = (
    "My dad cancelled his gym membership. "
    "He says he gets all his exercise running out of patience."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1-200 characters")
    if JOKE != JOKE.strip():
        raise SystemExit("joke must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # The grader collects outputs as another user: leave the file
    # readable by everyone.
    os.chmod(path, 0o644)
    # Verify the graded file before exiting: read it back and confirm
    # it holds exactly the joke, within the 200-character gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE or not 1 <= len(written) <= 200:
        raise SystemExit(f"verification failed for {path}")
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
