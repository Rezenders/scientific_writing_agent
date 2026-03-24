---
name: pre-submission
description: Use when preparing the manuscript for submission. Runs a structured go/no-go checklist covering build, lint, open annotations, consistency, and (optionally) implementation alignment.
---

# Pre-Submission Checklist

Structured go/no-go pipeline before submitting the manuscript. Run every step in order — do not skip steps even if earlier ones pass.

## Steps

### 1. Build + Lint

Invoke the `/paper-build` skill.

- **Pass**: PDF builds without errors and lint is clean.
- **Fail**: Report all errors and warnings from `/paper-build`. Stop and fix build errors before continuing; lint warnings may be addressed in parallel.

---

### 3. Open Annotations

Invoke the `/find-annotations` skill.

- **Pass**: Zero open annotations in active `.tex` files.
- **Fail**: List all open annotations. Flag `\todo` and `\red` as blocking; `\revise` and author comments as non-blocking unless they indicate unresolved technical questions.

---

### 4. Consistency Audit

Invoke `consistency-auditor` for a full manuscript audit.

Ask: "Perform a full consistency audit across all active section files. Focus on: terminology drift, acronym consistency, contribution-statement alignment, and cross-section contradictions."

- **Pass**: No critical inconsistencies.
- **Fail**: Report all critical and medium-priority findings.

---

### 5. Implementation Alignment Spot-Check (OPTIONAL)

<!-- OPTIONAL: Only run this step if your paper has an associated software implementation
     and you have configured the paper-implementation-checker agent. -->

Invoke `paper-implementation-checker` on the highest-risk claims in the paper (typically 2–3):
- Core type/schema descriptions
- Interface method names cited in the paper
- Running examples in the evaluation or results section

Ask each: "Does this description match the current implementation? Report CONSISTENT / DIVERGES / CANNOT_VERIFY."

- **Pass**: All CONSISTENT.
- **Fail**: Report divergences. Do not silently update either side — flag for author decision.

---

## Final Report Format

```
## Pre-Submission Report

| Step | Status | Notes |
|---|---|---|
| Build | PASS / FAIL | |
| Lint | PASS / FAIL | N warnings |
| Annotations | PASS / FAIL | N open |
| Consistency | PASS / FAIL | N critical issues |
| Implementation | PASS / SKIP / FAIL | N divergences |

### Verdict: GO / NO-GO

**Blocking issues** (must fix before submission):
- ...

**Non-blocking notes** (address if time allows):
- ...
```

## Constraints

- Do not edit any files during this skill — report only.
- Do not mark as GO if any non-optional step is FAIL.
- If the build environment is not available, note it and skip steps that require it.
