# Midjourney mockup replacement and full-surface revision pattern

Use when Chris asks to replace an existing mockup set with a different Midjourney source, or when he points out that a mockup surface is not fully filled.

## Trigger phrases

- “A-4를 미드저니 34번으로 교체해줘. 기존거는 삭제하고.”
- “A 4-1과 4-5가 아직 채워지지 않은 부분이 있는것 같아. 다시 합성해서 변경해줘.”
- Any request to swap a visible mockup rail slot to a new Midjourney number while preserving the same A/B position and removing the old visible entry.

## Replacement workflow

1. Inspect the current manifest and identify the visible mockup slot by display order, title, source graphic, internal ID, and item count.
2. Create a fresh internal example ID for the replacement set when replacing the source graphic, rather than mutating the old source identity in-place. Keep the visible title/order stable for Chris, e.g. visible `Outdoor Mockup A-4`, new internal `outdoor-mockup-example-a-11`.
3. Generate all items in the set against the new Midjourney source. Preserve original mockup geometry/camera/background, but treat every printable surface as needing source-material coverage.
4. Update the manifest so the old source is removed from the visible A/B list and the new source occupies the same display order. Do not leave the old example visible elsewhere unless Chris explicitly asks to archive it in a separate rail.
5. Build with `npm run build:public`, commit only the manifest and final asset files, push, then wait for GitHub Pages manifest to reflect the new IDs.
6. Verify direct live asset URLs and a browser/Playwright probe. Check dimensions, hashes, console errors, and horizontal overflow.

## Full-surface correction workflow

When Chris says a mockup is not filled enough, do not assume a generic regeneration will fix it. Use a targeted revision loop:

1. Compare current vs candidate in a contact sheet and inspect the exact unfilled areas Chris likely sees.
2. For simple cases, regenerate only the affected items, not the whole set.
3. If the model keeps preserving blank paper areas, create a rough local direction image that explicitly fills the missing printable surface with the source motif, then use it as a coverage reference for a naturalization pass.
4. If naturalization reintroduces blanks or creates a worse artifact, prefer a local corrective composite for the specific surface band over another broad regeneration. Preserve seams, steps, paper thickness, contact shadows, and physical separation lines manually if needed.
5. Reject candidates that fix one area while creating a bigger issue elsewhere, e.g. a small name-card turning blank white, broken geometry, logo-like marks, pseudo text, or strong sticker/patch edges.
6. Keep only final accepted rev assets under public assets. Remove uncommitted failed candidate files from the working tree before finishing.

## Preview-image performance rule

For every new or revised Midjourney + Mockup set, create lightweight preview assets for grid/list rendering while keeping full-resolution assets for detail/download.

- Add `previewImageSrc`, `previewWidth`, `previewHeight`, `previewAssetHash`, and `previewGeneratedAt` to each manifest item.
- Store previews under `public/assets/dna-brand-assets/midjourney-mockup-preview/<example-id>/<date>/` using WebP.
- Recommended preview size: longest side around `900px`, WebP quality around `72`; this keeps grid images visually acceptable but much faster to load.
- The React grid/list should render `previewImageSrc ?? imageSrc`; the detail modal and download links must continue to use full-resolution `imageSrc` / `downloadSrc`.
- Verification must include preview hash checks, build success, and a rendered-page probe confirming grid/list loads previews while detail/full asset remains available.

## QA criteria for printable-surface mockups

- No large blank white/cream printable faces unless the mockup intentionally has unprinted physical paper edges.
- Top stacks, lower bands, side faces, small cards, front overlap panels, and rear boards should all be considered candidate printable surfaces.
- A paper edge or thickness line may remain light/white, but it must read as thickness/depth, not as an unfilled surface.
- For board/booklet compositions, maintain visible seam/step/depth between separate pieces; do not flatten them into one panorama.
- Use different crops of the same Midjourney source per surface so the set feels physically plausible rather than a pasted single image.
- Verify visually with contact sheets before publishing, then verify technically with manifest hash/dimensions, build, live URLs, and browser probe.
- **Rendered grid verification is mandatory** when manifest items carry both `imageSrc` and `originalImageSrc`. Direct image URLs can pass while the UI still shows the original mockup if the React grid prefers `originalImageSrc`; inspect the actual rendered `<img src>`/network requests for the new example on the live page.
- If generated assets have provider marks/watermarks, do not publish until the contact sheet confirms they are gone. If using local cleanup, update manifest hashes after cleanup and re-run direct URL + rendered-page probes.

## Notes from the MJ34 Outdoor A-4 session

- A-4-1 originally left the upper card stack blank. A successful correction filled the top stack while preserving paper-layer depth.
- A-4-5 repeatedly reintroduced a lower white band. A broad naturalization pass made the small card worse by turning it white; the accepted fix used a narrower local correction for the lower band/card area.
- The durable lesson is the targeted loop: regenerate affected items only → make a rough filled direction if necessary → naturalize → reject worse artifacts → use local composite only for the specific remaining blank surface.

## Notes from the A-series item-5 booklet/card session

- The 5th Outdoor Mockup A composition (two rear boards/booklets plus a small front card) can repeatedly look under-filled even after generic regeneration. Treat this as a recurring class of issue, not a one-off asset flaw.
- When Chris says item `*-5` is not “꽉 차게” filled, inspect all visible printable surfaces: both rear boards/booklets, lower bands, front overlap panels, and the small front card. A light paper edge is acceptable only if it clearly reads as thickness/depth, not as an unprinted face.
- Use the best already-approved full-coverage sibling as a structural reference. In this session, `Outdoor Mockup A-3-5` was the successful reference for how booklets/cards should read: fully printed, physically separated, with seam/step/depth intact.
- For pale or cream-based source graphics, a technically full-bleed result may still read as blank. Prompt for **active graphic content in every surface crop**, especially the small card and lower bands, rather than merely asking for edge-to-edge coverage.
- If a first A-3-5-reference pass still looks too pale, run a stronger crop pass with language like: “crop and scale the source graphic so each visible surface contains active graphic content, not just pale background.”
- QA item-5 revisions in contact sheets comparing current vs new across affected A slots. Prefer replacing only the affected `*-5` assets and leaving the rest of the mockup set untouched.

## Notes from the Coffee Example 4 / rendered-thumbnail bug

- When adding generated mockup examples, verify the UI layer, not just manifest and direct asset URLs. In this session, generated Coffee Example 4 files existed and direct URLs passed, but the grid appeared as original mockups because the JSX used `originalImageSrc ?? imageSrc` for thumbnails.
- Correct pattern for generated mockup cards: list/grid thumbnails and detail views should display generated `imageSrc`; `originalImageSrc` is provenance/reference metadata, not the primary visual unless the lane is explicitly a raw mockup-asset moodboard.
- For ordering swaps (e.g. “Coffee Mockup 3 and 4 교체”), it is acceptable to swap visible titles/order while keeping large asset files and internal IDs stable, but the live manifest and rendered page must both confirm the requested visible order.