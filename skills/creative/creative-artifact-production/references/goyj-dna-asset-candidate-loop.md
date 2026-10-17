# GoYJ DNA asset candidate loop

Use when Chris asks to replace or operate Go Youn-jung's image-generation loop around Chris Archive / Design DNA / DNA Archive assets.

## Current operating model

- Owner/sender: Go Youn-jung specialist profile/bot, not Karina/default.
- Cadence: Monday/Wednesday/Friday in KST.
- User-facing output: 5 square (1:1) **graphic motif** candidates per run.
- Generation studio/model: Higgsfield CLI using **`gpt_image_2_5` only** for this loop. Do not substitute Seedream, Recraft, Kling, `image_auto`, or other models. If `gpt_image_2_5` is unavailable, report the blocker instead of generating with another model.
- Source of inspiration: Chris Archive references plus the synthesized `헤르메스디자인시스템.md` / Design DNA clusters.
- Intended asset range: composable motif materials for later Chris-led brand/package/mobile UI/mockup synthesis — surface fields, stroke/line motifs, soft object seeds, repeatable patterns, signal/accent fragments.
- Important framing: these are **not** finished posters, completed package labels, app icons, product mockups, UI screenshots, or final graphic-design deliverables. They should be useful layers that can be cropped, masked, overlaid, repeated, or placed onto later mockups.
- Save gate: do **not** publish or permanently save candidates by default. Show candidates to Chris for review. Only when Chris says `저장해줘` for a specific candidate should the agent save it into DNA Archive / webapp backdata; discard the rest.

## Candidate storage pattern

Temporary review candidates should live under:

- `/opt/data/dna-archive/candidates/YYYY-MM-DD/images/`
- `/opt/data/dna-archive/candidates/YYYY-MM-DD/candidate-manifest.json`
- `/opt/data/dna-archive/candidates/YYYY-MM-DD/candidate-analysis.md`

Selected/published assets should be represented separately, e.g.:

- `/opt/data/dna-archive/selected/`
- webapp public manifest `public/data/dna-archive.json`
- corresponding public image assets copied into the webapp only after the user selects them.

## Webapp representation

Do not put selected GoYJ generated images inside the Chris Archive tab. Chris corrected the IA:

- Chris Archive = user-curated inspiration/reference evidence only.
- Design DNA → DNA Dashboard = GoYJ-generated outputs selected by Chris.
- DNA Dashboard has separate rails: `GPT Image 2.5` (`public/data/dna-archive.json`) and `Midjourney` (`public/data/midjourney-dna-archive.json`). Keep these separated rather than mixing Midjourney manual uploads into the GPT rail.

In the webapp, keep the selected GoYJ outputs under the `Design DNA` tab as a `DNA Dashboard` subtab/section. Use a Chris Archive-like tile dashboard: image tile → detail modal with prompt, DNA clusters, intended use, and GoYJ analysis.

Before any selection, show an empty state rather than fake or placeholder assets. For visual consistency, match the DNA Dashboard grid/tile system exactly to Chris Archive across breakpoints: desktop 6 columns, tablet 3 columns, mobile 2 columns, same gap, tile padding, card radius, image min-height/radius, hover/focus behavior, and overflow checks.

### Midjourney manual upload/save pattern

When Chris attaches images and asks to save them to `DNA Dashboard > Midjourney`, treat the attachments as already user-selected manual Midjourney outputs and persist them sequentially:

1. Inspect the current `public/data/midjourney-dna-archive.json` item count and continue numbering from the highest visible tile number/title, not from the current batch size.
2. Copy each source image to both:
   - webapp public assets: `public/assets/dna-archive/midjourney/YYYY-MM-DD/NN_descriptive_slug.jpg`
   - original archive: `/opt/data/dna-archive/midjourney/YYYY-MM-DD/images/NN_descriptive_slug.jpg`
3. Add corresponding manifest items to `public/data/midjourney-dna-archive.json` with `sourceTool: "Midjourney"`, `status: "midjourney_manual_saved"`, `created`, `imageSrc`, `prompt`, `midjourneyPrompt`, `analysis`, `sourceRun`, `assetHash`, width/height, and `dnaClusters`.
4. Also write an archive-side batch manifest such as `/opt/data/dna-archive/midjourney/YYYY-MM-DD/midjourney-manual-manifest.json` so the original saved batch can be reconstructed without the webapp repo.
5. For analysis metadata, give each attachment a concise design-archive title and describe visual grammar, palette, material, motif type, and later use. Avoid claiming the exact Midjourney prompt is known unless Chris provided it; use a reconstruction prompt/motif prompt as a public-safe `midjourneyPrompt`.
6. Build, deploy, and verify the live Midjourney rail: total count increased, new same-day titles/numbers appear in order, images load, detail modal shows Midjourney prompt/analysis, desktop/mobile overflow is zero.

## Prompt guidance

Common prefix:

> Original Hermes design-system graphic motif material for future brand, package, UI, and mockup composition, based on repeated visual principles from an internal design archive. It is not a finished poster, not a product mockup, not a logo, not an app icon, and not a standalone artwork. 1:1 square composition, composable visual layer, useful for cropping, masking, overlaying, repeating, or placing on packaging/UI surfaces.

Run the five candidates as motif roles, not output categories:

1. Surface Field Motif — soft field/texture for package or UI backgrounds; avoid incidental lines, decorative scratches, random orbit marks, fake UI fragments, and unnecessary micro details.
2. Stroke / Line Motif — **line-only** rings, contours, lines, rhythm, orbit overlays; exclude filled planes, filled blobs, colored surface patches, heavy background shapes, decorative texture fields, and secondary motifs. Only lines/strokes on a quiet neutral base.
3. Soft Object Motif — crop-friendly object/mark seed, not a finished logo; keep the object simple and remove unrelated lines/decorations around it.
4. Pattern / Repeat Motif — repeatable/maskable pattern fragment; use one clear pattern logic, not many mixed decorative systems. Keep complexity lower than the model’s default, avoid over-dense multi-pattern compositions, and vary color tone rather than repeating the same archive palette every run.
5. Signal / Accent Motif — badge, seal fragment, state signal, small accent material; keep it clean and avoid extra decorative orbit lines unless they are the primary signal structure. Do not add yellow line graphics as decoration; yellow may appear only as a quiet filled accent/material cue if it is essential.

Latest GoYJ correction order to fold into all future runs: when refining motif candidates, prefer cleaner circular/formal geometry for Soft Object and Signal/Accent motifs when appropriate; reduce complexity in Pattern/Repeat motifs; change color tone for variety; and remove yellow line-graphic decorations, especially from the 5th signal/metaphor candidate.

2026-09-28 archive-divergence correction: Chris accepted the regenerated 02-05 set only after GoYJ escaped the repeated warm-gray/capsule/circle/contour-line default. For future five-candidate runs, choose distinct Chris Archive reference axes before prompting, and make at least four candidates visually distant in underlying grammar—not just color. Use axes like monochrome editorial block/geometric poster, iridescent chrome surface, bitmap/stripe rhythm, floral signal void, tactile paper/field, etc. If Chris says results feel repetitive, change the archive axis itself rather than doing minor color/style tweaks. Persisted method doc: `/opt/data/dna-archive/methods/2026-09-28-archive-divergence-visual-style-generation.md`.

Chris Archive priority rule: make the outputs feel maximally derived from the user-curated Chris Archive image language and design-system synthesis, not from generic AI image aesthetics. Translate archive color, spacing, motif rhythm, surface feeling, and quiet editorial structure into clean reusable motif materials.

Core DNA cues:

- Protected Human Context
- Warm-Cool Intelligence
- Quiet Signal Rhythm
- Tactile Optical Material
- Editorial Evidence System
- Soft Object / Presence Mark

Motif quality checks:

- Can it be placed on a mockup later?
- Does it crop, mask, overlay, or repeat well?
- Does it have clear negative space and useful edge behavior?
- Does it avoid looking like a complete AI artwork/wallpaper?

Negative prompt:

> No readable text, no third-party text, no brand names, no logos, no finished poster, no completed package label, no app icon, no exact reference layout, no product mockup, no UI screenshot, no robot, no brain symbol, no magic sparkle, no generic AI startup neon gradient, no cinematic object render, no decorative wallpaper-only image, no surveillance dashboard, no fake UI copy, no copyrighted character, no known package imitation, no sharp aggressive objects, no cluttered interface, no incidental decorative lines, no random scratches, no unnecessary orbit marks, no mixed visual systems, no yellow line graphic decoration. For Stroke / Line Motif specifically: no filled planes, no filled blobs, no color blocks, no surface patches, no object render, linework only.

## Delivery format

Final specialist DM should start with `고윤정입니다.` and include all five candidates using exact Telegram media syntax:

`MEDIA:/absolute/path/to/image`

For each candidate include: number, title, intended use, DNA clusters, why it was made, prompt gist, and GoYJ first critique. End with the selection instruction:

> 마음에 드는 번호를 말하고 `저장해줘`라고 하시면 그 이미지만 DNA Archive와 웹앱에 남기고 나머지는 버리겠습니다.

## Pitfalls

- Do not mirror every generated candidate into the public webapp. The whole point is Chris selection before persistence.
- When Chris later rejects/deletes a previously selected GoYJ DNA asset, prune it everywhere it was persisted: DNA Archive selected manifest, selected image file, webapp `public/data/dna-archive.json`, corresponding public image asset, and any method-card/doc axis list that would otherwise keep the deleted style visible. Verify the deleted title is absent and the deleted asset URL no longer resolves before reporting completion.
- Do not store selected GoYJ assets in `Chris Archive`; store them under `Design DNA → DNA Dashboard`.
- Do not let DNA Dashboard drift visually from Chris Archive: after CSS changes, verify computed grid/tile styles on desktop/tablet/mobile against Chris Archive, not only that images appear.
- Do not use non-`gpt_image_2_5` models for this GoYJ DNA candidate loop unless Chris explicitly changes the rule again.
- Do not keep the older “daily still + turntable” loop wording if Chris has changed the lane to M/W/F five still candidates.
- Do not ask the image model to render readable Korean or product UI text; use abstract/no-text graphical systems unless exact typography is applied locally.
- Do not use `MEDIA /path`; Telegram attachment syntax requires `MEDIA:/path`.
- Do not claim generation succeeded unless the five image files exist and dimensions are square or verified as intended.
