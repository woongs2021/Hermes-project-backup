# Higgsfield Nano Banana Pro mockup-composite lessons

Use when Chris asks to combine a saved Design DNA / Midjourney motif with physical product mockups (coffee cups, bags, signage, packaging) and publish the result back into the Hermes webapp.

## Preferred workflow

1. **Use Nano Banana Pro for the physical composite**
   - Model: `nano_banana_pro`.
   - Use the mockup image as reference 1 and the motif/graphic image as reference 2.
   - Ask the model to preserve the original mockup product, camera angle, lighting, shadows, material texture, depth of field, and composition.
   - Ask it to apply the motif only to the blank printable surface and follow the surface geometry: cylinder curvature, folds, fabric weave, bag creases, or sign-plane perspective.
   - Explicitly tell it not to generate logo text, letters, watermarks, placeholder marks, or extra graphics outside the printable surface.

2. **Treat logo typography as a separate design decision, not a default requirement**
   - Generated text may distort, add shadows, or use the wrong font.
   - Generate the mockup composite without logo text first.
   - If Chris explicitly asks for a logo, start with a logo-image reference rather than a plain text overlay: render the exact logo as transparent PNG/SVG, feed it to Nano Banana Pro with the patterned mockup, and ask for physical ink/material integration.
   - If Chris says the logo looks unnatural after one or two fusion attempts, stop forcing it. Remove the logo and publish a **pattern-only** mockup; update manifest titles/descriptions/status so stale logo language such as `ONBOARD` does not remain.

3. **Typography rules from Chris correction**
   - Logo font when requested: Open Sans via Google Fonts family `Open Sans`.
   - Use no drop shadow / no glow / no bevel / no stroke on logo text.
   - Prefer a small, quiet mark over a large hero logo when the surface already has a strong pattern; Chris may ask for ~70% or ~30% logo-reference scale, but the better final answer may still be pattern-only.
   - Natural physical integration matters more than perfect all-letter legibility unless Chris explicitly asks for a legibility-first lockup.

## Higgsfield CLI upload pitfall and fix

If local image-reference upload fails with S3 `SignatureDoesNotMatch`, do not conclude Higgsfield is unusable. First update the CLI:

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
npm install -g @higgsfield/cli@latest
higgsfield version
```

In the observed session, `@higgsfield/cli@1.1.9` produced presigned-upload signature errors, while `1.1.26` successfully uploaded local mockup and motif references.

## Example command shape

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
higgsfield generate create nano_banana_pro \
  --aspect_ratio 3:2 \
  --resolution 2k \
  --image-references /path/to/mockup.jpg \
  --image-references /path/to/motif.jpg \
  --prompt "Create a high-quality realistic coffee brand mockup based on reference image 1. Preserve the same product, camera angle, lighting, shadows, material texture, depth of field, and 3:2 composition. Apply the abstract motif language from reference image 2 onto only the blank white printable brand surface. Follow the product perspective, folds, cylinder curvature or sign-plane geometry so the motif looks physically printed on the material, not pasted flat. Keep the rest of the scene unchanged, premium, calm, and natural. Do not add any logo text, letters, watermark, mockup placeholder marks, extra graphics outside the printable surface, or drop shadows for typography." \
  --wait --wait-timeout 20m --wait-interval 5s --json
```

- For single-asset revisions inside an existing mockup set, generate at least two targeted candidates rather than accepting the first retry. Build a small contact sheet with `current`, `revision_01`, `revision_02`, then select by set consistency, physical integration, and surface coverage before overwriting the published asset.
- If a cyan arc / luminous edge motif becomes only a thin line overlay, strengthen the prompt with: “not only thin line art”, “substantial dark teal/black filled surface fields”, “smoky deep background patches”, and “apply to BOTH/ALL relevant printable surfaces.” This keeps tote/cup/sign compositions visually aligned with darker pattern sets.
- When replacing just one published image, update only that image file and its manifest item hash/description, preserve the previous version in an archive `replaced/` folder, and live-verify both the manifest hash and the browser modal image.

## Webapp publication checklist

- Download/store the raw Nano Banana Pro outputs before any optional post-processing.
- Do not mix source mockup assets and synthesized examples in the same rail; use the DNA Brand Asset `Mockup` and `Midjourney + Mockup` split.
- If publishing a logo-free final, remove `logoText`/`logoFont` from the manifest, rename item titles from logo-bearing names to pattern-oriented names, and use a status such as `nano_banana_pro_pattern_only`.
- Run build and browser-verify the Design DNA → DNA Brand Asset → Midjourney + Mockup tab on desktop/tablet/mobile.
- Verify every published image URL returns `200 image/*`.
- For modal/grid UI QA, verify desktop computed columns and modal dimensions with DOM metrics. Chris currently prefers Chris Archive and DNA Dashboard image grids at 5 columns on desktop, and the Chris Archive / DNA Dashboard / DNA Brand Asset modal family to share the same generous width (`min(90vw, 1280px)`) with the close button inside the modal card.
