# Design DNA outdoor mockup collection intake

Use when Chris sends batches of outdoor/lifestyle mockup reference images and asks to add them under **Design DNA → DNA Brand Asset** as a new tab such as `Outdoor Mockup Assets 1`, `Outdoor Mockup Assets 2`, etc.

## Routing

- These are **DNA Brand Asset mockup reference collections**, not Chris Archive, not DNA Dashboard GPT/Image assets, and not Midjourney manual motif rail assets.
- Store each batch as a separate collection in `public/data/brand-mockup-assets.json` under `collections[]`.
- Use collection IDs like `outdoor-mockup-assets-1`, `outdoor-mockup-assets-2` and titles like `Outdoor Mockup Assets 1`.
- Preserve the source images as provided. Do not crop, synthesize, upscale, or remaster unless Chris explicitly asks.

## Storage pattern

For collection `outdoor-mockup-assets-N` on date `YYYY-MM-DD`:

- Local archive: `/opt/data/dna-brand-assets/mockup/outdoor-mockup-assets-N/YYYY-MM-DD/`
- Public assets: `public/assets/dna-brand-assets/mockup/outdoor-mockup-assets-N/YYYY-MM-DD/`
- Manifest: `public/data/brand-mockup-assets.json`

Each `items[]` entry should include:

- `id`: `outdoor-mockup-assets-N-01`, etc.
- `title`: concise object/surface name, e.g. `White T-Shirt On Black Fence`.
- `description`: user-facing Korean description of visible object/surface, light/material/context, and brand-use role.
- `imageSrc`, `assetHash`, `width`, `height`.

## UI implementation lesson

- The webapp should render DNA Brand Asset mockup tabs from `brandMockupAssets.collections`, not hardcode only Coffee Mockup Assets.
- Keep `Midjourney + Mockup` as a separate manual synthesis tab after the collections.
- Once collection-driven rendering is in place, adding Outdoor Mockup Assets 2+ should require only manifest/assets updates, not React changes.

## QA checklist

1. Validate JSON: `python3 -m json.tool public/data/brand-mockup-assets.json`.
2. Run `npm run build:public`.
3. Verify local UI at desktop/tablet/mobile:
   - DNA Brand Asset shows the new tab.
   - Active tab title matches the collection title.
   - Tile count equals 6 or the batch size.
   - All tile images eventually load with nonzero `naturalWidth`/`naturalHeight`.
   - Clicking a tile opens the detail modal with the same image and metadata.
   - `overflowX` is 0 and there are no console errors.
4. After push, poll GitHub Pages until the live manifest hash matches local, then verify every new `imageSrc` returns `200 image/*`.
5. Re-run live UI verification. If Playwright initially reports `naturalWidth: 0` right after deploy, wait/scroll all lazy images into view and re-check before declaring a failure; the URLs may already be valid while browser image decode is still catching up.

## Naming examples

- Paper/tag: `Held Paper Tag On Shadow Wall`
- Tote: `Large Tote Bag On Shoulder`, `Tote Bag On Chair Outdoor`
- Mobile: `Phone Screen On Ribbed Glass`
- Apparel: `White Bucket Hat On Stand`, `White T-Shirt On Black Fence`
- Outdoor signage/boards: `Hanging Outdoor Sign On Glass Facade`, `Framed Wall Poster On Stone Facade`
