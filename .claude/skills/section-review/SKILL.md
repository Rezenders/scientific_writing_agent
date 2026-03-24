---
name: section-review
description: Use when a full section has been written or substantially rewritten and needs a combined scientific review and consistency check against the rest of the manuscript.
---

# Section Review

Section-level multi-agent review. Different from `/technical-paragraph-rewrite` (which works at paragraph level and produces rewrite suggestions): this skill audits a full section for scientific quality and manuscript-wide consistency, and reports findings without modifying anything.

## When to Use

- After rewriting a full section
- Before handing a section to a co-author
- As part of `/pre-submission` for high-risk sections
- When you suspect a section has drifted from the rest of the paper

## Inputs Required

Tell Claude:
1. **Target section**: the file and section name/heading
2. **Neighbouring sections**: what comes immediately before and after (file names or section names)
3. **Focus** (optional): any specific concerns (e.g. "check that the contributions still match", "verify the notation is consistent with Section 2")

## Workflow

### Phase 1 — Scientific Review

Invoke `scientific-paper-reviewer` with:
- The full target section text
- The neighbouring section context (preceding and following)

Ask: "Review this section across all five dimensions: local clarity, redundancy, claim precision, paragraph flow, and alignment with neighbouring sections. Flag critical issues first."

---

### Phase 2 — Consistency Audit

Invoke `consistency-auditor` targeted at the section:

Ask: "Audit this section against the rest of the manuscript for: terminology drift, acronym consistency, notation mismatches, and contribution-statement alignment. Report findings with file:line evidence from both the section and the conflicting location."

---

### Phase 3 — Unified Report

Combine findings from both phases into a single report:

```
## Section Review: [Section Name]

### Scientific Quality
[Findings from Phase 1 — grouped by dimension]

### Manuscript Consistency
[Findings from Phase 2 — grouped by issue type]

### Priority Actions
1. [Most urgent issue]
2. ...

### Verdict
READY / NEEDS REVISION / MAJOR ISSUES
```

## Constraints

- Do not edit any files. Report only.
- Do not propose rewrites inline — for rewrite suggestions, use `/technical-paragraph-rewrite` on specific paragraphs after this review.
- If neighbouring sections are not provided, note that alignment cannot be fully assessed.
