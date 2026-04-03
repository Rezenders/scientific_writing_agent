# scientific-writing-agent

A Claude Code configuration template for writing scientific papers in LaTeX. Drop it into any paper repository and get a multi-agent writing assistant that reviews, rewrites, and audits your manuscript — all without touching a file until you approve.

---

## What's included

### Agents

| Agent | Role |
|---|---|
| `writer` | Drafts, rewrites, and polishes scientific prose. Reads the whole repo for context before touching anything. |
| `consistency-auditor` | Reads-only auditor that detects terminology drift, acronym inconsistencies, notation mismatches, and cross-section contradictions. |
| `scientific-paper-reviewer` | Critiques a section across five dimensions: clarity, redundancy, claim precision, paragraph flow, and alignment with neighbouring sections. |
| `paper-implementation-checker` | *(Optional)* Cross-checks a manuscript claim against a software implementation. Only needed if your paper describes a codebase. |

### Skills (slash commands)

| Skill | When to use |
|---|---|
| `/section-review` | After rewriting a full section — runs scientific review + consistency audit in parallel and produces a unified report. |
| `/write-to-intent` | When you want to write or substantially rewrite a passage toward a stated rhetorical goal. Proposes multiple directions, gets your approval, then drafts and refines. |
| `/address-reviewer-comment` | When a reviewer (human or agent) targets a specific paragraph. Generates revision strategies, writes proposals, reviews them, and holds for your approval before touching the file. |
| `/technical-paragraph-rewrite` | *(Optional)* When a paragraph describes implementation behavior and needs accuracy-verification + rewrite. Only useful with an associated codebase. |
| `/paper-build` | Builds the PDF and runs chktex lint. Reports LaTeX errors, warnings, undefined references, and missing citations. Run after any substantive edit. |
| `/find-annotations` | Scans all `.tex` files for `\todo`, `\revise`, `\red`, and author comments. Run before any writing session or submission. |
| `/pre-submission` | Full go/no-go checklist: build, lint, annotations, consistency audit, and (optionally) implementation alignment. |
| `/sync-remote` | Safe git sync workflow — enforces pull-before-push and never stages build artifacts. Works with Overleaf, GitHub, or any remote. |

---

## Using the skills

Each skill is a slash command you type in Claude Code. Most skills need a few pieces of information upfront — provide them in the same message to avoid extra back-and-forth.

---

### `/find-annotations`

Scans all `.tex` files for `\todo`, `\revise`, `\red`, and per-author comments. Run this at the start of every writing session.

```
/find-annotations
```

No arguments needed. Example output:

```
### \todo  (2 open)
- introduction.tex:42  — "add citation for claim about X"
- approach.tex:118     — "clarify the role of the resolution model here"

### \revise  (1 open)
- evaluation.tex:73    — "this paragraph is too vague"

Total: 3 annotations across 2 files.
```

---

### `/paper-build`

Builds the PDF and runs chktex lint. Run after any substantive edit.

```
/paper-build
```

Reports build errors, lint warnings, undefined references, and missing citations.

---

### `/section-review`

Audits a full section for scientific quality and consistency with the rest of the manuscript. Reports only — no file changes.

**Minimal invocation:**
```
/section-review

Target: approach.tex — Section 3: Method
Neighbouring sections: background.tex (before), evaluation.tex (after)
```

**With a specific concern:**
```
/section-review

Target: evaluation.tex — Section 5: Results
Neighbouring sections: method.tex (before), conclusion.tex (after)
Focus: check that the metrics described here are consistent with how
       they were defined in Section 3, and that the contributions
       stated in the introduction are all addressed.
```

The skill produces a unified report with a READY / NEEDS REVISION / MAJOR ISSUES verdict.

---

### `/write-to-intent`

Writes or substantially rewrites a passage toward a stated rhetorical goal. Proposes multiple approach directions, waits for your pick, then drafts and refines without touching the file until you approve.

**New passage:**
```
/write-to-intent

Goal: Write a paragraph opening Section 2 that motivates why existing
      planning approaches fail under uncertainty, setting up our contribution.

Target: background.tex:1 (insert before first paragraph)
Context: background.tex:1–30 (what follows)
Constraints: must use the term "tactical retreat"; must not claim we
             solve the general case.
```

**Rewriting an existing paragraph:**
```
/write-to-intent

Goal: Rewrite the related work subsection intro so it identifies the gap
      our approach fills, rather than just summarizing prior work.

Target: related_work.tex:45 (existing intro paragraph, lines 45–58)
Context: related_work.tex:40–70
```

After answering a few clarifying questions, you will be shown 2-3 approach directions. You pick one (or more), and the skill produces full draft proposals for your approval.

---

### `/address-reviewer-comment`

Responds to a reviewer comment targeting a specific paragraph. Generates revision strategies, produces full rewrites, reviews them in parallel, and holds for your approval.

**Writing/clarity comment:**
```
/address-reviewer-comment

Comment: "The paragraph beginning 'The system derives...' is circular —
it explains the output in terms of itself without defining the mechanism."

Target: method.tex:88 (paragraph lines 88–97)
Context: method.tex:80–110
Comment type: writing
```

**Technical/factual comment:**
```
/address-reviewer-comment

Comment: "The claim that all reachable nodes are visited in O(n) is
not justified. The proof sketch in Section 4 only covers the acyclic case."

Target: method.tex:201 (lines 201–210)
Context: method.tex:195–220
Comment type: technical
```

For `technical` comments, the skill first runs an implementation check (if configured) before proposing rewrites. For `writing` or `consistency` comments, it skips straight to revision strategies.

---

### `/technical-paragraph-rewrite`

Verifies a paragraph against the implementation and produces accuracy-corrected rewrite proposals. Only useful if your paper describes a codebase.

```
/technical-paragraph-rewrite

Paragraph: "The selection function navigates the system graph by following
interface connections between components, returning the set of all nodes
reachable within two hops."

Implementation file: src/core/selector.py
```

The skill reports CONSISTENT / DIVERGES / CANNOT_VERIFY before producing any rewrites.

---

### `/pre-submission`

Full go/no-go pipeline: build, lint, open annotations, consistency audit, and (optionally) implementation alignment spot-check.

```
/pre-submission
```

No arguments. The skill runs all sub-steps in order and produces a structured report:

```
## Pre-Submission Report

| Step           | Status | Notes              |
|---|---|---|
| Build          | PASS   |                    |
| Lint           | PASS   | 0 warnings         |
| Annotations    | FAIL   | 3 open (\todo × 2) |
| Consistency    | PASS   |                    |
| Implementation | SKIP   | not configured     |

### Verdict: NO-GO

Blocking issues:
- introduction.tex:42  \todo "add citation for claim about X"
- approach.tex:118     \todo "clarify the role of the resolution model here"
```

---

### `/sync-remote`

Safe git sync with a remote (Overleaf, GitHub, or any other). Always pulls before pushing, never stages build artifacts.

**Pull from remote:**
```
/sync-remote

Action: pull
```

**Push local changes:**
```
/sync-remote

Action: push
Changed files: introduction.tex, approach.tex
Commit message: Edit: approach — tighten contribution framing
```

The skill stages only allowed source file types (`.tex`, `.bib`, figures), reviews what is staged before committing, and stops if conflicts are detected.

---

## How it works

The skills orchestrate the agents in multi-phase pipelines. For example, `/write-to-intent` runs:

```
user states goal
  → writer proposes approach directions
  → user picks one
    → writer drafts full proposals
      → scientific-paper-reviewer + consistency-auditor review in parallel
        → writer refines based on feedback
          → proposals presented to user for approval
            → user approves → file edited
```

No file is ever modified without your explicit approval.

---

## Setup

See **[SETUP.md](SETUP.md)** for the full step-by-step checklist. The short version:

1. Copy `.claude/` and `CLAUDE.md` into your paper repo.
2. Replace `<YOUR_PROJECT_ROOT>` in the three agent files with your repo's absolute path.
3. Create the agent memory directories.
4. Fill in all `<!-- CUSTOMIZE -->` sections in `CLAUDE.md`.
5. *(Optional)* Configure the implementation checker if your paper describes a codebase.

---

## Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed and authenticated.
- A LaTeX manuscript repository (Overleaf-synced or local).
- Build tools: `latexmk`, `chktex` (optional but recommended for `/pre-submission`).

---

## Agent memory

Each agent maintains a persistent memory system in `.claude/agent-memory/<agent>/`. Over time, the agents build up project-specific knowledge — defined acronyms, preferred terminology, contribution framing, style rules — so they get more accurate with every session.

Memory is version-controlled alongside the manuscript, so it persists across machines and collaborators.

---

## Adapting to your project

The template is designed to be generic. Things you will always customize:

- **CLAUDE.md**: paper title, research questions, document structure, build commands, annotation macros, LaTeX macros.
- **Agent memory paths**: one `<YOUR_PROJECT_ROOT>` per agent file.

Things you customize only if your paper has an associated codebase:

- `paper-implementation-checker.md`: implementation file paths.
- `technical-paragraph-rewrite`, `write-to-intent`, `address-reviewer-comment`: implementation reference tables.

Everything else works out of the box.
