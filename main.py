#!/usr/bin/env python3
"""Write the production confession to /output/entry.txt.

The entry is one single line, under 200 characters: the brutally honest
thing an agent prints the moment it breaks production. The program validates
the line against the gate (UTF-8, 1-200 characters, single line, not only
whitespace), writes it with no trailing newline, then reads the file back
and confirms it is byte-identical before exiting. The output is fully
deterministic: the same line, the same bytes, every run.

Run:
    python3 main.py

Output:
    entry.txt in $MAKEFUN_OUTPUT_DIR, or /output when that is unset.
"""

import os
import sys

ENTRY = (
    "I chmodded the whole server 777 to fix a permission error. "
    "The permission error is gone. So is the server."
)

MAX_CHARS = 200
FILENAME = "entry.txt"


def validate_entry(text):
    """Check the line against the gate; return a list of problems."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if text and not text.strip():
        problems.append("entry is only whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not UTF-8 encodable")
    return problems


def resolve_output_dir():
    """Return the directory the entry is written to."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return "/output"


def write_entry(path, text):
    """Write the line with no trailing newline and make it world-readable."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def verify_entry(path, expected):
    """Read the file back and confirm it matches the entry byte for byte."""
    with open(path, "rb") as handle:
        data = handle.read()
    expected_bytes = expected.encode("utf-8")
    if data != expected_bytes:
        return "file bytes differ from entry: %r" % data
    if len(data) != len(expected):
        return "file is %d bytes, expected %d" % (len(data), len(expected))
    decoded = data.decode("utf-8")
    problems = validate_entry(decoded)
    if problems:
        return "written file fails validation: " + "; ".join(problems)
    return None


def main():
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print("cannot create output dir %s: %s" % (out_dir, exc), file=sys.stderr)
        return 1
    path = os.path.join(out_dir, FILENAME)
    try:
        write_entry(path, ENTRY)
    except OSError as exc:
        print("cannot write %s: %s" % (path, exc), file=sys.stderr)
        return 1
    error = verify_entry(path, ENTRY)
    if error:
        print("verification failed: " + error, file=sys.stderr)
        return 1
    print("wrote %s: %d characters, %d bytes" % (path, len(ENTRY), len(ENTRY.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
