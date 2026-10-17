# Design DNA Dashboard Midjourney Prompt + Detail View Lessons

Use when Chris asks to expose GoYJ/DNA Dashboard assets as reusable prompts, add copyable prompt fields, refine the Design DNA webapp detail experience, or maintain separate GPT Image 2.5 vs Midjourney asset rails.

## Manifest/data pattern

### GPT Image 2.5 rail
## Manifest/data pattern

- For every saved GPT Image 2.5 DNA Dashboard item, include `midjourneyPrompt` in `public/data/dna-archive.json`.
- Keep `prompt` as the original generation prompt; do not overwrite it. Add `midjourneyPrompt` as a separate, copy-ready field.
- Split source rails when Chris wants GPT and Midjourney separated:
  - GPT Image 2.5 loop assets stay in `public/data/dna-archive.json` and continue to be populated by the GoYJ loop.
  - Chris's manual Midjourney uploads go in `public/data/midjourney-dna-archive.json` with assets under `public/assets/dna-archive/midjourney/YYYY-MM-DD/`.
  - The webapp should expose source tabs under Design DNA → DNA Dashboard: `GPT Image 2.5` and `Midjourney`.
  - Do not let the GoYJ scheduled loop write into the Midjourney rail; it is manual-upload only unless Chris explicitly changes the workflow.
- Prompt shape Chris accepted:
  - one English motif-description line
  - `--ar 1:1 --style raw --s 120`
  - strict negative tail such as `--no text, letters, numbers, logo, watermark, poster, app icon, UI screenshot, product mockup, people, photo, robot, brain, neon AI gradient`
- For line-only motifs, add negative terms for `filled shapes`, `dots`, `dashed lines`, `light trail`, etc. when relevant.
- For pattern/surface motifs, describe the usable material role: package surface, UI background, card edge, overlay, crop/mask/repeat/layer material.

### Midjourney manual rail

- Chris wants DNA Dashboard split into two rails:
  - **GPT Image 2.5**: GoYJ M/W/F loop continues here.
  - **Midjourney**: Chris manually enters prompts into Midjourney and sends selected outputs for storage.
- Store manual Midjourney outputs in a separate manifest such as `public/data/midjourney-dna-archive.json` and assets under a separate directory such as `public/assets/dna-archive/midjourney/YYYY-MM-DD/`.
- Do not let the GoYJ scheduled loop write to the Midjourney rail. The Midjourney rail is user-supplied/manual only.
- Number Midjourney items in the title and filename (`Midjourney 01`, `Midjourney 02`, etc.) and keep replacement requests stable: if Chris says “2번을 이걸로 교체,” overwrite the existing 02 asset path and update hash/analysis rather than appending a new 02 duplicate.
- If Chris sends multiple images in one message and then corrects with “취소” / “원형만 저장해줘,” save only the explicitly requested image/type and ignore the accidental/unrelated image.
- If Chris combines a casual vision question like “What do you see in this image?” with an explicit archive instruction such as “두개 이미지 순서대로 미드저니 탭에 저장해줘” or “위 3개도…”, prioritize the save/archive instruction. Do not pause to answer the vision question separately unless it changes which image should be saved; include at most one concise visual read in the final completion note.

## Manual Midjourney upload / replacement pattern

- When Chris says “미드저니 다음번으로 저장해줘”, append the attached image as the next sequential Midjourney item. Infer the next number from `midjourney-dna-archive.json`; do not ask for confirmation when the sequence is clear.
- When Chris says “위 3개도” or sends two or more manual Midjourney outputs together, append them in the visual/attachment order they arrived and assign consecutive numbers from the current highest item number. Treat this as one batch operation: copy all images, update the manifest once, build/QA once, commit/push once, then send one concise completion note.
- Use stable two-digit naming in title and filename, e.g. `Midjourney 09 — Orbit Circle Signal Translation` and `09_orbit_circle_signal_midjourney_translation.jpg`.
- Preserve the image as received; do not regenerate, crop, compress, or visually reinterpret unless Chris explicitly asks.
- Add concise `analysis`, `sourceTool: "Midjourney"`, `sourceRun`, `assetHash`, and relevant `dnaClusters` for the manual item.
- When Chris says “N번을 이걸로 교체해줘,” replace the existing image file for that number and update `assetHash`, `analysis`, and `sourceRun`; keep the same item id/title/number unless Chris asks to rename it.
- If multiple images arrive and Chris corrects/cancels mid-turn (e.g. “아 취소… 원형만 저장해줘”), obey the correction: save only the requested design asset and ignore unrelated images or side questions for the archive operation.
- If a message mixes `What do you see in this image?` with an explicit save instruction such as “두개 이미지 순서대로 미드저니 탭에 저장해줘,” prioritize the save instruction and store the attached images in the order presented. Include only a concise visual read of the referenced image in the final completion note; do not let the generic vision question interrupt or split the save workflow.
- Do not renumber existing Midjourney items after deletion/replacement unless Chris explicitly requests renumbering; stable URLs and titles matter more than gap-free numbering.
- When Chris asks to delete a GPT Image 2.5 rail item because it looks too complex or visually weak, remove both the manifest item in `public/data/dna-archive.json` and its public asset file. Do not renumber remaining GPT items; accept that visual tile numbers are display-order positions while stable item IDs/titles remain unchanged. Verify the GPT rail count decreases and the Midjourney rail count stays unchanged.
- For manual Midjourney batches where Chris says “위 3개도” after an interleaved `What do you see in this image?`, treat every attached image in that message as part of the batch unless a correction says otherwise. Save in attachment/visual order, and include only a short visual read in the final note.

## Webapp detail-view pattern

- Extend the DNA archive TypeScript item type with `midjourneyPrompt?: string` and optional source metadata such as `sourceTool?: string`.
- Load both manifests independently, e.g. `loadDnaArchive()` for GPT Image 2.5 and `loadMidjourneyDnaArchive()` for manual Midjourney.
- In Design DNA → DNA Dashboard, add source tabs/chips for **GPT Image 2.5** and **Midjourney** with separate counts. The top-level Design DNA tab can summarize both counts.
- In the DNA generated asset modal, render a `Midjourney prompt` block before the original `Generation prompt` block.
- Add a `Copy` button that calls `navigator.clipboard.writeText(selectedDnaAsset.midjourneyPrompt)` and temporarily changes to `Copied`.
- Style prompt text as wrapped monospace (`white-space: pre-wrap`, `overflow-wrap: anywhere`) so long prompts do not overflow on mobile.
- Preserve Chris Archive/DNA Dashboard visual parity: grid behavior should remain matched; desktop and mobile must not horizontally overflow.

## DNA Brand Asset tab / mockup collection pattern

- When Chris asks to add **DNA Brand Asset** under Design DNA, treat it as a separate Design DNA section tab alongside `Design DNA` and `DNA Dashboard`, not as another source tab inside DNA Dashboard.
- Add two internal source tabs/chips: **Mockup** and **Midjourney + Mockup**.
- Until assets exist, keep empty sub-tabs intentionally quiet with only centered Korean copy `준비중입니다`; avoid adding sample cards, placeholder thumbnails, or explanatory clutter unless Chris asks.
- When Chris later sends mockup photos for the Mockup tab, replace the empty state with a named moodboard collection rather than loose one-off cards. For the full pattern, use `references/design-dna-brand-asset-mockup-workflow.md`.
- QA both desktop and mobile: the top Design DNA nav has three sections, each Brand Asset sub-tab toggles active state, collection images load when present, `준비중입니다` remains centered for empty sub-tabs, and no horizontal overflow appears.

## Manual Midjourney upload workflow

1. Copy the attached image from `/opt/data/image_cache/...` into `public/assets/dna-archive/midjourney/YYYY-MM-DD/NN_descriptive_midjourney_translation.jpg`.
2. Compute and store a sha256 hash in the manifest as `assetHash` so replacements can be verified.
3. Add/update the item in `public/data/midjourney-dna-archive.json` with:
   - `id`
   - `title` beginning with `Midjourney NN — ...`
   - `created`
   - `status: midjourney_manual_saved`
   - `sourceTool: Midjourney`
   - `imageSrc`
   - `prompt` and `midjourneyPrompt`
   - concise Korean `analysis`
   - `sourceRun`
   - `assetHash`
   - `dnaClusters`
4. Run JSON validation and `npm run build:public`.
5. Browser-verify Design DNA → DNA Dashboard:
   - GPT rail count remains correct
   - Midjourney rail count increments or replacement count stays stable
   - all Midjourney images load with nonzero `naturalWidth`
   - modal still shows prompt block and copy button
   - no horizontal overflow
6. Commit and push the manifest/image change, then verify the live manifest and asset URL after GitHub Pages updates.

## Replacement workflow

- For “Midjourney N번을 이걸로 교체,” keep the same item id, title, and `imageSrc` path when possible.
- Overwrite the binary at that path, update `assetHash`, update `analysis` and `sourceRun` to note replacement, then build/verify.
- Live verification should compare the deployed image hash when feasible, not just the manifest count.

## Loop/skill persistence

- Update the GoYJ scheduled loop prompt and GoYJ creative skill so future saved GPT Image 2.5 assets require `midjourneyPrompt`; otherwise later assets will silently lack copyable Midjourney prompts.
- Keep this requirement save-gated: unselected candidates do not need public manifest prompts.
- The loop should explicitly save to the GPT Image 2.5 rail, not the Midjourney rail.

## QA checklist
## QA checklist

- Build the webapp.
- Browser-verify Design DNA → DNA Dashboard:
  - GPT Image 2.5 source tab count equals `public/data/dna-archive.json` item count
  - Midjourney source tab count equals `public/data/midjourney-dna-archive.json` item count
  - every tile opens a detail modal
  - every modal has one Midjourney prompt block when the manifest item includes `midjourneyPrompt`
  - every modal has one Copy button
  - clicking Copy changes button text to `Copied`
  - clipboard text starts with the expected prompt and includes `--ar 1:1`
  - no horizontal overflow on desktop/mobile
- For deployment, verify live manifests and assets:
  - live `data/dna-archive.json` reflects GPT additions/deletions
  - live `data/midjourney-dna-archive.json` reflects manual Midjourney additions/replacements
  - each newly added image URL returns `200 image/*`
  - for replacements, compare the live image SHA/hash prefix against the newly copied local asset so CDN delay does not mask stale content
  - live JS/CSS contain the source-tab and prompt/copy selectors when UI changed

## Related Design DNA visual/copy preferences learned in this session

- Chris prefers human design language over blunt functional copy. Avoid phrases that sound like internal workflow labels, e.g. `저장해줘`, `썸네일을 클릭하면 생성 프롬프트...`, or awkward abstractions like `조용한 지능` when a more human phrase works.
- Match Design DNA title/body rhythm to Chris Archive when asked: title/body width around 760px, visible title-body spacing, and consistent typography.
- If Design DNA 19:10 hero images crop vertically on desktop, fix desktop only with `object-fit: contain`/natural 19:10 ratio while preserving tablet/mobile crop behavior if Chris says those are OK.
