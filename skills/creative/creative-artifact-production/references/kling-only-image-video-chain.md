# Kling-only image + video chain for Chris's visual loop

Use this when Higgsfield credits block still-image generation and Chris asks whether Kling AI alone can create both the still image and the follow-up video/turntable.

## Session-proven pattern

1. Verify the existing user-account Kling CLI route without exposing credentials:
   ```bash
   export PATH="/opt/data/.npm-global/bin:$PATH"
   HOME=/opt/data kling who_am_i --quiet
   HOME=/opt/data kling account --quiet
   ```
2. Discover current model names and parameters from `who_am_i`; do not assume old names.
3. For a low-risk feasibility test, run one selected prompt first, not the whole daily two-image/two-video loop.
4. Generate a 1:1 still image with Kling text-to-image, for example:
   ```bash
   HOME=/opt/data kling text_to_image \
     --model kling-image-v3_0 \
     --aspectRatio 1:1 \
     --imgResolution 1k \
     --imageCount 1 \
     --poll 600 \
     "$IMAGE_PROMPT" > text-to-image-result.json 2> text-to-image.stderr.log
   ```
5. Download the returned `urlWithoutWatermark` / `url_without_watermark` immediately; Kling result URLs may expire.
6. Inspect the image before spending video credits. For Chris's Go Youn-jung lane, check at least:
   - no pseudo-text, logo, caption, UI frame, poster label, decorative corner mark, or typography-like detail
   - premium calm object quality, not generic AI-startup gloss
   - correct 1:1 shape, object family, palette, material, and simple background
7. If acceptable enough for motion testing, generate image-to-video:
   ```bash
   HOME=/opt/data kling image_to_video \
     --model kling-video-v3_0_turbo \
     --image "$IMAGE_PATH" \
     --duration 5 \
     --resolution 720p \
     --imageCount 1 \
     --poll 600 \
     "$TURNTABLE_PROMPT" > image-to-video-result.json 2> image-to-video.stderr.log
   ```
8. Download the returned video URL. Run `ffprobe` to verify duration, resolution, and streams.
9. If any audio stream exists, create a muted delivery copy:
   ```bash
   ffmpeg -y -i raw.mp4 -an -c:v copy muted.mp4
   ```
10. Generate a contact sheet from the muted MP4 and visually inspect for text carryover, object morphing, camera instability, and unwanted frame/UI remnants.
11. Save all artifacts under the daily visual folder, for example:
   - prompt TXT files
   - `text-to-image-result.json` and stderr log
   - downloaded PNG/JPG
   - `image-to-video-result.json` and stderr log
   - raw MP4 and muted MP4
   - contact sheet
   - concise quality notes

## Important quality lesson

Kling can technically complete the full chain: text-to-image → image-to-video. However, Kling text-to-image may ignore `no text` instructions and add fake English lettering, poster captions, UI-like frames, or decorative graphic marks. Treat the first successful chain as feasibility evidence, not production approval.

For Chris's premium daily Go Youn-jung loop, rewrite Kling-only image prompts more aggressively than Higgsfield prompts:

- Prefer: `single object only, isolated on plain studio background, no poster, no frame, no border, no graphic design layout, no typography, no labels, no caption, no watermark, no UI overlay, no decorative corner symbols, no menu dots, no invented language marks`.
- Avoid phrases that invite editorial poster composition, title treatment, interface framing, or graphic-layout decoration.
- Inspect and reject images with pseudo-text before running video, unless the goal is only a charged feasibility test.

## Reporting to Chris

Keep the report concise:

- Say whether the chain worked technically.
- Name the models used.
- State the main quality issue plainly.
- Attach or point to the image and muted MP4 only if generated and verified.
- Do not imply the output is production-ready if pseudo-text or UI artifacts remain.
