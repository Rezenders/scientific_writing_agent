---
name: bootstrap-memory
description: Use after bootstrap-project-context to pre-populate optional agent memory files from AGENTS.md, CLAUDE.md, `.agents/context/`, and the manuscript.
---

# Bootstrap Memory

Scans project policy files, `.agents/context/`, and the manuscript to pre-populate optional agent memory files with project-specific knowledge.

This is not the initial questionnaire or context-filling workflow. Use `bootstrap-project-context` first when `.agents/context/` still contains generic placeholders.

## Project Layout

- Manuscript entry point: `<MAIN_TEX>`
- Section files: see `.agents/context/paper-model.md` or derive from `<MAIN_TEX>`.
- Implementation checker: configure project-specific paths in `.agents/context/paper-model.md` when implementation verification is relevant.

## Workflow

### Phase 1 — Extract from AGENTS.md and focused context files

Read `AGENTS.md`, `.agents/context/manuscript-context.md`, `.agents/context/paper-model.md`, `.agents/context/terminology.md`, `.agents/context/contributions.md`, and `.agents/context/evaluation-claims.md`. Extract macros, terminology rules, style rules, section structure, implementation reference paths, contribution claims, evaluation-scope boundaries, and build commands.

### Phase 2 — Extract from Manuscript

Read `<SECTION_FILE>` for contribution claims and key term definitions. Scan all sections under `sections/` for acronym definitions and notation.

### Phase 3 — Write Memory Files

Write extracted knowledge to memory files for each agent. Update rather than overwrite if a more specific file already exists.

- Writer: terminology, macros, style rules, section map, contributions
- Consistency auditor: canonical macro list with drift variants, defined acronyms, contribution claims, multi-meaning terms
- Scientific reviewer: core claims, known overclaiming risks, evaluation setup, baselines, datasets, and metrics
- Implementation checker: reference paths and key non-obvious technical facts that are easy to misstate

All memory files must use the frontmatter format with `name`, `description`, `type: project`.

### Phase 4 — Update MEMORY.md Indices

For each agent that received new or updated files, update `MEMORY.md` with pointer lines.

### Phase 5 — Report

Report: files written or updated, facts extracted (macro count, acronym count, contribution count), and any unfilled `<!-- CUSTOMIZE -->` placeholders found.

## Constraints

- Do not overwrite memory content more specific than what was extracted.
- Do not record `<!-- CUSTOMIZE -->` placeholder text as facts — report them as gaps.
- If a section file is missing, note it and continue.
