# Outdoor mockup: using newly added Midjourney rail assets as A/B version slots

Use when Chris first adds manual Midjourney assets to the Design DNA Midjourney rail, then asks to synthesize one of those numbered assets into an Outdoor Mockup A/B child set or replace an existing visible slot.

## Session pattern captured

- Chris added three manual Midjourney assets as `Midjourney 31–33`, each with original `1024×1024` rail images and Kling 4K detail assets in `public/data/midjourney-dna-archive.json`.
- Immediately after, Chris asked to:
  - add `A-5` using `Midjourney 32`;
  - replace existing `A-4` with `Midjourney 31` and delete the old visible A-4.
- The successful pattern was to use the Midjourney **4K** asset as the synthesis source for mockups, while keeping the Midjourney rail manifest unchanged.

## Workflow

1. **Resolve the Midjourney source number first.** Read `public/data/midjourney-dna-archive.json` and confirm:
   - visible title, e.g. `Midjourney 32 — Rounded Overprint Color Blocks`;
   - `highResImageSrc` exists and is `4096×4096`;
   - original rail asset and 4K asset hashes match their manifest fields.
2. **Choose the operation type.**
   - New child set: append the next visible A/B number, e.g. `Outdoor Mockup A-5`.
   - Replacement: preserve the requested visible slot, e.g. `Outdoor Mockup A-4`, and replace only that manifest entry.
3. **Use a fresh internal ID / cache-busting asset root.** Examples that worked:
   - new A-5 from MJ32: `outdoor-mockup-example-a-09`;
   - replacement A-4 from MJ31: `outdoor-mockup-example-a-10`.
   Do not rely on the old slot's internal ID if the source changes; visible label and internal ID are separate concerns.
4. **Generate six images from the raw Outdoor Mockup A collection.** Use the same raw mockup collection (`outdoor-mockup-assets-1`) and the selected Midjourney 4K source motif.
5. **Special case item 5.** For the two-board/booklet/card mockup:
   - use accepted A-1/A-2/A-3/A-5 item-5 outputs as structure references only;
   - require left booklet, right booklet, and small front card to use different crops of the same source graphic;
   - explicitly forbid an unrelated image on the small card, blank cards, continuous panorama alignment, dirty mask edges, or broken geometry.
6. **Inspect a contact sheet before publishing.** Check for:
   - natural material integration;
   - no pseudo-text/logo/UI artifacts;
   - no dirty masks or broken geometry;
   - item 5 physical seam/step/card separation.
7. **Manifest surgery.**
   - New child set: insert the new example after the current last A set and set `displayOrder` accordingly.
   - Replacement: remove the old visible slot entry from `examples[]` and insert the new entry in the same visible position. Keep neighboring sets unchanged.
   - For user wording “기존꺼는 삭제”, remove from the **live manifest** so it is no longer exposed; do not delete historical asset files unless they are temporary/candidate mistakes.
8. **Verify before final response.**
   - JSON / local manifest assertions: A order and source labels are correct.
   - `npm run build:public` succeeds.
   - Commit only final manifest and final generated images; exclude contact sheets, raw provider logs, and candidate files.
   - Live Pages manifest shows the requested A/B order and source labels.
   - Each new live asset URL returns `200 image/png`, `2496×1664`, and hash matches manifest.
   - Playwright probe loads the new images, with no console errors and no overflow.

## Prompt cues that worked

For normal A/B mockups:

> Apply the source as full-surface physical print/fused material on the relevant product/poster/card/surface. Preserve perspective, shadows, folds, fabric/paper texture, foreground objects and 3:2 aspect ratio. Clean premium synthesis. No text, logo, watermark, sticker look, dirty mask edges, broken geometry, extra objects, fake UI.

For item 5:

> The left booklet, right booklet, and small front card must all use different crops of the same source graphic. Do not put any unrelated image on the small card. Keep two rear booklets clearly separated, not one continuous panorama. Realistic printed paper, shadows and thickness. No text, logo, watermark, UI, extra objects, dirty mask edges, broken geometry, blank white card.

## Pitfalls

- Do not confuse the Midjourney rail number with Outdoor Mockup visible numbering. `Midjourney 32` can become `Outdoor Mockup A-5`; `Midjourney 31` can replace `Outdoor Mockup A-4`.
- Do not use the 1024 rail image for mockup synthesis when a verified 4K `highResImageSrc` exists.
- Do not renumber A-5 when replacing A-4 unless Chris asks for a broader reorder.
- Do not claim deletion means filesystem deletion. For the webapp, “delete existing” normally means remove the old visible manifest entry so the dashboard no longer exposes it.
- Avoid committing raw Kling logs or contact sheets under public assets.
