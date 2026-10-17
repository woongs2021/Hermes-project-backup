# Restarting Today-Only Cron Work After a Credit Outage

Use this when Chris asks to reconnect/check the team and rerun only today's missed work, excluding older outage failures.

## Scope rule

- Determine the current KST date first.
- Include only jobs whose scheduled run for that KST date failed because of the outage/credit issue, plus profile-local jobs that are clearly today's daily/Saturday task.
- Exclude older weekday failures unless Chris explicitly asks for backfill.
- Do not rerun paused legacy jobs or weekly lanes whose scheduled day is not today.

## Compact verification sequence

1. Check gateway/profile health:
   - `hermes gateway status`
   - `hermes status --all`
   - `hermes profile list`
   - `send_message(action='list')` only if target discovery matters.
2. List relevant cron stores:
   - default/Karina: `hermes cron list --all`
   - profile-owned stores: `hermes --profile <name> cron list --all`
3. Select only today-relevant failed jobs.
4. Trigger jobs:
   - default cron store: `hermes cron run <job_id>` or the cronjob tool.
   - profile cron store: `hermes --profile <name> cron run <job_id>`.
5. If a triggered job only queues and does not run promptly, run an explicit tick for that cron store:
   - default: `hermes cron tick`
   - profile: `hermes --profile <name> cron tick`
6. Verify completion from job metadata, not from trigger success alone:
   - `last_run_at` should be after the repair attempt.
   - `last_status` should be `ok`.
   - `last_error` and `last_delivery_error` should be empty/none.

## Pitfalls

- `cronjob(action='run')` / `hermes cron run` means “queued for next scheduler tick,” not “completed.” Always verify after the tick.
- When several long LLM jobs are triggered together, one foreground `hermes cron tick` may time out while some jobs still finish. Inspect `jobs.json`/`cron list --all` afterward and rerun only the remaining failed jobs.
- Profile-local jobs may live under `/opt/data/profiles/<profile>/cron/jobs.json`, not the default cron store.
- For Chris-facing summaries, say “triggered/queued” only until `last_status=ok` or a delivery/status file confirms the artifact was actually sent.
- Keep the report concise: connected profiles, today-only reruns, excluded older failures, and any remaining blocker.
