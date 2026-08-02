# Monthly curated Hermes backup sets

Use this when Chris asks to prepare or push monthly GitHub backups for local Hermes/Faker/Karina data. The durable pattern is **repo-shaped curated export sets**, not raw runtime directory copies.

## Repository split

Prefer two private repositories:

1. `chris-obd-homepage-data`
   - Purpose: Faker-built homepage/dashboard source and curated public-facing homepage data.
   - Include: dashboard source, public-safe Markdown/JSON, webapp build-loop candidates/plans, image-gallery final data/assets.
   - Exclude: pending/private prompts unless explicitly approved, raw DMs, delivery scripts/status containing platform context, generated dependencies/caches.

2. `chris-karina-agent-system`
   - Purpose: private backup of the Karina-led Hermes agent-team operating system.
   - Include: agent role docs, safe work-log Markdown, local skills/workflows, planning docs, restore/boundary docs.
   - Exclude: `.env`, `auth.json`, OAuth stores, credential pools, tokens/API keys, Hermes `state.db`, sessions, gateway logs, request dumps, raw DM exports.

## Local prepared path from the session

The session-created local backup root was:

```bash
/opt/data/github-backup-sets/
```

Key outputs:

```bash
/opt/data/github-backup-sets/repos/chris-obd-homepage-data
/opt/data/github-backup-sets/repos/chris-karina-agent-system
/opt/data/github-backup-sets/scripts/export_backup_sets.py
/opt/data/github-backup-sets/README.md
```

## Monthly routine

Before each monthly GitHub push:

```bash
python3 /opt/data/github-backup-sets/scripts/export_backup_sets.py
python3 /opt/data/github-backup-sets/repos/chris-obd-homepage-data/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-obd-homepage-data
python3 /opt/data/github-backup-sets/repos/chris-karina-agent-system/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-karina-agent-system
```

Only push if both scans return `status: clean`.

## When GitHub remote URLs are provided

For each repo-shaped folder:

```bash
git init
git branch -M main
git remote add origin <REMOTE_URL>
git add .
python3 scripts/scan_export_safety.py .
git commit -m "chore: monthly curated backup"
git push -u origin main
```

## Pitfalls

- Do not `cp -r /opt/data` or raw `~/.hermes` into a repo.
- Do not trust `.gitignore` alone; run the scanner after staging/export.
- If the scan flags a file, remove/quarantine the whole file by default rather than trying to redact in-place unless Chris explicitly needs that content preserved.
- Keep the implementation split alive while coding, not only at export time: new data sources should declare their backup target before being added (`homepage/Faker` vs `Karina agent-system`), and mixed files should be split instead of relying on later cleanup.
- Keep both repos private initially. Review the homepage repo separately before any public conversion; keep the Karina agent-system repo private.
