# Webapp body-tab typography and animated underline

Use this reference when Chris asks to tune body-local dashboard tabs such as Personal AX / Corporate AX child tabs.

## Session-proven pattern

For body-local tabs (`OBD Map`, `Research`, `Visual Archive`, `Chris Archive`, `Design DNA`), keep the global header untouched and tune only `.workspace-tab-*` controls.

- If Chris asks to increase body-tab type by a percentage, verify the old computed value first. In this session, old child-tab font size was `15.04px`; 130% became `19.552px` via `font-size: 1.222rem`.
- For active underline that moves naturally between tabs, prefer a single nav-level indicator element over individual `::after` lines on every button.
- Add one indicator element inside the nav, e.g. `<span className="workspace-tab-indicator" aria-hidden="true" />`.
- Keep a `ref` on the nav. On active tab change and resize, read the active button `getBoundingClientRect()` and set CSS variables on the nav:
  - `--workspace-tab-indicator-left`
  - `--workspace-tab-indicator-width`
  - `--workspace-tab-indicator-opacity`
- CSS should absolutely position the indicator at the nav bottom and animate `left`, `width`, and `opacity`.
- Add `prefers-reduced-motion: reduce` to disable animation.

## Why this pattern

- A single moving underline avoids layout jitter that can happen when each button owns its own pseudo-element.
- The underline follows the exact rendered text/button width after responsive wrapping, font loading, or viewport changes.
- The indicator does not change button height if it is absolutely positioned and the nav reserves bottom padding.

## QA checklist

Run browser/computed checks on desktop, tablet, and mobile:

- Body tab font size equals the intended computed value (e.g. `19.552px` for 130% of `15.04px`).
- Exactly one `.workspace-tab-indicator` exists per visible body tab nav.
- Indicator width matches active button width within ~1px.
- Indicator left matches active button left within ~1px.
- Indicator transition includes `left`, `width`, and `opacity`.
- Hash/active state changes correctly after clicking each child tab.
- `document.documentElement.scrollWidth - clientWidth === 0`.
- No console/page errors.

## Pitfalls

- Do not add the underline to top-level parent tabs unless Chris explicitly asks; this request applied only to body-local child tabs.
- Do not use per-button active underline if Chris has recently complained about tab/content jitter; use the moving indicator pattern.
- In Vite/GitHub Pages deployments, asset string search can be unreliable after minification because variable names disappear. Prefer live browser computed QA for geometry and transitions.
