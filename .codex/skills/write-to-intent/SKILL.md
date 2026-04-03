---
name: write-to-intent
description: Use when you want to write or substantially rewrite a manuscript paragraph or short passage toward a stated goal — a framing, claim, or rhetorical function the passage should accomplish. Not for minor edits or for responding to a specific reviewer comment.
---

# Write to Intent

Multi-step workflow that turns a writing goal into 2 to 3 refined manuscript proposals without touching the file until the user explicitly approves.

## Inputs Required

Provide:

1. Goal
2. Target
3. Context
4. Constraints, optional

## Phase 0 - Clarifying Questions

Ask the user:

1. What is the rhetorical function of this passage?
2. Who is the implied reader at this point in the paper?
3. Are there specific terms, concepts, or examples from the manuscript that must appear?
4. Are there any claims this passage must not make?
5. Does the passage introduce new technical claims?

## Workflow

### Phase 1a - Optional Implementation Check

Use `.codex/agents/paper-implementation-checker.md` if the passage introduces or restates a technical claim about system behavior.

### Phase 1b - Writer Directions

Use `.codex/agents/writer.md` to propose 2 to 3 distinct ways to approach the passage. Stop and ask the user which to develop.

### Phase 2 - Writer Full Drafts

Use `.codex/agents/writer.md` to produce a full draft for each selected approach.

### Phase 3 - Parallel Review

Use `.codex/agents/scientific-paper-reviewer.md` and `.codex/agents/consistency-auditor.md`.

### Phase 4 - Writer Refined Proposals

Use `.codex/agents/writer.md` to refine the drafts based on review feedback.

### Phase 5 - Hold for Approval

Present all refined proposals and stop. Do not edit the manuscript file until the user explicitly selects or approves a proposal.
