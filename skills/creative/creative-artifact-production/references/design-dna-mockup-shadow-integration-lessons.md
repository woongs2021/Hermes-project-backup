# Design DNA Mockup Shadow & Surface Integration Lessons

Use this reference when revising **Design DNA → DNA Brand Asset → Midjourney + Mockup** outputs, especially outdoor poster/banner/card mockups where shadows, bright whites, or background bleed make the composition feel artificial.

## Core lesson: reset before over-patching

If a mockup has gone through several local/PIL edits and Chris reports new artifacts (weird light, damaged foreground objects, missing posts, rectangular overlays, or transparent-looking surfaces), stop patching the derivative. Reset to:

1. the original mockup file as the geometry/lighting authority,
2. the current best generated composite only as rough visual direction,
3. the source motif/brand metaphor as the graphic reference.

Then regenerate with Kling image-to-image using the original mockup first in the prompt. Explicitly preserve foreground objects, camera, wall/floor, shadows, and perspective.

## Poster / glass / shadow band workflow

When a poster lower band or glass/reflection area looks blank/excluded:

- First try model-native recomposition from the original mockup, not local shadow painting.
- Prompt for the graphic to continue into the poster/glass/shadow/reflection area naturally.
- Require preservation of foreground objects (e.g. black posts/bollards) and no wall/floor spill.
- Avoid manual masks that overlap foreground objects; they easily create light blooms or delete/alter posts.
- If natural shadow integration remains unreliable, prefer a clean full-panel metaphor inside the actual frame/board, but do not let it spill onto wall, floor, or foreground objects.

Good prompt shape:

```text
Use image 1 as the exact original mockup geometry, wall, frame, glass, foreground objects, floor, camera, and light. Use image 2 only as rough direction. Use image 3 as the brand metaphor. Regenerate a high-quality photorealistic mockup where the metaphor is integrated into the poster/glass surface, including the lower shadow/reflection zone. Preserve foreground objects. Do not create light blooms, rectangular masks, wall/floor spill, text, logos, or extra objects.
```

## Bright white / popping background areas

If Chris says 1-1/1-2/1-3 or similar items are too white compared with a calmer reference item:

- Keep the existing motif placement if it is liked.
- Reduce pure white/popping neutral regions to warm ivory, champagne, muted beige, amber-stone.
- Use a calm same-set item as tone reference (for example, `Outdoor Mockup Example 1-6`).
- If Kling still leaves pure whites, apply a targeted post-process only to high-brightness, low-saturation pixels; do not recolor amber/red motif areas or dark shadows.

## Banner transparency / brick-through issue

For vertical banners where the wall/brick appears to show through the fabric:

- Patch only the visible banner interior, constrained by the banner polygon.
- Fill with a warm champagne/amber background tone derived from the motif or nearby banner color.
- Preserve fabric shading and folds using the source luminance/texture.
- Do not touch surrounding wall/brick.
- Verify visually that the patch no longer reads as a hole or transparent fabric.

## Contact sheet QA checklist

Before publishing:

- Original mockup geometry preserved.
- Foreground objects preserved (posts, bollards, frame, hanging hardware).
- No wall/floor spill from the motif.
- No visible rectangular mask or hard stripe.
- No weird light bloom from local masks.
- No pure white/popping background if Chris requested a calmer palette.
- The final file uses a cache-busting revision filename.
- Manifest points only to final approved files; remove untracked intermediate public assets before commit.
