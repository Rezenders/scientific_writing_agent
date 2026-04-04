# scientific-writing-agent

A Claude Code and Codex configuration template for writing scientific papers in LaTeX. Drop it into any paper repository and get a multi-agent writing assistant that reviews, rewrites, and audits your manuscript. In proposal-first rewrite/edit workflows, it works without touching a file until you approve.

---

## Navigation

| I want to… | Go to |
|---|---|
| Understand what's included | [What's included](#whats-included) |
| See all agents at a glance | [Agents](#agents) |
| See all skills at a glance | [Skills](#skills) |
| Learn how to use a skill | [Using the skills](#using-the-skills) |
| Install via plugin marketplace | [Installation](#installation) |
| Set up on a new paper repo | [Setup](#setup) / [SETUP.md](SETUP.md) |
| Use the Codex plugin | [Codex Plugin](#codex-plugin) |
| Understand the agent pipelines | [How it works](#how-it-works) |
| Customize for my project | [Adapting to your project](#adapting-to-your-project) |
| Enable agent memory | [Agent memory](#agent-memory) |

---

## What's included

### Agents

| Agent | Role |
|---|---|
| `writer` | Drafts, rewrites, and polishes scientific prose. Reads the whole repo for context before touching anything. |
| `consistency-auditor` | Reads-only auditor that detects terminology drift, acronym inconsistencies, notation mismatches, and cross-section contradictions. |
| `scientific-paper-reviewer` | Critiques a section across five dimensions: clarity, redundancy, claim precision, paragraph flow, and alignment with neighbouring sections. |
| `paper-implementation-checker` | *(Optional)* Cross-checks a manuscript claim against a software implementation. Only needed if your paper describes a codebase. |

### Skills

| Skill | When to use |
|---|---|
| `/section-review` | After rewriting a full section — runs scientific review + consistency audit in parallel and produces a unified report. |
| `/write-to-intent` | When you want to write or substantially rewrite a passage toward a stated rhetorical goal. Proposes multiple directions, gets your approval, then drafts and refines. |
| `/address-reviewer-comment` | When a reviewer (human or agent) targets a specific paragraph. Generates revision strategies, writes proposals, reviews them, and holds for your approval before touching the file. |
| `/technical-paragraph-rewrite` | *(Optional)* When a paragraph describes implementation behavior and needs accuracy-verification + rewrite. Only useful with an associated codebase. |
| `/paper-build` | Builds the PDF and runs chktex lint. Reports LaTeX errors, warnings, undefined references, and missing citations. Run after any substantive edit. |
| `/find-annotations` | Scans all `.tex` files for `\todo`, `\revise`, `\red`, and author comments. Run before any writing session or submission. |
| `/pre-submission` | Full go/no-go checklist: build, lint, annotations, consistency audit, and (optionally) implementation alignment. |
| `/full-manuscript-audit` | Multi-phase audit of every section: annotations → consistency → per-section review → implementation spot-check → unified GO/NO-GO report. Run before `/pre-submission`. |
| `/sync-remote` | Safe git sync workflow — enforces pull-before-push and never stages build artifacts. Works with Overleaf, GitHub, or any remote. |
| `/bootstrap-memory` | Pre-populates all agent memory files from `CLAUDE.md` and the manuscript. Run once after setup to give agents immediate project context. |
| `/response-to-reviewers` | Full resubmission workflow: parses all reviewer comments, drafts a formal response letter with per-comment responses, and proposes manuscript edits. Nothing is written to file without your approval. |
| `/diff-review` | Targeted review of only what changed in a git diff — consistency and scientific review scoped to the modified hunks. Much faster than `/section-review` for incremental edits. |

---

## Using the skills

In Claude Code, each skill is a slash command you type directly.

In Codex, the same workflows live as repo-local skill specs under `.codex/skills/<skill>/SKILL.md`.

## Codex Plugin

This repository includes a repo-local plugin at `plugins/scientific-writing/`.
It is also registered in the repo-local marketplace at `.agents/plugins/marketplace.json` so Codex can discover it without manual path lookup.

- Setup workflow skill: `setup-paper-project`
- Script entrypoint: `plugins/scientific-writing/scripts/setup_paper_project.py`
- Repo config source of truth: `.scientific-writing.json`

Use this command to bootstrap or refresh the managed setup files for the current repo:

```bash
python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .
```

See `docs/plugin-setup.md` for ownership boundaries and rerun behavior.

Most skills need a few pieces of information upfront — provide them in the same message to avoid extra back-and-forth.

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

### `/full-manuscript-audit`

Runs a structured 5-phase audit across the entire manuscript and produces a unified GO / CONDITIONAL GO / NO-GO report. Use this before `/pre-submission` to catch issues early.

```
/full-manuscript-audit
```

No required arguments. Optional focus hint:

```
/full-manuscript-audit

Focus: pay extra attention to evaluation claims and
       all comparisons with the baseline approach.
```

The skill runs in order:
1. **Annotation inventory** — all open `\todo`, `\revise`, and author comments
2. **Consistency audit** — terminology drift, acronym consistency, contribution-statement alignment
3. **Section-by-section scientific review** — clarity, redundancy, claim precision, flow, alignment
4. **Implementation spot-check** *(skipped if not configured)* — highest-risk claims vs. codebase
5. **Unified report** — merged findings, per-section verdicts, recommended fix order

Example output:

```
## Full Manuscript Audit

### Open Annotations
4 open across 3 files (introduction.tex × 2, evaluation.tex × 2)

### Critical Issues
1. [Contribution drift] Introduction promises X but Section 4 demonstrates Y only
   ...

### Per-Section Verdicts
| Section      | Verdict          |
|---|---|
| Introduction | NEEDS REVISION   |
| Method       | READY            |
| Evaluation   | NEEDS REVISION   |
| ...          | ...              |

### Overall Verdict: CONDITIONAL GO
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

### `/bootstrap-memory`

Pre-populates all agent memory files from `CLAUDE.md` and the manuscript. Run this once after `/setup-paper-project` to give agents immediate project-specific context rather than building it up slowly over sessions.

```
/bootstrap-memory
```

No required arguments. The skill reads `CLAUDE.md` (and `AGENTS.md` if present) and scans the manuscript to extract macros, terminology rules, acronyms, contribution claims, and style rules, then writes them into all four agent memory directories.

Optional arguments if your layout differs from the defaults:
```
/bootstrap-memory

Memory root: .claude/agent-memory/
Manuscript root: sections/
Scope: full
```

Reports what was written, how many facts were extracted, and any `<!-- CUSTOMIZE -->` placeholders still unfilled.

---

### `/response-to-reviewers`

Full resubmission workflow. Handles all reviewer comments in a single structured session, producing a formal response letter and manuscript edit proposals. **Nothing is written to file until you explicitly approve.**

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

The skill parses comments into a numbered inventory (R1.1, R1.2, R2.1…), shows it to you for confirmation, then drafts responses and proposes manuscript edits. You review and approve each edit before any file is modified.

Use `Mode: draft-only` to produce the response letter only, without manuscript edit proposals.

---

### `/diff-review`

Reviews only what changed in a git diff — scoped to the modified hunks, not the entire section. Much faster than `/section-review` for incremental edits.

```
/diff-review
```

By default, Claude runs `git diff` automatically. Options:
- **Staged only**: say "staged" — Claude runs `git diff --cached`
- **Specific range**: provide a commit ref (e.g. `HEAD~1`, `abc123..HEAD`)
- **Manual**: paste the diff directly if not in a git repo

```
/diff-review HEAD~2..HEAD
```

Produces a targeted report with consistency and scientific findings scoped only to the changed passages, plus a CLEAN / MINOR ISSUES / NEEDS ATTENTION verdict.

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

In proposal-first rewrite/edit workflows, no file is modified without your explicit approval.

---

## Installation

### Via Claude Code plugin marketplace

Add this repository to your Claude Code marketplace once, then install the plugin into any paper project:

```bash
/plugin marketplace add https://github.com/Rezenders/scientific_writing_agent.git
```

Then from inside your paper repository:

```bash
/plugin install scientific-writing@scientific-writing-agent
```

Once installed, run the setup skill to bootstrap agent configuration into your project:

```
/setup-paper-project
```

This copies all agent definitions, skills, and policy files into your repo, ready to customize.

### Manual installation

If you prefer not to use the plugin system, copy the relevant directories directly into your paper repo:

```bash
# From the scientific_writing_agent root:
cp -r .claude/  your-paper-repo/.claude/
cp -r .codex/   your-paper-repo/.codex/
cp CLAUDE.md    your-paper-repo/CLAUDE.md
cp AGENTS.md    your-paper-repo/AGENTS.md
```

Then follow [SETUP.md](SETUP.md) to fill in the project-specific placeholders.

---

## Setup

See **[SETUP.md](SETUP.md)** for the full step-by-step checklist. The short version:

1. Copy `.claude/`, `.codex/`, `CLAUDE.md`, and `AGENTS.md` into your paper repo. If you plan to use the plugin bootstrap path, also copy `plugins/scientific-writing/`.
   In plugin-first mode, treat later setup edits as config/template work (`.scientific-writing.json` and `plugins/scientific-writing/assets/templates/root/`) to avoid losing changes on rerun.
2. Fill in all `<!-- CUSTOMIZE -->` sections in `CLAUDE.md`, `AGENTS.md`, and `.codex/context/manuscript-context.md`.
3. Replace any placeholder implementation paths in the optional checker and rewrite workflows if your paper describes a codebase.
4. If you want Claude's persistent memory, create the `.claude/agent-memory/*/` directories as described in `SETUP.md`.

---

## Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed and authenticated if you want the Claude workflow.
- Codex available in your environment if you want the Codex workflow.
- A LaTeX manuscript repository (Overleaf-synced or local).
- Build tools: `latexmk`, `chktex` (optional but recommended for `/pre-submission`).

---

## Agent memory

Each agent maintains a persistent memory system in `.claude/agent-memory/<agent>/`. Over time, the agents build up project-specific knowledge — defined acronyms, preferred terminology, contribution framing, style rules — so they get more accurate with every session.

Memory is version-controlled alongside the manuscript, so it persists across machines and collaborators.

For Codex, the analogous durable context is kept repo-local in `.codex/context/manuscript-context.md` rather than per-agent memory directories.

---

## Adapting to your project

The template is designed to be generic. Things you will always customize:

- **CLAUDE.md**: paper title, research questions, document structure, build commands, annotation macros, LaTeX macros.
- **AGENTS.md**: the same manuscript-specific rules for Codex.
- **`.codex/context/manuscript-context.md`**: stable terminology, notation, and known risks you want Codex to preserve.
- **Claude agent memory paths**: one `<YOUR_PROJECT_ROOT>` per Claude agent file if you use Claude memory.

Things you customize only if your paper has an associated codebase:

- `paper-implementation-checker.md`: implementation file paths in both `.claude/agents/` and `.codex/agents/`.
- `technical-paragraph-rewrite`, `write-to-intent`, `address-reviewer-comment`: implementation reference tables in both toolchains.

Everything else works out of the box.
