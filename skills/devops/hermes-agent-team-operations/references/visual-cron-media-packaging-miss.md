# Visual cron media packaging miss

Use this when a specialist-owned visual cron job reports `last_status=ok` and generated media exists, but Chris says the visual report did not arrive or arrived without attachments.

## Failure pattern

A generated-media cron run has two different “delivery-shaped” artifacts:

1. Local draft/status files inside the dated work folder, for example:
   - `/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/final-delivery-message.txt`
   - `/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/telegram-send-status.json`
2. The actual final cron response stored under the specialist profile, for example:
   - `/opt/data/profiles/goyounjung/cron/output/<job_id>/YYYY-MM-DD_HH-MM-SS.md`

Cron auto-delivery sends the final response, not arbitrary local draft files. If the local draft contains `MEDIA:` lines but the final response only contains a text summary, Chris receives no images/videos even though the job is `ok` and media files exist.

## Audit steps

1. Check the specialist cron entry and note `deliver`, `profile`, `last_run_at`, `last_status`, and `last_delivery_error`.
2. Inspect the dated visual folder for generated stills/videos and status files.
3. Read `telegram-send-status.json`:
   - `attempted=false` with `delivery_mode=scheduler_auto_final_response` means direct send did not happen; the final response must carry the media.
4. Read the profile cron output markdown for that run and verify whether the `## Response` section contains the expected `MEDIA:` lines.
5. Compare it with `final-delivery-message.txt` when present.
6. Verify actual media files exist and videos are usable before resending.

## Repair pattern

- Do not regenerate charged media if the files already exist.
- Patch the active cron prompt so future final responses include the actual user-facing `MEDIA:` lines, not just a local draft. Include an explicit instruction such as:

```text
Final Telegram response:
- 반드시 최종 응답 본문에 실제 전달할 MEDIA 라인을 포함한다. 자동 cron delivery가 최종 응답만 전송하므로, 로컬 final-delivery-message.txt에만 MEDIA를 저장하고 최종 응답에서 빼면 Chris에게 이미지/영상이 전달되지 않는다.
- 포함 순서: still 1 MEDIA, turntable 1 MEDIA, still 2 MEDIA, turntable 2 MEDIA.
```

- For specialist-owned DM loops, prefer explicit `deliver=telegram:<Chris chat id>` in the specialist profile cron store, or use the direct-specialist Telegram Bot API pattern when auto-delivery would route through the wrong bot.
- Resend the already-generated assets from the specialist bot and record a local resend status file with platform message IDs, without printing tokens.

## Reporting to Chris

Keep it short and distinguish the layers:

- “생성 실패가 아니라 전달 패키징 문제였어.”
- “로컬 draft에는 MEDIA가 있었지만, 실제 cron final response에는 MEDIA가 빠져 있었어.”
- “오늘 건은 이미 생성된 파일로 재전송했고, 내일 cron prompt도 고쳤어.”
