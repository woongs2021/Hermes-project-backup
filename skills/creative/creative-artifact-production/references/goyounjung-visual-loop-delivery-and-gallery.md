# Go Youn-jung Visual Loop: Delivery Identity + Webapp Gallery Feed

Use this reference for Chris's recurring Go Youn-jung Higgsfield image loop when it must both DM Chris and seed a future webapp gallery.

## User-facing delivery identity

Chris expects the daily visual loop to come from **Go Youn-jung's own DM/bot identity**, not Karina/default, even though Karina orchestrates the loop.

Pitfall discovered: a cron job can run with `profile: goyounjung` but still appear to Chris as Karina/default if `deliver: telegram` relies on scheduler/gateway auto-delivery. If Chris asks for the specialist to send it, do not assume profile ownership alone controls the visible Telegram sender.

Recommended pattern:

1. Keep the cron job owned by `profile: goyounjung`.
2. Set cron `deliver` to `local` for the user-facing visual loop output.
3. Inside the Go Youn-jung job, send the final DM and photo attachments directly from Go Youn-jung's Telegram bot/profile.
4. Start the DM copy with `고윤정입니다.` so the sender identity is explicit in the text as well.
5. Never print or log bot tokens. Load credentials from the profile-local env/config and mask errors.
6. Keep final cron output as a short local status, not the full DM, so the scheduler does not also auto-deliver from Karina/default.

## Daily content policy

- Generate two 1:1 Higgsfield images per day to conserve Higgsfield credits.
- Keep the two same-day color themes/metaphors non-overlapping, and use a 7-day rolling diversity rule so each day has a different color pairing and metaphor family when possible while preserving the approved premium soft-3D/editorial style.
- Exclude exact prompts from the recurring DM; save them locally and share only when Chris asks separately.
- Keep `왜 이 이미지인가` rationale in the DM.
- Prefer calm premium soft-3D / product-editorial / tactile object metaphors.
- Avoid strong wave, ripple, fluid, water, swirl, or flowing-sheet motifs unless Chris explicitly asks for them.

## Webapp gallery mirror

Chris wants the daily images to become one axis of Faker's future webapp: a Pinterest-like image dashboard tab where clicking an image reveals why it was generated.

After final image selection/delivery, mirror the webapp-ready set:

- Copy final PNGs to `/opt/data/hermes-webapp-build-loop/assets/image-gallery/YYYY-MM-DD/`.
- Write/update `/opt/data/hermes-webapp-build-loop/data/image-gallery/YYYY-MM-DD.json`.
- Append one normalized record per image to `/opt/data/hermes-webapp-build-loop/data/image-gallery/items.jsonl`.

Recommended record fields:

```json
{
  "id": "YYYY-MM-DD-short-title",
  "date_kst": "YYYY-MM-DD",
  "agent": "goyounjung",
  "title": "Image title",
  "theme": "Blue|Mint|Orange|Violet|...",
  "metaphor": "short metaphor label",
  "why": ["rationale bullet 1", "rationale bullet 2"],
  "model": "seedream_v5_pro",
  "webapp_asset_path": "/opt/data/hermes-webapp-build-loop/assets/image-gallery/YYYY-MM-DD/file.png",
  "source_path": "/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/...png",
  "display_mode": "pinterest_masonry_card",
  "interaction": "click_to_reveal_reason_drawer_or_modal",
  "prompt_policy": "exact_prompt_hidden_by_default; share only on Chris request"
}
```

## Faker handoff

Faker's future webapp planning/build loop should treat `data/image-gallery/items.jsonl` as a source adapter candidate:

- Top-level tab: `Images` or `Visual Archive`.
- Route candidate: `/visuals`.
- Default layout: masonry/Pinterest-style image cards.
- Card click opens a drawer/modal with large image, metaphor, `왜 이 이미지인가`, model, agent/date, and prompt-hidden policy.
- Public version may show polished image + short rationale; private/admin version may show richer metadata. Exact prompts stay hidden unless Chris approves or asks.
