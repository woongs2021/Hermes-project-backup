# GitHub Pages deploy job stuck in `waiting`

Use this when a webapp commit is pushed but GitHub Pages still serves the previous manifest/assets and the latest Actions run shows `deploy` waiting.

## Symptoms

- `git push` succeeded and `origin/main` points at the new commit.
- GitHub Actions build job completed successfully.
- Deploy job is `waiting` with no runner, and Pages URL still serves the previous manifest/hash.
- Recent workflow runs show an older run stuck in `waiting` while newer assets are not published.

## Diagnosis

1. Confirm remote main:
   ```bash
   git rev-parse HEAD
   git ls-remote origin main | cat
   ```
2. Inspect workflow runs via GitHub API if `gh` is unavailable:
   ```bash
   python3 - <<'PY'
   import urllib.request,json
   headers={'User-Agent':'Hermes-Agent'}
   url='https://api.github.com/repos/OWNER/REPO/actions/runs?per_page=5'
   data=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=20).read().decode())
   for r in data['workflow_runs']:
       print(r['id'], r['head_sha'][:7], r['display_title'][:48], r['status'], r.get('conclusion'), r['updated_at'])
   PY
   ```
3. Check jobs for the stuck run:
   ```bash
   python3 - <<'PY'
   import urllib.request,json
   headers={'User-Agent':'Hermes-Agent'}
   run='RUN_ID'
   url=f'https://api.github.com/repos/OWNER/REPO/actions/runs/{run}/jobs'
   data=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=20).read().decode())
   for j in data['jobs']:
       print(j['name'], j['status'], j.get('conclusion'), j.get('runner_name'), j.get('html_url'))
   PY
   ```

## Fix pattern

If the workflow has:

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

Then commit and push. This allows a new Pages deploy run to cancel a stuck waiting deploy instead of queueing behind it.

## Verification

- Confirm the previous stuck run becomes `completed / cancelled` and the new run proceeds.
- Prefer live service verification over only Actions status:
  ```bash
  python3 - <<'PY'
  import urllib.request,json,time
  base='https://OWNER.github.io/REPO/'
  data=urllib.request.urlopen(base+'data/brand-mockup-assets.json?v='+str(int(time.time())),timeout=20).read().decode()
  m=json.loads(data)
  print(m.get('generatedAt'))
  PY
  ```
- Fetch the expected new asset URL and ensure `200 image/*`.
- Browser-smoke the final Pages URL and capture/inspect the relevant tile or modal.

## Communication note

If the user asks why the deployed page has not changed, say clearly that the code/image push succeeded but the GitHub Pages deploy job is stuck/waiting. Avoid blaming browser cache until the live manifest actually contains the new asset.
