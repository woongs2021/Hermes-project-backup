# Chris Archive and Midjourney webapp intake lessons — 2026-10

Use when Chris sends images to save into the Hermes webapp archive surfaces, especially when Chris switches between **Design DNA → DNA Dashboard → Midjourney** and **Chris Archive** in the same conversation.

## Routing rules

- If Chris says **“미드저니 에셋에 추가해줘”**, save to the **Midjourney manual rail**:
  - Public manifest: `public/data/midjourney-dna-archive.json`
  - Public assets: `public/assets/dna-archive/midjourney/YYYY-MM-DD/`
  - Local archive: `/opt/data/dna-archive/midjourney/YYYY-MM-DD/`
  - Continue numbering from the existing highest Midjourney item (e.g. 21–23), do not restart from 1.
- If Chris says **“크리스 아카이브에 저장해줘”**, save to **Chris Archive**, even if the immediately previous task was Midjourney-related:
  - Local originals: `/opt/data/chris-archive/images/YYYY/MM/`
  - Entries: `/opt/data/chris-archive/entries/YYYY/`
  - Public manifest: `public/data/chris-archive.json`
  - Public assets: `public/assets/chris-archive/`
- If a save request is followed by additional image-only / “What do you see?” messages in the same burst, treat those images as part of the active save batch unless Chris changes destination. Do not answer each “What do you see?” separately when the active instruction is archive intake.

## Chris Archive batch implementation pattern

1. Build visual-DNA slugs from visible content, not cache filenames.
2. Copy each original image to local archive with `YYYY-MM-DD_<slug>_<sha12>.<ext>`.
3. Write one Markdown entry per image with: summary, Karina first-pass interpretation, visual DNA signals, caution/guardrail, GoYJ review request.
4. Append `index.md` and update `DESIGN_SYSTEM_DRAFT.md` with only tentative cluster-level signals.
5. Copy public assets and append `public/data/chris-archive.json` with public-safe fields only.
6. Build the webapp and verify locally before committing.

## Webapp verification pattern

- Fetch the relevant public manifest and assert the expected count and new titles.
- Fetch every newly-added image URL and require `200` plus `image/*` content type.
- Run Playwright on desktop/tablet/mobile to confirm:
  - tile count equals manifest count,
  - new titles are rendered,
  - representative modal opens,
  - representative modal image has `naturalWidth > 0`,
  - no console/page errors,
  - no horizontal overflow.
- For lazy-loaded grids, do not require every offscreen thumbnail to be immediately `complete`; image URL fetch checks plus representative modal `naturalWidth` are the reliable proof.
- After pushing, poll GitHub Pages manifest until the live count/titles update, then repeat a live browser smoke test.

## Public-safety cautions to encode in entries

- Exhibition/poster references with readable third-party text: archive the image, but extract only layout/material/type principles; do not copy names, slogans, or exact typographic composition.
- Dense terminal/code UI references: mark accessibility/readability risk; use as expert/data-pattern language, not normal consumer UX.
- Neon/high-saturation AI landscapes: mark as color/mood accent only; avoid turning them into the default Hermes aesthetic.
- Orb/sphere/contact references: useful for presence/contact clusters, but watch for repetitive sphere tropes; GoYJ review should decide whether it adds new evidence or only supports an existing cluster.
