---
name: paper-build
description: Use when validating a scientific manuscript after substantive edits or before review and submission checks.
---

# Paper Build

Build and validate the manuscript using the current repository `Makefile`.

## Workflow

1. Change to `<PROJECT_ROOT>`.
2. Run `make pdf`.
3. Scan build output for fatal LaTeX errors, especially lines beginning with `!`.
4. Report whether the build succeeded.
5. If the build fails, stop and report the error details instead of continuing.
6. If the build succeeds, run `make lint`.
7. Run `make lint-diff` (or `python3 scripts/lint_diff.py`) to determine whether any `chktex` warnings are new relative to `.agents/context/lint-baseline.json`.
8. Report non-suppressed `chktex` warnings grouped by file, and distinguish pre-existing baseline warnings from newly introduced warnings.
9. Report undefined references and missing citations found in build output.

## Commands

```bash
cd <PROJECT_ROOT>
make pdf
make lint
make lint-diff
```

## Repository-Specific Expectations

Customize these in `.agents/context/paper-model.md` for a concrete paper project:

- `<BUILD_COMMAND>` builds `<PDF_OR_ARTIFACT_PATH>`.
- `<LINT_COMMAND>` runs the project's LaTeX or manuscript lint checks.
- `<OPTIONAL_DIFF_LINT_COMMAND>` distinguishes newly introduced warnings from any accepted baseline.
- Update lint baselines only after intentional cleanup or when the user explicitly asks.

## Reporting Requirements

- Build status: `PASS` or `FAIL`
- PDF target status: `<PDF_OR_ARTIFACT_PATH>`
- Fatal LaTeX error details when present
- Undefined references: lines matching `LaTeX Warning: Reference ... undefined`
- Missing citations: lines matching `LaTeX Warning: Citation ... undefined`
- Lint status with warnings grouped by file
- Lint-diff status: `NO NEW WARNINGS` or list of newly introduced warnings

## Constraints

- If the TeX toolchain or `chktex` is unavailable, report that explicitly.
- Do not claim a clean result if the build failed, if undefined references remain, or if missing citations remain.
