# Public design-asset manifest sanitization

Use when a specialist-generated design asset record is copied into a public webapp manifest.

## Why
Specialist records are operational handoff data; public manifests are product data. A valid JSON record can still expose local paths, provider URLs, run identifiers, or failure diagnostics that do not belong in the shipped site.

## Safe publication pattern
1. Confirm the asset is explicitly selected/approved and its local preview file exists.
2. Copy the image into the public asset directory and verify its SHA-256 against the handoff `assetHash`.
3. Create a new, **allowlisted** public entry. Keep only fields the UI needs, typically:
   - `id`, `title`, `created`, `status`, `imageSrc`
   - public-facing `analysis` and `detailedDescription`
   - `referenceAxis`, `dnaClusters`, `model`, display dimensions (`width`/`height` or the existing schema equivalent)
   - `savedAt`, `assetHash`, and `midjourneyPrompt` when the UI exposes it
4. Remove operational fields such as `sourceRun`, `sourceCandidateRun`, local/reference file paths, remote/provider URLs, candidate handles, and upload-fallback flags.
5. Edit public-facing prose before publication. Remove embedded HTTP errors, fallback descriptions, local paths, or provider-debug remarks; validators usually cannot detect those inside natural-language strings.
6. Run the public-manifest validator, production build, and lint. After push, verify the live manifest contains the selected IDs and each direct image URL returns the expected media type, dimensions, and hash.

## Schema caution
Do not assume every asset record uses a `dimensions` array. Inspect the current manifest: GoYJ DNA records may use separate `width` and `height` fields.
