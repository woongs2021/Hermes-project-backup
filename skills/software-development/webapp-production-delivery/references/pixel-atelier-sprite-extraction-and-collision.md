# Pixel Atelier sprite extraction, layering, and movement zones

Use when putting generated full-body pixel-character sheets onto an editorial web scene with transparent sprite PNGs.

## 1. Extracting opaque figures from cream-sheet backgrounds

Generated sheets can have a subtly varying cream background. Avoid YUV `chromakey` for this material: it can key out dark hair or clothing that shares chroma characteristics with the backdrop, producing see-through bodies.

Prefer this deterministic pipeline:

1. Crop each direction frame consistently from the source sheet.
2. Use RGB `colorkey` rather than YUV `chromakey`; tune a conservative threshold against a dark QA board.
3. Remove remaining disconnected cream speckles by retaining the primary connected opaque component.
4. Normalize the retained figure alpha to binary values only: `0` for the intentional transparent exterior and `255` for every retained character pixel.
5. Composite representative light- and dark-clothed characters on a dark background and visually inspect for holes, rectangular cards, and halos.

A good acceptance check validates all runtime sprites are RGBA at the expected dimensions and have no semi-transparent alpha values. Validate multiple directions and at least one character with a dark outfit and one with pale clothing.

## 2. Scene stacking

Keep the background and walkers in an isolated stacking context:

```css
.scene { position: relative; isolation: isolate; }
.scene > img { position: absolute; z-index: 0; }
.walker { position: absolute; z-index: 3; opacity: 1; mix-blend-mode: normal; }
```

Put readable captions and controls above the walkers only if characters must not obscure them. Do not use a low-opacity walker to make the scene feel calm; manage calmness through size, cadence, and no-go zones instead.

## 3. Deriving movement constraints from the actual background

Do not block only obvious desks. Inspect the scene background and record normalized (`x`, `y`, `width`, `height`) no-go rectangles for walls/window ledges, shelving, plants, cabinets, tables, stools, and reserved text/control areas.

- Increase each character collision footprint when display size changes.
- Test each candidate destination *and sampled points along the full path*, not endpoints only.
- Verify all initial positions programmatically against the same constraints.
- Keep caption/control reserves non-walkable so large sprites do not cover essential copy.

When the scene is responsive, express sprite locations and collision rectangles in percentage space. Re-run the position validation whenever sprite scale or scene geometry changes.
