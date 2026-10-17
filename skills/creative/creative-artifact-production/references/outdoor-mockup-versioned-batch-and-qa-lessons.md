# Outdoor Mockup versioned batch + live QA lessons

Use when Chris asks to add versioned Outdoor Mockup child sets such as `A-3`, `B-2`, or `B-3` by mapping a numbered Midjourney asset to an existing mockup lane.

## Version/lane mapping

- Preserve stable lane/tab IDs where possible:
  - Outdoor Mockup A usually stays on existing `tabId: outdoor-mockup-1`.
  - Outdoor Mockup B usually stays on existing `tabId: outdoor-mockup-2`.
- Add new child collections rather than overwriting earlier sets:
  - `Outdoor Mockup A-1`, `A-2`, `A-3`...
  - `Outdoor Mockup B-1`, `B-2`, `B-3`...
- Insert new child collections immediately after the prior sibling in manifest order so the UI reads as a sequence.
- Use cache-busting filenames that include lane/version/source number, e.g. `05_outdoor-mockup-b-3-5_midjourney-22_kling_hq.png`.

## Generation workflow

1. Read `midjourney-dna-archive.json` and confirm the numbered Midjourney item's `highResImageSrc` before generating.
2. Read `brand-mockup-assets.json` and confirm the target raw mockup collection and existing child examples.
3. For each raw mockup item, create a rough direction image only as a placement guide. Keep this fast; do not run slow pixel-by-pixel loops for large 2496×1664 images when PIL vector/composite operations are enough.
4. Run Kling `image_to_image` with:
   - rough direction image,
   - exact original mockup image,
   - Midjourney high-res motif image,
   - plus an accepted structure reference when a seam/depth rule matters.
5. Update `brand-mockup-assets.json` with dimensions, hash, source motif, raw mockup source, and application mode.
6. Make a contact sheet and inspect before publishing.

## Multi-surface seam/crop rule

When a mockup has multiple adjacent surfaces, books, boards, cards, or panels, avoid a single panoramic graphic flowing across all surfaces unless Chris explicitly asks for that. Chris prefers physical separation to remain legible.

For book/board sets like `A-*-5`:
- Preserve the physical step/depth and visible vertical seam from accepted references such as `A-1-5`.
- Apply different motif crops to each surface.
- For stripe/band motifs, intentionally avoid horizontal band alignment across the seam. Offset band height, color order, or crop position so each board reads as separately printed.
- If a local patch still looks like a pasted panel or continuous surface, regenerate with Kling from the original mockup + accepted seam reference instead of continuing local patches.

## Apparel-specific motif scale corrections

Use these when Chris says a hat/shirt/apparel mockup feels too busy, too stripe-heavy, or too small-scale after a batch generation.

- For bucket hats or curved textile surfaces, a direct motif crop often over-emphasizes narrow central stripes. Regenerate with Kling using a rough direction image that shows **broad color fields** on the crown/brim and only sparse edge stripes. Prompt explicitly: no barcode-like central stripe curtain, no many narrow vertical stripes, front-center should be large coral/cream/black/gray areas, stripes only as side/edge accents.
- Do not ship a local/PIL patch that creates a flat rectangular patch on curved fabric. If local balancing introduces a visible box or pasted-panel edge, discard it and revert to the best natural Kling result even if it is not perfect. Natural material integration beats a more literal but visibly patched correction.
- For T-shirts, if the pattern looks too dense, regenerate from the original mockup with a direction image containing **fewer, larger modular blocks** over torso and sleeves. Prompt for broader rectangular modules, less dense checker/grid, and textile print following collar, sleeve, torso folds, wrinkles, and shadows.
- Generate at least two candidates for apparel-scale corrections and inspect a contact sheet. Prefer the candidate that preserves garment geometry/collar/sleeves and fabric shadows, even if another candidate pushes the pattern rule slightly harder.

## Item-level correction lessons after a published versioned batch

When Chris approves most of a generated batch but asks to regenerate only one or two numbered items, do **not** rerun or overwrite the whole set. Keep the existing child collection and replace only the selected manifest items with cache-busting `revNN` filenames, then build/push/live-verify those exact paths.

- For board-set items that Chris says look under-composited or “덜 합성된 것 같아,” generate new candidates with a stronger rough direction image: visibly fill every main surface with the source motif, preserve physical seams/steps, and explicitly forbid blank/white under-applied surfaces. Use accepted seam references for A-*-5 style two-board compositions and choose the candidate where the motif identity is obvious without becoming one continuous panorama.
- For tote/fabric items that Chris says feel dirty, stained, dusty, or worn, regenerate with clean-textile language and explicit negatives: no dirt, stains, grime, dusty speckles, aged cloth, muddy patches, or blotchy mask. Prefer a clean natural textile print that preserves highlights, folds, handles, and shadows over a more literal crop that makes the fabric look soiled.
- For these partial corrections, create at least two candidates per problematic item, inspect a contact sheet, select the best candidate, then copy it to a final non-candidate rev filename before updating the manifest. Candidate files may remain unreferenced; the manifest should point only to the chosen final rev asset.

## Reordering, renumbering, and replacing visible child sets

When Chris asks to change the order of A/B child sets or “rename the numbering,” treat it as a public manifest operation first, not a file-system rename.

- Preserve existing asset filenames and directories for cache/history stability; update visible `title`, item `title`, `description`, `displayOrder`, and `renumberedAt` in `brand-mockup-assets.json`.
- If Chris asks for order like `B1, B3, B4, B2`, rebuild only the relevant lane block in manifest order, then renumber visible titles to `B-1`, `B-2`, `B-3`, `B-4` while keeping each set's `sourceGraphic` and image paths intact.
- If Chris asks to move one set into another visible number and replace its old slot with a newly generated source (e.g. “A-2를 A-5로, 기존 A-5 삭제, 원래 A-2 자리에 Midjourney 13”), generate the new visible slot under a new internal set id if needed, remove the deleted set from manifest, and renumber the moved set in manifest. Do not delete old image binaries unless Chris explicitly asks; removing from manifest is the product-visible deletion.
- After reordering/replacement, verify the live manifest order and item titles, not just build output. Use Playwright/fetch to assert the lane order and at least one representative image probe.

## QA and false-negative handling

- Always verify:
  - JSON syntax,
  - local build,
  - live manifest contains the new child collection(s) or updated visible order,
  - every newly generated live asset URL returns `200 image/png`,
  - at least one modal/image probe loads at the expected natural size.
- GitHub Pages may take several minutes to update. Poll the live manifest before declaring failure.
- Playwright checks against lazy-loaded list thumbnails may show `naturalWidth: 0` even when assets are live and valid. Treat this as a possible timing false negative, not a product error, if:
  - direct asset URLs return `200 image/png`, and
  - modal image probe loads the same file at expected dimensions.
- Explain these false negatives calmly to Chris and continue verification rather than saying the webapp is broken.

## User-facing communication

- If Chris asks “무슨 에러야?” after an interrupted/failed QA tool, distinguish clearly between:
  - real deployment/image errors,
  - validation-script timing false negatives,
  - and GitHub Pages deployment lag/stuck runs.
- Keep the answer concise, then continue the concrete fix/update. Avoid overexplaining internal scripts unless it changes Chris's decision.

## 2026-10-08 A/B versioned mockup session notes

- Chris explicitly approved the multi-surface board/book rule: when a book/board mockup has two visible surfaces, do not let one graphic flow continuously across them. Use accepted examples such as `Outdoor Mockup A-1-5` as structure references, preserve the physical step/seam, and use clearly distinct motif crops. For stripe/band assets, intentionally offset band height/color/crop across the seam.
- For apparel fixes, prioritize natural Kling regeneration over local correction. If a hat has barcode-like central stripes, create a rough direction with broad color fields and sparse edge accents; if a T-shirt is too busy, regenerate with fewer/larger modules. Inspect candidates and prefer natural fabric/collar/sleeve geometry over a literal but patched correction.
- Do not ship local/PIL patches that create visible rectangular panels on curved fabric. In the B-2-4 hat case, a local balance patch reduced stripes but produced a boxy surface; the correct outcome was to discard the patch and publish the best natural Kling result.
- For large versioned batches (`A-4`, `B-4`), 12 images may finish after long silent Kling polling. Always inspect the process log before assuming failure. If Pages deployment stays `in_progress` and live manifest remains stale, query GitHub Actions and trigger a new commit only after confirming the stuck run; the newer run should cancel the old one when concurrency is configured correctly.
- Live QA priority: contact sheet visual inspection → JSON/build → live manifest includes the new child collections → every direct asset URL returns `200 image/png` → modal probe loads at `2496×1664`. Lazy grid thumbnail probes or modal-close failures in Playwright are test-script issues when direct assets and modal probes succeed.
- When Chris asks to reorder versioned mockup sets and “renumber” them (e.g. `B1 B3 B4 B2` → visible `B-1/B-2/B-3/B-4`), treat it as a manifest/display-order operation unless he explicitly asks to rename files. Keep asset filenames and stable IDs/paths where possible to avoid cache churn and broken references; reorder the `examples[]` entries, update visible `title`, item titles, short descriptions, optional `displayOrder`/`renumberedAt`, then JSON-validate, build, push, and verify live manifest order with sourceGraphic mapping. Explain the mapping back in human terms, e.g. “old B-3 is now visible B-2.”
- If GitHub Pages deploy stays `in_progress` but the live manifest has already updated, distinguish run-state lag from product failure. Verify live data/UI first; only retrigger with an empty commit when the manifest remains stale after repeated checks and the latest run is clearly stuck. After retrigger, confirm the older run is cancelled and the live manifest order/content is correct.
