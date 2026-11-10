# Midjourney batch asset 4K intake pattern

Use when Chris sends multiple manual Midjourney images in one Telegram burst and asks to add them to **Design DNA → DNA Dashboard → Midjourney**, especially when he asks for 4K detail views.

## Core pattern

1. Treat all attached images in the burst as one batch, even if Telegram captions such as “What do you see in this image?” appear on individual images. The active instruction is the surrounding request to add them as Midjourney assets.
2. Read `public/data/midjourney-dna-archive.json` and append the next contiguous visible sequence numbers. Do not overwrite, renumber, or reorder existing Midjourney entries.
3. Store each 1024/source image in both locations:
   - local canonical archive: `/opt/data/dna-archive/midjourney/YYYY-MM-DD/images/NN_slug_manual_midjourney.jpg`
   - webapp asset: `public/assets/dna-archive/midjourney/YYYY-MM-DD/NN_slug_manual_midjourney.jpg`
4. **Discover actual high-resolution capability before submitting any paid generation.** Run `kling who_am_i --quiet` (or the provider’s equivalent) and use only a model/resolution combination explicitly declared for the current account. Do not assume `kling-image-v3_0_omni` accepts 4K: account entitlements can expose only 1K/2K. If a real 4K-preservation path is available and the batch scope includes high-resolution detail/downloads, generate one exact-preservation asset per image and store it under:
   - local: `/opt/data/dna-archive/midjourney-4k/YYYY-MM-DD/images/NN_NN_slug_manual_midjourney_kling4k.png`
   - public: `public/assets/dna-archive/midjourney-4k/YYYY-MM-DD/NN_NN_slug_manual_midjourney_kling4k.png`
   If 4K is not explicitly available, publish the verified supplied originals only; do **not** create placeholder high-res fields, claim a 4K download, or silently spend credits on a different model. Record the capability boundary in the private work log and offer a separately approved remaster path when needed.
5. Parse structured generation JSON only when generation was actually performed; prefer `urlWithoutWatermark` / `url_without_watermark` / `url` from generation works. Do not save provider logs or uploaded-source URLs under `public/assets`.
6. For every new manifest item, always include source fields:
   - `imageSrc`, `originalImageSrc`, `width`, `height`, `assetHash`
   Add `highResImageSrc`, `highResWidth`, `highResHeight`, `highResAssetHash`, `highResSourceTool`, `highResRemasteredAt`, and `highResDownloadLabel` **only** after a real decoded high-res asset has been produced and verified.
7. Also include the modal-required DNA Dashboard fields for every Midjourney item, not only GPT items:
   - `dnaClusters` as a non-empty array
   - `prompt` (usually the same value as `midjourneyPrompt` for manual Midjourney items)
   - `sourceTool: "Midjourney"`
   - a modal-compatible `status`, e.g. `midjourney_manual_saved`
   Missing `dnaClusters` can break the shared detail modal when Chris clicks the asset, even if the manifest, thumbnail, and direct 4K URL are valid.
8. Write public-facing `analysis` about the visible material/composition/use, not the workflow. Keep provenance in `sourceRun`, hashes, and local manifests.
8. Optionally write/update a local day manifest at `/opt/data/dna-archive/midjourney/YYYY-MM-DD/midjourney-manual-manifest.json` for handoff continuity.

## Related follow-up workflow

- When a saved Midjourney asset is later used to replace an existing mockup rail slot or Chris points out unfilled mockup surfaces, use `references/midjourney-mockup-replacement-and-full-surface-revision.md`.

## Verification checklist

- Local manifest count increases by exactly the number of images in the batch.
- Each source file exists and is `1024×1024` or the provided source size; hash matches `assetHash`.
- When high-resolution fields are present, each high-res file exists as the declared size/format and its decoded dimensions and hash match the manifest. Never infer 4K from a filename.
- `npm run build:public` succeeds.
- Commit only the relevant manifest plus the new source and 4K assets. Avoid unrelated untracked candidate files.
- After pushing, wait for live Pages manifest to show the new IDs/count.
- Direct live URLs return:
  - originals: `200 image/jpeg` or `image/png`, expected source dimensions;
  - 4K assets: `200 image/png`, `4096×4096`.
- Browser/Playwright probe loads each new `highResImageSrc`, sees `4096×4096`, no console errors, no horizontal overflow.

## Prompt template for Kling 4K preservation

```text
Create an exact high-resolution preservation remaster of image 1. Preserve the same square composition, shapes, colors, material texture, paper grain, edges, proportions, and negative space. Do not add text, logo, icon, UI, objects, shadows, frames, people, or new elements. Keep it as a flat 2D abstract Midjourney graphic surface. Output clean 4K square PNG quality.
```

## Pitfalls

- Background processes can run under a different Python than the interactive terminal. If a batch helper uses PIL, call the intended venv explicitly (e.g. `/opt/hermes/.venv/bin/python script.py`) rather than relying on `python3` resolution.
- Git working trees often contain old untracked candidate images from mockup iterations. Always `git add` explicit paths only.
- A 4K detail field must be verified by actual image dimensions, not by filename or manifest alone.
