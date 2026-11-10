# Directional sprite atelier delivery

Use this pattern when a Vite/React team scene needs approved directional pixel sprites and GitHub Pages delivery.

## Asset contract

- Store runtime sprites under `public/assets/team/atelier-sprites/<agent>/`.
- Keep a stable five-direction filename set: `front`, `front-three-quarter`, `profile`, `back-three-quarter`, `back`.
- Normalize all runtime files to the same transparent PNG dimensions and validate PNG signature, dimensions, and RGBA colour type before publishing.
- Expose paths through one typed `teamAtelierSpriteMap` rather than assembling arbitrary strings in components. Keep an image-load fallback to the existing public profile/avatar asset.

## Calm autonomous motion

- Use small full-body figures, long movement durations, staggered starts, and pointer-events disabled when the scene is ambient rather than interactive.
- Derive the directional frame from the movement delta; mirror diagonal/sideward frames for left/right travel instead of duplicating art.
- For walkable spaces containing furniture, reject destination candidates and sample each candidate path against obstacle rectangles. A valid endpoint alone is not enough: a direct line may cross a table.
- `prefers-reduced-motion: reduce` must prevent the motion scheduler from starting, not only remove CSS transition duration.

## Focused Pages delivery

1. Run sprite validation, lint, and a production build before staging.
2. `git fetch origin main` and inspect divergence before commit. In a nested app directory, stage explicit feature paths only; do not accidentally include root README edits, generated public manifests, or runtime metadata.
3. Check staged paths, whitespace, and added text for credential-shaped values. Treat generated sprite PNG/WebP files as binary assets and verify their explicit inventory.
4. After push, locate the GitHub Pages Actions run by the pushed head SHA. If `gh` is unavailable, GitHub's public Actions REST endpoint is sufficient for public repositories.
5. Wait for the exact run to complete successfully, then fetch the live Pages index. Resolve the hashed JS path correctly whether it is root-relative or base-relative, assert the new motion marker occurs in the live bundle, and confirm representative scene/sprite URLs return `200` with `image/*` content type.

This validates the shipped code and assets. Add browser visual QA when a browser runner is available; do not describe HTTP/bundle verification as visual-motion proof.

## Smooth illustration turnarounds: extraction and responsive QA

When a generated five-view turnaround is used as the source of individual transparent sprites:

1. **Do not crop at equal panel boundaries blindly.** Adjacent figures can bleed a narrow limb or hair fragment into the next cell. In each panel, derive the alpha mask, select the largest connected opaque component, and crop to that component’s bounding box.
2. Normalize each resulting pose by a **shared target height**, then center-pad it on the common transparent sprite canvas. Scaling each crop to an equal width makes profile poses look unnaturally broad.
3. Make a dark-background contact sheet of all directional poses before integration. It exposes background-key halos, clipped limbs, and neighbor slivers that a light atelier background can hide.
4. Verify the final files are RGBA, the expected dimensions, and all five directions load through the typed sprite map. Exercise keyboard and pointer movement, not only static image URLs.
5. For role bubbles on small viewports, assert every selected character’s bubble stays inside the scene. Use a responsive above-head offset for normal positions, and switch to a below-character placement for characters close to the scene top. Keep left/right edge variants; visually inspect mobile and tablet, not just desktop.
6. If the selected state already gives clear contextual feedback (for example an open role bubble), remove any product-unwanted keyboard focus stroke and test computed `outline-width` after an actual Arrow-key action.
