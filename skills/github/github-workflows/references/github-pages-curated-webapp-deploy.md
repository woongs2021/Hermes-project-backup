# GitHub Pages deployment for curated webapp backup repos

Use this when pushing Chris's curated webapp export to GitHub and making it available via GitHub Pages.

## Pattern

1. Keep the repo split clear:
   - Backup/agent-system repo: operational docs, work logs, reusable skills, restore notes.
   - Webapp repo: app source, public-safe data, visual archive assets, Pages workflow.
2. Before pushing, run the curated export and safety scan. Do not copy broad runtime roots.
3. For Vite projects hosted under a repo path, set `base: '/Hermes-project-webapp/'` and verify public assets are base-aware.
4. After pushing, treat GitHub Pages as complete only after the live manifest/asset URLs and browser UI smoke pass.

## Pages deploy stuck in `waiting`

If a Pages run shows `build` completed successfully but the `deploy` job remains `waiting`, inspect workflow runs/deployments rather than assuming a cache problem. A common cause is a stale Pages deployment blocking the `pages` concurrency group while the workflow has:

```yaml
concurrency:
  group: pages
  cancel-in-progress: false
```

For Chris's webapp, prefer:

```yaml
concurrency:
  group: pages
  cancel-in-progress: true
```

Push a small workflow/config commit to trigger a new run. Verify the old stuck run becomes `cancelled`, the new run proceeds, and then live-smoke the Pages manifest and UI. If GitHub API polling hits rate limits, stop polling the API and verify the user-visible Pages manifest URL directly with a cache-busting query.


```bash
gh auth refresh -h github.com -s workflow
```

6. Enable GitHub Pages for workflow deployments if `actions/configure-pages` fails with `Get Pages site failed` / Pages API 404:

```bash
gh api -X POST repos/<owner>/<repo>/pages -f build_type=workflow
```

7. If deploy fails with `Branch "main" is not allowed to deploy to github-pages due to environment protection rules`, add the main branch to the `github-pages` environment deployment branch policy:

```bash
gh api -X POST repos/<owner>/<repo>/environments/github-pages/deployment-branch-policies -f name=main
```

8. Re-run the failed workflow and watch it to completion:

```bash
gh run rerun --repo <owner>/<repo> <run_id>
gh run watch --repo <owner>/<repo> <run_id> --exit-status
```

9. Verify the published URL with an HTTP check. Do not report success from workflow creation alone.

## Common pitfalls

- **Missing source data in CI:** a local build can pass because adjacent safe-source folders exist outside the repo. If CI fails with `ENOENT` for public-safe source files, include the safe-source folder in the curated webapp export, not raw/private data.
- **Committing generated/dependency folders:** running `npm ci` or `npm run build` inside a repo-shaped export creates `node_modules/` and `dist/`. Ensure `.gitignore` excludes them and remove them before staging.
- **Scanning `.git`:** safety scanners should skip `.git` internals; otherwise they may flag object files or Git metadata after `git init`.
- **Pages source branch ambiguity:** enabling Pages via API may set a source branch, but workflow deployment can still run from `main` once the environment branch policy allows it. Verify the actual successful run and final URL.
- **Double-prefixing Vite public assets:** when a Vite app uses `base: '/<repo>/'`, public assets referenced as `/assets/...` need base-prefixing for GitHub Pages. But do not run an already base-prefixed path back through the same helper again, or Team/profile images can become `/repo//repo/assets/...`. Use a guard such as `if (path.startsWith(import.meta.env.BASE_URL)) return path` in any `toAppAssetSrc()` helper.
- **HTTP 200 is not enough for image regressions:** an image URL can return 200 while the rendered React path is wrong. For user-reported broken images, verify in a browser/Playwright with `img.complete`, `naturalWidth > 0`, and no console/page errors for the relevant tab, not just direct URL checks.
- **Pages deploy job stuck in `waiting`:** if build succeeds but `deploy` stays `waiting` and the live manifest still serves the previous asset revision, inspect the workflow `concurrency` block. A Pages workflow with `cancel-in-progress: false` can leave a stuck deploy blocking later runs. For Chris's webapp, switch the Pages concurrency group to `cancel-in-progress: true`, commit, and push to retrigger deployment; verify the old waiting run becomes `cancelled`, the new run proceeds, and the live `data/brand-mockup-assets.json` points at the new revision filename before reporting success.

## Minimal verification checklist

- `npm run build` succeeds in a clean repo-shaped folder.
- `python3 scripts/scan_export_safety.py .` returns `status: clean`.
- Branch push succeeds.
- `main` points to the same commit as the branch after merge.
- Latest Pages workflow run succeeds.
- Pages URL returns HTTP 200.
- If image/public-asset paths changed, browser-smoke the deployed page and confirm the affected images have `complete: true` and non-zero `naturalWidth`.
