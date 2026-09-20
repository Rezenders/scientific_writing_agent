# CLAUDE.md

This file provides guidance to Claude Code when working in this repository. The shared, harness-independent workflow source is `.agents/`.

## Canonical Workflow Layer

- `.agents/agents/` contains shared agent role instructions.
- `.agents/skills/` contains shared manuscript workflows.
- `.agents/context/` contains focused project context templates and project-specific guardrails.
- `.claude/`, `.codex/`, and `.pi/` are adapters only. Preserve harness-specific settings and plugin metadata, but avoid divergent workflow copies.

When updating workflows, edit `.agents/` first and then relink or regenerate harness adapters if needed.

## Purpose

This repository is a reusable scientific-writing agent template for LaTeX research papers. Downstream projects should replace placeholders such as `<PROJECT_NAME>`, `<MAIN_TEX>`, `<SECTION_FILE>`, `<KEY_MACRO>`, `<IMPLEMENTATION_REFERENCE>`, and `<EVALUATION_CLAIM>` with paper-specific facts.

The goal is to support technically rigorous, internally consistent, publication-ready scientific manuscripts without changing intended technical meaning.

## Human-Controlled Writing Workflow

For substantive drafting or rewriting:

1. establish an explicit passage contract using `.agents/context/passage-contract.md`;
2. optionally create an argument plan;
3. produce one primary draft;
4. run read-only diagnostic review when needed;
5. ask the human to accept, reject, or modify findings;
6. perform at most one targeted revision from accepted findings;
7. run final diff, consistency, and build checks.

Reviewer and critic agents diagnose only; they do not rewrite. Do not feed unapproved findings to the writer and do not run automatic repeated critique/rewrite loops.

## Editing Priorities

1. technical correctness;
2. consistency with the manuscript;
3. clarity and precision;
4. concise academic style;
5. grammar and fluency.

## Writing Style

Use formal scientific English, precise terminology, and direct declarative sentences. Prefer “This work proposes X to achieve Y” for contributions and “This work uses X” for tool use. Avoid conversational wording, promotional tone, vague intensifiers, and unnecessary variation. Preserve LaTeX macros, labels, references, citations, equations, and established terminology unless a change is necessary and justified.

## Focused Context

Use `.agents/context/manuscript-context.md` as the compact index. Load focused files only when relevant: `paper-model.md`, `terminology.md`, `contributions.md`, `evaluation-claims.md`, `claim-ledger.md`, `do-not-say.md`, `open-findings.md`, `reviewer-contracts.md`, and `passage-contract.md`.

## Technical Content Rules

Do not invent claims, assumptions, results, citations, or implementation details. Do not silently strengthen claims or weaken limitations. If manuscript text conflicts with implementation or evidence, report the discrepancy rather than silently changing either side.

## Validation

Before editing, inspect the target file and search for related definitions, claims, and terminology. After substantive manuscript edits, run the build and lint commands documented in `.agents/context/paper-model.md` or the local build system when available. Report build errors, undefined references, missing citations, and newly introduced warnings.

## Adapter and Plugin Metadata

Do not delete Claude plugin, marketplace, or adapter metadata without verifying its purpose. Workflow content should remain canonical in `.agents/`; packaging metadata may remain in `.claude-plugin/`, `.claude/`, `.agents/plugins/`, or `plugins/` as required by distribution tooling.
