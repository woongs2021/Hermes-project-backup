# Outdoor framed wall poster replacement + resynthesis lesson

Use when Chris replaces a raw **Mockup** asset such as `Framed Wall Poster On Stone Facade` and then asks to apply an existing **Midjourney + Mockup** graphic to the new mockup.

## Durable lesson

1. Treat the raw mockup lane and the synthesized example lane as two separate assets.
   - Raw mockup: `public/assets/dna-brand-assets/mockup/<collection-id>/...`
   - Synthesized example: `public/assets/dna-brand-assets/midjourney-mockup/<example-id>/...`
2. When replacing a published raw mockup, do **not** rely on overwriting the same public filename.
   - Write a cache-busting filename such as `_rev01`.
   - Update `brand-mockup-assets.json` `imageSrc`, `downloadSrc`, `assetHash`, `width`, `height`, and `updatedAt`.
3. Verify the **Mockup** lane first before regenerating the synthesized example.
   - Live manifest should reference the new raw mockup filename.
   - Live image hash should match the local file hash.
   - Browser/Playwright should show the raw mockup tile loading the new filename.
4. For the downstream generated example, regenerate from the **new raw mockup** as the primary geometry reference.
   - Reference order for Kling: (1) new raw mockup, (2) previous synthesized example as rough direction only, (3) source motif/graphic.
   - Prompt to preserve wall/frame/glass/foreground/background objects and integrate the graphic into the poster/glass surface naturally.
5. Publish the synthesized example with a new revision filename as well, then verify the **Midjourney + Mockup** lane separately.

## Pitfalls seen

- Same-filename replacement can appear unchanged due to browser/GitHub Pages caching even when the file content changed.
- Verifying only the manifest is not enough; verify the live image bytes/hash and the actual DOM image `src` in the relevant lane.
- Raw mockup replacement does not automatically update the generated example; it must be explicitly regenerated or it will still show the old geometry.

## Acceptance checklist

- Raw Mockup lane tile uses the new raw mockup revision filename.
- Generated Example tile uses a separate new synthesized revision filename.
- Both live image URLs return `200 image/*` and match local hashes.
- Desktop/tablet/mobile UI load without console errors or horizontal overflow.
- The user-facing reply includes the cache-busted live link and, when useful, a live thumbnail capture.
