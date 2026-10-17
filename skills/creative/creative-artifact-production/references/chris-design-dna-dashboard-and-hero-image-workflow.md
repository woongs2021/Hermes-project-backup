# Chris Design DNA dashboard and hero-image workflow

Use this when Chris asks to save GoYJ-generated images, change where they appear in the Hermes webapp, replace Design DNA imagery, or make Design DNA sections feel more visual/infographic.

## Stable product structure

- `Chris Archive` = external/user-provided reference images and analysis.
- `Design DNA → DNA Dashboard` = GoYJ-generated assets that Chris explicitly selected with “저장해줘”.
- Do not place GoYJ selected/generated images under Chris Archive unless Chris explicitly reverses this structure.
- Keep GoYJ candidate generation save-gated: candidates may be shown for review, but only selected outputs are persisted/published.

## Generation model preference

- GoYJ image candidates should be generated with **GPT Image 2.5**.
- Do not silently substitute seedream/recraft/kling/image_auto for this lane. If GPT Image 2.5 is unavailable, report the blocker instead of generating with another model.

## DNA Dashboard grid parity

When changing DNA Dashboard layout, match Chris Archive’s grid/tile system unless Chris asks otherwise:

- Desktop: 6 columns.
- Tablet: 3 columns.
- Mobile: 2 columns.
- Match gap, card padding, border radius, image min-height, hover/focus behavior, and overflow behavior.
- Verify with browser/DOM computed values on desktop/tablet/mobile, not just by inspecting CSS.

## Design DNA hero image replacement

When Chris asks to replace the image under “헤르메스는 사람의 맥락을 보호하는 조용한 지능입니다.”:

1. Generate or prepare the image at the requested ratio. If using GPT Image 2.5 and exact 19:10 is unavailable, generate the closest wide ratio and crop locally to exact 19:10.
2. Use a durable public asset path under the webapp, e.g. `/assets/design-dna/hero/...png`.
3. The hero image should sit under the declaration text, not as a side ornament, unless Chris asks otherwise.
4. Match the text width rather than the full card width when Chris says it should align with “other text”: use the headline/text max-width, avoid oversized full-bleed treatment.
5. Avoid heavy shadows on this hero image. If Chris flags it as too shadowed, set `box-shadow: none` and verify computed style.
6. Verify natural image dimensions, rendered ratio, desktop/tablet/mobile layout, and no horizontal overflow.

## Infographic treatment for Design DNA axes

If Chris says the Core DNA / Expression Layer sections feel like “just text listed,” convert them into coded infographic structures rather than adding more prose.

Recommended pattern:

- Core DNA (`먼저 느껴져야 하는 3개의 중심축`): central `Hermes Experience` orbit / ring graphic + three axis cards connected conceptually to the center.
- Expression Layer (`브랜드 표면을 만드는 3개의 표현축`): layered/surface plate graphic (`material`, `evidence`, `presence`) + three explanation cards.
- Desktop can be two-column infographic; tablet/mobile should collapse to one column.
- Verify that the old plain cluster-card grid is gone, the new visual elements are present, and no horizontal overflow appears.

## Deployment/verification checklist

- Build the webapp before claiming completion.
- Push to Pages/main when the request asks to update the live webapp.
- Poll the live GitHub Pages asset hashes until the new JS/CSS/assets are served.
- Run browser checks on desktop/tablet/mobile for:
  - expected tile/card counts
  - image `complete` and `naturalWidth/naturalHeight`
  - rendered aspect ratio
  - computed styles when layout parity is requested
  - no horizontal overflow
- Keep the Chris-facing reply concise: what changed, where it lives, what was verified, and the live link.
