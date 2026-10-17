# Webapp tab-switch jitter QA pattern

Use this when Chris reports that content “덜컹거린다” while switching tabs or scrolling inside a dashboard/webapp.

## Durable lesson

Perceived tab jitter often comes from sibling sections having different computed layout primitives, not from scrolling itself. In the Hermes Project Webapp case, Chris Archive and Design DNA shared a Corporate AX parent, but only `.chrisArchive-workspace` had a custom `gap: clamp(...)`; Design DNA inherited the base `.workspace { gap: 28px; }`. At tablet width this created ~21px movement in the content start position when switching tabs.

## Diagnosis steps

1. Reproduce in a real browser at desktop, tablet, and mobile widths.
2. Measure geometry before/after switching the sibling tabs:
   - `navTop`
   - `headerTop`
   - first content/shell `top`
   - `scrollY`
   - computed `gap` on the shared workspace container
   - horizontal overflow
3. If `scrollY` stays fixed but element `top` changes, treat it as layout metric drift, not scroll anchoring.
4. Compare computed styles between the two sibling workspace roots, especially `gap`, margin, padding, min-height, and breakpoint overrides.

## Fix pattern

- Stabilize the shared parent primitives for the sibling tabs, for example:
  - set the same `gap` on both sibling workspace roots;
  - remove negative tab-nav margins that can change calculation paths;
  - give the shared header/description block a consistent `min-height` when titles/descriptions differ;
  - use `overflow-anchor: none` only as a secondary guard, not the primary fix.
- Avoid fixing only one tab; patch both siblings and dark-theme selectors if the app has theme-specific overrides.

## Verification target

Run a Playwright probe that switches A → B → A and asserts:

- old/removed copy is absent if the task also changed content;
- new card/count/content is present;
- `workspaceGap` is the same for both tabs;
- `navTop`, `headerTop`, and first content `top` deltas are `0px` or within a tiny tolerance (≤0.5px);
- `scrollY` deltas are `0`;
- desktop/tablet/mobile overflow is `0`;
- no console/page errors.

For hosted static apps, also prove the deployed HTML points to the new hashed CSS/JS and fetch those assets to confirm the new class/copy before claiming the live site is updated.
