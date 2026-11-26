#!/usr/bin/env python3
"""Check relative Markdown links for missing local files."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
MARKDOWN = list(ROOT.rglob("*.md"))

IGNORE_DIRS = {".git", ".venv", "venv"}

def main():
    errors = 0
    pattern = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')

    for document in MARKDOWN:
        if any(part in IGNORE_DIRS for part in document.parts):
            continue

        text = document.read_text(encoding="utf-8", errors="replace")

        for raw_target in pattern.findall(text):
            parts = raw_target.strip().split()

            if not parts:
                continue

            target = parts[0].strip("<>")

            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue

            target = target.split("#", 1)[0]
            if not target:
                continue

            resolved = (document.parent / target).resolve()

            if not resolved.exists():
                print(f"[FAIL] {document.relative_to(ROOT)} -> {target}")
                errors += 1

    if errors:
        print(f"\n[FAIL] Found {errors} broken local link(s).")
        return 1

    print("[PASS] No broken local Markdown links found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
