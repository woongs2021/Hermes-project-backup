# Chris Archive Webapp Dashboard QA Notes

Use when updating Chris's GitHub Pages webapp, especially the Chris Archive thumbnail dashboard or modal detail view.

## Durable patterns

- Treat visual polish requests as implementation + live verification tasks, not just CSS edits.
- For Chris Archive, verify responsive behavior with browser-computed values, not screenshots alone:
  - desktop around 1366px: archive grid should resolve to 6 columns when requested.
  - tablet around 834px: archive grid should resolve to 3 columns when requested.
  - mobile around 390px: archive grid can remain 2 columns unless Chris asks otherwise.
- For modal sizing on tablet, avoid fixed two-column minimums that exceed the viewport. Prefer `minmax(0, 1fr)` columns and a viewport-aware modal width such as `width: min(92vw, 820px)` inside tablet media queries.
- For modal overlays, avoid relying on blur-only backdrops. Use theme-specific base layers so text remains legible:
  - light mode: bright/warm high-opacity backdrop + subtle blur.
  - dark mode: dark high-opacity backdrop + subtle blur.
- For scrollbars that should only be visible while scrolling, avoid changing `scrollbar-width` between `none` and `thin`; that can change layout width and make content jump. Instead:
  - reserve scrollbar space from the start with `scrollbar-gutter: stable`.
  - keep `scrollbar-width: thin` but set `scrollbar-color: transparent transparent` by default.
  - on an `is-scrolling` class, change only the thumb color.
  - for WebKit, keep the scrollbar width constant and toggle only `::-webkit-scrollbar-thumb` background.
  - use a short timer, e.g. 800–900ms, to remove `is-scrolling` after scroll stops.
- After deduping archive images, validate both data and assets:
  - manifest item count equals rendered tile count.
  - every `imageSrc` returns HTTP 200 and an image content type.
  - exact duplicate hashes are zero.
- When verifying a freshly deployed Pages CSS fix, do not rely only on raw minified CSS string matching. Vite/minifiers may rewrite declarations such as `overflow-x: hidden; overflow-y: auto;` into compact shorthands like `overflow: hidden auto`, or preserve `transparent` instead of `#0000`. Use string polling only to detect approximate deployment freshness, then do a Playwright computed-style smoke test for the real acceptance criteria.

## Git/GitHub Pages pitfalls

- Chris's webapp `.gitignore` may ignore filenames containing secret-like words such as `token`. If a public image filename includes such a word, the asset may exist locally but not be tracked/published. Rename the public asset to a safe filename and update the manifest instead of forcing ignored files.
- When publishing directly after user approval, push a focused feature branch first, then update `main`, and verify the live Pages URL after the deployment cache changes.
- For downloadable Markdown documents with Korean user-facing filenames, prefer an ASCII-safe public URL path such as `public/docs/hermes-design-system.md` and set the link `download` attribute to the Korean filename (e.g. `헤르메스디자인시스템.md`). Verify the actual Pages doc URL returns 200; do not rely on the Korean/non-ASCII path alone.
- When the `Design DNA` tab is reorganized from Chris Archive evidence, verify all subtabs, not just the archive grid: expected compressed cluster count, prompt-package card count, explanatory `Chris Design Archive` copy, no desktop/tablet/mobile horizontal overflow, and unchanged Chris Archive manifest/doc popup behavior. If React panels are replaced, run the TypeScript build to catch unused constants before pushing.

## Suggested live smoke checks

Use Playwright or an equivalent browser probe to verify:

- no page errors or failed image responses.
- grid column count at desktop/tablet/mobile breakpoints.
- modal `left >= 0` and `right <= viewport width`.
- modal `overflow-x` is hidden and vertical scrolling works.
- before/during/after scroll: modal bounding width and `clientWidth` remain unchanged.
- scroll indicator behavior: class toggles on during scroll and off after the debounce period without layout shift.
