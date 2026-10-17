# Marked-area mockup correction lessons

Use this when Chris reports that a generated Design DNA / DNA Brand Asset mockup “still isn’t fixed,” especially after he provides a screenshot with a circled area.

## Lessons from the Outdoor Mockup Example 1-3 / 1-4 session

1. **Marked region is the acceptance target.** If Chris circles a problem area, do not infer another nearby area from memory. Inspect the marked screenshot and restate the exact target region before making changes.
2. **Do not over-patch.** After one failed local mask or one failed targeted generation, stop repeating tiny patches. Rebuild from the original mockup and the source metaphor.
3. **Generate multiple fresh candidates.** For persistent artifacts, ask Kling for at least two fresh candidates from original mockup + source metaphor, allowing the metaphor crop/area to change. Pick using a contact sheet.
4. **Prefer original mockup geometry first.** Prompt order should prioritize: original mockup geometry, source metaphor, tone reference. Use old composites only as rough direction, not as the main source when they contain the artifact.
5. **Use revision filenames.** If a visible asset is replaced, never rely on overwriting the same public filename. Save a new `_revNN...` file, update manifest `imageSrc`, then verify the live DOM uses the new path.
6. **Proof must be live and visual.** After deploy, verify live manifest, live asset hash, and Playwright DOM. Send a live thumbnail screenshot; if the thumbnail crops the change, also send modal-image or direct-asset proof.
7. **Pages deploy can be the blocker.** If main is pushed but Pages still shows the old asset, check whether the deploy job is stuck in `waiting`. A Pages workflow with `concurrency.cancel-in-progress: false` can leave a waiting deploy blocking newer output; changing to `true` and triggering a new run can clear it.

## Recommended Kling prompt shape for persistent mockup artifacts

- Image 1: exact original mockup; preserve geometry, camera, material, shadows, foreground objects.
- Image 2: source brand metaphor / graphic.
- Optional image 3: calm tone reference.
- Avoid making the previous flawed composite the primary reference.
- Explicitly allow crop/area changes if needed to remove the artifact.
- State the negative condition in concrete visual terms: “no transparent/hollow/cut-out area,” “no wall texture inside the fabric,” “no pasted rectangle,” etc.
