---
name: bootstrap-memory
description: Use at the start of a new paper project to pre-populate all agent memory files from CLAUDE.md/AGENTS.md and the manuscript. Run once after setup.
---

# Bootstrap Memory

Scans project policy files and the manuscript to pre-populate all agent memory files with project-specific knowledge.

## Workflow

### Phase 1 — Extract from AGENTS.md and manuscript-context.md

Read `AGENTS.md` and `.codex/context/manuscript-context.md`. Extract: macros, terminology rules, style rules, section structure, implementation reference paths, and build commands.

### Phase 2 — Extract from Manuscript

Read the introduction for contribution claims and key term definitions. Scan all sections for acronym definitions and notation.

### Phase 3 — Write Memory Files

Write extracted knowledge to memory files for each agent. Update rather than overwrite if a more specific file already exists.

- Writer: terminology, macros, style rules, section map, contributions
- Consistency auditor: canonical macro list with drift variants, defined acronyms, contribution claims, multi-meaning terms
- Scientific reviewer: core claims, known overclaiming risks, evaluation setup
- Implementation checker *(only if configured)*: reference paths, key non-obvious technical facts

All memory files must use the frontmatter format with `name`, `description`, `type: project`.

### Phase 4 — Update MEMORY.md Indices

For each agent that received new or updated files, update `MEMORY.md` with pointer lines.

### Phase 5 — Report

Report: files written or updated, facts extracted (macro count, acronym count, contribution count), and any unfilled `<!-- CUSTOMIZE -->` placeholders found.

## Constraints

- Do not overwrite memory content more specific than what was extracted.
- Do not record `<!-- CUSTOMIZE -->` placeholder text as facts — report them as gaps.
- If a section file is missing, note it and continue.
