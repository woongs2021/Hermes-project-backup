# Midjourney DNA Dashboard Kling 4K remaster workflow

Use when Chris asks to upscale/remaster saved Design DNA → DNA Dashboard → Midjourney rail assets while keeping the image itself intact and exposing downloadable high-resolution files in the webapp.

## Core lesson

Kling can produce true 4K image-to-image results for saved Midjourney assets, but the CLI output contains both uploaded source URLs and final result URLs. Do **not** scrape the first URL in the output. Parse the structured JSON and use the completed work result, preferably `urlWithoutWatermark` / `url_without_watermark`; otherwise you may accidentally download the uploaded 1024px source while thinking it is the 4K output.

## Recommended generation path

- Tool: Kling CLI `image_to_image`
- Model: `kling-image-v3_0_omni`
- Resolution: `--img_resolution 4k`
- Aspect ratio: `--aspect_ratio auto`
- Count: `--imageCount 1`
- Prompt shape:
  - Preserve exact composition, crop, colors, shapes, flat graphic style, texture, and design intent.
  - Do not redesign or reinterpret.
  - Only increase clarity, edge quality, texture fidelity, and print/mockup readiness.
  - Ban added text, logos, UI, objects, people, and decorative elements.

Example command shape:

```bash
HOME=/opt/data PATH="/opt/data/.npm-global/bin:$PATH" \
  kling image_to_image \
  --image /absolute/path/to/source.jpg \
  --model kling-image-v3_0_omni \
  --img_resolution 4k \
  --aspect_ratio auto \
  --imageCount 1 \
  --poll 900 \
  "Remaster image 1 into a true 4K high-resolution PNG while preserving the original image as closely as possible..."
```

## URL parsing pitfall

The raw output may include:

- uploaded source URL from `[kling] Uploaded -> ...`
- result `url`
- result `urlWithoutWatermark`
- result `url_without_watermark`

Always parse the leading JSON object before the `[kling]` log lines, then select:

```python
work = data["body"]["generations"][0]["result"]["works"][0]
url = work.get("urlWithoutWatermark") or work.get("url_without_watermark") or work.get("url")
```

Then download immediately because Kling result URLs can expire.

## Verification requirement

Before updating the webapp, verify every downloaded file by fully opening/loading the image and reading dimensions. For the Midjourney rail 4K pass, the correct result is usually `4096×4096 PNG`. Treat anything still `1024×1024` as a failed download/parsing mistake, not a successful 4K remaster.

Also treat a file that reports dimensions but fails `PIL.Image.open(...).load()` as corrupt/truncated. In that case, replace it with a new cache-busting filename rather than reusing the broken public path. If the priority is exact composition preservation and the AI remaster cropped or corrupted the image, a geometry-preserving local 4K upscale from the approved original is acceptable: resize the original to `4096×4096` with high-quality resampling, optionally apply a light sharpening pass, update `highResSourceTool` to say `Geometry-preserving local 4K upscale from original Midjourney source`, and verify the detail modal loads the new file.

Use PNG/JPEG header parsing if Pillow is unavailable in the active Python environment, but prefer a full decode/load check when investigating reports of cropped, broken, or truncated detail views.

## Webapp manifest pattern

For each `public/data/midjourney-dna-archive.json` item, keep the original source and add high-resolution fields. When adding a new manual Midjourney batch and Chris asks for detail view to be 4K, generate the 4K assets during intake rather than as a later pass, then add these fields before the first build/QA.

```json
{
  "originalImageSrc": "/assets/dna-archive/midjourney/YYYY-MM-DD/original.jpg",
  "highResImageSrc": "/assets/dna-archive/midjourney-4k/YYYY-MM-DD/item_kling4k.png",
  "highResDownloadLabel": "Kling 4K remaster PNG",
  "highResWidth": 4096,
  "highResHeight": 4096,
  "highResAssetHash": "sha256...",
  "highResSourceTool": "Kling image_to_image / kling-image-v3_0_omni",
  "highResRemasteredAt": "YYYY-MM-DDTHH:mm:ss+09:00"
}
```

For the UI detail view:

- Show `highResImageSrc ?? imageSrc` in the modal image so the detail preview uses the 4K asset when available.
- Add a visible link/button labeled `4K 고화질 PNG 다운로드` pointing to `highResImageSrc` with a `.png` download filename.
- Keep the rail count unchanged; this is a quality-layer update, not a new asset intake.

## Deployment/QA checklist

1. Generate and download all 4K PNG files into both local archive and webapp public assets.
2. Update the Midjourney manifest with high-res fields for every item.
3. Build with `npm run build:public`.
4. Verify local manifest has all `highResImageSrc` fields and each high-res URL is `200 / PNG / 4096×4096`.
5. Browser-test desktop and mobile:
   - Design DNA → DNA Dashboard → Midjourney rail count is unchanged.
   - Detail modal image natural size is 4096×4096 for a sample item.
   - `4K 고화질 PNG 다운로드` button is visible and points to `/assets/dna-archive/midjourney-4k/...`.
   - No horizontal overflow.
6. Commit only relevant manifest, assets, and UI/type changes; avoid staging unrelated public manifest churn.
7. After push, repeat live manifest and live detail-modal verification on GitHub Pages.

## User preference captured

Chris wants high-resolution remastering to preserve the image itself. Prefer exact-preservation remaster prompts and dimension verification over creative re-generation claims.