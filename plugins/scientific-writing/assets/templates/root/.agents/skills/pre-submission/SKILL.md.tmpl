---
name: pre-submission
description: Use when preparing a scientific manuscript for submission and you need a structured go or no-go checklist.
---

# Pre-Submission Checklist

Run this checklist in order. This skill is diagnostic only.

## Required Sequence

1. Run `paper-build`.
2. Run `find-annotations`.
3. Use `.agents/agents/consistency-auditor.md` for a full pass across the active manuscript sections.
4. Use `.agents/agents/paper-implementation-checker.md` for targeted spot-checks on the highest-risk technical claims, if the project has implementation-dependent claims.

## Consistency Audit Scope

Audit the active section files listed in `.agents/context/paper-model.md` or included by `<MAIN_TEX>`.

Focus on:

- macro drift
- terminology drift
- acronym consistency
- notation mismatches
- alignment between contribution statements and the body

Use an explicit prompt such as:

```text
Perform a full consistency audit across the active section files listed in `.agents/context/paper-model.md`. Focus on macro drift, terminology drift, acronym consistency, notation mismatches, and contribution-statement alignment between the introduction and body.
```

## Implementation Spot-Check Targets

Prioritize 3 to 5 high-risk claims, typically including:

- runtime or algorithmic behavior;
- interface, schema, or data-processing details;
- experiment scripts, datasets, metrics, or generated tables;
- any explicit artifact names, parameter values, or action names cited in the paper.

Ask the checker to report `CONSISTENT`, `DIVERGES`, or `CANNOT_VERIFY`.

Use `.agents/agents/paper-implementation-checker.md` rather than inventing an ad hoc check, and ask it to verify 3 to 5 claims with prompts such as:

```text
Does this description match the current implementation? Report CONSISTENT / DIVERGES / CANNOT_VERIFY.
```

## Pass And Fail Rules

- Do not edit files while running this checklist.
- Do not return `GO` if any step fails.
- If the build environment is unavailable, report that limitation explicitly and mark the affected step accordingly.
- Treat open `\todo`, `\red`, and author comment macros in active manuscript files as blocking.
- Treat `\hide` entries in active manuscript files as requiring author review even if they are not rendered.
- Report `old/` annotation matches separately and do not let them block submission unless the user explicitly asks to include archival content.

## Final Report

The final report must include:

- build status
- lint status
- annotation count
- consistency status
- implementation-alignment status
- final verdict: `GO` or `NO-GO`

Recommended format:

```text
## Pre-Submission Report

| Step | Status | Notes |
|---|---|---|
| Build | PASS / FAIL / SKIPPED | |
| Lint | PASS / FAIL / SKIPPED | |
| Annotations | PASS / FAIL | N open |
| Consistency | PASS / FAIL | |
| Implementation | PASS / FAIL | |

### Verdict: GO / NO-GO
```
