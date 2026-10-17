# Midjourney detail-view 4K integrity QA

Use when maintaining **Design DNA → DNA Dashboard → Midjourney** detail views, especially when Chris reports that a detail view does not open, a 4K image looks cropped, or the high-resolution version loads slowly/oddly.

## Failure modes observed

1. **Manifest schema mismatch breaks the shared modal**
   - Direct image URLs and thumbnails can be valid while clicking the card fails.
   - The shared DNA Dashboard modal expects modal-safe fields such as `dnaClusters`, `prompt`, `sourceTool`, and `status`.
   - If `dnaClusters` is missing, the modal can fail at render time when it calls `dnaClusters.map(...)`.

2. **A 4K file can report dimensions but still be corrupt/truncated**
   - A file may have enough header data to show `4096×4096` but fail during full decode/load.
   - Verify with a full image load, not only header or manifest dimensions.

3. **A technically correct 4K PNG can still be too heavy for comfortable modal loading**
   - Large 25–30MB PNG detail assets may decode slowly in browser probes and user sessions.
   - If the image is a flat graphic/material field and exact composition preservation matters more than lossless PNG, a high-quality 4K JPEG can be a better detail-view asset.

## Fix pattern

1. Inspect the affected item in `public/data/midjourney-dna-archive.json` and compare its schema against a working neighboring item.
2. Confirm both original and high-res files exist locally and on live Pages.
3. Open and fully decode the high-res file:
   - Python/Pillow: `Image.open(path); image.load(); image.size`
   - Browser: open the actual modal and wait for `img.complete && img.naturalWidth > 0`.
4. If the high-res asset is cropped/corrupt:
   - Prefer regenerating/remastering from the approved original when possible.
   - If AI remastering changes crop or corrupts the file, use a geometry-preserving local upscale from the original.
   - Write the replacement under a new cache-busting filename; do not reuse the broken public path.
5. Update manifest fields:
   - `highResImageSrc`
   - `highResWidth`
   - `highResHeight`
   - `highResAssetHash`
   - `highResSourceTool`
   - `highResRemasteredAt`
   - `highResDownloadLabel`
6. If the high-res file is JPEG, ensure the detail download UI uses the manifest label and a `.jpg` download filename rather than hardcoding `PNG`/`.png`.

## Required verification

- `python3 -m json.tool public/data/midjourney-dna-archive.json`
- `npm run build:public`
- Local browser path: `Corporate AX → Design DNA → DNA Dashboard → Midjourney → affected item`.
- The modal image uses the new `highResImageSrc` and reports expected natural dimensions.
- The download link points to the same new high-res file and uses the correct extension.
- Direct live URL returns `200 image/*`, fully decodes, dimensions match manifest, and hash matches.
- Live modal opens with no console/page errors and no horizontal overflow.

## User preference

Chris expects Midjourney detail/4K views to preserve the original composition. A high-res asset that is cropped, corrupt, or so heavy that it appears not to load is unacceptable even if the manifest says `4096×4096`.
