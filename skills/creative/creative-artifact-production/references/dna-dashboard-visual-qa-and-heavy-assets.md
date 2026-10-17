# DNA Dashboard / Brand Asset visual QA + heavy asset handling

Use this reference when changing Chris's Design DNA Dashboard, Midjourney rail, or DNA Brand Asset mockup UI/assets.

## Durable lessons from the Midjourney 4K + mockup work

### 1. Keep list views lightweight

- Heavy 4K PNGs can make list/grid views feel slow.
- For list/grid tiles, prefer the lightweight/original asset:
  - DNA Brand Asset mockups: render `item.originalImageSrc ?? item.imageSrc` in tiles.
  - Reserve `item.imageSrc` / `downloadSrc` high-resolution PNGs for modal/detail and download.
- Verify this explicitly with browser inspection: tile `img.src` should point to the low-res/original path, while modal `img.src` should point to the high-res path.

### 2. If low-res and high-res compositions diverge, preserve geometry

- Generative mockup re-synthesis can change crop, product geometry, cup/lid shape, package angle, or pattern direction.
- If Chris says the low-res and high-res versions differ, do not keep re-generating freely.
- Use the approved `originalImageSrc` as the geometry source and create a high-resolution geometry-preserving upscale/sharpened PNG.
- The accepted standard: list low-res and detail high-res should differ only in resolution/clarity, not in composition, crop, direction, or object shape.

### 3. Border-radius QA must be visual, not computed-style only

- A computed `border-radius` on `img` may still look square when the image has strong edge color fields.
- For DNA tiles and modal media where radius must be visually obvious, use a stronger clipping stack:
  - `aspect-ratio: 1 / 1`
  - `object-fit: cover`
  - explicit `border-radius`
  - `overflow: hidden`
  - `clip-path: inset(0 round <radius>)`
  - `-webkit-mask-image: -webkit-radial-gradient(white, black)`
  - a subtle 1px rounded border to reveal the corner on low-contrast assets
- Verify with actual screenshots on desktop, tablet, and mobile. Do not rely only on computed CSS values.

### 4. Live GitHub Pages verification pattern

- After push, GitHub Pages may serve the old bundle for a short time.
- Poll the live HTML for the current hashed CSS/JS filename, then inspect the live CSS or browser computed style.
- Use cache-busting query params for checks, e.g. `?cb=<timestamp>`.
- Final verification should include:
  - desktop, tablet, mobile viewport screenshots
  - tile image paths and dimensions
  - modal/detail image paths and natural dimensions
  - download button href
  - console/page errors
  - horizontal overflow (`scrollWidth - clientWidth == 0`)

## Suggested acceptance checklist

- [ ] Build succeeds.
- [ ] Live bundle is updated, not just local preview.
- [ ] Desktop/tablet/mobile tile screenshots look correct.
- [ ] Detail modal screenshots look correct.
- [ ] Lightweight list source and high-res detail/download source are intentionally separated when assets are large.
- [ ] If radius/shape is the issue, screenshots confirm visual appearance, not just CSS values.
