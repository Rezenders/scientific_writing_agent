#!/usr/bin/env python3
"""Bootstrap managed scientific-writing files from plugin templates."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PLACEHOLDER_RE = re.compile(r"{{\s*([a-zA-Z0-9_.]+)\s*}}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Set up or refresh scientific-writing repository configuration "
            "from .scientific-writing.json."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root where .scientific-writing.json is read and managed files are written.",
    )
    parser.add_argument(
        "--config",
        default=".scientific-writing.json",
        help="Config path relative to --repo-root (or absolute path).",
    )
    return parser


def resolve_template_root() -> Path:
    script_path = Path(__file__).resolve()
    plugin_root = script_path.parent.parent
    return plugin_root / "assets" / "templates" / "root"


def resolve_config_path(repo_root: Path, config_arg: str) -> Path:
    config_path = Path(config_arg)
    if config_path.is_absolute():
        return config_path
    return repo_root / config_path


def validate_repo_root(repo_root: Path) -> None:
    if not repo_root.exists():
        raise FileNotFoundError(f"Repository root does not exist: {repo_root}")
    if not repo_root.is_dir():
        raise NotADirectoryError(f"Repository root is not a directory: {repo_root}")


def validate_template_root(template_root: Path) -> None:
    if not template_root.exists():
        raise FileNotFoundError(f"Template root does not exist: {template_root}")
    if not template_root.is_dir():
        raise NotADirectoryError(f"Template root is not a directory: {template_root}")
    config_template = template_root / ".scientific-writing.json.tmpl"
    if not config_template.is_file():
        raise FileNotFoundError(f"Missing config template: {config_template}")


def ensure_config(repo_root: Path, template_root: Path, config_arg: str = ".scientific-writing.json") -> Path:
    config_path = resolve_config_path(repo_root, config_arg)
    if config_path.exists():
        if not config_path.is_file():
            raise IsADirectoryError(f"Config path is not a file: {config_path}")
        return config_path

    source = template_root / ".scientific-writing.json.tmpl"
    if not source.is_file():
        raise FileNotFoundError(f"Missing config template: {source}")

    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return config_path


def load_config(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Config root must be a JSON object: {path}")
    return data


def validate_config(config: dict[str, Any]) -> None:
    paper = config.get("paper")
    if not isinstance(paper, dict):
        raise ValueError("paper must be an object")

    research_questions = paper.get("research_questions")
    if not isinstance(research_questions, list) or len(research_questions) < 2:
        raise ValueError("paper.research_questions must be a list with at least 2 items")

    implementation = config.get("implementation", {})
    if not isinstance(implementation, dict):
        raise ValueError("implementation must be an object")

    if "enabled" in implementation and not isinstance(implementation["enabled"], bool):
        raise ValueError("implementation.enabled must be a boolean")

    implementation_paths = implementation.get("paths", {})
    if not isinstance(implementation_paths, dict):
        raise ValueError("implementation.paths must be an object")


def lookup(config: Any, dotted_key: str) -> Any:
    value: Any = config
    for part in dotted_key.split("."):
        if isinstance(value, list) and part.isdigit():
            index = int(part)
            if index < 0 or index >= len(value):
                raise KeyError(f"Missing key: {dotted_key}")
            value = value[index]
            continue
        if isinstance(value, dict) and part in value:
            value = value[part]
            continue
        raise KeyError(f"Missing key: {dotted_key}")
    return value


def render_text(template: str, config: dict[str, Any]) -> str:
    def replace(match: re.Match[str]) -> str:
        return str(lookup(config, match.group(1)))

    return PLACEHOLDER_RE.sub(replace, template)


def should_skip_output(output_rel: Path, config: dict[str, Any]) -> bool:
    implementation = config.get("implementation", {})
    if not isinstance(implementation, dict):
        raise ValueError("implementation must be an object")
    if implementation.get("enabled", False):
        return False
    return "paper-implementation-checker" in output_rel.as_posix()


def write_outputs(repo_root: Path, template_root: Path, config: dict[str, Any]) -> list[Path]:
    written: list[Path] = []
    for template_path in sorted(template_root.rglob("*.tmpl")):
        rel = template_path.relative_to(template_root)
        if rel.name == ".scientific-writing.json.tmpl":
            continue

        output_rel = Path(str(rel)[:-5])
        if should_skip_output(output_rel, config):
            output_path = repo_root / output_rel
            if output_path.exists() and output_path.is_file():
                output_path.unlink()
            continue

        output_path = repo_root / output_rel
        if output_path.exists() and output_path.is_dir():
            raise IsADirectoryError(f"Output path is a directory: {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_text(template_path.read_text(encoding="utf-8"), config)
        output_path.write_text(rendered, encoding="utf-8")
        written.append(output_path)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        repo_root = Path(args.repo_root).resolve()
        validate_repo_root(repo_root)

        template_root = resolve_template_root()
        validate_template_root(template_root)

        config_path = ensure_config(repo_root, template_root, args.config)
        config = load_config(config_path)
        validate_config(config)

        written = write_outputs(repo_root, template_root, config)
    except (OSError, ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {len(written)} managed files")
    for path in written:
        try:
            display_path = path.relative_to(repo_root)
        except ValueError:
            display_path = path
        print(display_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
