#!/usr/bin/env python3
"""Validate writeup structure and basic metadata without third-party packages."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
WRITEUPS = ROOT / "writeups"

REQUIRED_METADATA = (
    "title",
    "platform",
    "category",
    "difficulty",
    "date",
    "status",
)

def parse_simple_yaml(path: Path) -> dict:
    """Read simple top-level key:value metadata lines."""
    data = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.lstrip().startswith("#") or line.startswith(" "):
            continue

        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"').strip("'")

    return data

def main() -> int:
    if not WRITEUPS.exists():
        print("[FAIL] writeups directory is missing")
        return 1

    # A challenge is identified by its metadata file.
    # Platform and event README files are indexes, not challenges.
    challenge_dirs = [
        metadata.parent
        for metadata in WRITEUPS.rglob("metadata.yml")
    ]

    errors = 0

    for folder in sorted(set(challenge_dirs)):
        metadata = folder / "metadata.yml"
        readme = folder / "README.md"

        print(f"\nChecking: {folder.relative_to(ROOT)}")

        if not readme.is_file() or readme.stat().st_size == 0:
            print("[FAIL] Missing or empty README.md")
            errors += 1
            continue

        if not metadata.is_file():
            print("[FAIL] Missing metadata.yml")
            errors += 1
            continue

        values = parse_simple_yaml(metadata)
        missing = [key for key in REQUIRED_METADATA if not values.get(key)]

        if missing:
            print("[FAIL] Missing metadata fields:", ", ".join(missing))
            errors += 1
        else:
            print("[PASS] Required metadata fields present")

        if not readme.read_text(encoding="utf-8").strip():
            print("[FAIL] README has no content")
            errors += 1
        else:
            print("[PASS] README content present")

    if not challenge_dirs:
        print("[INFO] No writeups found yet; repository structure is valid.")

    if errors:
        print(f"\n[FAIL] Validation completed with {errors} issue(s).")
        return 1

    print("\n[PASS] Writeup validation completed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
