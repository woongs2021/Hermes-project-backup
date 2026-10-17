# Agent-team profile image asset handoff

Use this reference when Chris shares agent/profile images for a future homepage, dashboard, team-introduction page, or OBD/profile section.

## Workflow

1. Treat uploaded portraits as durable product assets, not just chat images.
2. Normalize filenames by role/name before handoff to implementation, e.g.:
   - `karina_profile.jpg`
   - `yuna_profile.jpg`
   - `goyounjung_profile.jpg`
   - `son_profile.jpg`
   - `faker_profile.jpg`
   - `muyeol_profile.jpg`
   - `chris_profile.png` for Chris's representative OBD/profile avatar.
3. Store canonical copies under `/opt/data/agent-team-assets/profile-images/`. When also used in the webapp, mirror the same normalized file into a stable public asset path such as `<webapp>/public/assets/team/chris_profile.png` and verify hashes match.
4. Create or update `MANIFEST.md` in the asset folder with file mapping, visual description, intended usage, user corrections, and implementation notes.
5. If Chris corrects which image belongs to which agent or asks for a new representative image, update the normalized filename mapping immediately and call out the correction in the manifest.
6. For homepage/team/OBD pages, use circular or rounded-square portraits and keep the design restrained, premium, and non-generic.
7. After implementation, verify both the stored durable asset and the webapp/public asset by dimensions/hash, then verify live DOM image load and responsive layout before reporting success.

## Current known mapping from this session

Check the live asset folder and `MANIFEST.md` before relying on this snapshot; Chris may manually rename or correct mappings. Current durable pattern:

- `karina_profile.jpg` — Karina agent profile image.
- `yuna_profile.jpg` — Yuna agent profile image.
- `goyounjung_profile.jpg` — Go Youn-jung agent profile image.
- `son_profile.jpg` — Son agent profile image.
- `faker_profile.jpg` — Faker agent profile image.
- `muyeol_profile.jpg` — Muyeol profile image; Chris corrected that the terracotta/rust portrait is the right Muyeol image.
- `chris_profile.png` — Chris representative AI avatar portrait generated/refined from Chris's reference photo; use as the canonical Chris image across About OBD and Operating Map cards.
- `chris_profile.png` — Chris representative AI avatar. Generate/refine from Chris's own reference portrait when asked, save durably under `/opt/data/agent-team-assets/profile-images/chris_profile.png`, and mirror into the webapp at `public/assets/team/chris_profile.png`. Current preferred treatment: front-facing direct gaze, slightly mannequin-like premium AI/avatar finish, dark blazer / black crew-neck, muted blue-gray studio background.

## Chris representative avatar workflow

When Chris asks to turn his own image into an agent-style representative image:

1. Use the uploaded portrait as a reference, not a raw persistent web asset.
2. Match the agent portrait system: square bust portrait, centered/front-facing pose, simple muted studio background, dark blazer/black crew-neck if present, warm but restrained expression.
3. If Chris asks for “more mannequin-like,” prompt for: more symmetrical front-facing gaze, squared shoulders, smooth refined skin, sculptural facial planes, polished synthetic AI-avatar quality; avoid plastic toy, cartoon, anime, neon, harsh shadows, text, logos, accessories.
4. With Kling CLI, use:
   ```bash
   HOME=/opt/data PATH="/opt/data/.npm-global/bin:$PATH" kling image_to_image \
     --image <reference> \
     --model kling-image-v3_0 \
     --img_resolution 2k \
     --aspect_ratio 1:1 \
     --imageCount 1 \
     --poll 240 \
     '<prompt>' \
     --quiet
   ```
   Then download `urlWithoutWatermark` and verify dimensions/hash. Never expose credentials or private auth files.
5. Save canonical and implementation copies:
   - `/opt/data/agent-team-assets/profile-images/chris_profile.png`
   - `<webapp>/public/assets/team/chris_profile.png`
6. For OBD About/Profile cards, interpret requested percentages like “70% size” or “80% of current” as rendered CSS size changes unless Chris asks to downsample the asset. Keep the 2K source and adjust width/grid columns in CSS. Session-proven values after the smaller refinements: desktop `101px`, mobile `92px` for the About OBD profile card.
7. In Operating Map cards, reuse the same `chris_profile.png` in both start/end Chris nodes, following the existing `.obd-agent-face` pattern (`50px` circular face, `object-fit: cover`).
8. For OBD pages, `#obd` defaults to About OBD; click the `Signal Loop` or `Operating Map` subtab in browser QA when validating those cards.

## Pitfalls

- Do not leave assets only in ephemeral Telegram cache names.
- Do not assume role mapping if the user corrects a filename or identity; the corrected mapping wins.
- Do not infer identity from background color or clothing when normalized filenames and the manifest disagree; inspect/update the manifest and keep filenames as the implementation source of truth.
- When refining Chris's representative portrait, small iterative instructions matter: “more front-facing,” “more mannequin-like,” and “profile size to 70/80%” should be encoded as image-generation/style or CSS-size changes, then verified with rendered pixel dimensions on desktop and mobile.
- Do not embed private platform identifiers or tokens in manifests or work logs.
- For webapp `<img>` elements that set `width`/`height` attributes, CSS `aspect-ratio` alone may not produce a square rendered box. Explicitly set `height: auto` or the intended CSS height, then verify with browser DOM metrics.
- When inserting profile images into responsive cards, verify desktop and mobile: image complete, natural dimensions, rendered square/rounded frame, `object-fit: cover`, and horizontal overflow 0.
- When validation scripts regenerate public data manifests with timestamp-only changes, revert those generated files before committing unless the task explicitly requires data refresh.
