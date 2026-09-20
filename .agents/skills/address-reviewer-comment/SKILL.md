---
name: address-reviewer-comment
description: Analyze a reviewer comment on a scientific manuscript, define an author-controlled response contract, produce one revision proposal, and use diagnostic review plus one controlled revision before editing.
---

# Address Reviewer Comment

Follow `AGENTS.md`. Use this workflow for a reviewer comment targeting a passage or section.

## Inputs

Require the verbatim comment, target text and location, immediate context, and comment type when known. Record the intended response in a passage contract using `.agents/context/passage-contract.md`. After the author approves the interpretation, append or update a trace entry in `.agents/context/reviewer-contracts.md`.

The contract must distinguish:

- what the reviewer correctly identifies
- what the manuscript can support
- what must not be conceded, claimed, or implied
- how the revision should resolve the comment

The author approves this interpretation before drafting when the response strategy is not unambiguous.

## Workflow

1. **Analyze the comment.** Identify the challenged claim, missing information, or presentation defect. Search the manuscript for related statements. Check `.agents/context/claim-ledger.md` and `.agents/context/do-not-say.md` for relevant guardrails.
2. **Verify when needed.** For technical or mixed comments, invoke `.agents/agents/paper-implementation-checker.md`. Stop on `DIVERGES`; carry `CANNOT_VERIFY` forward as an explicit limit.
3. **Confirm one direction.** If more than one materially different response is defensible, present short strategy options with their tradeoffs and obtain the author's choice. Do not create full prose alternatives at this stage.
4. **Record the contract.** Once the author approves the interpretation, append or update the response contract in `.agents/context/reviewer-contracts.md` using its template.
5. **Draft once.** Invoke `.agents/agents/writer.md` with the approved contract and evidence to produce one revision proposal.
6. **Diagnose.** Invoke `.agents/agents/scientific-paper-reviewer.md` for comment coverage and claim precision and `.agents/agents/consistency-auditor.md` for manuscript alignment. Use `.agents/agents/argument-reviewer.md` only when the response depends on a nontrivial inference. Critics report defects only and do not propose replacement prose.
7. **Obtain author decisions.** Present the proposal and deduplicated findings. The author accepts, rejects, or modifies material findings before they reach the writer.
8. **Revise once if needed.** Invoke `writer` with only accepted findings. Show a semantic diff, verify comment coverage and contract compliance, then stop. Begin another cycle only for a specific unresolved defect identified by the author.
9. **Edit only after approval.** Apply the approved revision only under the edit-approval rule in `AGENTS.md`, then run a targeted diff review and the required validation.

## Standard Proposal Output

Present reviewer-comment proposals in this order:

1. Response contract
2. Proposed readable text
3. LaTeX-ready text when useful
4. Claim-scope check
5. Approval question

After an approved edit, report:

1. Files changed
2. Semantic diff summary
3. Diff-review verdict for changed manuscript text
4. `make pdf` result
5. `make lint` and/or `scripts/lint_diff.py` result

## Constraints

- Do not invent implementation details, evidence, or citations to satisfy a reviewer.
- Do not silently strengthen or weaken claims.
- Do not generate multiple full drafts by default.
- Do not perform automatic writer-critic-writer loops.
- Preserve macros, labels, references, citations, math, and established terminology.
