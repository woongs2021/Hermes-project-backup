# Webapp visual content and cross-tab QA patterns

Use this reference for static React/Vite webapps where the user is iterating on visual quality, cross-tab navigation, hosted Pages deployment, and image insertion.

## Cross-tab card → detail navigation

When a card in one tab should open a related detail in another tab:

1. Lift the selected item id to the parent app state.
2. Pass a callback into the source tab, e.g. `onSelectResearchItem(item.id)`.
3. In the target tab, accept `selectedItemId` as a prop and set the local selected id only after the item exists in loaded data.
4. Clear conflicting local filters/search before selecting, if needed.
5. Do not use a generic `scrollTo({ top: 0 })`; it sends the user to the top of the tab rather than the detail.
6. If the desired landing is a specific detail/title area, attach a ref to the detail wrapper and compute an explicit target:

```ts
const detailTop = detailRef.current?.getBoundingClientRect().top ?? 0
const targetY = Math.max(window.scrollY + detailTop - 96, 0)
window.scrollTo({ top: targetY, left: 0, behavior: 'smooth' })
```

7. Guard programmatic scrolls with a `lastScrolledTargetRef` so React re-renders do not repeatedly scroll.
8. Clear the programmatic trigger on ordinary top-nav tab clicks so direct navigation does not inherit a previous cross-tab scroll target.

Browser probe should capture: pre-click item title/id, post-click hash/active tab, selected detail title, active card title, `scrollY`, detail/title bounding boxes, top-of-tab bounding box, and console/page errors.

## Visual QA for chart/card readability

For SVG/HTML overlay charts:

- Keep dots on the SVG line by converting viewBox coordinates to overlay percentages, e.g. `top = y / viewBoxHeight * 100%`.
- Separate explanatory cards from the line with a dedicated card offset instead of moving the dot off the line.
- Verify with geometry, not only screenshots: dot-center delta from line, card-bottom vs line separation, overflow count, and dot aspect ratio.

## User-facing visual tuning signals

If the user says the layout is visually confusing, over-bold, cramped, or not landing in the right place, treat it as an implementation bug, not copy feedback only. Update CSS/interaction and verify computed values:

- font-size and font-weight
- paragraph count/gap and line-height
- title top/bottom viewport position after navigation
- image natural size, `complete`, object-fit, overflow, and ordering relative to neighboring cards

## Static image insertion in a Vite public app

1. Copy the source image into `public/assets/<section>/...` with a descriptive, stable filename.
2. Reference with the app's public asset helper/base path, not an absolute local path.
3. Preserve intrinsic `width`/`height` on `<img>`.
4. For full-width visual cards, ensure later responsive `.content-card` rules do not reintroduce padding. Add same-breakpoint overrides after generic card padding rules when necessary.
5. Hosted verification: poll the live HTML for the new hashed CSS/JS, fetch the new asset path for HTTP 200/content length, then run browser QA across mobile/tablet/desktop.

## Mobile/tablet topbar edge alignment

When the user reports that a mobile or tablet top tab/header has unwanted margins, distinguish three different insets before editing:

1. **Viewport edge inset** — element `getBoundingClientRect().left/right/top` vs `innerWidth`/`0`.
2. **Sticky offset** — computed `position`, `top`, `margin`, `padding`, and transform on the topbar container.
3. **Internal row offset** — brand/title/hamburger rows, nav `margin-top`, and nav `padding-top`; the tab row may legitimately sit below a brand row unless the user asks to reorder the structure.

For mobile/tablet full-bleed top navigation in a centered static app:

```css
@media (max-width: 900px) {
  .topbar,
  :root[data-theme='dark'] .topbar {
    width: 100vw;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
    top: 0;
  }

  .topbar .tab-nav,
  .topbar .tab-nav.open {
    width: 100vw;
    min-width: 100vw;
    max-width: 100vw;
    flex-basis: 100vw;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
  }
}
```

If a follow-up says the top still has a margin, measure and remove container offsets such as `top: 10px` and child `margin-top: 20px`; do not assume left/right full-bleed solved top alignment. Verify with browser probes that mobile/tablet `topbarInsetTop === 0`, nav left/right inset `0/0`, `overflowX === 0`, and console/page errors are empty. Keep desktop spacing unchanged unless the user explicitly asks for desktop full-bleed too.
