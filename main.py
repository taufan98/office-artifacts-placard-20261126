#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — make.fun bounty entry.

Writes one museum placard for the humble office stapler, recast as a ritual
binding device of the Filing Clerks, to /output/entry.txt. Catalogue date,
materials and donor status included, as any good curator would insist.
"""

import os

ENTRY = "Stapler, c. 1998. Steel, rust, and quiet menace. Ritual binding device of the Filing Clerks; donor unknown, victim count unrecorded."


def validate(text: str) -> str:
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
