# Reducing Active Loop Volume and Rerunning Today After Credit Recovery

Use this when Chris asks to conserve tokens/credits by reducing only selected recurring loops, or asks to rerun a specific missed loop after a usage-limit outage.

## Reduce loop volume without over-pruning

1. Determine the exact requested scope from Chris's wording.
   - Example: “Yuna/Go Youn-jung 2+2 research → 1+1” means Yuna daily research becomes 1 pick and Go Youn-jung daily research becomes 1 pick.
   - Example: “Go Youn-jung visual loop → 1 per day” means one final still plus one turntable when credits allow.
   - “나머지는 유지” means do not pause unrelated active loops.
2. Inspect the active profile-owned cron stores first, not only the default/Karina store:
   - `hermes --profile yuna cron list --all`
   - `hermes --profile goyounjung cron list --all`
   - default/Karina `hermes cron list --all` only to find old duplicates/finalizers.
3. Patch existing cron prompts in place instead of creating new jobs.
4. Pause old default-store duplicates only when an active profile-owned job supersedes them and double delivery is possible.
5. Update downstream language that assumes the old count, such as finalizers, dashboard copy, or skill guidance.
6. Verify with both cron list output and a stale-count text scan of stored prompt JSON.
   - Search for stale phrases such as `Exactly 2`, `2 picks/day`, `2 items`, `각 2개`, `2장`, `two images`, `both images`.
   - For a 1+1 conversion, active research prompts should say exactly 1 visible item and do not exceed 1.

## Rerun a today-only missed specialist loop

1. Determine current KST date/time before selecting jobs.
2. Rerun only today's relevant failed job, not older outage failures or unrelated paused jobs.
3. For profile-owned jobs, run from that profile's cron store:
   - `hermes --profile faker cron run <job_id>`
   - then `hermes --profile faker cron tick` if queued execution does not happen promptly.
4. Verify completion from job metadata and output artifact:
   - `last_run_at` is after the repair attempt.
   - `last_status` is `ok`.
   - `last_error` and `last_delivery_error` are empty/none.
   - Read the latest cron output summary if the job can finish in a degraded mode.
5. If a coding-scope policy job gates the specialist loop, refresh that policy separately and distinguish:
   - loop execution succeeded, versus
   - actual implementation work happened.

## Chris-facing summary pattern

Keep it compact and concrete:

- what was changed/rerun;
- active job state after verification;
- what actually happened in the run;
- any remaining budget/credit blocker;
- reassure that unrelated loops were left alone when Chris asked that.

## Pitfall

A job can be `ok` while doing only a minimal verification path because a separate budget policy still says `minimal` or `0.0% remaining`. Do not report this as feature work completed. Say: “루프는 정상 실행됐고, 오늘은 예산 정책 때문에 코드 변경 없는 검증 모드로 끝났어.”
