---
name: section-review
description: Use when a full section has been written or substantially rewritten and needs combined scientific review and consistency checking against the rest of the manuscript.
---

# Section Review

Section-level review workflow. This skill audits a full section and reports findings without modifying files.

## Workflow

### Phase 1 - Scientific Review

Use `.codex/agents/scientific-paper-reviewer.md` on the full section with neighboring context.

### Phase 2 - Consistency Audit

Use `.codex/agents/consistency-auditor.md` on the section against the rest of the manuscript.

### Phase 3 - Unified Report

Combine both phases into a single review report with scientific findings, consistency findings, priority actions, and a verdict.
