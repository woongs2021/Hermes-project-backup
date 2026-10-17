# Kling object-only flat-background workflow

Use this when Chris wants Go Youn-jung/Kling visuals to be a single premium object on a plain basic color background, not a staged scene.

## Session learning

A Higgsfield-style prompt reused directly in Kling can produce a complex editorial scene: poster/card framing, background texture, fake text, floor/wall separation, or decorative context. For Chris's daily visual loop this is often wrong when the intended asset is an isolated object for UI/gallery reuse.

## Preferred prompt shape

Start with the background and isolation constraints before describing the object:

```text
Square 1:1 isolated product render. One single rounded soft-3D object only, centered. Completely flat solid background color #F6F3EE. No gradient, no texture, no shadows on walls, no floor, no room, no scenery, no poster, no frame, no card, no panel, no border. The entire background must be a single uniform color.

The object is ... [object description]. Premium tactile matte ceramic and soft rubber, simple calm editorial product object. Object should be fully visible with clean silhouette and no surrounding props.

Absolutely no text, no letters, no pseudo text, no logo, no watermark, no symbols, no numbers, no UI, no robot, no neon, no glassmorphism, no cyberpunk. Do not add decorations or background elements. Minimal studio cutout, object only on flat color.
```

Use Kling image models that support `aspect_ratio=1:1`, such as `kling-image-v3_0` or `kling-image-v3_0_omni`. In the observed test, the `v3_0_omni` run followed the object-only direction better than the first direct reused prompt.

## Video prompt shape

For image-to-video, keep the video prompt equally restrictive:

```text
Create a clean 5-second slow product turntable from the input image. Preserve the single rounded object exactly. Keep the background extremely simple: one plain warm off-white solid color, no scene, no room, no texture, no pattern, no frame, no text, no logo, no added props. Stable camera, gentle vertical-axis orbit, premium soft-3D product motion. No morphing, no new objects, no subtitles, no audio.
```

After generation, download the MP4, check it with `ffprobe`, and create a muted copy with `ffmpeg -an` when needed.

## Quality checks before delivery

- Background should read as a basic solid color, not a room, poster, panel, wall/floor set, or textured editorial backdrop.
- The image should contain one object only, centered, with no decorative props.
- There should be no pseudo-text, labels, symbols, UI, logos, or watermark-like marks.
- The turntable should preserve object identity and not introduce complex background elements.
- If Kling keeps adding floor shadows or mild gradients, report that limitation plainly; do not claim it is a mathematically flat vector background unless locally post-processed and verified.

## Optional local cleanup

If a generated object is good but the background has mild texture, a local post-process may help. Prefer edge-connected flood-fill or segmentation-style replacement over naive color-threshold masking, because naive masking can erase light object surfaces. Verify visually after cleanup; do not deliver if the object is visibly damaged.
