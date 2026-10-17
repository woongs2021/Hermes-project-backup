# GoYJ DNA candidate loop and DNA Dashboard workflow

Use when Chris asks to operate or revise Go Youn-jung's generated-image loop, save selected generated images, or update the webapp DNA Dashboard.

## Core operating contract

- GoYJ shows Chris **5 square (1:1) graphic motif material candidates** on **Mon/Wed/Fri**.
- Candidates should be inspired by Chris Archive + Hermes/Chris Design DNA, and useful as composable material for later Chris-led brand/package/mobile UI/mockup synthesis.
- They are not finished posters, package labels, app icons, UI screenshots, product mockups, or final graphic-design deliverables; they should work as crop/mask/overlay/repeat/layer ingredients.
- Generate with Higgsfield first when available; preserve prompts and analysis for each candidate.
- Candidates are temporary review material. **Do not publish or persist to final webapp/backend just because they were generated.**
- Chris's explicit save signal is `저장해줘`. Only then move selected image(s) into the selected archive and public webapp manifest. Discard or leave unselected candidates out of public data.

## Data layout

- Temporary candidates: `/opt/data/dna-archive/candidates/YYYY-MM-DD/`
  - `images/` for generated review images
  - `candidate-manifest.json` with prompt, negative prompt, intended use, DNA clusters, GoYJ analysis, local path, model/options, dimensions
  - `candidate-analysis.md` for human-readable summary
- Selected assets: `/opt/data/dna-archive/selected/YYYY-MM-DD/`
  - `images/` for Chris-selected final files
  - `selected-manifest.json` with the chosen items only
- Webapp public data:
  - assets under `august-dashboard/public/assets/dna-archive/YYYY-MM-DD/`
  - manifest at `august-dashboard/public/data/dna-archive.json`

## Webapp placement rule

Chris does **not** want selected GoYJ generated images dumped into the top-level Design DNA tab.

Preferred IA:

- Main tab: `Chris Archive`
- Inside that tab, provide dashboard tabs:
  - `Chris Archive` — reference/source images
  - `DNA Dashboard` — selected GoYJ generated assets only
- DNA Dashboard tiles should behave like Chris Archive tiles:
  - thumbnail grid
  - click opens modal/popup
  - Popup includes large image, status/date, GoYJ analysis, motif type, later synthesis use, DNA clusters, generation prompt, and source/save policy

## Update workflow for `저장해줘`

1. Read the relevant temporary candidate manifest and/or existing selected manifest.
2. Copy only Chris-approved images to `/opt/data/dna-archive/selected/YYYY-MM-DD/images/`.
3. Write/update `/opt/data/dna-archive/selected/YYYY-MM-DD/selected-manifest.json`.
4. Copy selected files into the webapp public assets folder.
5. Merge selected entries into `public/data/dna-archive.json` without overwriting unrelated prior selections.
6. Build the webapp (`npm run build:public`).
7. Browser-verify local preview:
   - Chris Archive dashboard tab exists
   - DNA Dashboard tab exists
   - reference grid still shows the expected reference count
   - DNA Dashboard shows selected asset count and today's selections
   - every DNA image asset fetches 200
   - click opens modal with prompt/analysis
   - no horizontal overflow on desktop/tablet/mobile
8. Commit only relevant files and push main/Pages.
9. Live-verify the GitHub Pages URL with the same checks.

## Pitfalls

- Do not treat `last_status=ok` or candidate file creation as proof that Chris received or approved images.
- Do not publish unselected candidates to `dna-archive.json`.
- Avoid timestamp-only manifest churn in unrelated data files; revert unrelated `generatedAt` diffs before commit.
- Do not leave selected GoYJ assets in the Design DNA explanatory page if Chris asked for a separate dashboard experience.
- Use `MEDIA:/absolute/path` for Telegram attachments; `MEDIA /path` will not attach reliably.