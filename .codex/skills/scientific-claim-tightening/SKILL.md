---
name: scientific-claim-tightening
description: Use when scientific manuscript prose contains broad, high-risk, or result-summary claims that may overstate evidence, especially in the abstract, introduction, related work, discussion, conclusion, or reviewer responses.
---

# Scientific Claim Tightening

Read-only diagnostic workflow for finding and tightening overbroad scientific claims. Do not edit files in this skill.

## When To Use

Use when a passage contains or may contain words and constructions such as:

- only, first, novel, best, general, scalable, efficient, reusable
- outperforms, demonstrates, proves, validates, guarantees
- existing approaches, all approaches, no work, none, always, never
- result summaries in the abstract, introduction, discussion, or conclusion
- reviewer comments about overclaiming, unsupported claims, or scope

## Required Inputs

- Target passage and location.
- Immediate context when available.
- Relevant evidence source, or permission to search the manuscript.

## Reference Context

Before diagnosing, read these files when relevant:

- `.agents/context/claim-ledger.md`
- `.agents/context/do-not-say.md`
- `.agents/context/manuscript-context.md`
- `.agents/context/contributions.md`
- `.agents/context/evaluation-claims.md`
- `.agents/context/terminology.md`

Use manuscript files as the current source of truth. For implementation-dependent claims, invoke `.agents/agents/paper-implementation-checker.md`.

## Workflow

1. Identify every high-risk claim in the target passage.
2. For each claim, classify risk:
   - **Scope risk**: claim broader than evaluated scenarios or reviewed literature.
   - **Evidence risk**: claim not supported by cited results or manuscript context.
   - **Causality risk**: causal wording where experiments show only association.
   - **Terminology risk**: ambiguous or drifting technical terms.
   - **Implementation risk**: claim depends on code behavior and needs verification.
3. Compare each claim against the claim ledger and do-not-say list.
4. Report the supported scope and a direction for safer wording.
5. Do not write a full replacement paragraph unless the user explicitly asks; use `/write-to-intent`, `/technical-paragraph-rewrite`, or `/address-reviewer-comment` for drafting.

## Output Format

```text
## Scientific Claim Tightening Report

### Risk Summary
- <short summary>

### High-Risk Claims
1. Claim: <quote>
   - Location: <file:line or passage>
   - Risk type: scope | evidence | causality | terminology | implementation
   - Evidence boundary: <what manuscript/implementation supports>
   - Problem: <why current phrasing is risky>
   - Safer direction: <high-level guidance, not polished replacement prose>
   - Severity: critical | major | minor

### Clean Claims
- <claims checked and found appropriately scoped>

### Verification Needs
- <implementation or evidence checks still needed, or None>
```

## Constraints

- Do not invent evidence, citations, implementation behavior, or results.
- Do not silently weaken a contribution beyond what the evidence requires.
- Do not produce multiple alternative rewrites.
- Do not edit files.
