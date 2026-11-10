# Package Midjourney + Mockup batch publication

Use this for Chris’s Design DNA package-mockup synthesis requests.

## Contract

- Raw source collection: `Package Mockup Assets` (`package-mockup-assets`), currently ten package references.
- Synthesized lane: `Midjourney + Mockup` with a peer underline subtab:
  - `tabId: "package-mockup"`
  - visible group title: `Package Mockup`
- The webapp’s Midjourney mockup group map is explicit. Add the Package group in `midjourneyMockupGroups`; adding only a manifest `tabId` will not make a new tab visible.

## Ordered example batches

When Chris gives Midjourney numbers, preserve their exact order.

- One requested source number = one collection named `Package Mockup Example N`.
- Each collection has `mockupCollectionId: "package-mockup-assets"` and ten items by default, one for every source package mockup.
- Item titles are `Package Mockup Example N-1` through `Package Mockup Example N-10`.
- Append example records atomically only after every requested image has passed generation and review. Never expose a partly generated collection in the public manifest.

## Composition direction

Use pattern-only Nano Banana Pro synthesis by default:

- Reference 1: clean original package mockup.
- Reference 2: selected Midjourney motif.
- Output: 3:2, 2K, natural physical surface integration.
- Preserve camera angle, product geometry, crop, lighting, shadows, material texture, and blank printable-surface boundaries.
- Prohibit text, logos, watermarks, placeholder marks, extra objects, sticker overlays, and graphics outside the printable surface.

Surface-specific QA:

- Bottle/can/canister: cylindrical curvature, label seam, reflections.
- Crown cap: crimped-metal shape and highlight behavior.
- Carton/tube: folds, edges, tube curvature and crimp.
- Wood gift crate: wood grain, inset label plane, bottle placement and shadows.

## Publication verification

1. Make a contact sheet and visually reject geometry changes, pasted-on patterns, altered products, unreadable artifacts, or unwanted text.
2. Save accepted public PNGs under `public/assets/dna-brand-assets/midjourney-mockup/<example-id>/<date>/` and mirror originals to the durable local brand-asset archive.
3. Validate manifest JSON, asset hashes and image dimensions; run lint/build.
4. Deploy and verify the live manifest, every new image URL, and the `Package Mockup` tab’s visible example/item counts.
