# Webapp asset-repo split for 4K/HQ downloads

Use when Chris wants to keep the Hermes Project Webapp lightweight while preserving downloadable 4K/HQ originals.

## Recommended architecture

- `Hermes-project-webapp`: UI code, public manifests, thumbnails/previews, lightweight display images.
- `Hermes-project-assets` or similar public asset repo: GitHub Releases holding 4K/HQ originals as release assets.
- Webapp manifest separates:
  - `imageSrc` / `previewImageSrc`: local lightweight Pages asset.
  - `downloadSrc`: external release asset URL for 4K/HQ download.
  - optional: `downloadLabel`, `sourceAssetStore`, `sourceAssetRelease`, `assetTier`.

Example:

```json
{
  "imageSrc": "/assets/dna-brand-assets/previews/outdoor-a-5-1.webp",
  "previewImageSrc": "/assets/dna-brand-assets/previews/outdoor-a-5-1.webp",
  "downloadSrc": "https://github.com/woongs2021/Hermes-project-assets/releases/download/design-dna-2026-10/design-dna-2026-10__outdoor-mockup-a-5-1__4k.png",
  "downloadLabel": "4K 원본 다운로드"
}
```

## Why

GitHub accepts repos above 1GB in some cases, but the safe operating pattern is to avoid growing the Pages repo with many 4K/HQ PNGs. Chris's webapp already has multi-GB public assets; future updates should avoid adding 4K originals directly when a release/download URL can serve them.

## Migration phases

1. Inventory current large assets: local path, size, sha256, manifest references, proposed public release filename, proposed `downloadSrc`, preview existence, public-safe status.
2. Create/confirm a public asset repo such as `woongs2021/Hermes-project-assets`. Public is preferred if the webapp should download without login.
3. Create release tags by batch, e.g. `design-dna-2026-10`.
4. Upload 4K/HQ originals as release assets; avoid filenames containing broad secret-scan words like `token`, `secret`, or `key`.
5. Update webapp manifests so display images remain local previews and `downloadSrc` points to release assets.
6. Build/deploy and verify:
   - webapp previews render;
   - download links return `200` and expected content type/size;
   - no private paths/credentials in manifest;
   - GitHub Pages live JSON references the new URLs.
7. Only after stable verification, consider removing 4K files from the webapp working tree. Full historical size reduction requires `git filter-repo`/history rewrite and explicit approval.

## Do not do without explicit approval

- Do not rewrite git history or force-push just to reduce repo size.
- Do not replace working download links with URLs for a repo/release that does not exist yet.
- Do not expose private asset repo release links in a public webapp if login/auth would be required.
