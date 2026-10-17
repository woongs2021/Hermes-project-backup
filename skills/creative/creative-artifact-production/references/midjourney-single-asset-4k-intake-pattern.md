# Midjourney single-asset 4K intake pattern

Use when Chris sends one manual Midjourney image and asks to add it to **Design DNA → DNA Dashboard → Midjourney** with a 4K detail view.

## Pattern

1. Treat it as a manual Midjourney rail item, not Chris Archive or GPT Image 2.5.
2. Read `public/data/midjourney-dna-archive.json` and append the next visible sequence number; do not overwrite or renumber existing entries.
3. Store the original in both places:
   - local archive: `/opt/data/dna-archive/midjourney/YYYY-MM-DD/images/NN_slug_manual_midjourney.<ext>`
   - webapp public asset: `public/assets/dna-archive/midjourney/YYYY-MM-DD/NN_slug_manual_midjourney.<ext>`
4. Generate the 4K detail asset immediately with Kling `image_to_image` using `kling-image-v3_0_omni`, `--img_resolution 4k`, `--aspect_ratio auto`, and an exact-preservation prompt.
5. Parse Kling's structured JSON result and download `urlWithoutWatermark` / `url_without_watermark` / `url`; never scrape the first URL from mixed CLI logs.
6. Verify the downloaded high-res file by reading PNG/JPEG headers. Expected detail asset: `4096×4096 PNG`.
7. Add public-safe manifest fields: `imageSrc`, `originalImageSrc`, `highResImageSrc`, `highResWidth`, `highResHeight`, `highResAssetHash`, `highResSourceTool`, `highResRemasteredAt`, plus image-specific `analysis`, `midjourneyPrompt`, and `dnaClusters`.
8. Keep provider logs out of `public/assets`; store logs only in local archive/work locations if needed.
9. Run `npm run build:public`, then local browser QA and live Pages QA.

## QA checklist

- Manifest count increased by exactly 1.
- New title appears as the last Midjourney tile on desktop/tablet/mobile.
- Detail modal image `naturalWidth/naturalHeight` is `4096×4096`.
- `4K 고화질 PNG 다운로드` points to `/assets/dna-archive/midjourney-4k/...`.
- New original and high-res asset URLs return `200` with `image/*`.
- `overflowX` is 0 and console errors are empty.

## Copy guidance

For `analysis`, describe the visible image itself: composition, color, material/texture, mood, and how it can be used for brand/package/UI surfaces. Do not mention that it was just saved, replaced, requested, or generated in this workflow.
