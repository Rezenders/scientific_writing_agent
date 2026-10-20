---
name: bootstrap-project-context
description: Use immediately after installing the scientific-writing workflow to interview the user, inspect the manuscript, and fill the `.agents/context/` templates with project-specific facts before writing or review work begins.
---

# Bootstrap Project Context

Use this skill after `scientific_writing_agent.py install` and before `bootstrap-memory`, `write-to-intent`, or substantive review workflows.

This skill is an interactive setup workflow. Its purpose is to replace generic placeholders in `.agents/context/` with author-approved project facts. Do not invent missing scientific content.

## Goals

Populate or update these focused context files:

- `.agents/context/manuscript-context.md`
- `.agents/context/paper-model.md`
- `.agents/context/terminology.md`
- `.agents/context/contributions.md`
- `.agents/context/evaluation-claims.md`
- `.agents/context/claim-ledger.md`
- `.agents/context/do-not-say.md`
- `.agents/context/reviewer-contracts.md` when reviews exist

Leave `.agents/context/open-findings.md` empty or initialized unless there are known unresolved findings.

## Workflow

### Phase 1 — Inspect Existing Project Evidence

Before asking questions, inspect the repository for available facts:

1. Locate the manuscript entry point (`<MAIN_TEX>`) by checking common names such as `main.tex`, `paper.tex`, `main-acm.tex`, and files containing `\documentclass`.
2. Read the entry point and identify `\input` / `\include` section files.
3. Inspect macro/config files when obvious, such as `macros.tex`, `preamble.tex`, `config/macros.tex`, or files included before `\begin{document}`.
4. Inspect `Makefile`, `latexmkrc`, CI files, or README build instructions for build and lint commands.
5. Scan the abstract, introduction, conclusion, and evaluation/results sections when available for contribution and evaluation claims.
6. Check for existing `AGENTS.md`, `CLAUDE.md`, reviewer-response files, or project notes.

Report the facts inferred from repository evidence and clearly mark uncertain items.

### Phase 2 — Ask a Minimal Questionnaire

Ask only for information not inferable from the repository or requiring author confirmation.

Use this questionnaire, omitting questions already answered by evidence:

```text
1. Project name and short paper title?
2. Venue or format target, if any?
3. Main TeX entry point and expected PDF output path?
4. Build, lint, and optional diff-lint commands?
5. Active section files and their roles?
6. Canonical system/method/dataset/baseline/metric names and required macros?
7. Key terminology distinctions that must not be blurred?
8. Approved contribution statements?
9. Evaluation claims that are supported by the current evidence?
10. Claims or phrasings the paper must avoid?
11. Does the paper depend on an implementation, dataset, or analysis pipeline? If yes, what paths are read-only ground truth?
12. Are there current reviewer comments, open findings, or response contracts to track?
```

Do not continue to write context files until the user has confirmed materially important answers, especially contribution scope, evaluation claims, and implementation references.

### Phase 3 — Draft Context Updates

Prepare proposed updates for the context files. Preserve useful existing project-specific content. Replace placeholders only when evidence or user answers support the replacement.

Use conservative wording:

- mark uncertain facts as `TBD` or `Requires author confirmation`;
- keep claims evidence-bounded;
- distinguish manuscript facts from implementation facts;
- do not add unsupported evaluation conclusions;
- do not encode temporary guesses as durable context.

### Phase 4 — Human Approval Before Editing

Show a concise summary of proposed context changes and ask for approval before modifying files unless the user explicitly requested direct edits.

After approval, edit only `.agents/context/` files and, if needed, append a short policy reminder to `AGENTS.md` or `CLAUDE.md`. Do not modify manuscript `.tex` files in this skill.

### Phase 5 — Validate Setup

After editing:

1. Run `python3 /path/to/scientific_writing_agent/scripts/scientific_writing_agent.py doctor --repo-root .` when the installer is available, or manually verify equivalent checks.
2. Search `.agents/context/` for remaining placeholders: `<PROJECT_NAME>`, `<MAIN_TEX>`, `<SECTION_FILE>`, `<KEY_MACRO>`, `<IMPLEMENTATION_REFERENCE>`, `<EVALUATION_CLAIM>`.
3. Report remaining placeholders that are intentional or still need author input.
4. Recommend running `bootstrap-memory` only after core context files are populated.

## Output Format

```text
## Bootstrap Project Context

### Inferred from repository
- ...

### Needs author confirmation
1. ...

### Proposed context updates
- `.agents/context/paper-model.md`: ...
- `.agents/context/terminology.md`: ...

### Remaining gaps
- ...

### Next step
Run `bootstrap-memory` after approving these context files, or start a writing/review workflow if no additional memory step is needed.
```

## Constraints

- Do not invent project facts.
- Do not overwrite existing project-specific context without preserving or explicitly replacing it.
- Do not edit manuscript source files.
- Do not run writing/review loops during setup.
- Do not treat placeholders as facts.
