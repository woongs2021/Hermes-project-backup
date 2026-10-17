# GoYJ reference-to-motif reinterpretation lessons

Use this when Chris says GoYJ/DNA candidates look too similar to the Chris Archive references or says the agent should use references visually but reinterpret them as graphic motifs.

## Session learning

In the 2026-10-02 Chris Archive batch, the first GoYJ one-shot passed the newly archived images as direct `--image-references` to `gpt_image_2_5`. Even though the prompt said "do not copy," the outputs still looked like close derivatives of the source poster/object/orb/landscape/UI. Chris corrected the approach: the references should guide visual taste, but the generated outputs should be original graphic motif materials.

Durable lesson: for GoYJ DNA motif candidates, direct image-reference input can overpower the desired abstraction. When Chris asks for reinterpretation, do not pass source images as image references by default. Extract principles first, then prompt text-only.

## Correct workflow

1. Read the Chris Archive entries and identify abstract design principles:
   - surface logic
   - rhythm / spacing
   - material mood
   - color tension
   - crop behavior
   - layer behavior
   - negative-space structure
2. Explicitly list what must not be copied:
   - exact composition/layout
   - literal poster, phone, landscape, sun, orb, helix, object, UI screen
   - readable text, numbers, logos, third-party marks
3. Generate with `gpt_image_2_5` as **text-only prompts** unless Chris specifically asks for image-reference fidelity.
4. Reframe each candidate as a reusable motif role:
   - surface field
   - line/stroke overlay
   - color/gradient plate
   - repeat/data texture
   - accent/signal fragment
5. QA with a contact sheet and reject candidates that still look like:
   - copied source artifacts
   - a finished poster/artwork
   - a phone/UI screenshot
   - a literal object remake
   - generic AI neon/glassmorphism
6. Store in a fresh temporary run folder and mark as not selected/published until Chris says `저장해줘`.

## Prompt pattern

```text
PURE 2D GRAPHIC MOTIF MATERIAL ONLY for future brand, package, mobile UI, and mockup composition.
The source archive is used only as visual inspiration, never as a template.
Do not recreate the reference image, do not imitate its exact composition, object, poster, phone, sun, orb, helix, or layout.
Translate only abstract visual principles into a new composable graphic motif: surface logic, rhythm, material mood, color tension, crop behavior, negative space, and layer behavior.
Square 1:1. Useful for cropping, masking, overlaying, repeating, or placing on surfaces.
No readable text, no letters, no numbers, no logos, no watermark, no poster, no app icon, no UI screenshot, no product mockup, no people, no photo, no literal object copy, no generic AI startup neon, no glassmorphism cliché, no exact reference layout.
```

## Example translation moves

- Poster reference → cut-edge editorial surface field, not a poster.
- Helical/object reference → protected aperture line system, not a helix object.
- Orb/contact reference → warm relational gradient plates, not glass balls.
- Neon landscape reference → muted spectral bands, not a landscape/sun scene.
- Coded phone UI reference → nonlinguistic diagnostic mesh, not a screen or fake UI.

## Partial save + regenerate pattern

When Chris approves some candidates and rejects others in the same message, do not rerun the whole set.

1. Save/publish the approved numbers first using the normal DNA Dashboard selected-asset workflow.
2. Regenerate only the rejected numbers in a fresh temporary folder.
3. Change the underlying **visual family**, not just color or prompt adjectives. Useful reset moves from the 2026-10-02 correction:
   - paper-cut / editorial field → organic plaster or watercolor color-field surface
   - aperture / line overlay → flat modular hinge / slot / block geometry
   - diagnostic data mesh → quiet raster-weave or textile-like repeat pattern
4. QA the regenerated subset with a contact sheet before delivering.
5. Keep regenerated candidates temporary until Chris explicitly says `저장해줘` for them.

## Pitfall

Do not assume a negative prompt is enough to prevent copying when the source image is passed as an image reference. If Chris's goal is abstract reinterpretation, the safer default is text-only principle extraction plus QA.

Do not treat Chris saying “1,2 are still like before; save 3,4; regenerate 1,2,5” as permission to alter the approved 3,4. Save the approved candidates first, then separately regenerate only the rejected numbers.