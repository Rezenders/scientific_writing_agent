"""Exercise real installation and regeneration, including nested skill resources."""
import importlib.util
import io
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('.agents/skills/scientific-grammar-review')
PREF = Path('.agents/context/style-preferences.md')


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class GrammarInstallationTests(unittest.TestCase):
    def setUp(self):
        self.installer = module('installer', 'scripts/scientific_writing_agent.py')
        self.plugin = module('plugin_setup', 'plugins/scientific-writing/scripts/setup_paper_project.py')

    def assert_resources(self, root):
        for name in ('SKILL.md', 'references/grammatical-patterns.md'):
            expected = (ROOT / SKILL / name).read_bytes()
            for prefix in ('.agents', '.claude', '.codex'):
                actual = root / prefix / 'skills/scientific-grammar-review' / name
                self.assertTrue(actual.is_file())
                self.assertFalse(actual.is_symlink())
                self.assertEqual(actual.read_bytes(), expected)
        self.assertEqual(self.installer.check_skill_frontmatter(root / '.agents/skills'), [])
        self.assertTrue((root / '.agents/skills/write-to-intent/SKILL.md').is_file())
        self.assertTrue((root / PREF).is_file())

    def test_install_update_preserve_preferences_and_nested_resources(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            root = Path(tmp)
            args = ['--repo-root', str(root), '--source-root', str(ROOT)]
            self.assertEqual(self.installer.main(['install'] + args), 0)
            self.assert_resources(root)
            (root / PREF).write_text('Semicolons: avoid.\n')
            for command in ('install', 'update', 'update'):
                self.assertEqual(self.installer.main([command] + args), 0)
                self.assert_resources(root)
                self.assertEqual((root / PREF).read_text(), 'Semicolons: avoid.\n')
            self.assertEqual((root / 'AGENTS.md').read_text().count(self.installer.POLICY_MARKER), 1)
            self.assertEqual((root / '.codex/context/style-preferences.md').read_text(), 'Semicolons: avoid.\n')
            self.assertEqual(self.installer.main(['doctor', '--repo-root', str(root)]), 0)

    def test_update_seeds_preferences_in_older_installation(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            root = Path(tmp)
            context = root / '.agents/context'
            context.mkdir(parents=True)
            (context / 'paper-model.md').write_text('Project-specific build instructions.')
            self.assertEqual(self.installer.main(['update', '--repo-root', str(root)]), 0)
            self.assertTrue((root / PREF).is_file())
            self.assertEqual((context / 'paper-model.md').read_text(), 'Project-specific build instructions.')

    def test_plugin_regeneration_preserves_preferences_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            root = Path(tmp)
            args = ['--repo-root', str(root)]
            self.assertEqual(self.plugin.main(args), 0)
            self.assert_resources(root)
            (root / PREF).write_text('Prefer direct verbs. Semicolons: avoid.\n')
            self.assertEqual(self.plugin.main(args), 0)
            snapshot = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(self.plugin.main(args), 0)
            self.assertEqual(snapshot, {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()})
            self.assert_resources(root)
            self.assertEqual((root / PREF).read_text(), 'Prefer direct verbs. Semicolons: avoid.\n')
            self.assertEqual((root / '.codex/context/style-preferences.md').read_bytes(), (root / PREF).read_bytes())

    def test_changed_canonical_workflows_match_packaged_templates(self):
        paths = [SKILL / 'SKILL.md', SKILL / 'references/grammatical-patterns.md', PREF,
                 Path('.agents/context/manuscript-context.md'),
                 Path('.agents/agents/prose-reviewer.md'), Path('.agents/agents/writer.md')]
        paths += [Path(f'.agents/skills/{n}/SKILL.md') for n in ('write-to-intent', 'section-review', 'diff-review')]
        for rel in paths:
            with self.subTest(path=rel):
                template = ROOT / 'plugins/scientific-writing/assets/templates/root' / (str(rel) + '.tmpl')
                self.assertEqual((ROOT / rel).read_bytes(), template.read_bytes())


if __name__ == '__main__':
    unittest.main()
