---
name: creative-artifact-production
description: "Use when creating visual, design, diagram, browser-demo, generative-art, text-art, or interactive creative artifacts; umbrella for HTML/CSS mockups, diagrams, ASCII art/video, p5.js, ComfyUI, TouchDesigner MCP, design systems, Excalidraw, infographics, and real-time visual tools."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [creative, design, diagrams, html, css, ascii, p5js, excalidraw, infographics, prototypes]
    related_skills: [media-content-production]
---

# Creative Artifact Production

## Overview

This is the class-level umbrella for producing creative artifacts rather than prose-only answers. The shared workflow is: clarify the output medium, choose the right artifact lane, generate a concrete file or machine-readable artifact, then verify it visually or structurally before presenting it.

Use this instead of searching for narrow one-off skills such as a particular diagram renderer, web-design style catalog, ASCII utility, or prototype pattern. The details below name the lane-specific tools and pitfalls so one searchable skill covers the whole creative-artifact family.

## When to Use

- The user asks for a diagram, infographic, visual explanation, architecture/cloud graphic, or hand-drawn-style sketch.
- The user asks for HTML/CSS mockups, landing pages, design variants, design-system references, or token/spec files.
- The user asks for ASCII art, text-as-visuals, p5.js/gen-art, browser demos, or interactive prototypes.
- The user asks for TouchDesigner, Excalidraw, p5.js, pretext, or another creative coding environment by name.
- The user asks to humanize or make generated copy sound more natural as part of a creative artifact.

## Core Workflow

1. **Pick the artifact lane first.** Do not mix output formats accidentally: SVG/HTML diagram, Excalidraw JSON, p5.js sketch, static HTML mockup, DESIGN.md, ASCII, or real-time TouchDesigner network.
2. **Create a durable artifact.** Prefer a file path, HTML document, JSON scene, script, or generated media handle over a prose description.
3. **Use references/templates when present.** Many legacy narrow packages had large template banks; treat this umbrella as the routing surface and keep specialized catalogs as archived packages or support files.
4. **Verify.** Run syntax checks for JSON/JS/HTML where practical; use browser or vision review for visual layout claims.
5. **Report the handle and tradeoffs.** Tell the user where the artifact is and which constraints guided the design.

## Lane Guide

### HTML/CSS design artifacts

- For one-off landing pages, dashboards, decks, or prototypes, produce a self-contained HTML file with embedded CSS/JS unless the project requires a framework.
- For throwaway comparison work, generate 2-3 distinct variants rather than over-polishing one direction.
- For real-brand inspiration, use a design-system catalog mindset: extract typography, spacing, color, layout rhythm, and interaction patterns without copying private assets.
- For token/spec work, author DESIGN.md-style sections in canonical order: colors, typography, spacing, components, states, and export notes.
- For Chris's research / OBD / agent-team dashboard work, use `woongdesignv2` tokens with a clean high-end SaaS/bento admin style: light off-white canvas, rounded cards, soft shadows, generous spacing, restrained typography, metric/chart/list panels, and no neon/glassmorphism/generic AI-startup look. See `references/chris-dashboard-ui-reference.md`.
- When Chris shares agent/team profile images for a future homepage or team-introduction page, normalize them into durable role-based filenames, store them as product assets, and create a manifest for the future builder agent. See `references/agent-team-profile-image-assets.md`.

### Diagrams and infographics

- Architecture diagrams: favor dark themed SVG/HTML, clear grouping, labeled flows, and deployment boundaries.
- Infographics: choose layout by information shape (timeline, funnel, matrix, hierarchy, hub-spoke, comparison), then choose style separately.
- Excalidraw: output valid scene JSON, use rough/hand-drawn defaults, and keep element IDs unique.
- Always optimize for readable labels; a beautiful illegible diagram fails the task.

### ASCII and text visuals

- Use local CLI tools when available for banners, boxes, cowsay, and image-to-ASCII conversions.
- For ASCII video or dense text animation, treat it as a media pipeline: inputs, frame composition, palette, encoding, and output verification.
- Keep monospace assumptions explicit and avoid layouts that collapse on mobile chat clients unless the user wants terminal output only.

### Creative coding and interactive demos

- p5.js: use a minimal HTML viewer, deterministic seeds when useful, and export frames when the user needs deliverable media.
- Pretext/text-layout demos: use it when the creative idea is text as geometry, text flowing around obstacles, or DOM-free typographic interaction.
- TouchDesigner MCP: control a running instance by creating operators, wiring networks, setting parameters, and exporting screenshots/video; verify operator state rather than assuming the graph exists.
- ComfyUI or image/video generation pipelines belong here when the task is creative production, but model setup and batch execution details may also overlap with media/ML workflows.
- For Chris's image/video generation workflow, prefer Higgsfield CLI/MCP as the generation studio when credits are available, with Karina/Go Youn-jung handling brief, prompt, and critique. See `references/higgsfield-cli-generation-workflow.md` for install/auth/generation patterns, including loopback OAuth callback handling.
- For Chris's Higgsfield Korean summary cards/infographics, do not ask the image model to render Korean text. Generate a text-free soft-3D/editorial background, then overlay exact Korean typography locally at the requested pixel size and verify legibility before sending. See `references/higgsfield-korean-summary-card-workflow.md`.
- For Chris's weekly paper-report visual loop, Go Youn-jung should **not** produce SNS/carousel prompt packs. After Muyeol-selected weekly best-3 reporting, generate only one 1:1 abstract metaphor image with Higgsfield when available, and leave the exact prompt used. Use `woongdesignv2` only as a restraint/material/editorial-quality reference, not as a requirement to create UI slides. Chris's core quality bar is that the result should not look AI-generated (`AI티가 안 나는 것`): avoid glossy AI-startup aesthetics, neon/glassmorphism, fake 3D UI, stock AI symbols, distorted pseudo-text, synthetic glow, and over-smooth gradients. Store the generated image, exact prompt, output path/URL, quality notes, and limitations under `/opt/data/agent-team-work-log/visuals/YYYY-WW/`. Final delivery must also include `왜 이 그림인가`: 2-4 concise Korean bullets explaining why this image/metaphor was chosen, how it connects to the weekly best-3 and Muyeol's validation/caution, and how Chris should read it. Do not repeat the same visual look every week: check previous visual notes when possible and deliberately vary metaphor, composition, material texture, color temperature, art/reference movement, density, lighting, or depth. See `references/chris-weekly-paper-abstract-visual.md` for the current weekly abstract-image pattern.
- For Chris's daily Go Youn-jung graphic loop, produce **two** 1:1 Higgsfield images per day to conserve credits: choose two non-overlapping `woongdesignv2` theme sets or nuanced palette mixes, include one abstract/systemic metaphor and one concrete metaphor, and bias the visual language toward premium illustration / soft-3D objects with rounded, tactile, non-sharp forms. Across any 7-day rolling window, each day should feel like a different color/metaphor chapter: check recent daily-graphics logs and avoid repeating the same daily color pairing, object/metaphor family, material language, silhouette, or composition logic when possible. Avoid spiky, blade-like, needle-like, jagged, hazardous, aggressive object silhouettes, and excessive wave/ripple/fluid/flowing-sheet motifs unless Chris explicitly asks for them. Use simple theme-matched solid backgrounds. Save exact prompts and JSONL under `/opt/data/agent-team-work-log/visuals/daily-graphics/`, but do not include exact prompts in the recurring delivery; share prompts only when Chris separately asks Go Youn-jung/Karina for them. Deliver concise Korean rationale including why each image was made, the Higgsfield model used, and why that model was chosen. For Telegram delivery, prefer Go Youn-jung's own DM/bot identity rather than Karina/default delivery; if cron auto-delivery makes the message appear from Karina, set cron delivery to local and send via the Go Youn-jung profile's Telegram bot without logging credentials. Mirror only the final approved/tone-matched image assets and rationale metadata into `/opt/data/hermes-webapp-build-loop/data/image-gallery/` for Faker's future home `HomeVisualHero` and Pinterest-like image tab. Drafts, rejected candidates, and tone-mismatched prior assets should be removed from the webapp feed/assets. Maintain a stable current pointer at `/opt/data/hermes-webapp-build-loop/data/image-gallery/final/current-home-visual-set.json`. Weekly Muyeol governance should review metaphor diversity, prompt drift, model/credit/session risk, media-attachment delivery, and whether loop changes should be KEEP/ADJUST/HOLD/REMOVE before Karina applies them. If Higgsfield auth/credits/model access blocks generation, label the result as dry-run only and never imply media was generated. See `references/chris-daily-higgsfield-graphic-loop.md` and `references/goyounjung-visual-loop-delivery-and-gallery.md`.

### Programmatic explainer video / Manim

Use this lane for 3Blue1Brown-style educational animations, math/algorithm visualizations, architecture explainers, research-paper explainers, equation derivations, and data stories built with Manim Community Edition.

- Start with a narrative arc in `plan.md`: misconception, aha moment, scene list, visual elements, palette, and optional voiceover script.
- Use one Python script with one independently renderable `Scene` class per scene; keep shared color/font constants at the top and add subcaptions when helpful.
- Prefer geometry before algebra, opacity layering for attention, monospace text for reliable Pango rendering, and deliberate pauses after each reveal.
- Iterate with `manim -ql`, then render production with `-qh`; stitch scene clips with ffmpeg and inspect preview stills/video before claiming completion.
- Re-homed Manim references live under `references/manim-video/` and setup tooling under `scripts/manim-video/setup.sh`.

### Voice and copy humanization

- When the artifact includes narrative or product copy, strip generic AI phrasing and add specific voice, stakes, concrete nouns, and rhythm.
- Do not make unsupported biographical claims; humanization changes style, not factual grounding.

## Consolidated Legacy Knowledge

- `architecture-diagram`: dark SVG/HTML architecture and cloud diagrams with strict visual hierarchy.
- `ascii-art`: pyfiglet/cowsay/boxes/toilet/image-to-ASCII utilities and terminal-friendly presentation.
- `ascii-video`: colored ASCII MP4/GIF pipelines with composition, shader, optimization, and troubleshooting references.
- `baoyu-infographic`: 21 layout families x 21 visual styles for structured infographics.
- `claude-design`: context-first one-off HTML artifacts; ask only questions that change the design.
- `design-md`: Google DESIGN.md token/spec authoring and validation.
- `excalidraw`: hand-drawn JSON diagrams with dark-mode/color references and upload script patterns.
- `future-mobile-ux-leadership`: warm product-design coaching and agent-team delegation for future mobile UX work.
- `humanizer`: remove AI-isms and tune prose voice in creative deliverables.
- `p5js`: p5.js sketches, shaders, interaction, 3D, frame export, and local preview.
- `popular-web-designs`: real design-system catalog for style borrowing without copying.
- `pretext`: @chenglou/pretext browser demos and text-as-geometry patterns.
- `sketch`: quick divergent HTML mockups for comparison before implementation.
- `touchdesigner-mcp`: twozero MCP control of TouchDesigner networks, operators, animation, audio-reactive visuals, and export.
- `manim-video`: Manim CE narrative planning, math/algorithm/research-paper animation, rendering, ffmpeg stitching, and production-quality visual design references.

## Common Pitfalls

1. **Returning prose instead of an artifact.** Creative tasks usually need a file, JSON, rendered image, or runnable page.
2. **Choosing the renderer too late.** Pick the output medium before writing content; each lane has different constraints.
3. **Flattening package-specific assets.** If an archived narrow skill had support files, do not reference its old relative paths unless those files were explicitly re-homed.
4. **Template cargo culting.** Use templates as starting points, not as a substitute for the user's content and constraints.
5. **No visual verification.** If the artifact is visual, inspect it with browser/vision or run a renderer when possible.
6. **Assuming remote OAuth callback works on the user's localhost.** For CLI tools like Higgsfield in a remote Hermes host, have the user paste the failed `localhost/callback?...` URL and call it from the agent host while the login process is waiting.
7. **Forgetting profile-local Higgsfield state.** Specialist-profile cron jobs may run with that profile's `HOME`, so Higgsfield auth/workspace config that works in the default profile may be missing for Go Youn-jung or another specialist. Before rerunning a specialist-owned Higgsfield job, verify with `HOME=/opt/data/profiles/<profile>/home PATH="/opt/data/.npm-global/bin:$PATH" higgsfield workspace status`. If Chris intends the specialist to use the same Higgsfield account, align the profile-local `.config/higgsfield/{credentials.json,config.json}` from the working profile with `0600` permissions and never print tokens.
8. **Trusting generated Korean text blindly.** For Korean-heavy diagrams/cards, generated image text may break; keep labels short and switch to HTML/SVG/editable artifacts when legibility is the goal.

## Verification Checklist

- [ ] Output lane chosen deliberately.
- [ ] Artifact was actually created or transformed.
- [ ] Syntax/rendering checked where practical.
- [ ] Final response includes path/URL plus short design rationale.
- [ ] Any unverified visual assumptions are labeled.
