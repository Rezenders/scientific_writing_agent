# Plugin Setup

## What the plugin manages

The repo-local plugin at `plugins/scientific-writing/` provides the `setup-paper-project` workflow.

It renders managed setup files from plugin templates using values in `.scientific-writing.json`.

Current managed outputs (exact paths):
- `AGENTS.md`
- `CLAUDE.md`
- `.codex/agents/consistency-auditor.md`
- `.codex/agents/paper-implementation-checker.md` (only when `implementation.enabled=true`)
- `.codex/agents/scientific-paper-reviewer.md`
- `.codex/agents/writer.md`
- `.codex/context/manuscript-context.md`
- `.codex/skills/address-reviewer-comment/SKILL.md`
- `.codex/skills/find-annotations/SKILL.md`
- `.codex/skills/paper-build/SKILL.md`
- `.codex/skills/pre-submission/SKILL.md`
- `.codex/skills/section-review/SKILL.md`
- `.codex/skills/sync-remote/SKILL.md`
- `.codex/skills/technical-paragraph-rewrite/SKILL.md`
- `.codex/skills/write-to-intent/SKILL.md`
- `.claude/agents/consistency-auditor.md`
- `.claude/agents/paper-implementation-checker.md` (only when `implementation.enabled=true`)
- `.claude/agents/scientific-paper-reviewer.md`
- `.claude/agents/writer.md`
- `.claude/skills/address-reviewer-comment/SKILL.md`
- `.claude/skills/find-annotations/SKILL.md`
- `.claude/skills/paper-build/SKILL.md`
- `.claude/skills/pre-submission/SKILL.md`
- `.claude/skills/section-review/SKILL.md`
- `.claude/skills/sync-remote/SKILL.md`
- `.claude/skills/technical-paragraph-rewrite/SKILL.md`
- `.claude/skills/write-to-intent/SKILL.md`

## First run

Run from the repository root:

```bash
python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .
```

If `.scientific-writing.json` does not exist, it is created from the plugin template, then managed files are written.

## Rerun behavior

- If `.scientific-writing.json` exists, it is reused (not replaced).
- The script rewrites managed outputs from current config values.
- Manual edits to plugin-managed output files are overwritten on rerun.
- If `implementation.enabled` is `false`, outputs whose path contains `paper-implementation-checker` are skipped, and existing generated files at those paths are removed.

## Customization mode (plugin-first)

- In plugin-first mode, treat `.scientific-writing.json` as the main customization input.
- For structural or wording defaults across generated outputs, edit plugin templates in `plugins/scientific-writing/assets/templates/root/`.
- Avoid ad hoc edits directly in plugin-managed outputs unless you intentionally accept that rerun will overwrite them.
- If no implementation is available, keep `implementation.enabled=false` and skip implementation-only workflows in usage instead of deleting managed files.

When following `SETUP.md`, interpret steps that ask you to edit generated files as manual/non-plugin mode unless you accept overwrite on rerun; for durable plugin-mode updates, edit the corresponding templates instead.

## Ownership boundaries

- User-owned: `.scientific-writing.json`, manuscript source files (for example `*.tex`, `*.bib`, figures), and files not listed above.
- Plugin-managed: only the exact output paths listed above, rendered from `plugins/scientific-writing/assets/templates/root/*.tmpl` (excluding `.scientific-writing.json.tmpl`).
