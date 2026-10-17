# Multi-surface mockup crop/seam correction lessons

Use this when Chris says a mockup with multiple physical surfaces (books, boards, cards, panels) looks like one continuous graphic, or asks for A/B/A-1-like physical separation.

## User preference signal

Chris expects mockup graphics to respect the physical object structure. If there are two books/boards, the result should show:

- a clear physical step/depth difference;
- a visible seam or overlap edge;
- separate face geometry and shadows;
- different crops/angles of the same source motif on each surface when requested;
- no single panorama/continuous graphic running across both surfaces unless explicitly requested.

## Recommended workflow

1. **Use the best existing accepted mockup as a structure reference.** If Chris names `A-1-5` or another accepted item, inspect it and capture the separation logic: seam position, overlap, shadow, crop break, and relative depth.
2. **Do not keep patching if the issue is object-structure-level.** Local polygon patches can fix color/crop but often create mask edges or miss the full physical separation. For multi-surface failures, regenerate with Kling from:
   - rough direction image showing desired crops;
   - original clean mockup as camera/geometry/light source;
   - accepted reference mockup for seam/depth structure;
   - source motif/graphic.
3. **Generate at least 2 candidates** when the composition is subtle. Use a contact sheet and choose the one with the clearer seam/depth and more natural material integration.
4. **Prompt language that worked:**
   - “two distinct boards/booklets, visible vertical overlap/seam, slight depth difference, separate front faces”
   - “left board keeps one crop; right board uses a different crop/angle of the same graphic”
   - “do NOT look like one continuous panorama”
   - “preserve original camera, pebbles/background/table, lighting, shadows, tactile printed board texture”
   - negative: no text, logos, watermark, UI, extra objects, broken geometry, dirty mask edges, continuous graphic across the seam.
5. **Use cache-busting final filenames.** Keep candidates as working files if needed, but manifest should point only to the chosen final revision filename.
6. **Verify live, not just build.** Check:
   - JSON validation;
   - `npm run build:public`;
   - live manifest path changed to the new rev file;
   - asset URL returns `200 image/png`;
   - Playwright modal loads the final image at natural dimensions with no console errors/overflow.
7. **Separate real webapp/image errors from verification-harness timing.** For large lazy-loaded mockup images, Playwright page-level `naturalWidth: 0` can be a loading-timing false negative even when the asset is deployed. Before telling Chris there is an error, verify the exact manifest image paths directly: live manifest contains the new rev filename, direct asset request returns `200 image/png`, PNG signature is valid, and opening the image URL directly in Chromium reports the expected natural dimensions. Treat that as a verifier retry/fallback pattern, not a webapp failure.

## Manifest deletion and visible renumbering lessons

Use this when Chris asks to delete a visible mockup set (e.g. “A-3번은 삭제”) and “renumber/reorder” the remaining A/B versions.

- **Delete from the manifest, not necessarily from disk.** Unless Chris explicitly asks to remove files from storage, remove the set from the public manifest and keep underlying asset files intact for traceability/cache safety.
- **Renumber the visible layer only.** Preserve stable asset paths, hashes, and source image paths; update `title`, `displayOrder`, item `title`s (`A-3-1` etc.), and human descriptions so the UI reads cleanly.
- **Validate the resulting sequence deterministically.** Check count, order, sourceGraphic mapping, first/last item labels, and absence of the deleted source before building.
- **Build and verify live manifest.** `npm run build:public` and local JSON validation are necessary but not sufficient. After push, poll the live manifest with a cache-busting query and confirm the deleted set is absent and the remaining visible labels are contiguous.
- **GitHub Pages can lag even after push.** If a Pages deploy stays `in_progress`/`waiting` unusually long, an empty retrigger commit can be used to supersede the stuck run when workflow concurrency is configured to cancel in-progress runs. Do not report completion until the live manifest reflects the new order.
- **Playwright final check:** fetch the live manifest from the page context and verify the visible A/B list has expected titles, sources, item counts, and no console errors/overflow.

## Outdoor bucket hat motif-scale lessons

Use this when Chris says a hat mockup is “아쉽다,” too busy, too stripe-heavy, or too small-patterned.

- **Stripe/block motifs on hats:** if Chris asks to reduce “가운데 줄 여러개,” do not rely on a generic “large fields” prompt alone. Kling may keep a central barcode-like stripe curtain because the source motif contains strong stripes. Prompt with explicit placement: “front-center crown must be mostly broad coral/cream/black/gray color fields; stripes are sparse side/edge accents only; at most 2–3 vertical stripe accents; no central barcode / no repeated stripe curtain.”
- **Pattern-grid motifs on hats:** if Chris says it is too “오밀조밀,” ask for larger modules, fewer blocks, and calm negative-space rhythm: “scale the modular woven block pattern much larger; use fewer, bigger blocks; avoid small checkerboard noise.”
- **Avoid heavy local patching on curved fabric.** A rectangular local patch can float on top of the bucket hat and destroy material believability. If a post-composite correction creates visible rectangular edges, discard it and use the best natural Kling candidate instead.
- **Candidate policy for subtle hat revisions:** generate at least 2 candidates, make a contact sheet, and choose the one that best satisfies Chris’s exact correction even if another candidate is technically cleaner.

## Pitfalls

- A local patch can accidentally apply at the wrong scale/coordinates when reviewing thumbnails vs full-res. Use full image dimensions and verify with vision before publishing.
- A crop difference alone is not enough; Chris specifically cares about the physical seam/step that proves the boards are separate objects.
- If a generated candidate preserves the seam but the right/left graphics still mirror too closely, regenerate with stronger “different crop/angle” language instead of only editing the manifest.
- For horizontal stripe/band motifs, “different crop” must also mean **non-aligned band positions**: the stripe heights, color order, and horizontal bands should not line up across the seam. Prompt explicitly: “The horizontal bands must NOT line up across the seam; colors and band heights should be offset like independent printed boards.”
- For board/booklet sets that also include a small front business card/name-card, validate the small card as its own physical surface. Chris may reject the image if that card appears to contain an unrelated graphic even when the rear books look acceptable. In the regeneration prompt, explicitly state: “the left booklet, right booklet, and small front name-card/business-card must all use different crops of the SAME source graphic; do not put any unrelated image on the small card; no blank white unprinted card.” In candidate QA, reject candidates where the small card becomes a striped/foreign card or mismatched artwork.
- When a candidate fixes the small card but leaves one rear booklet too blank, prefer a candidate that balances both constraints: same-source card plus visible printed rear surfaces plus seam/step. If no candidate satisfies all three, regenerate rather than publishing a partially fixed result.
