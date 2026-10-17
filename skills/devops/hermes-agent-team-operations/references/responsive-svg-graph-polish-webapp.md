# Responsive SVG graph polish for Chris-facing webapps

Use this when tuning an SVG-based graph in the Hermes/OBD webapp after Chris gives perceptual feedback such as “desktop x-axis is too short,” “the line feels too thick,” “the dots/labels look stretched,” or “cards overlap the line.”

## Session-proven pattern

1. **Separate width expansion from visual element distortion.**
   - If the desktop graph looks too narrow inside a wide card, the root cause may be SVG aspect-ratio preservation, not only CSS margin.
   - `preserveAspectRatio="none"` can make the plotted line use the full card width, but it will also horizontally stretch SVG-native `<text>` and `<circle>` elements.

2. **Keep stretched SVG only for scalable geometry.**
   - It is acceptable to stretch the SVG coordinate space for `line`, `polyline`, and guide geometry when the desired result is a wider x-axis.
   - Add `vector-effect: non-scaling-stroke` to axes, guide lines, and data polylines so stroke weight does not scale visually with the stretched viewport.
   - For very delicate Chris-facing graph lines, CSS source values around `0.25px` plus reduced opacity can read better than `0.5px` or `1px`; verify the CSS source because browser computed style may normalize sub-pixel SVG strokes to `1px`.

3. **Move non-stretchable visuals out of SVG.**
   - Do not leave axis labels or dots as SVG `<text>` / `<circle>` when using `preserveAspectRatio="none"`.
   - Render axis labels in an absolutely positioned HTML layer over the graph so text keeps normal proportions.
   - Render dots in an HTML layer (`span`/button/etc.) with fixed width/aspect-ratio so circles remain circular.

4. **Convert y positions to the SVG viewBox coordinate system.**
   - If the SVG viewBox is `0 0 100 86`, HTML overlay `top` values must use `y / 86 * 100%`, not raw `y%`.
   - Raw `y%` will place overlay dots/cards below the corresponding SVG polyline after the SVG is stretched or if the viewBox height is not 100.

5. **Separate dots from cards.**
   - Keep small dots exactly on the line.
   - Lift explanatory cards upward with a separate card offset variable so the data point remains anchored while the card reads as a floating annotation.
   - Verify both card center and card bottom are above the line if the requirement is visual separation, not just center offset.

## Verification probes

Use browser-level assertions, not just source diff:

- Current live JS/CSS asset names changed after GitHub Pages deployment.
- CSS source contains the intended sub-pixel stroke (`stroke-width:.25px`, etc.).
- SVG has `preserveAspectRatio="none"` only if necessary for desktop width.
- SVG-native text/circle count is `0` when using stretched SVG geometry.
- HTML dot rectangles are square (`width == height`, ratio `1`).
- Axis label computed transform is `none` and font size is normal CSS px/rem, not tiny SVG units.
- Dot center is aligned to the expected SVG coordinate:
  - expectedX = svg.left + `(x / 100) * svg.width`
  - expectedY = svg.top + `(y / viewBoxHeight) * svg.height`
- Card bottom sits above line Y by a positive margin on mobile/tablet/desktop.
- Point/card overflow count is `0` for mobile, tablet, and desktop.
- Console/page errors are `0`.

## Pitfalls

- A graph can look “positionally correct” but still feel wrong if circles and text are stretched by `preserveAspectRatio="none"`.
- `getComputedStyle(svgLine).strokeWidth` may report `1px` even when bundled CSS source contains `.25px`; check the CSS asset text for sub-pixel values.
- Updating only desktop may regress mobile card overlap; test all three viewport classes after every offset change.
