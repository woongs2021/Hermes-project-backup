# Photo-derived pixel avatar pipeline

Use this when a web product needs recognizable pixel portraits that are strictly derived from already-approved public profile images.

## Contract

- Treat the source-to-sprite mapping as product data, not an implicit filename convention. Keep a typed map with exactly the approved identities, source asset paths, and output sprite paths.
- Never add external, generated, or replacement faces. Keep the original thumbnail as the runtime fallback if a sprite fails to load.
- Avoid reading runtime/private operational data while rendering an avatar surface.

## Deterministic generation

A portable FFmpeg flow is sufficient for small static sprites:

1. Center-crop the source to a square.
2. Apply only restrained grading when needed for a coherent set.
3. Downsample to a small grid (for example 16×16) with nearest-neighbor.
4. Quantize to a restrained palette (for example <=12 colors) with no dithering.
5. Upscale with nearest-neighbor to a compact shipped PNG (for example 80×80).

Keep the generator in `scripts/` and expose an npm command. Store generated sprites under a role-scoped public path such as `public/assets/team/pixel/`.

## Verification

Automate checks for:

- the exact expected identity set and one-to-one unique source/output mappings;
- approved public source paths only;
- output existence, PNG signature, dimensions, palette/color ceiling, and decoder readability;
- reproducibility: regenerate and compare hashes when practical.

For UI integration, verify the emitted image path respects the app base URL and that `onError` swaps to the approved source thumbnail without a retry loop. Add `image-rendering: pixelated` / `crisp-edges` for scaled display.

Finally, make a labeled contact sheet or otherwise inspect all sprites visually. A successful decoder check is not enough: look for empty/corrupt tiles, indistinguishable portraits, or an overly muddy palette.

## Scope control

Keep avatars separate from the scene. Do not silently introduce office layout, movement, interactions, or a new data surface in the avatar phase. Those require their own implementation and accessibility review.
