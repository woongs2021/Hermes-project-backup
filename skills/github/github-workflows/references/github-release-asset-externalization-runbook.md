# GitHub Release asset externalization runbook

Use when moving high-resolution downloadable originals out of a GitHub Pages/Vite webapp while retaining fast local previews.

## Proven migration contract

- **Webapp repo:** UI, manifests, thumbnails, and display-ready WebP/JPEG previews.
- **Asset repo:** public GitHub Releases containing 4K/HQ download originals.
- Each manifest item keeps local `imageSrc` / `previewImageSrc`, while `downloadSrc` becomes a versioned GitHub Release URL. Add `sourceAssetStore`, `sourceAssetRelease`, and `assetTier` when the manifest supports provenance fields.

## Safe execution sequence

1. Confirm the new asset repo is accessible and public if download links must work without authentication.
2. Build an inventory **only from manifest-referenced high-res files**. Record source-relative path, bytes, SHA-256, manifest item id/title/field, proposed deterministic release filename, and intended release URL.
3. Check every high-res display item has a valid local preview before changing `imageSrc`. If any does not, generate or preserve a suitable display asset first.
4. Create a dated/batched release tag (example: `design-dna-YYYY-MM`) and upload originals as release assets. Release attachment filenames should be deterministic, URL-safe, and avoid secret-like words (`token`, `secret`, `key`) that may collide with ignore/scanner rules.
5. Verify the release asset count and total bytes, then check **every** generated `downloadSrc` returns HTTP 200 before updating the webapp manifest.
6. Update manifest fields atomically: high-res `imageSrc` → existing local preview; high-res `downloadSrc` → verified Release URL. Preserve download labels and add source/tier metadata consistently.
7. Run manifest validation, lint, production build, and whitespace/diff checks. Stage only the intended manifest files; do not accidentally stage scratch tests or build output.
8. Push the asset repo and webapp separately. Wait for GitHub Pages deployment completion, then verify the live manifest has the expected external URL count and test both one live local preview (`image/*`) and one live release download (HTTP 200).

## Safety boundaries

- Do not delete local originals or rewrite git history in the same migration. Keep them until external URLs, Pages, and user-facing downloads are stable; require explicit approval for history rewrite/force push.
- Never upload broad runtime directories. Release inventory and upload sources must be an explicit, manifest-derived allowlist.
- Do not log or commit GitHub tokens. If automation needs HTTPS credentials, read them only through the configured credential helper at runtime and never print or persist them.
- Make the uploader resumable: query existing release assets by name/size and skip already uploaded files so interrupted uploads can safely continue.
