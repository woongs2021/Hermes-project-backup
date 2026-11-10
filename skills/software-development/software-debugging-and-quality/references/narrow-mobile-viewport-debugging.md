# Narrow Mobile / Fold Viewport Debugging

Use this for responsive defects reported on very narrow phones or Fold cover displays (roughly 280–320 CSS px).

## Principle
Do not treat a build or a CSS source inspection as visual completion. Confirm `document.documentElement.scrollWidth === window.innerWidth` at the target viewport, then inspect the actual rendered screen. If the reported symptom is visually ambiguous, request one screenshot before making successive speculative patches.

## Diagnostic order
1. **Viewport floor first**: inspect `html`, `body`, root app containers, and layout shells for `min-width` values (especially legacy `320px`). A `body { min-width: 320px }` guarantees horizontal overflow on a 280px cover screen.
2. **Full-bleed hacks second**: inspect `100vw`, `min-width: 100vw`, `flex-basis: 100vw`, and `calc(50% - 50vw)`. Inside centered or padded shells these can shift a header/menu past the viewport. Prefer `width: 100%`, `max-width: 100%`, `min-width: 0`, and normal margins for narrow breakpoints.
3. **Flex/grid containment**: check every ancestor between the problematic element and the page root for `min-width: 0`; grid/flex children otherwise retain intrinsic width.
4. **Intentional wide content**: tables, code, timelines, and media can retain a local scroll wrapper. Put `overflow-x: auto` on that wrapper, not the document, and confirm page-level scrolling does not occur.
5. **Unbreakable content**: long URLs, identifiers, and buttons need wrapping or truncation rules; do not hide overflow globally as a first response.

## Release gate
- Run lint, production build, and diff check.
- Deploy and verify the live asset contains the relevant CSS.
- On a real or emulated target viewport, record page `scrollWidth`, viewport `innerWidth`, and a screenshot of the affected route.
- State separately whether static/live-asset verification and rendered-device verification each passed.

## Communication
Tell Chris the exact root cause once known. Avoid saying a Fold fix is complete based only on source rules or a successful deploy. Provide the live route and ask for a screenshot only when it is needed to distinguish remaining visual defects.