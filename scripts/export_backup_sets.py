#!/usr/bin/env python3
"""Curated local export sets for Chris's GitHub backup repos.

This script prepares two local repository-shaped datasets without copying
Hermes runtime secrets, sessions, auth stores, gateway logs, or .env files.

Targets:
- chris-obd-homepage-data: Faker/homepage/dashboard source + curated webapp data
- chris-karina-agent-system: public-safe-ish Karina/team system docs, skills, plans
"""

from __future__ import annotations

import fnmatch
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/opt/data/github-backup-sets')
REPOS = ROOT / 'repos'
HOMEPAGE_REPO = REPOS / 'chris-obd-homepage-data'
AGENT_REPO = REPOS / 'chris-karina-agent-system'

SOURCES = {
    'august_dashboard': Path('/opt/data/projects/august-dashboard'),
    'webapp_loop': Path('/opt/data/hermes-webapp-build-loop'),
    'agent_team_log': Path('/opt/data/agent-team-work-log'),
    'skills': Path('/opt/data/skills'),
    'hermes_plans': Path('/opt/data/.hermes/plans'),
    'karina_soul': Path('/opt/data/SOUL.md'),
    'profiles': Path('/opt/data/profiles'),
}

TEXT_EXTS = {
    '.md', '.txt', '.json', '.jsonl', '.ts', '.tsx', '.js', '.mjs', '.css', '.html',
    '.svg', '.yaml', '.yml', '.toml', '.lock', '.gitignore', '.example', '.py'
}

SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|access[_-]?token|refresh[_-]?token|bot[_-]?token|oauth|secret|password)\s*[:=]\s*["\']?[^"\'\s]{12,}'),
    re.compile(r'(?i)(TELEGRAM|SLACK|OPENAI|ANTHROPIC|OPENROUTER|GITHUB|GEMINI|GOOGLE|HIGGSFIELD|MINIMAX|ELEVENLABS)[A-Z0-9_]*\s*[:=]\s*["\']?[^"\'\s]{12,}'),
    re.compile(r'xox[baprs]-[A-Za-z0-9-]{20,}'),
    re.compile(r'\b[0-9]{8,}:[A-Za-z0-9_-]{30,}\b'),
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{30,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{20,}'),
]

GLOBAL_EXCLUDE_NAMES = {
    '.git', '.env', '.env.local', '.env.production', '.env.development', 'auth.json',
    'state.db', 'state.db-shm', 'state.db-wal', 'node_modules', '__pycache__', '.pytest_cache',
    '.mypy_cache', '.ruff_cache', '.DS_Store', '.cache', 'logs', 'sessions', 'audio_cache',
    '.archive', '.curator_backups', '.curator_state', '.usage.json',
}

GLOBAL_EXCLUDE_GLOBS = [
    '*.pem', '*.key', '*.crt', '*.p12', '*.sqlite', '*.db', '*.log', '*.bak', '*.tmp',
    '*token*', '*credential*', '*credentials*', '*auth*', '*.telegram-status.txt',
    'send_*telegram*.py', '*telegram-dm.txt',
]


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def excluded(path: Path, root: Path, extra_globs: list[str] | None = None, md_only: bool = False) -> bool:
    rel = path.relative_to(root)
    parts = set(rel.parts)
    if parts & GLOBAL_EXCLUDE_NAMES:
        return True
    globs = GLOBAL_EXCLUDE_GLOBS + (extra_globs or [])
    name = path.name
    rel_posix = rel.as_posix()
    if any(fnmatch.fnmatch(name, pat) or fnmatch.fnmatch(rel_posix, pat) for pat in globs):
        return True
    if md_only and path.is_file() and path.suffix.lower() != '.md':
        return True
    return False


def copy_tree_filtered(src: Path, dst: Path, *, extra_globs: list[str] | None = None, md_only: bool = False) -> list[str]:
    copied: list[str] = []
    if not src.exists():
        return copied
    for path in src.rglob('*'):
        if excluded(path, src, extra_globs=extra_globs, md_only=md_only):
            continue
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, out)
        copied.append(str(out.relative_to(dst)))
    return copied


def copy_file(src: Path, dst: Path) -> bool:
    if not src.exists() or src.name in GLOBAL_EXCLUDE_NAMES:
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def write_common_repo_files(repo: Path, title: str, description: str) -> None:
    (repo / '.gitignore').write_text(
        '\n'.join([
            '# Secrets / local runtime',
            '.env', '.env.*', '!.env.example', 'auth.json', 'state.db*', '*.db', '*.sqlite',
            '*.log', 'logs/', 'sessions/', 'request_dumps/', 'credential*', '*token*', '*secret*',
            '',
            '# Dependencies / generated cache',
            'node_modules/', 'dist/', '.cache/', '__pycache__/', '.pytest_cache/', '.DS_Store',
            '',
        ]) + '\n',
        encoding='utf-8',
    )
    (repo / '.env.example').write_text(
        '# Placeholder only. Never commit real tokens or OAuth credentials.\n'
        'PROVIDER_KEY=replace_me\n',
        encoding='utf-8',
    )
    (repo / 'README.md').write_text(
        f'# {title}\n\n{description}\n\n'
        '## Backup safety\n'
        '- This repository is produced from a curated allowlist export.\n'
        '- Do not copy `.env`, OAuth/auth stores, session DBs, gateway logs, raw DMs, or credential pools.\n'
        '- Before each push, run `python scripts/scan_export_safety.py .`.\n'
        '- Start private on GitHub; decide public visibility separately later.\n',
        encoding='utf-8',
    )


def write_homepage_pages_workflow(repo: Path) -> None:
    """Add GitHub Pages deployment for the August dashboard sub-app."""
    workflow = repo / '.github' / 'workflows' / 'pages.yml'
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(
        '''name: Deploy August dashboard to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: august-dashboard/package-lock.json
      - name: Install dependencies
        working-directory: august-dashboard
        run: npm ci
      - name: Build
        working-directory: august-dashboard
        run: npm run build
      - name: Configure Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: august-dashboard/dist
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
''',
        encoding='utf-8',
    )
    (repo / 'README.md').write_text(
        (repo / 'README.md').read_text(encoding='utf-8')
        + '\n## GitHub Pages\n'
        + '- Webapp repo: `https://github.com/woongs2021/Hermes-project-webapp`\n'
        + '- Pages URL after the first successful workflow run: `https://woongs2021.github.io/Hermes-project-webapp/`\n'
        + '- The Vite app uses `base: /Hermes-project-webapp/` so assets resolve correctly under GitHub Pages.\n',
        encoding='utf-8',
    )


def export_homepage() -> dict:
    reset_dir(HOMEPAGE_REPO)
    write_common_repo_files(
        HOMEPAGE_REPO,
        'Chris Hermes Project Webapp',
        'Faker-built webapp/dashboard source and curated public-facing data for Chris’s Hermes/OBD/August dashboard work.',
    )
    write_homepage_pages_workflow(HOMEPAGE_REPO)
    copied: dict[str, int] = {}

    copied['august_dashboard'] = len(copy_tree_filtered(
        SOURCES['august_dashboard'],
        HOMEPAGE_REPO / 'august-dashboard',
        extra_globs=['dist/*', 'screenshots/*'],
    ))
    copied['august_dashboard_safe_sources'] = len(copy_tree_filtered(
        SOURCES['august_dashboard'].parent / 'august-dashboard-safe-sources',
        HOMEPAGE_REPO / 'august-dashboard-safe-sources',
    ))

    loop = SOURCES['webapp_loop']
    selected = ['SCHEMA.md', 'events.jsonl']
    for file_name in selected:
        copy_file(loop / file_name, HOMEPAGE_REPO / 'webapp-build-loop' / file_name)
    copied['webapp_candidates'] = len(copy_tree_filtered(loop / 'candidates', HOMEPAGE_REPO / 'webapp-build-loop' / 'candidates'))
    copied['webapp_plans'] = len(copy_tree_filtered(loop / 'plans', HOMEPAGE_REPO / 'webapp-build-loop' / 'plans'))
    copied['webapp_daily_md'] = len(copy_tree_filtered(loop / 'daily', HOMEPAGE_REPO / 'webapp-build-loop' / 'daily', md_only=True))
    copied['image_gallery_data'] = len(copy_tree_filtered(
        loop / 'data' / 'image-gallery',
        HOMEPAGE_REPO / 'webapp-build-loop' / 'data' / 'image-gallery',
        extra_globs=['pending/*', 'private*', '*prompt*'],
    ))
    copied['image_gallery_assets'] = len(copy_tree_filtered(
        loop / 'assets' / 'image-gallery',
        HOMEPAGE_REPO / 'webapp-build-loop' / 'assets' / 'image-gallery',
    ))
    return copied


def export_agent_system() -> dict:
    reset_dir(AGENT_REPO)
    write_common_repo_files(
        AGENT_REPO,
        'Chris Karina Agent System',
        'Curated private backup of Karina-led Hermes agent-team structure, operating docs, skills, and safe work-log memory.',
    )
    copied: dict[str, int] = {}

    copied['agent_team_work_log_md'] = len(copy_tree_filtered(
        SOURCES['agent_team_log'],
        AGENT_REPO / 'agent-team-work-log',
        md_only=True,
    ))
    copied['skills'] = len(copy_tree_filtered(
        SOURCES['skills'],
        AGENT_REPO / 'skills',
    ))
    copied['hermes_plans'] = len(copy_tree_filtered(
        SOURCES['hermes_plans'],
        AGENT_REPO / 'hermes-plans',
        md_only=True,
    ))

    # Only persona/routing documents are exported from profiles; never copy runtime state.
    copied['karina_soul'] = int(copy_file(
        SOURCES['karina_soul'], AGENT_REPO / 'system' / 'souls' / 'karina' / 'SOUL.md'
    ))
    copied['specialist_souls'] = 0
    for profile in ['yuna', 'goyounjung', 'son', 'faker', 'muyeol']:
        copied['specialist_souls'] += int(copy_file(
            SOURCES['profiles'] / profile / 'SOUL.md',
            AGENT_REPO / 'system' / 'souls' / profile / 'SOUL.md',
        ))

    docs = AGENT_REPO / 'docs'
    docs.mkdir(parents=True, exist_ok=True)
    (docs / 'restore-notes.md').write_text(
        '# Restore notes\n\n'
        '- This repo is not a raw Hermes home copy. It is a curated backup.\n'
        '- Recreate real `.env`, OAuth auth, gateway home channels, and profile-specific tokens manually on the target machine.\n'
        '- Copy skills/docs back only after reviewing paths and profile ownership.\n'
        '- Never restore old `state.db`, session transcripts, or gateway logs from GitHub.\n',
        encoding='utf-8',
    )
    (docs / 'repo-boundary.md').write_text(
        '# Repository boundary\n\n'
        '## Included\n'
        '- Agent role/system documentation\n'
        '- Markdown daily work memory where useful\n'
        '- Local skills and reusable workflows\n'
        '- Planning documents\n\n'
        '## Excluded\n'
        '- `.env`, `auth.json`, tokens, OAuth stores, credential pools\n'
        '- Telegram/Slack raw IDs where avoidable, raw DMs, gateway logs\n'
        '- Hermes `state.db`, sessions, request dumps, caches\n',
        encoding='utf-8',
    )
    (docs / 'system-restore-scope.md').write_text(
        '# Hermes system restore scope\n\n'
        '## Captured\n'
        '- Karina and active specialist `SOUL.md` role/routing documents\n'
        '- Curated skills, operational workflows, plans, and agent-team Markdown work memory\n\n'
        '## Intentionally not captured\n'
        '- `.env`, provider configuration, API/OAuth credentials, auth stores, tokens, and channel directories\n'
        '- Hermes session database/transcripts, cron output histories, gateway logs, caches, runtime locks, and profile homes\n\n'
        '## Restore approach\n'
        'Restore the curated documents first, then configure providers, credentials, gateways, and delivery channels manually on the target machine.\n',
        encoding='utf-8',
    )
    source_repos = [
        ('Hermes-project-webapp', Path('/opt/data/projects/Hermes-project-webapp')),
        ('Hermes-project-assets', Path('/opt/data/tmp/Hermes-project-assets')),
    ]
    anchors = ['# Source repository anchors', '', 'These refs identify the source-repository snapshots protected before history cleanup.', '']
    for name, source in source_repos:
        if not (source / '.git').is_dir():
            continue
        head = subprocess.run(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True, capture_output=True, check=True).stdout.strip()
        branch = subprocess.run(['git', '-C', str(source), 'branch', '--show-current'], text=True, capture_output=True, check=True).stdout.strip()
        remote = subprocess.run(['git', '-C', str(source), 'remote', 'get-url', 'origin'], text=True, capture_output=True, check=True).stdout.strip()
        anchors.extend([f'## {name}', f'- Remote: `{remote}`', f'- Branch at export: `{branch}`', f'- Commit at export: `{head}`', ''])
    (docs / 'source-repository-anchors.md').write_text('\n'.join(anchors) + '\n', encoding='utf-8')
    return copied


def scan_for_secrets(repo: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in repo.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(repo)
        if '.git' in rel.parts:
            continue
        if rel.as_posix() in {'scripts/scan_export_safety.py'}:
            continue
        if excluded(path, repo):
            findings.append({'path': rel.as_posix(), 'pattern': 'excluded-file-name', 'line': '0'})
            continue
        if path.suffix.lower() not in TEXT_EXTS and path.name not in {'.gitignore'}:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            lower = line.lower()
            if any(marker in lower for marker in ['placeholder', 'replace_me', '<your_', 'example only']):
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append({'path': rel.as_posix(), 'pattern': pattern.pattern[:60], 'line': str(i)})
                    break
    return findings


def prune_secret_findings(repo: Path) -> list[str]:
    removed: list[str] = []
    findings = scan_for_secrets(repo)
    for finding in findings:
        rel = finding['path']
        path = repo / rel
        if path.exists() and path.is_file():
            path.unlink()
            removed.append(rel)
    if removed:
        docs = repo / 'docs'
        docs.mkdir(exist_ok=True)
        (docs / 'SECURITY_OMISSIONS.json').write_text(
            json.dumps({'removed_files_due_to_secret_scan': sorted(set(removed))}, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
        )
    return sorted(set(removed))


def write_scan_script(repo: Path) -> None:
    scripts = repo / 'scripts'
    scripts.mkdir(exist_ok=True)
    (scripts / 'scan_export_safety.py').write_text(
        '''#!/usr/bin/env python3
from __future__ import annotations

import fnmatch
import json
import re
import sys
from pathlib import Path

TEXT_EXTS = {
    '.md', '.txt', '.json', '.jsonl', '.ts', '.tsx', '.js', '.mjs', '.css', '.html',
    '.svg', '.yaml', '.yml', '.toml', '.lock', '.gitignore', '.example', '.py'
}
SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|access[_-]?token|refresh[_-]?token|bot[_-]?token|oauth|secret|password)\\s*[:=]\\s*["\\']?[^"\\'\\s]{12,}'),
    re.compile(r'(?i)(TELEGRAM|SLACK|OPENAI|ANTHROPIC|OPENROUTER|GITHUB|GEMINI|GOOGLE|HIGGSFIELD|MINIMAX|ELEVENLABS)[A-Z0-9_]*\\s*[:=]\\s*["\\']?[^"\\'\\s]{12,}'),
    re.compile(r'xox[baprs]-[A-Za-z0-9-]{20,}'),
    re.compile(r'\\b[0-9]{8,}:[A-Za-z0-9_-]{30,}\\b'),
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{30,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{20,}'),
]
EXCLUDE_NAMES = {
    '.git', '.env', '.env.local', '.env.production', '.env.development', 'auth.json',
    'state.db', 'state.db-shm', 'state.db-wal', 'node_modules', '__pycache__', '.pytest_cache',
    '.mypy_cache', '.ruff_cache', '.DS_Store', '.cache', 'logs', 'sessions', 'audio_cache', '.archive',
    '.curator_backups', '.curator_state', '.usage.json',
}
EXCLUDE_GLOBS = [
    '*.pem', '*.key', '*.crt', '*.p12', '*.sqlite', '*.db', '*.log', '*.bak', '*.tmp',
    '*token*', '*credential*', '*credentials*', '*auth*', '*.telegram-status.txt',
    'send_*telegram*.py', '*telegram-dm.txt',
]


def excluded(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if set(rel.parts) & EXCLUDE_NAMES:
        return True
    name = path.name
    rel_posix = rel.as_posix()
    return any(fnmatch.fnmatch(name, pat) or fnmatch.fnmatch(rel_posix, pat) for pat in EXCLUDE_GLOBS)


def scan_for_secrets(repo: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in repo.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(repo)
        if '.git' in rel.parts:
            continue
        if rel.as_posix() == 'scripts/scan_export_safety.py':
            continue
        if excluded(path, repo):
            findings.append({'path': rel.as_posix(), 'pattern': 'excluded-file-name', 'line': '0'})
            continue
        if path.suffix.lower() not in TEXT_EXTS and path.name != '.gitignore':
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            lower = line.lower()
            if any(marker in lower for marker in ['placeholder', 'replace_me', '<your_', 'example only']):
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append({'path': rel.as_posix(), 'pattern': pattern.pattern[:60], 'line': str(i)})
                    break
    return findings


if __name__ == '__main__':
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    findings = scan_for_secrets(target)
    if findings:
        print(json.dumps({'status': 'blocked', 'findings': findings}, ensure_ascii=False, indent=2))
        raise SystemExit(2)
    print(json.dumps({'status': 'clean', 'repo': str(target)}, ensure_ascii=False, indent=2))
''',
        encoding='utf-8',
    )


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    homepage_counts = export_homepage()
    agent_counts = export_agent_system()
    for repo in [HOMEPAGE_REPO, AGENT_REPO]:
        write_scan_script(repo)

    pruned = {
        HOMEPAGE_REPO.name: prune_secret_findings(HOMEPAGE_REPO),
        AGENT_REPO.name: prune_secret_findings(AGENT_REPO),
    }
    scan_results = {
        HOMEPAGE_REPO.name: scan_for_secrets(HOMEPAGE_REPO),
        AGENT_REPO.name: scan_for_secrets(AGENT_REPO),
    }
    manifest = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'repos': {
            HOMEPAGE_REPO.name: {
                'path': str(HOMEPAGE_REPO),
                'counts': homepage_counts,
                'secret_scan_findings': len(scan_results[HOMEPAGE_REPO.name]),
                'pruned_files_due_to_secret_scan': len(pruned[HOMEPAGE_REPO.name]),
            },
            AGENT_REPO.name: {
                'path': str(AGENT_REPO),
                'counts': agent_counts,
                'secret_scan_findings': len(scan_results[AGENT_REPO.name]),
                'pruned_files_due_to_secret_scan': len(pruned[AGENT_REPO.name]),
            },
        },
    }
    (ROOT / 'EXPORT_MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (HOMEPAGE_REPO / 'EXPORT_MANIFEST.json').write_text(json.dumps(manifest['repos'][HOMEPAGE_REPO.name], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (AGENT_REPO / 'EXPORT_MANIFEST.json').write_text(json.dumps(manifest['repos'][AGENT_REPO.name], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if any(scan_results.values()):
        print(json.dumps({'status': 'blocked', 'scan_results': scan_results}, ensure_ascii=False, indent=2))
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
