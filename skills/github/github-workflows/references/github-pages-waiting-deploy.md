# GitHub Pages waiting deploy recovery

Use when Chris's Pages webapp update is pushed but the live URL still shows the previous manifest or images.

## Symptom

- `git push` succeeds and remote `main` points at the new commit.
- The workflow build job may be `success`, but the live `data/*.json` or asset URL still serves the previous version.
- GitHub Actions shows the Pages `deploy` job in `waiting`, or a deployment status is `waiting`.

## Recovery pattern

1. Verify remote state first:
   - `git rev-parse HEAD`
   - `git ls-remote origin main`
2. Inspect Actions via GitHub API if `gh` is unavailable:
   - `/repos/<owner>/<repo>/actions/runs?per_page=5`
   - `/repos/<owner>/<repo>/actions/runs/<run_id>/jobs`
   - `/repos/<owner>/<repo>/deployments?per_page=5`
3. If the latest run has build success but deploy `waiting`, check `.github/workflows/pages.yml` concurrency.
4. If it uses:

```yaml
concurrency:
  group: pages
  cancel-in-progress: false
```

change it to:

```yaml
concurrency:
  group: pages
  cancel-in-progress: true
```

5. Commit and push a small follow-up change so the new run cancels the stuck deploy and starts a fresh deployment.
6. Verify the user-visible result, not just Actions status:
   - Fetch live manifest with cache-busting query.
   - Compare live manifest hash/path/asset hash against local.
   - Fetch the live asset URL and compare SHA-256 when possible.
   - Browser-smoke the page and capture tile/modal screenshots when Chris reports “it still looks unchanged.”

## Reporting rule

Do not tell Chris “deployed” from `git push` alone. Say “pushed; waiting for Pages” until the live manifest or browser smoke confirms the new asset/path.
