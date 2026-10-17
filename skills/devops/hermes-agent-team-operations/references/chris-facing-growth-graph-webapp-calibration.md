# Chris-facing growth graph webapp calibration

Use this when updating the Hermes/OBD webapp with graphs or visualizations that summarize Chris's growth, Son questions, research loops, or agent-team outputs.

## Session learning

Chris pushed back on a graph that looked like a steep personal-growth curve: he did not feel that level of growth and asked what the growth basis was. The correct framing was that the plotted values represented **Son's question-log / OBD structure maturity**, not Chris's subjective or measured personal growth.

## Rules for future graph work

1. **Do not label inferred structure as personal growth.**
   - Avoid y-axis labels like `성장` or titles like `Chris의 성장선` unless Chris supplied self-assessment data or explicit growth criteria.
   - Prefer `질문 구조화`, `OBD 구조화 수준`, `운영 성숙도 체크포인트`, or `question maturity` when the source is agent logs.
2. **State the measurement basis in the UI copy.**
   - Say whether values come from Son growth logs, public-safe manifests, weekly picks, validation status, user answers, or manual self-rating.
   - If values are ordinal/illustrative, call them `checkpoint` or `structure level`, not score.
3. **Use restrained slopes.**
   - If the user has not validated growth intensity, use a gentle progression or step/checkpoint visualization instead of a steep upward line.
   - Better default: low-range values (e.g. 20–45) with text explaining “not a personal growth score.”
4. **Show raw supporting questions near the chart.**
   - Add a scrollable weekly question/archive section, grouped by week, so the graph can be inspected against the underlying Son questions.
   - Keep it public-safe: no raw private DMs, IDs, credentials, or sensitive logs.
5. **Legibility calibration matters.**
   - Axis labels should be small and secondary; they should not dominate the chart.
   - Data-point markers should be visually light. If Chris says dots feel too large, shrink both default and active markers proportionally (session fix: SVG dot r `2.4 → 1.2`, active CSS r `3 → 1.5`).
6. **Profile images on GitHub Pages / Vite.**
   - Public assets referenced from React should respect `import.meta.env.BASE_URL` when served under a repo subpath such as `/Hermes-project-webapp/`.
   - Use a small helper like `const publicAssetPath = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`` and reference `/assets/team/son_profile.jpg` through it.

## Verification checklist

- [ ] UI copy distinguishes personal growth from log/structure maturity.
- [ ] y-axis/x-axis labels are accurate and visually quiet.
- [ ] Graph slope does not overclaim unmeasured growth.
- [ ] Supporting Son questions are visible in a scrollable weekly archive.
- [ ] Profile image URLs resolve under the deployed GitHub Pages base path.
- [ ] Run `npm run validate:data`, `npm run lint`, `npm run build:public`, `git diff --check`.
- [ ] After push, verify live JS/CSS markers and image HTTP 200 from the Pages URL.
