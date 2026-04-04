---
name: response-to-reviewers
description: Use when preparing a formal response letter for a journal or conference resubmission. Takes the full review (all reviewers, all comments) and produces a structured response letter with per-comment responses and manuscript edit proposals. Nothing is written to file without explicit user approval. Differs from /address-reviewer-comment, which handles one comment in isolation.
---

# Response to Reviewers

Full resubmission workflow. Generates a formal response-to-reviewers letter covering all reviewer comments, with per-comment responses, action summaries, and manuscript edit proposals. Nothing is written to file until you explicitly approve.

## When to Use

- After receiving a major or minor revision decision from a journal or conference
- When preparing a resubmission and need to produce the formal response letter
- When you want to handle all reviewer comments in a single structured session

## Not For

- Responding to a single comment in isolation → use `/address-reviewer-comment`
- Rewriting prose without a review → use `/write-to-intent`

## Inputs Required

Provide:
1. **Reviews**: paste the full review text, clearly labelled by reviewer (Reviewer 1, Reviewer 2, etc.)
2. **Decision** (optional): the editor's decision and meta-comments
3. **Mode**: `draft-only` (letter only, no manuscript edits) or `full` (letter + edit proposals)

---

## Workflow

### Phase 0 — Parse and Categorize

Read all reviewer comments and for each one:
- Assign a unique ID: R1.1, R1.2, R2.1, etc.
- Categorize: `technical` | `writing` | `consistency` | `scope` | `question`
- Note the affected manuscript location if identifiable from context

Present the structured comment inventory:

```
| ID   | Reviewer | Category    | Summary                                  | Location        |
|------|----------|-------------|------------------------------------------|-----------------|
| R1.1 | R1       | writing     | "paragraph X is circular"                | method.tex:88   |
| R1.2 | R1       | technical   | "O(n) claim not justified"               | method.tex:201  |
| R2.1 | R2       | scope       | "comparison with baseline Y is missing"  | evaluation      |
```

**USER GATE — confirm the inventory is correct.** Flag any comments to skip or merge, then continue.

---

### Phase 1 — Technical Verification *(technical comments only)*

For each `technical` comment, invoke `paper-implementation-checker`:

Ask: "Does the current manuscript text accurately describe the implementation at this location? Report CONSISTENT / DIVERGES / CANNOT_VERIFY with file:line evidence."

<!-- CUSTOMIZE: Fill in your implementation reference paths if applicable -->

Surface any DIVERGES findings to the user before drafting responses.

---

### Phase 2 — Draft Responses *(per comment)*

For each comment in order, invoke `writer`:

Ask: "Draft a response to this reviewer comment for the response letter. The response should:
1. Acknowledge the comment in one sentence
2. State the action taken (revised at [location] / added [what] / clarified [what] / respectfully disagree with justification)
3. Point to the specific manuscript location of any change
4. Quote the revised text inline if the change is short

Also propose the corresponding manuscript edit, if any. Do not modify the file."

---

### Phase 3 — Consistency Check

Invoke `consistency-auditor` on all proposed manuscript edits in aggregate:

Ask: "Do any of these proposed edits, taken together, introduce new terminology drift, acronym inconsistencies, or contradictions with the rest of the manuscript? Report only issues introduced by these edits, with file:line evidence."

Surface conflicts to the user before assembling the letter.

---

### Phase 4 — Assemble Response Letter

Produce the complete response letter in the following format:

```
Dear Editor and Reviewers,

We thank the reviewers for their careful reading and constructive feedback.
We have revised the manuscript in response to all comments. Below we address
each comment in turn.

---

## Reviewer 1

**R1.1** [Original comment quoted verbatim]

*Response:* [Drafted response — action taken, manuscript location]

> [Revised text if short, or "See [section], lines X–Y"]

**R1.2** ...

---

## Reviewer 2

...

---

We believe the revised manuscript is substantially stronger as a result of
this feedback and hope it now meets the standards for publication.

Sincerely,
[Authors]
```

---

### Phase 5 — Hold for Approval

Present:
1. The complete response letter draft
2. All proposed manuscript edits, labelled by comment ID
3. Any unresolved conflicts from Phase 3

**Stop here. Do not modify any manuscript file until the user explicitly approves each edit.**

After approval, apply edits one at a time and confirm each before moving to the next.

---

## Hard Constraints

- Never modify the manuscript before explicit user approval.
- Never fabricate manuscript locations — if the location of a change is unclear, flag it.
- Do not claim a comment was addressed if no change was made.
- Preserve all LaTeX macros, `\ref`, `\cite`, labels, and math environments in proposed edits.
- Do not add citations not already in the bibliography unless the user explicitly requests it.
- Do not silently weaken a limitation or strengthen a claim to satisfy a reviewer.

---

## Invocation Example

```
/response-to-reviewers

Mode: full

Decision: Major revision. The paper requires clearer motivation and stronger experimental validation.

Reviewer 1:
The paper presents an interesting approach, but the motivation in Section 1
is unclear. Also, the claim on line 87 that the method runs in O(n) is
not adequately justified...

Reviewer 2:
I found the experimental setup well-described. However, the paper lacks
a comparison with baseline Y, which is standard in this area...
```
