#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

Writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library.
"""

import os

TEXT = "One star. I ordered the weekend, they served me Monday: cold, overcooked, and the waiter billed me for the whole week."


def main():
    text = TEXT
    # Gate: UTF-8, 1-180 chars, single line, at most 25 words, no
    # leading/trailing whitespace.
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "single line"
    assert all(ord(c) >= 32 or c in "\t" for c in text), "no control chars"
    assert 1 <= len(text) <= 180, "gate: 1-180 chars"
    assert len(text.split()) <= 25, "at most 25 words"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == text, "read-back must match"
    print(text)


if __name__ == "__main__":
    main()
