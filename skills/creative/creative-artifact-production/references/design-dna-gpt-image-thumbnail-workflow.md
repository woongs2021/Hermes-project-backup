# Design DNA GPT Image thumbnail workflow

Use when Chris asks to improve Design DNA infographic/card thumbnails, representative visuals, or profile-like placeholders in the Hermes webapp.

## Durable preference

Chris disliked CSS-only gradient placeholders for Design DNA axes. For representative thumbnails in this area, prefer real Go Youn-jung-style generated images made with Higgsfield `gpt_image_2_5`, especially when the visual is meant to carry brand/DNA meaning.

## Recommended workflow

1. Use the current selected GoYJ/DNA assets as style references when available, especially:
   - `Complete Circle — Outer Stroke Light`
   - `Woven Bar Close-up — Cobalt / Cyan`
2. Generate each axis thumbnail with Higgsfield CLI and **`gpt_image_2_5` only**.
   - Use `HOME=/opt/data` and `PATH=/opt/data/.npm-global/bin:$PATH` in this environment.
   - Upload local reference images first with `higgsfield upload create <file> --json`, then pass the returned upload ID via `--image-references`.
3. Prompt for abstract graphic design, not literal people or UI:
   - wide 19:10 representative card image
   - Go Youn-jung generated graphic style
   - warm off-white paper, cobalt/cyan intelligence, coral/yellow warmth, quiet One UI/Hermes polish
   - no text, logo, readable letters, UI chrome, robot, brain, generic AI neon
   - explicitly forbid people/faces/portraits/bodies; GPT Image may introduce portraits if the prompt says context/human.
4. Higgsfield GPT Image 2.5 may not support exact 19:10. Generate `16:9`, then crop locally to exact 19:10.
   - Example crop: `ffmpeg -y -i source.png -vf "crop=iw:round(iw*10/19):(iw-ow)/2:(ih-oh)/2" -frames:v 1 output-19x10.png`
   - Verify dimensions with `ffprobe`; session target used `2688×1415`.
5. Review a contact sheet before publishing.
   - Reject/regenerate anything with faces, people, text-like marks, logos, or broken artifacts.
   - A small abstract grid or non-readable metadata-like mark is acceptable for editorial evidence; readable text is not.
6. Copy approved thumbnails into the webapp public assets, e.g.:
   - `public/assets/design-dna/thumbnails/<axis-slug>-19x10.png`
7. Use actual `<img>` thumbnails in the cards instead of CSS gradient placeholders.
   - Keep frame ratio `aspect-ratio: 19 / 10`.
   - Use `object-fit: cover` and verify rendered ratio across desktop/tablet/mobile.
8. Verify live after deploy:
   - all 6 images return HTTP 200
   - `naturalWidth/naturalHeight` matches expected generated/cropped size
   - rendered ratio is ~1.9
   - no horizontal overflow on desktop/tablet/mobile

## Pitfalls

- Do not call generated thumbnails “saved GoYJ assets” unless Chris explicitly selects them for DNA Dashboard. Axis thumbnails are webapp section support visuals; DNA Dashboard remains selection-gated.
- CSS gradients are acceptable for small decorative badges, but not as the primary Design DNA axis thumbnail after Chris’s feedback.
- If GPT Image creates a portrait/person, regenerate with strong `no person, no human, no face, no portrait, no eyes, no body, no character` language.
- Avoid heavy shadows in hero/thumbnail frames unless Chris asks for depth; he prefers clean, text-aligned frames in this Design DNA page.
