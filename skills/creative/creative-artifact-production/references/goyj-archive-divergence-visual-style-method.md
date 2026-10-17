# GoYJ Archive-Divergence Visual Style Method

Use this reference when Chris asks to save, reuse, or publish Go Youn-jung's Design DNA visual-generation method, or when future GPT Image 2.5 motif candidates start feeling repetitive.

## Session learning

On 2026-09-28, Chris approved candidate 01 from a GoYJ DNA set, but asked 02-05 to be regenerated because the set was drifting back into the familiar warm-gray / capsule / circle / contour-line vocabulary. The regenerated 02-05 set was accepted because it deliberately sampled different Chris Archive visual axes before prompting.

The durable lesson: if Chris says the style is repetitive, do not make minor color tweaks. Change the **archive axis** before generating again.

## Core method

1. Pick the five reference axes before prompting.
   - At least four of five candidates should come from distinct Chris Archive families.
   - The axis is a visual grammar, not a color palette.

2. Enforce distance between candidates.
   - Candidates must differ in form logic: block, surface, bitmap, bloom, material, editorial, pattern, etc.
   - Avoid presenting five variants of the same capsule/circle/line system.

3. Keep outputs as motif material.
   - Not finished poster, logo, app icon, package label, UI screenshot, or product mockup.
   - Must be usable for crop, mask, overlay, repeat, background, package surface, mobile UI accent, or future mockup synthesis.

4. Preserve no-text/no-logo guardrails.
   - Reference images may contain typography, but output should extract structure/rhythm/color tension only.
   - Ban readable text, letters, numbers, logos, watermarks, UI chrome, product mockups, people, and generic AI startup effects.

## 2026-09-28 accepted axes

- Warm Gray Context Surface Field — quiet background surface / label zone.
- Monochrome Editorial Block System — strong editorial crop / geometric poster surface.
- Iridescent Chrome Surface Field — hero background / material mood surface; flatten if it becomes too object-like.
- Bitmap Stripe Rhythm Surface — repeat pattern / energetic card or package texture.
- Floral Signal Void Field — bold accent/background surface with emotional signal-field tension.

## Prompt skeleton

```text
PURE 2D GRAPHIC MOTIF MATERIAL ONLY.
No readable text, letters, numbers, logos, watermark, poster copy, app icon, UI screenshot, product mockup, people, photography.

Create a square 1:1 composable motif material from this Chris Archive reference axis: [AXIS NAME].
Do not copy any reference layout. Extract only structure, rhythm, material mood, color tension, and crop logic.
The output must be useful as [background / overlay / repeat pattern / package surface / mobile UI accent].
Avoid recent saved defaults: warm-gray capsule, circular seal, contour line, orbit, dot motif, generic AI glow.
Make it visually distant from the other candidates in this set.
```

## Webapp publication pattern

When Chris asks to “save this method and update the webapp”:

1. Save a canonical internal method doc under `/opt/data/dna-archive/methods/`.
2. Copy a public-safe version to `public/docs/` in the Hermes webapp.
3. Add a concise Design DNA card summarizing the method and exposing the MD download link.
4. If the selected assets were part of the same decision, publish them to Design DNA → DNA Dashboard, not Chris Archive.
5. Verify:
   - `npm run build:public` succeeds.
   - Public doc returns HTTP 200.
   - Method card renders on desktop/mobile without overflow.
   - DNA Dashboard contains the selected same-day assets and their images load.

## QA checklist

- [ ] Five candidates use distinct underlying visual grammars.
- [ ] No more than one candidate resembles recent warm-gray/capsule/circle/contour-line defaults.
- [ ] No text/logo/number/watermark appears in final images.
- [ ] Each candidate has a `reference axis`, `motif type`, `intended later use`, and `why different` note.
- [ ] Public webapp surfaces do not expose private local paths or raw internal logs.
