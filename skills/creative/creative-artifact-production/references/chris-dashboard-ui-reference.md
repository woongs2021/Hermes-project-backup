# Chris dashboard UI reference

Use this reference when designing or implementing Chris's research / OBD / agent-team dashboard web app, especially the planned Faker-built local dashboard.

## Visual direction

Chris prefers a clean, high-end SaaS / bento admin dashboard style similar to the two supplied UI screenshots:

- Light off-white or pale-gray canvas with white/near-white cards.
- Left sidebar or calm app shell navigation.
- Rounded cards, generous spacing, soft shadows, and subtle borders.
- Modular dashboard panels: metric cards, charts, lists, comments/notes, customer/research-item cards, and status chips.
- Restrained typography and hierarchy: small labels, clear section titles, readable body text, not loud marketing copy.
- Small blue/green/accent highlights are acceptable, but the base should remain quiet and premium.
- Use chart/list/bento composition to make operational/research data scannable.

## Apply woongdesignv2

Use `woongdesignv2` as the design-token and material-quality base:

- Warm off-white canvas, ink text, restrained color planes.
- Samsung Sharp Sans / Pretendard-like typography when possible.
- Hairline/card/surface logic, 28px-ish rounded tiles, strong whitespace.
- Tactile paper/material subtlety rather than synthetic glow.
- Human editorial composition over generic AI-startup dashboard aesthetics.

## Avoid

- Neon, glassmorphism, glossy AI-startup gradients, fake 3D UI, stock-tech symbolism.
- Overcrowded analytics screens that hide the research narrative.
- Heavy dashboards that require real backend/data wiring before the UI skeleton is useful.
- Copying reference screenshots directly; borrow structure, rhythm, and restraint only.

## Suggested dashboard layout

For an early skeleton, prefer:

1. **Home** — weekly/monthly growth overview, key metrics, recent selected papers.
2. **Team** — Karina/Yuna/Go Youn-jung/Son/Faker/Muyeol status and outputs.
3. **OBD** — ontology/business-design growth themes, tags, and reflection notes.
4. **Research** — daily 3+3 candidates, search/filter, source links/DOIs/IDs.
5. **Muyeol Report** — weekly best-3 validation, GO/HOLD/WATCH, cautions.

Start with static or local data placeholders; only add real loaders once the app shell and visual system are stable.
