# GitHub Pages deploy waiting / cache-busted asset verification

Use when a webapp push succeeds but the GitHub Pages site still shows an older manifest or image.

## Durable lesson

A push to `main` is not proof that Pages is serving the new build. Verify the deployed artifact itself.

## Diagnostic sequence

1. Verify git state:
   - `git rev-parse HEAD`
   - `git ls-remote origin main`
2. Check whether the live manifest changed by fetching it with a cache-busting query string.
3. If the live manifest stays old for several minutes, inspect GitHub Actions/Pages deployment status.
   - A run can have `build` completed successfully while the `deploy` job is still `waiting`.
4. If deploy is stuck waiting and workflow concurrency is:
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
   Then push a small workflow commit to trigger a new deploy. This can cancel the stuck waiting deployment and let the newer deploy proceed.
5. After the deploy completes, verify by live data, not by assumption:
   - live manifest hash / expected `imageSrc`
   - live image URL returns `200 image/*`
   - live image bytes/hash match local file
   - Playwright/browser DOM loads the expected filename

## User communication

If Pages deploy is waiting, tell Chris plainly that the live site is legitimately still on the old version. Do not blame browser cache until the live manifest and DOM have been checked.
