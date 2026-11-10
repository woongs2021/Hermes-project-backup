# Smooth turnaround sprite extraction

Use this when a generated five-view non-pixel character turnaround must become directional PNG sprites for a small interactive scene.

## Problem to guard against

A generated sheet can have uneven spacing. A fixed five-column crop can silently include a narrow fragment of the adjacent pose—especially in front-three-quarter or back-three-quarter views. At scene size this looks like a broken limb, a vertical ghost line, or a doubled silhouette.

## Safe extraction procedure

1. Generate or acquire a sheet with exactly five complete figures ordered: `front`, `front-three-quarter`, `profile`, `back-three-quarter`, `back`.
2. Remove the uniform sheet background conservatively. Do not use an aggressive color-key tolerance: warm ivory backgrounds can be close to skin and light fabric colors.
3. Within each expected directional cell, identify connected opaque components and retain **only the largest component** as the character. Treat all smaller disconnected components as neighbor-pose residue or generation noise.
4. Crop to that component's bounding box. Do not use the original equal-width cell as the final crop.
5. Normalize every retained figure onto the app's shared transparent canvas. Preserve aspect ratio; scale by a common figure height, then center with transparent padding. Never stretch profile poses to match front-pose width.
6. Audit all five directions on a dark test background. Explicitly inspect both three-quarter directions for slivers, doubled bodies, cut limbs, and inconsistent apparent scale.
7. Validate the runtime contract (all required directional paths, identical PNG dimensions, RGBA), then test actual keyboard/pointer-driven direction changes in the browser.

## Acceptance checks

- No opaque pixels from an adjacent pose appear in any direction.
- Faces and hair preserve their light tones; no dark holes caused by over-removal.
- Each figure is intact from hair to shoes and directionally readable.
- Every generated sprite is transparent RGBA at the declared shared dimensions.
- At least one live directional interaction test confirms the new image has loaded after the direction state changes.
