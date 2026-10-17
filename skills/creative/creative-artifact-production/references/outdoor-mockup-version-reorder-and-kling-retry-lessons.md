# Outdoor mockup version reorder + Kling retry lessons

Use when Chris asks to reorder versioned Outdoor Mockup child sets (A/B lanes) or append a new child set from a Midjourney source.

## Reordering versioned child sets

When Chris says e.g. `B1 b3 b4 b2 순서로 변경하고 넘버링은 다시 1234` or `A 4, 3, 1, 2로 변경`:

1. Interpret this as **visible order and visible naming**, not a need to rename physical asset files.
   - Keep `imageSrc` / asset filenames unchanged for cache stability and to avoid unnecessary binary churn.
   - Reorder the manifest `examples[]` entries.
   - Update visible `title` values for the parent examples and each child item (`A-1-1…`, `B-3-6…`).
   - Lightly update descriptions if they mention the old visible set number.
   - Add/update `displayOrder` and `renumberedAt` fields for clarity, but do not depend on them unless the UI reads them.
2. Preserve source-graphic identity. After reordering, verify by source graphic, not old IDs alone.
   - Example from 2026-10-08 B reorder: old `B-1/B-3/B-4/B-2` became visible `B-1/B-2/B-3/B-4` while internal IDs stayed stable.
   - Example A reorder: old `A-4/A-3/A-1/A-2` became visible `A-1/A-2/A-3/A-4`.
3. Validate with the live manifest order, not just local JSON diff.

## Appending a new versioned set

When adding a new child set such as `A-5`:

1. Confirm the Midjourney source high-res asset path from `midjourney-dna-archive` / public assets.
2. Use the current visible sequence to choose the next visible title (`Outdoor Mockup A-5`) while keeping a stable new manifest ID such as `outdoor-mockup-example-a-05`.
3. Generate all raw mockup items for the lane; create a contact sheet before publishing.
4. For board/book/panel item 5 variants, preserve the physical seam and use distinct crops. Do not let the motif become a single panorama across adjacent boards.
5. Append the new example immediately after the current last sibling in the same lane.

## Kling batch retry pattern

Kling image generation can fail transiently with service availability messages even when inputs and uploaded reference URLs are valid. Do not encode this as “Kling is broken.” Instead:

- Treat `Kling service is temporarily unavailable. Please retry later.` as transient.
- Save stdout/stderr per attempt under the raw generation folder.
- Skip already-created output files on rerun so a partial batch can resume from the first missing item.
- Retry each item up to a small bounded count with a short increasing cool-down.
- If a single item repeatedly fails after bounded retries, stop and report the blocker honestly rather than replacing it with a local fake.

## Live QA checklist after reorder or append

- `python3 -m json.tool public/data/brand-mockup-assets.json`
- `npm run build:public`
- Commit only the manifest and intended new asset files; avoid sweeping untracked candidate leftovers.
- Push to main.
- GitHub Pages can sit in `in_progress`; first poll status and live manifest. If it remains stale for several minutes, a new empty commit can retrigger the workflow and cancel the stuck run when concurrency is configured correctly.
- Verify live manifest order/count and direct asset URLs (`200 image/png`, expected dimensions).
- Use Playwright for page load, console errors, horizontal overflow, and at least one representative image probe. Lazy thumbnails can false-negative; direct asset and modal/image probes are more reliable.

## User communication

Chris does not need repeated internal logs. Keep progress notes short: state what is running, any real blocker, and the verified final result. For long Kling batches, mention that generation is quiet but alive only if the user may worry it is stalled.
