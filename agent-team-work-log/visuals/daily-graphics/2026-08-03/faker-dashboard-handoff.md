# Faker dashboard handoff — 2026-08-03

- Status: ready
- Package: 2 final stills + 2 turntable MP4s
- Data JSON: `/opt/data/hermes-webapp-build-loop/data/image-gallery/2026-08-03.json`
- Current set: `/opt/data/hermes-webapp-build-loop/data/image-gallery/final/current-home-visual-set.json`

## Implementation contract
- Grid: render `faker_dashboard.grid_still_asset_path` as static 1080×1080 image.
- Detail: render `faker_dashboard.detail_turntable_asset_path` as `autoplay muted loop playsinline`.
- Metadata: show `date_data`, `why_this_image.design_rationale`, `metaphor`, `theme`, and QA note.
- Prompt: keep hidden unless Chris asks.

## Items
- Calm Settlement Basin
  - date: 2026-08-03
  - why: 복잡한 사용자 신호가 즉시 결론으로 튀지 않고, 한 번 가라앉아 공통의 가치 규칙으로 정리되는 과정을 ‘얕은 basin’으로 표현했습니다.
  - still: `/opt/data/hermes-webapp-build-loop/assets/image-gallery/2026-08-03/stills-1080/01-mint-calm-settlement-basin-1080.png`
  - turntable: `/opt/data/hermes-webapp-build-loop/assets/image-gallery/2026-08-03/turntables/01-mint-calm-settlement-basin-turntable-1080.mp4`
  - QA: source_still_is_tight_crop; turntable usable but object remains cropped/tight in side/end frames
- Frictionless Journey Slipper
  - date: 2026-08-03
  - why: 미래 One UI의 좋은 AI 경험을 “기능을 더하는 것”보다 먼저, 사용자가 부담 없이 발을 들이는 낮은 마찰의 동선으로 해석했습니다.
  - still: `/opt/data/hermes-webapp-build-loop/assets/image-gallery/2026-08-03/stills-1080/02-neutral-frictionless-journey-slipper-1080.png`
  - turntable: `/opt/data/hermes-webapp-build-loop/assets/image-gallery/2026-08-03/turntables/02-neutral-frictionless-journey-slipper-turntable-1080.mp4`
  - QA: best_current_candidate; mostly full object, last frame mildly tight but acceptable
