# DNA Brand Asset outdoor mockup sequence and live QA lessons

Use when Chris asks to reorganize Outdoor Mockup examples, add a new A/B/C sequence, or synthesize a new Midjourney motif across an existing outdoor mockup set.

## Naming / hierarchy pattern

- Keep the top Midjourney + Mockup source tabs as broad lanes, e.g. `Outdoor Mockup A`, `Outdoor Mockup B`.
- Put versions/examples underneath that lane as collection titles, e.g. `Outdoor Mockup A-1`, `Outdoor Mockup A-2`, `Outdoor Mockup B-1`.
- Preserve stable internal `tabId` values where possible (`outdoor-mockup-1`, `outdoor-mockup-2`) and change only visible labels unless Chris explicitly asks for data/schema IDs to change. This reduces React state and manifest compatibility risk.
- For a new `A-2` set, append a new `examples[]` entry with the same `tabId` as A and insert it directly after `A-1` in the manifest so the UI stack order matches the visible naming.
- Rename item titles consistently: `Outdoor Mockup A-2-1` through `Outdoor Mockup A-2-6`. Avoid leaving older visible strings like `Outdoor Mockup Example 1-1` once Chris asks for A/B naming.

## New motif × outdoor mockup synthesis pattern

1. Identify the source Midjourney item from `public/data/midjourney-dna-archive.json`; prefer its `highResImageSrc` when present.
2. Identify the target mockup collection from `public/data/brand-mockup-assets.json` under `collections[]`.
3. Generate one new revision filename per output under `public/assets/dna-brand-assets/midjourney-mockup/<example-id>/YYYY-MM-DD/`.
4. For full-surface outdoor synthesis, use the proven reference ordering for Kling image-to-image:
   - image 1: rough placement/direction composite only
   - image 2: exact original mockup geometry/camera/light/material
   - image 3: source Midjourney motif/high-res graphic
5. Prompt for full-surface physical print/fused material, preserving original camera, outdoor light, shadows, folds, paper/fabric texture, foreground objects, perspective, and aspect ratio.
6. Explicitly forbid text, letters, numbers, logos, watermarks, extra objects, fake annotations, dirty mask edges, holes, transparent fabric, wall texture bleeding through fabric, weird glow, pasted rectangles, and broken geometry.
7. Store local archive and public copies, update `assetHash`, dimensions, `downloadSrc`, `sourceGraphicHighResImageSrc`, `resynthesisSourceImageSrc`, `mockupCollectionId`, and `applicationMode`.

## Contact-sheet visual QA

- Create a quick 2×3 contact sheet before deploy.
- Check: full-surface application, physical integration, no pseudo text/logo, no transparent fabric, no foreground damage, no obvious mask edge, no broken perspective.
- If one image is weak, revise only that item with a new filename; do not regenerate the entire set unless the motif direction itself is wrong.

## Live verification pitfall

GitHub Pages + lazy-loaded images may report `naturalWidth: 0` in DOM immediately after scrolling even when the URL is valid and the image later displays. Do not treat that alone as failure.

Verification should include:

- Fetch live manifest with a cache buster and confirm the new `examples[]` entry, title, and item count.
- Fetch at least one new image URL and confirm `200 image/*`.
- In Playwright, verify visible tab labels and headers (`Outdoor Mockup A`, `Outdoor Mockup A-1`, `Outdoor Mockup A-2`, etc.).
- For lazy image dimensions, use an in-page `new Image()` probe against each `src` and wait for `onload`/`naturalWidth`, instead of relying only on the already-mounted lazy `<img>` DOM node.
- Open a detail modal and verify the modal image source and natural dimensions.
- Check no horizontal overflow and no console errors.

## Reporting to Chris

Keep the completion note concise: what changed, where it lives, and what was actually verified. Mention the cache-busting deploy URL/commit when useful. Do not include raw generation logs or provider internals.
