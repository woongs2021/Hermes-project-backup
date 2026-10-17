# Design DNA Dashboard Source Rails + Manual Midjourney Intake

Use when Chris asks to split or maintain the Design DNA Dashboard by generation source, or asks to save/replace “미드저니 N번” assets from Telegram images.

## Dashboard rail model

- Keep **GPT Image 2.5** and **Midjourney** as separate rails inside Design DNA → DNA Dashboard.
- GPT Image 2.5 rail is owned by the GoYJ scheduled loop and continues to receive Chris-approved loop outputs.
- Midjourney rail is for Chris’s manual Midjourney outputs only; do not let the GoYJ automated loop write into this rail.
- Preserve counts independently in UI copy, e.g. `16 GPT · 7 Midjourney`.

## Data files

- GPT rail uses `public/data/dna-archive.json` and assets under `public/assets/dna-archive/<date>/...`.
- Midjourney rail uses `public/data/midjourney-dna-archive.json` and assets under `public/assets/dna-archive/midjourney/<date>/...`.
- Midjourney items should still use the same `DnaArchiveItem` shape, including:
  - `sourceTool: "Midjourney"`
  - `prompt` and `midjourneyPrompt` as copy-ready prompt text
  - `analysis`
  - `assetHash`
  - `dnaClusters`

## Manual Midjourney save/replace workflow

1. Determine intent from Chris’s wording:
   - “다음번 순서로 저장해줘” → append next Midjourney item number.
   - “N번으로 저장해줘” → append that numbered item if it does not exist, or intentionally create that numbered item if Chris is sequencing manually.
   - “N번을 이걸로 교체해줘” → overwrite the existing asset file for N and update manifest hash/analysis/sourceRun; keep the same id/title/number.
   - “취소… 원형만 저장해줘” with multiple images → save only the corrected target image; ignore accidental/unrelated images.
2. Use stable filenames such as `07_warm_earth_oval_surface_midjourney_translation.jpg` and stable ids such as `2026-09-26-midjourney-07-warm-earth-oval-surface-translation`.
3. Choose the prompt/title from the corresponding Design DNA prompt family when obvious; otherwise write a concise material-style title and prompt based on the visual.
4. For every Chris-approved Midjourney save/replace triggered by “저장해줘”, automatically create and attach a Kling 4K remaster before final verification:
   - Use the original saved Midjourney image as the reference, preserving it as `originalImageSrc`.
   - Run `python3 scripts/remaster_midjourney_4k.py --missing` after appending new Midjourney items, or `python3 scripts/remaster_midjourney_4k.py --numbers N --force` when replacing/remastering a specific numbered item.
   - The script must use `kling-image-v3_0_omni`, `img_resolution=4k`, `aspect_ratio=auto`, and must extract the structured generated `urlWithoutWatermark` / `url_without_watermark` result — never the CLI upload/reference URL.
   - Require the downloaded PNG to be true 4K (`max(width,height) >= 4096`) before writing `highResImageSrc`, `highResWidth`, `highResHeight`, `highResDownloadLabel`, `highResAssetHash`, `highResSourceTool`, and `highResRemasteredAt`.
   - Store remasters under `public/assets/dna-archive/midjourney-4k/<date>/...` and ensure detail view shows the 4K image plus a `4K 고화질 PNG 다운로드` button.
5. Build and browser-verify:
   - GPT rail count unchanged except intentional GPT deletes.
   - Midjourney rail count matches manifest.
   - all Midjourney original and 4K images load with nonzero natural dimensions.
   - newly saved Midjourney detail view loads a 4K image and exposes the `4K 고화질 PNG 다운로드` button.
   - no horizontal overflow.
6. Commit and push the manifest plus original/4K asset changes, then verify the live Pages manifest, original image URL, 4K image URL, and detail-view download button.

## Deleting GPT rail items

- If Chris says a GPT Image 2.5 item is too complex and asks to delete a numbered item, remove both the manifest entry and its public asset file.
- Verify the GPT count decreases and the Midjourney count is unchanged.

## Midjourney 4K and mockup resynthesis details

- When downloading Kling image-to-image results, parse the structured completed work fields (`urlWithoutWatermark`, `url_without_watermark`, then `url`) from the JSON response. Do **not** scrape the first URL in CLI logs, because upload/reference URLs may appear before the generated 4K result and can silently save the original low-resolution input.
- Validate generated files by reading image dimensions before manifest updates. For Midjourney DNA rail 4K remasters, require true 4K (`max(width,height) >= 4096`). For 3:2 mockup resynthesis outputs, expect large PNGs such as `4992×3328` and require at least `max(width,height) >= 3000`.
- Store Midjourney remasters under `public/assets/dna-archive/midjourney-4k/<date>/...` and preserve `originalImageSrc` on the manifest item.
- Store Midjourney + Mockup high-resolution outputs under `public/assets/dna-brand-assets/midjourney-mockup-4k/<collection>/<date>/...`; update each mockup item with `originalImageSrc`, `downloadSrc`, `downloadLabel`, `width`, `height`, `assetHash`, and source graphic metadata.
- Pitfall: generative re-synthesis can change the approved mockup's crop, product geometry, cup/lid shape, packaging angle, or pattern direction. If Chris asks for the high-resolution version to match the low-resolution/list image, do **not** use a generative re-composition as the final source. Use the approved `originalImageSrc` as the geometry source and create a geometry-preserving upscale/sharpened PNG so low-res list and high-res detail differ only in resolution/clarity.
- For Brand Asset lists, keep heavy PNGs out of the list view: render `item.originalImageSrc ?? item.imageSrc` in grid/list tiles, and reserve `item.imageSrc` / `downloadSrc` high-resolution PNGs for the modal detail view and download button.
- Detail views should use the high-resolution asset for the modal image and expose a download button:
  - DNA Dashboard: `4K 고화질 PNG 다운로드`
  - DNA Brand Asset Midjourney + Mockup: `목업 완성본 PNG 다운로드`
- For heavy asset batches, verify both data and UI: manifest count/fields, sample asset URLs and dimensions, list image `src` stays low-res, desktop/mobile modal natural size uses high-res, download button href, console/page errors, and horizontal overflow.
- See `references/mockup-highres-normalization.md` for the session-derived normalization workflow when low-res and high-res mockup compositions diverge.
- Pitfall: generative mockup resynthesis can change crop, object scale, or lid/rim geometry on tight close-up assets. If Chris flags a specific mockup as weird, compare against `originalImageSrc`; for geometry-sensitive close-ups, prefer a geometry-preserving upscale/sharpen of the original crop over another free generative resynthesis. Keep the high-resolution download path but do not let the model zoom out or reinterpret the object.
- For heavy asset batches, verify both data and UI: manifest count/fields, sample asset URLs and dimensions, desktop/mobile modal natural size, download button href, list tile `src` stays on the lightweight original when intended, console/page errors, and horizontal overflow.

## Communication preference

- For repetitive manual saves, keep the reply concise: saved name, rail count, verification, live URL, commit link.
- Do not re-explain the whole architecture every time once the rails are established.
