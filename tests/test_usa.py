import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('usa', Path(__file__).resolve().parents[1]/'scripts/usa.py')
usa = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(usa)

class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.config = {'project':'demo', 'profile':'desktop', 'answers':{f'q{i}':f'คำตอบ {i}' for i in range(1,6)}, 'paths':{}}

    def load(self):
        p = self.root/'input.json'
        p.write_text(json.dumps(self.config), encoding='utf-8')
        return usa.load(p)

    def test_all_profiles_and_examples(self):
        for profile in usa.PROFILES:
            self.config['profile'] = profile
            c = self.load(); out = self.root/profile
            usa.initialize(c, out, True)
            self.assertEqual(usa.validate(out), c)
        examples = list((Path(__file__).resolve().parents[1]/'examples').glob('*.json'))
        self.assertEqual(len(examples), 5)
        for p in examples:
            c = usa.load(p); out = self.root/('example-'+p.stem)
            usa.initialize(c, out, True); usa.validate(out)

    def test_preview_and_idempotence(self):
        c = self.load(); out = self.root/'out'
        usa.initialize(c, out); self.assertFalse(out.exists())
        usa.initialize(c, out, True)
        before = {p:p.stat().st_mtime_ns for p in out.rglob('*') if p.is_file()}
        self.assertTrue(all(a == 'UNCHANGED' for a,_ in usa.initialize(c,out,True)))
        self.assertEqual(before, {p:p.stat().st_mtime_ns for p in before})

    def test_adaptive_path(self):
        self.config['paths'] = {'interface':'window','docs':'knowledge'}
        c=self.load(); out=self.root/'out'; usa.initialize(c,out,True)
        self.assertTrue((out/'window/README.md').is_file())
        self.assertTrue((out/'knowledge/PROJECT_BRIEF.md').is_file())
        usa.validate(out)

    def test_reject_unsafe_paths(self):
        for path in ('../outside','/tmp/out','C:/out','a\\b','a/../b','a//b','.git','CON','scripts/inner'):
            with self.subTest(path=path):
                self.config['paths']={'interface':path}
                with self.assertRaises(ValueError): self.load()

    def test_case_collision_and_nested_roles(self):
        for paths in ({'interface':'Tests'},{'interface':'tests/ui'}):
            self.config['paths']=paths
            with self.assertRaises(ValueError): self.load()

    def test_project_credit_reentry_and_plan_edits(self):
        self.config['paths']={'docs':'knowledge'}
        c=self.load(); out=self.root/'out'; usa.initialize(c,out,True)
        for rel in ('README.md','AGENTS.md','ARCHITECTURE.md','knowledge/PLAN.md','knowledge/SYSTEM_FLOW.md','knowledge/HANDOFF.md'):
            self.assertTrue((out/rel).read_text(encoding='utf-8').endswith(usa.CREDIT))
        self.assertIn('knowledge/PLAN.md',(out/'README.md').read_text(encoding='utf-8'))
        self.assertIn('ไม่ถาม initialization 5 ข้อ',(out/'AGENTS.md').read_text(encoding='utf-8'))
        self.assertIn('ต้องการหน้าตาโปรแกรมแบบไหนครับ',(out/'README.md').read_text(encoding='utf-8'))
        p=out/'knowledge/PLAN.md'
        p.write_text(p.read_text(encoding='utf-8').replace('## Mechanism','## Mechanism\n\nProduct-specific details'),encoding='utf-8')
        usa.validate(out)
        p.write_text('## Outcome\n'+usa.CREDIT,encoding='utf-8')
        with self.assertRaises(ValueError): usa.validate(out)

    def test_missing_or_empty_answers(self):
        del self.config['answers']['q5']
        with self.assertRaises(ValueError): self.load()
        self.config['answers']['q5']=' '
        with self.assertRaises(ValueError): self.load()

    def test_conflict_preflight_writes_nothing(self):
        c=self.load(); out=self.root/'out'; out.mkdir()
        p=out/'ARCHITECTURE.md'; p.write_text('user work', encoding='utf-8')
        with self.assertRaises(ValueError): usa.initialize(c,out,True)
        self.assertEqual(p.read_text(), 'user work')
        self.assertFalse((out/'usa.project.json').exists())

    def test_stale_generated_file_fails(self):
        c=self.load(); out=self.root/'out'; usa.initialize(c,out,True)
        (out/'ARCHITECTURE.md').write_text('stale',encoding='utf-8')
        with self.assertRaises(ValueError): usa.validate(out)

    def test_symlink_escape(self):
        out=self.root/'out'; out.mkdir(); outside=self.root/'outside'; outside.mkdir()
        try: (out/'desktop').symlink_to(outside, target_is_directory=True)
        except OSError: self.skipTest('OS denies symlink creation')
        with self.assertRaises(ValueError): usa.initialize(self.load(),out,True)
        self.assertFalse(list(outside.iterdir()))

if __name__ == '__main__': unittest.main()
