# GoYJ selected DNA assets → webapp publication handoff

Use this when Chris asks Karina to “reflect what Go Youn-jung saved today in the webapp” or similar, especially after GoYJ has already selected/saved GPT Image 2.5 DNA assets.

## Trigger

- Chris references GoYJ/Goyounjung saved content rather than sending new images directly.
- GoYJ daily work log says Chris selected specific candidate numbers and that assets were written to `public/data/dna-archive.json` and `public/assets/dna-archive/YYYY-MM-DD/`.
- The task is publication/verification, not image generation.

## Workflow

1. **Read GoYJ’s daily log first.** Check `/opt/data/agent-team-work-log/goyounjung/daily/YYYY-MM-DD.md` for:
   - candidate run root;
   - selected numbers;
   - whether assets are temporary review candidates or Chris-selected saved assets;
   - target manifest/assets already written by GoYJ.
2. **Inspect the webapp worktree state.** In `/opt/data/tmp/hermes-pages-worktree/august-dashboard`, expect:
   - `public/data/dna-archive.json` modified;
   - new files under `public/assets/dna-archive/YYYY-MM-DD/`;
   - unrelated untracked candidate/mockup files may exist from prior work.
3. **Commit only the selected DNA publication files.** Do not add unrelated untracked candidates. Stage only:
   - `public/data/dna-archive.json`;
   - the exact selected image files named by the manifest/log.
4. **Validate manifest shape defensively.** `dna-archive.json` is a dict with an `items` array, not necessarily a bare array. Use `data.get('items', data)` and filter selected IDs by date/run prefix.
5. **Verify before committing.** For each selected item:
   - image file exists at `public` + `imageSrc`;
   - dimensions match manifest, usually `1024×1024` for GPT Image 2.5 DNA assets;
   - SHA-256 matches `assetHash`;
   - status is `chris_selected`;
   - `midjourneyPrompt` exists when this dashboard rail expects copy-ready prompts.
6. **Build and deploy.** Run `npm run build:public`, commit, push to `main`.
7. **Live verification.** If GitHub API is rate-limited or slow, do not block on Actions polling. Poll the live manifest directly with a cache-busting query (`/data/dna-archive.json?v=<commit>`), then verify each direct image URL returns `200 image/png`, dimensions match, and hash matches manifest.
8. **Playwright page probe.** Load the live app with `?v=<commit>` and probe the live manifest/image URLs. Treat lazy thumbnail timing separately from direct asset URL success.

## Pitfalls

- GoYJ may create temporary candidates that are **not** approved. Do not publish unselected review candidates unless Chris explicitly selected them or GoYJ’s log says they were Chris-selected.
- Existing worktrees can contain many unrelated untracked mockup candidate files. Avoid `git add .`; stage exact files only.
- A validation script that assumes `dna-archive.json` is a list will fail with `AttributeError: 'str' object has no attribute 'get'`. Read the root shape first.
- GitHub API polling can hit rate limits during frequent deploy checks. The durable fallback is live manifest polling plus direct image URL/hash verification.
- Build success alone is not completion. Chris expects a usable link backed by live manifest and real asset loading.

## Completion note shape

Keep the final note concise:

- list the saved asset titles;
- say build/push/live verification passed;
- include commit hash and cache-busted Pages link;
- mention image count/dimensions only if useful.
