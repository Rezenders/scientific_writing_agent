---
name: full-manuscript-audit
description: Use when preparing for submission or after a major revision cycle to run a complete audit of the manuscript across all sections. Orchestrates consistency, scientific review, and (optionally) implementation checking in a structured multi-phase workflow. Use before /pre-submission to catch issues early.
---

# Full Manuscript Audit

Full-manuscript pre-submission audit. Orchestrates all review agents across every section and produces a unified go/no-go report.

## When to Use

- Before submission or resubmission
- After a major revision cycle affecting multiple sections
- When starting a new writing session after a long break
- As the final step before running `/pre-submission`

## Inputs Required

Tell Claude:
1. **Scope**: "full manuscript" or a list of specific sections to prioritize
2. **Focus** (optional): known risk areas (e.g. "pay extra attention to evaluation claims" or "check all comparisons with the baseline")

## Workflow

### Phase 1 — Annotation Inventory

Run `/find-annotations` to get a complete list of open todos, author comments, and revision markers across the manuscript.

Report: how many open annotations exist, which sections have the most, and whether any are in blocking positions (near key claims or marked for attention).

---

### Phase 2 — Full Consistency Audit

Invoke `consistency-auditor` with scope: full manuscript.

Ask it to check:
- Macro and terminology drift across all section files
- Acronym consistency (first use, expansion, subsequent use)
- Contribution-statement alignment (introduction vs. body vs. conclusion)
- Ambiguous terminology that has multiple meanings in the paper
- Cross-section contradictions in claims

---

### Phase 3 — Section-by-Section Scientific Review

For each section in order, invoke `scientific-paper-reviewer`:

Ask: "Review for clarity, redundancy, claim precision, paragraph flow, and alignment with neighbouring sections. Flag critical issues only — skip minor style notes for speed."

Sections to cover (adapt to your document structure):
- Introduction
- Background / Related Work
- Model / Method / Approach
- Framework / System / Architecture
- Implementation (if present)
- Evaluation / Experiments / Results
- Discussion
- Conclusions

---

### Phase 4 — Implementation Spot-Check *(optional)*

If the paper describes a codebase, invoke `paper-implementation-checker` on the highest-risk claims:
- How key data structures or algorithms are represented
- Trigger conditions or control flow described in prose
- Any claim in the Evaluation section about system behavior or performance

Skip this phase if `paper-implementation-checker` is not configured.

---

### Phase 5 — Unified Report

Combine all findings:

```
## Full Manuscript Audit

### Open Annotations
[Count and location summary from Phase 1]

### Critical Issues (block submission)
[Merged from Phases 2–4, deduplicated, ordered by section]

### Medium Issues (should fix)
[Merged from Phases 2–4]

### Per-Section Verdicts
| Section | Verdict |
|---|---|
| Introduction | READY / NEEDS REVISION / MAJOR ISSUES |
| ... | ... |

### Implementation Claims (if Phase 4 ran)
[Findings]

### Recommended Fix Order
1. [Most urgent — file:line]
2. ...

### Overall Verdict
GO | CONDITIONAL GO | NO-GO
```

## Constraints

- Do not edit any files during this workflow.
- Do not propose rewrites inline — use `/write-to-intent` or `/technical-paragraph-rewrite` after this audit to address findings.
- If the manuscript is large, prioritize Phase 2 and Phase 4; Phase 3 can be scoped to sections with open annotations or recent revisions.
- Related skills: `/section-review` for a single section, `/pre-submission` for the final submission checklist.
