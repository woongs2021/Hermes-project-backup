# Webapp internal image-border crop QA

Use when a user reports that thumbnails or modal images still show a light/ivory edge even after `border-radius`, `overflow: hidden`, or wrapper-frame fixes.

## Core diagnosis

Distinguish three different problems before editing:

1. **Frame/border issue**: the CSS border or card frame is visible outside the image.
2. **Image fill issue**: the rendered `<img>` is smaller than its clipping frame, often because a real `border` or padding reduces the image box.
3. **Source-pixel border issue**: the source image itself contains a light/ivory outer rim. The image may already fill the frame perfectly, but the rim is part of the bitmap.

If the user says “only a thin stroke appeared” or “the image still does not fill the frame,” measure frame and image rects first. If the user later says “the image itself looks like it has an ivory outline,” treat it as source-pixel border and crop the displayed image, not the frame.

## Safer implementation pattern

Prefer non-destructive display crop over rewriting original assets:

```css
.asset-media {
  position: relative;
  overflow: hidden;
  border-radius: 24px;
  clip-path: inset(0 round 24px);
}

.asset-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transform: scale(1.08);
  transform-origin: center;
}
```

For detail modals, add a dedicated class if the base modal media class is shared with other asset types. Avoid letting the crop affect mockups, brand assets, or images that must preserve full bleed/layout.

```tsx
<div className="generated-modal-media dashboard-modal-media">
  <img src={...} alt={...} />
</div>
```

```css
.dashboard-modal-media {
  width: 100%;
  aspect-ratio: 1;
  padding: 0;
  overflow: hidden;
}
```

## Verification probe

Use Playwright/computed geometry, not eyeballing CSS:

- Open the exact dashboard/tab/subtab where the assets render.
- Check desktop/tablet/mobile.
- For each viewport capture:
  - media frame width/height
  - image width/height
  - crop pixels: `(img.width - media.width) / 2`
  - computed `transform`
  - media `overflow`
  - natural image dimensions
  - console errors
- Expected outcome for source-pixel crop: image rect is larger than media frame and `transform` is a scale matrix, e.g. `matrix(1.08, 0, 0, 1.08, 0, 0)`.

## Tuning guidance

- Start with `scale(1.08)` for subtle embedded outer rims.
- If a rim remains visible, move to `1.10` or `1.12` rather than adding visible strokes.
- Keep the original source image intact unless the user explicitly asks for destructive asset cropping/downloadable cropped files.
- Do not use a real `border` to simulate a stroke when the user is judging fill; a real border changes the available image box and can create a 1px inset. Use an inset `box-shadow` overlay if a visual edge is needed without shrinking the image.
