---
name: argument-plan
description: Use before substantive drafting when a scientific manuscript passage needs an inspectable argument or paragraph skeleton without generating polished prose.
---

# Argument Plan

Read-only planning workflow. Use this skill to turn an author-controlled passage contract into an inspectable argument structure before drafting. Do not write polished manuscript prose and do not edit files.

## When To Use

Use when:

- a passage has a nontrivial rhetorical function;
- the author has specified intent but not paragraph structure;
- a reviewer response requires careful positioning before prose is drafted;
- a section transition, contribution framing, limitation, or results interpretation could overclaim;
- `/write-to-intent` reaches its “Confirm The Argument” step and the structure is not already explicit.

Do not use for minor wording fixes or straightforward local edits.

## Required Inputs

Require a passage contract based on `.agents/context/passage-contract.md`, including at least:

- rhetorical function;
- required scientific content and evidence;
- prohibited claims or implications;
- relevant neighboring context;
- target length or structural constraints when known.

If any missing field would materially change the argument, ask the author before planning.

## Reference Context

Read only what is needed:

- `.agents/context/passage-contract.md`
- `.agents/context/claim-ledger.md` for high-risk evidence boundaries
- `.agents/context/do-not-say.md` for prohibited overclaims
- `.agents/context/terminology.md` for canonical terms
- `.agents/context/contributions.md` for contribution alignment
- `.agents/context/evaluation-claims.md` for evaluation-result scope
- target passage and immediate neighboring manuscript text

For implementation-dependent claims, request or perform a targeted `.agents/agents/paper-implementation-checker.md` pass before planning.

## Workflow

1. **Check the contract.** Identify missing or ambiguous scientific content, evidence, scope conditions, and prohibited claims.
2. **Map evidence to claims.** For each required point, record the manuscript, result, implementation, or citation basis that permits it.
3. **Build the argument skeleton.** Produce a claim-level structure, not prose. Each step should state:
   - role in the passage;
   - claim or transition;
   - evidence/source;
   - allowed inference;
   - prohibited overextension.
4. **Check local flow.** Explain how the skeleton connects to the preceding and following text.
5. **Ask for approval.** Stop and ask the author to approve, reject, or modify the skeleton before any drafting skill is used.

## Output Format

```text
## Argument Plan

### Contract Gaps
- <material gaps, or None>

### Proposed Skeleton
1. Role: <setup / contrast / claim / evidence / limitation / transition>
   - Claim content: <non-polished claim>
   - Evidence/source: <file, result, citation, or author instruction>
   - Allowed inference: <what the prose may conclude>
   - Do not imply: <scope guardrail>

### Local Flow
- Preceding connection: <how this follows from prior text>
- Following connection: <how this prepares the next text>

### Approval Request
Please approve, reject, or modify this argument plan before drafting.
```

## Constraints

- Do not generate polished prose or LaTeX-ready paragraphs.
- Do not invent claims, evidence, citations, or implementation details.
- Do not decide the paper's argument for the author; expose the structure for author approval.
- Do not produce multiple complete alternatives unless the author identifies genuinely different rhetorical strategies.
- Do not edit files.
