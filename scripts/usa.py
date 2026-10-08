"""USA scaffold: standard-library only, no shell execution or dependency installs."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROLES = ('interface', 'application', 'domain', 'infrastructure', 'contracts', 'tests', 'operations', 'docs')
PROFILES = {
    'web': dict(zip(ROLES, ('apps/web', 'src/application', 'src/domain', 'src/infrastructure', 'contracts', 'tests', 'ops', 'docs'))),
    'desktop': dict(zip(ROLES, ('desktop/ui', 'desktop/application', 'desktop/domain', 'desktop/adapters', 'contracts', 'tests', 'ops', 'docs'))),
    'cli': dict(zip(ROLES, ('cli', 'core/use_cases', 'core/domain', 'adapters', 'contracts', 'tests', 'ops', 'docs'))),
    'service': dict(zip(ROLES, ('api', 'src/application', 'src/domain', 'src/infrastructure', 'contracts', 'tests', 'ops', 'docs'))),
    'data': dict(zip(ROLES, ('entrypoints', 'pipelines', 'rules', 'connectors', 'schemas', 'tests', 'ops', 'docs'))),
}
RESPONSIBILITIES = {
    'interface': 'รับ input และแสดงผล; ส่งงานให้ application; ห้ามซ่อนกฎธุรกิจใน UI',
    'application': 'จัดลำดับ use case และกำหนด ports; ใช้ domain; ไม่ผูกกับ SDK ผู้ให้บริการ',
    'domain': 'กฎธุรกิจและ invariants; ไม่ import UI, database หรือ framework',
    'infrastructure': 'adapters สำหรับ persistence และบริการภายนอก; implement ports',
    'contracts': 'ข้อตกลงข้อมูลและ public interfaces; ระบุ compatibility และ validation',
    'tests': 'หลักฐานตรวจ behavior, boundaries และ acceptance criteria',
    'operations': 'คู่มือ config, deploy, recovery และ observability; ห้ามใส่ secrets',
    'docs': 'เหตุผลการออกแบบ, แผนที่โปรแกรม, ขอบเขตและการส่งต่อ',
}

def relative(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('Path must be a non-empty POSIX relative path')
    p = PurePosixPath(value)
    if p.is_absolute() or any(x in ('', '.', '..') for x in value.split('/')):
        raise ValueError('Absolute paths and traversal are forbidden')
    if any(not re.fullmatch(r'[A-Za-z0-9_-]+', x) for x in p.parts):
        raise ValueError('Path segments allow ASCII letters, digits, hyphen and underscore only')
    if any(x.upper() in {'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))} for x in p.parts):
        raise ValueError('Windows reserved names are forbidden')
    if p.parts[0] in {'scripts', 'assets', 'examples'}:
        raise ValueError('Path overlaps template tooling')
    return value

def load(path):
    c = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if set(c) != {'project', 'profile', 'answers', 'paths'}:
        raise ValueError('Expected project, profile, answers, paths only')
    if not isinstance(c['project'], str) or not re.fullmatch(r'[a-z][a-z0-9-]{0,63}', c['project']):
        raise ValueError('Project must be a lowercase slug, max 64 characters')
    if not isinstance(c['profile'], str) or c['profile'] not in PROFILES:
        raise ValueError('Unknown profile')
    if not isinstance(c['answers'], dict) or set(c['answers']) != {f'q{i}' for i in range(1,6)}:
        raise ValueError('Exactly q1 through q5 are required')
    if any(not isinstance(v, str) or not v.strip() for v in c['answers'].values()):
        raise ValueError('Every answer must be non-empty text; record unknowns explicitly')
    if not isinstance(c['paths'], dict) or set(c['paths']) - set(ROLES):
        raise ValueError('Invalid path role')
    paths = PROFILES[c['profile']] | c['paths']
    for v in paths.values(): relative(v)
    values = list(paths.values())
    for i, a in enumerate(values):
        for b in values[i+1:]:
            if a.casefold() == b.casefold() or a.casefold().startswith(b.casefold()+'/') or b.casefold().startswith(a.casefold()+'/'):
                raise ValueError('Role paths must be distinct and non-nested, including case differences')
    c['paths'] = paths
    return c

def render(c):
    files = {'usa.project.json': json.dumps(c, ensure_ascii=False, indent=2)+'\n'}
    rows = '\n'.join(f'| {r} | `{c["paths"][r]}` | {RESPONSIBILITIES[r]} |' for r in ROLES)
    files['ARCHITECTURE.md'] = f'# {c["project"]} — แผนที่โปรแกรม\n\nสถานะ: SCAFFOLDED / application NOT_IMPLEMENTED\n\n## Role → Path\n\n| Role | Path | Responsibility |\n|---|---|---|\n{rows}\n\n## Dependency direction\n\ninterface → application → domain; infrastructure → application ports/domain; contracts เป็นข้อตกลงร่วม\n\n## Runtime flow\n\nInput → boundary validation → use case → domain → port → adapter → result → output\n\n## Source of truth\n\nusa.project.json เป็นเจ้าของคำตอบและ path; เอกสารนี้เป็น generated view ห้ามแก้ mapping แยกจาก config\n\n## Constraints / data / integrations\n\nดู [{c["paths"]["docs"]}/PROJECT_BRIEF.md]({c["paths"]["docs"]}/PROJECT_BRIEF.md); ยังไม่มี runtime, storage หรือ API ที่พิสูจน์แล้ว\n\n## Verification\n\nตรวจ structural consistency ด้วย scripts/usa.py validate; Dev ต้องเพิ่ม build, behavior, integration และ acceptance checks ตาม stack\n'
    d = c['paths']['docs']
    brief = '\n\n'.join(f'## {k.upper()}\n\n{v}' for k,v in c['answers'].items())
    files[f'{d}/PROJECT_BRIEF.md'] = f'# {c["project"]} — Project Brief\n\n{brief}\n\nคำตอบผู้ใช้เป็น reported requirements; ทางเลือกของ Agent ต้องลง ADR พร้อมเหตุผลและสถานะ inferred\n'
    files[f'{d}/HANDOFF.md'] = '# Dev Handoff\n\nสถานะ: STRUCTURE_READY; APPLICATION_NOT_IMPLEMENTED\n\n- อ่าน PROJECT_BRIEF.md และ ARCHITECTURE.md\n- ตัดสิน stack/version จากข้อจำกัดและลง ADR\n- เริ่มหนึ่ง vertical slice: input → use case → domain → adapter → result\n- เพิ่ม contracts, behavior tests, build/run commands และ acceptance evidence\n- Security: auth, input validation, secret handling, least privilege และ error redaction ยัง NOT_RUN\n- Production/deploy/device acceptance: NOT_RUN\n- ห้ามอ้าง scaffold validation ว่าโปรแกรมทำงานจริง\n'
    files[f'{d}/decisions/0001-structure.md'] = '# ADR 0001 — Adaptive structure\n\nStatus: accepted for scaffolding\n\nContext: คงหน้าที่ของ USA และเลือก path ตาม profile/คำตอบ\n\nDecision: usa.project.json คือ canonical map; folder name เปลี่ยนได้ผ่าน config\n\nConsequences: ไม่กำหนด framework; Dev ต้องตรวจ dependencies ในโค้ดจริง\n\nAlternatives: ใช้โครงของ framework เดิมและ map role ให้ตรง โดยไม่ย้ายไฟล์เพียงเพื่อชื่อ\n'
    for r,p in c['paths'].items():
        prefix = '../' * len(PurePosixPath(p).parts)
        files[f'{p}/README.md'] = f'# {r}\n\n{RESPONSIBILITIES[r]}\n\nสถานะ: ยังไม่มี application implementation\n\nดู [ARCHITECTURE.md]({prefix}ARCHITECTURE.md); authoritative path อยู่ใน usa.project.json\n'
    return files

def safe_target(root, rel):
    p = root / rel
    for part in [p, *p.parents]:
        if part.is_symlink(): raise ValueError('Symlinks are forbidden in generated output paths')
        if part == root: break
    if not p.resolve().is_relative_to(root.resolve()): raise ValueError('Path escapes output root')
    return p

def initialize(c, root, apply=False):
    root = Path(root).absolute()
    if root.is_symlink(): raise ValueError('Symlink output root is forbidden')
    files = render(c)
    actions = []
    for rel, content in files.items():
        p = safe_target(root, rel)
        if p.exists():
            if not p.is_file() or p.read_text(encoding='utf-8') != content:
                raise ValueError(f'Conflict: {rel}; no files written. Use a fresh output directory.')
            actions.append(('UNCHANGED', rel))
        else: actions.append(('CREATE', rel))
    if apply:
        # Preflight all paths before mutation. Run only in an isolated local workspace.
        for rel, content in files.items():
            p = safe_target(root, rel)
            if not p.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
                with p.open('x', encoding='utf-8', newline='\n') as f: f.write(content)
    return actions

def validate(root):
    root = Path(root).absolute()
    c = load(root/'usa.project.json')
    for rel, content in render(c).items():
        p = safe_target(root, rel)
        if not p.is_file() or p.read_text(encoding='utf-8') != content:
            raise ValueError(f'Missing or stale generated file: {rel}')
    return c

def main():
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='command', required=True)
    i = s.add_parser('init'); i.add_argument('--config', required=True); i.add_argument('--output', required=True); i.add_argument('--apply', action='store_true')
    v = s.add_parser('validate'); v.add_argument('--root', required=True)
    a = p.parse_args()
    try:
        if a.command == 'init':
            for action, rel in initialize(load(a.config), a.output, a.apply): print(action, rel)
            print('APPLIED' if a.apply else 'DRY_RUN: add --apply to write')
        else:
            validate(a.root); print('PASS: scaffold mapping/content consistent; application tests NOT_RUN')
    except (ValueError, OSError, TypeError, KeyError) as e:
        print(f'FAIL: {e}', file=sys.stderr); return 1
    return 0

if __name__ == '__main__': sys.exit(main())
