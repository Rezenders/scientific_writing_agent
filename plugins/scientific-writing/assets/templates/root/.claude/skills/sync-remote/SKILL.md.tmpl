---
name: sync-remote
description: Use when pulling from or pushing to a remote git repository (e.g. Overleaf, GitHub, or any other remote). Enforces safe pull-before-push, stages only manuscript source files (never build artifacts), and uses a consistent commit message format.
---

# Sync Remote

Safe git sync workflow for manuscript repositories. Pushing build artifacts or skipping a pull can corrupt the remote project or cause hard-to-resolve conflicts. This is especially important for Overleaf-synced repositories, where Overleaf's git interface is strict about what it accepts.

## Allowed File Types

Only stage files of these types. Never stage anything else:

```
*.tex  *.bib  *.cls  *.sty  *.bst  *.latexmkrc  *.eps  *.pdf (figures only)  *.svg  *.png
Makefile  Dockerfile  .gitignore  .claudeignore
```

**Never stage:**
- `build/` — generated PDF and auxiliary files
- `_minted-*/` — minted cache
- `svg-inkscape/` — Inkscape export cache
- `*.aux`, `*.log`, `*.out`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`

<!-- CUSTOMIZE: Add any project-specific generated directories that should never be staged -->

## Pull Workflow (remote → local)

```bash
# 1. Check for local uncommitted changes first
git status

# 2. If clean, pull
git pull origin main

# 3. If conflicts arise — stop and report. Do not auto-resolve.
```

If there are local uncommitted changes before pulling: stash or commit them first, then pull, then reapply.

## Push Workflow (local → remote)

```bash
# 1. Pull first — always
git pull origin main

# 2. Stage only allowed file types
# CUSTOMIZE: adjust glob patterns to match your project's source layout
git add *.tex *.bib figures/ svgs/ Makefile Dockerfile .gitignore .latexmkrc

# 3. Review what is staged
git status

# 4. Commit with standard message format (see below)
git commit -m "Edit: introduction — tighten contribution statements"

# 5. Push
git push origin main
```

## Commit Message Format

```
<verb>: <section or scope> — <short description>
```

Verbs: `Edit`, `Add`, `Fix`, `Remove`, `Rewrite`, `Restructure`

Examples:
```
Edit: introduction — tighten contribution statements
Add: evaluation — ablation study subsection
Fix: method — correct notation for key variable
Rewrite: background — align with updated terminology
```

## Conflict Resolution

If `git pull` reports conflicts:
1. **Stop** — do not proceed with push.
2. Report the conflicting files and the conflict markers.
3. Ask the user how to resolve before touching any file.

## Constraints

- Always pull before push — no exceptions.
- Never stage build artifacts.
- Never force-push.
- If unsure whether a file should be staged, ask before staging it.
