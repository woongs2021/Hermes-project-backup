# Webapp research board + Design DNA asset update workflow

Use when Chris asks to update the Hermes Project Webapp with the current weekly research pick, new Yuna/GoYJ papers, or GoYJ-selected DNA images.

## Research board update

1. Source of truth is `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl` plus weekly pick notes under `/opt/data/agent-team-work-log/muyeol/weekly-research-1pick/` and `/opt/data/agent-team-work-log/paper-candidates/weekly-selected-papers.md`.
2. In `august-dashboard`, run `npm run generate:research-board` before validation so `public/data/research-board.json` reflects the latest JSONL.
3. Watch for source records that use `agent: goyounjung` instead of `lane`/`owner`. The adapter filter must include `record.lane ?? record.owner ?? record.agent`; otherwise new GoYJ records are silently omitted while normalization can still handle them.
4. Verify expected counts from the generated manifest, including current-date Yuna/GoYJ counts and the Muyeol 1-pick status, e.g. `friday_final_pick / GO`.
5. Keep research manifest public-safe: no raw local paths, prompts, private IDs, or logs.

## GoYJ selected DNA image update

1. Check `/opt/data/dna-archive/selected/YYYY-MM-DD/selected-manifest.json` and its `images/` folder.
2. Copy selected images into `august-dashboard/public/assets/dna-archive/YYYY-MM-DD/`.
3. Append selected items to `august-dashboard/public/data/dna-archive.json` with public-safe fields:
   - keep: `id`, `title`, `created`, `status`, `imageSrc`, `prompt`, `midjourneyPrompt`, `analysis`, `sourceTool`, `dnaClusters`, dimensions, `selectedReason`, intended-use/motif fields, `assetHash`, `savedAt`.
   - avoid exposing local paths such as `localSelectedPath`, `sourceRun`, `sourceCandidateRun`, `sourceCandidateManifest`, `sourceReferences.assetPath`, or private archive paths in public JSON unless already intentionally public-safe.
4. Sort items chronologically/title if rewriting the manifest; update `generatedAt`.

## Verification

Run from `august-dashboard`:

```bash
npm run validate:data
npm run lint
npm run build:public
git diff --check
```

Browser/live checks:
- Local preview first if practical.
- Fetch live `data/research-board.json` and `data/dna-archive.json` after Pages deploy; assert counts and target titles.
- Fetch every newly added image URL and require `200` plus `image/*` content type.
- For rendered UI, navigate the real tab path (`Research`, `Design DNA → DNA Dashboard`) and assert titles appear, console/page errors are empty, and horizontal overflow is `0`.
- Lazy images may show `complete=false` while off-screen; combine DOM title checks with direct image URL fetches instead of failing solely on lazy decode state.

## GitHub Pages caveat

A push may complete before Pages serves the new JSON. Confirm the workflow deploy job and the live JSON `generatedAt`/counts. If GitHub API rate-limits or lags, compare raw GitHub `main` to live Pages JSON and inspect cache headers before reporting completion.
