# Chris Archive batch intake pattern

Use this reference when Chris uploads several visual references in one session and says `추가해줘`.

## What changed in the session

Chris corrected the intake experience after repeated progress fragments made the assistant feel like it was “말을 하다말어.” The workflow should be quiet while processing and send one concise completion message after verification.

## Preferred interaction pattern

- If the image caption/message includes `추가해줘`, proceed immediately.
- Do not send repeated step-by-step progress messages for routine archive intake.
- Work quietly through: image inspection, file copy, entry creation, index update, design-system draft update, verification.
- Send a single completion reply with:
  - 저장 완료
  - asset path
  - entry path
  - `index.md` and `DESIGN_SYSTEM_DRAFT.md` updated
  - strongest 3–6 design-DNA signals
  - one caution if relevant
- Send an interim message only for a real blocker or unusually long operation.

## Efficient implementation pattern

For straightforward repeated image additions, prefer one compact `execute_code` call after vision analysis that:

1. Gets KST date via `terminal("TZ=Asia/Seoul date +%Y-%m-%d")`.
2. Copies `/opt/data/image_cache/<id>.jpg` to `/opt/data/chris-archive/images/YYYY/MM/YYYY-MM-DD_<slug>_<sha12>.jpg`.
3. Writes `/opt/data/chris-archive/entries/YYYY/YYYY-MM-DD_<slug>.md` with the standard analysis sections.
4. Appends the entry to `/opt/data/chris-archive/index.md` if not already present.
5. Adds only tentative candidate clusters to `/opt/data/chris-archive/DESIGN_SYSTEM_DRAFT.md`.
6. Prints a compact JSON verification object with `asset`, `entry`, sizes, and `verified: true`.

## Analysis consistency

Keep every entry comparable. Use stable sections:

- Short description
- Visible content
- Visual tags
- Color observations
- Typography observations
- Texture/material observations
- Layout/composition observations
- Metaphor/system meaning
- Product/UX implications
- Aesthetic score and rationale
- Karina interpretation
- Go Youn-jung review request
- Extraction candidates for future `DESIGN_SYSTEM.md`

## Guardrail

Do not turn one image into a final design rule. The draft may accumulate candidate clusters, but final `DESIGN_SYSTEM.md` requires repeated patterns, Go Youn-jung review, or Chris approval.