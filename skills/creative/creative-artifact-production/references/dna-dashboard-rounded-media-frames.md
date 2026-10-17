# DNA Dashboard rounded media frames

Use when Chris flags that DNA Dashboard / Chris Archive thumbnails or detail images look square, do not fill their rounded frame, or only show a thin stroke without the image filling the frame.

## Durable lesson

Do not rely on `border-radius` directly on an `<img>` inside a grid tile when the visual requirement is “image fills a rounded frame.” In this dashboard class, use an explicit media-frame wrapper so the frame, clipping, and image fill are separate concerns.

## Recommended structure

```tsx
<button type="button" className="dna-generated-tile">
  <span className="dna-generated-tile-media" aria-hidden="true">
    <img src={toAppAssetSrc(item.imageSrc)} alt="" loading="lazy" decoding="async" />
  </span>
  ...metadata...
</button>
```

## Recommended CSS pattern

```css
.dna-generated-tile-media {
  position: relative;
  display: block;
  width: 100%;
  aspect-ratio: 1 / 1;
  min-height: 150px;
  overflow: hidden;
  border-radius: 24px;
  clip-path: inset(0 round 24px);
  -webkit-mask-image: -webkit-radial-gradient(white, black);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--ink) 8%, transparent);
  background: rgba(0, 0, 0, 0.04);
}

.dna-generated-tile-media img {
  position: absolute;
  inset: 0;
  display: block;
  width: 100%;
  height: 100%;
  max-width: none;
  object-fit: cover;
  object-position: center;
}
```

For mobile, override the wrapper radius/min-height, not the image alone.

## Pitfall

A normal `border: 1px solid ...` on the media frame reduces the content box, so the image can appear inset by 1px. If Chris says “only a thin stroke appeared and the image still does not fill the frame,” replace the border with `box-shadow: inset 0 0 0 1px ...` and verify image and media-frame rects are identical.

## Verification checklist

Use Playwright/DOM checks across desktop, tablet, and mobile:

- `mediaRect` and `imgRect` must match exactly.
- `imgInset` should be `[0, 0, 0, 0]`.
- wrapper has rounded `clip-path` and `overflow: hidden`.
- image has `position: absolute`, `inset: 0`, `width/height: 100%`, `object-fit: cover`.
- detail modal still loads the high-res image and has rounded clipping.
- `overflowX` is 0 and no console/page errors.

## Why this matters

Some Midjourney assets have strong edge color fields; even when CSS `border-radius` is technically applied to the image, the visual can still read as square. A dedicated rounded media frame makes the radius visually reliable and keeps the image fully filled.