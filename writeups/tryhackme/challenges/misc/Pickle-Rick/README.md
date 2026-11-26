# Pickle Rick — TryHackMe Learning Notes

## Challenge Overview

| Field | Details |
|---|---|
| Platform | TryHackMe |
| Room | Pickle Rick |
| Category | CTF |
| Difficulty | Easy |
| Status | Completed |
| Portfolio | BlackTrace |

## Learning Objective

This challenge provided practical experience with network reconnaissance, web enumeration, source-code inspection, Linux command-line navigation, and privilege-escalation concepts.

## Scope and Authorization

All activity was performed against the machine deployed for the TryHackMe Pickle Rick room.

The target was accessed only within the authorized training environment.

## Skills Practiced

- Network service discovery
- Web directory enumeration
- HTML source-code inspection
- Identifying application clues
- Linux filesystem navigation
- Understanding command execution in a web application
- Reverse-shell concepts in a controlled lab
- Reviewing sudo permissions
- Understanding privilege escalation risks

## Tools Used

- Nmap
- Gobuster
- Browser Developer Tools
- Netcat
- Linux command-line utilities

## Evidence Organization

Screenshots collected during the challenge are organized in the local `evidence/` directory.

Evidence filenames follow a numbered naming convention to keep the investigation in chronological order.

## Key Lessons

1. Review the page source instead of relying only on the rendered website.
2. Check commonly exposed web resources during enumeration.
3. Keep reconnaissance results organized and reproducible.
4. Understand the security impact of command execution through a web application.
5. Review user permissions carefully during Linux enumeration.
6. Apply least-privilege principles when assessing sudo configuration.
7. Sanitize screenshots before sharing any security evidence.

## Completion

The TryHackMe room was completed successfully.

Detailed room answers and walkthrough material are retained as personal study notes and are not published while the room is active.

## Responsible Disclosure and Platform Rules

This document is a learning record. Detailed solutions, flags, and walkthrough steps will not be published unless TryHackMe marks the room as retired and its current rules permit publication.

## Disclaimer

This repository documents authorized cybersecurity learning and lab practice only.
