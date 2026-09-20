# Setup Checklist

Follow these steps when adding the scientific-writing workflow to an existing paper project.

## Recommended install

From anywhere, run the conservative installer against your paper repository:

```bash
python3 /path/to/scientific_writing_agent/scripts/scientific_writing_agent.py install \
  --repo-root /path/to/your-paper-repo \
  --mode symlink
```

Then validate the installation:

```bash
python3 /path/to/scientific_writing_agent/scripts/scientific_writing_agent.py doctor \
  --repo-root /path/to/your-paper-repo
```

What this does:

- installs `.agents/` as the canonical workflow layer;
- links `.agents/agents` and `.agents/skills` to the reusable workflow source by default;
- creates local starter templates under `.agents/context/` without overwriting existing context files;
- creates Claude/Codex adapter symlinks when safe;
- appends a short `.agents/` policy block to `AGENTS.md` and `CLAUDE.md` instead of replacing existing project policy.

If symlinks are not suitable for your environment, use copies:

```bash
python3 /path/to/scientific_writing_agent/scripts/scientific_writing_agent.py install \
  --repo-root /path/to/your-paper-repo \
  --mode copy
```

To refresh reusable workflows later without overwriting project-specific context:

```bash
python3 /path/to/scientific_writing_agent/scripts/scientific_writing_agent.py update \
  --repo-root /path/to/your-paper-repo
```

## Harness layout

- `.agents/` is canonical.
- `.claude/`, `.codex/`, and `.pi/` are adapters only.
- Prefer adapter symlinks or generated mirrors; do not maintain divergent copies of agent and skill instructions.
- Keep plugin and marketplace metadata if your harness uses it.

## Project-specific customization

After installation, either run the `bootstrap-project-context` skill or manually fill in the context templates under `.agents/context/`.

Use `bootstrap-project-context` when you want the agent to inspect the repository, ask a minimal questionnaire, and propose context-file updates for approval.

Manual checklist:

1. `manuscript-context.md` — compact index and active manuscript entry point.
2. `paper-model.md` — section map, build commands, validation commands, implementation references.
3. `terminology.md` — canonical terms, acronyms, macros, and distinctions.
4. `contributions.md` — approved contribution statements and narrative commitments.
5. `evaluation-claims.md` — evidence-backed result claims and limits.
6. `claim-ledger.md` — high-risk claims with evidence and qualifications.
7. `do-not-say.md` — prohibited overclaims and fragile phrasings.
8. `reviewer-contracts.md` and `open-findings.md` — active review-response and diagnostic state.

Use placeholders such as `<PROJECT_NAME>`, `<MAIN_TEX>`, `<SECTION_FILE>`, `<KEY_MACRO>`, `<IMPLEMENTATION_REFERENCE>`, and `<EVALUATION_CLAIM>` until paper-specific facts are known.

## Build and validation setup

Record the project commands in `.agents/context/paper-model.md`:

```bash
<BUILD_COMMAND>
<LINT_COMMAND>
<OPTIONAL_DIFF_LINT_COMMAND>
```

Typical examples:

```bash
make pdf
make lint
make lint-diff
```

The `paper-build`, `pre-submission`, and review skills read this context rather than assuming a fixed LaTeX layout.

## Optional memory bootstrap

After the `.agents/context/` files are populated, you may run `bootstrap-memory` if your harness uses agent memory files. Do not use `bootstrap-memory` as the initial questionnaire; it assumes the core project context is already known or inferable.

## Writing workflow rule

For substantive drafting or rewriting, preserve this sequence:

1. explicit passage contract;
2. optional argument plan;
3. one main draft;
4. read-only diagnostic review;
5. human approval of findings;
6. one targeted revision;
7. final diff, consistency, and build check.

Reviewer and critic agents diagnose only. They do not rewrite, and their findings should not be passed to the writer until a human accepts them.

## Plugin bootstrap alternative

The repo-local plugin script remains available for projects that want generated files from `.scientific-writing.json`:

```bash
python3 plugins/scientific-writing/scripts/setup_paper_project.py --repo-root .
```

In plugin-first mode, edit `.scientific-writing.json` and templates under `plugins/scientific-writing/assets/templates/root/.agents/`; rerunning the plugin script rewrites managed outputs and recreates adapter symlinks.
