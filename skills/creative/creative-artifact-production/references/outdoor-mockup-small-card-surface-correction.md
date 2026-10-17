# Outdoor mockup small-card surface correction lessons

Use this when Chris says a multi-surface outdoor mockup is mostly acceptable, but a small front business-card/name-card surface contains the wrong graphic, looks like another version (e.g. A-1 ring motif), or does not match the current Midjourney source.

## Core lesson

If Chris says the rear books/boards are acceptable, do **not** regenerate the whole item first. Preserve the accepted rear surfaces and correct only the small card surface. Whole-image regeneration can re-break the seam/depth separation that Chris already approved.

## Recommended workflow

1. **Confirm the exact mismatch visually.** Compare the current item against the active source motif. For Midjourney 02, the card should read as beige/navy/coral directional-flow geometry, not circular/ring imagery.
2. **Preserve accepted surfaces.** Use the current accepted mockup as the base image when the books/boards are OK.
3. **Create several card-only candidates.** Locally composite 3–4 crop variants from the correct source motif into the small card polygon. Avoid unrelated motif families and avoid blank white cards.
4. **Use a contact sheet with both full view and card zoom.** Choose the candidate that (a) removes the wrong motif, (b) matches the current source graphic, and (c) still reads as a physical card sitting in the scene.
5. **Only escalate to Kling naturalization if needed.** If local replacement creates visible patch edges or lighting mismatch, then run Kling using the card-fixed local image as strict direction and the accepted book/board version as geometry reference.
6. **Publish with a cache-busting final filename.** Candidate files should not be the manifest target; copy the chosen candidate to a final `revNN` filename.
7. **Verify like a live asset change.** Run the build, update the manifest, push, wait for Pages, then verify live manifest path, direct asset URL (`200 image/png`, dimensions, hash), and a Playwright/direct image probe.

## Prompt / QA language

- “Preserve the accepted rear booklets/boards and their seam/depth separation.”
- “Only the small front name-card/business-card surface must be corrected.”
- “The small card must use a different crop of the SAME active source graphic.”
- “No unrelated graphic, no prior version motif, no circular/ring motif if the source is directional geometry.”
- “Keep natural paper edge, shadow, thickness, and tabletop contact.”

## Pitfalls

- A generated whole-image candidate may fix the card but regress book separation; avoid if the rear surfaces were already approved.
- A local patch that ignores existing shading will look pasted on. Reuse the base card shading and restore subtle paper edges.
- A card can be small in the full thumbnail but still drive rejection. Always zoom the small card in the contact sheet before publishing.
