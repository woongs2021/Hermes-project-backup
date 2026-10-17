# Design DNA webapp visual-system update patterns

Use this when Chris asks to refine the Hermes webapp `Design DNA` tab, `DNA Dashboard`, selected GoYJ assets, hero imagery, or Design DNA infographic sections.

## Session-proven patterns

### 1) GoYJ selected assets live under Design DNA → DNA Dashboard
- Treat `Chris Archive` as reference/evidence storage.
- Treat `Design DNA → DNA Dashboard` as the home for Chris-approved GoYJ generated assets.
- Do not place selected GoYJ images under the Chris Archive tab unless Chris explicitly asks.
- If Chris says “저장해줘”, persist only that selected asset; discard or leave uncommitted the unselected candidates.

### 2) Generation model preference
- For the GoYJ DNA candidate loop, Chris wants **GPT Image 2.5** as the default/required image model.
- Do not silently substitute Seedream/Recraft/Kling/image_auto for the scheduled GoYJ DNA image lane.
- If GPT Image 2.5 is unavailable, report the blocker rather than generating with a different model.

### 3) DNA Dashboard grid must mirror Chris Archive
When changing `DNA Dashboard`, keep it visually aligned with `Chris Archive`:
- Desktop: 6 columns.
- Tablet: 3 columns.
- Mobile: 2 columns.
- Match the same tile gap, padding, border radius, image min-height, hover/focus behavior, and overflow discipline.
- Verify computed styles for both grids rather than checking screenshots only.

### 4) Design DNA hero imagery
When Chris asks to place a representative image under the declaration “헤르메스는 사람의 맥락을 보호하는 조용한 지능입니다.”:
- Use a clean framed hero image, not an oversized glowing/decorative object.
- Preferred ratio for the current hero slot: **19:10**.
- Remove excessive shadows; align the image width to the text column/headline width rather than filling the full card if Chris asks for a calmer editorial layout.
- Verify natural image size, rendered ratio, loaded status, and no horizontal overflow on desktop/tablet/mobile.

### 5) Core DNA / Expression Layer should not read as flat text cards
If Chris says these sections feel like text lists, convert them into coded infographics:
- Core DNA: use a central “Hermes Experience” orbit/metaphor plus the three axis cards.
- Expression Layer: use layered surface plates/metaphors plus the three expression cards.
- Preserve the text content, but make the relationship spatial: orbit/center for foundational axes, stacked layers for brand-surface expression.
- Keep desktop as richer two-column infographic; stack naturally on tablet/mobile.

### 6) Fill empty profile/thumbnail slots with Design DNA gradients
If profile images or representative thumbnails look empty:
- Add 19:10 gradient thumbnail frames inside each card.
- Use colors from the Design DNA system rather than generic rainbow AI gradients:
  - warm white / soft container / protected void
  - cobalt and cyan intelligence
  - coral and muted yellow warmth/agency
  - charcoal base
  - frosted glass / tactile optical material
  - editorial grid / archive paper
  - soft orb / presence rim
- Badge/profile placeholders should also use these gradients; avoid black empty squares that look like missing avatars.
- Keep thumbnails framed and shadowless unless Chris asks for depth.

## Verification checklist
- `npm run build:public` passes.
- Live GitHub Pages resolves the new hashed JS/CSS/assets.
- Desktop/tablet/mobile checks pass.
- No horizontal overflow.
- Images load with expected natural dimensions and rendered ratio.
- If matching two grid systems, compare computed CSS values: column count, gap, padding, radius, image min-height, and hover/focus structure.
