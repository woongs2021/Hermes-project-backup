# Webapp OBD CSS micro-tuning notes

Use this for small visual refinements in Chris's Hermes webapp OBD sections, especially when he asks for proportional changes like “80% size,” “70% opacity,” or “a little more/less.”

## Pattern

1. **Translate proportional feedback into explicit CSS numbers.**
   - If Chris asks for 80% of the current avatar size, multiply both desktop and mobile CSS widths and their grid column caps.
   - If he asks for softer Signal Loop gradients, reduce only the color-mix percentages that drive the colored layer, not unrelated text, border, or layout values.
2. **Patch the narrowest selector.**
   - About OBD Chris portrait: `.profile-chris-layout` and `.profile-chris-image`.
   - Operating Map Chris card faces: data nodes in `src/extendedPanels.tsx` use `faces`; rendering uses `.obd-agent-face`.
   - Signal Loop five cards: `.signal-loop-card-step:nth-child(n) .signal-loop-detail-card` background overrides near the end of `App.css`.
3. **Avoid committing generated manifest timestamps.**
   - `npm run validate:data` can rewrite `public/data/dashboard-manifest.json`, `home-visual-set.json`, and `research-board.json` generatedAt fields. Revert them before commit unless the task is intentionally updating data manifests.
4. **Use computed browser values as proof.**
   - For avatars: assert `naturalWidth/naturalHeight`, rendered rect, square/circle radius, `object-fit`, and overflow on desktop/mobile.
   - For gradient tuning: assert the active Signal Loop subtab, five card count, computed `backgroundImage`, and overflow. Browser may serialize `color-mix()` as `rgba()`/`color(srgb ... / alpha)`, so compare the effective alpha/percent values rather than the literal source string.
5. **Deployment proof for hashed static bundles.**
   - After push, poll GitHub Actions for the exact commit and then poll live HTML for the new hashed CSS/JS bundle before running live browser QA.

## Session-proven values

- About OBD Chris profile portrait was reduced from 126×126 desktop / 115×115 mobile to about 80%: 101×101 desktop / 92×92 mobile.
- Signal Loop gradient softening moved from roughly radial 17–18%, linear 10% → radial 12–13%, linear 7% → radial 9–10%, linear 5% after Chris asked for another small reduction.
- Operating Map Chris faces reuse `public/assets/team/chris_profile.png` as 50×50 circular `.obd-agent-face` images in the first and last Chris nodes.

## Pitfalls

- Do not treat “opacity” as a global CSS `opacity` change for these cards; that would fade text and reduce legibility. Tune the gradient `color-mix()` color percentages instead.
- Do not edit only desktop values when a mobile override exists; Chris usually expects the same proportional visual change on both.
- Do not claim visual success from source diff alone; run at least one browser probe for the active subtab and computed style values.
