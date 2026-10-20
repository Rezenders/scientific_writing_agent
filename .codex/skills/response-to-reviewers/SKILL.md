---
name: response-to-reviewers
description: Use when preparing a formal response letter for a journal or conference resubmission. Takes the full review and produces a structured response letter with per-comment responses and manuscript edit proposals. Nothing modifies a file without explicit user approval.
---

# Response to Reviewers

Full resubmission response workflow for journal/conference reviews.

## Workflow

### Phase 0 — Parse and Categorize

Parse all reviewer comments into a structured inventory with IDs (R1.1, R1.2, R2.1…), category (technical / writing / consistency / scope / question), and identified manuscript location. Present inventory to user for confirmation before continuing.

### Phase 1 — Technical Verification *(technical comments only)*

Use `.agents/agents/paper-implementation-checker.md` on technical claims.

Implementation reference paths:
- Primary implementation artifact: `<IMPLEMENTATION_REFERENCE>`
- Experiment or analysis scripts: `<IMPLEMENTATION_REFERENCE>`
- Generated data/tables: `<IMPLEMENTATION_REFERENCE>`
- Public interfaces, schemas, or configuration: `<IMPLEMENTATION_REFERENCE>`

Surface DIVERGES findings to the user before drafting responses.

### Phase 2 — Draft Responses

Use `.agents/agents/writer.md` to draft a response per comment: (1) acknowledge, (2) state action taken, (3) point to manuscript location, (4) quote revised text if short. Also propose the manuscript edit. Do not modify files.

### Phase 3 — Consistency Check

Use `.agents/agents/consistency-auditor.md` on all proposed edits in aggregate. Pay attention to required macros versus free-text variants, project-name consistency, baseline framing, and terminology rules in `.agents/context/terminology.md`.

### Phase 4 — Assemble Letter

Produce the complete response letter: cover paragraph thanking reviewers, then per-reviewer / per-comment structure — original comment quoted, response, manuscript location.

### Phase 5 — Hold for Approval

Present the full letter and all proposed manuscript edits labelled by comment ID. Do not modify any file until the user explicitly approves each edit.

## Constraints

- Never modify files before explicit approval.
- Do not fabricate manuscript locations — flag uncertainty instead.
- Do not add citations not in the bibliography.
- Do not silently weaken limitations or strengthen claims to satisfy a reviewer.
- Preserve all canonical LaTeX macros (`<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, `<KEY_MACRO>`, etc.) in proposed edits.
