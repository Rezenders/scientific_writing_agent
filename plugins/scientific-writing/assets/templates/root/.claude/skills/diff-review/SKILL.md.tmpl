---
name: diff-review
description: Use after making targeted edits to one or more manuscript files to review only what changed — not the whole section. Runs consistency and scientific review scoped to the diff, checking for new inconsistencies introduced, claims that now need evidence, and prose that broke from surrounding context. Much faster than /section-review for small incremental edits.
---

# Diff Review

Targeted review of manuscript changes. Scopes the review to what actually changed rather than auditing the entire section. Faster and more precise than `/section-review` for incremental edits.

## When to Use

- After editing one or more passages in response to a reviewer comment
- After a writing session, before committing to git
- When you want fast feedback on a specific change without a full section audit

## Not For

- First-draft review of a newly written section → use `/section-review`
- Pre-submission audit of the full manuscript → use `/full-manuscript-audit`
- When the diff spans most of a section → use `/section-review` instead

## Inputs Required

Provide one of:
1. **Auto** (default): nothing — Claude runs `git diff` and parses it
2. **Staged only**: say "staged" — Claude runs `git diff --cached`
3. **Specific range**: a commit ref or range (e.g. `HEAD~1`, `abc123..HEAD`)
4. **Manual**: paste the diff directly if not in a git repo

---

## Workflow

### Phase 1 — Get and Parse the Diff

Run `git diff` (or the specified variant) to obtain the current changes.

For each changed hunk, extract:
- File name and line range
- Removed text (what it said before)
- Added text (what it says now)
- Surrounding unchanged lines (±5 lines for context)

Skip non-manuscript file changes. Note `.bib` changes separately but do not run prose review on them.

If the diff is very large (more than 20 hunks), warn the user and suggest running `/section-review` on the affected section(s) instead.

---

### Phase 2 — Targeted Consistency Audit

For each changed passage, invoke `consistency-auditor` with:
- The added text
- The ±5 lines of surrounding context

Ask: "Does this change introduce any new terminology drift, macro drift, acronym inconsistency, or contradiction with the rest of the manuscript? Report **only issues introduced or made worse by this specific change**. File:line evidence required. Do not report pre-existing issues in the surrounding unchanged text."

---

### Phase 3 — Targeted Scientific Review

For each changed passage, invoke `scientific-paper-reviewer` with:
- The removed text (what it said before)
- The added text (what it says now)
- The surrounding context

Ask: "Does this change introduce new clarity issues, redundancy, overclaiming, weakened precision, or broken paragraph flow? Does the addition disconnect from the preceding or following context? Focus on what changed — do not re-review stable surrounding text."

---

### Phase 4 — Report

```
## Diff Review

### Changes reviewed
- sections/method.tex: 2 hunks (lines 88–97, 201–210)
- sections/evaluation.tex: 1 hunk (lines 45–52)

### Consistency
[Findings with file:line evidence, or CLEAN]

### Scientific quality
[Findings with file:line evidence, or CLEAN]

### Verdict
CLEAN | MINOR ISSUES | NEEDS ATTENTION

### Recommended actions
1. [Most urgent issue — file:line]
2. ...
```

Only flag issues introduced or made worse by the changes. Do not report pre-existing issues in unchanged text.

---

## Constraints

- Review only what changed. Do not report pre-existing issues in unchanged text.
- If a change is purely formatting (whitespace, line breaks, macro renaming with no semantic effect), note it and skip prose review.
- Do not propose inline rewrites — use `/write-to-intent` or `/address-reviewer-comment` to address any findings.
- If the diff is very large (>20 hunks), warn the user and suggest `/section-review` instead.

---

## Invocation Example

```
/diff-review
```

Or with a specific range:

```
/diff-review HEAD~2..HEAD
```
