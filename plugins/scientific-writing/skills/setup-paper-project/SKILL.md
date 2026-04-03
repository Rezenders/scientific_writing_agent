---
name: setup-paper-project
description: Set up or refresh the scientific-writing configuration for the current repository from `.scientific-writing.json`.
---

# Setup Paper Project

Use this workflow when the current repository should be configured or refreshed for a specific scientific paper.

## Steps

1. Inspect `.scientific-writing.json` in the current repository root.
2. If it does not exist, run:

```bash
python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .
```

3. If it exists but needs updates, edit the config first, then rerun the same command.
4. Report which managed files were created or refreshed.
5. Highlight remaining placeholders and note that implementation-checker outputs are skipped when `implementation.enabled` is `false`.

## Constraints

- This workflow updates the current repository in place.
- Treat `.scientific-writing.json` as user-owned.
- Treat `AGENTS.md`, `CLAUDE.md`, `.codex/...`, and `.claude/...` as setup-managed outputs.
