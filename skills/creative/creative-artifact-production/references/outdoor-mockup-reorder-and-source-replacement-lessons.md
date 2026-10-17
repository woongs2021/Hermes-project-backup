# Outdoor Mockup A/B reordering and source replacement lessons

Use when Chris asks to reorder `Outdoor Mockup A/B` child sets, renumber visible labels, or replace a version such as `A-2` with a different Midjourney source while preserving the rest of the lane.

## Reordering / visible renumbering

- Treat the manifest as the source of truth for visible order and labels. Do not rename binary asset files just to reorder a lane; keep existing asset paths stable and update titles/descriptions/display metadata.
- When Chris says “B1 B3 B4 B2 순서로 변경하고 넘버링은 다시 1234,” map old versions to new visible labels explicitly before editing:
  - old B-1 → new B-1
  - old B-3 → new B-2
  - old B-4 → new B-3
  - old B-2 → new B-4
- Apply the same mapping to item titles (`B-2-1 … B-2-6`) and short Korean descriptions. Preserve IDs and image paths unless a new generated set is replacing the content.
- After editing, verify the manifest order by fetching/parsing live `brand-mockup-assets.json`; UI screenshots can lag or lazy-load.

## Replacing one version with a different Midjourney source

- For a request like “A-2 전체를 미드저니 2로 변경,” generate a new example ID/directory instead of overwriting the previous generated asset directory. This avoids browser/GitHub Pages cache confusion and preserves rollback options.
- Remove the old replacement example from the **manifest** (e.g. previous A-2/MJ29), but do not spend time deleting historical asset folders unless Chris explicitly asks. The public UI should point only to the current chosen set.
- Keep neighboring visible versions stable: if only A-2 changes, A-1/A-3/A-4/A-5 should retain their current visible labels and items.
- For `A-*-5` board/booklet items, run separate candidate generation and contact-sheet QA if the first full-set output has weak seam/card application. This item is structurally sensitive and can deserve extra candidates even when the other five images are acceptable.

## QA selection cues from the 2026-10-08 session

- Chris may reject an otherwise clean A-2 set if the overall source choice feels aesthetically wrong. Swapping the entire A-2 source is valid; do not over-defend the previous source.
- For Midjourney source trials, keep short status updates factual: source confirmed → generation running → contact sheet QA → manifest/build/live verification.
- When a contact sheet filename is stale because it was copied from a previous script, explain only if needed; verify the actual generated filenames and manifest source fields instead.
- In QA, prefer candidates that satisfy the user’s exact complaint over technically interesting alternatives. Example: for A-2-5, reject a candidate where the small card looks like a different striped card, even if the rear books are clean.

## Verification checklist

1. Validate JSON (`python3 -m json.tool`).
2. Run `npm run build:public`.
3. Commit only the manifest and final selected images when possible; remove accidental candidate files from git if they were staged/pushed.
4. Verify GitHub Pages run status. If a run is genuinely stuck behind an older in-progress run, a cache-busting empty commit can retrigger; but first check run/job status and live manifest.
5. Verify live manifest order/source fields.
6. Verify direct asset URLs return `200 image/png` and expected dimensions (`2496×1664` for these mockups).
7. Run a lightweight Playwright probe for console errors, horizontal overflow, and final image natural dimensions.
