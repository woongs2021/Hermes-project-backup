# DNA Brand Asset coffee pattern example sequence

Use when Chris asks to add another `Coffee Pattern Example NN` in **Design DNA → DNA Brand Asset → Midjourney + Mockup** using an existing DNA Dashboard / Midjourney motif.

## Durable pattern from Example 02–04

- Source mockup set: the existing six `Coffee Mockup Assets` under `public/assets/dna-brand-assets/mockup/coffee-mockup-assets/2026-09-26/`.
- Source motif: a saved Midjourney rail item. Historical mappings may change after curation/reindexing; trust the current manifest over old chat labels. Examples from 2026-09-28:
  - `Midjourney 15 — Cyan Luminous Arc Edge Translation` and `Midjourney 18 — Floral Radial Signal Bloom` were generated but later removed from public display because Chris judged them visually too complex; keep archives recoverable but do not assume they should stay published.
  - `Midjourney 20 — Monochrome Architectural Block Surface` → retained after reindex as `Coffee Pattern Example 02`
  - `Midjourney 08 — Soft Circular Ring Translation` → retained after reindex as `Coffee Pattern Example 03`
  - `Midjourney 07 — Warm Earth Oval Surface Translation` → `Coffee Pattern Example 04`
  - `Midjourney 11 — Ambient Blue-Peach Gradient Surface Translation` → `Coffee Pattern Example 05`
- Synthesis tool: Higgsfield `nano_banana_pro`, 3:2, 2k.
- Synthesis tool: Higgsfield `nano_banana_pro`, 3:2, 2k.
- Output style: **pattern-only**. Do not add logo text, letters, watermarks, placeholder marks, or extra graphics outside the printable surfaces.
- Webapp manifest: append one collection to `public/data/brand-mockup-assets.json` under `examples[]` with id `coffee-asset-example-NN`, title `Coffee Pattern Example NN`, `sourceGraphic`, six `items[]`, and `synthesisTool: Higgsfield Nano Banana Pro`.
- Webapp assets: `public/assets/dna-brand-assets/midjourney-mockup/coffee-asset-example-NN/YYYY-MM-DD/`.
- Archive originals: `/opt/data/dna-archive/brand-assets/coffee-asset-example-NN/YYYY-MM-DD/` with `raw/`, `images/`, `contact_sheet.jpg`, and `manifest.json`.

## Prompt shape

Use two image references: mockup first, motif second.

Core prompt:

> Create a high-quality realistic coffee brand mockup based on reference image 1. Preserve the same product, camera angle, lighting, shadows, material texture, depth of field, and 3:2 composition. Apply the [motif name] skin from reference image 2 only onto the blank printable [surface]. Use substantial printed color/shape fields that match the motif. Make the skin look physically printed on the material, following perspective, folds, cylinder curvature, fabric weave, paper grain, or sign-plane geometry as appropriate. Keep it pattern-only: no logo, no text, no letters, no watermark, no placeholder marks, no extra graphics outside the printable surface. Preserve a premium calm coffee mockup mood.

Adjust motif-specific language:

- Cyan arc: “substantial dark teal/black filled surface fields”, “cyan edge/rim accents”, “not only thin line art”, and apply to **all** relevant printable surfaces.
- Floral bloom: “petal-like radial wedges, coral, deep red, black, peach beige, muted teal accents.”
- Monochrome block: “substantial black fields, warm white slab shapes, gray diagonal planes, hard-edged editorial geometry, tactile print grain, high-contrast negative space.”
- Soft circular ring: “substantial printed circular fields, softened ring bands, warm ivory, muted blush beige, charcoal, soft gray, subtle orange-red accent arcs.” Expect a brighter, calmer set than the darker cyan/monochrome examples; this is acceptable if the ring is physically integrated and the set remains pattern-only.
- Soft circular ring: “substantial printed circular fields, softened ring bands, warm ivory, muted blush beige, charcoal, soft gray, subtle orange-red accent arcs.” Expect a brighter, calmer set than the darker cyan/monochrome examples; this is acceptable if the ring is physically integrated and the set remains pattern-only.
- Warm earth oval: “substantial printed oval fields, soft capsule-like shapes, warm terracotta, clay brown, muted cream, sand beige, charcoal, subtle rust accent arcs.” Use when Chris wants warmer, calmer physical-surface applications after removing visually dense examples.
- Ambient blue-peach gradient: “substantial printed gradient fields, soft atmospheric blue, peach, warm cream, pale coral, misty gray, subtle blurred transition bands.” Explicitly avoid busy linework; this set should feel calm, premium, and material-integrated rather than graphic-heavy.

## Curation, deletion, and reindexing lessons

- If Chris says a set is “too complex” or visually noisy, remove it from the public webapp manifest/assets instead of arguing or over-explaining. Preserve the local source archive under `/opt/data/dna-archive/brand-assets/` so it can be restored later.
- After deleting middle examples, reindex the public examples to close gaps when Chris asks for renumbering. Update **both** collection ids/titles and every item id/imageSrc path; move/rename public asset directories so the URLs match the new numbering.
- Keep source identity in `sourceGraphic` even after reindexing. Example title numbers are presentation order; `sourceGraphic` records the actual Midjourney motif lineage.
- Verify reindexing with JSON inspection plus browser QA: expected ids in order, expected titles `Coffee Pattern Example 01..NN`, old removed numbers absent when appropriate, all tile images loaded, modal sourceGraphic correct, and overflow zero.

## QA and publishing sequence

1. Generate all six images, retrying only failed items when Higgsfield/Kling returns transient failures.
2. Build a contact sheet before publishing; check surface integration, coverage, no text/logo/watermark, no broken crops, and set consistency. If Chris says a set is “too complex” or visually noisy, remove it from public display rather than defending the output; preserve source archives for possible recovery.
3. Use the output format intentionally:
   - Older Higgsfield/Nano Banana examples often used web JPEG derivatives around `2528×1696`.
   - Kling 4K coffee examples can be published directly as `4992×3328` PNGs under `public/assets/dna-brand-assets/midjourney-mockup-4k/...` when Chris asks for a high-quality new mockup example.
4. Update manifest and archive manifest; validate JSON. For new 4K examples, include `originalImageSrc`, `downloadSrc`, `sourceGraphicHighResImageSrc`, and `resynthesisSourceImageSrc` for each item.
5. Build the webapp.
6. Browser-check desktop/tablet/mobile:
   - Example count increases as expected.
   - The new collection has six tiles.
   - Every tile image loads with nonzero natural width.
   - Detail modal shows the correct `sourceGraphic` and image.
   - Horizontal overflow is zero.
7. After deploy, verify live manifest and all six URLs return `200 image/*`, then run live browser QA. For `4992×3328` PNGs, direct URL hash verification can exceed a short timeout; split the checks into smaller batches or raise the timeout instead of treating it as a failed deploy.

## Kling 4K coffee example variant

Use this when Chris says “커피 목업 예시 N번으로 미드저니 NN번 매칭해서 합성 후 새로 추가해줘” and the requested example number is a new visible coffee mockup example.

- Resolve the current Midjourney item from `public/data/midjourney-dna-archive.json`; use its `highResImageSrc` as the source graphic.
- Reuse the six raw Coffee Mockup Assets under `public/assets/dna-brand-assets/mockup/coffee-mockup-assets/YYYY-MM-DD/`.
- Generate with Kling `image_to_image`, model `kling-image-v3_0_omni`, `--img_resolution 4k`, `--aspect_ratio 3:2`, references ordered as mockup first and motif second.
- Store outputs under `public/assets/dna-brand-assets/midjourney-mockup-4k/coffee-asset-example-NN/YYYY-MM-DD/` and mirror to `/opt/data/dna-brand-assets/midjourney-mockup-4k/coffee-asset-example-NN/YYYY-MM-DD/`.
- Append a new `examples[]` entry with visible title `Coffee Mockup Example N`, sourceGraphic set to the Midjourney title, six items, and no pseudo-logo/text fields.
- Contact-sheet QA should check: motif visible on cup/bag/sign printable surfaces, no large blank white panels, no pseudo typography/logo, geometry preserved, and all six outputs feel like one coherent cafe identity set.
- 2026-10-10 precedent: `Coffee Mockup Example 4` used `Midjourney 35 — Diagonal Textile Stripe Bands`; all six Kling 4K PNGs were `4992×3328` and required split direct-URL verification because the full batch was slow to download.
- Rendering pitfall from the same session: the generated files and manifest can be correct while the webapp grid still shows raw mockup originals if the React tile uses `originalImageSrc ?? imageSrc`. For Midjourney + Mockup and generated brand-mockup tiles, the card/list thumbnail must prefer `imageSrc`; keep `originalImageSrc` only as provenance/detail metadata. Always run a rendered DOM/network probe that proves the visible grid loads synthesized filenames, not just direct asset URLs or manifest entries.

## Curation, removal, and reindexing

- When Chris asks to delete examples because they feel complex/noisy, remove those collections from `public/data/brand-mockup-assets.json` and remove their public asset directories so the live webapp is visually curated.
- Do **not** delete the source archive under `/opt/data/dna-archive/brand-assets/<example>/...`; leave it recoverable and optionally write a small removal marker under `_removed-from-public/`.
- If deletions leave gaps, reindex public examples so the visible webapp sequence is contiguous (`Example 01`, `02`, `03`, ...). Update each collection `id`, `title`, each item `id`, and each item `imageSrc` directory path.
- Rename or move public asset directories to match the new ids; then validate JSON, build, and QA desktop/tablet/mobile. Check that old numbers are gone from visible text and the expected tile count equals `visible_examples × 6`.
- After GitHub Pages deployment, poll the live manifest until the new order appears, then live-verify all images and at least one modal for the newest/reindexed collection.

## Curation, pruning, and numbering

- Chris may reject generated example sets as “too complex” or “ambiguous.” Treat that as a public curation decision, not a generation failure.
- When removing rejected examples, delete them from the public webapp manifest and public assets, but keep the local source archive under `/opt/data/dna-archive/brand-assets/` so the set can be restored later.
- Do **not** automatically renumber after deletions. Preserve the current public numbering unless Chris explicitly asks for “넘버링 재정렬.”
- If Chris explicitly asks to reindex, update both `examples[].id/title` and every item id/imageSrc path, then live-verify that the intended sequence and sourceGraphic mapping are correct.
- When Chris says “현재 기준으로 3,4번 삭제,” interpret the currently visible public numbering literally, not the historical generation order.

## Revision/caching lesson

If Chris says desktop still shows an old image while mobile/tablet look updated, suspect public image caching when the filename stayed the same. For single-item replacements, write a revision filename such as `_rev01`, update manifest `imageSrc`, and live-verify desktop/tablet/mobile DOM loads the new URL.

## Curation/removal lesson

Coffee pattern examples are a curated rail, not a purely append-only gallery. If Chris says an example is too complex, visually dense, or no longer fits the direction, remove it from the **public webapp** while preserving the source archive for possible future recovery.

Removal workflow:

1. Remove the target `coffee-asset-example-NN` entries from `public/data/brand-mockup-assets.json` `examples[]`.
2. Delete the corresponding public asset directory under `public/assets/dna-brand-assets/midjourney-mockup/coffee-asset-example-NN/` so stale images are not shipped.
3. Do **not** delete `/opt/data/dna-archive/brand-assets/coffee-asset-example-NN/`; keep raw outputs, contact sheets, and manifests for restoration or future comparison.
4. Optionally write a small marker under `/opt/data/dna-archive/brand-assets/_removed-from-public/YYYY-MM-DD/` noting that public exposure was removed by Chris feedback.
5. Validate JSON, build, and browser-check desktop/tablet/mobile that:
   - removed example titles are absent,
   - remaining examples and tile counts match expectation,
   - remaining images and modals still load,
   - horizontal overflow is zero.
6. After deploy, wait for the live manifest to update and verify the removed examples are absent from the hosted manifest before final reporting.
