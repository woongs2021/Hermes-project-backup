# Pixel team turnaround-sheet production

Use when Chris approves team character fronts and asks for a unified five-direction pixel character set.

## Goal

Produce one square sheet per character with exactly five full-body views in this left-to-right order:

1. front
2. three-quarter front
3. profile
4. three-quarter back
5. back

The target is a shared **2.5-head-tall chibi proportion**: an oversized head around 42% of total figure height, compact torso and legs, and identical scale across all five views.

## Proven workflow

1. **Gate the work.** Generate/approve full-body front candidates first. Do not create a full cast of turnarounds until Chris accepts the direction.
2. **Choose one accepted ratio master.** Use the accepted lead-character turnaround as the primary style/proportion reference for every other character. Use each character's approved front candidate only for identity, outfit, hair, glasses, and palette.
3. **Use GPT Image 2.5 through Higgsfield.** Generate a 1:1, high-quality, 2K sheet with the two references.
4. **Prompt constraints explicitly.** State the exact order, five views only, complete head-to-shoes bodies, 2.5-head ratio, same outfit/shoes, neutral pose, warm blank background, pixel outlines, and a strict negative list: no text, labels, grid, arrows, props, UI, logo, watermark, extra people, duplicate views, cropped limbs, photorealism, or painterly style.
5. **If the model drifts on proportion, regenerate rather than accept.** Make the ratio numeric and visual: “head about 42% of figure height; short compact torso and legs; match first reference exactly.” Passing a generic sprite reference can yield taller 3-head-ish figures or inconsistent sheets.
6. **Treat every result as candidate-only until visual inspection.** Reject a sheet that has a broken face, fewer/more than five views, unreadable profile, inconsistent clothing, non-matching body ratios, watermark/text, or cropped feet. A technically completed job is not an accepted asset.
7. **Verify and store.** Confirm PNG signature/dimensions and visually inspect all six sheets. Keep approved/candidate assets outside webapp public paths until Chris separately approves integration.

## Higgsfield upload reliability

For reference-heavy generation, use moderately sized reference images. If a reference upload fails transiently, make a nearest-neighbor 768px proxy of the style image and each front candidate, then retry the same generation with those proxy references. Keep the full-resolution output as the deliverable.

```bash
ffmpeg -y -loglevel error -i input.png \
  -vf 'scale=768:-2:flags=neighbor' -frames:v 1 reference-768.png
```

## Delivery

Send the six image sheets first, with a concise line that confirms the shared proportion and five-view order. Do not publish them to the webapp, split them into directional sprites, or deploy until Chris explicitly asks for that next phase.
