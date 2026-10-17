# Dashboard Thumbnail Radius + Heavy Asset Loading Pattern

Use when maintaining visual dashboards such as Design DNA, Chris Archive, or DNA Brand Asset where thumbnails can look square/uneven or large PNGs slow list views.

## Symptoms

- A few square thumbnails appear to have no radius even though `border-radius` is set.
- Items with strong full-bleed rectangular color fields, e.g. Midjourney 02/10, look more square than neighboring assets.
- Heavy 4K/PNG assets in a grid make the list feel slow.
- Low-resolution list image and high-resolution detail/download image diverge in composition after generative resynthesis.

## Durable UI fix

For list/grid tiles, use a fixed media frame and force clipping on the image itself:

```css
.dashboard-tile img {
  display: block;
  width: 100%;
  aspect-ratio: 1 / 1;
  height: auto;
  min-height: 150px;
  border-radius: 22px;
  object-fit: cover;
  overflow: hidden;
  clip-path: inset(0 round 22px);
  background: rgba(0, 0, 0, 0.04);
}

@media (max-width: 768px) {
  .dashboard-tile img {
    min-height: 120px;
    border-radius: 18px;
    clip-path: inset(0 round 18px);
  }
}
```

`clip-path: inset(... round ...)` is the important belt-and-suspenders fix when `border-radius` appears to be ignored or visually weak on full-bleed images.

## Heavy asset loading rule

- Grid/list view should use a lightweight preview/thumbnail path and never default to large full-res PNGs.
- For **Midjourney + Mockup** sets specifically, always create a separate `previewImageSrc` asset for every generated mockup item, then render grids/lists with `previewImageSrc ?? imageSrc`.
- Keep detail modal, zoom/detail imagery, and download buttons on the high-resolution path: `imageSrc`, `highResImageSrc`, or `downloadSrc` depending on the manifest shape.
- Do not load 20–40MB PNGs in the default grid.

### Midjourney + Mockup preview contract

When adding or replacing any Midjourney-applied mockup set such as Coffee Mockup Examples, Outdoor Mockup A, or Outdoor Mockup B:

1. Generate the normal high-resolution mockup asset first and keep it as the canonical `imageSrc` / detail asset.
2. Generate a lightweight preview derivative from the approved high-res asset, typically WebP at about `900px` wide and visually acceptable quality around `70–75`.
3. Store the preview next to or under a clearly named preview directory/path; do not overwrite or downsample the canonical high-res PNG.
4. Add manifest metadata for the preview:
   - `previewImageSrc`
   - `previewWidth`
   - `previewHeight`
   - `previewAssetHash`
   - `previewGeneratedAt`
5. Render list/grid cards from `previewImageSrc ?? imageSrc`.
6. Render detail modals and download links from the original full-resolution fields, not the preview.

Target outcome: preview payload should be tiny compared with the full asset set, while detail view remains publication/download quality.

## Mockup high-res normalization rule

If low-res and high-res mockup compositions diverge, prefer geometry-preserving upscale from the approved `originalImageSrc` instead of another generative re-composition. The high-res should differ only in resolution/clarity, not crop, object geometry, pattern direction, or scene layout.

## Verification checklist

- Build succeeds.
- Desktop and mobile list tile computed styles show nonzero radius, expected `clip-path`, 1:1 aspect ratio, and square rendered dimensions.
- List image `src` points to lightweight/original asset.
- Modal image `src` points to high-resolution asset and reports expected natural dimensions.
- Download button `href` matches high-resolution asset.
- `overflowX` is 0 and console/page errors are empty.
