---
name: technical-paragraph-rewrite
description: "Use when a manuscript paragraph describes implementation behavior (functions, interfaces, data structures, system methods) and needs accuracy verification plus rewrite suggestions. Never modifies text without explicit user approval. OPTIONAL: only useful if your paper has an associated software implementation."
---

# Technical Paragraph Rewrite

## Overview

Multi-agent pipeline that verifies a manuscript paragraph against a software implementation, gathers scientific review feedback, and iterates through two rounds of rewrite suggestions — without touching the file until the user explicitly approves.

<!-- OPTIONAL SKILL
     This skill is only useful if your paper describes a software implementation.
     If your paper is purely theoretical or has no associated codebase, you can
     delete this file or skip invoking it. -->

## When to Use

- A paragraph describes what a function, query, interface method, or data structure does
- You want to verify the description is accurate before editing
- You want 2-3 concrete rewrites with peer review baked in

## Implementation Reference Paths

<!-- CUSTOMIZE: Replace with your project's actual implementation paths -->
| What to verify | Where to look |
|---|---|
| Type names, data structures, schemas | `<path>` |
| Running examples referenced in the paper | `<path>` |
| Runtime behavior, interface method names | `<path>` |
| Design intent / architecture documentation | `<path>` |

## Workflow

### Phase 1 — Implementation Check

Invoke `paper-implementation-checker` with:
- The paragraph text (quoted verbatim)
- The implementation file to check against (use the table above)

Ask: "Does this paragraph accurately describe what this function/interface/schema does? Report CONSISTENT / DIVERGES / CANNOT_VERIFY with file:line evidence."

> If CANNOT_VERIFY: note this prominently, then proceed with Phase 2 using the existing text only.

---

### Phase 2 — Scientific Review of Findings

Invoke `scientific-paper-reviewer` with:
- The paragraph text
- The implementation checker's full findings

Ask: "Given these implementation findings, does the feedback make sense scientifically? What are 2-3 approaches to address any accuracy or clarity issues?"

---

### Phase 3 — Writer: First Round of Suggestions

Invoke `writer` with:
- The original paragraph
- Phase 1 findings
- Phase 2 suggested approaches

Ask: "Produce 2-3 alternative rewrites of this paragraph that address the identified issues. Preserve all LaTeX macros, `\ref`, `\cite`, labels, and math environments verbatim.
<!-- CUSTOMIZE: List your project-specific macros here.
     Example: Preserve macros such as \approachname, \systemname, etc. -->
Do not modify the file."

---

### Phase 4 — Scientific Review of Suggestions

Invoke `scientific-paper-reviewer` with:
- The original paragraph
- All suggestions from Phase 3

Ask: "Review each suggestion for claim precision, clarity, and alignment with the manuscript's style. Which is strongest? Flag remaining issues in each."

---

### Phase 5 — Writer: Refined Proposals

Invoke `writer` with:
- The original paragraph
- Phase 3 suggestions
- Phase 4 reviews

Ask: "Based on the reviewer's feedback, produce 2-3 refined rewrite proposals. Do not modify the file."

---

### Phase 6 — Hold for Approval

Present all proposals clearly to the user. **Stop here.**

**Do not edit the manuscript file until the user explicitly selects or approves an option.**

---

## Hard Constraints

- **Never modify the manuscript before user approval.**
- Preserve all LaTeX labels, `\ref`, `\cite`, math environments, and project macros.
- Do not introduce technical claims not present in either the original paragraph or the implementation.
- Do not add citations not already in the bibliography.

## Invocation Example

```
/technical-paragraph-rewrite

Paragraph: "The selection function navigates the system graph by
following interface connections between components..."

Implementation file: <path/to/your/relevant/implementation/file>
```
