# Chris Archive dashboard UI polish and duplicate cleanup

Use this reference when Chris asks to refine the Chris Archive tab in the Hermes GitHub Pages webapp.

## Durable patterns from 2026-09-13 work

### Responsive thumbnail grid

Chris prefers the Chris Archive dashboard to read as a dense visual board rather than a loose auto-fill gallery:

- Desktop: 6 columns.
- Tablet: 3 columns.
- Mobile: 2 columns.

Prefer explicit breakpoint rules over `auto-fill` when Chris asks for an exact visual count.

Example CSS shape:

```css
.chris-archive-grid {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 0.9rem;
}

@media (max-width: 1024px) and (min-width: 761px) {
  .chris-archive-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 760px) {
  .chris-archive-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

### Modal legibility and sizing

For archive detail popups, Chris prefers readability over heavy glass/blur effects:

- Use a theme-aware solid-ish backdrop layer behind the blur.
- Light mode: bright/warm light overlay.
- Dark mode: dark charcoal overlay.
- Keep the modal body mostly opaque.
- Desktop target: about 70% viewport width/height.
- Tablet: avoid clipping by widening to about `92vw` with a max around `820px`.
- Use `minmax(0, 1fr)` in tablet/desktop modal columns to prevent content from forcing horizontal overflow.
- Mobile can keep the bottom-sheet feeling.

### Scrollbars inside the modal

Chris requested the modal scrollbar to stay hidden before scrolling and appear only briefly while scrolling.

Implementation pattern:

- CSS default: `overflow-x: hidden; overflow-y: auto; scrollbar-width: none;` and WebKit scrollbar width/height `0`.
- Add an `is-scrolling` class while the modal scrolls.
- Remove it after a short timeout, e.g. 850ms.
- In `is-scrolling`, set `scrollbar-width: thin` and lightweight thumb styles.
- Verify `overflowX === 'hidden'`, scrollbar hidden before/after, and scrollbar thin during scroll with Playwright computed-style probes.

### Duplicate cleanup

When Chris says archive images look duplicated:

1. Compare public webapp archive assets by file hash first; remove exact duplicates from the public manifest and public assets.
2. Preserve the first occurrence as canonical unless there is a clearly better title/metadata reason to keep another.
3. Verify after cleanup:
   - manifest item count equals rendered tile count;
   - all manifest `imageSrc` assets return HTTP 200 and image content-type;
   - exact duplicate hash count is 0.
4. Be careful with `.gitignore` patterns such as `*token*`; web asset filenames containing sensitive-looking words may be ignored and cause GitHub Pages 404. Rename public asset filenames to neutral names if needed, then update the manifest.

### Live verification checklist

After pushing to `main`, verify the GitHub Pages URL, not only local preview:

- CSS marker from the new build is present in the live asset.
- Manifest item count is expected.
- Desktop/tablet/mobile grid columns match requested counts.
- Modal opens and closes.
- Tablet modal bounding rect stays inside viewport.
- Modal `overflow-x` is hidden.
- Scrollbar class appears during scroll and disappears after the timeout.
- All archive image assets return 200.
