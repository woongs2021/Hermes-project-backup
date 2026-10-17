# Webapp Design DNA dashboard, MD popup, and visual parity QA

Use this when updating Chris's Hermes webapp Design DNA / DNA Dashboard areas, especially manifest-backed saved assets, Markdown principle documents, and visual parity with other tabs.

## Implementation pattern

1. Keep public data and assets together:
   - Copy selected Design DNA assets into `public/assets/dna-archive/YYYY-MM-DD/`.
   - Update `public/data/dna-archive.json` so `items` references those public paths.
   - Do not publish unselected candidate sets; only Chris-selected/saved assets belong in the public manifest.
2. For a Markdown principles/guideline popup:
   - Place the `.md` under `public/docs/`.
   - Add a `publicAssetPath('/docs/<file>.md')` href constant.
   - Fetch it with `cache: 'no-store'` when the user clicks the view button.
   - Reuse the Chris Archive modal/download pattern: a view button, an `<a download>` link, modal header controls, and a `<pre>` body with `white-space: pre-wrap`.
3. For Design DNA imagery parity with other dashboard tabs:
   - Treat the three Design DNA hero images as the same class of image card as other full-width tab images.
   - Use the shared responsive image-card height pattern: `height: clamp(220px, 34vw, 420px)`, `width: 100%`, `object-fit: cover`, `object-position: center`.
   - Avoid local width caps like `width: min(100%, 860px)` or only using `aspect-ratio` if the user says the image sizing feels different from other tabs.
4. For typography parity:
   - Match the other tab hero/brief heading tone, e.g. `font-size: clamp(1.8rem, 3vw, 3.2rem)`, `font-weight: 420`, `line-height: 0.98`, `letter-spacing: -0.07em`.
   - Keep body copy at the shared dashboard body scale; verify computed size rather than eyeballing.

## Verification checklist

Run a real build first, then browser probes locally and after deploy.

- Build: `npm run build:public`.
- For desktop/tablet/mobile, check:
  - the Design DNA page renders with no horizontal overflow;
  - the three Design DNA image cards have equal heights at each viewport;
  - each image is loaded (`complete`, `naturalWidth > 0`);
  - hero and section title computed font sizes/line heights match;
  - body text computed font size matches the other tabs;
  - the Markdown popup opens, contains expected durable phrases, and the download href points at `/docs/<file>.md`.
- For GitHub Pages or hashed static deployments:
  - Poll live `index.html` until the new CSS/JS hash appears.
  - Fetch the live CSS and search for exact new rules, not just the local source.
  - Use a cache-busting query string on the page and CSS/doc/assets during verification.

## Pitfalls

- GitHub Pages can briefly serve old hashed CSS while data/assets already updated. If visual probes still show old font sizes or old image widths, first verify the live HTML asset hash and fetched CSS markers before editing again.
- Lazy-loaded images may report `currentSrc: ''` or `naturalWidth: 0` until scrolled into view or decoded. Scroll the tiles into view and await `img.decode()` before treating image loading as failed.
- Re-running broad manifest-generation scripts can introduce unrelated timestamp or research-board diffs. Revert unrelated manifest changes before committing a focused visual/layout fix.
