# Contributing to BlackTrace CTF Writeups

Thank you for helping improve this cybersecurity documentation repository.

## Contribution Principles

- Keep documentation accurate, clear, and reproducible.
- Respect CTF and training-platform rules.
- Do not publish prohibited flags, challenge files, or solutions.
- Never include real credentials, tokens, private keys, or personal data.
- Use only authorized environments.

## Adding a Writeup

1. Select the appropriate platform and category.
2. Create a challenge folder using lowercase kebab-case.
3. Copy the relevant template from `templates/`.
4. Add a `README.md` and `metadata.yml`.
5. Include scripts only when they materially improve reproducibility.
6. Add sanitized evidence when useful.
7. Run the repository validation scripts.
8. Review the final changes before committing.

## Naming Convention

Use descriptive lowercase names separated by hyphens.

Examples:

- `password-reset`
- `linux-privilege-escalation`
- `machine-name`

Avoid spaces, random abbreviations, and misleading names.

## Evidence and Files

- Store screenshots in `evidence/`.
- Store permitted challenge artifacts in `files/`.
- Do not commit large files without reviewing their necessity.
- Redact sensitive information from screenshots and logs.

## Commit Messages

Use meaningful commit messages:

- `docs: add web challenge writeup`
- `docs: improve repository guide`
- `fix: correct command in writeup`
- `feat: add writeup validation script`

## Review Checklist

Before submitting:

- [ ] Writeup follows the relevant template.
- [ ] Commands and outputs are clearly explained.
- [ ] Metadata is valid.
- [ ] Links work.
- [ ] Sensitive information is removed.
- [ ] Platform rules permit publication.
