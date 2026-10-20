# AGENTS.md

This file provides repository policy for Codex-style agents. The harness-independent workflow source is `.agents/`.

## Canonical Workflow Layer

- `.agents/agents/` contains shared agent role instructions.
- `.agents/skills/` contains shared manuscript workflows.
- `.agents/context/` contains focused project context templates and project-specific guardrails.
- `.claude/`, `.codex/`, and `.pi/` are adapters only. Keep harness-specific settings and plugin metadata there, but do not maintain divergent workflow copies.

When updating workflows, edit `.agents/` first. Use generated mirrors for harnesses that require a specific directory layout. Avoid symlinks in Overleaf-compatible repositories.

## What This Repository Is

This repository is a reusable scientific-writing agent template for LaTeX research papers. Downstream paper projects should replace placeholders such as `<PROJECT_NAME>`, `<MAIN_TEX>`, `<SECTION_FILE>`, `<KEY_MACRO>`, `<IMPLEMENTATION_REFERENCE>`, and `<EVALUATION_CLAIM>` with project-specific facts.

The goal is to support technically rigorous, internally consistent, publication-ready scientific manuscripts. Edits must improve clarity, precision, coherence, and argument strength without changing intended technical meaning.

## Editing Priorities

Apply these priorities in order:

1. technical correctness;
2. consistency with the manuscript;
3. clarity and precision;
4. concise academic style;
5. grammar and fluency.

Do not optimize prose elegance at the expense of precision.

## Human-Controlled Writing Workflow

For substantive drafting or rewriting, preserve this workflow:

1. establish an explicit passage contract using `.agents/context/passage-contract.md`;
2. optionally create an argument plan for complex rhetorical work;
3. produce one primary draft;
4. run read-only diagnostic review when needed;
5. ask the human to accept, reject, or modify findings;
6. perform at most one targeted revision from accepted findings;
7. run final diff, consistency, and build checks.

Reviewer and critic agents diagnose only. They do not rewrite. Do not feed unapproved reviewer findings to the writer. Do not run automatic repeated critique/rewrite loops.

## Writing Style

- Use formal scientific English.
- Prefer precise terminology over stylistic variation.
- Prefer direct, declarative sentences.
- Prefer “This work proposes X to achieve Y” for contributions.
- Prefer “This work uses X” over vague role-based phrasing.
- Avoid conversational wording, promotional tone, vague intensifiers, and decorative flourish.
- Avoid redundancy across adjacent sentences and paragraphs.
- Preserve established manuscript terminology unless there is a strong reason to change it.
- Preserve LaTeX macros, labels, references, citations, and equations unless a change is necessary and justified.

## Focused Context Files

Use `.agents/context/manuscript-context.md` as the compact index. Load only relevant focused files:

- `paper-model.md` for repository layout, sections, validation commands, and implementation references;
- `terminology.md` for canonical terms, acronyms, macros, and distinctions;
- `contributions.md` for approved contribution scope;
- `evaluation-claims.md` for result claims and evidence boundaries;
- `claim-ledger.md` and `do-not-say.md` for high-risk claims and prohibited phrasings;
- `open-findings.md` and `reviewer-contracts.md` for unresolved diagnostics and review-response plans.

## Technical Content Rules

- Do not add technical claims, assumptions, results, or citations unless supported by manuscript context or explicitly requested.
- Do not silently strengthen claims.
- Do not silently weaken limitations.
- Do not invent implementation details.
- If the manuscript and implementation disagree, report the discrepancy instead of silently changing either side.

## LaTeX Handling

- Keep LaTeX syntax valid.
- Do not break environments, labels, references, bibliography commands, macros, or math notation.
- Preserve comments unless they are obsolete or explicitly targeted.

## Validation

Before editing, inspect the target file and search for related terminology, definitions, and claims. After substantive manuscript edits, run the project’s build and lint commands from `.agents/context/paper-model.md` or the local `Makefile` when available. Report errors, undefined references, missing citations, and warnings introduced by the change.

## Plugin and Adapter Metadata

Do not delete plugin, marketplace, or adapter metadata without verifying its purpose. Workflow content belongs in `.agents/`; packaging metadata may remain under `.agents/plugins/`, `.claude-plugin/`, `.claude/`, `.codex/`, or `plugins/` as required by distribution tooling.
