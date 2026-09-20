---
name: technical-paragraph-rewrite
description: Verify implementation-dependent claims in a scientific manuscript paragraph, then produce one evidence-bounded rewrite with diagnostic review, author-selected findings, and at most one controlled revision.
---

# Technical Paragraph Rewrite

Follow `AGENTS.md`. Use this workflow when a paragraph describes implementation behavior and technical verification must precede rewriting.

## Workflow

1. **Read context.** Inspect the target paragraph, its neighbors, related manuscript claims, and canonical macros.
2. **Verify implementation.** Invoke `.agents/agents/paper-implementation-checker.md` with the paragraph and relevant implementation files. Require `CONSISTENT`, `DIVERGES`, or `CANNOT_VERIFY` with evidence.
3. **Handle uncertainty.** Stop before drafting on `DIVERGES`. On `CANNOT_VERIFY`, record the limit and prohibit wording that assumes the unverified fact.
4. **Create the contract.** Use `.agents/context/passage-contract.md` to record the verified content, rhetorical function, prohibited implications, and LaTeX that must remain unchanged. Ask the author only about material ambiguity.
5. **Draft once.** Invoke `.agents/agents/writer.md` for one conservative rewrite. Generate alternatives only for a specific author-identified technical or rhetorical choice.
6. **Diagnose.** Invoke `.agents/agents/scientific-paper-reviewer.md` for evidential fidelity and `.agents/agents/consistency-auditor.md` for manuscript alignment. Use `.agents/agents/prose-reviewer.md` only when expression remains a material risk. Critics report defects and do not rewrite.
7. **Obtain author decisions.** Present the draft and deduplicated findings. Ask the author to accept, reject, or modify each material finding before revision or editing.
8. **Revise once if needed.** Give `writer` only the accepted findings and original evidence. Show a semantic diff, audit against the contract, and stop. Start another cycle only for a specific unresolved defect identified by the author.

## Constraints

- Treat implementation repositories as read-only ground truth.
- Do not invent details or normalize away manuscript-code disagreement.
- Do not run automatic rewrite loops or generate routine stylistic alternatives.
- Preserve macros, labels, references, citations, math, and technical scope.
- Follow the propose-first and validation rules in `AGENTS.md`.
