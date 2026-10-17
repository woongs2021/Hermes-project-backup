# Visual Archive hero image replacement and frame-fill QA

Use when Chris asks to replace the Hermes webapp Visual Archive hero/camera image or reports black bands/letterboxing in that image frame.

## Stable paths

- Component reference usually lives in `august-dashboard/src/App.tsx` near `.visual-archive-image-card`.
- Current public asset path: `august-dashboard/public/assets/visuals/visual-archive-camera-object.jpg`.
- Prefer preserving the public asset path when replacing the hero image, then only update the `alt` text. This avoids touching route/base-path logic.

## Replacement pattern

1. Copy the approved source image over the existing public asset path.
2. Verify source and destination bytes with `sha256sum`.
3. Update `alt` text to describe the new image accurately.
4. Run:
   - `npm run validate:data`
   - `npm run lint`
   - `npm run build:public`
   - `git diff --check`
5. Revert generated `public/data/*` timestamp-only changes unless the task intentionally updates public manifests.
6. Commit only the image and intentional source/CSS changes.
7. Push `main`, wait for GitHub Pages Actions to complete, then verify live asset/load state.

## Frame-fill / black-band fix

If Chris says the image does not fill the frame or black bands are visible:

- Do not replace the image again unless the crop itself is wrong.
- First inspect CSS for `.visual-archive-image-card` and later `.content-card` overrides.
- The common failure mode is that a generic `.content-card` padding wins on mobile, leaving the image inset over a dark figure background.
- Use a specific selector so only the Visual Archive hero is affected:

```css
.content-card.visual-archive-image-card {
  padding: 0;
}

.content-card.visual-archive-image-card > img {
  width: 100%;
  height: 100%;
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
  object-position: center;
  transform: scale(1.16);
  transform-origin: center;
}
```

Adjust scale if Chris requests a different crop, but verify mobile as well as desktop.

## Verification without screenshots

If Chris has asked not to capture screenshots, use DOM/computed-style probes instead:

- image `complete === true`
- image `naturalWidth > 0` and expected natural dimensions
- card padding is all `0px`
- `objectFit === 'cover'`
- transform includes the intended scale
- rendered image rect width and height are each >= frame rect width and height
- `document.documentElement.scrollWidth - window.innerWidth === 0`
- live asset SHA-256 matches the local replacement image when verifying deployment

If a first browser check catches the image before decode (`complete: false`, `naturalWidth: 0`), wait for `img.complete && img.naturalWidth > 0` and retry; the lesson is to wait for decode, not that the asset is broken.
