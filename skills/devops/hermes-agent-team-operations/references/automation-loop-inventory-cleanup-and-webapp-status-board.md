# Automation loop inventory, cleanup, and webapp status board

Use when Chris asks what automations are currently running, wants paused/duplicate cron jobs removed, or wants the final automation state reflected in the Hermes Project Webapp.

## Operating principle

Distinguish three things before reporting:

1. **Gateway/process health** — whether default and specialist gateways are running and can receive/send messages.
2. **Cron enabled state** — whether a job is scheduled (`enabled=true`) or paused/deleted.
3. **Recent run result** — whether the last run was `ok`, `error`, or stale. An enabled job with a recent `error` is not “off”; it is active but needs verification/repair.

## Inventory checklist

- Inspect cron stores for default and specialist profiles:
  - `/opt/data/cron/jobs.json`
  - `/opt/data/profiles/yuna/cron/jobs.json`
  - `/opt/data/profiles/goyounjung/cron/jobs.json`
  - `/opt/data/profiles/son/cron/jobs.json`
  - `/opt/data/profiles/faker/cron/jobs.json`
  - `/opt/data/profiles/muyeol/cron/jobs.json`
- Check gateway status for default plus all specialist profiles.
- Report only enabled jobs when Chris asks for the final running list.
- When listing active loops, include owner, schedule/rhythm, next run, last status, delivery target, and whether it is LLM-backed or `no_agent`/script-only.
- Treat `no_agent` watchdog jobs as low-token infrastructure loops, not research/content loops.

## Cleanup pattern

When Chris asks to delete paused/redundant jobs:

1. List first; never guess job IDs.
2. Back up affected cron JSON files before bulk deletion.
3. Keep explicitly requested active loops, e.g. Karina warm notes and specialist watchdog.
4. Delete only paused jobs that are clearly duplicates, superseded, or explicitly requested by Chris.
5. Re-list after deletion and confirm no paused jobs remain in the targeted store.
6. Record substantive cleanup in Karina’s daily team work log.

## Error-state verification pattern

For enabled jobs whose `last_status` is `error`:

- Inspect the latest cron output before assuming the product workflow failed.
- A job may have completed core work but failed only at final reporting or an overly broad QA step.
- Verify the actual user-facing artifact independently when possible: live data, deployed HTML asset names, browser DOM, console/page errors, and overflow.
- Patch the cron prompt to keep future verification compact if it failed due to tool-call limits after successful deployment. Prefer one consolidated live verification script over many small probes.

## Webapp reflection pattern

When Chris wants the automation state shown in the Hermes Project Webapp:

- Put the detailed board in **Team** because it explains the living agent operating system.
- Put only compact status metrics in **Weekly** because Weekly is a summary surface.
- Recommended Team board metrics:
  - active loops
  - healthy/ok loops
  - needs-check loops
  - paused default jobs
- Recommended row fields:
  - owner
  - loop name
  - rhythm/schedule
  - next run
  - delivery
  - cost type (`LLM`, `no-agent`, `script-only`)
  - status (`ok`, `needs check`)
  - short note
- Verify the rendered UI, not only source edits:
  - build/data validation/lint
  - local browser DOM for Team and Weekly
  - desktop and mobile overflow
  - live GitHub Pages HTML points to the new hashed CSS/JS
  - live browser DOM shows the board/summary and correct metric counts.

## Reporting tone

Chris prefers concise Korean status tables for this class of operational work. Keep the final report short and clear: what is running, what was deleted, what still needs observation, and the final URL if webapp changes were deployed.