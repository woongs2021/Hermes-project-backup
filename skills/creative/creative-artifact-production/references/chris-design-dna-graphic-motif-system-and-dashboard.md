# Chris Design DNA graphic motif system + DNA Dashboard workflow

Use when Chris is refining GoYJ-generated Design DNA assets, saving selected motif candidates, or asking to expose Design DNA rules in the Hermes webapp.

## Core correction from Chris

GoYJ images are **not finished graphic design deliverables**. They are composable **graphic motif materials** Chris will later combine with mockup, package, brand, or UI designs.

Evaluate and prompt them as materials that can be:

- cropped
- masked
- overlaid
- repeated
- layered
- placed on package surfaces
- used as UI/card background fields
- used as small signal/accent fragments

## Persistent motif generation rules

- Use GPT Image 2.5 only for the GoYJ DNA motif candidate loop unless Chris explicitly changes the model rule.
- Use Chris Archive / Design DNA as the primary visual source, not generic AI aesthetics.
- Avoid finished posters, completed labels, app icons, logos, product mockups, UI screenshots, and standalone artworks.
- Favor clean primary motif logic over decorative filler.

### Five candidate roles

1. **Surface Field Motif** — broad surface/texture/background material. Remove incidental lines, random decoration, scratches, fake UI fragments, and unnecessary micro details.
2. **Stroke / Line Motif** — line-only overlay. No filled planes, blobs, color blocks, surface patches, object renders, or secondary motifs.
3. **Soft Object Motif** — simple crop-friendly object/mark seed. Prefer cleaner circular/formal geometry when appropriate; avoid logo/app-icon framing.
4. **Pattern / Repeat Motif** — one clear repeat/mask logic. Reduce complexity and vary color tone when refining.
5. **Signal / Accent Motif** — small badge/seal/state cue material. Do not add yellow line-graphic decoration; yellow is allowed only as a quiet filled accent/material cue when essential.

## Negative prompt additions

Always include or preserve these constraints when relevant:

- no incidental decorative lines
- no random scratches
- no unnecessary orbit marks
- no mixed visual systems
- no yellow line graphic decoration
- for Stroke / Line Motif: linework only on a quiet neutral base; no filled planes/blobs/color blocks/surface patches/object render

## Save and publish rule

- Unselected GoYJ candidates remain temporary review sets.
- Only images Chris explicitly selects with `저장해줘` should be copied into the selected DNA archive and the webapp.
- Selected GoYJ images belong under **Design DNA → DNA Dashboard**, not Chris Archive.
- Chris Archive remains source/reference/evidence; DNA Dashboard is for selected generated outputs.

## Webapp implementation pattern

When Chris asks to show saved GoYJ selections in the webapp:

1. Copy selected images into `public/assets/dna-archive/YYYY-MM-DD/` with durable safe filenames.
2. Merge entries into `public/data/dna-archive.json` without changing unrelated manifests.
3. Keep the DNA Dashboard grid visually matched to Chris Archive.
4. If Chris asks for the principles to be visible, add a public Markdown document such as `public/docs/design-dna-system-principles.md` and expose two controls:
   - `Design DNA 시스템 원칙 보기` — modal/popup with the Markdown text.
   - `MD 다운로드` — direct download link.
5. Use the same modal/action pattern as the Chris Archive design-system document.
6. If Chris says the Design DNA / DNA Dashboard toggles feel heavy, remove shadows, reduce stroke intensity, and keep active state flat — no loud gradient, no card-like elevation.

## Verification checklist

- Production build succeeds.
- Manifest item count equals rendered DNA Dashboard tile count.
- Newly selected images return HTTP 200 and load as square images after scroll/lazy-load if needed.
- Principles Markdown returns HTTP 200, opens in the modal, and download link points to the public doc.
- Design DNA / DNA Dashboard toggle wrapper and active tabs have `box-shadow: none`.
- Desktop/tablet/mobile have no horizontal overflow.
- Commit only relevant webapp files; revert timestamp-only or unrelated manifest churn before commit.
