# Kling CLI Turntable Fallback Workflow

Use this when Higgsfield video/turntable credits are depleted but Chris wants turntable-style motion from Go Youn-jung daily graphics or other still images.

## What worked

- Official Kling CLI package: `@klingai/cli-global`
- Install location used in this environment: `/opt/data/.npm-global`
- Required command prefix:
  ```bash
  export PATH="/opt/data/.npm-global/bin:$PATH"
  HOME=/opt/data kling <command>
  ```
- OAuth credentials are saved under `/opt/data/.kling/`. Never print, mirror, or log the credentials file.
- The CLI is a thin client over Kling's MCP backend and supports:
  - `who_am_i`
  - `account`
  - `tool_list`
  - `text_to_image`
  - `image_to_image`
  - `text_to_video`
  - `image_to_video`
  - `file_upload`
  - `query_tasks`

## Headless OAuth pattern

1. Start login in a PTY so the authorization URL is visible:
   ```bash
   export PATH="/opt/data/.npm-global/bin:$PATH"
   HOME=/opt/data kling login
   ```
2. Send Chris only the current authorization URL.
3. Chris opens it, approves Kling access, then sends back the final browser URL that looks like:
   ```text
   http://127.0.0.1:8787/callback?code=...&state=...
   ```
4. Call that callback URL from the Hermes host while the login process is still waiting:
   ```bash
   curl -sS -i 'http://127.0.0.1:8787/callback?code=...&state=...'
   ```
5. Verify the response says `Login successful`, then verify with:
   ```bash
   HOME=/opt/data kling who_am_i --quiet
   HOME=/opt/data kling account --quiet
   ```

### Pitfalls

- The Kling login process times out after about 300 seconds. If it expires, start a new login and use only the newest URL.
- If callback returns `state mismatch`, Chris sent a callback URL from an older expired login. Ask him to use the current authorization URL and ensure the returned `state=` matches the running process.
- Run login with `pty=true` or an equivalent real terminal when using Hermes background process tools; non-PTY runs may not flush the login URL promptly.
- Sanitize any command output that could contain token-like strings. Do not print `/opt/data/.kling/.credentials`.

## Turntable generation recipe

For a still image that should become a 5-second product/object turntable:

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
export HOME=/opt/data
IMG=/absolute/path/to/image.png
OUT=/absolute/path/to/output-dir
mkdir -p "$OUT"
PROMPT='Create a clean 5-second seamless turntable animation of the exact object in the reference image. Keep the object identity, proportions, material, colors, lighting, and simple background unchanged. Slow smooth 360 degree rotation around the vertical center axis, premium soft-3D editorial product motion, stable camera, no zoom, no morphing, no added text, no extra objects, no audio.'

HOME=/opt/data kling image_to_video \
  --model kling-video-v3_0_turbo \
  --image "$IMG" \
  --duration 5 \
  --resolution 1080p \
  --imageCount 1 \
  --poll 600 \
  "$PROMPT" \
  --quiet > "$OUT/result.json" 2> "$OUT/stderr.log"
```

Then parse `result.json` for `urlWithoutWatermark` / `url_without_watermark` first, falling back to `url`, and download immediately because Kling result URLs may expire.

## Verification and Telegram delivery

- Verify downloaded video with `ffprobe`; expected successful test shape was h264, 1:1, about 5.04s, 24fps.
- Kling may include an audio track even when the prompt requests no audio. For Telegram delivery, create a muted copy:
  ```bash
  ffmpeg -y -i input.mp4 -an -c:v copy output.muted.mp4
  ```
- For Chris's Go Youn-jung visual loop, send final test videos from Go Youn-jung's Telegram bot identity, not Karina/default. Use the profile-local bot token carefully without printing it; record only message IDs and local file paths.

## When to use which model

- `kling-video-v3_0_turbo`: good default for single-image-to-video turntable tests; faster/value-oriented and supports 1:1 1080p.
- `kling-video-v3_0_omni`: consider for multi-image reference or more complex direction, but avoid it for simple turntables unless the added cost/complexity is justified.

## Recordkeeping

For Go Youn-jung daily graphics, store Kling fallback outputs under the same daily graphics date folder, for example:

```text
/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/kling-turntable/
```

Keep:
- raw Kling `result.json`
- stderr log if useful
- downloaded mp4
- muted Telegram-ready mp4
- Telegram send-status JSON with message IDs

Do not store raw OAuth tokens, private credentials, or full bot tokens in logs.
