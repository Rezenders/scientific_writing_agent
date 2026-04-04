---
name: bootstrap-memory
description: Use at the start of a new paper project, or after a long break, to pre-populate all agent memory files with manuscript-specific knowledge extracted from CLAUDE.md and the manuscript itself. Run this once after setup to give agents immediate context rather than building it up slowly over sessions.
---

# Bootstrap Memory

Scans `CLAUDE.md` and the manuscript to extract project-specific knowledge and writes it into all four agent memory directories. Run this once after `/setup-paper-project`, or any time you want to refresh agent knowledge after major revisions.

## When to Use

- After running `/setup-paper-project` on a new manuscript
- After a major rewrite that changed terminology, contributions, or section structure
- When agents are giving inconsistent or generic responses that suggest they lack project context

## Not For

- Ongoing memory updates during normal editing — agents do this themselves as they work
- Fixing stale or incorrect memories — edit the specific memory file directly

## Inputs Required

Tell Claude:
1. **Memory root** (default: `.claude/agent-memory/`)
2. **Manuscript root** (default: `sections/` — or wherever your `.tex` section files live)
3. **Scope** (optional): `full` (all four agents) or a specific agent name

---

## Workflow

### Phase 1 — Extract from CLAUDE.md

Read `CLAUDE.md` (and `AGENTS.md` if present) and extract:

- All canonical macros and their rendered forms
- Terminology distinctions and rules (e.g. "never use X where Y is established")
- Style rules and prohibited patterns (e.g. no em-dashes, no semicolons)
- Annotation macro definitions
- Section structure: file names and their roles
- Build commands
- Implementation reference paths (if present)

---

### Phase 2 — Extract from Manuscript

Read the introduction section and extract:
- Contribution claims (bullet points or numbered list)
- Key defined terms with their first-use definitions
- The paper's central argument in one or two sentences

Scan all section files and extract:
- Acronym definitions — patterns like "X (ABC)" or "\acr{}" on first mention
- Key notation from math environments
- Repeated terminology patterns

---

### Phase 3 — Write Agent Memory Files

Before writing each file, check whether it already exists. If it does, update rather than overwrite — preserve any content that is more specific or detailed than what was just extracted.

**Writer** → `<memory-root>/writer/project_paper_context.md`
Contents:
- All macros (name → rendered form)
- Terminology distinctions and rules
- Style rules and prohibited patterns
- Section map (file → role)
- Contribution framing as stated in the introduction

**Consistency Auditor** → `<memory-root>/consistency-auditor/project_context.md`
Contents:
- Canonical macro list with known free-text variants to flag
- Defined acronyms and their first-use locations
- Key contribution claims (for cross-section verification)
- Multi-meaning terms that need disambiguation

**Scientific Paper Reviewer** → `<memory-root>/scientific-paper-reviewer/project_context.md`
Contents:
- Core claims and contributions as framed in abstract and introduction
- Known overclaiming risks (e.g. generality beyond evaluated scenarios)
- Evaluation setup summary: baselines, metrics, scenarios

**Paper Implementation Checker** *(only if implementation paths are configured in CLAUDE.md)*
→ `<memory-root>/paper-implementation-checker/project_context.md`
Contents:
- Implementation reference paths
- Key technical facts that are non-obvious and often misstated in prose

All memory files must use the frontmatter format:
```markdown
---
name: ...
description: ...
type: project
---
```

---

### Phase 4 — Update MEMORY.md Indices

For each agent that received new or updated memory files, update (or create) `<memory-root>/<agent>/MEMORY.md` with a pointer line for each file.

---

### Phase 5 — Report

```
## Bootstrap Memory Report

### Files written
- .claude/agent-memory/writer/project_paper_context.md          [written / updated / skipped]
- .claude/agent-memory/consistency-auditor/project_context.md   [written / updated / skipped]
- .claude/agent-memory/scientific-paper-reviewer/...            [written / updated / skipped]
- .claude/agent-memory/paper-implementation-checker/...         [written / updated / skipped — not configured]

### Key facts extracted
- Macros defined: N
- Acronyms found: N
- Contribution claims: N
- Style rules recorded: N

### Gaps / warnings
[Any <!-- CUSTOMIZE --> placeholders still unfilled, sections that could not be parsed,
or facts that require manual verification before trusting]
```

## Constraints

- Do not overwrite memory content that is more specific or detailed than what was extracted.
- Do not invent facts not present in `CLAUDE.md` or the manuscript.
- If `CLAUDE.md` still contains `<!-- CUSTOMIZE -->` placeholders, report them as gaps rather than recording the placeholder text as facts.
- If a section file does not exist at the expected path, note it and continue.
