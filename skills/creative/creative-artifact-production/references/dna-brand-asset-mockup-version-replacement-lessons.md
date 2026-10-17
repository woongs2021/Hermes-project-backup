# DNA Brand Asset mockup version replacement lessons

Use when Chris asks to replace an existing Outdoor Mockup child set (for example `A-2`) with a different numbered Midjourney source, while preserving the visible lane/version position.

## Replacement pattern

- Treat the visible label (`A-2`, `B-3`, etc.) as the product-facing slot, not as a permanent file/ID identity.
- Generate the replacement under a fresh internal example ID and cache-busting asset root when useful, then update the manifest so the visible title remains the requested slot.
- Keep neighboring sets' visible numbering stable unless Chris explicitly asks to reorder them.
- If Chris says a full set is still wrong (`여전히 맘에 안들어`, `전체를 ...로 변경`), replace all six images for that visible set rather than doing tiny local tweaks.
- Do not delete old generated assets from disk just because the manifest no longer references them, unless they were mistakenly committed as candidate/temporary files. The live dashboard should only expose the final manifest-selected files.

## Manifest workflow

1. Confirm the requested Midjourney numbered source high-res path in `public/assets/dna-archive/midjourney-4k/`.
2. Generate six new mockup images using the same raw mockup collection for the visible slot.
3. Write a temporary `new_<slot>_example.json` or equivalent so generation and manifest surgery are decoupled.
4. Replace only the manifest entry for the visible slot with the new example object.
5. Preserve the intended A/B ordering and renumber item titles (`A-2-1` ... `A-2-6`) in the manifest.
6. Remove public candidate files from git if they were accidentally staged; keep only final images referenced by the manifest.

## Visual QA before publishing

- Always inspect a contact sheet before committing.
- For multi-board mockups (`*-5`), check both conditions:
  - every main surface is visibly printed enough; no large blank white board should remain unless it is part of the source design,
  - the seam/step and separate paper/board thickness remain visible so it does not read as one continuous panorama.
- If only item 5 fails, regenerate just item 5 with two candidates and select before manifest insertion. Use prompts that explicitly say both large boards must be visibly printed and the seam must remain separated.
- If the replacement source has strong directional lines/stripes/flow, avoid continuous alignment across the seam; offset or crop each board differently.

## Deployment / verification

- Run JSON validation and `npm run build:public` before committing.
- Push the manifest and final image files together.
- Verify live manifest order and source labels after GitHub Pages deployment.
- Probe each new live asset URL for `200 image/png` and expected dimensions (`2496×1664` for these Kling 2K 3:2 outputs).
- Use a Playwright manifest/image probe for console errors and overflow; lazy thumbnail checks can be timing-sensitive, so direct asset and modal/image probes are stronger evidence.

## Communication

- Keep Chris updated briefly: say what changed, which Midjourney source is now in the visible slot, and whether deploy/live verification passed.
- If a generated set looks off during QA, say so and fix it before publishing rather than presenting the flawed set as done.
