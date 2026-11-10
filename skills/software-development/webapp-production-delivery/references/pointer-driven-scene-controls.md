# Pointer, touch, and keyboard controls for interactive sprite scenes

Use when a selectable visual character must remain editorial rather than game-like, but can be repositioned by input.

## Interaction contract
- First click/tap selects a character, freezes only that character, and reveals its role bubble. Other autonomous characters keep moving.
- Once selected, permit mouse/pointer drag, touch drag, and `ArrowUp` / `ArrowDown` / `ArrowLeft` / `ArrowRight` input. Keep the selected character selected until background deselection.
- Use a real `<button>` for each character. Implement `onPointerDown`, `onPointerMove`, `onPointerUp`, `onPointerCancel`, and `onKeyDown`; set `touch-action: none` only on the draggable button, not the full page.

## Implementation pattern
1. Keep character state in scene-relative percentages: `{ x, y, direction, mirrored, duration }`.
2. At pointer-down, capture the pointer and save the pointer-to-character offset. On move, map `clientX/clientY` to scene percentages and subtract that offset. This prevents the character from jumping under the pointer.
3. Route pointer and keyboard movement through one state updater. It must reject an input position if either the grounded footprint is non-walkable or the sampled route crosses a wall, table, or other forbidden region.
4. Use a small fixed keyboard step (for example 3 scene-percent). Update the directional sprite/mirroring from the delta and set the manual movement duration to `0`.
5. Release pointer capture on pointer-up and pointer-cancel. Do not allow a click emitted after drag to re-freeze or reset the selected character’s just-updated position.

## Bubble geometry and visual QA
- A sprite image commonly has a tall transparent canvas. Never assess "above the head" from the button/canvas box alone: inspect the rendered alpha silhouette or screenshot.
- Keep the bubble centered to the character’s scene anchor (`left: 50%; translateX(-50%)`) on desktop. Place it above the visual head with an explicit gap (`bottom` plus `margin-bottom`), including the tail/arrow in the clearance.
- Reserve walkable top headroom for the *bubble*, not just the character footprint. If the bubble clips near the top, increase the allowed minimum y/starting y before lowering the bubble into the face.
- For narrow screens, test lateral overflow independently; use edge alignment variants only when needed, without changing desktop center alignment.

## Required browser checks
1. Click every character and assert its bubble stays fully in the scene; capture the topmost selection as a screenshot and inspect the actual head-to-bubble gap.
2. Verify all four arrow keys in valid corridors; invalid moves must not pass through objects.
3. Verify a mouse drag and a touch drag with real pointer/touch events. Choose a known walkable destination—an unchanged position can correctly mean collision prevention worked, not input failure.
4. Assert selected character stays still during inspection, other walkers still move, background click releases selection, and no console/page errors occur.
5. Repeat a minimal selection + keyboard + mouse-drag test against the deployed URL after confirming hashed assets changed.
