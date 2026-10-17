# Iterative webapp legibility and GitHub Pages smoke pattern

Use when Chris gives iterative feedback on the Hermes/OBD webapp UI, especially About OBD graphs, Research detail panels, profile imagery, and GitHub Pages deployment.

## Session-proven lessons

- Treat visual comments as product requirements. If Chris says a graph feels too steep, crowded, or not personally felt, change the semantics and visual encoding rather than defending the data.
- For OBD/Son graph copy, avoid phrasing that sounds like an internal fix note, e.g. “not a growth score.” Use marketing-facing value copy instead, e.g. “questions make OBD a clearer operating language,” while still making axis labels precise.
- Do not imply Chris personally grew unless the data is self-reported by Chris. If the underlying data is Son questions/logs, label the graph as question structure, operating maturity, checkpoints, or operating language.
- If a desktop graph/copy/detail area feels complex, use sequential vertical layout even on desktop: intro → graph → active detail/question → archive/list. Validate with computed layout: card grid should be one column and child top positions should increase sequentially.
- For graph legibility, verify real computed stroke widths. Chris may perceive lines as heavy even if numerically small; use direct CSS values such as `stroke-width: 1px` for SVG axes/lines/guides when asked.
- For interactive graph point spacing on desktop, combine wider x-values (for example near 6% through 94%) with reduced stage/layer inset so points use the available width.
- For dense Research 1-pick detail copy, render synthesized detail as multiple paragraphs rather than one long `<p>`. Split by decision function: core claim/validation, Chris relevance, source/access/local/duplicate context, and decision/judgment frame. Add paragraph gap and comfortable line-height.
- For Vite on GitHub Pages, public assets referenced from React need base-aware paths. If some paths are already base-prefixed and then passed through a helper like `toAppAssetSrc`, guard against double-prefixing with `path.startsWith(import.meta.env.BASE_URL)`.

## Verification checklist

- Run `npm run validate:data`, `npm run lint`, `npm run build:public`, and `git diff --check` before commit.
- For Pages deployments, push the feature branch and `main`, then wait for the new hashed JS/CSS assets to appear at the Pages URL.
- Use a browser/Playwright smoke test when the issue is visual/layout/image-related:
  - image fix: assert relevant `<img>` elements are `complete` and `naturalWidth > 0`.
  - graph layout: assert computed grid columns, SVG `strokeWidth`, point spread, and active question font size.
  - mobile sticky topbar: assert `.topbar` top is `0px` and its bounding rect top is `0`.
  - research detail readability: assert paragraph count, paragraph gap, font size, and line-height.
- If a local Vite preview process is used, start it as a tracked background process and kill it after smoke testing. A later `exit code -15` notification is expected when the agent terminated the preview deliberately.
