# Scientific Writing Plugin Design

## Goal

Create a repo-local Codex plugin that can bootstrap and refresh the scientific-writing configuration for the current repository through a single setup workflow. The plugin should make it easy to adapt the generic template to a specific paper project without manually editing many files.

## Scope

This design covers:

- a repo-local plugin scaffold under `plugins/`
- a setup skill discoverable by Codex
- a script-backed bootstrap workflow that updates the current repository in place
- a small repo-local config file used as the source of truth for paper-specific values

This design does not cover:

- publishing to a shared marketplace outside the repository
- Claude-specific plugin packaging
- migration of the existing Claude workflows into a Claude plugin system

## Requirements

### Functional

1. Codex should be able to use a repo-local plugin to configure a paper repository.
2. The setup workflow should target the current repository in place.
3. The workflow should collect or read paper-specific values and apply them consistently across managed files.
4. The workflow should support both:
   - paper-only repositories
   - papers with an associated implementation codebase
5. The workflow should be rerunnable so a repo can be refreshed after the paper configuration changes.

### Non-Functional

1. The setup path should minimize manual editing.
2. Template-managed changes should be deterministic.
3. The file layout should remain understandable to humans without plugin knowledge.
4. The repo should keep version-controlled local copies of the final writing configuration.

## Recommended Approach

Use a hybrid repo-local plugin with a script-backed setup skill.

The plugin provides the user-facing entry point and reusable setup logic. The script performs the actual repository updates. The final generated files remain checked into the paper repository so everyday writing tasks do not depend on live plugin execution.

## Alternatives Considered

### 1. Script only

Pros:

- simplest implementation
- minimal Codex plugin surface area

Cons:

- weaker UX
- less discoverable
- no obvious repo-local “setup this paper” workflow for Codex

### 2. Put all writing workflows inside the plugin

Pros:

- less duplication of `.codex/skills/*`
- centralizes reusable Codex behavior

Cons:

- increases runtime dependence on plugin availability
- makes each repo less self-contained
- creates more coupling between plugin evolution and existing paper repos

### 3. Recommended hybrid

Pros:

- clean user entry point
- deterministic setup
- generated repo stays self-contained
- easy to rerun when project metadata changes

Cons:

- slightly more moving parts than a script-only design

## Architecture

### Plugin Root

The plugin should live at:

- `plugins/scientific-writing/`

It should contain:

- `.codex-plugin/plugin.json`
- `skills/setup-paper-project/SKILL.md`
- `scripts/setup_paper_project.py`
- `assets/templates/...`

### Managed Templates

The plugin should own template copies of:

- `AGENTS.md`
- `.codex/agents/*`
- `.codex/skills/*`
- `.codex/context/manuscript-context.md`
- `CLAUDE.md`
- `.claude/agents/*`
- `.claude/skills/*`

These should live under the plugin template directory, not be generated inline inside Python string literals.

### Repo Config File

Add a machine-readable config file at repo root:

- `.scientific-writing.json`

This becomes the source of truth for paper-specific values. The setup script reads it, prompts for missing values when needed, and rewrites managed files from it.

## Data Model

The config file should contain:

- `paper.title`
- `paper.topic`
- `paper.format`
- `paper.research_questions`
- `paper.entrypoint`
- `paper.sections`
- `paper.support_files`
- `build.pdf_command`
- `build.lint_command`
- `build.output_pdf`
- `annotations.commands`
- `macros.key_macros`
- `terminology.rules`
- `implementation.enabled`
- `implementation.paths`

The implementation section should be optional. If disabled, the setup workflow should either omit or clearly mark the implementation-checker files as inactive.

## Workflow

### Initial Setup

1. User asks Codex to use the scientific-writing setup skill.
2. The skill explains what it configures.
3. The skill gathers required missing values or instructs the script to read them from `.scientific-writing.json`.
4. The script writes or updates:
   - `AGENTS.md`
   - `.codex/...`
   - `CLAUDE.md`
   - `.claude/...`
5. The script prints a summary of what changed and any remaining placeholders.

### Refresh / Reconfigure

1. User updates `.scientific-writing.json` or answers prompts again.
2. User reruns the setup skill.
3. The script re-renders managed files.
4. The script reports drift and updated files.

## Update Strategy

Managed files should be treated as generated from templates plus config values.

Preferred behavior:

- deterministic overwrite for fully generated files
- no attempt to merge arbitrary hand edits inside generated files
- clear header comments in generated files warning that the setup command owns them

This is more reliable than partial in-file patching for template-heavy prompt files.

## File Ownership

### Generated / Managed by Setup

- `AGENTS.md`
- `CLAUDE.md`
- `.codex/agents/*`
- `.codex/skills/*`
- `.codex/context/manuscript-context.md`
- `.claude/agents/*`
- `.claude/skills/*`

### User-Owned

- manuscript `.tex` sources
- bibliography files
- figures
- `.scientific-writing.json`

### Mixed / Optional

- `.claude/agent-memory/*`

These may still be created by setup, but their future contents are user- and agent-driven rather than regenerated from the plugin.

## Error Handling

The script should fail clearly when:

- the current directory is not a writable repository
- a required config field is missing and non-interactive mode is requested
- a configured path is invalid
- a managed output path already exists with an unexpected incompatible type

The script should warn, not fail, when:

- implementation support is disabled
- optional paths are missing
- placeholders remain in optional sections

## Testing Strategy

### Unit-Level

Test:

- config parsing
- template rendering
- path normalization
- implementation-enabled versus implementation-disabled generation

### Integration-Level

Test the bootstrap command in a temporary fixture repo and verify:

- expected files are created
- expected placeholders are replaced
- rerunning is idempotent for unchanged config
- implementation-disabled mode omits or deactivates implementation-specific sections correctly

## Rollout Plan

### Phase 1

Create the plugin scaffold and manifest.

### Phase 2

Add the setup skill and bootstrap script.

### Phase 3

Move the current repo templates into plugin-owned template assets.

### Phase 4

Add tests and documentation for the new setup flow.

### Phase 5

Optionally reduce top-level duplication in the template repo once the plugin path is stable.

## Open Decisions Resolved

- Plugin location: repo-local
- Target repository: current repository in place
- Setup mechanism: script-first, exposed through a skill
- Reusable source of truth: yes, via `.scientific-writing.json`

## Success Criteria

The design is successful if a user can:

1. clone or copy this repo,
2. ask Codex to run the scientific-writing setup workflow,
3. answer a compact set of questions or edit one config file,
4. get a fully configured `AGENTS.md`, `.codex/`, `CLAUDE.md`, and `.claude/` layout for the specific paper,
5. rerun the workflow later without manual multi-file maintenance.
