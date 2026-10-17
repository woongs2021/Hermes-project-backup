# Outdoor mockup version reordering + replacement lessons

Use when Chris asks to reorder or replace versioned Outdoor Mockup child sets in Design DNA → DNA Brand Asset → Midjourney + Mockup, especially A/B lanes with labels like `A-1`…`A-5` or `B-1`…`B-4`.

## Reordering visible versions

- Treat Chris's request as a visible sequence/label change unless he explicitly asks to rename physical files.
- Preserve existing asset file paths and internal historical IDs when possible; change manifest order, visible `title`, item titles, `displayOrder`, and short descriptions.
- Example: “B1 B3 B4 B2 순서로, 넘버링은 1234” means:
  - old `B-1` → visible `B-1`
  - old `B-3` → visible `B-2`
  - old `B-4` → visible `B-3`
  - old `B-2` → visible `B-4`
- After reordering, verify via live manifest rather than relying on local JSON or push success.

## Replacing one version while moving another

When Chris says “A-2를 A-5로 변경하고 현재 A-5는 삭제, 원래 A-2 자리에 새 그래픽 합성”:

1. Generate the new replacement set under a new stable manifest/example ID or new asset root to avoid path ambiguity.
2. Move the old visible `A-2` entry to visible `A-5` by retitling its example and items.
3. Remove the current visible `A-5` from the manifest. Do not delete original files unless explicitly requested; removing from manifest is enough for the webapp.
4. Insert the newly generated replacement into visible `A-2`.
5. Rebuild the lane order explicitly, e.g. `[A-1, new A-2, A-3, A-4, moved old A-2 as A-5]`.

## Quality gate for multi-board item 5

For A/B item `*-5` board/booklet sets:

- Contact-sheet QA must check that all intended large surfaces are actually printed. A board left mostly white is a failure even if the other board looks good.
- If one big board is blank/under-composited, regenerate only item 5 with stronger direction and prompt language: “BOTH large boards must be visibly printed; no large blank white board left unprinted.”
- Generate two item-5 candidates and choose the one that best balances:
  - both boards visibly printed,
  - physical seam/step preserved,
  - non-continuous crops across the seam,
  - no barcode/panorama alignment across adjacent boards.
- Update the manifest to reference only the selected final file.

## Candidate-file hygiene

- Keep provider logs and local candidate/contact-sheet files outside the public webapp when possible.
- If public candidate files are accidentally committed, remove unused candidates in a follow-up cleanup commit so the public asset tree contains only the manifest-referenced final assets.
- The manifest is the source of truth for what the webapp shows, but public asset clutter makes future QA harder.

## Deployment QA

- For GitHub Pages, push/build completion is not sufficient. Verify:
  - workflow run completed success,
  - live `brand-mockup-assets.json` has the intended order/source graphics,
  - every new/referenced live asset URL returns `200 image/png` at expected dimensions,
  - Playwright page probe has no console errors and no horizontal overflow.
- Pages runs may appear long-running; if a newer commit cancels the old run, keep checking the latest run and live manifest before declaring completion.
