# GitHub Pages webapp UI polish and live verification

Use this reference when Chris asks for small visual/copy/layout changes to the Hermes webapp and wants them deployed to GitHub Pages.

## Pattern

1. Treat visual polish as a working-artifact task, not a plan: edit the app, run build checks, deploy, then verify the live page.
2. For Chris-facing copy, avoid language that sounds like an internal correction/changelog (for example “not a growth score”). Rewrite as marketing/product-intro copy that still preserves factual caution and does not overclaim Chris’s personal growth.
3. When graph copy implies growth, define the measured axis clearly. If the data is question/log maturity rather than Chris’s subjective growth, label it as structure, operating language, maturity checkpoint, or question progression.
4. For dashboard graph legibility, prefer thin strokes and modest emphasis. Chris has preferred 1px graph axis/line/guide strokes, small axis labels, small active-question titles, and horizontally spacious point placement on desktop.
5. If desktop feels crowded, do not assume mobile-only layout is enough: verify desktop separately and consider a single-column stacked sequence even on desktop.
6. For GitHub Pages + Vite public assets, avoid double-prefixing base paths. If a helper adds `import.meta.env.BASE_URL`, guard paths that already start with the base URL before passing them through again.
7. For mobile top navigation, verify the actual computed top position. Chris prefers the topbar/tabs visually flush to the top edge on mobile rather than floating below with a margin.
8. For OBD Operating Map Chris cards, keep Chris visually distinct but restrained:
   - add an explicit class such as `.is-chris` instead of relying on fragile `nth-child` selectors;
   - use the same blue accent family as the Signal Loop Chris/source card for Chris card background tint, border, title text, and step number text;
   - make the Chris title slightly larger and heavier than other operating-card titles;
   - avoid heavy number badges unless the user explicitly asks for badge treatment.
9. When a layout uses mapped wrapper elements, put grid-area / step classes on the wrapper, not only the nested `article`, so CSS grid placement and connector arrows remain stable.
10. Before adding new layout rules, search for later follow-up/override blocks in the same CSS file. In Chris's webapp, older section-specific rules can be superseded by later simplified-layout rules; if you add grid-area or card styling before a later override, it may be partially overwritten and cause mobile overlap. Put the final correction after the last relevant override, or explicitly reset wrapper `grid-area: auto` in the final block.
11. For Visual Archive hero image replacement, see `references/visual-archive-hero-image-replacement.md`. Preserve the existing public asset path when possible, update the alt text, and verify both direct asset bytes and browser image load state.
12. If Chris reports black bands/letterboxing in a hero image frame, check for generic `.content-card` padding or later CSS overrides before changing the source image. Verify frame fill by comparing rendered image rect to frame rect on desktop and mobile; the image rect should cover the frame in both dimensions.

## Verification checklist

- `npm run validate:data`
- `npm run lint` — distinguish existing warnings from new errors.
- `npm run build:public`
- `git diff --check`
- Local or live browser smoke with Playwright for computed styles when layout is the task:
  - graph stroke widths
  - graph point spread and order
  - active title font size
  - image `complete`/`naturalWidth`
  - mobile topbar `top` and app margin
  - UI element counts, vertical order, overflow, unique colors, badge/background/border styles when those are the requested visual changes
- If Chris says not to capture screenshots, do not create or send screenshots. Verify with live URL, asset markers, DOM counts, and computed styles instead.
- Push branch and `main`, then verify GitHub Pages live assets and page behavior before reporting completion.
  - mobile topbar `top` and app margin
- Respect Chris's requested review mode: if he says not to capture screenshots, do not create or send screenshots. Verify visually-relevant changes with live asset markers plus DOM/computed-style probes instead.
- Push branch and `main`, then verify GitHub Pages live assets and page behavior before reporting completion.
