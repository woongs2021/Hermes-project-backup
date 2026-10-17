# Iterative webapp graph polish and research cross-linking

Use this reference for Chris-facing Hermes/OBD webapp polish when graph legibility and research navigation are refined through repeated visual feedback.

## Graph stretching without visual distortion

When a graph needs to feel wider on desktop but its markers/text become distorted:

1. First identify whether the SVG is constrained by default aspect-ratio behavior. `preserveAspectRatio="none"` can make the line use the full horizontal card width, but it also stretches SVG text and circles.
2. Keep the wide SVG line geometry, but remove distortion-prone presentation from the SVG:
   - Remove SVG `<text>` labels and render axis labels in an absolutely positioned HTML layer.
   - Remove SVG `<circle>` markers and render dots in an absolutely positioned HTML layer.
   - Keep line/polyline/guide elements inside SVG and add `vector-effect: non-scaling-stroke` so strokes do not thicken under scaling.
3. Map HTML overlay coordinates to the SVG viewBox, not naive percent values. If the viewBox is `0 0 100 86`, use:
   - `left: x%`
   - `top: (y / 86) * 100%`
4. Keep dot and card layers separate:
   - Dot layer: stays exactly on the line coordinate.
   - Card layer: can use an additional vertical offset to float above the line for legibility.
5. Verify with browser measurements, not visual guessing:
   - SVG text/circle count should be 0 if labels/dots were externalized.
   - Dot rect width/height ratio should be 1.
   - Label computed `transform` should be `none`.
   - Dot center should be within ~1px of the expected SVG line coordinate.
   - Card bottom should sit above the line if cards are meant to be visually separated.
   - Check mobile/tablet/desktop overflow and console/page errors.

## Monthly shortlist → Research detail linking

When Monthly top candidates should open the matching Research detail:

1. Prefer item-id routing over title matching.
2. Convert shortlist rows from static containers to `<button>` elements with accessible labels.
3. Lift the selected item id to the parent `App` state.
4. On click:
   - switch active tab to Research,
   - clear query/lane filters if necessary so the target item is visible,
   - set the Research selected id,
   - update hash to `#research`,
   - optionally scroll to top for context.
5. Verify with Playwright/browser checks:
   - Before click: Monthly hash/state.
   - After click: hash is `#research`.
   - Research detail title equals shortlist title.
   - Active research card title equals shortlist title.
   - No console/page errors.

## Research detail readability pattern

For Chris-facing 1-pick research detail pages:

- Keep the title smaller and less heavy than hero copy.
- Split detailed explanation into function-based paragraphs: claim/validation, Chris relevance, source/local/duplicate context, judgment frame.
- Use visible paragraph gaps and generous line-height.
- Reduce inline bold weight rather than making many terms visually loud; reserve stronger emphasis for the main content only.
