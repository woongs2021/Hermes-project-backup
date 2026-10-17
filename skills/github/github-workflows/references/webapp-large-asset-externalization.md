# Webapp large-asset externalization for GitHub Pages

Use when Chris's Pages webapp is growing because 4K/HQ generated images, mockups, or videos are committed under `public/assets`, and he still wants download buttons in the webapp.

## Why this matters

- GitHub's 1GB repository size is mostly an operational recommendation, not an immediate hard push stop, but large repos degrade clone/push/build/Pages deploy reliability.
- More direct hard limits usually appear as large-file constraints: GitHub warns around 50MB per file and blocks normal git pushes around 100MB per file.
- A repo can keep updating while already several GB if individual files stay below the hard limit, but that is not a sustainable webapp architecture.
- Deleting large files from the working tree stops future growth but does **not** shrink `.git` history; history rewrite is a separate, explicit-approval operation.

## First measure, do not guess

Run size checks before proposing a migration:

```bash
cd /path/to/Hermes-project-webapp
printf 'worktree_total\t'; du -sh . | cut -f1
printf 'git_dir_total\t'; du -sh .git | cut -f1
printf 'august_dashboard\t'; du -sh august-dashboard | cut -f1
printf 'public_assets\t'; du -sh august-dashboard/public/assets 2>/dev/null | cut -f1 || true
printf 'dist\t'; du -sh august-dashboard/dist 2>/dev/null | cut -f1 || true
du -h -d 3 august-dashboard/public 2>/dev/null | sort -h | tail -20
git count-objects -vH
git ls-files -z | xargs -0 du -ch 2>/dev/null | tail -1
git ls-files -z | xargs -0 du -h 2>/dev/null | sort -h | tail -20
```

If network access/API is available, compare with GitHub's repo size field:

```bash
python3 - <<'PY'
import json, urllib.request
url='https://api.github.com/repos/OWNER/REPO'
req=urllib.request.Request(url, headers={'Accept':'application/vnd.github+json','User-Agent':'Hermes-Agent'})
with urllib.request.urlopen(req, timeout=20) as r:
    data=json.loads(r.read().decode())
print(data['full_name'], 'size_mb_api=', round(data.get('size',0)/1024,1), 'default=', data.get('default_branch'))
PY
```

## Recommended architecture

Keep the webapp repo focused on fast display:

- `previewImageSrc`: lightweight `.webp` / thumbnail / display image kept in the Pages repo.
- `imageSrc`: usually the same lightweight display image, or another bounded-size web image.
- `downloadSrc`: stable external URL for 4K/HQ original.
- `downloadLabel`: make the file tier explicit, e.g. `4K 원본 다운로드`.

Store large originals outside the Pages repo:

1. **Best simple path:** separate public asset repo such as `Hermes-project-assets` with GitHub Releases attachments.
2. **More product-like path:** object storage/CDN such as Cloudflare R2 or S3.
3. **Less preferred for this webapp:** Git LFS, because Pages/download behavior and bandwidth quotas are easier to trip over.

Example manifest item:

```json
{
  "id": "outdoor-mockup-a-5-1",
  "title": "Outdoor Mockup A-5-1",
  "previewImageSrc": "/assets/dna-brand-assets/previews/outdoor-mockup-a-5-1.webp",
  "imageSrc": "/assets/dna-brand-assets/previews/outdoor-mockup-a-5-1.webp",
  "downloadSrc": "https://github.com/woongs2021/Hermes-project-assets/releases/download/design-dna-2026-10/design-dna-2026-10__outdoor-mockup-a-5-1__4k.png",
  "downloadLabel": "4K 원본 다운로드",
  "sourceAssetStore": "github-release",
  "sourceAssetRelease": "design-dna-2026-10",
  "assetTier": "preview+external-4k"
}
```

## Public/private rule

- Public webapp + direct download button needs public or otherwise anonymously accessible URLs.
- Private release assets can require login/authorization and may not be stable for public Pages download UX.
- Keep private/sensitive originals out of public manifests entirely; do not expose internal paths, prompts, chat IDs, credentials, or private source metadata.

## Migration phases

1. **Inventory**
   - Identify 4K/HQ directories and files.
   - Record local path, size, SHA-256, manifest references, proposed release filename, proposed download URL, preview existence, and public-safety status.
2. **Prepare asset store**
   - Create/confirm public asset repo or object storage bucket.
   - Define release tag such as `design-dna-2026-10`.
3. **Upload originals**
   - Upload 4K/HQ files as release assets or storage objects.
   - Verify each URL returns `200` and the expected content type/size.
4. **Update webapp manifest**
   - Keep preview/display image local and lightweight.
   - Change only `downloadSrc` to the external URL.
   - Build and live-smoke the download button.
5. **Stop future growth**
   - From this point on, new 4K/HQ originals should go to the external asset store first; the Pages repo gets preview assets only.
6. **Optional later history cleanup**
   - Only after explicit approval, use `git filter-repo`/BFG to purge old large files from history and force-push. This requires careful coordination and likely fresh clones.

## Naming guidance

Use stable, URL-safe filenames:

```text
design-dna-2026-10__outdoor-mockup-a-5-1__4k.png
design-dna-2026-10__coffee-mockup-a-3-4__4k.png
```

Avoid spaces, Korean-only filenames for release assets, unstable provider dump names, excessive length, and broad secret-scan words such as `token`, `secret`, or `key`.

## Do not do without explicit approval

- Do not rewrite git history just because the repo is large.
- Do not delete local/public 4K files before verifying external download URLs and backups.
- Do not switch `downloadSrc` to URLs that do not exist yet.
- Do not use private repo URLs for public download UX unless Chris explicitly accepts login/permission friction.
