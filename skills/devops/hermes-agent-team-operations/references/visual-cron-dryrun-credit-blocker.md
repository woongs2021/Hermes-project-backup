# Visual cron dry-run / credit-blocker delivery check

Use this when Chris reports that Go Youn-jung's daily visual work did not arrive, or when auditing specialist-owned generated-media cron jobs.

## Session-proven check pattern

1. Check the relevant cron entry, but do **not** treat `last_status=ok` as delivery proof.
   - A visual job can finish `ok` after writing dry-run notes or status files, while generating no media and sending nothing.
2. Inspect the dated visual folder, usually:
   - `/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/`
3. Look for delivery and generation status files before reporting to Chris:
   - `telegram-send-status.json`
   - `generation-results.json`
   - `delivery.md` or `delivery-message.txt` when present
   - actual media paths under `generated/`, `generated_png/`, `kling-turntable/`, `normalized/`, or similar folders
4. Interpret common fields:
   - `attempted: false` in `telegram-send-status.json` means no real platform send was attempted.
   - empty `photos` / `videos` means no user-facing media attachments exist.
   - `status: blocked_higgsfield_credits` or `attempted_generation: false` means the job prepared prompts only.
5. If generation was blocked by credits, verify the current media workspace status with the configured CLI before promising a rerun. Do not print tokens or raw credential output.
6. Report the distinction clearly:
   - scheduler executed
   - generation blocked or succeeded
   - Telegram/Slack delivery attempted or not attempted
   - actual media delivered or not delivered
7. If credits/auth are restored and the user asks for repair, rerun from the saved dry-run prompts rather than inventing new work, then verify generated file paths and real send status/message IDs.

## Chris-facing summary style

Keep it short and calm:

- “전달 안 된 게 맞아.”
- “원인은 Telegram이 아니라 Higgsfield credits 0으로 이미지가 생성되지 않은 거야.”
- “cron은 ok였지만 실제 미디어는 없었어.”
- “크레딧 복구되면 저장된 dry-run 프롬프트로 재생성해서 보낼 수 있어.”
