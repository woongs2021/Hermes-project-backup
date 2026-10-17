# Midjourney asset → Outdoor Mockup version workflow

Use when Chris first adds one or more manual Midjourney assets to the Design DNA Midjourney rail and then asks to synthesize one of those assets into a new `Outdoor Mockup A/B-N` version, e.g. “A-5로 미드저니 32 합성해서 추가해줘.”

## Core pattern

1. **Resolve the source Midjourney item by visible sequence number.**
   - Read `public/data/midjourney-dna-archive.json`.
   - Find the item whose title starts with `Midjourney NN — ...`.
   - Prefer `highResImageSrc` as the synthesis motif when present; this should be the `4096×4096` detail/download asset.

2. **Resolve the target mockup lane.**
   - For `Outdoor Mockup A-N`, use `public/data/brand-mockup-assets.json` collection `outdoor-mockup-assets-1`.
   - For `Outdoor Mockup B-N`, use `outdoor-mockup-assets-2`.
   - Append the next visible version number without changing earlier version labels unless Chris explicitly asks to reorder.

3. **Use a new cache-busting example id and asset directory.**
   - Example: `outdoor-mockup-example-a-09/2026-10-09/` for a new A version.
   - Do not overwrite existing A/B version files.
   - Keep underlying historic paths stable; update visible manifest metadata.

4. **Generate all six outputs with original mockup geometry + source motif.**
   - image 1: rough placement/direction composite.
   - image 2: original clean mockup from the target collection.
   - final image: Midjourney high-res motif.
   - Prompt for full-surface physical print/material integration while preserving camera, perspective, shadows, folds, fabric/paper texture, foreground objects, and 3:2 aspect ratio.

5. **Treat item 5 as a special multi-surface QA case.**
   - The white board/booklet set includes two rear boards/booklets and a small front card/name-card.
   - Include accepted structure references from previous item-5 successes when available.
   - Prompt explicitly: the left booklet, right booklet, and small front card all use different crops of the SAME source graphic; do not put an unrelated image on the small card; preserve seam/step/overlap/depth; do not make a continuous panorama.

6. **Create a contact sheet before publishing.**
   - Check all six for natural physical integration, no pseudo text/logo, no dirty masks, no broken geometry.
   - For item 5, specifically check same-source card/booklet usage and physical separation.
   - If one image is weak, revise only that numbered item with a new filename.

7. **Update and verify the manifest.**
   - Add a new `examples[]` entry with `tabId` matching the lane, `displayOrder` as the next visible number, `sourceGraphic` matching the Midjourney item, and six `items[]` entries.
   - Each item needs `imageSrc`, `downloadSrc`, `assetHash`, dimensions, `sourceGraphicHighResImageSrc`, `resynthesisSourceImageSrc`, `mockupCollectionId`, `applicationMode`, `updatedAt`, and `displayOrder`.

8. **Run full verification before reporting.**
   - `npm run build:public`.
   - Local manifest assertions: visible A/B order includes the new version, six items, files exist, dimensions match, hashes match.
   - Push only the new final assets and manifest; do not include candidate files or provider logs.
   - Live Pages: manifest reflects new version, all six image URLs return `200 image/png`, dimensions match, hashes match.
   - Playwright/new-Image probe: all six images load, no console errors, no horizontal overflow.

## Copy / naming guidance

- Title: `Outdoor Mockup A-5`, item titles `Outdoor Mockup A-5-1` … `A-5-6`.
- Description should describe the visible synthesis and physical surface use, not internal generation history.
- Good item-5 description: “two boards/booklets and the small front card use different crops of the same Midjourney source while preserving seam/step/physical separation.”

## Pitfalls

- Do not use the 1024 thumbnail/original when a `highResImageSrc` exists; use the 4K source for synthesis.
- Do not trust lazy mounted DOM image `naturalWidth` alone. Verify direct URLs and in-page `new Image()` loads.
- Do not commit raw Kling/Higgsfield logs under `public/assets`; local logs belong under `/opt/data/dna-archive/...` or `/opt/data/dna-brand-assets/...`.
- Do not let item 5’s front card drift to a previous A version’s graphic. Chris notices card-source mismatches even when rear boards look acceptable.
