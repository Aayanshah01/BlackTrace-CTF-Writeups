#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATES="$ROOT/templates"
WRITEUPS="$ROOT/writeups"

usage() {
  cat <<'USAGE'
Usage:
  ./scripts/new-writeup.sh <platform> <type> <name> [category]

Platforms:
  hackthebox | tryhackme | ctf | other-platforms | personal-labs

Types:
  machine | challenge | room | lab | report

Example:
  ./scripts/new-writeup.sh hackthebox machine forest windows
USAGE
}

if [[ $# -lt 3 || $# -gt 4 ]]; then
  usage
  exit 1
fi

platform="$1"
type="$2"
name="$3"
category="${4:-misc}"

# Validate simple path components to prevent path traversal.
for value in "$platform" "$type" "$name" "$category"; do
  if [[ ! "$value" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]*$ ]]; then
    echo "[ERROR] Invalid argument: $value"
    echo "Use letters, numbers, hyphens, and underscores only."
    exit 1
  fi
done

case "$platform" in
  hackthebox)
    case "$type" in
      machine) base="$WRITEUPS/hackthebox/machines" ;;
      challenge) base="$WRITEUPS/hackthebox/challenges/$category" ;;
      *) echo "[ERROR] HTB supports machine or challenge."; exit 1 ;;
    esac
    ;;
  tryhackme)
    case "$type" in
      room) base="$WRITEUPS/tryhackme/rooms" ;;
      challenge) base="$WRITEUPS/tryhackme/challenges/$category" ;;
      *) echo "[ERROR] THM supports room or challenge."; exit 1 ;;
    esac
    ;;
  ctf)
    year="$(date +%Y)"
    base="$WRITEUPS/ctf/$year"
    ;;
  other-platforms)
    base="$WRITEUPS/other-platforms"
    ;;
  personal-labs)
    base="$WRITEUPS/personal-labs/$category"
    ;;
  *)
    echo "[ERROR] Unsupported platform: $platform"
    usage
    exit 1
    ;;
esac

case "$type" in
  machine) template="machine-template.md" ;;
  challenge) template="challenge-template.md" ;;
  room) template="lab-template.md" ;;
  lab) template="lab-template.md" ;;
  report) template="report-template.md" ;;
  *)
    echo "[ERROR] Unsupported type: $type"
    usage
    exit 1
    ;;
esac

destination="$base/$name"

if [[ -e "$destination" ]]; then
  echo "[ERROR] Destination already exists: $destination"
  echo "No files were overwritten."
  exit 1
fi

if [[ ! -f "$TEMPLATES/$template" ]]; then
  echo "[ERROR] Template not found: $TEMPLATES/$template"
  exit 1
fi

mkdir -p "$destination"
cp "$TEMPLATES/$template" "$destination/README.md"

mkdir -p "$destination/evidence"
mkdir -p "$destination/files"
mkdir -p "$destination/scripts"

cat > "$destination/metadata.yml" <<META
title: "$name"
platform: "$platform"
category: "$category"
difficulty: "unknown"
date: "$(date +%F)"
status: "in-progress"

skills: []
tools: []
tags: []

writeup: "README.md"
scripts: []
evidence: []

flag_policy: "follow-platform-rules"
public_writeup: false
META

echo
echo "[PASS] Writeup created:"
echo "$destination"
echo
echo "Next steps:"
echo "  1. Edit README.md"
echo "  2. Complete metadata.yml"
echo "  3. Add sanitized evidence"
echo "  4. Run the repository validator"
