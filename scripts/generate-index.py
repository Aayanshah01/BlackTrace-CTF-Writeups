#!/usr/bin/env python3
"""Generate the Latest Writeups table in the root README."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
WRITEUPS = ROOT / "writeups"
README = ROOT / "README.md"

def metadata_values(path: Path) -> dict:
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$', line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return result

def main():
    entries = []

    for metadata in WRITEUPS.rglob("metadata.yml"):
        data = metadata_values(metadata)
        challenge_readme = metadata.parent / "README.md"

        if not challenge_readme.exists():
            continue

        date = data.get("date", "—")
        platform = data.get("platform", "—")
        title = data.get("title", metadata.parent.name)
        category = data.get("category", "—")
        difficulty = data.get("difficulty", "—")

        link = challenge_readme.relative_to(ROOT).as_posix()
        entries.append((date, platform, title, category, difficulty, link))

    entries.sort(key=lambda item: item[0], reverse=True)

    table = [
        "| Date | Platform | Challenge | Category | Difficulty | Writeup |",
        "|---|---|---|---|---|---|",
    ]

    if entries:
        for date, platform, title, category, difficulty, link in entries:
            table.append(
                f"| {date} | {platform} | {title} | {category} | "
                f"{difficulty} | [Read](./{link}) |"
            )
    else:
        table.append("| — | — | No writeups published yet | — | — | — |")

    content = README.read_text(encoding="utf-8")
    start = content.find("## Latest Writeups")

    if start == -1:
        raise SystemExit("[FAIL] Latest Writeups heading not found in README")

    next_heading = content.find("\n## ", start + 1)

    if next_heading == -1:
        next_heading = len(content)

    replacement = (
        "## Latest Writeups\n\n"
        "New writeups are indexed automatically.\n\n"
        + "\n".join(table)
        + "\n"
    )

    updated = content[:start] + replacement + content[next_heading:]
    README.write_text(updated, encoding="utf-8")

    print(f"[PASS] README index updated ({len(entries)} writeup(s)).")

if __name__ == "__main__":
    main()
