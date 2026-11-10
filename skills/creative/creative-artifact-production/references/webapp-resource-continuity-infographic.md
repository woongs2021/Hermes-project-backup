# Public Webapp Resource Continuity Infographic

Use when a dashboard needs to explain a verified asset-delivery and recovery structure without exposing operational internals.

## Three-layer information model

1. **Current experience** — the live app and lightweight previews. Emphasize speed and browsing.
2. **Versioned originals** — high-resolution files in a versioned public-safe release. Emphasize deliberate download access, not inline payload weight.
3. **Pre-cleanup recovery** — a private backup release containing pre-cleanup history/archive and integrity checks. Describe this as recoverability, never as a public download destination.

## Recommended copy pattern

- Kicker: `Resource continuity · verified`
- Title: `검증된 3단계 리소스 백업 구조`
- Lead: state that verification confirmed the three roles continue together.
- Footer: summarize the separation: preview / versioned original / pre-cleanup history backup.

Write factual, public-safe copy. Do not include local filesystem paths, private URLs, raw checksum values, credentials, commands, branch names, or release asset internals.

## Visual pattern

- Use one calm `content-card`, not a literal cloud/server/lock illustration.
- Render three compact cards with `01–03`, a short role label, a human-readable title, storage class, and one explanatory sentence.
- Use faint connector lines between cards; do not use arrows, generic AI iconography, or decorative infrastructure symbols.
- Desktop: three columns. Narrow screens: one column with a short vertical continuation line.
- Reuse existing dashboard surface, stroke, muted text, and spacing tokens so the visual reads as part of Weekly rather than a new feature surface.

## Verification

1. Confirm each layer from existing verified release/backup evidence before writing the claim.
2. Build and lint the app.
3. After hosted deployment, fetch the live hashed JS and CSS and assert the new copy and selectors are present; do not claim visual geometry without browser/screenshot evidence.
4. Keep the panel at the top of the Weekly surface when it explains an operational change that contextualizes the remainder of the weekly report.
