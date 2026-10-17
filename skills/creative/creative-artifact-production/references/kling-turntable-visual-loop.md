# Kling-first turntable workflow for Chris's Go Youn-jung visual loop

## Context

Chris's daily Go Youn-jung visual loop now produces two still images and two turntable videos. Higgsfield remains the image-generation studio for the still images, but turntable/video generation should use Kling AI directly while Kling credits remain.

This rule came from Chris's correction: do not treat Kling as a fallback only when Higgsfield turntable credits fail. Use Kling-first for turntables until Kling credits are exhausted; only then check Higgsfield balance/availability.

## Operating rule

1. Generate exactly two final/pending-review still images for the day using the existing Go Youn-jung image workflow and style rules.
2. For each final still image, generate a Kling image-to-video turntable by default.
3. Use the official Kling CLI OAuth connection:
   - `export PATH="/opt/data/.npm-global/bin:$PATH"`
   - `HOME=/opt/data kling ...`
   - Do not print, read, copy, or log `/opt/data/.kling/.credentials`.
4. Preferred generation shape:

```bash
HOME=/opt/data kling image_to_video \
  --model kling-video-v3_0_turbo \
  --image "$IMAGE_PATH" \
  --duration 5 \
  --resolution 1080p \
  --imageCount 1 \
  --poll 600 \
  "$TURNTABLE_PROMPT" \
  --quiet
```

5. Prompt intent: clean 5-second seamless slow 360-degree vertical-axis product turntable; preserve object identity, color, material, lighting, and simple background; stable camera; no morphing; no added text; no extra objects; no audio.
6. Download `urlWithoutWatermark` / `url_without_watermark` when available.
7. Save all Kling artifacts under the daily folder, preferably `kling-turntable/`:
   - result JSON
   - stderr log
   - raw MP4
   - muted MP4
   - ffprobe/quality metadata if practical
   - Telegram send status JSON
8. If the MP4 contains audio, create a muted delivery copy with ffmpeg.
9. Send from Go Youn-jung's own Telegram bot: text + two still images + two muted turntable videos.
10. Write `telegram-send-status.json` with real Telegram `message_id`s. Do not consider the run complete merely because media files were generated.

## Credit and fallback rule

- Do not check/use Higgsfield turntable first.
- Keep using Kling while Kling credits remain.
- If Kling reports insufficient credits or credit exhaustion, then check Higgsfield balance/availability and report a temporary fallback recommendation.
- If Kling times out or has a service error that is not confirmed credit exhaustion, report the blocker and ask Chris before resubmitting another charged job.

## Delivery contract

The daily Go Youn-jung DM should include:

- Two still images as native Telegram photo attachments.
- Two Kling turntable videos as native Telegram video attachments.
- Concise Korean 존댓말 rationale.
- Image model used and why.
- Kling turntable model used and constraints.
- A note that exact prompts are saved locally and shared only on request.

## Common pitfall

A cron run can show `last_status=ok` even when direct Telegram send was skipped or not verified. Always check for the daily `telegram-send-status.json` and real message IDs. If missing, resend from the Go Youn-jung bot without regenerating media, to avoid unnecessary Kling credit use.