# Chris DNA Dashboard — selected GoYJ generated assets

Use when Chris asks to publish Go Youn-jung generated visual assets that he explicitly selected with `저장해줘`.

## Placement rule

- Do **not** mix generated GoYJ outputs into the raw `Chris Archive` reference grid.
- Do **not** leave the selected-output dashboard as a loose block inside the main Design DNA narrative.
- Preferred IA: open the main **Design DNA** tab, then provide a subtab/section switch:
  - `Design DNA` — principles, DNA clusters, prompt packages, guardrails.
  - `DNA Dashboard` — GoYJ-generated assets that Chris selected/saved.
- `Chris Archive` remains source/reference material only.
- `DNA Dashboard` is output/evidence: selected generated graphics, prompts, GoYJ analysis, DNA clusters, and source run metadata.

## Data shape

- Selected local manifest: `/opt/data/dna-archive/selected/YYYY-MM-DD/selected-manifest.json`.
- Public webapp manifest: `public/data/dna-archive.json`.
- Public assets: `public/assets/dna-archive/YYYY-MM-DD/<file>`.
- Each item should include at least: `id`, `title`, `created`, `status`, `imageSrc`, `prompt`, `analysis`, `sourceRun`, `dnaClusters`, model/options if known, and selected reason if available.

## Webapp behavior

- The `DNA Dashboard` grid should mirror the Chris Archive tile pattern but use GoYJ-selected assets.
- Clicking a tile opens a modal with:
  - large image
  - title/date/status
  - GoYJ analysis
  - DNA clusters
  - generation prompt
  - save/source policy
- Verify that `Chris Archive` still shows only raw reference images and no DNA Dashboard controls.
- Verify that `Design DNA` contains the `DNA Dashboard` subtab and that images load from GitHub Pages with HTTP 200.

## Verification checklist

1. Build locally: `npm run build:public`.
2. Browser-smoke local and live for desktop/tablet/mobile:
   - Chris Archive reference count remains expected.
   - No DNA Dashboard tiles inside Chris Archive.
   - Design DNA has two subtabs/section tabs.
   - DNA Dashboard shows all selected GoYJ assets.
   - Recently selected assets are visible by title.
   - Asset fetches return 200.
   - Modal exposes prompt + analysis.
   - No horizontal overflow.
3. Deploy through the existing webapp GitHub Pages workflow and verify the live `#design-dna` URL.

## Pitfalls

- Chris may initially say “design archive” conversationally, but if he corrects “not Chris Archive, Design DNA,” follow the IA above.
- Do not stage unrelated generatedAt churn in other public manifests while publishing DNA assets.
- Do not persist temporary candidates; only selected assets belong in `DNA Dashboard`.
