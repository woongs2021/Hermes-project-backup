# Mockup high-res normalization workflow

Use when DNA Brand Asset / Midjourney + Mockup high-resolution outputs should match an already-approved low-resolution mockup exactly.

## Trigger

- Chris says low-res and high-res versions differ in composition, synthesis direction, crop, product geometry, pattern direction, cup/lid shape, package angle, or visual placement.
- A generative re-synthesis looks sharper but changes the approved mockup scene.

## Preferred fix

1. Treat the approved low-resolution mockup as the visual source of truth.
2. Keep the low-resolution file path in `originalImageSrc` for list/grid tiles.
3. Create the detail/download PNG from `originalImageSrc` via geometry-preserving upscale/sharpening, not generative re-composition.
4. Overwrite or replace the high-res `imageSrc`/`downloadSrc` PNG with the geometry-preserving version.
5. Update manifest fields:
   - `imageSrc`: high-resolution PNG path
   - `originalImageSrc`: approved low-resolution JPG path
   - `downloadSrc`: high-resolution PNG path
   - `downloadLabel`: `목업 완성본 PNG 다운로드`
   - `width` / `height`
   - `assetHash`
   - `fixNote`: mention geometry-preserving upscale from original mockup
6. UI binding:
   - grid/list tile: `item.originalImageSrc ?? item.imageSrc`
   - modal/detail image: `item.imageSrc`
   - download button: `item.downloadSrc`

## Verification checklist

- Manifest count unchanged.
- Every target item has both `originalImageSrc` and high-res `imageSrc`/`downloadSrc`.
- List/grid image `src` points to the low-res/original path and does not include the high-res folder segment.
- Detail modal natural size matches the high-resolution PNG.
- Download button href matches `downloadSrc`.
- Desktop/mobile: no console/page errors and no horizontal overflow.

## Pitfall

Do not assume “higher quality” means “better” if composition changes. For approved brand mockups, visual continuity wins: high-res detail must be the same composition as the list thumbnail, only clearer.
