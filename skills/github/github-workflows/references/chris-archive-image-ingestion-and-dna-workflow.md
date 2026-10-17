# Chris Archive image ingestion and DNA workflow

Use when Chris sends an image with “추가해줘” for Chris Archive, especially when the webapp must stay in sync.

## Trigger and intent

- If Chris attaches an image and says `추가해줘`, treat it as approval to add the image to Chris Archive without another confirmation.
- If Chris attaches an image without an add phrase, ask before archiving.
- The archive goal is not just storage: each image is source material for later Design DNA extraction and brand/package/system asset generation.

## Ingestion steps

1. Inspect the image visually and write a concise first-pass analysis from visible evidence only.
2. Compute a content hash for the source image and use a safe public filename:
   - avoid secret-like words in public asset filenames, especially `token`, because broad `.gitignore` patterns may exclude them from Pages deployment.
   - include date, descriptive slug, and a short hash suffix.
3. Check exact-duplicate hashes before adding:
   - archive images under `/opt/data/chris-archive/images/**/*`.
   - webapp public assets under `august-dashboard/public/assets/chris-archive/`.
   - if an exact duplicate exists, do not create another public tile unless Chris explicitly wants a duplicate narrative entry.
4. Save the original/archive copy and an entry note:
   - archive image: `/opt/data/chris-archive/images/YYYY/MM/YYYY-MM-DD_slug_hash.jpg`.
   - entry note: `/opt/data/chris-archive/entries/YYYY/YYYY-MM-DD_slug.md`.
5. Update `/opt/data/chris-archive/index.md` and `DESIGN_SYSTEM_DRAFT.md` with only tentative extraction candidates.
6. Update the webapp manifest `august-dashboard/public/data/chris-archive.json` and copy the asset into `august-dashboard/public/assets/chris-archive/`.
7. Build and verify before reporting completion.

## Entry note structure

Keep notes compact but reusable for DNA analysis:

- Short description
- Visible content
- Visual tags
- Color observations
- Typography observations
- Texture / material observations
- Layout / composition
- Metaphor / system meaning
- Product / UX implications
- Aesthetic score
- Karina interpretation
- Go Youn-jung review brief
- Extraction candidates

## Webapp verification checklist

- `npm run build:public` succeeds.
- Manifest item count equals rendered tile count.
- New tile is findable by title.
- New modal opens and its image reports `complete && naturalWidth > 0`.
- Desktop/tablet/mobile grid counts still match current product expectation: desktop 6 columns, tablet 3 columns, mobile 2 columns.
- All manifest `imageSrc` assets return HTTP 200 and image content type.
- Exact duplicate hash count is zero after dedupe/add.
- Live GitHub Pages confirms the new manifest item and public asset after cache/deploy propagation.

## DNA threshold pattern

When Chris says a target count like “60개 했으니까 … DNA분석 들어가자,” treat the count as a milestone:

- Finish the requested final ingestion and webapp sync first.
- Verify the archive count exactly.
- Then the next session/task can move into cross-image Design DNA analysis.
- For the DNA phase, synthesize clusters across images rather than narrating each image one by one.

## Pitfalls

- The webapp loader sorts items by date then title, so the newest ingested item may not visually appear as the literal last tile if another item shares the same date and sorts later alphabetically. When verifying a new item, locate it by title/id rather than clicking only `.last()`.
- Do not over-preserve third-party campaign wording or brand-specific UI copy. Extract layout, color, material, type, and metaphor principles; avoid copying literal copy/branding into future assets.
- Do not stop at local file writes. Chris expects the public Pages link to reflect archive additions when the webapp is part of the request.