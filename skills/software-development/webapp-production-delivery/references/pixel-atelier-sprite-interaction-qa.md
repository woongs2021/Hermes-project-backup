# Pixel sprite interaction QA: reusable delivery pattern

Use this reference when a production web scene combines sprite cutouts, autonomous movement, and click-to-inspect behavior.

## Asset cleanup
- For cream-background pixel character sheets, use an RGB color-key pass followed by connected-component cleanup; retain the primary character component only.
- Inspect representative directions on a dark neutral composite. Look specifically for cream/white backdrop fragments, rectangular remnants, and alpha holes through dark hair or clothing.
- Keep the character body opaque and the intended background fully transparent. Verify the complete directional asset set after regeneration.

## Motion and spatial behavior
- Model non-walkable furnishings/walls separately from the sprite canvas. Use a small grounded-footprint collision shape rather than the entire tall transparent image.
- Give each walker a minimum Euclidean separation during initial placement and destination selection; validate all initial positions against the collision map.
- When speeding up ambient motion, reduce both travel duration and dwell/cadence proportionally so the perceived rhythm—not just the CSS transition—becomes faster.

## Selection interaction
- Make each character an accessible button. On selection, freeze only that character at its rendered screen location, change it to the front-facing sprite, and show role-only copy in a bubble.
- Keep the scheduler alive for every other character. A background click must clear selection and immediately send the released character to a fresh valid destination.
- A selected bubble can clip near the scene edge. Reserve adequate walkable headroom and visually inspect the topmost possible selection; do not assume CSS positioning is enough.

## Verification sequence
1. Run asset validator, lint/type/build, and whitespace checks.
2. Run a real browser smoke test: assert walker count; observe ambient motion; select one; assert bubble and selected position remain stable; assert at least one other walker moves; click empty background; assert selection clears and movement resumes.
3. Capture a selected-state screenshot and inspect bubble legibility, sprite transparency, dispersion, and clipping.
4. After deployment succeeds, inspect the live bundle for the expected markers and repeat a minimal live-browser selection/release smoke test.
5. Stage only the feature files and regenerated assets; preserve unrelated modified files in the worktree.