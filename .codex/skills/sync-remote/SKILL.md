---
name: sync-remote
description: Use when pulling from or pushing to the manuscript remote and you need the safe staging and sync rules for this repository.
---

# Sync Remote

Safe git sync workflow for the scientific manuscript repository, including Overleaf-compatible constraints.

## Core Rules

- Always pull before push.
- Never force-push.
- Never stage build artifacts.
- Never stage generated manuscript PDFs from the repository root or `build/`.
- Stop and ask the user if pull conflicts occur.

## Allowed Staged Content

Stage only manuscript source files and intentional assets such as:

- `*.tex`
- `*.bib`
- `*.cls`
- `*.sty`
- `*.bst`
- figure assets such as `*.png`, `*.svg`, `*.eps`, and figure `*.pdf`
- `.gitignore`

If unsure whether a file is a source asset or a generated artifact, ask before staging it.

## Never Stage

- `*.aux`
- `*.log`
- `*.out`
- `*.fls`
- `*.fdb_latexmk`
- `*.synctex.gz`
- generated manuscript PDFs
- `_minted-*` caches
- unrelated workspace files such as `COLCON_IGNORE`

## Pull Workflow

```bash
cd <PROJECT_ROOT>
git status
```

If `git status` shows local changes, stop and ask the user whether to commit, stash, or postpone the sync. Do not choose on the user's behalf.

Only pull when the worktree is clean:

```bash
git pull origin main
```

If `git pull` reports conflicts:

1. Stop.
2. Report the conflicting files.
3. Ask the user how to proceed.

## Push Workflow

```bash
cd <PROJECT_ROOT>
git status
test -z "$(git status --short)" || exit 1  # clean worktree required before pull
git pull origin main
git add -- <MAIN_TEX> <SECTION_FILE>
git diff --cached --name-only
git commit -m "Edit: scope - short description"
git push origin main
```

Stage explicit paths that actually exist instead of broad globs. Replace `<SECTION_FILE>` with the real files you intend to sync. This avoids accidental staging and works even when optional directories or file patterns are absent.

## Commit Message Pattern

Use:

```text
<verb>: <section or scope> - <short description>
```

Preferred verbs:

- `Edit`
- `Add`
- `Fix`
- `Remove`
- `Rewrite`
- `Restructure`
