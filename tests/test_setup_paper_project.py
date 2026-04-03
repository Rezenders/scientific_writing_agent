import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "plugins" / "scientific-writing" / "scripts" / "setup_paper_project.py"


def load_module():
    spec = importlib.util.spec_from_file_location("setup_paper_project", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SetupPaperProjectTests(unittest.TestCase):
    def test_resolve_template_root_points_to_plugin_assets(self):
        module = load_module()
        template_root = module.resolve_template_root()
        self.assertTrue(template_root.is_dir())
        self.assertTrue((template_root / ".scientific-writing.json.tmpl").is_file())

    def test_load_config_reads_json(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ".scientific-writing.json"
            path.write_text(json.dumps({"paper": {"title": "X"}}), encoding="utf-8")
            cfg = module.load_config(path)
            self.assertEqual(cfg["paper"]["title"], "X")

    def test_render_text_replaces_known_placeholders(self):
        module = load_module()
        cfg = {
            "paper": {"title": "My Paper", "topic": "ML"},
            "implementation": {"enabled": False},
        }
        rendered = module.render_text("Title: {{ paper.title }}", cfg)
        self.assertEqual(rendered, "Title: My Paper")

    def test_write_outputs_renders_and_skips_implementation_checker_when_disabled(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template_root = root / "templates"
            (template_root / ".codex" / "agents").mkdir(parents=True)
            (template_root / "AGENTS.md.tmpl").write_text(
                "Title: {{ paper.title }}", encoding="utf-8"
            )
            (template_root / ".codex" / "agents" / "paper-implementation-checker.md.tmpl").write_text(
                "Types: {{ implementation.paths.types }}", encoding="utf-8"
            )

            cfg = {
                "paper": {"title": "My Paper"},
                "implementation": {
                    "enabled": False,
                    "paths": {"types": "src/types.py"},
                },
            }
            written = module.write_outputs(root, template_root, cfg)

            self.assertEqual((root / "AGENTS.md").read_text(encoding="utf-8"), "Title: My Paper")
            self.assertFalse((root / ".codex" / "agents" / "paper-implementation-checker.md").exists())
            self.assertIn(root / "AGENTS.md", written)

    def test_ensure_config_creates_file_from_template_if_missing(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template_root = root / "templates"
            template_root.mkdir(parents=True)
            template_text = '{"paper": {"title": "Paper Title"}}\n'
            (template_root / ".scientific-writing.json.tmpl").write_text(template_text, encoding="utf-8")

            config_path = module.ensure_config(root, template_root)
            self.assertEqual(config_path, root / ".scientific-writing.json")
            self.assertEqual(config_path.read_text(encoding="utf-8"), template_text)

    def test_main_returns_non_zero_for_invalid_repo_root(self):
        module = load_module()
        bad_root = REPO_ROOT / "does-not-exist"
        code = module.main(["--repo-root", str(bad_root)])
        self.assertNotEqual(code, 0)

    def test_main_returns_non_zero_for_invalid_json_config(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".scientific-writing.json").write_text("{ not valid json", encoding="utf-8")
            code = module.main(["--repo-root", str(root)])
            self.assertNotEqual(code, 0)

    def test_main_fails_cleanly_when_research_questions_list_is_too_short(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = {
                "paper": {
                    "title": "My Paper",
                    "topic": "X",
                    "format": "Y",
                    "research_questions": ["Only one question"],
                    "entrypoint": "main.tex",
                },
                "build": {
                    "pdf_command": "make pdf",
                    "lint_command": "make lint",
                    "output_pdf": "build/paper.pdf",
                },
                "implementation": {"enabled": False, "paths": {}},
            }
            (root / ".scientific-writing.json").write_text(
                json.dumps(config),
                encoding="utf-8",
            )
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                code = module.main(["--repo-root", str(root)])
            self.assertEqual(code, 1)
            self.assertIn("Error:", stderr.getvalue())
            self.assertIn("research_questions", stderr.getvalue())
            self.assertNotIn("Traceback", stderr.getvalue())

    def test_main_fails_cleanly_when_implementation_section_is_not_an_object(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = {
                "paper": {
                    "title": "My Paper",
                    "topic": "X",
                    "format": "Y",
                    "research_questions": ["RQ1", "RQ2"],
                    "entrypoint": "main.tex",
                },
                "build": {
                    "pdf_command": "make pdf",
                    "lint_command": "make lint",
                    "output_pdf": "build/paper.pdf",
                },
                "implementation": "disabled",
            }
            (root / ".scientific-writing.json").write_text(
                json.dumps(config),
                encoding="utf-8",
            )
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                code = module.main(["--repo-root", str(root)])
            self.assertEqual(code, 1)
            self.assertIn("Error:", stderr.getvalue())
            self.assertIn("implementation", stderr.getvalue())
            self.assertNotIn("Traceback", stderr.getvalue())

    def test_write_outputs_prunes_stale_implementation_checker_when_disabled(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template_root = root / "templates"
            (template_root / ".codex" / "agents").mkdir(parents=True)
            (template_root / ".codex" / "agents" / "paper-implementation-checker.md.tmpl").write_text(
                "Types: {{ implementation.paths.types }}",
                encoding="utf-8",
            )

            enabled_cfg = {
                "paper": {"title": "My Paper"},
                "implementation": {
                    "enabled": True,
                    "paths": {"types": "src/types.py"},
                },
            }
            disabled_cfg = {
                "paper": {"title": "My Paper"},
                "implementation": {
                    "enabled": False,
                    "paths": {"types": "src/types.py"},
                },
            }

            module.write_outputs(root, template_root, enabled_cfg)
            checker_path = root / ".codex" / "agents" / "paper-implementation-checker.md"
            self.assertTrue(checker_path.exists())

            module.write_outputs(root, template_root, disabled_cfg)
            self.assertFalse(checker_path.exists())


if __name__ == "__main__":
    unittest.main()
