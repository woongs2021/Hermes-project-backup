# Outdoor mockup selected-item surface-fit revision

Use when Chris says specific numbered items inside an already-published Outdoor Mockup A/B version look poorly composited, e.g. “A-4-2, A-4-3, A-4-5가 이상하게 합성된 것 같아. 목업에 잘 들어가도록 다시 재생성해줘.”

## Trigger

- Only a subset of items in a versioned mockup set are criticized.
- The issue is not the source motif choice, but that the graphic does not sit correctly on the physical mockup surface.
- Typical cases:
  - single card on metal grid: graphic bleeds beyond or does not align to the tilted card;
  - vertical fabric banner on wall: graphic leaks to wall/window/rod, or fabric material/folds are lost;
  - board/booklet set with small front card: card/booklet crops look foreign, blank, continuous, or physically unseparated.

## Workflow

1. **Do not regenerate the whole version first.** Keep accepted items unchanged and regenerate only the criticized item numbers.
2. **Inspect the original clean mockup for each criticized item.** Identify the exact physical surface that should receive the graphic and what must remain untouched.
3. **Build stricter direction images.** Avoid broad brightness masks for these items:
   - card-on-grid: polygon-mask only the tilted card; preserve all metal bars/grid/background;
   - fabric banner: polygon-mask only the hanging textile rectangle; preserve stone wall, windows, rods, shadows;
   - board/booklet + small card: polygon-mask each physical surface separately; enforce different crops of the same motif and visible seam/step.
4. **Generate at least two candidates per criticized item.** For each candidate, keep provider logs and candidate files outside the public webapp tree until selected.
5. **Contact-sheet QA by item row.** Choose the candidate that best fits the physical surface, not just the prettiest motif crop.
6. **Publish only selected finals with cache-busting filenames.** Example suffixes:
   - `rev02_surface-fit`
   - `rev02_banner-surface-fit`
   - `rev02_card-booklets-separated`
7. **Update only the affected manifest entries.** Leave unchanged items’ `imageSrc`, hashes, and titles intact.
8. **Verify live.** Run build, push, then confirm live manifest paths changed for the revised items, direct asset URLs return `200 image/png` at expected dimensions, hashes match, and Playwright/direct probes load the new images with no console errors or overflow.

## Prompt language that worked

### Single card on metal grid

> Apply the graphic only to the tilted paper/card surface; keep all black metal grid bars, background floor, shadows, card thickness and edges natural and unchanged. The graphic must look printed/fused into the paper, not pasted.

### Vertical fabric banner

> Apply the graphic only to the white hanging fabric banner, preserving opaque fabric material, vertical folds, bottom/top rods, shadows, and wall unchanged. Do not print on the stone wall or windows. Forbid transparent fabric holes and wall texture inside the banner.

### Board/booklet + small card

> The left booklet, right booklet, and small front name-card must all use different crops of the same source graphic. Both rear boards must be visibly printed; preserve visible seam, overlap edge, depth step, separate paper surfaces and natural shadows. Do not create one continuous panorama and do not put an unrelated image on the small card.

## Pitfalls

- Brightness/white-area masks are too broad for card/banner items; they can pull the motif onto the surrounding environment or flatten the mockup. Use explicit polygons and strong prompt constraints instead.
- Candidate 1 may look more dramatic but candidate 2 can be better if it preserves the physical surface more accurately. Optimize for believable product/mockup integration.
- Do not commit public candidate files. Copy only the chosen candidates to final rev filenames and point the manifest at those files.
- When replacing selected items after a previous version replacement, preserve the visible version slot and existing neighboring items. The user expects the named items to change, not the whole A/B ordering to churn.
