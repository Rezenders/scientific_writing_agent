---
name: address-reviewer-comment
description: Use when a reviewer comment (human or agent) targets a specific paragraph or section and requires a written response that modifies manuscript text. Never modifies the file without explicit user approval.
---

# Address Reviewer Comment

## Overview

Multi-agent pipeline that responds to reviewer comments by generating 2-3 candidate revision directions, subjecting full rewrites to parallel scientific and consistency review, and refining the surviving proposals — without touching the file until the user explicitly approves.

Differs from `/technical-paragraph-rewrite`: that skill verifies a paragraph against the implementation and rewrites it. This skill starts from a reviewer comment and works backward to a revision that satisfies the comment while preserving manuscript quality.

## Inputs Required

Provide:
1. **Comment(s)**: quoted verbatim (reviewer comment or finding from `/section-review`)
2. **Target**: file and line range of the affected paragraph/section
3. **Context**: preceding and following paragraph text (paste or cite file:line)
4. **Comment type** (optional — helps skip irrelevant phases):
   - `technical` — challenges a factual claim about the implementation
   - `writing` — clarity, redundancy, flow, precision
   - `consistency` — terminology, notation, acronym
   - `mixed` — multiple types

---

## Workflow

### Phase 0 — Implementation Check (technical comments only)

> **Skip this phase for `writing` or `consistency` comments.**
>
> <!-- OPTIONAL: Only run this phase if your paper has an associated software implementation
>      and you have configured the paper-implementation-checker agent. -->

Invoke `paper-implementation-checker` with:
- The affected paragraph (verbatim)
- The implementation file most relevant to the challenged claim

<!-- CUSTOMIZE: Fill in your implementation reference paths -->
| What to verify | Where to look |
|---|---|
| Type names, data structures, schemas | `<path>` |
| Running examples | `<path>` |
| Runtime behavior, interface method names | `<path>` |
| Design intent / documentation | `<path>` |

Ask: "Does this paragraph accurately describe the implementation? Report CONSISTENT / DIVERGES / CANNOT_VERIFY with file:line evidence."

---

### Phase 1 — Writer: Solution Directions

Invoke `writer` with:
- The comment(s) (verbatim)
- The target paragraph and surrounding context
- Phase 0 findings (if applicable)

Ask: "Propose 2-3 distinct approaches to addressing this comment. For each, write one short paragraph describing the strategy — not a full rewrite. Label them Approach A, B, C. Do not modify the file."

**USER GATE — stop here.** Present the approaches and ask the user which to develop. Do not proceed to Phase 2 until the user responds.

---

### Phase 2 — Writer: Full Proposals

Invoke `writer` with:
- The original paragraph
- The selected approach(es) from Phase 1
- Phase 0 findings (if applicable)

Ask: "Produce a full rewrite for each selected approach. Preserve all LaTeX macros, `\ref`, `\cite`, labels, and math environments verbatim.
<!-- CUSTOMIZE: List your project-specific macros here so the writer knows to preserve them.
     Example: Preserve macros such as \approachname, \systemname, \metricname, etc. -->
Do not modify the file."

---

### Phase 3 — Parallel Review

Invoke `scientific-paper-reviewer` and `consistency-auditor` **in parallel**, each receiving:
- The original paragraph
- All Phase 2 proposals

`scientific-paper-reviewer`: "Review each proposal for claim precision, clarity, and alignment with the manuscript's style and the reviewer's concern. Which is strongest? Flag remaining issues in each."

`consistency-auditor`: "Audit each proposal against the rest of the manuscript for terminology drift, acronym consistency, and notation mismatches. Report findings with file:line evidence."

---

### Phase 4 — Writer: Refined Proposals

Invoke `writer` with:
- The original paragraph
- Phase 2 proposals
- Phase 3 findings from both reviewers

Ask: "Based on the reviewer and auditor feedback, produce 2-3 refined rewrite proposals. Do not modify the file."

---

### Phase 5 — Hold for Approval

Present all refined proposals, labelled **Proposal 1, 2, 3**, alongside:
- Which comment(s) each proposal addresses
- Any remaining concerns from Phase 3 that were not resolvable

**Stop here. Do not edit the manuscript file until the user explicitly selects or approves a proposal.**

---

## Hard Constraints

- **Never modify the manuscript before user approval.**
- Preserve all LaTeX labels, `\ref`, `\cite`, math environments, and project macros.
- Do not introduce technical claims not present in either the original paragraph or the implementation.
- Do not add citations not already in the bibliography.
- Do not change meaning to satisfy a comment; flag the conflict and let the user decide.

---

## Invocation Example

```
/address-reviewer-comment

Comment: "The claim that the system derives 'all nodes transitively reachable'
is imprecise — the graph is directed and reachability is not symmetric."

Target: method.tex:120
Context: (lines 115–130)
Comment type: writing
```
