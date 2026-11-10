---
name: webapp-production-delivery
description: "Use when preparing, publishing, or validating a production static web app: asset delivery, public-data contracts, GitHub Pages/CDN deployment, and live verification."
---

# Webapp Production Delivery

For nested dissertation/research report expansion with responsive live verification—including promoting Dissertation to a peer of Report while retaining Idea 01, Idea 02, and References as its local tabs—see [`references/nested-research-report-surfaces.md`](references/nested-research-report-surfaces.md). For a user-supplied image assigned to one data-driven report/dissertation subtab, use [`references/data-driven-report-thumbnail-replacement.md`](references/data-driven-report-thumbnail-replacement.md).

> **Pixel Atelier note:** For transparent directional sprites, autonomous scene movement, and click-to-role-bubble QA, use [`references/pixel-atelier-sprite-interaction-qa.md`](references/pixel-atelier-sprite-interaction-qa.md). For selected-character pointer/touch dragging, keyboard movement, bubble headroom, and live interaction QA, use [`references/pointer-driven-scene-controls.md`](references/pointer-driven-scene-controls.md).

## Use when
- A static web app needs production-ready assets, manifests, download links, or release-hosted originals.
- A change alters public data, documentation, deployment behavior, or the site’s shipped UI.
- You must prove a deployed site—not merely a local build—contains the intended change.

## Core delivery workflow

> For a full collection rewrite from research-heavy Korean into readable blog prose, follow [`references/korean-report-prose-rewrite.md`](references/korean-report-prose-rewrite.md) alongside the normal delivery checks.

1. **Map the contract first.** Inspect the README, relevant UI components, data types, all affected public manifests, validation scripts, package scripts, and deployment workflow. Identify which fields are genuinely rendered before removing or changing them.
2. **Separate product assets by role.** Keep source/UI code and lightweight display previews in the app repository. Put large, versioned download originals in durable external storage such as GitHub Releases or a dedicated asset repository. The public manifest must distinguish the preview URL from the external download URL.
3. **Treat public data as product output.** Remove internal paths, source-run identifiers, candidate paths, private operational fields, and stale TypeScript fields. Audit every related manifest, not just the modified file.
4. **Document the same contract twice.** README material explains operational ownership, inventory/history state, and contributor guardrails. The in-product message concisely explains preview-versus-download behavior without promising downloads that do not exist.
5. **Automate public-boundary checks.** Add a deterministic validator to normal validation/CI that rejects local paths (for example `/opt/data/` and `file://`) and forbidden internal keys across all relevant public manifests.
6. **Validate locally.** Run the data/manifest validation, lint, production build, and a final diff/whitespace review. If a full build regenerates public manifests, distinguish those generated-data diffs from the feature’s deliberate source changes before staging or publishing.
7. **Treat editorial reports as product surfaces.** Keep public-safe report copy in a typed data module and render it through a reusable tabbed article panel. Make the visible provenance reference-led: name the source work and state the research target, method or evidence type, applicable finding, and generalization limit. Do **not** expose internal agent names, selection labels, review ownership, or workflow lore unless the user explicitly asks for an editorial byline. Separate source evidence from interpretation and caveats; when a length is requested, measure report-body characters programmatically rather than counting headings, citations, prompts, or shared UI copy. For a downloadable report, generate a self-contained escaped HTML Blob in the browser; offer `window.print()` with print-specific CSS as the reliable PDF-save path. Do not claim a native PDF file exists unless one was actually rendered and verified.
8. **Publish safely.** Confirm the working branch is current with its remote, use the repository’s established Git identity, commit/push, and wait for deployment success.
8. **Verify the live artifact.** Fetch the deployed index, resolve referenced application assets with URL joining, inspect the shipped bundle for new UI copy, and fetch affected live manifests. Account for short CDN propagation delays by retrying before declaring failure.

## Consolidating manifest-backed tabs, collections, or lanes
When a request combines existing tabs (for example A/B source collections and A/B composite lanes), treat it as a public-data migration rather than a cosmetic label change:

1. Map every reference before editing: collection IDs, item IDs, `tabId`, example titles/order, `mockupCollectionId`, nested item references, and any UI group definitions. Confirm which identifiers are public links versus internal grouping values.
2. Preserve the published assets unless deletion is explicitly requested. Create one merged collection with stable, unique item IDs and a clear unified title; re-map every old relation to its new collection ID, including records where a relation was formerly omitted.
3. Make the visible composite lane one group in the UI and normalize its examples to a single `tabId`. Define a deterministic display order and user-facing names rather than relying on the former A/B insertion order.
4. Make migrations atomically. Build the new collection/example arrays in memory from an unmodified manifest, assert source counts before mutating, then write once. Do not compute the "remaining" records after changing their discriminator fields; that can duplicate migrated entries.
5. Add a focused invariant check in addition to ordinary manifest validation: exactly one merged collection, expected asset/example counts, no retired IDs or tab labels, and every expected reference mapped to the unified collection.
6. After Pages deploys, fetch the live manifest and check those same invariants. Resolve the hashed script URL from the live index with URL joining (the base path can already be present), then assert the old visible labels are absent and the new single label is shipped.

## Removing a numbered Design DNA archive item

When Chris asks to delete a numbered item from a public, manifest-backed archive (for example, `Midjourney 53`), treat the visible archive number—not a local array index—as the identifier:

1. Start from a freshly fetched `origin/main` detached worktree. Confirm the local manifest count and target record match the deployed manifest before editing; do not rely on an older primary worktree copy.
2. Locate the entry by its stable `id` or exact `Midjourney NN` title, record its `imageSrc`, and search for other references before removal.
3. Remove both the manifest record and its exact public asset when Chris says to delete it. This is current-tree removal only; do not rewrite Git history unless explicitly requested.
4. Run public-manifest validation, lint, production build, and a focused assertion that the count decreased by one, the ID is absent, and the source asset path no longer exists.
5. After Pages deploys, fetch the live manifest to confirm the new count and target absence, then request the former image URL and confirm `404`. Include the live navigation path in the completion note.

## Removing an explicitly selected public archive item

When Chris identifies one numbered public archive item for deletion, remove the **manifest record and its referenced public preview/source asset together**—but only after mapping the exact `id`, title, and `imageSrc` from the currently deployed manifest.

1. Do not trust a stale or dirty checkout for inventory counts. Fetch `origin/main`, create an isolated worktree from that exact remote commit when necessary, and assert the target appears exactly once before mutation.
2. Search all public source/manifests for the target ID and asset basename. Remove only the manifest record and files that are exclusively referenced by it; preserve any reused assets.
3. Assert the count transition explicitly (for example, 56 → 55), target ID absence, and local asset absence. Then run the repository's public-manifest validator, lint, production build, and `git diff --check`.
4. After publishing, retry against the live manifest until the new count and target absence are visible. Fetch the former public asset URL and require the expected `404`; this proves both the UI data and asset delivery no longer expose the item.
5. Report the stable Pages URL and navigation path, plus the verified before/after inventory. Do not imply Git history was purged unless a separate history-rewrite task was explicitly requested.

## GitHub Pages artifact-size recovery for partially externalized assets

When a Pages workflow builds successfully but `deploy` fails because its uploaded artifact exceeds the 1 GB limit, treat the failure as an incomplete preview/original migration—not a transient deploy delay.

1. Read the failed deploy log and record the reported artifact size. Inventory the entire `public/` tree by bytes, then identify the largest directory and **all** manifest references to its files. Include display fields (`imageSrc`, `previewImageSrc`, `downloadSrc`) *and* provenance/source fields (`originalImageSrc`, `resynthesisSourceImageSrc`) before deleting anything.
2. Reuse the existing public asset repository and create a dated Release batch. Upload a manifest-derived allowlist of every removal candidate, using deterministic release filenames. Make the uploader resumable: compare existing Release asset name and byte size, skip verified assets, and never print credentials.
3. For any HQ `imageSrc` without a local preview, generate a display-ready WebP/JPEG preview first. Keep the preview in the webapp, set `imageSrc` and `previewImageSrc` to it, and set `downloadSrc` to the verified external Release URL. Do not point gallery rendering at the HQ download merely to avoid preview work.
4. Verify the Release asset count and total bytes; fetch at least one Release asset with HTTP 200; assert every changed local preview exists; and assert no affected public manifest still contains the retired local HQ prefix. Only then remove the current-tree originals. This does **not** authorize a history rewrite.
5. Rebuild and measure `dist/` before push. Keep the Pages artifact materially below 1 GB, stage only the manifest, generated previews, exact deletions, and documentation, then verify the exact workflow's **build and deploy** jobs both conclude success.
6. Live-smoke the current Pages manifest with a cache-busting request: the new Release tag must be present, the old local-HQ prefix absent, and a representative preview must return `200 image/*`. If the same release also carries a pending UI update, check its marker in the current hashed bundle as a separate assertion.
7. Update the webapp README and the asset-repository README together with the new Release tag/count and the preview-versus-download contract. State current-tree cleanup accurately; do not imply Git history was purged.

## History cleanup
Removing a current-tree asset is not Git-history cleanup. Before rewriting history, make an independently verifiable recovery archive and validate the rewritten mirror. Document clone re-synchronization implications succinctly after the rewrite.

## Completion checklist
- README and UI state a consistent public delivery contract.
- Preview and versioned download URLs are correct where applicable.
- Public manifests contain no internal metadata or local paths.
- Boundary validation runs in ordinary validation/CI.
- Validation, lint, and production build succeed.
- The remote deployment succeeds and the actual live bundle/manifests are checked.

## Focused Pages changes with a dirty working tree

When a user approves a narrow Pages feature while generated public data or another task has already left unrelated modifications in the worktree:

1. Inspect the full diff and identify the feature-owned source files explicitly; do not stage generated manifests merely because a full build rewrote them.
2. **Treat local dev startup as a write-capable action.** In this webapp, `npm run dev` runs data generators before Vite. Re-check `git status` after starting it and keep regenerated public data (`dashboard-manifest`, home-visual sets, research board) out of a narrow UI commit unless the task explicitly includes their semantic changes.
3. Run the full validation/build first, then stage only the reviewed feature files with explicit paths.
4. Run `git diff --cached --name-only`, `git diff --cached --check`, and a credential-pattern scan that examines **added lines**. Avoid broad keyword scans that flag harmless prose such as “token” or removed private-copy text.
5. Commit and push only that focused set. Confirm local HEAD equals the remote target branch SHA. If the configured SSH remote is unavailable but the repository has approved HTTPS credentials, push the same reviewed commit directly to the canonical HTTPS repository URL; do not change the saved remote protocol merely to work around a transient connection path.
6. Wait for the exact GitHub Actions run associated with that SHA. After success, fetch the live Pages index, resolve its hashed JS asset, and assert the newly shipped user-facing controls/copy occur in that live bundle. For a newly added image surface, also fetch the exact live public asset and check HTTP 200 plus its expected `image/*` content type; then perform desktop and mobile browser smoke checks for `img.complete && naturalWidth > 0`, layout overflow, and console/page errors. This is a useful no-browser fallback, but it does not replace a DOM/click or visual check.

### Consolidating related asset tabs without losing content legibility

When merging sibling asset collections or content tabs, treat it as an IA change rather than a mere identifier rename:

1. Inventory the source collections, examples, item counts, visible titles, ordering, and every linking field (such as `tabId` and `mockupCollectionId`) before editing. Make a deterministic post-change assertion that the merged collection count equals the original total and that every example/item still resolves to the intended collection.
2. Keep the **tab** singular when requested, but preserve recognizable internal series labels when they carry meaning (for example, keep `A-1…A-5` and `B-1…B-5` as section titles inside one `Outdoor Mockup` tab). Do not replace them with an opaque `1…10` sequence unless the user explicitly asks for renumbering.
3. Preserve original display order deliberately; do not rely on JSON insertion order after merging. Make the visible order explicit with the existing ordering field where the UI supports it.
4. Verify both data and rendering after deployment: inspect the live manifest for expected counts **and** use a real browser/DOM path to click through the navigation, select the merged tab, assert no empty state, count rendered sections and tiles, and confirm decoded images have non-zero natural dimensions. A valid manifest alone does not prove the user can find the merged content.
5. In the completion message, state the new navigation path and what remains visibly distinct inside the combined tab.

### Publishing a narrow Pages update when the primary worktree is dirty and behind `origin/main`

When a reviewed feature is ready but the primary worktree contains unrelated edits and its local `main` is behind the remote, do not rebase, reset, stash, or mix the feature into that tree. Preserve the other work and ship from an isolated worktree instead.

1. Fetch `origin` and compare the primary `HEAD` with `origin/main` before staging. If the primary tree is behind, create a temporary detached worktree from `origin/main`.
2. Transfer only the reviewed feature diff into that worktree (for example, a single typed report-data file), then run dependency install plus lint, production build, and `git diff --check` there.
3. Stage only explicit feature-owned paths. Run a cached-diff credential-pattern scan on added lines, commit from the clean worktree, re-fetch to confirm `origin/main` has not advanced, and push `HEAD:main`.
4. Wait for the exact commit’s Pages workflow to complete successfully. Then prove the live deployment by resolving the hashed bundle from the Pages index with URL joining (the index may already include the base path), searching it for the new visible copy, and exercising the live DOM path on desktop or mobile.
5. For lazy report hero images, scroll the image into view and wait for decode before using `complete` / `naturalWidth` as evidence. Remove the temporary worktree afterward.

This preserves in-progress local work while still delivering a narrow, current-base production change.

### Visual-style correction: scene assets versus profile assets

When Chris corrects an illustration direction—for example, asking that a scene use readable full-body blocky 2D characters rather than mosaic-style portrait tiles—treat that as a visual acceptance criterion, not a file-format change.

1. Keep the stylized asset scoped to the scene that needs it. If Team/profile cards are intended as identity surfaces, restore the original public profile image there; do not apply scene pixel treatment to those cards by default.
2. Define a concrete silhouette checklist for every in-scene character: readable head/face, hair, torso, independent arms, separate legs/shoes, transparent background, and a restrained role-specific prop. Preserve nearest-neighbor rendering and verify the natural asset dimensions, transparency, palette bound, and fallback behavior deterministically.
3. Derive colors only from approved public reference imagery when the work is public-safe. Avoid creating or implying a new photorealistic likeness; role props should aid wayfinding, not turn the scene into a generic game interface.
4. Inspect rendered screenshots at both desktop and narrow mobile widths. Image `naturalWidth` alone is insufficient: confirm the figures remain visibly full-body, labels remain unobscured, and profile cards visibly render their original non-pixelated images. Test a failed scene-sprite request to confirm the original public profile fallback.
5. In the final live verification, assert the split explicitly: scene sprites retain crisp pixel rendering; introduction/profile images use normal rendering. Include the live navigation path when reporting completion.

### Art-direction gate for illustrated team spaces

When a request evolves toward a GatherTown-like, Pixel Office, or other character-led collaborative scene, do **not** assume that adding CSS zones, generated portraits, and looping movement will reach the desired quality. Treat it as an art-direction decision before it becomes a feature implementation.

1. Before expanding to a full team scene, make one **single-frame direction board** or one finished representative zone. State the intended visual grammar: perspective, character/presence treatment, material palette, hierarchy, and motion philosophy.
2. Ask whether the product needs a true game world (which requires a coherent sprite system, tiled environment, direction-specific walk cycles, collision/interaction rules, and substantial art production) or an editorial/atelier surface (which should use a composed illustration, material cues, and restrained presence signals). Do not ship a low-fidelity hybrid as a substitute for either.
3. If generated visual candidates contain provider watermarks or artifacting, discard them. Never remove, crop out, or otherwise obscure attribution marks. Extract only non-proprietary, high-level learnings—such as desired silhouette density or warm material balance—then create original replacement art.
4. For a calm premium dashboard, prefer role-specific **traces** (paper, swatches, research card, tool, review marker) over game avatars and floating status labels when character identity reduces editorial quality. Keep operational status accessible in normal text outside the illustration.
5. Keep the direction-board artifact separate from the production webapp until Chris approves it. Do not let an exploratory visual mock silently turn into a deployed feature.

### Pixel-character sprite extraction and background-aware movement

For generated directional sprite sheets, background-aware collision zones, opaque extraction, stacking guarantees, and deterministic QA, use [references/pixel-atelier-sprite-extraction-and-collision.md](references/pixel-atelier-sprite-extraction-and-collision.md). In particular, prefer RGB `colorkey` over YUV `chromakey` for cream-background character sheets, then retain the primary connected component and normalize retained pixels to opaque alpha; test the result on a dark board before publishing.

For smooth, non-pixel five-view turnaround sheets, use [references/smooth-turnaround-sprite-extraction.md](references/smooth-turnaround-sprite-extraction.md). Do **not** finalize equal-width cell crops: preserve only each cell's largest connected opaque component, normalize by a shared figure height (not width), and visually audit both three-quarter poses for neighboring-pose slivers before shipping.

### Replacing a pixel-art character set with smooth illustrated sprites

When Chris says a character face looks broken or pixelated, inspect the **native sprite art and a rendered scene screenshot** before changing CSS. `image-rendering: auto` can soften nearest-neighbor edges, but it cannot restore facial information that was authored as coarse pixel blocks. If source facial detail is the issue, replace the artwork rather than repeatedly tuning CSS.

1. Keep the established character contract: preserve each member's silhouette, hair, recognizable wardrobe colors, role cues, required five directions (`front`, `front-three-quarter`, `profile`, `back-three-quarter`, `back`), and the existing transparent 400×1500 RGBA sprite canvas unless a separate layout change is approved.
2. Generate or commission a single **five-view turnaround sheet per character** first. Require the exact five-view order, complete body-to-shoes figures, smooth anti-aliased editorial illustration, no text/watermarks, and a plain even background. Visually inspect all sheets for identity consistency, especially face, hair, and outfit across directions, before extracting assets.
3. Background removal is a visual-quality step, not just a format conversion. Use a conservative extraction that protects light skin and pastel wardrobe colors; an aggressive cream color key can remove facial tones. Composite representative extracted sprites on a dark board and inspect for rectangular fills, halos, missing facial detail, and unwanted floor shadows before replacing public assets.
4. Normalize every accepted direction to the established canvas, run the repository's directional-sprite verifier, and test real scene rendering at desktop and narrow mobile widths. Assert all six images are complete, have their expected natural dimensions, use normal smoothing rather than pixelated rendering, and show no console errors.
5. Preserve motion and accessibility behavior: exercise each character's selection, role bubble, pointer/touch drag, keyboard movement, and direction switching after the asset swap. Publish only the reviewed asset paths; keep generated source sheets/candidates outside the public app unless Chris explicitly asks to archive or publish them.

This is a full art replacement, not a CSS polish: do not claim a pixelated face has been fixed until the rendered scene is visually checked.

#### When “pixelated” is a source-art defect, not a CSS defect

If Chris says faces or silhouettes still look broken after `image-rendering` is changed, inspect the native sprite at full size before touching more CSS. A source sprite that was generated as pixel art cannot become a premium smooth character through browser resampling or simple upscaling; preserve the role, hair, outfit, and silhouette, then regenerate a coherent high-resolution non-pixel **five-view turnaround** for every affected character.

- Do not publish a front-view-only replacement: ambient movement will expose the remaining pixelated 3/4, profile, and back views. Keep the existing typed five-direction asset contract intact.
- First create and art-direct a representative front candidate. Once Chris approves it, create all required sheets in one shared visual grammar, then inspect every sheet for exactly five complete figures, directional order, consistent proportions, intact faces, and no text/watermarks before extracting sprites.
- Treat background removal as a separate visual-quality gate. A warm-ivory RGB `colorkey` can erase light skin, hair highlights, or pale clothing; always composite extracted PNGs over a dark board and inspect face/edge preservation. If source background variance makes a keyed matte destructive, use a foreground-segmentation/rembg workflow rather than shipping degraded faces.
- Keep rejected candidate sheets and temporary extraction attempts outside the public app tree. Copy only the visually approved, alpha-verified 30 directional PNGs into `public/assets/team/atelier-sprites/`.

### Replacing pixel sprites with smooth editorial characters

When Chris says a character face looks broken, blocky, or out of place against the atelier background, inspect the **native sprite asset** as well as the rendered scene before adjusting CSS. `image-rendering: auto` can remove nearest-neighbor scaling artifacts, but it cannot recover facial detail that is intrinsically pixel-art source content. Do not present CSS smoothing as a complete fix when the source face is made of visible pixel blocks.

1. Preserve each character's approved identity contract—hair silhouette, wardrobe, palette, role prop, body proportion, and five directions—then generate a single high-resolution five-view turnaround on a uniform plain background. Specify the strict order: front, three-quarter front, profile, three-quarter back, back. Avoid a separate generation per direction unless the sheet fails consistency review.
2. Use smooth, anti-aliased editorial illustration language explicitly: delicate facial features, natural fabric texture, gentle tonal gradients, and **no pixel art / blocky edges / mosaic texture**. Keep figures 2.5-head-tall only if that is already approved; do not accidentally shift toward plastic 3D toys or exaggerated anime styling.
3. Before background removal or slicing, create and visually inspect a contact sheet for all team turnarounds. Reject sheets with extra people, incomplete feet, text/watermarks, inconsistent outfits, direction-order errors, or faces that are still pixelated. Do not silently publish a generated sheet just because it has the expected dimensions.
4. Remove the uniform background using a quality alpha-capable removal pass when available; then split and normalize all 30 directional images. On transparent output, verify no cream halo, no holes in dark clothing/hair, and no square matte on both light and dark test boards.
5. Preserve existing sprite-map routes, movement collision, drag/keyboard controls, role bubbles, and accessibility. Validate desktop and mobile composition after replacement because the revised silhouette/transparent bounds can change bubble headroom and collision footprint.
6. In the final live check, assert each image is decoded with its expected natural dimensions, all six walkers render, no console/page errors occur, and visually inspect the two previously flagged characters at their displayed size—not just the generated source image.

### Replacing broken pixel character faces with smooth illustrated figures

When Chris says a character’s face looks broken, blocky, or mismatched with the background, first inspect the **native sprite asset** and a rendered scene crop. Do not assume the problem is CSS scaling: `image-rendering:auto` can soften nearest-neighbor edges, but it cannot restore facial information that was generated as coarse pixel blocks.

1. If the source face is truly pixel-art or malformed, do not ship blur/upscale-only as the final correction. Preserve the approved identity cues—hair silhouette, outfit, proportions, palette, and role—but create a smooth high-resolution **front-pose candidate** first.
2. Use the existing sprite or approved reference image as an identity/wardrobe reference in generation. Require: full body, clean silhouette, no text/watermark/props, non-pixel editorial illustration, and a simple removable background or alpha. Visually reject candidates with facial artifacts, changed wardrobe, unreadable hands, or generic plastic/3D-toy styling.
3. Share the two most affected candidate figures with Chris before generating the full directional set. A front-only candidate is a direction board, not a production replacement: do not silently substitute it into a moving 5-direction scene.
4. After approval, generate or draw all five directions (front, 3/4 front, profile, 3/4 back, back) in the same style. Extract transparency, normalize canvas/feet alignment, and verify that movement never falls back to an old pixel sprite.
5. Perform rendered desktop and mobile visual QA at the actual scene size. Confirm faces read cleanly, every direction has the same identity, the new smoother treatment fits the background, transparent edges are clean, and selection/drag/keyboard movement still work. Only then commit, deploy, and verify the live asset dimensions and rendering mode.

### Reintroducing motion to an approved atelier surface

If Chris later asks for characters to move through an approved editorial/atelier scene, treat it as **ambient presence**, not a return to a game world:

1. Default to no more than one or two small full-body pixel figures at once. If Chris explicitly asks for the entire team to circulate, honor that direction while keeping figures small, staggered, and visually secondary; do not add nameplates or route indicators.
2. Give each figure a short local path and a long, staggered cadence (roughly 15–20 seconds), with visible pauses. For multi-character scenes, test the actual travel path against furniture/obstacles rather than only checking destination points. Keep size, opacity, and shadows restrained so the illustration remains the hero.
3. Reuse only approved public-safe sprite assets. Crop sprite sheets deterministically, retain an image-load fallback, and verify that the fallback does not break the composition.
4. Implement `prefers-reduced-motion: reduce` as a true static state: do not start the JavaScript motion scheduler, rather than merely reducing the CSS transition duration.
5. Visually QA desktop and narrow mobile after the animation has progressed beyond its initial pause. Assert: no horizontal overflow, no overlap with essential caption/controls, and no console/page errors. For a six-person scene, assess density and readability rather than enforcing the default two-person count.
6. Keep this refinement as a focused source-only change. If Chris has not explicitly asked to publish it, do not silently commit, push, or deploy; show the verified local artifact first.

For the typed sprite contract, path-safe Pages verification, and a focused deployment checklist, see `references/directional-sprite-atelier-delivery.md`.

### Preserving character identity while improving sprite finish

When Chris says in-scene characters look broken, overly dotted, or visually weaker than a warm illustrated background, distinguish **rendering artifacts** from an actual character-art replacement need before generating new likenesses:

1. Inspect the native transparent sprite and a rendered desktop screenshot together. If the existing source is already substantially larger than its rendered footprint and the silhouette/identity is approved, keep the asset set and first inspect CSS resampling.
2. Do not force `image-rendering: pixelated` or `crisp-edges` for a character that must feel smooth and premium. Use normal browser interpolation (`image-rendering: auto`) so the existing high-resolution RGBA source is downsampled softly; retain the same directional files, interactions, and recognizable appearance.
3. Visually compare the revised rendered scene against the background—not only the standalone source. Accept only if hard pixel stair-stepping is reduced, facial readability remains intact, and the character still has enough edge definition to separate from the scene.
4. Generate an all-new non-pixel character system only when normal resampling cannot solve the mismatch. A replacement must preserve the approved face, hair, clothing, silhouette, transparent background, and every required movement direction; do not trade identity continuity for a generic polished avatar.
5. In live verification, assert the shipped CSS uses the intended image-rendering rule, all directional sprites load at their expected natural dimensions, six-character layout remains intact, and console/page errors are zero.

### Click-to-role bubbles in animated character scenes

When Chris asks to turn an ambient character into an explorable team surface, make the role bubble a concise, semantic mini-card rather than a name tag:

1. Keep each character's role copy in a typed ID-keyed map with a short **English title** (for example `Orchestrator`, `AI Researcher`, `Design Specialist`, `Product Manager`, `Developer`, `Validator`) and a one-sentence Korean description. Do not repeat the character name in the bubble unless Chris explicitly asks for it.
2. On selection, freeze only the selected walker, force its front-facing sprite, and keep the other walkers moving. A background click must remove the bubble and restart the selected walker. Use a real `<button>` with `aria-pressed` and a focus-visible style rather than a pointer-only sprite wrapper.
3. Position the bubble above the head—not across the face—and visually inspect a rendered screenshot. Source/CSS intent is insufficient: measure the bubble and scene boxes to detect clipping, then tune the vertical offset and allowed movement range together. Do not merely hide a clipped bubble with `overflow`; preserve legibility.
4. In Playwright, click every walker and assert its exact title and description, one selected state/bubble at a time, no page errors, and a fully visible bubble in the target desktop viewport. Also smoke-test selection freeze, other-walker motion, and background-click resume before publishing.
5. After Pages deploy, assert all role titles and the bubble positioning rule occur in the live hashed bundles, then repeat at least one live DOM/click smoke test—not only an asset fetch.

### Responsive team-scene overlays and loop overview placement

When a Team-tab illustrated office has selected-character role bubbles and a companion automation overview:

1. Treat the sprite button's transparent canvas—not just the visible figure—as the positioning reference. At tablet/mobile widths, measure every selected bubble against the scene bounds. A desktop-safe `bottom:%` offset can overlap the head or clip above the scene after the sprite scales down.
2. Use a responsive placement rule: raise normal bubbles enough to clear the head; for walkers near the scene's upper boundary, add a semantic `--below` modifier and flip the tail so the bubble remains entirely inside the scene. Test every character at desktop, tablet, and mobile, asserting bubble bounds stay within the scene rectangle.
3. If keyboard navigation already selects the character and exposes the role bubble, do not leave a decorative focus outline that reads like an unwanted sprite stroke. Verify the actual computed focus outline after an arrow-key interaction; preserve the selected/bubble state as the visible interaction context.
4. When Chris asks to position the office “above” a named Team section, make it immediately adjacent in JSX order—not merely earlier somewhere on the page—and assert the rendered top-coordinate ordering in desktop and mobile DOM QA.
5. Before restoring an operations/loop overview, recover its previous inventory from the app history and inspect the live scheduler separately. Do **not** replace a known full team-loop inventory with the smaller subset currently visible to one scheduler API. If both concepts matter, label and render them separately: **registered team loops** (the preserved operational inventory) versus **scheduler active** (jobs currently enabled in Hermes). Present only public-safe owner, cadence, delivery class, and status; omit identifiers, prompts, credentials, raw errors, and stale next-run timestamps. Derive every summary count from the displayed rows and visually verify the summary matches them.
6. If Chris asks to resume a paused loop, resume the exact scheduler job first, immediately re-list it to verify `enabled`/`scheduled` state and next run, then update and redeploy the public overview so its active/paused counts agree with the live scheduler.

## Editorial report sizing and revision requests

When a user asks to extend a report to an approximate Korean character count, measure the rendered report-data strings programmatically rather than estimating from lines or paragraphs. State whether the count includes only Hangul or all visible non-whitespace characters; headings, tabs, shared bylines, citations, and prompts should not silently substitute for requested body copy. For a request such as “halve the title size,” update every value in a responsive `clamp()` typography rule proportionally, then verify the exact declaration in the live CSS after deployment.

For report-style static surfaces, browser-generated HTML download (`Blob` + object URL) and `window.print()` with print CSS are a public-safe download pattern: describe the latter accurately as **Print / Save as PDF**, not server-generated PDF.

### Editorial emphasis and shipping autonomy

When Chris asks for a highlighter-style emphasis in report prose, highlight only a small curated set of thesis-level phrases per tab—not every citation, heading, or sentence. Render a semantic `<mark>` around selected phrases and use a partial-height background gradient rather than a solid block: a restrained fluorescent accent at approximately 15% opacity should preserve the editorial reading surface. Ensure wrapped lines retain the marker treatment with `box-decoration-break: clone`, keep the text color inherited for contrast, and include the emphasis in the print/download representation when those exports are part of the requested surface.

When Chris explicitly authorizes the requested webapp task to ship without further approval, treat commit, push, exact Pages-workflow verification, and live-link delivery as the completion path. Do not stop after a local build or leave a pushed deployment as an unverified “in progress” final state; distinguish unrelated generated public-data diffs and commit only the feature-owned source files.

### Selected Design DNA assets: specialist-owned publication

When Chris explicitly selects a Go Youn-jung visual with `저장해줘`, the intended outcome is both durable local archival **and** publication to `Design DNA → DNA Dashboard → GPT Image 2.5`—not a local-only save.

- Publish only the exact Chris-selected images. Do not publish candidates, contact sheets, generation logs, provider URLs, source-run folders, or unselected variants.
- Treat the selected local manifest as a **private intake record**, not a ready-to-copy public manifest. Build a minimal public entry from rendered fields (id, title, date, safe description/analysis, clusters, model/options, dimensions, selected reason, Midjourney prompt, and public `imageSrc`). Strip all local paths and operational keys such as source runs/references, remote URLs, hashes if not needed by the UI, and generation metadata.
- Do not overwrite the canonical public DNA manifest with a specialist's temporary Pages worktree copy: it can be stale or carry unrelated historical changes. Append only the new selected entries to the canonical repo manifest and copy only their exact public image files.
- Before committing, run `npm run validate:public-dna`, lint, `npm run build:public`, and `git diff --check`; stage only `public/data/dna-archive.json` plus the explicit new `public/assets/dna-archive/...` files.
- If Chris authorizes Go Youn-jung direct deployment, constrain it to the single `Hermes-project-webapp` `main` path and those manifest/asset locations. The profile-owned script must reject other staged paths and candidate directories, then commit/push and verify the exact Pages workflow, live manifest entries, and decodable live image URLs.

### Confirming a specialist-owned research or Design DNA update before changing it

When Chris asks to update a Muyeol-selected research card and Go Youn-jung-selected DNA assets, first establish whether the specialist flow has already published the exact approved state. Do not create a duplicate commit merely because the main working tree has not been refreshed.

1. Read the current specialist handoff/log and identify exact research IDs, validation state, selected image IDs, and intentionally excluded candidates.
2. Fetch the canonical remote and compare commit ancestry (`git fetch origin --prune`; inspect `origin/main` versus local commits). If `origin/main` already contains the research and asset commits, treat it as an already-shipped change and move to verification rather than reapplying it.
3. If the primary worktree is dirty with unrelated work, create a temporary detached worktree from `origin/main` for validation. Never reset, stash, or overwrite another in-progress task just to run a build.
4. Verify both layers independently: query the live `research-board.json` for the exact research item and its status/validation fields; query `dna-archive.json` for only the selected IDs; then fetch every new asset and verify it decodes as the expected image type. A manifest is evidence of data publication, while an asset fetch proves the public path is usable.
5. Run lint, production build, and diff check in the clean validation worktree. If UI navigation exposes the relevant surface, perform a focused DOM/click smoke check; if the selected assets belong to a manifest-backed archive not rendered by the current route, state that boundary accurately rather than treating a generic page check as visual proof.
6. Report that the live site was *verified*, not newly deployed, when no new change was needed. Include the stable Pages URL and navigation path, and retain the research generalization limits (for example, a small qualitative design-study sample must not become a universal productivity claim).

### Dissertation-reference tabs sourced from an accumulated research pool

When Chris asks to turn already accumulated Yuna / Go Youn-jung paper candidates into a dissertation-specific **References** tab, make it a dedicated public evidence-map surface rather than silently relabeling the general Research board:

1. Have the research specialist rank **only existing candidate records** against each dissertation idea. Retain stable candidate IDs, English/Korean paired titles, source URL/DOI, access scope, current verification state, fit rationale, and explicit evidence boundaries. Do not add newly discovered papers unless Chris separately requests discovery.
2. Publish a minimal dedicated manifest such as `public/data/dissertation-references.json`; strip internal source line numbers, agent workflow/provenance fields, local paths, and private notes. Assert exact total, Idea 01/Idea 02 split, unique IDs, valid public source URLs, and contiguous Top-10 ranks.
3. Add `References` as a separately addressable Personal AX tab. Show all relevant papers with an Idea 01/Idea 02 filter and a selectable detail view. Preserve a legacy dissertation hash only when the existing route needs compatibility; do not merge the two dissertation ideas back into a nested control.
4. Reuse the **visual card structure** of the validated-paper stack for the Top 10 if Chris requests it, but never label relevance-ranked or `unreviewed`/`WATCH` records as validated. Use a title such as `가장 논문 아이디어와 연관된 논문 10개`, a `Top 10` badge, and expose each record's actual source-access and review status in the detail view.
5. Validate locally and live: Top-10 count, complete-reference count, exact title, filter behavior, card-to-detail selection, no page errors, and `document.documentElement.scrollWidth === window.innerWidth` at narrow Fold/mobile width. Then wait for the exact Pages workflow, fetch the dedicated live JSON and current hashed bundle for the new tab label/title/manifest path, and repeat the hosted DOM check.
6. If the repository-wide research-board validator fails on a pre-existing malformed candidate unrelated to the new dedicated manifest, report that boundary plainly. Still run lint, production build, diff check, focused manifest assertions, and deployment/live verification; do not claim the full validator passed.

### Weekly research dashboard lane summaries

When Chris asks to split a Weekly/total research status surface by research owner, treat the **same public `research-board.json` manifest** as the source of truth for every displayed count. Present a calm, comparable three-part summary with no agent names in the public UI: **Total Paper Research** (all items + current-week intake), **AI Paper Research** (AI·agent UX lane, all-time + current-week), and **Design Paper Research** (UX·BX·design lane, all-time + current-week). The section title is **Total Paper Research Overview**. Keep archive/DNA metrics visually secondary so the paper-research picture reads first.

- Derive the latest ISO week from the manifest data, then calculate all-time lane totals and current-week lane totals independently; do not use a combined “lane balance” number as a substitute for lane-level visibility. Any remaining balance or shortlist labels must also use the public research categories rather than agent names.
- Before validation/build, regenerate the public research manifest when its validator reports it is stale (`npm run generate:research-board`), then run `npm run validate:data`, lint, and the production build. Stage the regenerated research manifest only when it contains semantic research changes; do not accidentally include unrelated generated dashboard/home-visual timestamp churn.
- For this user, every published webapp update response must include the stable Pages URL **and the navigation path to the changed view**. After GitHub Pages reports success, verify the live hashed JS bundle contains the intended visible English labels and fetch the live manifest to confirm the displayed item count.

### User-supplied thumbnail / media replacement release loop

When Chris supplies a replacement image for a report, card, or tab, treat it as a complete release task—not only a data-field update.

1. Copy the supplied image to a stable public asset path with a semantic filename. Update only the intended record and supply accurate alt text.
2. Run lint, production build, and diff checks. In a locally rendered page, select the exact destination tab and verify the image `src`, `complete`, `naturalWidth`, `naturalHeight`, and document-level no-overflow at the relevant narrow viewport.
3. Commit both the data reference and binary asset, push, then verify the actual Pages/host deployment job reaches **completed / success**. A successful build job does not establish that the deploy job succeeded.
4. After live success, fetch the public image and rendered page to confirm the new asset is served. Then proactively send Chris the stable live URL and the navigation path. If deployment is pending or fails, separate local verification from live status and never imply that the live link has updated.

### Narrow Fold/mobile viewport overflow: inspect global floors before local components

When a user reports that a page still scrolls horizontally on a Fold or another very narrow device after a component-level overflow fix, inspect global viewport constraints before repeatedly adjusting the named component.

1. Search base styles (`index.css`, reset files, `html`, `body`, app shell) for `min-width`, fixed widths, `100vw`, and unbreakable content. A global floor such as `body { min-width: 320px; }` guarantees whole-document horizontal overflow on a roughly 280px CSS viewport, regardless of whether a table wrapper correctly scrolls internally.
2. Remove or relax the global floor when the product supports those viewports; preserve intentional wide content inside its own `overflow-x: auto` wrapper. For a report table, apply `min-width: 0; max-width: 100%` to the card/wrapper chain and keep the table's readable minimum width inside that wrapper.
3. Make the acceptance probe explicit: in a real browser at the target viewport, require `document.documentElement.scrollWidth === window.innerWidth`; separately allow a deliberately wide table wrapper to have local horizontal scroll.
4. Check grid track sizing as well as explicit width rules. A one-column `grid-template-columns: 1fr` track has an automatic min-content floor: a non-wrapping tab rail can widen the entire `.app-shell` even when `body` has no `min-width`. At compact breakpoints use `grid-template-columns: minmax(0, 1fr)` and apply `min-width: 0; max-width: 100%` through the app shell → workspace → tab-rail chain. Put `overflow-x: auto` and `overscroll-behavior-x: contain` on the *local* tab rail so its labels remain reachable without making the document draggable.
5. Probe the exact target route, not only the app home: load the relevant hash/path (for example `#dissertation`) at Fold/mobile/tablet widths. Require `document.documentElement.scrollWidth === window.innerWidth` at each target width; a deliberately wide research table may exceed its own wrapper only if that wrapper, rather than the document, owns local scrolling.
6. Do not infer a failed Pages workflow from a slow CDN alone. Check the exact workflow run and its build/deploy job conclusions. If the build succeeded but deployment failed transiently, re-run or trigger one clean retry, then verify the live hashed CSS bundle. CSS minifiers can reorder declarations, so test semantic presence/absence (for example, `body` has `min-height:100svh` and no `min-width:320px`) rather than a brittle exact declaration order. If a live browser navigation itself times out, do not describe the page as browser-live-verified; report the successful workflow and completed local route/viewport probe separately.

### Report typography refinements and completion messaging
 Keep the cover, eyebrow, title, dek/abstract, headings, references, prompt notes, and bullet lists unindented so the reading hierarchy remains clean. Mirror the same paragraph treatment in the self-contained HTML download stylesheet whenever it is offered.

When Chris requests a webapp update, every completion message must include the stable live Pages URL and the navigation path to the changed view. Include it even when CDN propagation may still be occurring; state the deployment state accurately rather than omitting the link.

### Pages propagation: never substitute push success for live proof

A successful `git push` and a `200` response from the stable Pages URL do **not** prove that the new UI copy is deployed: the page can still serve the preceding hashed bundle while the Actions workflow is running or CDN propagation is incomplete.

#### User-requested deployment monitoring

When Chris asks to keep checking a pending Pages deployment, create a **silent, script-only cron monitor** rather than sending repeated conversational updates. The script must check all three conditions: the exact Actions run is `completed/success`; the cache-busted Pages index resolves a current hashed JS asset; and that bundle contains a feature-specific visible marker. Print a concise Korean confirmation only once, then record a local sentinel file so later ticks remain silent. Schedule it at the requested cadence (for example `every 3m`) with `no_agent=true` and origin delivery. This avoids both premature "live" claims and repetitive success notifications.

1. After pushing, identify the workflow run whose `head_sha` matches the pushed commit and wait until it concludes `success`. Do not say the change is live before this.
2. Fetch the Pages index with a cache-busting query, extract its current hashed JS asset, and fetch that asset with another cache-busting query.
3. Assert the exact newly visible string (or another feature-specific shipped signal) is present in that live bundle. Also check that replaced text is absent when the task is a wording correction.
4. If the first live probe still yields the old bundle, report the accurate state as *pushed / deploying* and retry with bounded delays. Only call it *live-verified* after the new bundle passes the exact-string check.
5. State the final navigation path and, when a user has already seen stale copy, suggest a fresh reload without implying this replaces the server-side verification.

### Report cover-image intake and placement

When Chris supplies an ordered batch of images for existing report tabs, preserve that order unless he explicitly asks for semantic remapping. First inspect all supplied images, then map them one-to-one to the tab order and publish them as durable, public repo assets—not temporary chat-cache paths.

- Extend the typed report data with `heroImage` and Korean `heroAlt` fields; keep asset paths relative to the app base (for example `assets/personal-ax-reports/<report-id>-hero.jpg`).
- Render the cover image at the beginning of the report header, ahead of the eyebrow, title, and dek. Use a calm full-bleed frame with `object-fit: cover`, a wide editorial ratio near `2.4 / 1`, rounded corners, and a restrained border.
- Include the same cover in the browser-generated HTML download using an absolute public URL built from the current origin and app base. Do not serialize a local filesystem or image-cache path into a public document.
- Verify every copied image is a decodable image file before build, then include only the explicit cover assets and report-owned source/CSS/data files in the feature commit.
- For a single supplied replacement cover, keep the change deliberately narrow: copy the chat-cache image into `public/assets/personal-ax-reports/<report-id>-hero.jpg`, update only that typed report record’s `heroImage` and Korean `heroAlt`, and retain the prior asset unless removal is explicitly requested. Use a **report-ID-specific new path** even when the prior record pointed to a generic/shared hero; never overwrite a generic asset that another report may still reference. Inspect the image for visible watermark/pseudo-text before publishing; record its actual dimensions and hash, then verify the deployed bundle references the new relative asset and the direct public URL returns `image/jpeg` (or its expected image type). Write alt text from the actual supplied composition rather than reusing the old cover description. A common supplied 1280×640 image remains suitable for the existing wide editorial cover frame; do not distort it merely to match the frame ratio.
- When several report covers arrive in sequence, treat each request as an independent, narrowly scoped release: fetch `origin/main` before every edit, use a report-ID-specific new asset path rather than overwriting a prior public asset, and stage only the record plus its exact image. Pages/CDN propagation for a hashed bundle can take several minutes even after push; retry the live index/bundle and direct image probe until both the new path is referenced and the image decodes before announcing completion.
- When Chris then asks to make the report reading experience less academic and more blog-like, do **not** dilute or delete cited evidence as a shortcut. Keep the title/dek as the quick read, place the first one or two readable paragraphs before optional detail, and move long evidence/context into a native, accessible `details/summary` disclosure such as `더 깊이 읽기`. Remove first-line indentation from screen and downloaded report prose; use short, direct Korean introductions that explain what the reader will get. Apply the layout to every report via the shared renderer, but preserve evidence limits, source links, and the separate research-stage caveat for dissertation content. If Chris asks to rewrite the prose itself while keeping its volume, revise **every** reader-facing Korean text field (title, dek, heading, paragraphs, bullets, follow-up paragraphs, and alt text), not only a representative sample; preserve claims, study methods, numbers, named sources, and limits, then measure/review the diff for coverage. This is a shared-surface change: run build/lint, commit/push, and verify the new disclosure text appears in the live bundle before saying it is complete.

### Removing time-bound editorial framing from reports

When Chris asks not to limit reports to a particular month or date, remove the editorial time framing consistently from every report title area and reader-facing prose: report eyebrows, deks, section headings, and contextual sentences such as “this month’s observation” or “next month’s priority.” Also inspect shared rendering strings and export metadata—not just typed report data—including `aria-label`, HTML download filenames, print titles, tabs, and empty-state copy; a stale month in those surfaces silently breaks the request. Replace them with durable language such as “this research,” “the current priority,” or “the next operating question.” Preserve years that are part of a cited paper title, DOI, source URL, or factual study metadata; those are evidence, not editorial timestamps. Before publishing, search all report-owned source files for month names and display-date labels, review each remaining result, then verify the live bundle contains the new neutral wording. Do not describe the update as live-verified if CDN propagation has not actually completed; state that it has been pushed and is still propagating instead.

### Reference-led report revisions and new report tabs

When Chris asks to make an existing report “more paper-like,” revise the **visible prose**, not only the eyebrow or citation list. Structure each report around: research scope/problem → source-specific evidence (study type, sample/materials or review corpus when verified) → finding → product/design interpretation → generalization limit. Keep the source’s evidence and the editorial interpretation in separate sentences or paragraphs.

- Do not expose specialist names, internal review/selection labels, or team-workflow provenance in public report copy unless explicitly requested. Show only public sources and a concise access label such as `full text` or `abstract/metadata`.
- For a new domain tab (for example package design or design education), add it to the same typed report data array so the existing tab UI, HTML download, and Print/Save-as-PDF flow work automatically. Give it its own source list and image-prompt placeholders; do not create a parallel report surface.
- When Chris asks for a new report tab on the “right,” append the typed record as the final array entry and add its ID to the report-ID union. Verify this ordering deterministically (last record ID, expected section/source counts) before build. Keep the report evidence-led: state the research question, method, claim boundary, ethics/data boundary, and next validation separately rather than presenting an early concept as a completed study.
- If Chris then asks to promote one internal report to the same level as `Report`, treat it as an IA migration rather than a duplicate page: add a primary workspace `TabId`, `Tab`, and the correct `TabGroup` ordering; route that tab to the same reusable article renderer using an explicit report ID; and exclude that ID from the Report panel’s internal navigation. Keep its download/print path intact. Assert both boundaries before shipping: the primary navigation contains the promoted label in the requested position, and the Report panel’s visible report collection excludes it.
- For dissertation/proposal content, label an abstract and anticipated findings as **research-stage proposals or hypotheses**, never completed results. Add a concise scope note that distinguishes design requirements/initial-use exploration from effectiveness or pedagogical-outcome claims; retain privacy, human approval, and generalization limits in the visible copy.
- When Chris asks to turn a dissertation idea into a publication-facing surface, place the proposed Korean paper title and abstract at the top of the Dissertation view. Render the title as a distinct semantic treatment (bold and underlined), rather than leaving it as ordinary body copy. Keep the abstract around a conventional Korean abstract length, leave uncollected findings as an explicit `ooo` placeholder, and do not imply completed results. In the middle of the methodology section, add a readable responsive HTML table that maps research phase → material/analysis method → output. For an exploratory educator-AI study with expert interviews and a short single-case log, recommend reflexive thematic analysis for interviews, a task–approval–evidence–exception matrix for design translation, within-case pattern matching plus process tracing for the log, and participant/second-coder/negative-case checks for interpretation. State that descriptive quantitative counts are supplementary, not effectiveness evidence. Keep this ordering and table treatment consistent in browser HTML download/print output as well as the live view.
- For design-education trend reports, treat AI use as a learning-process question rather than a tool-adoption binary: connect problem framing, exploration, critique, disclosure/provenance, revision, and assessment. Separate evidence for AI literacy constructs, studio/creative-process studies, and ethics/disclosure from the editorial recommendation; state participant/task/course limits explicitly.
- Verify each cited DOI against a scholarly metadata index as well as its public DOI resolver where practical. Publisher endpoints can deny automated access even when the record is valid; in that case, accurately label the report source as `초록·메타데이터 확인` and do not imply full-text review.
- A package-design report should assess the full experience chain—attention/selection, information interpretation, use, and disposal/reuse—rather than treating packaging as a graphic-only artifact. Keep retail, label, material, and sustainability evidence scoped to the study’s product category, country, and method.
- If the user specifies an approximate length such as 3,000 Korean characters, measure **Hangul body text only** for every tab before publishing. Treat 3,000 as a target range of roughly 2,700–3,300; if an added tab is materially shorter, expand or explicitly flag it before claiming consistency. Do not count headings, sources, prompts, or shared UI copy toward the requested body length.

### Replacing the source graphic of a manifest-backed mockup example

When Chris asks to change a specific mockup example from one numbered Design DNA/Midjourney graphic to another, treat it as a **derived-asset replacement**, not a metadata-only edit:

1. Start in a fresh detached worktree from `origin/main`. Locate the exact example by stable ID and map its current source graphic, item count, output paths, hashes, prompts, and the selected replacement graphic from the canonical public archive.
2. Re-render every composite item belonging to that example with the requested source graphic while preserving each approved base mockup’s composition, product silhouette, lighting, and framing. Store the replacement images under a new dated revision directory; do not overwrite an older published revision in place.
3. Atomically replace the example’s derived records in the public manifest: `sourceGraphic`, per-item image paths, hashes, and source-aware prompt/provenance fields. Assert the expected item count, source title/ID, PNG dimensions, and SHA-256 agreement for every item before staging.
4. Run a visual acceptance pass across the output set—not only file/decode checks. Confirm the new motif is visibly applied to the intended printable/label surface, preserves the base product and camera treatment, and contains no watermark or unintended generated text. If a base mockup itself has incidental physical markings, distinguish that from the requested graphic rather than repeatedly regenerating without improving the result.
5. Run data validation where compatible with the current public-data inventory, plus lint, production build, `git diff --check`, an added-lines credential-pattern scan, and explicit-path staging. A generic validator failure caused by an unrelated pre-existing dataset must be reported accurately; it does not replace the focused integrity assertions.
6. After the exact Pages workflow succeeds, fetch the live manifest and assert the requested source title plus expected derived item count. Fetch every new live image for `200 image/png`; perform a live DOM/click smoke test when a compatible browser is available. In the completion note, include the stable Pages URL and full navigation path to the changed mockup example.

### Fast art-direction reversion after a just-published mockup-source swap

When Chris reviews a newly deployed source-graphic replacement and says the result feels awkward, treat that as a visual acceptance correction—not a request to merely rename the manifest back.

1. Use the newly requested numbered graphic as the canonical source and regenerate the complete derived example set. Keep the current published revision intact in Git history; publish the correction under a new cache-busting revision directory.
2. Re-run visual QA across representative object types (for example bottle/cylindrical label, flexible tube or carton, and cap/detail surface) before publishing. Judge motif scale, crop, surface fit, silhouette/camera preservation, incidental text/watermarks, and whether the overall palette feels coherent with the original object scene.
3. Atomically update all source fields, per-item paths, prompts/provenance, dimensions, and hashes. Do not mix assets from the rejected and accepted source graphics inside one visible example.
4. Re-run focused asset integrity assertions, lint, production build, staged-path/credential checks, the exact Pages workflow, and live manifest plus 10/10 image probes. In the delivery, state the replacement graphic plainly and provide the stable Pages URL and navigation path.

## Detailed field guide
See [the asset-delivery field guide](references/static-webapp-asset-delivery.md) for asset-externalization details and known verification pitfalls.
