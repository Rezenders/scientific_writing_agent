import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "scientific_writing_agent.py"


def load_module():
    spec = importlib.util.spec_from_file_location("scientific_writing_agent", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ScientificWritingAgentInstallerTests(unittest.TestCase):
    def test_install_preserves_existing_policy_and_creates_links(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("# Existing Policy\n", encoding="utf-8")

            code = module.main([
                "install",
                "--repo-root",
                str(root),
                "--source-root",
                str(REPO_ROOT),
            ])

            self.assertEqual(code, 0)
            self.assertTrue((root / ".agents" / "agents").is_symlink())
            self.assertTrue((root / ".agents" / "skills").is_symlink())
            self.assertTrue((root / ".codex" / "context").is_symlink())
            self.assertTrue((root / ".agents" / "context" / "paper-model.md").is_file())
            agents_text = (root / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("# Existing Policy", agents_text)
            self.assertIn(module.POLICY_MARKER, agents_text)

    def test_update_leaves_context_and_policy_unchanged(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            context = root / ".agents" / "context"
            context.mkdir(parents=True)
            (context / "paper-model.md").write_text("custom", encoding="utf-8")
            (root / "AGENTS.md").write_text("# Existing\n", encoding="utf-8")

            code = module.main([
                "update",
                "--repo-root",
                str(root),
                "--source-root",
                str(REPO_ROOT),
            ])

            self.assertEqual(code, 0)
            self.assertEqual((context / "paper-model.md").read_text(encoding="utf-8"), "custom")
            self.assertEqual((root / "AGENTS.md").read_text(encoding="utf-8"), "# Existing\n")

    def test_doctor_reports_clean_install(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertEqual(module.main(["install", "--repo-root", str(root), "--source-root", str(REPO_ROOT)]), 0)
            self.assertEqual(module.main(["doctor", "--repo-root", str(root)]), 0)


if __name__ == "__main__":
    unittest.main()
