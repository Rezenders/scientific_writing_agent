#!/usr/bin/env python3
"""Conservative installer for the scientific-writing agent workflow.

The installer is intended for existing paper repositories. It keeps `.agents/`
as the canonical workflow layer, preserves project-specific context by default,
and creates thin Claude/Codex adapter symlinks when safe.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

AGENT_DIRS = ("agents", "skills")
CONTEXT_FILES = (
    "passage-contract.md",
    "manuscript-context.md",
    "paper-model.md",
    "terminology.md",
    "contributions.md",
    "evaluation-claims.md",
    "claim-ledger.md",
    "do-not-say.md",
    "open-findings.md",
    "reviewer-contracts.md",
)
ADAPTER_LINKS = {
    Path(".claude/agents"): "../.agents/agents",
    Path(".claude/skills"): "../.agents/skills",
    Path(".codex/agents"): "../.agents/agents",
    Path(".codex/skills"): "../.agents/skills",
    Path(".codex/context"): "../.agents/context",
}
POLICY_MARKER = "<!-- scientific-writing-agent canonical-workflow -->"
POLICY_BLOCK = f"""\n{POLICY_MARKER}\n\n## Scientific-Writing Agent Workflow\n\nThis project uses `.agents/` as the canonical shared workflow layer:\n\n- `.agents/agents/` contains reusable agent role instructions.\n- `.agents/skills/` contains reusable manuscript workflows.\n- `.agents/context/` contains project-specific scientific context and guardrails.\n\nHarness-specific directories such as `.claude/`, `.codex/`, and `.pi/` are adapters only. Prefer symlinks or generated mirrors rather than divergent copies. Reviewer and critic agents diagnose only; the writer uses an author-approved passage contract, human-approved findings, and at most one targeted revision.\n"""


def repo_default_source() -> Path:
    return Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Install, update, or validate scientific-writing agent workflows.")
    parser.add_argument("command", choices=("install", "update", "doctor"), nargs="?", default="install")
    parser.add_argument("--repo-root", default=".", help="Target paper repository root.")
    parser.add_argument("--source-root", default=None, help="Source scientific_writing_agent repository root.")
    parser.add_argument("--mode", choices=("symlink", "copy"), default="symlink", help="Install reusable agents/skills as symlinks or copies.")
    parser.add_argument("--force", action="store_true", help="Replace existing reusable workflow paths when needed.")
    parser.add_argument("--force-adapters", action="store_true", help="Replace existing Claude/Codex adapter directories with symlinks.")
    parser.add_argument("--no-policy-block", action="store_true", help="Do not create or append AGENTS.md / CLAUDE.md policy blocks.")
    return parser


def validate_source(source_root: Path) -> None:
    required = [source_root / ".agents" / "HARNESS.md"]
    required += [source_root / ".agents" / name for name in AGENT_DIRS]
    required += [source_root / ".agents" / "context" / name for name in CONTEXT_FILES]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("source root is missing required workflow files:\n" + "\n".join(missing))


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def same_target(path: Path, target: Path) -> bool:
    try:
        return path.resolve() == target.resolve()
    except FileNotFoundError:
        return False


def install_dir(source: Path, dest: Path, mode: str, force: bool, actions: list[str]) -> None:
    if same_target(dest, source):
        actions.append(f"kept existing source path {dest}")
        return
    if dest.exists() or dest.is_symlink():
        if not force:
            actions.append(f"kept existing {dest} (use --force to replace)")
            return
        remove_path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if mode == "symlink":
        dest.symlink_to(source.resolve(), target_is_directory=True)
        actions.append(f"linked {dest} -> {source.resolve()}")
    else:
        shutil.copytree(source, dest)
        actions.append(f"copied {source} -> {dest}")


def copy_file_if_missing(source: Path, dest: Path, force: bool, actions: list[str]) -> None:
    if same_target(dest, source):
        actions.append(f"kept existing source file {dest}")
        return
    if dest.exists() or dest.is_symlink():
        if not force:
            actions.append(f"kept existing {dest} (project-owned)")
            return
        remove_path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    actions.append(f"copied {source} -> {dest}")


def ensure_adapter_link(repo_root: Path, rel: Path, target: str, force: bool, actions: list[str], warnings: list[str]) -> None:
    path = repo_root / rel
    if path.is_symlink() and os.readlink(path) == target:
        actions.append(f"adapter OK {rel} -> {target}")
        return
    if path.exists() or path.is_symlink():
        if not force:
            warnings.append(f"kept existing adapter {rel}; use --force-adapters to replace with {target}")
            return
        remove_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.symlink_to(target, target_is_directory=True)
    actions.append(f"linked adapter {rel} -> {target}")


def append_policy_block(repo_root: Path, filename: str, actions: list[str]) -> None:
    path = repo_root / filename
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if POLICY_MARKER in text:
            actions.append(f"policy block already present in {filename}")
            return
        path.write_text(text.rstrip() + "\n" + POLICY_BLOCK + "\n", encoding="utf-8")
        actions.append(f"appended policy block to {filename}")
    else:
        title = f"# {filename}\n"
        path.write_text(title + POLICY_BLOCK.lstrip() + "\n", encoding="utf-8")
        actions.append(f"created {filename} with policy block")


def install_or_update(args: argparse.Namespace, update_only: bool = False) -> tuple[list[str], list[str]]:
    repo_root = Path(args.repo_root).resolve()
    source_root = Path(args.source_root).resolve() if args.source_root else repo_default_source()
    validate_source(source_root)
    actions: list[str] = []
    warnings: list[str] = []

    target_agents = repo_root / ".agents"
    target_agents.mkdir(parents=True, exist_ok=True)

    force_reusable = args.force or update_only
    for name in AGENT_DIRS:
        install_dir(source_root / ".agents" / name, target_agents / name, args.mode, force_reusable, actions)

    copy_file_if_missing(source_root / ".agents" / "HARNESS.md", target_agents / "HARNESS.md", force_reusable, actions)

    context_dest = target_agents / "context"
    context_dest.mkdir(parents=True, exist_ok=True)
    if not update_only:
        for name in CONTEXT_FILES:
            copy_file_if_missing(source_root / ".agents" / "context" / name, context_dest / name, False, actions)
    else:
        actions.append("left .agents/context project-specific files unchanged")

    for rel, target in ADAPTER_LINKS.items():
        ensure_adapter_link(repo_root, rel, target, args.force_adapters, actions, warnings)

    if not args.no_policy_block and not update_only:
        append_policy_block(repo_root, "AGENTS.md", actions)
        append_policy_block(repo_root, "CLAUDE.md", actions)
    elif update_only:
        actions.append("left AGENTS.md and CLAUDE.md unchanged")

    return actions, warnings


def check_skill_frontmatter(skills_dir: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(skills_dir.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path}: missing frontmatter")
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append(f"{path}: missing closing frontmatter delimiter")
            continue
        frontmatter = text[4:end].splitlines()
        fields = {line.split(":", 1)[0]: line.split(":", 1)[1].strip() for line in frontmatter if ":" in line}
        if not fields.get("name"):
            errors.append(f"{path}: missing name")
        if not fields.get("description"):
            errors.append(f"{path}: missing description")
    return errors


def doctor(repo_root: Path) -> tuple[list[str], list[str]]:
    checks: list[str] = []
    errors: list[str] = []
    agents_root = repo_root / ".agents"
    for rel in [Path(".agents/HARNESS.md"), Path(".agents/agents"), Path(".agents/skills"), Path(".agents/context")]:
        if (repo_root / rel).exists():
            checks.append(f"OK {rel}")
        else:
            errors.append(f"missing {rel}")
    skills = agents_root / "skills"
    if skills.exists():
        fm_errors = check_skill_frontmatter(skills)
        if fm_errors:
            errors.extend(fm_errors)
        else:
            checks.append("OK skill frontmatter")
    for rel, target in ADAPTER_LINKS.items():
        path = repo_root / rel
        if path.is_symlink() and os.readlink(path) == target and path.exists():
            checks.append(f"OK {rel} -> {target}")
        elif path.exists():
            errors.append(f"adapter is not canonical symlink: {rel}")
        else:
            errors.append(f"missing adapter {rel}")
    for filename in ("AGENTS.md", "CLAUDE.md"):
        path = repo_root / filename
        if path.exists() and ".agents/" in path.read_text(encoding="utf-8"):
            checks.append(f"OK {filename} mentions .agents/")
        else:
            errors.append(f"{filename} missing .agents/ policy reference")
    return checks, errors


def print_results(title: str, actions: list[str], warnings: list[str]) -> int:
    print(title)
    for action in actions:
        print(f"- {action}")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 1 if title.endswith("FAILED") else 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        repo_root = Path(args.repo_root).resolve()
        if args.command == "doctor":
            checks, errors = doctor(repo_root)
            if errors:
                return print_results("Doctor FAILED", checks, errors)
            return print_results("Doctor OK", checks, [])
        actions, warnings = install_or_update(args, update_only=args.command == "update")
        title = "Update complete" if args.command == "update" else "Install complete"
        return print_results(title, actions, warnings)
    except Exception as exc:  # noqa: BLE001 - CLI should fail cleanly.
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
