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
