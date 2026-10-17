# GoYJ DNA asset candidate loop

Use this when Chris asks to operate, repair, verify, or extend Go Youn-jung's generated-image loop based on Chris Archive / Hermes Design DNA.

## Current operating contract

- Owner/sender: Go Youn-jung profile and bot, not Karina/default.
- Cadence: Monday / Wednesday / Friday in KST.
- Output per run: 5 square (1:1) graphic design candidates.
- Source of taste/DNA: Chris Archive references + `/opt/data/chris-archive/헤르메스디자인시스템.md` + webapp `public/data/chris-archive.json`.
- Tooling: Higgsfield CLI is the preferred generation path for still graphics. Verify workspace/model availability without printing credentials.
- Candidate scope: brand/package/mobile UI/OBD/editorial/media graphic assets, not only soft-3D metaphor objects or turntables.
- Selection gate: do **not** publish candidates to the final DNA Archive or webapp until Chris explicitly selects and says `저장해줘`.
- Persistence: selected assets only go to `/opt/data/dna-archive/selected/YYYY-MM-DD/` and the webapp `public/data/dna-archive.json`; unselected candidates remain temporary under `/opt/data/dna-archive/candidates/YYYY-MM-DD/` and should not become public/backdata.

## Candidate run checklist

1. Confirm KST date and the GoYJ profile cron job if debugging schedule/delivery.
2. Read the current Design DNA document and archive manifest.
3. Generate exactly 5 distinct 1:1 candidates, varying medium/use: e.g. presence mark, package label/seal, mobile AI context UI, OBD signal field, editorial cover/pattern surface.
4. Save temporary review files under `/opt/data/dna-archive/candidates/YYYY-MM-DD/`:
   - `images/01.*` … `images/05.*`
   - `candidate-manifest.json`
   - `candidate-analysis.md`
   - optional `telegram-send-status.json`
5. Final GoYJ DM should include all 5 images as exact `MEDIA:/absolute/path` attachments and say they are temporary candidates.
6. Instruct Chris: choose a number and say `저장해줘`; only selected images will be saved to DNA Archive/webapp, others discarded.

## Selection / webapp publishing checklist

When Chris has already selected final images and asks Karina to update the webapp:

1. Inspect `/opt/data/dna-archive/selected/YYYY-MM-DD/selected-manifest.json` for selected items.
2. Copy selected image files into the Pages worktree under `public/assets/dna-archive/YYYY-MM-DD/`.
3. Merge selected metadata into `public/data/dna-archive.json`; preserve prompt/analysis/source fields for the tile detail modal.
4. Avoid committing unrelated generatedAt-only diffs from other manifests unless the user requested those data refreshes.
5. Run the webapp build.
6. Verify locally and live:
   - `data/dna-archive.json` includes the selected IDs.
   - selected asset URLs return HTTP 200.
   - Design DNA tab shows the expected tile count and selected titles.
   - tile images fetch successfully, with no desktop/tablet/mobile overflow.
7. Commit/push to the webapp repo and provide the GitHub Pages `#design-dna` link.

## Pitfalls

- Do not auto-save generated candidates just because the cron ran successfully; Chris's `저장해줘` is the approval boundary.
- Do not let Karina/default proxy-deliver the recurring visual loop; user-facing recurring output should come from GoYJ.
- Do not convert this loop back into the older Kling-only still+turntable pattern unless Chris explicitly asks.
- Do not expose raw tokens, provider job IDs beyond public asset URLs, or private delivery IDs in webapp data.
- Do not stage unrelated refreshed research/home/dashboard manifests while publishing selected DNA assets; keep commits narrowly scoped.
