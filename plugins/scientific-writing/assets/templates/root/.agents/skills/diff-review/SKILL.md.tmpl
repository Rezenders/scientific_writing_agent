---
name: diff-review
description: Use after targeted manuscript edits to review only what changed. Scopes consistency and scientific review to the diff. Faster than /section-review for incremental edits.
---

# Diff Review

Targeted review of manuscript changes. Reviews only what changed in the diff, not the full section.

## Inputs

Provide the diff as:
- Run `git diff` (or `git diff --cached` for staged changes) and paste the output
- Or specify a commit range (e.g. `HEAD~1`)
- Or paste the diff directly

## Workflow

### Phase 1 — Parse Diff

Extract changed hunks with ±5 lines of surrounding context. Identify affected files and line ranges. Skip non-manuscript files. If the diff is very large (>20 hunks), warn and suggest `/section-review` instead.

### Phase 2 — Targeted Consistency Audit

Use `.agents/agents/consistency-auditor.md` on each changed passage with context. Ask: does this change introduce new terminology drift, macro drift, acronym inconsistency, or contradiction? Pay particular attention to required macros versus free-text variants, project-name consistency, baseline framing, and terminology rules in `.agents/context/terminology.md`. Report only issues introduced or worsened by this change — not pre-existing issues in unchanged text.

### Phase 3 — Targeted Scientific Review

Use `.agents/agents/scientific-paper-reviewer.md` on each changed passage (before + after + context). Ask: does this change introduce new clarity issues, overclaiming, weakened precision, or broken context? Focus only on what changed.

### Phase 4 — Report

Report: files and hunks reviewed, consistency findings, scientific findings, CLEAN / MINOR ISSUES / NEEDS ATTENTION verdict, and recommended actions.

## Optional grammar focus

When the author requests focused grammar diagnosis, use
`.agents/skills/scientific-grammar-review/SKILL.md` on the relevant passage with
context. Do not add a grammar pass by default. Merge duplicate diagnoses and
preserve this workflow's report, scope, and human findings gate. Return structural
recommendations separately; do not supply a rewritten passage or pass unapproved
findings to the writer.

## Constraints

- Review only what changed. Do not report pre-existing issues in unchanged text.
- Do not propose inline rewrites — use `/write-to-intent` or `/address-reviewer-comment` for fixes.
