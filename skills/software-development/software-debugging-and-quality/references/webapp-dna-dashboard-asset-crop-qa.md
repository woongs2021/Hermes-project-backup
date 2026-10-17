# Webapp DNA Dashboard Asset Crop QA

Use this when Chris reports that Design DNA / DNA Dashboard thumbnails or detail images still show an unwanted light/ivory edge even after CSS `object-fit`, rounded clipping, or border changes.

## Durable lesson

If the visible edge is part of the raster image itself, CSS frame fixes will not remove it. Confirm whether the problem is:

1. **Layout/frame issue**: image rect does not match media frame, border reduces content box, or object-fit leaves inset.
2. **Raster-content issue**: image rect equals frame but the pixels inside the image include a light outer matte/border.

For raster-content issues, Chris may prefer destructive crop of the public asset itself over display-only scale hacks.

## Recommended sequence

1. Verify the relevant manifest(s) and asset paths.
   - Typical files: `public/data/dna-archive.json`, `public/data/midjourney-dna-archive.json`.
   - Include both `imageSrc` and `highResImageSrc` when the detail modal uses 4K assets.
2. Back up originals outside the published public tree before destructive edits.
   - Example pattern: `/opt/data/backups/hermes-webapp-dna-crop-YYYY-MM-DD/` preserving relative paths.
3. Crop inward by a small ratio and resize back to the original dimensions.
   - Session-proven ratio: 4% per side for square DNA assets.
   - Preserve the original dimensions so existing layouts and manifest width assumptions remain stable.
   - Use Pillow if available: crop `(w*0.04, h*0.04, w-w*0.04, h-h*0.04)` then resize to `(w, h)` with LANCZOS.
4. Update manifest hashes after modifying files.
   - `assetHash` for `imageSrc`.
   - `highResAssetHash` for `highResImageSrc`.
5. Remove temporary display-level crop rules such as `transform: scale(...)` to avoid double cropping.
6. Fix detail-modal layout separately if it is visually off.
   - CSS grid children can stretch to the height of the long text column.
   - Add `align-items: start` to the modal grid so the image panel stays image-sized while the copy panel can be longer.
7. Verify in browser, not only source text:
   - thumbnail frame and image rect match (`inset` 0)
   - `transform: none` after destructive crop
   - modal image natural dimensions load
   - `overflowX` is 0
   - console errors are absent
   - live manifest asset URLs return `200` and `image/*`
8. Poll hosted hashed assets before claiming live deployment.

## Pitfalls

- A border or inset stroke can make the image appear not to fill the frame because CSS border consumes content box space. Prefer overlay/inset shadows for visual strokes when the asset should fill exactly.
- `object-fit: cover` does not remove unwanted pixels that are already inside a square image.
- Applying modal crop styles to a shared class can accidentally affect Brand Asset / mockup modals. Keep DNA Dashboard-specific rules isolated or remove them once the asset itself is cropped.
- Lazy thumbnails may report `naturalWidth: 0` in a quick probe. Scroll/wait for a representative thumbnail or separately fetch every manifest URL.
