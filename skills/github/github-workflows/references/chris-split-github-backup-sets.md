# Chris split GitHub backup sets

Use when Chris asks to back up Faker/homepage/webapp data or the Karina/Hermes agent-team system to GitHub.

Current operating split:
- `Hermes-project-backup` remains **command-triggered only**: do not run recurring pushes unless Chris explicitly asks for that backup.
- `Hermes-project-webapp` may have a recurring local coding loop, but GitHub publication is **weekly and approval-gated**: daily Faker coding stays local; Saturday weekly prep builds/scans/commits a local release candidate and asks Chris for approval; only after explicit approval should an agent push the branch, merge/fast-forward main, run Pages, and verify the URL.

## Repository split

Keep two curated repositories by default:

1. `Hermes-project-webapp`
   - Remote: `https://github.com/woongs2021/Hermes-project-webapp.git`
   - Purpose: Faker-built webapp/dashboard source and curated public-facing data.
   - Local export set: `/opt/data/github-backup-sets/repos/chris-obd-homepage-data/`.
   - Includes: August Dashboard source, public-safe dashboard source documents, webapp build-loop candidates/plans/daily Markdown, public-ish image-gallery JSON, image assets, GitHub Pages workflow.
   - Excludes: `node_modules/`, generated `dist/`, raw DMs, private prompts, token/auth/session/log/runtime files.
   - GitHub Pages target: `https://woongs2021.github.io/Hermes-project-webapp/`; Vite apps under this repo should set `base: '/Hermes-project-webapp/'` before build/push.

2. `Hermes-project-backup`
   - Remote: `https://github.com/woongs2021/Hermes-project-backup.git`
   - Purpose: private operational/restore backup of the Karina-led Hermes agent team.
   - Local export set: `/opt/data/github-backup-sets/repos/chris-karina-agent-system/`.
   - Includes: agent-team work-log Markdown, local reusable skills/workflows, Hermes planning Markdown, restore/boundary docs.
   - Excludes: `.env`, `auth.json`, OAuth stores, credential pools, Telegram/Slack bot tokens, Hermes `state.db`, sessions, gateway logs, request dumps, raw private DM dumps.

## Export and push routine

Do not copy broad runtime roots. Rebuild the curated export sets with:

```bash
python3 /opt/data/github-backup-sets/scripts/export_backup_sets.py
python3 /opt/data/github-backup-sets/repos/chris-obd-homepage-data/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-obd-homepage-data
python3 /opt/data/github-backup-sets/repos/chris-karina-agent-system/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-karina-agent-system
```

Only continue if both scans return `status: clean`.

For the webapp export, include public-safe dashboard source inputs required by the build, not just the generated manifest. In this setup, the August dashboard build expects `august-dashboard-safe-sources/dashboard-documents.json` beside `august-dashboard/`; if the GitHub Actions build fails with `ENOENT ... august-dashboard-safe-sources/dashboard-documents.json`, patch the curated export allowlist to copy that safe-source folder and rerun the scan/build before pushing.

Then, in each local repo-shaped folder, use a branch → main flow:

```bash
git init
git config user.name "Hermes Agent"
git config user.email "hermes-agent@users.noreply.github.com"
git remote add origin <REMOTE_URL>  # or set-url if origin exists
git fetch origin --prune || true
git checkout -B <dated-branch>
git add .
python3 scripts/scan_export_safety.py .  # scanner must skip .git internals; if not, patch it before trusting the result
git commit -m "chore: curated Hermes project backup"  # or focused webapp message
git push -u origin <dated-branch>
git checkout -B main <dated-branch>
git push -u origin main
```

## GitHub auth and workflow-scope pitfall

If the webapp repo includes `.github/workflows/pages.yml`, GitHub rejects pushes from a `gh` OAuth token that lacks `workflow` scope with an error like `refusing to allow an OAuth App to create or update workflow ... without workflow scope`. Refresh auth before pushing workflow files:

```bash
gh auth refresh -h github.com -s workflow
# device-flow authentication may be required; after approval:
gh auth setup-git
```

Then re-run the branch push and main push. Do not print raw tokens; `gh auth status` may show a masked token and scopes only.

If push fails because GitHub credentials are not configured, stop honestly after local branch/commit preparation and report the exact non-secret blocker. Do not print or request raw tokens in chat; ask Chris to connect HTTPS credentials, SSH key, or a configured GitHub CLI/session in the environment, then retry the push and verify remote branch/main.

Operational pitfall: safety scanners that walk the whole repo must skip `.git/` after `git init`; otherwise they can produce false `excluded-file-name` findings for `.git/FETCH_HEAD`, objects, hooks, and index files. Prefer running export safety scans before `git init`, and make any reusable `scan_export_safety.py` ignore paths containing `.git`.

## Webapp recurring coding vs approval-gated Pages publish

Chris's preferred webapp loop separates local implementation from GitHub publication:

- Daily Faker coding can run locally in `/opt/data/projects/Hermes-project-webapp` and should report local build/safety status to Chris.
- Do **not** push branches, merge main, or trigger Pages every day.
- The weekly webapp publish checkpoint runs on **Saturday**. It should prepare a local release candidate, run `cd august-dashboard && npm run build`, run `python3 scripts/scan_export_safety.py .`, commit locally if needed, and send Chris an approval request.
- The approval request must clearly state the local branch, local commit SHA, changed-file summary, build/safety status, and that GitHub push/Pages deploy will happen only after approval.
- Silence or older approvals do not count. Require explicit current approval from Chris after the weekly request.
- After approval, perform the side effects manually or in a separate approved run: push the weekly branch, fast-forward/merge main, push main, watch GitHub Pages, and verify `https://woongs2021.github.io/Hermes-project-webapp/` returns HTTP 200.
- Telegram cannot open the server's raw `localhost`; use GitHub Pages as the user-checkable preview unless Chris explicitly approves a scoped public tunnel.

## GitHub Pages setup for the webapp repo

- The Vite app should set `base: '/Hermes-project-webapp/'` so built assets resolve under `https://woongs2021.github.io/Hermes-project-webapp/`.
- Include `.github/workflows/pages.yml` that builds `august-dashboard` and deploys `august-dashboard/dist` using `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`.
- The GitHub token must include `workflow` scope to create/update `.github/workflows/*.yml`. If push is rejected with `refusing to allow an OAuth App to create or update workflow ... without workflow scope`, run `gh auth refresh -h github.com -s workflow` and have Chris approve the device code; never print raw tokens.
- If the first Pages run fails with `Get Pages site failed ... Not Found`, enable Pages for workflow deploys: `gh api -X POST repos/woongs2021/Hermes-project-webapp/pages -f build_type=workflow`, then rerun the workflow.
- If deploy fails with `Branch "main" is not allowed to deploy to github-pages due to environment protection rules`, add `main` to the `github-pages` environment branch policies with the GitHub API, then rerun. Verify success with `gh run watch ... --exit-status` and an HTTP 200 check against the Pages URL.

## Implementation boundary rule

When coding new data producers, decide the backup lane before creating files:

- Homepage/Faker/public-facing app data must live in or export cleanly to `chris-obd-homepage-data`.
- Karina/Hermes operations, role docs, reusable skills, restore guides, and work-memory docs must live in or export cleanly to `chris-karina-agent-system`.
- If one file mixes public homepage content with private operations, split it into two files rather than relying on later cleanup.
- Keep the export allowlist-based even as the app grows; never add `/opt/data` or a full Hermes home/profile as a repo source.

## When Chris provides or changes remote URLs

Map Chris's URL names to the local export folders, then initialize, branch, scan, commit, push, and main-update from each folder:

```bash
# Backup/private agent-system repo
cd /opt/data/github-backup-sets/repos/chris-karina-agent-system
git init
git branch -M main
git remote add origin https://github.com/woongs2021/Hermes-project-backup.git
git checkout -B backup-curated-YYYYMMDD
git add .
python3 scripts/scan_export_safety.py .
git commit -m "chore: curated Hermes project backup"
git push -u origin backup-curated-YYYYMMDD
git checkout -B main backup-curated-YYYYMMDD
git push -u origin main

# Webapp/Pages repo
cd /opt/data/github-backup-sets/repos/chris-obd-homepage-data
git init
git branch -M main
git remote add origin https://github.com/woongs2021/Hermes-project-webapp.git
git checkout -B webapp-pages-YYYYMMDD
git add .
python3 scripts/scan_export_safety.py .
git commit -m "feat: publish Hermes project webapp backup"
git push -u origin webapp-pages-YYYYMMDD
git checkout -B main webapp-pages-YYYYMMDD
git push -u origin main
```

Start the backup/agent-system repository private. Review the webapp repository separately before any broad public exposure; if GitHub Pages is enabled, verify the Actions run and then open `https://woongs2021.github.io/Hermes-project-webapp/`.
