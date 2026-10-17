# Design DNA Brand Mockup Collection Grouping

Use when Chris asks to add multiple raw mockup reference sets under **Design DNA → DNA Brand Asset**.

## Current grouping pattern

- Keep **DNA Brand Asset** as the top-level Design DNA section.
- Inside it, use a two-level navigation structure:
  1. Top level:
     - `Brand Mockup Assets`
     - `Midjourney + Mockup`
  2. Under `Brand Mockup Assets`, render one sub-tab per raw mockup collection from `public/data/brand-mockup-assets.json` `collections[]`.
     - Examples: `Coffee Mockup Assets`, `Outdoor Mockup Assets 1`, `Outdoor Mockup Assets 2`.
- Do not let every raw collection compete with `Midjourney + Mockup` at the same top level once there are multiple collections; it makes the IA feel flat/noisy.
- `Midjourney + Mockup` should remain a sibling of `Brand Mockup Assets`, not a child of the raw mockup collection group.

## Manifest pattern

- Raw/reference mockup assets belong in `collections[]`.
- Synthesized/pattern-applied examples belong in `examples[]`.
- For each new raw collection:
  - append a new collection object with `id`, `title`, `created`, `status`, `description`, and `items[]`.
  - store images under `public/assets/dna-brand-assets/mockup/<collection-id>/YYYY-MM-DD/`.
  - preserve original image geometry; do not synthesize/crop unless Chris asks.

## UI implementation pattern

- Use one state for the top lane, e.g. `activeBrandAssetLane: 'brandMockup' | 'midjourneyMockup'`.
- Use a second state for the active raw collection id, e.g. `activeBrandMockupCollectionId`.
- If the active collection id is missing after manifest load, fall back to `collections[0]`.
- Render collection sub-tabs only when top lane is `Brand Mockup Assets`.
- Card tiles should remain clickable and open the existing DNA Brand Asset detail modal.

## Verification checklist

- Build with `npm run build:public`.
- Verify local and live desktop/tablet/mobile:
  - top tabs show `Brand Mockup Assets` and `Midjourney + Mockup`.
  - `Brand Mockup Assets` shows collection sub-tabs for all manifest `collections[]` entries.
  - each collection shows the expected item count and all images load with nonzero natural dimensions.
  - `Midjourney + Mockup` still renders all `examples[]` collections and is not nested under raw mockup assets.
  - no horizontal overflow and no console errors.
- After push, poll Pages until the new JS hash is served before running live Playwright checks.
