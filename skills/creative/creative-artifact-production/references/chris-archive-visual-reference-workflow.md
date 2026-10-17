# Chris Archive visual reference workflow

Use this when Chris uploads images intended for a long-term archive that will later inform brand assets, design-system tokens, visual prompts, package systems, UI directions, or package/brand systems.

## Purpose

Chris Archive is not just file storage. It is a structured reference library for accumulating many images, comparing their aesthetic quality, and extracting repeated design DNA into a future `DESIGN_SYSTEM.md`.

## Recommended root

```text
/opt/data/chris-archive/
├── SCHEMA.md
├── index.md
├── DESIGN_SYSTEM_DRAFT.md
├── images/YYYY/MM/<date>_<slug>_<hash>.jpg
├── entries/YYYY/<date>_<slug>.md
└── exports/
```

## Intake trigger rule

Chris's operating preference:

- If Chris attaches an image and explicitly says `추가해줘`, proceed immediately with archive storage and first-pass analysis.
- If Chris attaches an image without `추가해줘`, do **not** add it to Chris Archive automatically. First ask whether he wants it archived/analyzed.
- This avoids mixing casual visual discussion with long-term design-system source material.

## Per-image workflow

1. Copy the original uploaded image into `images/YYYY/MM/` using a stable slug and short content hash.
   - Recommended filename: `YYYY-MM-DD_<concise-visual-slug>_<sha12>.<ext>`.
   - Slugs should describe the visual DNA, not the Telegram/cache filename, e.g. `luminous-gradient-rounded-portal`, `blue-orange-modular-glow-blocks`, `toward-blue-black-directional-stack`, `we-are-hornet-chrome-blob-poster`.
2. Create/update `SCHEMA.md` if the archive does not yet exist.
3. Add an `entries/YYYY/<date>_<slug>.md` note with:
   - asset path
   - source context
   - short description
   - visible content
   - visual tags
   - color observations
   - typography observations (`none / not applicable` when the image has no text)
   - texture/material observations
   - layout/composition observations
   - metaphor/system meaning
   - product/UX implications
   - aesthetic score and rationale
   - Karina interpretation
   - Go Youn-jung review status/brief
   - extraction candidates for future `DESIGN_SYSTEM.md`
4. Update `index.md` with the entry path, asset path, and review status.
5. Update `DESIGN_SYSTEM_DRAFT.md` only with tentative candidate patterns, not final rules. Add candidates under reusable class-level headings such as `Ambient AI Presence`, `Directional Graphic Force`, `Soft Modular Intelligence`, `Warm-cool luminous field`, `Soft Relational Intelligence`, `Warm Emotional Mesh`, or `Bold Manifesto Typography + Material Overlay`. Do not promote a single-image observation into a final design-system rule.
6. When several images are added in one session, keep the Chris-facing reply short and avoid dumping every analysis section. Confirm saved paths and summarize only the strongest 3–6 design-DNA signals; the detailed entry file carries the full analysis.
7. For Chris Archive intake over Telegram, avoid sending repeated mid-work progress fragments like “분석했어, 저장할게” before every tool step. If the task is straightforward, work quietly through storage/analysis/index/draft updates and send one concise completion message only after verification. Send an interim note only for a real blocker or unusually long-running operation.
8. Verify the asset and entry exist before reporting completion.
9. If the same visual/hash appears again, still archive it when Chris explicitly says `추가해줘`, but mark it as related/supporting evidence rather than pretending it creates a wholly new design-DNA cluster. Summarize that relationship briefly in the completion note.
10. As the archive grows, prefer one combined script/tool pass for copy → entry → index → draft → verification so Telegram receives a single clean completion rather than fragmented progress chatter.
11. When Chris asks to put the archive into the webapp, publish via a **public-safe manifest**, not by making the webapp read private archive folders directly:
   - copy only selected/reference images into the webapp's `public/assets/chris-archive/` path;
   - generate `public/data/chris-archive.json` with title, created date, image path, short summary, tags, and extraction candidates;
   - add a dedicated tab/dashboard that fetches the manifest with `import.meta.env.BASE_URL` and renders thumbnails from public assets;
   - thumbnail click should open an accessible modal/dialog with the image, Karina summary, tags, candidates, and a visible `×` close button;
   - verify local preview with manifest item count = rendered tile count, at least the first image loading, modal open/close behavior, and mobile grid columns before claiming completion.
12. If several images are uploaded in one message, process them as a batch and send one completion summary with counts and strongest clusters rather than one long per-image report.

## First-pass analysis pattern

Use a consistent but lightweight Korean structure so many future images remain comparable:

- **Short description:** one concise read of what the image is.
- **Visible content:** what is actually visible; avoid inventing hidden intent.
- **Visual tags:** compact nouns/adjectives for later filtering and clustering.
- **Color:** role of key hues, not just names.
- **Typography:** font/microcopy/rhythm when present; if absent, note that the image is text-free and therefore useful as mood/material reference.
- **Texture/material:** grain, glow, blur, plastic, glass, paper, metal, tactile softness, mesh, halftone, chrome, etc.
- **Composition:** grid, center object, negative space, symmetry, crop, depth, repetition, occlusion.
- **Metaphor/system meaning:** what design-system or product metaphor the image can support.
- **Product/UX implications:** where it could be used and where it would be risky.
- **Extraction candidates:** color/material/shape/layout/metaphor/brand-asset implications.

## Patterns observed in the initial archive session

Treat these as **candidate clusters**, not final rules:

- **Ambient AI cards:** compact rounded cards, tiny system labels, warm signal accents, context-aware/personal-state UI.
- **Luminous presence:** warm-cool glow, rounded portals, AI as atmosphere rather than robot/avatar.
- **Directional manifesto graphics:** electric blue/black/white, large uppercase type, stacked directional forms, future-facing motion.
- **Soft modular intelligence:** rounded blocks/modules, blue structure with warm orange backlight, central voids/corridors.
- **Relational mesh fields:** overlapping spheres/orbs, coral-pink-violet-blue transitions, woven mesh/halftone textures.
- **Warm emotional mesh:** red/orange/magenta orbs for warmth/creative energy; use carefully to avoid warning/overload tone.
- **Bold type + material overlay:** oversized uppercase type as background architecture, intentional occlusion, coral organic blobs, soft chrome/liquid-metal objects.
- **Product/component grammar:** dot-matrix AI processing, glass capsule progress bars, honest status semantics, pause/stop affordances, and accessibility labels.
- **Design-system/token boards:** bento/masonry specimen cards for showing colors, type, controls, state tokens, and future `DESIGN_SYSTEM.md` companion visuals.
- **Human/lens identity:** human silhouette, eyewear/perception metaphors, monochrome identity fields, and brand marks as layout tension; isolate third-party logos/wordmarks.
- **Pattern/motion/mobility:** phase-shift glyph grids, violet displacement/audio waves, motion-principle boards, and cockpit/media contexts with safety/glanceability review.

## Brand-safety and originality guardrails

- Preserve originals, but never directly copy reference images into new brand output.
- Extract principles, tokens, composition logic, material mood, and metaphor direction.
- If an image includes third-party text/brand names (e.g. a manifesto poster), do **not** reuse literal wording, names, or brand identity. Extract only type scale, layering, occlusion, color/material relationships, and composition principles.
- For common AI aesthetics such as glow gradients, spheres, chrome blobs, and glassy 3D, require Go Youn-jung to define restraint: saturation, grain/mesh density, blur, darkness ratio, usage frequency, and where it should be limited to hero/campaign/package/motion rather than daily UI.
- For sensitive UI references involving emotion, stress, social profiles, or personal state scoring, explicitly note privacy/agency/overclaim risks and reframe toward user control and psychological safety.

## Karina vs Go Youn-jung roles

- Karina: first intake, durable storage, metadata, product/UX interpretation, privacy/overclaim caution, orchestration, draft design-system candidate updates.
- Go Youn-jung: aesthetic judgment, brand/design DNA extraction, keep/discard critique, color/type/layout/metaphor token candidates, shortlist recommendation.

## Good Chris-facing completion reply

Keep it warm and concise in Korean:

- Say 저장 완료.
- Provide asset path and entry path.
- Mention index and `DESIGN_SYSTEM_DRAFT.md` were updated.
- Summarize the strongest 3–6 signals only.
- Note one caution when relevant (e.g. generic AI glow, over-intense red, third-party text/brand copying, cold/aggressive tone).

Avoid turning every uploaded image into a production task unless Chris asks.
