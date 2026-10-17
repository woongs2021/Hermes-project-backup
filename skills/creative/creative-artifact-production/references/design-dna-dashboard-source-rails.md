# Design DNA Dashboard Source Rails

Use when Chris asks to split, update, or save Design DNA / DNA Dashboard graphic assets by generation source.

## Rails

- **GPT Image 2.5 rail**
  - Holds GoYJ loop outputs that Chris explicitly approves/saves.
  - Backed by `public/data/dna-archive.json`.
  - Future GoYJ M/W/F loop saves continue here.
  - Keep copyable `midjourneyPrompt` on each item so the GPT asset can be re-created or translated in Midjourney.

- **Midjourney rail**
  - Holds only Chris's manual Midjourney uploads/outputs.
  - Backed by `public/data/midjourney-dna-archive.json`.
  - Save sequentially as `Midjourney 01`, `Midjourney 02`, etc.; do not mix with the GPT Image 2.5 manifest.
  - Store assets under `public/assets/dna-archive/midjourney/YYYY-MM-DD/` with numbered descriptive filenames.

## Item shape

Each saved Midjourney item should include:

- `id`: stable date/source/number/title slug
- `title`: `Midjourney NN — <source prompt family> Translation`
- `created`
- `status`: `midjourney_manual_saved`
- `sourceTool`: `Midjourney`
- `imageSrc`
- `prompt` and `midjourneyPrompt`: copy-ready prompt used or corresponding prompt family
- `analysis`: short Korean note on how the manual output translates the GPT/DNA motif and what it is useful for
- `sourceRun`: `manual_midjourney_upload_YYYY_MM_DD_NN`
- `assetHash`
- `dnaClusters`

## Webapp pattern

- Load both manifests in the Design DNA panel.
- Add source tabs inside DNA Dashboard: `GPT Image 2.5` and `Midjourney`.
- Show counts per rail in the main DNA Dashboard tab subtitle.
- Use the same tile/detail modal component for both rails.
- In the modal kicker, show source tool (`Midjourney` or `GPT Image 2.5 loop`) and status.
- Use the source-specific manifest policy in the modal footer.

## QA checklist

- Validate both JSON manifests with `python3 -m json.tool`.
- Build with `npm run build:public`.
- Browser-check Design DNA → DNA Dashboard:
  - GPT rail tile count equals `dna-archive.json` item count.
  - Midjourney rail tile count equals `midjourney-dna-archive.json` item count.
  - New Midjourney image loads with nonzero `naturalWidth` / `naturalHeight`.
  - Detail modal opens and prompt copy still works.
  - No horizontal overflow on desktop and mobile.
- After push, poll live GitHub Pages JSON and asset URL until the new item and image return 200.
