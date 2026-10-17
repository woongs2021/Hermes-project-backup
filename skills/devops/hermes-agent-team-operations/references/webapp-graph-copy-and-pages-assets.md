# Webapp graph copy, measured-growth framing, and GitHub Pages asset paths

Use this when Chris asks Faker/Karina to refine the Hermes/OBD webapp, especially About OBD graphs, Son-question visualizations, team profile images, and GitHub Pages deployment checks.

## Lessons from session

### Do not imply Chris personally grew unless measured

If a graph is based on Son's questions, logs, or operating-framework maturity, do **not** label it as Chris's personal growth score unless Chris explicitly provided self-assessment data.

Safer framing:
- `OBD 질문 구조화 수준`
- `Son 실제 로그 흐름`
- `OBD operating language`
- `질문이 쌓일수록, OBD는 더 선명한 운영 언어가 됩니다`

Avoid:
- `Chris 성장선`
- steep “growth score” curves such as `30 → 94`
- copy that reads like a change note: `성장 점수가 아니라...`

Better visual approach:
- Keep the line gentle and checkpoint-like, e.g. low-range values such as `22 → 43`.
- Explain as “question-system becoming clearer,” not “user dramatically improved.”
- If the user says they do not feel that growth, treat it as a data-validity correction, not a cosmetic preference.

### Make intro copy marketing-facing, not implementation-facing

For public/intro sections, avoid copy that sounds like an internal correction or release note. Replace “what this is not” wording with a positive product/story proposition.

Example:
- Weak: `성장 점수가 아니라, Son 질문이 정리한 OBD 구조화 흐름입니다`
- Better: `질문이 쌓일수록, OBD는 더 선명한 운영 언어가 됩니다`

### Son-question archive pattern

When visualizing Son's contribution:
- Use the actual Son growth-loop logs as source (`events.jsonl`, `insights.md`, daily/son-prep notes when available).
- Group questions by week or phase.
- Put a scrollable question archive under the visualization, similar to the Research tab's dense reading pattern.
- If Son is the named source, include Son's profile image in the title/header but keep the section about the product value, not the agent biography.

### Vite/GitHub Pages public asset path pitfall

For a Vite app hosted at `/Hermes-project-webapp/`, raw public assets are served under:

`https://woongs2021.github.io/Hermes-project-webapp/assets/...`

If code uses both a base-safe helper and a second `toAppAssetSrc()` wrapper, profile images can break by double-prefixing:

`/Hermes-project-webapp//Hermes-project-webapp/assets/...`

Safe pattern:

```ts
const publicAssetPath = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`

function toAppAssetSrc(path: string) {
  if (path.startsWith('http') || path.startsWith(import.meta.env.BASE_URL)) return path
  return path.startsWith('/') ? `${import.meta.env.BASE_URL}${path.slice(1)}` : path
}
```

### Verification checklist for image/path changes

After changing team/profile image paths:
1. Run app validation/lint/build.
2. Push and wait for Pages to serve the new asset bundle.
3. HTTP-check each expected public image URL.
4. Use browser/Playwright live verification when possible:
   - page loads with no console/page errors
   - each profile image has `complete: true`
   - each has non-zero `naturalWidth`/`naturalHeight`
   - broken image count is 0

### Graph marker size

If graph dots feel visually loud, reduce both static and active states together. A session-proven 50% reduction was:
- SVG circle `r="2.4" → r="1.2"`
- CSS active dot `r: 3 → r: 1.5`

### Research text scale refinement

When Chris says Research detail/trend body text feels too large, target the body text, not the section title:

```css
.validated-detail-synthesis p {
  font-size: clamp(0.88rem, 0.95vw, 0.98rem);
  line-height: 1.64;
}

.weekly-research-trend > p {
  font-size: clamp(0.86rem, 1vw, 0.98rem);
  line-height: 1.74;
}
```
