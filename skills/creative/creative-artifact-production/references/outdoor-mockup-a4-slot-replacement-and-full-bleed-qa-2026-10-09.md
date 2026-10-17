# Outdoor Mockup A-4 slot replacement and full-bleed QA — 2026-10-09

Use this as a session-specific reference when Chris asks to replace a visible Outdoor Mockup A slot with a newly added manual Midjourney rail item, especially after the item was just appended with a 4K detail asset.

## What worked

- Resolve the requested Midjourney number from `public/data/midjourney-dna-archive.json`, and use its `highResImageSrc` as the motif source.
- Treat the visible slot label (e.g. `Outdoor Mockup A-4`) as a UI slot, not a stable internal ID.
- Generate the replacement under a fresh internal example ID and cache-busting asset root, then replace only the manifest-visible slot.
- Keep neighboring A-lane entries stable. Example after replacing A-4:
  - A-1: Midjourney 08
  - A-2: Midjourney 02
  - A-3: Midjourney 28
  - A-4: new requested Midjourney source
  - A-5: Midjourney 32
- Do not physically delete the old generated assets unless they are accidental candidates; remove the old set from the live manifest so it no longer appears.

## Item 5 full-bleed handling

For board/booklet/card item 5, prompt and direction images must cover both physical separation and surface coverage:

- use distinct crops per rear board and the small front card;
- preserve seam, step, overlap, paper thickness, shadows, and card depth;
- avoid one continuous panorama across both rear boards;
- require every visible paper/card/board face to be printed edge-to-edge;
- explicitly forbid blank white lower bands, unprinted paper base, large cream empty fields, and partially blank small cards.

If the source motif itself has large dark/light regions, a white or cream area may be interpreted as blank paper by Chris. Prefer a candidate where the source motif visibly occupies the lower bands and small card, even if the seam/crop is less elegant.

## QA loop that should be repeated

1. Generate all six outputs for the replacement set.
2. Build a contact sheet and inspect it before publishing.
3. For item 5, check full-bleed coverage separately from seam/step separation.
4. Run local manifest verification:
   - A-lane order and titles;
   - new internal ID in the visible slot;
   - old internal ID absent from the visible A manifest;
   - six files exist, dimensions `2496×1664`, hashes match.
5. Run `npm run build:public`.
6. Commit only the manifest and final six output files.
7. After push, poll the live `brand-mockup-assets.json` until the new slot appears.
8. Verify all six direct live image URLs return `200 image/png`, dimensions `2496×1664`, and manifest hash matches.
9. Run a browser/Playwright manifest-image probe to confirm no console errors and no overflow.

## Communication pattern

When reporting to Chris, say:

- which visible slot changed;
- which previous Midjourney source was removed from the live manifest;
- which new Midjourney source is now in that slot;
- build/commit/live verification status;
- the cache-busting URL with the commit query.

Avoid saying old files were deleted if they were only removed from the live manifest. Say “기존 세트는 live 목록에서 제거됨” unless actual filesystem deletion was requested and performed.
