# Setup Checklist

Follow these steps when starting a new paper project from this template.

---

## Preferred: plugin-based bootstrap

If you are using Codex with the repo-local plugin, start with the setup workflow managed by `plugins/scientific-writing/`.

The bundled plugin is registered in the repo-local marketplace at `.agents/plugins/marketplace.json`, so Codex can discover `scientific-writing` without manual path lookup once the repo is opened.

```bash
python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .
```

What this does:
- Creates `.scientific-writing.json` from template on first run (if missing)
- Generates or refreshes managed setup files (for example `AGENTS.md`, `CLAUDE.md`, `.codex/...`, `.claude/...`)

Rerun workflow:
- Edit `.scientific-writing.json`
- Rerun the same command to refresh managed outputs

Plugin mode behavior:
- Plugin-managed outputs are rewritten on rerun.
- Manual edits inside plugin-managed output files are overwritten on rerun.
- In plugin-first mode, prefer customization through `.scientific-writing.json` and plugin templates under `plugins/scientific-writing/assets/templates/root/`, not ad hoc edits to generated files.

How to read Steps 2-9 in plugin-first mode:
- Treat each step as identifying project-specific values and policy choices.
- Put config-backed values in `.scientific-writing.json`.
- When a step says to edit a generated output file, treat that as manual/non-plugin mode unless you intentionally accept overwrite on rerun; for durable plugin-mode changes, edit the corresponding template under `plugins/scientific-writing/assets/templates/root/`.

You can then use the checklist below for manual fine-tuning and optional customizations.

---

## 1. Copy the template

Copy or clone this repository into your paper project directory. If your paper is already in a git repo, copy the Claude files, the Codex files, the top-level instruction files, and the repo-local plugin files you need.

```bash
cp -r scientific_writing_agent/.claude /path/to/your/paper/
cp -r scientific_writing_agent/.codex /path/to/your/paper/
mkdir -p /path/to/your/paper/.agents/plugins
cp scientific_writing_agent/.agents/plugins/marketplace.json /path/to/your/paper/.agents/plugins/
cp scientific_writing_agent/CLAUDE.md /path/to/your/paper/
cp scientific_writing_agent/AGENTS.md /path/to/your/paper/
mkdir -p /path/to/your/paper/plugins
cp -r scientific_writing_agent/plugins/scientific-writing /path/to/your/paper/plugins/
```

If you skip copying `plugins/scientific-writing/`, the plugin bootstrap command
`python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .`
will fail because the script and templates are missing.

If you skip copying `.agents/plugins/marketplace.json`, the plugin can still work, but Codex may not discover it automatically from the repo-local marketplace.

---

## 2. Set the memory path in all three agent files

The agents use a persistent memory system that requires an **absolute path**. Find and replace `<YOUR_PROJECT_ROOT>` in all three agent files:

```bash
# From your paper repo root:
find .claude/agents -name "*.md" | xargs sed -i 's|<YOUR_PROJECT_ROOT>|'"$(pwd)"'|g'
```

macOS/BSD `sed` requires an explicit backup suffix argument (empty string means no backup file):

```bash
# From your paper repo root (macOS/BSD):
find .claude/agents -name "*.md" | xargs sed -i '' 's|<YOUR_PROJECT_ROOT>|'"$(pwd)"'|g'
```

Or edit manually — the placeholder appears once in each of:
- `.claude/agents/writer.md`
- `.claude/agents/consistency-auditor.md`
- `.claude/agents/scientific-paper-reviewer.md`

Then create the memory directories:

```bash
mkdir -p .claude/agent-memory/writer
mkdir -p .claude/agent-memory/consistency-auditor
mkdir -p .claude/agent-memory/scientific-paper-reviewer
```

Plugin-safe note:
- The `.claude/agents/*.md` files above are plugin-managed outputs. In plugin-first mode, set persistent edits in `plugins/scientific-writing/assets/templates/root/.claude/agents/*.md.tmpl` and rerun bootstrap.
- Direct edits in `.claude/agents/*.md` are manual/non-plugin mode unless you accept overwrite on rerun.

---

## 3. Customize CLAUDE.md

Open `CLAUDE.md` and fill in every `<!-- CUSTOMIZE -->` section:

- [ ] Paper title, topic, and format (journal/conference)
- [ ] Research questions (RQ1, RQ2, ...)
- [ ] Build commands and output path (`make pdf`, `latexmk`, etc.)
- [ ] Document structure (entry point, section files, support files)
- [ ] Inline annotation commands (standard + per-author)
- [ ] Key LaTeX macros your agents must preserve
- [ ] Project-specific terminology rules (if any)
- [ ] Implementation reference paths (if your paper describes a codebase)
- [ ] Known implementation details easy to misstate (if applicable)

---

## 4. Customize AGENTS.md and Codex context

Open `AGENTS.md` and fill in the same manuscript-specific information you added to `CLAUDE.md`:

- [ ] Paper title, topic, and format
- [ ] Research questions
- [ ] Build commands and output path
- [ ] Document structure
- [ ] Inline annotation commands
- [ ] Key LaTeX macros your agents must preserve
- [ ] Project-specific terminology rules
- [ ] Implementation reference paths (if applicable)

Then open `.codex/context/manuscript-context.md` and record any durable manuscript context that should remain stable across Codex sessions:

- [ ] Canonical system, method, dataset, and macro names
- [ ] Preferred terminology and important distinctions
- [ ] Notation conventions
- [ ] Known consistency risks
- [ ] Open exposition gaps
- [ ] Pre-existing build issues

---

## 5. Configure the implementation checker (OPTIONAL)

Only needed if your paper describes a software implementation:

- [ ] Open `.claude/agents/paper-implementation-checker.md` and replace all `<PATH_TO_...>` placeholders with your actual file paths.
- [ ] Open `.codex/agents/paper-implementation-checker.md` and replace all `<PATH_TO_...>` placeholders with your actual file paths.
- [ ] Open `.claude/skills/technical-paragraph-rewrite/SKILL.md` and update the Implementation Reference Paths table.
- [ ] Open `.codex/skills/technical-paragraph-rewrite/SKILL.md` and update the Implementation Reference Paths table.
- [ ] Open `.claude/skills/address-reviewer-comment/SKILL.md` and update the Phase 0 table.
- [ ] Open `.codex/skills/address-reviewer-comment/SKILL.md` and update the Phase 0 table.
- [ ] Open `.claude/skills/write-to-intent/SKILL.md` and update the Phase 1a table.
- [ ] Open `.codex/skills/write-to-intent/SKILL.md` and update the Phase 1a table.

If you do not have an associated implementation:

- Plugin mode (recommended): set `implementation.enabled` to `false` in `.scientific-writing.json`, rerun `setup_paper_project.py`, and skip implementation-only workflows in usage.
- Manual non-plugin mode: if you do not rerun the plugin bootstrap, you may delete implementation-checker and technical rewrite files from `.claude/` and `.codex/` if you want a smaller local setup.

---

## 6. Customize the paper-build skill

Open `.claude/skills/paper-build/SKILL.md` and follow the `CUSTOMIZE` instructions at the top:

- [ ] Replace `<YOUR_PROJECT_ROOT>` with the absolute path to your manuscript repository
- [ ] Replace `<YOUR_OUTPUT_PDF>` with the actual output path (e.g. `build/paper.pdf`)
- [ ] Update the build command if you don't use `make pdf`
- [ ] Update the lint command if you don't use `make lint`, or delete Step 2 if you don't lint
- [ ] Copy your suppressed chktex warning IDs from CLAUDE.md into the lint step comment

Mirror the same project-specific build behavior in `.codex/skills/paper-build/SKILL.md`.

Plugin-safe note:
- In plugin-first mode, edit `plugins/scientific-writing/assets/templates/root/.claude/skills/paper-build/SKILL.md.tmpl` and `plugins/scientific-writing/assets/templates/root/.codex/skills/paper-build/SKILL.md.tmpl`, then rerun bootstrap.
- Direct edits in generated `.../paper-build/SKILL.md` files are manual/non-plugin mode unless you accept overwrite on rerun.

---

## 7. Add project macros to the writer skills

In each of the three writing skills below, find the `<!-- CUSTOMIZE: List your project-specific macros -->` comment and replace it with your actual macro list:

- [ ] `.claude/skills/address-reviewer-comment/SKILL.md` (Phase 2)
- [ ] `.codex/skills/address-reviewer-comment/SKILL.md` (Phase 2)
- [ ] `.claude/skills/write-to-intent/SKILL.md` (Phase 2)
- [ ] `.codex/skills/write-to-intent/SKILL.md` (Phase 2)
- [ ] `.claude/skills/technical-paragraph-rewrite/SKILL.md` (Phase 3)
- [ ] `.codex/skills/technical-paragraph-rewrite/SKILL.md` (Phase 3)

Plugin-safe note:
- In plugin-first mode, apply these macro-list changes to the matching templates under `plugins/scientific-writing/assets/templates/root/.claude/skills/` and `plugins/scientific-writing/assets/templates/root/.codex/skills/`, then rerun bootstrap.
- Direct edits in generated skill files are manual/non-plugin mode unless you accept overwrite on rerun.

---

## 8. Add author annotation commands (OPTIONAL)

If your project uses per-author annotation macros (e.g. `\alice{...}`, `\bob{...}`):

- [ ] Add them to the annotation table in `CLAUDE.md`
- [ ] Add them to the annotation table in `AGENTS.md`
- [ ] Add them to `.claude/skills/find-annotations/SKILL.md` (grep command and output format)
- [ ] Add them to `.codex/skills/find-annotations/SKILL.md`

Plugin-safe note:
- In plugin-first mode, update the matching `find-annotations` templates under `plugins/scientific-writing/assets/templates/root/...`, then rerun bootstrap.
- Direct edits in generated `find-annotations` skill files are manual/non-plugin mode unless you accept overwrite on rerun.

---

## 9. Configure sync-remote (OPTIONAL)

If you sync with a remote (Overleaf, GitHub, etc.):

- [ ] Open `.claude/skills/sync-remote/SKILL.md` and adjust the `git add` glob patterns to match your project's source layout (figures directory name, etc.).
- [ ] Open `.codex/skills/sync-remote/SKILL.md` and adjust the same staging rules.

Plugin-safe note:
- In plugin-first mode, edit the matching `sync-remote` templates under `plugins/scientific-writing/assets/templates/root/...`, then rerun bootstrap.
- Direct edits in generated `sync-remote` skill files are manual/non-plugin mode unless you accept overwrite on rerun.

---

## 10. Verify the setup

Run a quick smoke test:

```bash
# In your paper repo, start Claude Code and try:
/find-annotations     # should scan .tex files and report annotations
/section-review       # try on one section to confirm agents are reachable
```

For Codex, open the repo and ask it to follow the repo-local `find-annotations` or `section-review` workflow from `.codex/skills/`.

---

## Summary of What You Customized

After completing setup, you should have:

| File | What you changed |
|---|---|
| `.claude/agents/*.md` | `<YOUR_PROJECT_ROOT>` replaced with absolute path |
| `.claude/agent-memory/*/` | Directories created |
| `CLAUDE.md` | All CUSTOMIZE sections filled in |
| `AGENTS.md` | Matching manuscript rules filled in for Codex |
| `.codex/context/manuscript-context.md` | Stable manuscript context recorded |
| `.codex/agents/*.md` | Optional implementation placeholders filled in |
| `paper-build/SKILL.md` | Project root, output path, build/lint commands filled in |
| `paper-implementation-checker.md` | Plugin mode: set `implementation.enabled=false` to skip/remove managed checker outputs on rerun; Manual non-plugin mode: optional file deletion if you will not rerun bootstrap |
| `technical-paragraph-rewrite/SKILL.md` | Plugin mode: keep managed file and skip implementation-only usage when `implementation.enabled=false`; Manual non-plugin mode: optional file deletion if you will not rerun bootstrap |
| `address-reviewer-comment/SKILL.md` | Phase 0 table filled in |
| `write-to-intent/SKILL.md` | Phase 1a table filled in |
| `find-annotations/SKILL.md` | Author commands added (if applicable) |
| `sync-remote/SKILL.md` | git add patterns adjusted (if applicable) |
