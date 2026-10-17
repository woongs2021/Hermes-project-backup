# GoYJ DNA Dashboard webapp pattern

Use when Chris asks to save Go Youn-jung generated graphic assets into the webapp, adjust the Design DNA dashboard, or replace Design DNA hero imagery.

## Current product contract

- `Chris Archive` is for user-provided inspiration/reference images and first-pass analysis.
- `Design DNA → DNA Dashboard` is for GoYJ-generated assets that Chris explicitly selected with `저장해줘`.
- Do not publish or preserve unselected GoYJ candidates in the webapp or final public manifest.
- GoYJ candidate generation uses five 1:1 graphic candidates on Mon/Wed/Fri and must use GPT Image 2.5 unless Chris explicitly changes the model.

## Webapp placement rules

1. Keep GoYJ saved/generated images under **Design DNA → DNA Dashboard**, not under Chris Archive.
2. The DNA Dashboard tile/grid system should match the Chris Archive dashboard exactly across breakpoints:
   - desktop: 6 columns
   - tablet: 3 columns
   - mobile: 2 columns
   - same gap, tile padding, border radius, image min-height, image radius, card shadow/hover/focus behavior.
3. Tile click should open a detail modal with:
   - large image
   - status/date
   - GoYJ analysis
   - DNA cluster chips
   - generation prompt
   - save policy / manifest note
4. Verify with computed browser checks, not visual assumptions: compare Chris Archive grid/tile/img styles against DNA Dashboard styles for desktop/tablet/mobile and assert no horizontal overflow.

## Data and asset pattern

- Canonical selected source: `/opt/data/dna-archive/selected/YYYY-MM-DD/selected-manifest.json`.
- Public assets: `public/assets/dna-archive/YYYY-MM-DD/<asset-name>.<ext>`.
- Public manifest: `public/data/dna-archive.json`.
- Manifest items should keep public-safe fields only: id, title, created/status, imageSrc, prompt, analysis, sourceRun/sourceCandidateRun when safe, dnaClusters, model/options, width/height, selectedReason.
- When reconciling selected manifests against the public manifest, do **not** compare by `id` alone: older local selected manifests may use short ids such as `02`, while the public manifest may already contain the same asset under a normalized date/title id. Compare by `(created date, image filename)` or `imageSrc` basename first, then add only true missing assets.
- If a public manifest already references new GoYJ assets but their `public/assets/dna-archive/...` files are untracked, commit the referenced asset files together with the manifest. A dashboard can look correct locally while GitHub Pages still misses the binaries if only the JSON was committed.
- Do not commit generation scripts, raw provider JSON, token-bearing logs, or temporary candidate folders unless explicitly needed and scrubbed.

## Merge/update workflow for existing saved GoYJ images

1. Read every `/opt/data/dna-archive/selected/*/selected-manifest.json` and the webapp `public/data/dna-archive.json`.
2. Build public keys from `(item.created, basename(item.imageSrc))`; build selected keys from `(item.created, basename(localSelectedPath || imageSrc))`.
3. Copy only true missing binaries into `public/assets/dna-archive/<date>/` and append public-safe manifest entries.
4. Preserve/derive a `midjourneyPrompt` for each published GPT Image 2.5 asset so the modal remains useful.
5. Stage all manifest-referenced asset files, including previously untracked date folders; leave unrelated dashboard/research/home manifest changes unstaged.

## Design DNA hero replacement pattern

When Chris asks to replace the image below the phrase `헤르메스는 사람의 맥락을 보호하는 조용한 지능입니다.`:

1. Generate the requested hero from the selected DNA asset using GPT Image 2.5 via Higgsfield.
2. If local `--image-references <path>` upload fails because of a signed-upload issue, first upload the local reference with `higgsfield upload create <file> --json`, then pass the returned upload `id` as `--image-references <id>`.
3. If GPT Image 2.5 supports only a nearby ratio (for example 16:9), generate the nearest wider source and crop locally to the exact target ratio with ffmpeg.
   - 19:10 target crop example from a 16:9 source: `ffmpeg -y -i source.png -vf "crop=iw:round(iw*10/19):(iw-ow)/2:(ih-oh)/2" -frames:v 1 output-19x10.png`
4. Store public hero assets under `public/assets/design-dna/hero/`.
5. Replace the Design DNA hero visual with a real `<img>` below the headline/copy. Use CSS `aspect-ratio: 19 / 10; object-fit: cover;` and verify natural image dimensions plus rendered ratio on desktop/tablet/mobile.

## Verification checklist

- `npm run build:public` succeeds.
- Local browser smoke passes before push.
- Push to `main`, wait for GitHub Pages to serve the new hashed JS/CSS and assets.
- Live manifest/content verification:
  - Fetch `/data/dna-archive.json` from the hosted URL and assert the expected item count/titles.
  - Fetch every manifest `imageSrc` and assert HTTP 200 with an `image/*` content type.
- Live browser checks pass for desktop/tablet/mobile:
  - DNA Dashboard location is Design DNA, not Chris Archive.
  - DNA image count and selected titles are present.
  - Open at least one newly-added tile detail modal and verify the large modal image has `naturalWidth > 0` and the prompt/analysis blocks render.
  - Do not require every lazy thumbnail outside the viewport to report `complete`/`naturalWidth` during a headless pass; browser lazy-loading can legitimately defer off-screen thumbnails even when the asset URLs are valid. Use full URL fetch + representative modal image verification as the stronger deployment proof.
  - grid/tile styles match Chris Archive where requested.
  - Design DNA hero image loads with expected natural dimensions and rendered ratio.
  - no page errors and no horizontal overflow.
