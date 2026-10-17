# Muyeol Direct Friday Report Delivery

Use this reference when Chris asks that the Friday paper/validation report be spoken by Kim Muyeol directly, not proxy-delivered by Karina/default.

## Operating pattern

- Store Friday paper/validation jobs in Muyeol's own profile cron store (`/opt/data/profiles/muyeol/cron/jobs.json` or `hermes --profile muyeol cron ...`).
- Keep the candidate-pool/prep job local-only.
- Make the user-facing Friday report job deliver explicitly to both visible destinations: `slack,telegram:<Chris chat id>`.
- The visible report should start clearly as Muyeol, e.g. `김무열입니다.` or `김무열 보고드립니다.`
- Pause default/Karina-store jobs that would duplicate, rewrite, or proxy-deliver the same Friday report.
- Update downstream jobs to depend on Muyeol's selected-report output or `/opt/data/agent-team-work-log/paper-candidates/weekly-selected-papers.md`, not on a Karina final-report job.

## Same-day test / replay pattern

When Chris says “오늘자도 무열이가 보내도록” or asks to test direct delivery the same day:

1. Prefer rerunning Muyeol's profile-local prep/report jobs and verify completion with `last_run_at`, `last_status=ok`, output files, and delivery errors.
2. If the scheduler queues but does not produce a fresh output promptly, do not claim success from the trigger alone.
3. For an urgent same-day replay, use the latest already-validated Muyeol Friday report or `weekly-selected-papers.md` as source material and send a concise Muyeol-authored message directly through Muyeol's Telegram/Slack credentials.
4. Never print or log raw bot tokens. Load credentials only inside the sending process and report only verifiable handles:
   - Telegram: `ok=true` and `message_id`.
   - Slack: `ok=true`, channel, and `ts`.
5. Record substantive replay/ownership changes in Karina's daily team work log.

## Verification checklist

- [ ] Muyeol profile gateway has Telegram and Slack configured/running.
- [ ] Muyeol report job is in Muyeol profile cron store, not only `profile: muyeol` inside the default cron store.
- [ ] `deliver` is explicit: `slack,telegram:<Chris chat id>`.
- [ ] Default/Karina Friday proxy-delivery jobs are paused if they would duplicate the report.
- [ ] Visible text starts as Muyeol.
- [ ] Same-day manual replay, if used, returns real Telegram `message_id` and Slack `ts`.

## Pitfalls

- A successful cron `run` command only queues a job for a scheduler tick; it is not proof that the report was delivered.
- `last_status` and output files matter more than `next_run_at` when verifying same-day replay.
- Do not convert a specialist-owned delivery back into Karina/default auto-delivery just because the prompt has `profile: muyeol`.
- Avoid recording private chat IDs beyond existing approved explicit targets, and never record raw tokens.
