# Midjourney + Mockup Detail Copy Pattern

Use when maintaining **Design DNA → DNA Brand Asset → Midjourney + Mockup** detail views, cards, or manifests.

## Trigger

Chris says the detail-view explanations feel too process/history-oriented, or asks for mockup descriptions to explain the image itself rather than how it was made.

## Principle

The public-facing detail view should read like a design/archive description, not a changelog. Keep process/provenance available only where useful, but the primary description should explain what the viewer sees and how the image works as a brand surface.

## Rewrite target

For each Midjourney + Mockup collection and item, rewrite visible copy around:

- color and tonal behavior
- graphic motif / surface rhythm
- material and physical surface
- composition and crop behavior
- how the motif reads on the specific mockup object
- brand-asset use context, e.g. coffee cup, bag, sign, outdoor board, apparel, phone surface

Avoid making the item description about:

- generation provider/tool names
- resynthesis/revision history
- “added as last example” or ordering history
- previous-version defects
- correction narratives
- prompt/process plumbing

## Fields to check

In `public/data/brand-mockup-assets.json`, detail views may expose more than `item.description`. Check all visible fields, especially:

- root `sourcePolicy`
- collection `description`
- collection `status`
- collection `synthesisTool`
- item `description`

It is fine to keep `sourceGraphic` as provenance, but do not let it dominate the primary description.

## Good public-copy shape

Example item description:

> 코발트 블루와 블랙의 찢어진 종이 가장자리가 거친 레이어감과 선명한 대비를 만드는 그래픽 시스템입니다. 보드와 북렛, 작은 카드가 각각 다른 표면으로 분리되어 보이면서도 같은 그래픽 언어로 연결됩니다.

Example collection note:

> 코발트 블루와 블랙의 torn-paper 표면을 Outdoor Mockup A에 적용한 세트입니다. 종이 가장자리, 찢긴 면, 강한 대비가 야외 표면 위에서 또렷하게 작동합니다.

## Verification

1. Validate JSON.
2. Run the webapp build.
3. Scan visible text fields for history/process terms such as `Kling`, `resynthesis`, `revision`, `rev`, `교정`, `재합성`, `added`, `last`, `기존`, `이전`, `수정`, `image_to_image`, `nano_banana`.
4. Open at least one live detail modal from the Midjourney + Mockup rail.
5. Confirm the modal shows image-native copy, full-resolution detail image still loads, no console errors appear, and no horizontal overflow exists.

## Deployment pitfall

After a successful push and Pages run, the live manifest can lag briefly behind the deployment. Verify the public JSON with a cache-busting query and compare it against the local `dist/data/brand-mockup-assets.json` hash before reporting live completion.
