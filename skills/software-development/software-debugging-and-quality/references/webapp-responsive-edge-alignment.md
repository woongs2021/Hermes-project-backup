# Webapp responsive edge-alignment and full-bleed UI checks

Use this when a user says a mobile/tablet header, top tab bar, sticky nav, image strip, or other edge-to-edge UI has unwanted left/right margins.

## Session-proven pattern

1. **Measure rendered geometry before editing.** In Playwright, capture viewport width, `documentElement.clientWidth/scrollWidth`, and bounding boxes for the shell, topbar/header, nav, first tab/button, and content container. Report `left`, `right`, `width`, plus computed `margin`, `padding`, `gap`, and layout mode.
2. **Separate full-bleed chrome from content width.** If only the navigation strip should touch the viewport edges, keep the content shell/card widths intact and apply the full-bleed rule only to the header/nav layer.
3. **Use viewport-based sizing when parent width constrains the nav.** If `width: calc(100% + padding)` still leaves one side inset because grid/flex sizing clamps the child, use a stronger viewport rule on mobile/tablet:

```css
@media (max-width: 900px) {
  .topbar,
  :root[data-theme='dark'] .topbar {
    width: 100vw;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
  }

  .topbar .tab-nav,
  .topbar .tab-nav.open {
    width: 100vw;
    min-width: 100vw;
    max-width: 100vw;
    flex-basis: 100vw;
    justify-self: center;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
  }
}
```

4. **Do not over-apply to desktop unless requested.** For this app pattern, mobile/tablet top tabs should be full-bleed while desktop can keep its centered page margin.
5. **Verify both sides, not just visual impression.** Acceptance checks should include `navInsetLeft === 0`, `navInsetRight === 0`, `overflowX === 0`, and `console/page error === 0` for mobile and tablet. Also check desktop remains unchanged when that is part of the contract.

## Pitfalls

- A parent `.app-shell` may be centered with margins while `.topbar` appears visually global. Fixing `.app-shell` can unintentionally change all content; prefer a scoped topbar/nav override first.
- `width: calc(100% + 24px)` plus negative margins may fix the left edge but still leave right inset because grid/flex item sizing is clamped. Promote to `100vw` with `min-width`, `max-width`, and `flex-basis` when measured geometry proves this.
- If browser checks show a selector is missing, confirm whether the tested route is actually rendering the component you edited before treating it as a style failure.
