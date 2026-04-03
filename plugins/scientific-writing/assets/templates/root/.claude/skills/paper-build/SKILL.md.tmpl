---
name: paper-build
description: Build the manuscript PDF and run chktex lint. Reports LaTeX errors and warnings. Run after any substantive manuscript edit.
disable-model-invocation: true
---

Build and validate the manuscript.

## Usage

```
/paper-build
```

## Steps

<!-- ============================================================
     CUSTOMIZE THIS SKILL before use:
     1. Replace <YOUR_PROJECT_ROOT> with the absolute path to your
        manuscript repository (same value as in the agent files).
     2. Replace <YOUR_OUTPUT_PDF> with the actual output path
        (e.g. build/paper.pdf, out/main.pdf).
     3. If your build command is not `make pdf`, update Step 1.
     4. If your lint command is not `make lint`, update Step 2.
        If you don't use chktex at all, delete Step 2.
     5. In Step 2, list your suppressed warning IDs and reasons —
        copy them from CLAUDE.md's "Building and Validation" section.
     ============================================================ -->

### Step 1 — Build PDF

```bash
cd <YOUR_PROJECT_ROOT>
make pdf 2>&1
```

Scan output for fatal errors (lines starting with `!`). Report:
- **SUCCESS**: `<YOUR_OUTPUT_PDF>` built successfully
- **FAILURE**: the full LaTeX error message, the source file, and the line number

If the build fails, stop here and report the error. Do not proceed to Step 2.

---

### Step 2 — Lint

```bash
make lint 2>&1
```

<!-- CUSTOMIZE: List the warning IDs suppressed in your project and why.
     Copy from CLAUDE.md "Building and Validation" section.
     Example:
       Suppress warnings: 1 (command terminated with space),
                          3 (inter-sentence spacing),
                          8 (dash length) — consistent false positives.
-->

Report any warnings grouped by file. Skip warnings that are suppressed per CLAUDE.md.

- **PASS**: no non-suppressed warnings
- **FAIL**: list each warning with file, line, and warning text

---

### Step 3 — Summary

Report:
- PDF status (OK / FAILED)
- Lint warning count by file (0 = clean)
- Any undefined references: lines matching `LaTeX Warning: Reference .* undefined`
- Any missing citations: lines matching `LaTeX Warning: Citation .* undefined`
