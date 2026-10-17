# Outdoor mockup full-bleed surface coverage lessons

Use when Chris says a mockup item is not “꽉차게 합성” or that a Midjourney motif is present but does not fully occupy the product surface.

## Trigger pattern

- The seam/step/physical object separation is acceptable, but the graphic still feels under-applied.
- A board/booklet/card contains large blank-looking white, cream, or base-material areas that read as unprinted paper rather than intentional motif color.
- A small front business card/name-card or rear board uses the correct source family but only partially fills the visible face.

## Lesson from Outdoor Mockup A-4-5 / Midjourney 31

Chris rejected A-4-5 even after rev02 because, although the seams and same-source small card were improved, the composition still looked underfilled:

- the right rear booklet had a large cream/blank-looking field;
- the lower portions of the boards still read like original white paper/base rather than full printed surface;
- the small card lower area also looked less fully covered.

This means “same-source card/booklet separation” is necessary but not sufficient. The final composite must read as a full-bleed printed/mockup surface.

## Recommended correction workflow

1. **Inspect only the criticized image first.** Identify which visible surfaces read as unprinted or underfilled before regenerating.
2. **Regenerate only the criticized item** unless Chris asks for the whole set.
3. **Use stronger full-bleed prompt language:**
   - “all visible paper/card/board faces must be fully printed edge-to-edge with the source motif”
   - “no blank white lower band, no unprinted paper base, no empty cream field unless it is clearly part of the source motif and has paper texture/print integration”
   - “the small front name-card must also be fully printed edge-to-edge, not a partly blank card”
   - “preserve seam, overlap edge, paper thickness, shadows, and physical depth while filling each surface”
4. **For multi-surface item 5 cases, generate at least two candidates.** Candidate QA must check both dimensions:
   - physical separation: seam/step/depth and different crops per surface;
   - coverage: no large unprinted-looking zones on any visible face.
5. **Prefer a candidate with full coverage over a candidate with perfect crop aesthetics but obvious blank/unprinted paper.** If no candidate satisfies both, regenerate with a stronger rough direction image that paints every visible face, including lower board bands and the small card.
6. **Publish with a cache-busting rev filename** and live-verify exact manifest path, direct asset URL, and page probe.

## QA checklist for future item-5 revisions

- [ ] Left rear board/booklet is printed to all visible edges.
- [ ] Right rear board/booklet is printed to all visible edges.
- [ ] No lower white/cream band reads as original blank paper.
- [ ] Small front card is fully printed and same-source.
- [ ] Seam/step/overlap remains visible; not a single panorama.
- [ ] Shadows, paper thickness, pebbles/table/background are preserved.
- [ ] No pseudo-text, logos, UI, dirty mask edges, or broken geometry.
