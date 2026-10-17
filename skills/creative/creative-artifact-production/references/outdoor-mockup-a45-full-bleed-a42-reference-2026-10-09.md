# Outdoor Mockup A-4-5 full-bleed correction using A-4-2 as print reference

Use when Chris says a multi-surface Outdoor Mockup item, especially `A-4-5`, is still not “꽉차게 합성” after earlier seam/card corrections.

## Session lesson

For `Outdoor Mockup A-4-5` with `Midjourney 31 — Torn Burgundy Olive Paper Collage`, Chris asked to use `A-4-2` as a reference. The useful reference value was not geometry; it was **natural paper-print integration**: burgundy/olive MJ31 material felt fused into a physical surface without a sticker edge.

The repeated failure mode was that Kling preserved the original white board/booklet lower bands and cream paper fields even when prompts said full-bleed. This made the result read as partly unprinted paper, despite correct seams and same-source card/booklet motifs.

## Recommended workflow

1. **Inspect the criticized item only.** Identify whether the problem is coverage, seam/step, wrong motif, or dirty/sticker edges. For A-4-5 the main issue was coverage: lower white bands and a cream blank-looking field.
2. **Use a nearby accepted item as a print-quality reference.** If Chris names `A-4-2`, include it as a reference for natural MJ31 paper integration, not as a geometry target.
3. **Create a strong rough direction image** that paints every visible board/card face edge-to-edge, including lower bands and the small name-card. Keep seam/step lines visible in the direction image.
4. **Do not publish a rough/local patch if it looks patched.** Local/PIL fill can solve coverage but may create collage/sticker seams. Treat it as a direction/reference unless it is visually clean enough for final publication.
5. **Run Kling naturalization from:**
   - rough full-bleed direction image;
   - original clean mockup geometry;
   - accepted print-quality reference such as `A-4-2`;
   - prior structured version as caution/reference;
   - source Midjourney 4K motif.
6. **Generate multiple candidates.** Models may reintroduce white bands. Compare naturalized candidates against rough directions and the current published item, not just against each other.
7. **Choose the best tradeoff honestly.** If no candidate eliminates every light lower band, prefer the one that best reduces blank/cream-field reading while preserving natural integration, seam/step, and small-card same-source use.
8. **Publish with a cache-busting final filename** such as `rev04_full-bleed-a42-ref`, update only that manifest item, and verify live manifest, direct asset URL, hash, dimensions, and browser probe.

## Prompt clauses that helped

- “Use A-4-2 as the quality/style reference for natural Midjourney 31 print integration on paper.”
- “All visible faces of left rear board, right rear board, and small front name-card must be fully printed edge-to-edge.”
- “No blank white lower band, no unprinted paper base, no empty cream field, no partially blank small card.”
- “Preserve seam, overlap edge, paper thickness, depth step, separate boards, natural shadows.”
- “Make the lower printed areas look naturally printed into the paper, not patched, not sticker, not dirty mask.”

## QA checklist

- [ ] Rear left board/booklet has no blank-looking lower band.
- [ ] Rear right board/booklet has no large empty cream field.
- [ ] Small front name-card is printed edge-to-edge with same-source MJ31.
- [ ] Seam/step/overlap stays visible; boards do not become one panorama.
- [ ] Print feels fused into paper like the accepted reference, not pasted.
- [ ] No pseudo-text, logo, UI, dirty mask, or broken geometry.
