# DNA Brand Asset outdoor mockup collection tabs

Use when Chris asks to add outdoor/mockup reference images under **Design DNA → DNA Brand Asset** as a named tab/collection.

## Durable lesson

The DNA Brand Asset area should not be hardcoded to a single Coffee collection. Mockup reference sets belong in `public/data/brand-mockup-assets.json` under `collections[]`, and the React UI should render those collections as source tabs automatically. This lets later sets such as `Outdoor Mockup Assets 1`, `Packaging Mockup Assets`, etc. appear without rewriting the UI each time.

## Intake pattern

1. Treat user-supplied outdoor mockup images as **mockup reference assets**, not Midjourney DNA motif assets and not synthesized `Midjourney + Mockup` examples.
2. Store originals unchanged:
   - Local archive: `/opt/data/dna-brand-assets/mockup/<collection-id>/YYYY-MM-DD/`
   - Public assets: `public/assets/dna-brand-assets/mockup/<collection-id>/YYYY-MM-DD/`
3. Append or replace one collection in `public/data/brand-mockup-assets.json`:
   - `id`, `title`, `created`, `status: mockup_moodboard_saved`, `description`
   - `items[]` with `id`, `title`, `description`, `imageSrc`, `assetHash`, `width`, `height`
4. Use descriptive titles that name the surface/object rather than the upload sequence, e.g.:
   - `Outdoor Paper Stack On Concrete`
   - `Single Card On Metal Grid`
   - `Vertical Fabric Banner On Stone Wall`
   - `Framed Wall Poster On Stone Facade`
   - `White Board Set With Pebble Background`
   - `Hanging Outdoor Sign On Glass Facade`

## Webapp implementation pattern

If the UI is still hardcoded to Coffee mockups, refactor it once:

- Keep `activeBrandAssetSource` as a string collection id, defaulting to `coffee-mockup-assets`.
- Derive:
  - `brandMockupCollections = brandMockupAssets.collections`
  - `activeBrandMockupCollection = brandMockupCollections.find(c => c.id === activeBrandAssetSource) ?? brandMockupCollections[0]`
- Render `brandMockupCollections.map(...)` as DNA Brand Asset source tabs.
- Keep `Midjourney + Mockup` as the separate synthesis lane using the sentinel id `midjourneyMockup`.
- For the active collection, render the existing mockup tile grid and detail modal with `lane: 'Mockup'`.

## Verification checklist

- `python3 -m json.tool public/data/brand-mockup-assets.json`
- `npm run build:public`
- Local browser QA for desktop/tablet/mobile:
  - DNA Brand Asset shows the new collection tab.
  - The tab count matches the manifest item count.
  - Every image has nonzero natural dimensions.
  - Clicking a tile opens the detail modal.
  - No horizontal overflow and no console errors.
- After push, poll live Pages until the live manifest hash matches local; verify each new image URL returns `200 image/*`.
- Repeat live browser QA on desktop/tablet/mobile.

## Pitfalls

- Do not add outdoor mockup references to the Midjourney rail unless Chris explicitly says they are Midjourney outputs for DNA Dashboard.
- Do not put mockup reference assets into `examples[]`; reserve `examples[]` for synthesized Midjourney+Mockup outputs.
- Do not keep adding one-off hardcoded tabs in React; the tab list should come from `collections[]` so later mockup sets stay cheap to add.
