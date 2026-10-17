# Chris Design DNA webapp hero/card image lessons

Use when editing the Hermes webapp `Design DNA` tab, especially Core DNA / Expression Layer infographic sections, GoYJ-generated images, and representative card imagery.

## Lessons from the Design DNA iteration

1. **Avoid CSS placeholder art as final visual identity.**
   - Chris rejected coded gradient placeholders as looking weak/"별로".
   - For meaningful Design DNA imagery, prefer actual GoYJ-style generated graphic assets via Higgsfield `gpt_image_2_5`.
   - CSS-only gradients are acceptable for tiny utility badges, not primary hero/card imagery.

2. **Section imagery should be hero-level, not many small thumbnails.**
   - Six per-card thumbnails made the infographic feel busy.
   - Preferred structure for the two axis sections:
     - Core DNA section: one 19:10 hero image above the three axis cards.
     - Expression Layer section: one 19:10 hero image above the three expression cards.
     - Individual axis cards should stay mostly text + badge + chips, not carry separate generated thumbnails.

3. **Use 19:10 frames consistently for Design DNA hero graphics.**
   - Generate 16:9 source if the provider lacks 19:10.
   - Center-crop to exact 19:10 with ffmpeg, e.g. `crop=iw:round(iw*10/19):(iw-ow)/2:(ih-oh)/2`.
   - Verify natural dimensions and rendered ratio in browser; successful examples were `2688x1415`.

4. **Keep imagery calm and simple.**
   - Chris rejected the Expression Layer hero when it became complex/organic/"징그러워".
   - Safer pattern: simple complete circle / outer-stroke presence mark with only color/gradient changed.
   - If reusing the main circle, avoid making it identical: keep the circular form but shift rim/gradient color, e.g. cyan → pastel magenta/rose.

5. **Badges should be quiet solid pastel, not gradient.**
   - For number badges 01–06, Chris preferred single pastel fills over gradient backgrounds.
   - Good direction: warm beige, pale cobalt, soft sage, pale blue-gray, archive beige, soft rose.
   - Keep text contrast calm but legible.

6. **Cache-bust changed public images.**
   - If replacing a public image at the same path on GitHub Pages, browser/CDN cache can obscure the update.
   - Prefer a new descriptive filename when the visual meaning changes, e.g. `expression-layer-hero-circle-pastel-19x10.png`, then update the TSX reference.

7. **Verify with real browser metrics.**
   - Confirm on desktop/tablet/mobile:
     - 2 section hero images present
     - per-card thumbnails removed
     - hero image asset status 200
     - natural size matches expected image dimensions
     - rendered ratio is ~1.9
     - number badges use solid background (`backgroundImage === 'none'`)
     - no horizontal overflow

## Prompt guardrails for GPT Image 2.5 Design DNA section heroes

Use `gpt_image_2_5` via Higgsfield and keep prompts strict:

- pure abstract graphic design only
- no photography, person, face, portrait, body, character
- no text, logo, icon, UI chrome, readable letters
- no generic AI neon, robot, brain, clutter
- warm off-white paper, premium editorial minimalism, soft 2D material
- refined cobalt/cyan/coral/yellow signal gradients, quiet One UI/Hermes polish

For Expression Layer, if unsure, prefer:

> one complete circle / open ring, outer rim only, no complex texture, no organic forms, color-shifted from the main hero so it is related but not identical.
