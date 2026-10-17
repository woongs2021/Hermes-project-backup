# Specialist recurring loop profile migration

Use this reference when Chris reports that specialist recurring messages appear to come from Karina/default, or asks to move/test today's loops so each agent sends from its own bot/profile.

## Durable lesson

Setting `profile: <specialist>` on a job stored in the default/Karina cron store is not enough for Chris's sender-ownership requirement. For user-facing Slack/Telegram recurring loops, the effective sender path must be owned by the specialist: profile-local cron store, specialist gateway, explicit delivery target, and platform delivery evidence.

## Safe migration sequence

1. **Audit every cron store, not only default.** Check `/opt/data/cron/jobs.json` and `/opt/data/profiles/*/cron/jobs.json` or use `hermes cron list` plus `hermes --profile <name> cron list`.
2. **Classify active jobs by content owner.** Karina/default should keep only Karina-owned loops such as weather/greetings and explicit orchestration. Specialist-owned research, design, PM, coding, or validation loops belong to that specialist.
3. **Back up before editing cron JSON.** Copy the relevant default and profile `jobs.json` files to a timestamped backup directory before moving jobs.
4. **Copy active specialist jobs into the owner profile cron store.** Preserve job id, prompt, schedule, skills, model, enabled toolsets, workdir, and repeat fields unless intentionally changing them.
5. **Use explicit delivery targets.** Prefer `telegram:<Chris chat id>` or `slack,telegram:<Chris chat id>`. Avoid `origin` or bare `telegram` for migrated specialist user-facing jobs because those can resolve through the wrong gateway/home target.
6. **Remove stale origin binding where appropriate.** If the migrated job has an `origin` object from the default/Karina store, remove it from the profile-local copy so the explicit `deliver` target controls delivery.
7. **Pause the default-store source job.** Do not delete it immediately. Set `enabled=false`, `state=paused`, `paused_at=<now>`, `paused_reason='Migrated to specialist profile-local cron...'`, and clear `next_run_at` if needed.
8. **Check profile gateways.** `hermes --profile <agent> cron status` must show the gateway running for scheduled future runs. If not service-installed, a tracked background `hermes --profile <agent> gateway run` process is an acceptable immediate repair, but report that it is manual/non-service.
9. **Run today's jobs from the owner profile.** Use `hermes --profile <agent> cron run <job_id>` then `HERMES_ACCEPT_HOOKS=1 hermes --profile <agent> cron tick` or wait for the profile gateway tick.
10. **Verify completion and delivery separately.** `last_status=ok` is not enough; confirm logs include both `using Hermes profile '<agent>'` and `Job '<id>': delivered to telegram:<chat id>` or Slack `ts/channel` evidence.
11. **Handle provider failures without confusing sender verification.** If an LLM-driven cron fails due to quota/transport after producing no final response, do not claim the full cron succeeded. If the goal is sender-path verification, send a concise one-shot message through the specialist's own bot/API and record only non-secret handles such as Telegram `message_id` and Slack `ts`.
12. **Record substantive migrations in Karina's daily team work log.** Include moved job ids, owner profiles, gateway state, delivery evidence, blockers, and next action. Do not record raw tokens or long logs.

## Evidence checklist

For each migrated active specialist loop, capture:

- job id and job name
- old location: default/Karina cron store
- new owner profile and profile-local cron location
- final `deliver` target shape
- profile gateway running status
- latest `last_run_at` and `last_status`
- log line proving `using Hermes profile '<agent>'`
- log line proving delivery to Telegram/Slack, or direct-send handle (`message_id`, Slack `ts`)

## Pitfalls

- Do not present `cron run` trigger output as delivered. It only queues the job for the next scheduler tick.
- Do not rely on `profile` metadata in a default cron store as sender proof.
- Do not use `origin` copied from default/Karina for migrated specialist jobs unless you have verified it resolves through the specialist gateway.
- Do not print or persist Telegram/Slack bot tokens while doing one-shot API verification.
- Do not reactivate paused predecessor loops while moving current active loops unless Chris explicitly asks for those old loops back.
- If a specialist gateway is only running manually, tell Chris it is operational now but should be service-installed for durable scheduling.
