# Design DNA Brand Asset Mockup Workflow

Use when Chris asks to add or maintain **Design DNA → DNA Brand Asset** moodboard/mockup surfaces in the Hermes webapp.

## Structure Chris wants

- Treat **DNA Brand Asset** as a top-level section inside the existing `Design DNA` page, alongside `Design DNA` and `DNA Dashboard`.
- Inside DNA Brand Asset, keep two internal tabs/chips:
  - **Mockup**: user-supplied or approved mockup reference assets.
  - **Midjourney + Mockup**: later combined/synthesized outputs; leave empty until assets exist.
- If a tab has no assets yet, keep it quiet and centered with only `준비중입니다`. Do not add explanatory filler or placeholder thumbnails unless Chris asks.

## Mockup collection pattern

- Store mockup collections separately from DNA motif images.
- Recommended manifest: `public/data/brand-mockup-assets.json`.
- Recommended assets root: `public/assets/dna-brand-assets/mockup/<collection-id>/YYYY-MM-DD/`.
- For synthesized outputs, use a separate `examples[]` rail in the same manifest, with assets under `public/assets/dna-brand-assets/midjourney-mockup/<example-id>/YYYY-MM-DD/`.
- For logo-bearing examples, Chris prefers natural printed/image-fused logo integration over perfect flat legibility. It is acceptable if not every mockup shows the whole word, as long as at least one example is clearly readable and the set feels physically plausible.
- If Chris says the logo still feels unnatural after image-fusion attempts, remove the logo entirely rather than continuing to force it. Revert to **pattern-only** synthesis, update titles/descriptions/status to remove logo language, and keep the example focused on surface/pattern application.
- For each collection, include:
  - `id`, `title`, `created`, `status`, `description`
  - `items[]` with `id`, `title`, `description`, `imageSrc`, `assetHash`, `width`, `height`
- Group related assets under a named collection rather than adding loose cards. Example: `Coffee Mockup Assets` for cup, pouch, counter, takeaway, and cafe sign references; `Outdoor Mockup Assets 1/2` for outdoor stationery, apparel, mobile, tote, wall, and sign mockup references.
- Preserve source images as provided; do not crop, compress, upscale, remaster, or synthesize unless Chris explicitly asks.
- For repeated outdoor/lifestyle batches, follow `references/design-dna-outdoor-mockup-collections.md`: append a new `collections[]` entry such as `outdoor-mockup-assets-2`, store public/local assets under the matching collection ID, and verify the new collection tab on live desktop/tablet/mobile.
- When several raw mockup collections exist, group Coffee/Outdoor/etc. under a top-level **Brand Mockup Assets** lane and keep **Midjourney + Mockup** as the peer lane. Chris asked for the raw collection selector to be underline-style tabs, not card chips; implementation/CSS/QA details are in `references/design-dna-brand-mockup-tab-hierarchy-and-subtab-style.md`.

## Webapp implementation pattern

- Add a lightweight loader module such as `src/brandAssets.ts` with fallback manifest + `loadBrandMockupAssets()`.
- In `DesignDnaPanel`, load mockup assets alongside GPT/Midjourney manifests.
- Render the Mockup tab as a collection header plus a responsive moodboard grid.
- Keep `Midjourney + Mockup` as centered `준비중입니다` until Chris sends actual combined outputs.
- Once assets exist, make every DNA Brand Asset tile clickable. Use button tiles, not inert figures, so keyboard/focus states work.
- Reuse the DNA Dashboard modal language for enlarged preview: backdrop, rounded card, large image, right-side metadata, close button, and mobile single-column layout.
- Populate brand asset modals with useful details when available: collection title, created date, status, image size, item id, collection note, synthesis tool, source graphic, logo text/treatment, and source policy. For mockup-only assets, include their role as brand-surface references.
- Keep visual parity with Chris Archive / DNA Dashboard: clean cards, rounded image frames, no heavy shadows, no busy placeholder content.

- For Coffee Asset examples, keep raw **Coffee Mockup Assets** and synthesized **Midjourney + Mockup** outputs as separate tabs/rails. Use simple sequential English collection titles like `Coffee Mockup Example 1`, `Coffee Mockup Example 2`, `Coffee Mockup Example 3`; item titles should be `Coffee Mockup Example 1-1`, `Coffee Mockup Example 1-2`, etc. Avoid skipped numbering such as 1/2/5 and avoid descriptive item names in the visible title once Chris asks for clean numbering.
- Do not hardcode the webapp to a single example id such as `coffee-asset-example-01`. Render the full `examples[]` array as stacked collections so later Example 02/03/04 sets remain visible alongside earlier examples.
- When Midjourney + Mockup grows beyond Coffee examples, split `examples[]` into sub-tabs using a lightweight manifest field such as `tabId` (`coffee`, `outdoor-mockup-1`, `outdoor-mockup-2`). Keep Coffee examples with no `tabId` backward-compatible by grouping them under Coffee. Reuse the same centered underline subtab style and moving indicator as Brand Mockup Assets. For Outdoor visible titles, use simple English numbering only: collection titles `Outdoor Mockup Example 1`, `Outdoor Mockup Example 2`; item titles `Outdoor Mockup Example 1-1`, `Outdoor Mockup Example 1-2`, etc. Do not expose descriptive synthesis names like `Wall Poster Cropped Amber Surface HQ Natural Natural` as visible titles.
- For outdoor Midjourney + Mockup composites, prefer full-surface applications unless Chris explicitly asks for small marks. Chris corrected the workflow on 2026-10-06: do **not** use small mark-only or solid-only treatments for this rail; make all mockups full-surface composites, with variation coming from cropped motif placement. Preserve source mockup lighting, fabric/paper folds, shadows, foreground objects, and surface texture. If local/PIL compositing leaves gritty dust, visible mask edges, shadow spill, distorted product surfaces, weird light blooms, deleted foreground posts/bollards, rectangular overlays, see-through wall/brick texture inside fabric, or the user says the same area is still not fixed, stop patching the derivative and reset to the original mockup geometry. Use Kling `image_to_image` / `kling-image-v3_0_omni` with references that prioritize: (1) original mockup, (2) current best direction only as a rough guide, (3) source graphic, plus a calm tone reference or the user's marked screenshot if needed. Treat circles/arrows/markup as the exact defect target, but explicitly prompt not to reproduce the annotation. If frustration appears, generate 2+ fresh candidates, compare a contact sheet, and choose the one that clearly fixes the defect rather than the one closest to the previous version. Use new cache-busting filenames and verify contact sheet + live desktop/tablet/mobile. For poster/glass/shadow bands, bright-white background suppression, and banner transparency fixes, follow `references/design-dna-mockup-shadow-integration-lessons.md`; for fabric banners, explicitly prompt for “opaque printed fabric, no wall/brick texture inside the fabric, no hole/transparent patch,” and allow metaphor area/crop to vary for naturalness.
- Once the webapp already renders `examples[]` generically, adding a new Coffee Pattern Example usually requires only: generate/store six assets, append one manifest entry under `examples[]`, build, and verify the new collection count/tile count/modal. Do not rework React for each new example unless the UI structure itself changes.
- Logo-word selection may be made by Karina when Chris delegates it. For OBD/onboarding-oriented coffee brand examples, `ONBOARD` is a good first logo word because it connects project entry, onboarding, and a calm brand-system doorway without overclaiming.
- Keep visual parity with Chris Archive / DNA Dashboard: clean cards, rounded image frames, no heavy shadows, no busy placeholder content.

## QA checklist
## Logo-image fusion pattern for mockups

When Chris asks for a logo to feel naturally merged into a generated mockup, avoid plain post-generation text overlays as the final answer unless he explicitly wants editable typography. Better pattern:

1. Generate or prepare the mockup surface first without text.
2. Render the logo as a transparent image reference with the requested font/treatment, for example Open Sans 700, no shadow, no stroke.
3. Feed both the mockup and the logo image into Higgsfield Nano Banana Pro and prompt for **physical ink/material integration** rather than perfect text-layer readability.
4. If Chris says the logo can be partially obscured, prioritize natural surface behavior over full word visibility. It is acceptable for the logo to bend, crop, or blend with pattern/curvature as long as at least one hero/example image preserves brand recognition.
5. For “make the logo smaller” requests, create a smaller logo reference image rather than only asking the model to scale it. In the coffee mockup workflow, a 70% logo reference produced a more natural, less overlaid result; a 30% navy corner mark can be used when Chris wants a quiet brand mark on a bright area.
6. Review a contact sheet before replacing web assets; choose the set by naturalness first, not by all-letter legibility unless Chris asks for legibility.
7. If multiple logo-fusion rounds still read as pasted-on or visually awkward, stop forcing the logo. Return to pattern-only mockups, remove `logoText`/`logoFont` metadata from the manifest, rename items from `Onboard...` to `Pattern...`, and describe the example as pattern-only synthesis.

## DNA Brand Asset detail modal pattern

For manifest-backed DNA Brand Asset images, make every asset card clickable and reuse the DNA Dashboard modal visual language:

- Render cards as `<button>` elements, not inert `<figure>` cards, while preserving the visual tile style.
- Use one selected state shape carrying `item`, `collection`, and lane label (`Mockup` or `Midjourney + Mockup`).
- Modal should include a large image, title, created/status, collection title, dimensions, item id, and collection note.
- For synthesized examples, also show synthesis tool, source graphic, logo text/treatment/font when present, and source policy. If a later revision removes the logo, remove logo metadata from the modal/manifest rather than leaving stale `ONBOARD` language.
- Keep public-facing Midjourney + Mockup explanations image-native rather than history/process-native: describe color, surface, material, motif rhythm, composition, and use context; avoid visible copy centered on generation tools, resynthesis, revisions, fixes, ordering history, or previous defects. Check not only `item.description` but also collection `description`, `status`, `synthesisTool`, and root `sourcePolicy`. See `references/midjourney-mockup-detail-copy-pattern.md`.
- Use `object-fit: contain` and the mockup aspect ratio in the modal so generated/package mockups are enlarged without crop.
- Chris prefers the enlarged modal to feel generous: apply the same sizing globally where this modal family is reused, around `width: min(90vw, 1280px)` on desktop and 90% viewport width on mobile. Chris Archive modals should not keep narrower tablet/mobile overrides if Design DNA modals are wider; keep the family visually unified unless he asks otherwise.
- Keep the close `×` button inside the modal card, anchored near the top-right with absolute positioning, not outside the panel or occupying a grid row.
- For desktop image lists, keep Chris Archive and DNA Dashboard grid parity. Chris corrected the 6-column desktop grid to **5 columns** for both lists; preserve tablet/mobile overrides separately.
- Verify both lanes: original Mockup assets and Midjourney + Mockup examples.

## GoYJ pick / Midjourney graphic generation criteria

When Chris asks Go Youn-jung to pick images or generate Midjourney-style graphics for Design DNA / DNA Brand Asset work, use these defaults:

- Prioritize images that can become **brand-system DNA**, not just nice standalone pictures: strong color logic, surface behavior, metaphor, repeatable composition, and asset extensibility.
- Prefer warm, calm, premium, human, tactile, and emotionally stable images over loud AI-startup aesthetics, generic neon, or over-rendered sci-fi surfaces.
- Favor full-surface metaphor potential: images should be usable across posters, fabric, cards, packaging, dashboard panels, and environmental mockups without relying on tiny marks or logo-only placement.
- Look for controlled tension: enough visual energy to feel alive, but not so much contrast/white glare/noise that the mockup set becomes fragmented.
- Avoid obvious AI artifacts, hollow/transparent-looking surface confusion, pasted rectangles, over-bright white voids, illegible pseudo-text, and decorative complexity that will not survive downstream mockup synthesis.
- When generating, create several candidates with intentionally different crop/metaphor distributions, then review them as a contact sheet before saving or publishing. Choose by system usefulness and natural mockup compatibility, not only by first-glance beauty.
- If a generated/mocked-up result repeatedly fails through local patching, reset to the clean original mockup and regenerate with Kling from scratch rather than continuing to patch derivatives.

## Coffee / brand-surface synthesis lessons

- If applying a graphic motif to mockup assets, first create a **pattern-only** synthesis without logo text. This is often the cleanest baseline and may be preferable when logo integration feels artificial.
- Do not rely on image generation to render exact brand text directly. If Chris asks for logo text, make the logo as a separate transparent PNG/reference image, then feed it as an additional image reference; still review for naturalness and spelling.
- When Chris says a logo is not natural, prefer removing or minimizing the logo rather than forcing legibility. For this class of design mockup, natural printed-surface integration matters more than showing every letter.
- Keep manifest copy aligned with the actual asset state. If logos are removed, remove `logoText` / `logoFont` fields and rename items away from logo-specific titles like `Onboard ...`; use `Pattern ...` naming instead.
- For iterative variants, review a contact sheet before replacing web assets. Check: surface integration, no floating overlay, no unwanted text artifacts, no broken crop, no foreground-object damage, no light blooms/rectangular mask artifacts, and whether the result still matches the tab description. If Chris provides a circled/marked screenshot, first name the exact target region and make that marked area the primary acceptance criterion. If Chris points out repeated artifacts after two revision attempts, stop patching patched derivatives; reset to the clean original mockup and rebuild the item from scratch with Kling, allowing motif crop/area changes if needed. When Chris sends a screenshot with a circled/marked problem area, treat that marked screenshot as the primary problem reference before generating or patching; explicitly target the circled region, not a guessed nearby area. If a local patch or partial Kling regeneration fails twice on the same visual issue, stop incremental fixing and create 2 fresh Kling candidates from the original mockup + source motif, then compare and publish the better candidate.
- When Chris marks a precise problem area with a screenshot/circle, treat the marked image as the primary spec before editing. First restate the exact region in visual terms (e.g. “upper-left/center fold,” not just “left-middle”), then target that location. Do not keep patching nearby guessed areas. If a local/PIL patch does not visibly fix the marked area after one attempt, stop patching and regenerate from the original mockup in Kling.
- For stubborn fabric/banner mockup defects that read as transparency, holes, or wall showing through, prefer a from-scratch Kling regeneration from the original mockup plus motif/palette references. Explicitly allow a changed motif crop/area and ask for an opaque printed textile. Generate at least two candidates (e.g. revA/revB), compare against the current version in a contact sheet, and publish the candidate that removes the defect most clearly even if the composition changes.
- When Chris marks a specific defect with a screenshot/circle, treat that marked image as the authoritative problem definition. Do not infer a nearby area from the asset alone. First inspect the marked screenshot, then either target exactly that region or, if the issue has already survived one local patch, regenerate the item from the original mockup with Kling instead of continuing small local masks. It is better to change motif crop/coverage noticeably than to preserve a composition that keeps the defect.
- For stubborn mockup defects, generate at least two from-scratch Kling candidates from the original mockup + source motif + tone reference, make a quick comparison/contact sheet against the current published version, and choose the candidate that removes the defect most clearly before updating the manifest. Do not deploy repeated “almost same” revisions without showing/validating the visible difference.
- For iterative variants, review a contact sheet before replacing web assets. Check: surface integration, no floating overlay, no unwanted text artifacts, no broken crop, no foreground-object damage, no light blooms/rectangular mask artifacts, and whether the result still matches the tab description. If Chris points out repeated artifacts after several revisions, reset to the clean original mockup and rebuild the item rather than continuing to patch the patched derivative. If Chris marks/circles a problem area, treat that marked area as the primary acceptance target before changing any other region. When a published update still appears unchanged, verify manifest path + live DOM src; if the same public filename was reused, switch to a new revision filename to avoid cache ambiguity.
- When Chris marks a problem area with a circle/screenshot, treat the marked region as the ground truth target. Use the marked screenshot as an explicit Kling reference only if needed, but do not assume nearby/lower areas are the problem. If the marked area remains unresolved after one local patch or one generation, stop patching derivatives and regenerate from the original mockup from scratch; create at least 2 fresh Kling candidates and compare them.
- When replacing a published image asset that users have already viewed, avoid reusing the exact same public filename if any viewport/browser may cache it. Prefer writing a revision filename such as `_rev01`, update the manifest `imageSrc`, and verify the live desktop/tablet/mobile DOM is loading the new URL. If the hash changed but the old filename remains, desktop users may still report the old image while mobile/tablet appears updated. Also verify the correct lane: replacing a raw **Mockup** asset does not automatically replace **Midjourney + Mockup** synthesized examples; if Chris expects the generated rail to change, regenerate or update the relevant `examples[]` item with a new filename too.
- If Chris asks to revise only one mockup within an already-published example set, do not regenerate or republish the whole collection. Generate 2+ focused candidates for that one item, compare against the current image in a contact sheet, choose the version that best matches the rest of the set, then replace only that asset file plus its manifest fields (`assetHash`, description, optional `updatedAt`). Keep a backup of the previous asset in the archive/replaced folder, then verify the live image hash and modal/tile rendering.
- When Chris says a specific mockup still “looks unchanged,” “is cropped,” or repeatedly points to a marked/circled defect, stop patching the derivative. Start over from the clean original mockup plus the source metaphor/graphic, remove the previous composite from model references unless it is explicitly needed, generate at least two fresh Kling candidates, and compare them against the current version in a contact sheet. Let the motif area/crop change if needed to solve the physical integration issue. Use a new cache-busting filename and verify both tile and modal image screenshots from the live Midjourney + Mockup rail.
- For Chris-facing proof after a replacement, do not rely on a potentially cropped tile screenshot alone. Also capture the modal image or original image URL/natural dimensions/hash when the user questions whether an asset changed.
- For raw-mockup replacement followed by generated example replacement, do not let the old generated composite dominate the new result. Use the new raw mockup + source metaphor as the primary Kling references; omit the previous composite or use it only as a weak rough guide. If Chris says “it still looks unchanged,” regenerate from the new raw mockup and source metaphor only, then pick the candidate that makes the new mockup geometry unmistakable.
- Thumbnail screenshots can crop generated images because card tiles use fixed visual frames. Do not use a cropped tile capture as the only proof for a generated asset. Verify and, when Chris doubts the result, send both the tile screenshot and a modal/full-image screenshot (or the source image file) showing the uncropped composition and the exact `imageSrc` loaded by the DOM.


## Webapp interaction/layout conventions

- DNA Brand Asset cards should be clickable and open a detailed modal styled like DNA Dashboard. Include large image, collection/title/status/date, dimensions, asset id, collection note, source graphic, synthesis tool, and logo treatment only when present.
- For Chris Archive and DNA Dashboard image lists, desktop should be **5 columns from 1024px upward**. Use an explicit `@media (min-width: 1024px)` rule and ensure tablet rules start at `max-width: 1023px`; otherwise exactly 1024px can accidentally fall into tablet layout.
- Modal width should be consistent across Chris Archive, DNA Dashboard, and DNA Brand Asset: `width: min(90vw, 1280px)` with the close button positioned inside the modal top-right (`position: absolute`). Verify both desktop and mobile.

## QA checklist

- Validate JSON with `python3 -m json.tool public/data/brand-mockup-assets.json`.
- Run the webapp build.
- Browser-verify desktop and mobile:
  - `DNA Brand Asset` top section exists.
  - `Mockup` tab shows the expected collection and item count.
  - Every mockup image loads with nonzero `naturalWidth`/`naturalHeight`.
  - `Midjourney + Mockup` shows the expected asset collection or only `준비중입니다` when empty.
  - Clicking any DNA Brand Asset card opens a modal with image and details.
  - Modal close button is inside the modal bounds.
  - Chris Archive and DNA Dashboard modal widths match.
  - At viewport widths 1023, 1024, and desktop size, verify expected columns (1024+ = 5 columns).
  - No horizontal overflow.
- After deploy, verify the live manifest and each new image URL returns `200 image/*`, then browser-verify the live page rather than trusting local build only. For visual disputes, capture both the tile and the modal/large image from the exact live tab Chris is discussing; tile screenshots can crop by design, so do not use them alone to prove the source artwork changed. If the repo push succeeded but the live manifest remains on the old hash, check the GitHub Actions/Pages deployment status before telling Chris it is just browser cache; a `waiting` Pages deploy means the live site legitimately has not updated yet.


## Communication note

When Chris interleaves “What do you see in this image?” with a concrete save instruction, prioritize the save workflow and include only a concise visual read in the completion note. Avoid interrupting the batch with separate analysis unless the visual content changes what should be saved.
