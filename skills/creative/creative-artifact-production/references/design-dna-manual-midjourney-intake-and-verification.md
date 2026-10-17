# Design DNA manual Midjourney intake and verification

Use when Chris sends manual Midjourney outputs/images and asks to add them to the webapp or Midjourney rail.

## Product placement

- Manual Midjourney uploads belong in **Design DNA → DNA Dashboard → Midjourney**.
- GoYJ/GPT Image 2.5 selected assets belong in **Design DNA → DNA Dashboard → GPT Image 2.5**.
- Do not put manual Midjourney images in Chris Archive or the GPT rail.

## Durable storage pattern

1. Read `public/data/midjourney-dna-archive.json` and determine the current highest visible sequence number.
2. Add new manual images as the next contiguous sequence numbers, e.g. if the rail ends at 20, save the next three as 21–23.
3. Copy each original image into both:
   - Local canonical archive: `/opt/data/dna-archive/midjourney/YYYY-MM-DD/images/NN_slug_manual_midjourney.<ext>`
   - Webapp public assets: `public/assets/dna-archive/midjourney/YYYY-MM-DD/NN_slug_manual_midjourney.<ext>`
4. Update `public/data/midjourney-dna-archive.json` with public-safe fields only:
   - `id`, `title`, `created`, `status: midjourney_manual_saved`, `sourceTool: Midjourney`
   - `imageSrc`, `prompt`, `midjourneyPrompt`, `analysis`, `sourceRun`, `assetHash`, `width`, `height`, `localArchivePath`, `dnaClusters`
5. Also write/update the local day manifest at `/opt/data/dna-archive/midjourney/YYYY-MM-DD/midjourney-manual-manifest.json`.

## Naming and analysis pattern

- Use concise descriptive titles that preserve the sequence: `Midjourney NN — <Visual System Name>`.
- For manual image-only uploads, create a copy-ready `midjourneyPrompt` that describes the visible image and keeps the Design DNA negative tail:
  `--ar 1:1 --style raw --s 120 --no text, letters, numbers, logo, watermark, poster, app icon, UI screenshot, product mockup, people, photo, robot, brain, neon AI gradient`.
- Write a short Korean analysis that states what is visible, why it is useful as a brand/package/UI surface, and which DNA clusters it supports.
- Never include raw chat IDs, provider account details, private prompt logs, tokens, or credentials.

## Verification

Run the actual webapp loop before reporting completion:

1. `npm run build:public` from the webapp project.
2. Fetch local or live `data/midjourney-dna-archive.json` and assert:
   - item count increased as expected,
   - the new titles are present,
   - every new `imageSrc` returns HTTP 200 and `image/*`.
3. Browser-check Design DNA → DNA Dashboard → Midjourney:
   - tile count equals manifest count,
   - the new titles are visible on desktop/tablet/mobile,
   - no horizontal overflow,
   - at least one new tile opens a detail modal with loaded image and Midjourney prompt block.
   - if high-res fields are present, the modal image loads from `highResImageSrc`, natural size is `4096×4096`, and the `4K 고화질 PNG 다운로드` link points to the high-res asset.
4. After pushing, poll GitHub Pages until the live manifest count and new image assets are served, then repeat the browser smoke on the live URL.

## Visible numbering and user corrections

- The rendered rail may sort manifest items (for example by `created` then `title`) before assigning visible tile numbers. When Chris refers to “18번”, “last item”, or another visible number, map against the **rendered sorted grid**, not raw manifest array index or append order.
- To restore or edit a numbered item, first derive the visible order exactly as the app does, then identify the title/path(s). For Midjourney items, remember a visible item may have both `imageSrc` and `highResImageSrc`; restore/update both when the detail view uses 4K.
- If a wrong item was changed due to manifest-vs-visible numbering, correct it immediately: put the wrongly changed item back to its intended state, then apply the user’s requested change to the visible item.

## Detail-view analysis copy

- Chris prefers detail-view descriptions to describe the image itself, not the intake history. Avoid copy such as “저장했습니다”, “교체 요청”, “몇 번째 결과”, “Chris가 평가”, or workflow provenance inside `analysis`.
- Good `analysis` content: visible composition, color, material/texture, mood, and how the surface can be used for brand/package/UI assets.
- Keep provenance in manifest fields like `sourceRun`, `sourceTool`, hashes, and local logs—not in user-facing detail copy.

## Pitfalls

- Do not assume a `What do you see in this image?` caption means the user only wants description if the surrounding instruction asks to add the images to Midjourney assets. Treat the images as the requested asset batch and add a concise visual description to the manifest.
- Do not overwrite or renumber existing Midjourney items. Append in sequence.
- Do not rely on all offscreen lazy thumbnails having `complete === true` in Playwright. For offscreen images, verify image URLs directly and use a representative modal natural-size check.
- If a local selected manifest and public manifest use different IDs, compare by `(created, filename)` or public `imageSrc` filename before declaring an asset missing.
- Do not commit generator logs or provider output logs under `public/assets`; keep public assets to images/manifests and store logs in local work/archive locations if needed.
