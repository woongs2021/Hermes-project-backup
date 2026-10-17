# Cron automation audit, cleanup, and repair pattern

Use when Chris asks what automations are running vs paused, wants paused/duplicate jobs cleaned up, or asks to verify that active scheduled loops really work.

## Operating principle

Separate three states that are easy to conflate:

1. **Gateway/process health** — whether default and specialist bots can receive/send messages.
2. **Cron scheduling state** — whether a job is `enabled=true` and has a future `next_run_at`.
3. **Last-run health** — whether the last run ended `ok` or `error`, and whether the error actually blocks user-visible value.

Report these separately. A gateway can be running while a cron job is paused. A cron job can be enabled while the last run failed. A last run can be marked failed even when the core deployment/data update succeeded but a final optional verification step exceeded a tool/time limit.

## Audit workflow

1. **List cron stores, not only the current profile.**
   - Default store: `/opt/data/cron/jobs.json`
   - Specialist stores: `/opt/data/profiles/{yuna,goyounjung,son,faker,muyeol}/cron/jobs.json`
2. **Check gateway status for all profiles.**
   - `hermes gateway status`
   - `hermes --profile <profile> gateway status`
   - Summarize as running/stopped; do not paste long logs or tokens.
3. **Tabulate active jobs.** Include owner/profile, cadence, next run, last status, and whether it is healthy, needs repair, or intentionally paused.
4. **Tabulate paused jobs separately.** Distinguish:
   - explicitly requested paused jobs to keep
   - migrated/default-store duplicates
   - old one-off trial jobs
   - superseded draft/publishing chains
5. **Before deleting, back up JSON.** Use a timestamped backup directory such as `/opt/data/logs/cron-cleanup-YYYYMMDD/`. Never delete from memory alone.
6. **Delete only clear duplicates/superseded jobs.** If a paused job is a separate capability rather than an obvious duplicate, leave it paused and ask/offer before deletion.
7. **After edits, re-read all stores and report final counts.** Show active, paused, and removed jobs.

## Handling Chris requests like “turn only X back on”

- Reactivate exactly the named class. Example: if Chris says “Karina 아침점심저녁 노트만,” enable morning/midday/evening and keep night/week/month/other notes paused.
- If the requested jobs are already enabled, say so and still verify their next runs.
- Do not infer that adjacent jobs such as night notes, weekly summaries, work logs, or specialist reports should also be reactivated.

## Repairing active jobs with recent `error`

1. Inspect the latest cron output file under the profile’s cron output directory.
2. Separate core outcome from final verification outcome:
   - Did the job create/commit/push/update the intended artifact?
   - Did build/lint/data validation pass?
   - Did live data or direct asset URLs reflect the change?
   - Was the failure only a final browser smoke check, API polling limit, tool-call limit, or timeout?
3. If core work succeeded but optional verification failed, do the missing verification manually from Karina/default, then patch the cron prompt so future runs use a compact verification path.
4. For webapp jobs, prefer one consolidated live verification script: fetch live manifest/data/HTML with cache busting, navigate the actual UI tab path with Playwright, confirm the expected title/status appears, and check console/page errors plus horizontal overflow.
5. Do not claim the cron is fully healthy until either:
   - a rerun ends `last_status=ok`, or
   - you clearly label the cron’s last status as historical error while saying the live artifact was manually verified and the next-run prompt was patched.

## Reporting format for Chris

Use a compact Korean table-driven summary:

- `Gateway 상태`
- `현재 켜져 있는 자동화`
- `최근 error / 점검 필요`
- `삭제한 중복 paused job`
- `아직 paused로 남긴 job과 이유`
- `백업 위치`

Keep it warm and direct. Avoid long raw logs; provide only job names, owners, status, next run, and the important decision.