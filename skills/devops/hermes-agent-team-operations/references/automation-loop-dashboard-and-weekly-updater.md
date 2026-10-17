# Automation Loop Dashboard + Weekly Updater Pattern

Use when Chris asks to show the currently active Hermes automations in the Hermes Project Webapp, or to keep that dashboard updated automatically.

## Goal

Represent Hermes as a living agent operating system without exposing private operational details. The Team tab should show the detailed operating board; Weekly should show a compact status summary.

## Source of truth

Read enabled cron jobs from all active cron stores:

- `/opt/data/cron/jobs.json` for Karina/default-owned jobs
- `/opt/data/profiles/yuna/cron/jobs.json`
- `/opt/data/profiles/goyounjung/cron/jobs.json`
- `/opt/data/profiles/son/cron/jobs.json`
- `/opt/data/profiles/faker/cron/jobs.json`
- `/opt/data/profiles/muyeol/cron/jobs.json`

Collect only `enabled: true` jobs. Treat `last_status: ok` as healthy. Treat `last_status: error` as needs-check. For newly created scheduled jobs with no `last_status` yet, label them as scheduled/ok if they are enabled and have a valid `next_run_at`, but mention first-run pending in notes if useful.

## Public-safe transformation

Do not expose:

- raw chat IDs or private platform targets
- absolute private paths
- raw cron prompts
- tokens, credentials, OAuth/app secrets
- raw logs or internal tracebacks

Use public-safe labels instead:

- delivery: `Telegram · Chris DM`, `local only`, or `Slack/Telegram` when applicable
- cost type: `LLM`, `no-agent`, or `script-only`
- owner: `Karina`, `Yuna`, `GoYJ`, `Son`, `Faker`, `Muyeol`
- status: `ok` or `needs check`
- note: one concise sentence explaining user-facing purpose

## Webapp placement

Recommended IA:

1. **Team tab**: detailed `Automation Loop Status` board.
   - Summary metrics: active, ok, needs-check, paused/default.
   - Group rows by owner.
   - Per row: name, purpose note, rhythm, next run, delivery category, cost type, status.
2. **Weekly tab**: compact operating status card only.
   - active loops
   - healthy/ok
   - needs check
   - paused default jobs

Avoid putting this under Design DNA, Chris Archive, or Research; those are asset/research content spaces, not system operations.

## Weekly updater loop

When Chris wants the dashboard kept current, create a specialist-owned recurring job, usually Faker-owned because it updates webapp code/data. A good default cadence is Monday 10:10 KST, after Muyeol's Monday 09:40 webapp data-count loop.

The updater prompt should require:

1. Read all cron stores listed above.
2. Update Team and Weekly automation dashboard data.
3. Keep copy public-safe.
4. Run `npm run validate:data`, `npm run lint`, `npm run build:public`, and `git diff --check`.
5. Commit and push to `main`.
6. Verify live GitHub Pages Team and Weekly DOM on desktop and mobile: row count matches enabled loop count, metrics match summary, console/page errors empty, horizontal overflow 0.

## Verification pattern

Before reporting success:

- Verify the cron job exists and is enabled.
- Build locally.
- Browser-check Team tab and Weekly tab locally.
- Push and verify live HTML references the new hashed JS/CSS.
- Live browser-check Team and Weekly on desktop and mobile.
- Include final link with commit cache-buster, e.g. `?v=<shortsha>`.

## Pitfalls

- Do not leave old paused default jobs cluttering the dashboard unless Chris explicitly wants paused history shown.
- Do not count the local no-agent watchdog as an LLM loop; it is effectively script-only/no-agent and low token cost.
- Do not mark a newly created enabled updater loop as failed just because it has no `last_status` yet; it has not run. Label it as scheduled/first-run pending or include it in ok if the UI only supports ok/needs-check.
- If GitHub Actions API rate limits, verify deployment by fetching live HTML/assets and then running browser DOM checks instead of waiting on API polling only.
