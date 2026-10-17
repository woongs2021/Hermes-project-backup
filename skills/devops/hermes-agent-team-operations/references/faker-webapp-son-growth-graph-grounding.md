# Faker webapp: grounding Son growth/question graphs

Use this when Chris asks Faker/Karina to visualize Son's questions, growth loops, OBD maturity, or similar agent-derived progress in the Hermes/OBD webapp.

## Session lesson

Chris pushed back on a graph that looked like a steep personal growth curve. The underlying data was not Chris's self-reported growth; it was Son's question-log structure becoming more complex. That mismatch made the visualization feel exaggerated and untrue to Chris's lived experience.

## Pattern

1. **Identify what is actually measured.**
   - If the source is Son's `events.jsonl`, `insights.md`, daily logs, or prep files, the measure is usually question framing / operating-structure maturity, not Chris's personal growth.
   - Do not label inferred structure metrics as `growth`, `Chris growth`, or high maturity scores unless Chris supplied self-assessment data.
2. **Name axes conservatively.**
   - Prefer `질문 구조화`, `OBD 구조화 수준`, `Son 실제 로그 흐름`, or `운영 체크포인트`.
   - Avoid `성장`, `성장 점수`, or very high `maturity 94` style labels when the user has not confirmed that growth.
3. **Use gentle shapes.**
   - Replace steep up-and-right curves with shallow progression, checkpoint timelines, or stage cards.
   - If numeric values are needed for plotting, keep them low/moderate and explain they are structure checkpoints, not personal scores.
4. **Show source questions.**
   - Add a nearby scrollable archive/list of the actual Son questions, grouped by week or loop phase, so the graph has visible evidence.
   - Include Son's face/avatar in the title area when the section is explicitly Son-owned.
5. **Verify and deploy.**
   - Run `npm run validate:data`, `npm run lint`, `npm run build:public`, and `git diff --check` before committing.
   - After pushing to GitHub Pages, smoke-test the live URL for both new JS/CSS assets and representative content/style markers.

## Copy guidance

Good:
- `성장 점수가 아니라, Son 질문이 정리한 OBD 구조화 흐름입니다`
- `y축은 Chris의 체감 성장치가 아니라 Son 질문 로그에서 보이는 OBD 질문 구조화 수준입니다.`
- `structure checkpoint 43`

Risky:
- `Chris의 성장선이 94까지 올라갔습니다`
- `Son의 질문은 Chris의 OBD 성장선을 다시 그립니다` when no self-report growth data exists.
- Any steep graph that implies Chris should feel a growth he did not report.
