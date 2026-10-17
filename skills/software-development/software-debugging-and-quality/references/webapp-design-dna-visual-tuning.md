# Chris Hermes Webapp — Design DNA visual tuning lessons

Use this reference when Chris asks to tune the Design DNA / DNA Dashboard area of the Hermes webapp.

## Copy and tone
- If Chris says a phrase feels too direct, internal, or unnatural, rewrite it as human-facing product language before changing layout.
- Avoid internal instruction artifacts in UI copy such as `저장해줘`, `썸네일을 클릭하면 생성 프롬프트...`, or process-heavy labels unless Chris explicitly wants operational language.
- Avoid over-abstract phrases like `조용한 지능` when Chris says they feel unlike his language. Prefer concrete human language: the system reads situation/intent and helps turn that into better design judgment.

## Matching another tab's text rhythm
When Chris says “match this tab’s row/column/sentence rhythm,” verify computed geometry against the named source tab rather than eyeballing CSS.

Probe both source and target:
- title width
- body width
- title-to-body gap (`body.top - title.bottom`)
- title font-size
- title line-height
- title margin-bottom
- body font-size
- body line-height
- overflow

In the 2026-09 Design DNA tuning, Chris Archive overview was the source pattern:
- title/body width: `760px`
- title-to-body gap: `12px`
- desktop title font: `37.44px`
- body font: `16px`
- body line-height: `25.28px`

## Image card parity
For Design DNA's 3 large images, use the same responsive image-card height system as other tabs:
- `height: clamp(220px, 34vw, 420px)`
- `width: 100%`
- `object-fit: cover`
- `object-position: center`

If Chris asks for a flatter image presentation:
- remove image wrapper border/stroke (`border: 0`)
- remove image box-shadow
- remove decorative wrapper background gradients around Core DNA / Expression Layer (`background-image: none`, e.g. `background: var(--surface)`)

## Global title leading adjustments
If Chris asks for “4dp more line-height” on big titles, compute/verify with browser reality:
- line-height ratio change should be checked as pixels at the actual rendered font size.
- Example: `37.44px` font at `line-height: 1.09` renders `40.81px`; moving to `1.2` renders `44.93px`, about +4.1px.
- After global title changes, run desktop and mobile probes and check no horizontal overflow.

## Publishing newly saved GoYJ DNA assets
When Chris asks to “add the GoYJ image updates” and share the GitHub link:
- Treat `public/data/dna-archive.json` plus `public/assets/dna-archive/YYYY-MM-DD/` as the source of truth for DNA Dashboard publication.
- Revert unrelated generated manifest churn before commit, especially `public/data/dashboard-manifest.json`, `public/data/home-visual-set.json`, and unrelated `public/data/research-board.json` changes, unless the user explicitly asked to publish those too.
- Compare manifest image references with files under the dated asset directory and remove unreferenced public assets before committing.
- Run `npm run build:public` and a Playwright dashboard probe: switch to DNA Dashboard, assert total tile count, assert latest dated tile count, scroll lazy images into view, wait/decode, and verify latest images have `naturalWidth > 0`.
- Commit only the DNA manifest and referenced image assets. If push is rejected as non-fast-forward, `git pull --rebase origin main` and push again; this is normal when another automation/agent published meanwhile.
- After push, poll the live `data/dna-archive.json` until the new item count/latest date appears, then request each latest `imageSrc` and confirm `200` plus `image/*` before giving Chris the GitHub commit link.

## Static deployment verification pitfall
For GitHub Pages/Vite hashed assets, do not trust a generic text search in the CSS bundle. A CSS bundle may contain both old and new line-height values for different selectors. Fetch the live hashed CSS/JS and inspect the exact selector chunk, e.g. `.design-dna-unified-hero h3`, before claiming the deployed rule is live.

If browser `networkidle` hangs on GitHub Pages due to long image loads, use `domcontentloaded`, wait for the target selector, then inspect computed styles. Still report the limitation if image loading is relevant to the requested change.