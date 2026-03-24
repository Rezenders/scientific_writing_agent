# Setup Checklist

Follow these steps when starting a new paper project from this template.

---

## 1. Copy the template

Copy or clone this repository into your paper project directory. If your paper is already in a git repo, copy only the `.claude/` directory and the top-level files you need.

```bash
cp -r scientific_writing_agent/.claude /path/to/your/paper/
cp scientific_writing_agent/CLAUDE.md /path/to/your/paper/
```

---

## 2. Set the memory path in all three agent files

The agents use a persistent memory system that requires an **absolute path**. Find and replace `<YOUR_PROJECT_ROOT>` in all three agent files:

```bash
# From your paper repo root:
find .claude/agents -name "*.md" | xargs sed -i 's|<YOUR_PROJECT_ROOT>|'"$(pwd)"'|g'
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

## 4. Configure the implementation checker (OPTIONAL)

Only needed if your paper describes a software implementation:

- [ ] Open `.claude/agents/paper-implementation-checker.md` and replace all `<PATH_TO_...>` placeholders with your actual file paths.
- [ ] Open `.claude/skills/technical-paragraph-rewrite/SKILL.md` and update the Implementation Reference Paths table.
- [ ] Open `.claude/skills/address-reviewer-comment/SKILL.md` and update the Phase 0 table.
- [ ] Open `.claude/skills/write-to-intent/SKILL.md` and update the Phase 1a table.

If you do not have an associated implementation, you can delete `.claude/agents/paper-implementation-checker.md` and `.claude/skills/technical-paragraph-rewrite/` entirely.

---

## 5. Customize the paper-build skill

Open `.claude/skills/paper-build/SKILL.md` and follow the `CUSTOMIZE` instructions at the top:

- [ ] Replace `<YOUR_PROJECT_ROOT>` with the absolute path to your manuscript repository
- [ ] Replace `<YOUR_OUTPUT_PDF>` with the actual output path (e.g. `build/paper.pdf`)
- [ ] Update the build command if you don't use `make pdf`
- [ ] Update the lint command if you don't use `make lint`, or delete Step 2 if you don't lint
- [ ] Copy your suppressed chktex warning IDs from CLAUDE.md into the lint step comment

---

## 7. Add project macros to the writer skills

In each of the three writing skills below, find the `<!-- CUSTOMIZE: List your project-specific macros -->` comment and replace it with your actual macro list:

- [ ] `.claude/skills/address-reviewer-comment/SKILL.md` (Phase 2)
- [ ] `.claude/skills/write-to-intent/SKILL.md` (Phase 2)
- [ ] `.claude/skills/technical-paragraph-rewrite/SKILL.md` (Phase 3)

---

## 8. Add author annotation commands (OPTIONAL)

If your project uses per-author annotation macros (e.g. `\alice{...}`, `\bob{...}`):

- [ ] Add them to the annotation table in `CLAUDE.md`
- [ ] Add them to `.claude/skills/find-annotations/SKILL.md` (grep command and output format)

---

## 9. Configure sync-remote (OPTIONAL)

If you sync with a remote (Overleaf, GitHub, etc.):

- [ ] Open `.claude/skills/sync-remote/SKILL.md` and adjust the `git add` glob patterns to match your project's source layout (figures directory name, etc.).

---

## 10. Verify the setup

Run a quick smoke test:

```bash
# In your paper repo, start Claude Code and try:
/find-annotations     # should scan .tex files and report annotations
/section-review       # try on one section to confirm agents are reachable
```

---

## Summary of What You Customized

After completing setup, you should have:

| File | What you changed |
|---|---|
| `.claude/agents/*.md` | `<YOUR_PROJECT_ROOT>` replaced with absolute path |
| `.claude/agent-memory/*/` | Directories created |
| `CLAUDE.md` | All CUSTOMIZE sections filled in |
| `paper-build/SKILL.md` | Project root, output path, build/lint commands filled in |
| `paper-implementation-checker.md` | Paths filled in (or file deleted) |
| `technical-paragraph-rewrite/SKILL.md` | Paths filled in (or file deleted) |
| `address-reviewer-comment/SKILL.md` | Phase 0 table filled in |
| `write-to-intent/SKILL.md` | Phase 1a table filled in |
| `find-annotations/SKILL.md` | Author commands added (if applicable) |
| `sync-remote/SKILL.md` | git add patterns adjusted (if applicable) |
