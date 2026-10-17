# GitHub Pages deploy stuck in `waiting` after successful build

Use this when a Pages workflow build succeeds but the deploy job stays in `waiting`, and the live site keeps serving the previous manifest/assets.

## Symptom

- `git push` succeeds and remote `main` points to the new commit.
- The workflow build job succeeds, including artifact upload.
- The `deploy` job remains `waiting` and Pages continues to serve the previous asset/manifest.
- Live checks such as `/data/brand-mockup-assets.json?v=<sha>` still show an older manifest.

## Durable fix pattern

1. Check `.github/workflows/pages.yml` concurrency configuration.
2. If it uses the same Pages group with `cancel-in-progress: false`, a stuck waiting deploy can block later deploys.
3. Change it to:

```yaml
concurrency:
  group: pages
  cancel-in-progress: true
```

4. Commit and push the workflow-only fix or include it in the next deploy-triggering commit.
5. Confirm the previous waiting run becomes `cancelled` and a new run starts.
6. Do not claim deployment from push/build success alone. Verify the live site by:
   - fetching the public manifest with a cache-busting query string;
   - comparing expected asset path/hash/dimensions;
   - fetching the actual asset URL and checking HTTP 200 + content type/hash;
   - running a browser smoke test when UI placement matters.

## Communication to Chris

- Explain that the code was pushed but Pages deploy was stuck in `waiting`.
- Say the workflow was changed to let a new deploy cancel the stuck waiting job.
- Provide the cache-busted Pages link only after the live manifest/asset checks pass.
