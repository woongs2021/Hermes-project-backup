# Public-safe Pixel Office: phased delivery and QA

Use this pattern when a team/status UI is being translated into a warm pixel-office scene without exposing private operations.

## Delivery order

1. **Public-safe contract** — decide allowed public fields, Korean state labels, fallback behavior, and prohibited data before UI work.
2. **Typed adapter** — map only public profile and simple owner/status fields into scene data. Use explicit `unknown`/empty/malformed/error fallbacks; do not infer freshness from schedules or timestamps.
3. **Photo-derived sprites** — keep explicit source-to-sprite mapping; generate deterministic limited-palette, nearest-neighbor assets; verify sources, PNG dimensions/decodability, palette, and provide original-thumbnail fallback.
4. **Scene** — semantic DOM/CSS, 16:10 desktop composition, six role-bound zones, human owner as a small review marker, and an equivalent text status list below.
5. **Motion and accessibility** — static zones should not receive `tabIndex`; mark the visual scene `aria-hidden` when its contents are duplicated by a useful text list. Add only purpose-driven cues and disable them completely under reduced motion.

## Public boundary

Allowed: public team names, roles, pre-approved profile sources, coarse state labels, and conservative freshness labels.

Never render or derive: credentials, private IDs, exact runtime times, cron/schedule strings, delivery targets, raw prompts, logs, internal paths, or runtime details. Existing surrounding panels may have separate scopes; do not copy their operational metadata into the scene.

## Motion standard

- Animate only active-work furniture and the owner/review marker, never every avatar/zone.
- Use transform/opacity only; keep cues slow and nearly imperceptible (for example, a 1px movement over 16s and a 0.5px/opacity marker cue over 20s).
- Wrap motion declarations in `@media (prefers-reduced-motion: no-preference)` and retain a reduced-motion rule that forces `animation` and `transition` off.

## QA gate

Run typecheck, lint, public production build, and whitespace/diff validation. Then use a production preview and Playwright to verify:

- Desktop and 390px mobile: six zones, six textual alternatives, no horizontal overflow, no page errors.
- Desktop: 16:10 scene; mobile: 2×3 zone reflow. If scene microcopy is cramped, use a taller mobile-only ratio such as 4:3 rather than pushing type below readable scale.
- Normal motion: only the intended active-work elements and owner marker have animation names.
- `reducedMotion: 'reduce'`: those animation names are `none`.
- Visual screenshot review: no overlap, no clipping, quiet warm material palette, no neon or generic AI-dashboard styling.
