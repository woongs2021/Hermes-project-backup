# Cron automation inventory and cleanup pattern

Use when Chris asks which automations are running, paused, duplicated, or consuming tokens, or asks to delete paused/duplicate loops.

## Inventory scope

Check cron stores across the default profile and specialist profiles, not just the active profile:

- `/opt/data/cron/jobs.json`
- `/opt/data/profiles/yuna/cron/jobs.json`
- `/opt/data/profiles/goyounjung/cron/jobs.json`
- `/opt/data/profiles/son/cron/jobs.json`
- `/opt/data/profiles/faker/cron/jobs.json`
- `/opt/data/profiles/muyeol/cron/jobs.json`

Also check gateway status separately. A gateway being alive only proves the bot can receive messages; it does not prove a scheduled job is enabled or recently successful.

## Status language

Separate these dimensions in the user-facing summary:

1. **Enabled/scheduled**: `enabled=true` / state scheduled.
2. **Paused/stopped**: `enabled=false` / state paused.
3. **Recently healthy**: `last_status=ok`.
4. **Enabled but needs attention**: `enabled=true` with recent `last_status=error`.
5. **Script-only/no-agent**: e.g. watchdog loops; usually no LLM/model tokens.
6. **Gateway/process status**: profile gateway running/stopped.

Do not collapse these into one vague “running” label. For Chris, use compact Korean tables.

## Cleanup workflow

1. List the jobs first; never guess IDs.
2. If deleting multiple jobs, keep a backup of affected `jobs.json` files before manual edits or bulk removal.
3. Prefer `cronjob(action='remove')` for default-profile jobs when available.
4. For profile-local cron stores that are not accessible through the current cronjob tool, carefully edit the relevant profile `jobs.json` only after backing it up.
5. Delete only jobs that are clearly duplicate, migrated, superseded, or explicitly requested by Chris. If a paused job is a separate lane rather than a duplicate, report it and wait unless Chris says to delete all remaining paused jobs.
6. After cleanup, list again and verify that the intended jobs remain enabled and that no unintended paused default jobs remain.

## Current Chris pattern

Chris may ask to keep only Karina’s warm-note cadence plus essential operations. The established keep set for default cron is:

- Karina morning 09:00 warm/weather note
- Karina midday 12:00 warm note
- Karina evening 18:00 warm note
- Karina night 22:00 warm note
- Specialist gateway watchdog (`no_agent`, local delivery)
- Muyeol weekly webapp data count report when Chris still wants the Weekly/webapp count loop

The specialist gateway watchdog is a maintenance loop, not a content/research loop: it checks Yuna/GoYJ/Son/Faker/Muyeol gateway processes and restarts missing ones. It is `no_agent=true`, `deliver=local`, and should be described as negligible LLM-token usage.

## Verifying enabled jobs with prior errors

For jobs whose `enabled=true` but `last_status=error`:

1. Inspect the latest cron output before assuming failure.
2. If the output shows the artifact/deployment/data update actually succeeded but one final verification step exceeded tool/time limits, run the missing verification manually.
3. Patch the job prompt to use a compact, consolidated verification script if it is likely to hit tool-call or time limits again.
4. Report honestly: distinguish “cron history still says error” from “actual live artifact/data/DOM is verified OK.”

## Reporting format

Use short tables:

- Gateway/process state
- Enabled automations
- Enabled but attention-needed automations
- Removed paused/duplicate jobs
- Remaining paused jobs, if any

Keep raw logs and tokens out of the message. Mention backup paths only when useful.