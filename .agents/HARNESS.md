# Harness Adapter Notes

This repository keeps reusable scientific-writing workflows in `.agents/` so they can be shared across Codex, Claude Code, Pi, and other agent harnesses with minimal adaptation.

## Canonical Source

- `.agents/agents/` contains reusable diagnostic and drafting agent instructions.
- `.agents/skills/` contains task workflows.
- `.agents/context/` contains project-specific scientific context, templates, and guardrails.
- Harness-specific directories such as `.claude/`, `.codex/`, and `.pi/` are adapters only. They should be symlinks, generated mirrors, or small configuration layers, not independent workflow forks.

Avoid duplicated divergent definitions. When workflow policy changes, update `.agents/` first and regenerate or relink harness adapters.

## Adapter Rules

- Preserve harness-specific settings, plugin metadata, marketplace manifests, trust files, and model configuration.
- Prefer symlinks from `.claude/agents` and `.codex/agents` to `.agents/agents`, and from `.agents/skills` and `.codex/skills` to `.agents/skills`, when the harness supports symlink discovery.
- If a harness cannot follow symlinks, keep generated mirrors and document the generation command; do not hand-edit the mirror.
- Do not store scientific facts in harness prompts. Store them in `.agents/context/` and load only the files needed for the task.

## Progressive Disclosure

Keep permanent instructions compact:

1. Root policy files (`AGENTS.md`, `CLAUDE.md`, etc.) define repository-wide safety, editing, and validation rules.
2. Skill files define task workflows.
3. Agent files define focused roles.
4. Context files define project-specific scientific facts and guardrails.

Load detailed context only when relevant. For example, a terminology audit should load `terminology.md`; an evidence-bounded result rewrite should also load `evaluation-claims.md`, `claim-ledger.md`, and `do-not-say.md`.

## Human-Controlled Writing Workflow

Reusable writing workflows should preserve this pattern:

1. explicit passage contract;
2. optional argument plan;
3. one main draft;
4. read-only diagnostic review;
5. human selection or approval of findings;
6. one targeted revision;
7. final diff, consistency, and build check.

Reviewer and critic agents diagnose only. They do not rewrite, and their findings should not be fed to the writer until a human accepts them.

## Experimental Comparability

To compare harness or model behavior, keep the shared workflow stable:

- same passage contract;
- same context files and claim guardrails;
- same draft/review/revision limits;
- same validation commands;
- same output formats where practical.

Record deviations in the task notes so output differences can be attributed to the harness, model, context loaded, or workflow variant rather than accidental instruction drift.
