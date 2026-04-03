---
name: address-reviewer-comment
description: Use when a reviewer comment targets a specific paragraph or section and requires a written response that may lead to manuscript edits. Never modify the file without explicit user approval.
---

# Address Reviewer Comment

Multi-step workflow for responding to reviewer comments without editing the manuscript before the user approves a proposal.

## Inputs Required

Provide:

1. Comment or comments quoted verbatim
2. Target file and line range
3. Preceding and following paragraph context
4. Optional comment type: `technical`, `writing`, `consistency`, or `mixed`

## Workflow

### Phase 0 - Implementation Check

Skip this phase for purely writing or consistency comments.

Use `.codex/agents/paper-implementation-checker.md` to verify whether the challenged technical claim matches the implementation.

| What to verify | Where to look |
|---|---|
| Type names, data structures, schemas | `<path>` |
| Running examples | `<path>` |
| Runtime behavior, interface method names | `<path>` |
| Design intent / documentation | `<path>` |

### Phase 1 - Writer Directions

Use `.codex/agents/writer.md` to propose 2 to 3 distinct revision directions. Each direction should be a short strategy paragraph, not a full rewrite.

Stop and ask the user which direction to develop.

### Phase 2 - Full Proposals

Use `.codex/agents/writer.md` to produce a full rewrite for each selected direction. Preserve all LaTeX macros, references, citations, labels, and math environments verbatim.

### Phase 3 - Parallel Review

Review the proposals with:

- `.codex/agents/scientific-paper-reviewer.md`
- `.codex/agents/consistency-auditor.md`

If the user explicitly asks for parallel agent work, delegate these reviews in parallel. Otherwise perform the two reviews sequentially.

### Phase 4 - Refined Proposals

Use `.codex/agents/writer.md` again to refine the proposals based on the review feedback.

### Phase 5 - Hold For Approval

Present the refined proposals as `Proposal 1`, `Proposal 2`, and `Proposal 3`.

Do not edit the manuscript until the user explicitly selects or approves a proposal.
