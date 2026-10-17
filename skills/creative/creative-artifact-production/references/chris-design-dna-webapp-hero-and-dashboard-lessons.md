# Chris Design DNA webapp hero / dashboard lessons

Use this when modifying Chris's Hermes webapp `Design DNA`, `Chris Archive`, or `DNA Dashboard` visual sections.

## Durable preferences from the Design DNA iteration

- `Chris Archive` is for reference evidence. GoYJ-generated selected outputs belong under `Design DNA → DNA Dashboard`, not inside Chris Archive.
- If GoYJ images are generated for Design DNA assets, use Higgsfield CLI with `gpt_image_2_5` only unless Chris explicitly changes the rule.
- CSS-only gradient placeholders can feel cheap for key Design DNA visuals. For hero/representative brand visuals, prefer real generated image assets in GoYJ style and then verify them in the page.
- Section-level visuals work better than many small card thumbnails when Chris says the page feels cluttered or “별로”: remove per-card thumbnail clutter and use one 19:10 hero image per conceptual section.
- Number/profile badges for 1–6 can be CSS gradients only; keep them small and content-linked. Do not use black placeholder badges.
- Generated Design DNA hero images should be exact 19:10 framed assets, with no excessive shadow. Align hero image width to surrounding text/card rhythm.

## Proven implementation pattern

1. Generate source images with Higgsfield `gpt_image_2_5`:
   - `export PATH="/opt/data/.npm-global/bin:$PATH"`
   - `HOME=/opt/data higgsfield generate create gpt_image_2_5 ... --aspect-ratio 16:9 --quality high --resolution 2k --variant flare --background opaque --wait`
   - If using local references, upload first with `higgsfield upload create <file> --json` and pass the upload UUID via `--image-references`. Direct local auto-upload can hit presigned S3 signature issues.
2. Crop generated 16:9 source to exact 19:10 with ffmpeg:
   - `ffmpeg -y -i source.png -vf "crop=iw:round(iw*10/19):(iw-ow)/2:(ih-oh)/2" -frames:v 1 output-19x10.png`
3. Store webapp assets under `public/assets/design-dna/...` with stable descriptive filenames.
4. In React, render generated section visuals as `<figure className="..."><img ... /></figure>`; avoid CSS pseudo-art for primary brand visuals.
5. For section hero images, verify:
   - image count and HTTP 200
   - natural size (e.g. 2688×1415)
   - rendered ratio ≈ 1.9
   - desktop/tablet/mobile overflow false
   - intended elements removed (e.g. per-card thumbnails = 0 when Chris asked to remove them)
6. Use Playwright/DOM computed checks rather than only trusting build success.

## Prompt guardrails for GoYJ-style Design DNA assets

Use wording like:

> Original Hermes Design DNA hero image in Go Youn-jung generated graphic style, based on the provided selected Hermes assets as style references. Wide 19:10 hero banner, pure abstract graphic design only, no photography, no person, no human, no face, no portrait, no body, no character, no text, no logo, no icon, no UI chrome, no readable letters, no generic AI neon, no robot, no brain, no clutter. Warm off-white paper, premium editorial minimalism, soft 2D material, refined cobalt/cyan/coral/yellow signal gradients, quiet One UI/Hermes polish, crisp frame-ready composition.

If a generated image introduces faces/people/text/logos, discard and regenerate with stronger negative language; do not publish it.

## UX/layout lessons

- Chris prefers visual acceptance over internal explanation. Make the change, build, live-verify, then give a concise Korean completion note.
- When matching one webapp grid to another, compare computed layout values across desktop/tablet/mobile rather than eyeballing.
- For modal scroll jitter, use stable scrollbar gutters and avoid layout shifts in scrollable overlay content.
- For Design DNA section graphics, exact ratio and framing matters: “딱 떨어지게 프레임에 넣어줘” means the image should sit cleanly inside a defined frame, not float with heavy shadow.
