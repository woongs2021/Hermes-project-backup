# DNA Brand Asset mockup version reordering

Use when Chris asks to change the visible order of versioned Outdoor Mockup child sets (for example `B1 b3 b4 b2` or `A 4, 3, 1, 2`) and asks to “다시 네이밍 순서 맞춰줘.”

## Core rule

Reorder and renumber the **manifest display metadata**, not the image files, unless Chris explicitly asks for physical file renaming.

Why:
- Existing image URLs are already deployed and cache-stable.
- Renaming files creates unnecessary asset churn and cache risk.
- Chris usually means the webapp-visible tab/order/title numbering.

## Manifest workflow

1. Read `public/data/brand-mockup-assets.json`.
2. Identify the target lane by `tabId`:
   - A lane: `outdoor-mockup-1`
   - B lane: `outdoor-mockup-2`
3. Interpret the requested old-order list as a mapping to new visible numbers.
   - Example: `B1 b3 b4 b2` means:
     - old B-1 → new B-1
     - old B-3 → new B-2
     - old B-4 → new B-3
     - old B-2 → new B-4
   - Example: `A 4, 3, 1, 2` means:
     - old A-4 → new A-1
     - old A-3 → new A-2
     - old A-1 → new A-3
     - old A-2 → new A-4
4. Reorder only the affected `examples[]` entries in manifest order.
5. Update display fields:
   - example `title`: `Outdoor Mockup A-1`, etc.
   - item `title`: `Outdoor Mockup A-1-1` through `A-1-6`, etc.
   - optional `displayOrder` and `renumberedAt` fields for traceability.
   - descriptions only where they mention visible set numbering; keep `sourceGraphic`, image paths, hashes, and source motif references unchanged.
6. Run JSON validation and `npm run build:public`.
7. Commit/push.
8. Verify live manifest order and at least a lightweight page load/console/overflow probe.

## GitHub Pages deployment note

Pages runs for these manifest-only changes can remain `in_progress` while the live manifest is still stale. If the run remains stuck after a reasonable wait, an empty commit can retrigger deploy and cancel the old run when workflow concurrency is configured to cancel in progress. Verify with:
- Actions run status via GitHub API or CLI,
- live `data/brand-mockup-assets.json` with a cache-busting query,
- the ordered lane entries and visible titles.

## User-facing communication

Keep the completion note compact:
- state old → new order mapping,
- list the final live order with source Midjourney numbers,
- mention build/deploy/live manifest/Playwright checks.

Avoid over-explaining internal IDs unless Chris asks; focus on what changed in the webapp.
