# Setup Checklist

Follow these steps when starting a new paper project from this template.

---

## 1. Copy the template

Copy or clone this repository into your paper project directory. If your paper is already in a git repo, copy the Claude files, the Codex files, and the top-level instruction files you need.

```bash
cp -r scientific_writing_agent/.claude /path/to/your/paper/
cp -r scientific_writing_agent/.codex /path/to/your/paper/
cp scientific_writing_agent/CLAUDE.md /path/to/your/paper/
cp scientific_writing_agent/AGENTS.md /path/to/your/paper/
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

If you do not have an associated implementation, you can delete the implementation checker and technical rewrite workflow from both `.claude/` and `.codex/`.

---

## 6. Customize the paper-build skill

Open `.claude/skills/paper-build/SKILL.md` and follow the `CUSTOMIZE` instructions at the top:

- [ ] Replace `<YOUR_PROJECT_ROOT>` with the absolute path to your manuscript repository
- [ ] Replace `<YOUR_OUTPUT_PDF>` with the actual output path (e.g. `build/paper.pdf`)
- [ ] Update the build command if you don't use `make pdf`
- [ ] Update the lint command if you don't use `make lint`, or delete Step 2 if you don't lint
- [ ] Copy your suppressed chktex warning IDs from CLAUDE.md into the lint step comment

Mirror the same project-specific build behavior in `.codex/skills/paper-build/SKILL.md`.

---

## 7. Add project macros to the writer skills

In each of the three writing skills below, find the `<!-- CUSTOMIZE: List your project-specific macros -->` comment and replace it with your actual macro list:

- [ ] `.claude/skills/address-reviewer-comment/SKILL.md` (Phase 2)
- [ ] `.codex/skills/address-reviewer-comment/SKILL.md` (Phase 2)
- [ ] `.claude/skills/write-to-intent/SKILL.md` (Phase 2)
- [ ] `.codex/skills/write-to-intent/SKILL.md` (Phase 2)
- [ ] `.claude/skills/technical-paragraph-rewrite/SKILL.md` (Phase 3)
- [ ] `.codex/skills/technical-paragraph-rewrite/SKILL.md` (Phase 3)

---

## 8. Add author annotation commands (OPTIONAL)

If your project uses per-author annotation macros (e.g. `\alice{...}`, `\bob{...}`):

- [ ] Add them to the annotation table in `CLAUDE.md`
- [ ] Add them to the annotation table in `AGENTS.md`
- [ ] Add them to `.claude/skills/find-annotations/SKILL.md` (grep command and output format)
- [ ] Add them to `.codex/skills/find-annotations/SKILL.md`

---

## 9. Configure sync-remote (OPTIONAL)

If you sync with a remote (Overleaf, GitHub, etc.):

- [ ] Open `.claude/skills/sync-remote/SKILL.md` and adjust the `git add` glob patterns to match your project's source layout (figures directory name, etc.).
- [ ] Open `.codex/skills/sync-remote/SKILL.md` and adjust the same staging rules.

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
| `paper-implementation-checker.md` | Paths filled in (or file deleted) |
| `technical-paragraph-rewrite/SKILL.md` | Paths filled in (or file deleted) |
| `address-reviewer-comment/SKILL.md` | Phase 0 table filled in |
| `write-to-intent/SKILL.md` | Phase 1a table filled in |
| `find-annotations/SKILL.md` | Author commands added (if applicable) |
| `sync-remote/SKILL.md` | git add patterns adjusted (if applicable) |
