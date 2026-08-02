# Chris split GitHub backup sets

Use when Chris asks to back up Faker/homepage data or the Karina/Hermes agent-team system to GitHub.

## Repository split

Keep two private repositories by default:

1. `chris-obd-homepage-data`
   - Purpose: Faker-built homepage/dashboard source and curated public-facing data.
   - Local export set: `/opt/data/github-backup-sets/repos/chris-obd-homepage-data/`.
   - Includes: August Dashboard source, webapp build-loop candidates/plans/daily Markdown, public-ish image-gallery JSON, image assets.
   - Excludes: `node_modules/`, `dist/`, raw DMs, private prompts, token/auth/session/log/runtime files.

2. `chris-karina-agent-system`
   - Purpose: private operational/restore backup of the Karina-led Hermes agent team.
   - Local export set: `/opt/data/github-backup-sets/repos/chris-karina-agent-system/`.
   - Includes: agent-team work-log Markdown, local reusable skills/workflows, Hermes planning Markdown, restore/boundary docs.
   - Excludes: `.env`, `auth.json`, OAuth stores, credential pools, Telegram/Slack bot tokens, Hermes `state.db`, sessions, gateway logs, request dumps, raw private DM dumps.

## Export routine

Do not copy broad runtime roots. Rebuild the curated export sets with:

```bash
python3 /opt/data/github-backup-sets/scripts/export_backup_sets.py
python3 /opt/data/github-backup-sets/repos/chris-obd-homepage-data/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-obd-homepage-data
python3 /opt/data/github-backup-sets/repos/chris-karina-agent-system/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-karina-agent-system
```

Push only if both scans return `status: clean`.

## Implementation boundary rule

When coding new data producers, decide the backup lane before creating files:

- Homepage/Faker/public-facing app data must live in or export cleanly to `chris-obd-homepage-data`.
- Karina/Hermes operations, role docs, reusable skills, restore guides, and work-memory docs must live in or export cleanly to `chris-karina-agent-system`.
- If one file mixes public homepage content with private operations, split it into two files rather than relying on later cleanup.
- Keep the export allowlist-based even as the app grows; never add `/opt/data` or a full Hermes home/profile as a repo source.

## When Chris provides remote URLs

Inside each local repo-shaped folder:

```bash
git init
git branch -M main
git remote add origin <REMOTE_URL>
git add .
python3 scripts/scan_export_safety.py .
git commit -m "chore: monthly curated backup"
git push -u origin main
```

Start both repositories private. Review the homepage repo separately before any public conversion; keep the agent-system repo private.
