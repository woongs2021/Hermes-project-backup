# Static web-app asset delivery field guide

This preserves the detailed, session-derived guidance absorbed from the former `static-webapp-asset-delivery` skill.

## Delivery contract

1. Keep UI code, thumbnails, and display-ready previews in the web-app repository.
2. Store high-resolution originals in a durable, versioned download location (for example, a GitHub Release or an asset repository).
3. Point public manifests to previews for display and external versioned URLs for downloads.
4. State the contract in README operational guidance and a concise in-app explanation near the relevant detail/archive experience.
5. Do not call cleanup complete until release/download paths, local previews, build, and deployed site are all checked.

## Public-manifest boundary

Public JSON is product output rather than an internal work log. Remove local filesystem paths, source-run identifiers, candidate paths, raw operational metadata, and private runtime details. Remove matching unused TypeScript fields. Preserve fields the UI actually renders, such as titles, analyses, deliberately public prompts, preview/download URLs, dimensions, and labels.

Use a deterministic validator in the normal `validate:data` (or equivalent) command. It should reject local-path markers such as `/opt/data/` and `file://`, plus explicitly forbidden internal keys. Audit all adjacent public manifests, not merely the one changed.

## Implementation and verification notes

- Determine render usage before changing data types or fields.
- A production static `index.html` often only references scripts. Resolve the app-script URL correctly and look for UI copy in the delivered JS bundle—not only raw HTML.
- A successful workflow can precede CDN visibility. Retry live requests before diagnosing an apparent deployment failure.
- Never leave a high-resolution fallback pointing to a deleted local original when the external release URL is meant to be authoritative.
- For history rewriting, make and verify a recovery archive independently; current-tree deletion alone does not reduce historical repository size.
