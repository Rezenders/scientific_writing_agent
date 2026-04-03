---
name: sync-remote
description: Use when pulling from or pushing to a remote git repository such as Overleaf or GitHub. Enforces pull-before-push, safe staging, and conservative conflict handling.
---

# Sync Remote

Safe remote sync workflow for manuscript repositories.

## Allowed File Types

Typical allowed files:

- `*.tex`
- `*.bib`
- `*.cls`
- `*.sty`
- `*.bst`
- `*.latexmkrc`
- `*.eps`
- figure `*.pdf`
- `*.svg`
- `*.png`
- `Makefile`
- `Dockerfile`
- `.gitignore`
- `AGENTS.md`
- `.codex/**`
- `.claude/**`

Never stage generated artifacts such as `build/`, LaTeX aux files, minted caches, or export caches.

## Constraints

- Always pull before push.
- Never force-push.
- If unsure whether a file belongs in the sync, ask before staging it.
