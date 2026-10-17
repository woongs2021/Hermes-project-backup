# Chris Design DNA hero + axis visual refinement lessons

Use when refining the Hermes webapp `Design DNA` tab, especially the Core DNA / Expression Layer visual system.

## What Chris corrected

- CSS-only gradient placeholders for Design DNA axis thumbnails felt low quality and “별로”. For this surface, use real generated assets when a visual is meant to carry brand value.
- Six small generated thumbnails inside every axis card made the page too busy. Prefer two strong 19:10 section hero images — one for Core DNA, one for Expression Layer — and keep the 1–6 cards typographic.
- If an Expression Layer hero feels complex/organic/“징그러워”, simplify aggressively: keep a clean circle, remove organic texture, and change only the gradient/color treatment.
- If a hero repeats the main circle too closely, preserve the circle form but shift color logic, e.g. split left/right with pale blue and pastel pink.
- When using a split blue/pink Expression Layer circle hero, do not stop at splitting the background. Split the circle stroke and soft halo to match the side it sits on: left stroke/halo blue, right stroke/halo soft pink. Chris explicitly preferred this over a single blue stroke crossing both halves.
- Number badges 1–6 should not be loud gradients. Use very light solid pastel fills with readable muted ink.

## Recommended implementation pattern

1. For section heroes, generate or derive 19:10 images at `2688×1415` and store under:
   - `public/assets/design-dna/section-heroes/`
2. Use cache-busting filenames when replacing live GitHub Pages assets, e.g. `expression-layer-hero-circle-blue-pink-19x10.png`, not the previous filename.
3. Keep `<figure className="design-dna-section-hero-image">` at the top of each section and verify:
   - exactly 2 section hero images
   - no per-card thumbnail images unless Chris asks for them
   - natural image size `2688×1415`
   - rendered ratio close to `1.9`
   - no horizontal overflow on desktop/tablet/mobile
4. For badge colors, set per-axis CSS variables as solid pastel fills, not gradients. Known-good lighter palette:
   - 01 `#faf4ec`
   - 02 `#f0f5ff`
   - 03 `#f4f8e9`
   - 04 `#f0f7f8`
   - 05 `#fbf3e8`
   - 06 `#fbf0f2`
5. When deriving a blue/pink circle from an existing circle hero, it is acceptable to use deterministic local image processing rather than regenerate: split/tint left and right halves while preserving the original circle geometry. If the original stroke remains one color after the background split, run a second pass that hue-shifts only the stroke/halo pixels on the opposite half so the stroke also follows the background split.
6. Use a new cache-busting filename for each visual correction, then update the JSX/image reference and verify the live `currentSrc` points to the new file.

## Verification checklist

- Run a production build before reporting completion.
- DOM/Playwright checks should confirm:
  - `.design-dna-section-hero-image img` count = 2
  - `.dna-gradient-thumb img` count = 0 if Chris asked to remove thumbnails
  - `.axis-map-number,.expression-layer-index` count = 6
  - badge `backgroundImage === 'none'`
  - hero image HTTP status 200
  - no page overflow across desktop/tablet/mobile
- If deploying to GitHub Pages, wait for the hashed JS/CSS and new public asset to be live, then verify again with a cache-busted URL.
