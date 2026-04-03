---
name: write-to-intent
description: Use when you want to write or substantially rewrite a manuscript paragraph or short passage toward a stated goal — a framing, claim, or rhetorical function the passage should accomplish. Not for minor edits; not for responding to a specific reviewer comment.
---

# Write to Intent

## Overview

Multi-agent pipeline that turns a writing goal ("I want this paragraph to establish X") into 2-3 refined manuscript proposals — without touching the file until the user explicitly approves.

Differs from `/technical-paragraph-rewrite` (which checks accuracy and fixes an existing paragraph) and `/address-reviewer-comment` (which responds to a specific critique). This skill starts from what you want the paragraph to **do**.

## When to Use

- You want a new paragraph or subsection intro with a specific framing
- You want to substantially rewrite an existing paragraph toward a new rhetorical goal
- You have rough notes or a sketch and want manuscript-ready prose
- You want to explore several ways of making the same argument

**Not for:** minor wording fixes, responding to a reviewer, or accuracy-checking an existing paragraph.

---

## Inputs Required

Provide:
1. **Goal**: what should this passage establish, argue, or introduce? (one or two sentences is enough)
2. **Target**: file and line range (existing passage to rewrite, or insertion point for new text)
3. **Context**: the preceding and following paragraph(s) — paste text or give file:line
4. **Constraints** (optional): terminology to preserve, claims to avoid, mandatory content

---

## Phase 0 — Clarifying Questions

**Claude asks the user the following before any agent runs.** Do not skip.

1. What is the rhetorical function of this passage? (e.g., motivate, define, bridge, summarize, introduce)
2. Who is the implied reader at this point in the paper? (expert in the subfield? broad audience?)
3. Are there specific terms, concepts, or examples from the manuscript that must appear?
4. Are there any claims this passage must NOT make (to avoid overstating or conflicting with elsewhere)?
5. Does the passage introduce new technical claims? (if yes, Phase 1a — implementation check — may be needed)

**Wait for the user's answers before proceeding.**

---

## Phase 1a — Optional: Implementation Check

> **Only if** the passage introduces or restates a technical claim about system behavior.
>
> <!-- OPTIONAL: Only run this phase if your paper has an associated software implementation
>      and you have configured the paper-implementation-checker agent. -->

Invoke `paper-implementation-checker` with:
- The intended claim (from the user's goal + clarification answers)
- The most relevant implementation file

<!-- CUSTOMIZE: Fill in your implementation reference paths -->
| What to verify | Where to look |
|---|---|
| Type names, data structures, schemas | `<path>` |
| Running examples | `<path>` |
| Runtime behavior, interface method names | `<path>` |
| Design intent / documentation | `<path>` |

> If DIVERGES: surface the conflict to the user before continuing. Do not silently write around it.

---

## Phase 1b — Writer: Approach Directions

Invoke `writer` with:
- The stated goal and all clarification answers
- The target passage and surrounding context
- Phase 1a findings (if applicable)

Ask: "Propose 2-3 distinct ways to approach this passage. For each, write one sentence describing the strategy — not a full draft. Label them Approach A, B, C."

**USER GATE — stop here.** Present the approaches and ask the user which to develop. Do not continue until the user responds.

---

## Phase 2 — Writer: Full Drafts

Invoke `writer` with:
- The stated goal and clarification answers
- The selected approach(es)
- The target passage and surrounding context
- Phase 1a findings (if applicable)

Ask: "Produce a full draft for each selected approach. Preserve all LaTeX macros, `\ref`, `\cite`, labels, and math environments verbatim.
<!-- CUSTOMIZE: List your project-specific macros here so the writer knows to preserve them.
     Example: Preserve macros such as \approachname, \systemname, \metricname, etc. -->
Do not modify the file."

---

## Phase 3 — Parallel Review

Invoke `scientific-paper-reviewer` and `consistency-auditor` **in parallel**, both receiving:
- The stated goal
- All Phase 2 drafts
- The surrounding context

`scientific-paper-reviewer`: "Review each draft for claim precision, clarity, paragraph flow, and alignment with the stated rhetorical goal and the manuscript's style. Which is strongest? Flag remaining issues in each."

`consistency-auditor`: "Audit each draft against the rest of the manuscript for terminology drift, acronym consistency, notation mismatches, and alignment with the stated contributions. Report findings with file:line evidence."

---

## Phase 4 — Writer: Refined Proposals

Invoke `writer` with:
- Phase 2 drafts
- Phase 3 findings from both reviewers

Ask: "Refine each draft based on the reviewer and auditor feedback. Produce 2-3 polished proposals. Do not modify the file."

---

## Phase 5 — Hold for Approval

Present all refined proposals, labelled **Proposal 1, 2, 3**, alongside:
- A one-line summary of each proposal's approach
- Any remaining concerns from Phase 3 that were not resolvable

**Stop here. Do not edit the manuscript file until the user explicitly selects or approves a proposal.**

---

## Hard Constraints

- **Never modify the manuscript before user approval.**
- Preserve all LaTeX labels, `\ref`, `\cite`, math environments, and project macros.
- Do not introduce technical claims beyond what the user's goal and the implementation support.
- Do not add citations not already in the bibliography.
- Prefer the established manuscript term over a synonym.

---

## Invocation Example

```
/write-to-intent

Goal: Rewrite the related work subsection intro to motivate why existing
approaches fall short for our problem, setting up our contribution.

Target: related_work.tex:45 (existing intro paragraph)
Context: lines 40–65
```

Clarifying-question answers (fill in before agents run):
1. Rhetorical function: motivate the contribution by identifying a gap
2. Implied reader: domain researcher familiar with the area
3. Must use: [your key terms here]
4. Must NOT claim: [claims that would conflict with elsewhere]
5. New technical claims? No — framing only
