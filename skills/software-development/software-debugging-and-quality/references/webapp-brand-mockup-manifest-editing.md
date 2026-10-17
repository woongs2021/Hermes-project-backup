# Webapp Brand Mockup Manifest Editing

Use this when Chris asks to remove, rename, reorder, or renumber DNA Brand Asset / Midjourney + Mockup items in the Hermes webapp.

## Key lessons

- The user-facing mockup number is usually in `public/data/brand-mockup-assets.json` titles, not necessarily in the internal `id`.
  - Example: visible `Outdoor Mockup A-5` may have an id like `outdoor-mockup-example-a-09`.
  - Resolve the target by rendered/manifest `title` and `tabId`, not by assuming `a-05` ids exist.
- For Outdoor Mockup A/B, distinguish lanes:
  - `Brand Mockup Assets` shows original reference mockup collections.
  - `Midjourney + Mockup` shows synthesized example sets such as `Outdoor Mockup A-1` through `A-5`.
  - If verifying a synthesized set, click `Design DNA` → `Brand Asset` → `Midjourney + Mockup` → `Outdoor Mockup A` before reading visible titles.
- When renumbering a visible set, update display text (`title`, item `title`, and any public-facing description text that mentions the number). Do not rename image files/paths unless the files are actually moved; preserving paths avoids broken assets.
- If removing a set, delete the entire example object and verify the remaining examples count and tile count. For 5 sets × 6 images, expected tile count is 30.

## Verification checklist

1. Parse `public/data/brand-mockup-assets.json` and list examples filtered by `tabId` (for Outdoor Mockup A: `outdoor-mockup-1`). Confirm the target visible titles and counts before editing.
2. After editing, run:
   - `npm run validate:data`
   - `npm run lint`
   - `npm run build:public`
   - `git diff --check`
3. Local browser smoke check using Playwright:
   - Navigate to `#design-dna`.
   - Click `.design-dna-section-tab` containing `Brand Asset`.
   - Click `.dna-dashboard-source-tab` containing `Midjourney + Mockup`.
   - Click `.midjourney-mockup-subtabs .brand-mockup-subtab` containing the relevant group (`Outdoor Mockup A`, etc.).
   - Assert visible collection titles match the requested numbering, removed titles are absent, tile count matches expectation, images load (`naturalWidth > 0`), console/page errors are empty, and horizontal overflow is 0.
4. After push, do not stop at commit success. Verify deployment:
   - Fetch raw GitHub `main` JSON to confirm the repo has the edit.
   - Fetch live Pages JSON with a cache-busting query and compare SHA/length or manifest titles.
   - If live Pages initially serves stale JSON, check GitHub Actions deploy status and response headers (`last-modified`, `etag`, `cache-control`, `age`, `x-cache`) before concluding failure; GitHub Pages data files can lag briefly even after push.
5. Run a final live UI Playwright check in the correct lane. Report the final visible titles, tile count, image load status, console/page errors, overflow, commit hash, and URL.
