# Pixel Atelier turnaround-to-runtime sprite preparation

Use when Chris approves multi-view pixel-character sheets and asks for local webapp-ready character assets without publishing.

## Outcome

Create a reusable local asset set for each approved cast member:

- five named direction PNGs: `front`, `front-three-quarter`, `profile`, `back-three-quarter`, `back`;
- transparent RGBA runtime files in `public/assets/team/atelier-sprites/<agent>/`;
- a typed public-path map (`teamAtelierSpriteMap.ts`) so the UI does not rely on filename interpolation alone;
- a deterministic verification command that checks the full expected 6 × 5 file set, PNG signature, dimensions, and RGBA color type.

Keep original sheets and generation JSON outside the public webapp. Do not commit, push, or publish until Chris explicitly asks.

## Extraction workflow

1. **Acceptance gate first.** Confirm every sheet has exactly five complete, same-scale views in the required order; inspect for missing limbs, broken faces, extra figures, text, logos, watermarks, or incompatible proportions. Reject faulty sheets rather than cropping them into runtime assets.
2. **Normalize source selection.** Use the accepted sheet for each character. If an approved character already has direction-specific sprites, normalize those into the same destination contract rather than regenerating them.
3. **Crop deterministically.** Record the source cell geometry and direction order in a local script or reproducible command. Preserve a generous vertical frame around feet and hair.
4. **Remove a uniform background conservatively.** Generated sheets frequently use a warm-cream backdrop that is near skin/light-shirt colors. Start with a very low chroma-key similarity (session-proven FFmpeg starting point: `chromakey=0xfaf6ec:0.018:0`) and visually inspect on a dark board. A broad key such as `0.13` can erase pale skin and clothing; do not accept it merely because the alpha channel exists.
5. **Use `format=rgba` and nearest-neighbor scaling.** Keep pixel edges crisp. Normalize all runtime sprites to one canvas size only after extraction, padding with real alpha.
6. **Map and integrate.** Add the direction paths to a typed sprite map. Preserve an original public portrait/pixel fallback for image-load failure. Wire only the requested interaction(s); do not turn the asset-preparation task into a broader team-scene expansion.
7. **Verify locally.** Run the asset validator, lint, TypeScript/production build, and a local preview asset smoke test. For a sampled cross-section, visually inspect sprites on a contrasting background—not the original cream backdrop—to catch alpha damage.

## Suggested public-safe contract

```ts
export const atelierDirections = [
  'front', 'front-three-quarter', 'profile', 'back-three-quarter', 'back',
] as const

export const teamAtelierSpriteMap = {
  karina: { front: '/assets/team/atelier-sprites/karina/front.png' /* ... */ },
  // approved cast only
} as const
```

## Local-only delivery checklist

- [ ] 6 approved cast members × 5 direction files are present.
- [ ] Every runtime file is an RGBA PNG with the agreed canvas size.
- [ ] Files decode and transparent pixels remain transparent.
- [ ] Typed map covers every agent and direction.
- [ ] Existing interaction resolves through the map and retains fallback behavior.
- [ ] Validator, lint, build, and local HTTP image smoke test pass.
- [ ] No Git commit, push, external backup, or deployment happened unless explicitly authorized.
