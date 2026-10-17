# Design DNA mockup iterative correction lessons

Use this when Chris is iterating on a Design DNA / DNA Brand Asset mockup and points out a visual artifact.

## Marked/circled problem areas

- If Chris uploads a screenshot with a circle/mark, treat the marked area as the primary source of truth. Do not infer a nearby or lower/adjacent area from prior context.
- First restate the exact area in plain language before regenerating: e.g. “upper-left/center fold area inside the banner,” not just “left middle.”
- When using Kling or another image model, include the marked screenshot as a problem-reference image and explicitly prompt: “the marked area identifies what to fix; do not reproduce the marker.”

## When patches fail

- After two failed local/masked fixes on the same artifact, stop patching the patched derivative.
- Reset to the clean original mockup plus the source motif/metaphor and generate from scratch.
- Create at least two focused candidates when time allows, build a small contact sheet, and choose by the specific defect Chris named first, then overall aesthetics.
- If Chris permits changed metaphor area/crop, prioritize a solid, natural surface over preserving the old composition.

## Banner / fabric transparency artifacts

- For vertical fabric banners, avoid compositions where wall/brick texture appears inside folds, bright triangular gaps, or side folds. These read as holes or transparent fabric.
- Prompt for “opaque printed fabric / one continuous textile surface / wall visible only outside the banner.”
- If a local patch still reads as a pasted patch or wall-through artifact, regenerate with Kling from the original mockup rather than repainting the same region.

## Raw mockup replacement

- If Chris asks to replace a raw mockup source image, update the original Mockup collection asset and manifest hash/dimensions, but do not touch synthesized Midjourney+Mockup outputs unless explicitly asked.
- If reusing the same public filename, verify by live manifest hash and live image SHA-256, not just by URL, because browser/GitHub Pages caching can hide replacements.
