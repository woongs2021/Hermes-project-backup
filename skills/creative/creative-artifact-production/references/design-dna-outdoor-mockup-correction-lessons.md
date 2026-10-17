# Design DNA outdoor mockup correction lessons — 2026-10-06

## What happened

During Outdoor Mockup Example 1 corrections, repeated small fixes missed Chris's intended defect because the target area was inferred incorrectly. Chris later sent a screenshot with a circle; the actual problem was the upper-left/center fold area of the vertical fabric banner, not the lower-left/center region.

## Durable workflow lessons

1. **Use the user's marked screenshot as the primary target reference.**
   - If Chris circles a defect, include that marked image as an explicit image reference for Kling/Higgsfield when regenerating.
   - In the prompt, say the annotation identifies the target area but must not be reproduced.
   - Restate the exact region in the response before acting, e.g. “upper-left/center fold area,” not just “left-middle.”

2. **Stop incremental patching after repeated misses.**
   - Local/PIL patches can introduce new artifacts: light blooms, pasted rectangles, foreground object damage, or wrong-region fixes.
   - If two attempts do not fix the user's perceived defect, discard the derivative direction and regenerate from the clean original mockup.

3. **Generate multiple fresh candidates when a defect is visually ambiguous.**
   - For fabric/banner transparency or hollow-looking folds, create at least two Kling candidates from scratch using:
     1. original mockup geometry,
     2. source brand metaphor,
     3. calm tone reference if needed.
   - Allow metaphor crop/area changes when Chris permits; solving the defect matters more than preserving the exact previous motif placement.
   - Compare candidates in a contact sheet before publishing.

4. **Prompt language for opaque fabric defects.**
   - Use: “opaque printed fabric,” “one continuous solid cloth,” “wall visible only outside the banner,” “no see-through area,” “no brick/wall texture inside fabric,” “no hollow/cutout/translucent patch.”
   - Explicitly forbid reproducing user annotations: “do not reproduce the black circle/annotation.”

5. **For multi-board/booklet mockups, preserve physical separation rather than painting one panorama.**
   - If a mockup has two overlapping boards, books, cards, or booklets, do not let the source graphic flow continuously across them unless Chris explicitly asks for a panoramic wrap.
   - Use the best prior example with clear separation as a reference image (e.g. A-1-5): visible step/depth difference, vertical seam/overlap edge, separate front faces.
   - One board can keep the primary crop; the other should use a different crop/angle/scale of the same motif so it reads as a related but separate application.
   - When local patching only changes the surface but not the perceived object structure, regenerate with Kling from the clean original mockup + separation reference + source motif. Prompt for: “two distinct boards/booklets,” “visible physical step/seam,” “separate front faces,” “different crop on the right board,” and “no continuous panorama across the seam.”
   - Generate at least two candidates and choose via contact sheet; publish only after the live manifest and modal image point to the new rev filename.

6. **Deployment verification pitfall.**
   - GitHub Pages can accept the push while the deploy job remains `waiting`; live manifest may still serve the previous hash.
   - Report that distinction clearly: code pushed/local build verified vs live Pages reflected.
   - If live is still waiting, share the generated local asset for visual review and, if useful, create a short watchdog that notifies when the live manifest contains the new cache-busting filename.

## Good user-facing behavior

- Acknowledge the miss plainly and briefly.
- Do not over-explain; move immediately to a fresh generation path.
- When the user is frustrated, avoid defending previous attempts. Say what changed in the workflow: “I’m discarding the patched derivative and regenerating from the original mockup.”
