---
name: write-to-intent
description: Draft or substantially rewrite a scientific manuscript passage from an author-controlled passage contract, using one primary draft, diagnostic review, human-selected findings, and at most one controlled revision before stopping.
---

# Write To Intent

Follow `AGENTS.md`. Use this workflow for substantive drafting or rewriting toward a rhetorical goal. Use a smaller direct edit for unambiguous wording changes.

## Inputs

Build a passage contract from `.agents/context/passage-contract.md` containing the rhetorical function, required scientific content and evidence, prohibited claims, terminology to preserve, reader state, local connections, and relevant length constraints.

Read the target and neighboring manuscript text. Ask only for missing contract information that would materially change scientific meaning or argument structure. Do not start prose generation while such an ambiguity remains.

## Workflow

### 1. Establish Ground Truth

Search the manuscript for related definitions, claims, terminology, macros, and limitations. Load focused context files as needed: `.agents/context/terminology.md`, `.agents/context/contributions.md`, `.agents/context/evaluation-claims.md`, `.agents/context/claim-ledger.md`, and `.agents/context/do-not-say.md`. Invoke `.agents/agents/paper-implementation-checker.md` only for implementation-dependent claims. Stop and surface any `DIVERGES` result before drafting; treat `CANNOT_VERIFY` conservatively.

### 2. Confirm The Argument

When the structure is not already explicit, use `.agents/skills/argument-plan/SKILL.md` or produce its equivalent: a claim-level outline only, with no manuscript prose. Show how each required point supports the rhetorical function. Obtain author approval for the outline before drafting.

Skip this gate when the author supplied an explicit, complete structure.

### 3. Produce One Draft

Invoke `.agents/agents/writer.md` with the approved contract, relevant context, and verified findings. Request one primary draft. Request alternatives only for a specific unresolved rhetorical choice identified by the author.

### 4. Run Diagnostic Review

Use read-only critics. Always use:

- `.agents/agents/scientific-paper-reviewer.md` for support, scope, and technical accuracy
- `.agents/agents/consistency-auditor.md` for terminology, macros, notation, and manuscript-wide alignment

For a difficult passage, additionally use only the critic relevant to the risk:

- `.agents/agents/argument-reviewer.md` for inferential structure and contract satisfaction
- `.agents/agents/prose-reviewer.md` for clarity and economy after scientific content is settled

Critics must identify defects in the standard `Location / Criterion / Evidence / Problem / Severity / Confidence` form. They must not rewrite the passage or supply replacement prose. Parallel execution is optional and affects latency only; it is not a requirement for quality.

### 5. Human Findings Gate

Present the draft and deduplicated findings. Do not pass critic output directly to the writer. Ask the author to accept, reject, or modify each material finding.

If the author accepts the draft without findings, stop. If the author requests a file edit, apply the approved draft and validate it under `AGENTS.md`.

### 6. Make One Controlled Revision

Invoke `writer` with only the author-accepted findings, the original contract, and the same evidence. Produce one revised draft. Preserve unaffected wording where practical.

Show a semantic diff or concise change ledger, then audit the revision against the contract. Stop after this revision. Begin another cycle only when the author identifies a specific unresolved defect; never continue because a generic improvement loop remains available.

## Optional grammar focus

When the author requests focused grammar diagnosis, use
`.agents/skills/scientific-grammar-review/SKILL.md` on the relevant passage with
context. Do not add a grammar pass by default. Merge duplicate diagnoses and
preserve this workflow's report, scope, and human findings gate. Return structural
recommendations separately; do not supply a rewritten passage or pass unapproved
findings to the writer.

## Constraints

- Keep the author in control of argument structure and review decisions.
- Do not invent claims, evidence, implementation details, or citations.
- Do not generate multiple full drafts by default.
- Do not perform automatic writer-critic-writer loops.
- Preserve manuscript macros, labels, references, citations, math, and established terminology.
- Follow the propose-first and validation rules in `AGENTS.md`.
