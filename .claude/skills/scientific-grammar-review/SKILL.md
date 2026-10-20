---
name: scientific-grammar-review
description: Diagnose grammatical errors and sentence-level syntactic ambiguity in scientific prose, with optional educational explanations and conservative structural proposals. Use for focused linguistic review rather than general rewriting.
---

# Scientific Grammar Review

Prefer grammatical constructions that communicate scientific relationships directly and unambiguously, without sacrificing technical precision. Complexity is justified when it expresses necessary distinctions or supports the passage's rhetorical purpose.

## Scope and inputs

Review a supplied passage or file and line range, with adjacent sentences when available. Default to **concise** mode; use **detailed** mode when requested. Respect any focus list. Read `AGENTS.md`, the context index, relevant terminology, and `.agents/context/style-preferences.md` if present. Missing preferences mean no additional author preferences. Do not require a drafting contract for diagnosis alone.

This is read-only diagnosis, not a new drafting agent. Do not edit manuscript files, produce a rewritten passage, or start a writer automatically. Recommend grammatical structures; a short illustrative transformation is permitted only as an unapplied proposal when its meaning is established. The existing prose reviewer retains clarity, concision, cohesion, and readability review.

## Procedure

1. Read the target and immediate context. Establish referents, technical terms, logical relations, modality, quantification, and the sentence's function. Search related manuscript definitions only when necessary. State material context limits.
2. Identify a concrete defect before naming a grammatical feature. Consult only the relevant sections of [grammatical-patterns.md](references/grammatical-patterns.md), using its rule index. Check the counterexample and exceptions before reporting. Sentence length and feature counts are not diagnostics.
3. Separate three judgments:
   - `GRAMMATICAL_ERROR`: a supported violation of standard formal English syntax or sentence punctuation.
   - `CLARITY_PROBLEM`: grammatical wording permits a materially unclear relationship or imposes identifiable processing difficulty.
   - `STYLE_PREFERENCE`: acceptable grammar conflicts with an explicit author preference or has a demonstrable, context-specific readability cost. Identify that basis. Be conservative with subjective findings.
4. Assign **major** severity if interpretation of a central claim, argument, condition, or comparison is materially affected; otherwise **minor**. Severity and confidence are independent of classification. Use **high**, **medium**, or **low** confidence. Do not present low-confidence preferences as defects; record a necessary author question separately.
5. Propose the smallest structural remedy. Preserve agency, tense/aspect, negation, causal versus associative relationships, quantifiers, comparison groups, conditions, uncertainty, terminology, and all LaTeX. If the intended attachment or relation is unknown, describe the alternatives and ask the author to specify it; do not choose a scientific interpretation. Missing scientific facts are verification needs, not grammatical errors.
6. Deduplicate by underlying problem. Use the most specific rule: GRAM-009 before GRAM-003 for dangling participles, GRAM-007 for coordination scope, GRAM-004 for pronoun antecedents, GRAM-015 for remaining semantic scope. Do not add generic ambiguity findings for the same defect. Prioritize meaning and correctness ahead of preferences.

Never automatically penalize passive voice, nominalization, relative clauses, long sentences, copulas, technical repetition, or complex noun phrases. Passive voice may preserve the topic when agency is irrelevant; repeated technical nouns may be necessary for unambiguous reference. A valid semicolon is not an error. Preferences never override grammatical correctness or scientific precision.

## Report

Return `CLEAN` when there are no meaningful supported findings. Do not manufacture a minimum number. Otherwise, provide a concise prioritized list. Each finding includes:

- **Location**: file:line or sentence/clause identifier.
- **Classification / Criterion**: one of the three classes above.
- **Phenomenon**: stable GRAM rule identifier and name.
- **Original / Evidence**: exact expression from the target.
- **Explanation / Problem**: the actual defect, including the basis of a preference.
- **Preferred structure**: structural recommendation, conditional if meaning is unresolved.
- **Severity** and **Confidence**.

Concise mode uses a brief explanation. Detailed mode additionally identifies the relevant constituents and grammatical relationship, explains the transformation and its semantic checks, and states why a superficially similar valid construction should be retained. Use accurate linguistic terminology with plain-language glosses; do not present a preference as a rule of English.

## Author-controlled handoff

Present findings for the author to accept, reject, or modify. Only accepted diagnoses may enter `write-to-intent` or an equivalent authorized local-edit workflow. The writer independently resolves them from source and context; it must not copy reviewer wording uncritically. Preserve the passage-contract, single-draft, human-findings gate, and at-most-one-targeted-revision policy. This skill does not authorize edits or repeated critique/rewrite cycles.
