# Chris Archive high-volume curation lessons

Use this when Chris uploads many visual references for Chris Archive in one session and says `추가해줘`.

## Session signals captured

- Chris corrected the Telegram experience: repeated mid-work progress fragments looked like the assistant was “말을 하다 말어.” For straightforward archive intake, work quietly and send one concise completion after verification.
- The archive can grow quickly to dozens of entries. Per-image storage is useful, but `DESIGN_SYSTEM_DRAFT.md` should not grow by inventing a wholly new class for every single image when it is really supporting evidence for an existing cluster.
- Several uploads are close variants or exact/same-source detail crops. Still archive when Chris explicitly asks, but mark them as related/supporting/detail evidence and summarize that relationship.
- Some images include third-party words, logos, brands, products, or UI examples. Preserve the source but extract only principles; do not reuse literal marks, copy, product names, or exact layouts.

## High-volume intake pattern

1. Load the Chris Archive workflow reference.
2. For each image, compute a short content hash and stable slug.
3. Copy original to `/opt/data/chris-archive/images/YYYY/MM/`.
4. Write one entry in `/opt/data/chris-archive/entries/YYYY/` with the standard analysis schema.
5. Update `index.md`.
6. Update `DESIGN_SYSTEM_DRAFT.md` as tentative cluster evidence:
   - Prefer adding the entry under an existing candidate cluster.
   - Create a new cluster only when the image introduces a genuinely new class-level pattern.
   - Avoid turning every image into a new final principle.
7. Verify asset and entry exist before final reply.
8. Reply once, concisely: saved paths + 3–6 strongest design-DNA signals + one caution if relevant.

## When the user says “아까 하던일 마저해줘”

- Treat it as an interruption-recovery request.
- First finish any pending archive item that had a tool result but no user-facing summary.
- Then process the newly attached image if present.
- In the final reply, mention both: what was already finished and what was newly completed.

## Cluster discipline

Prefer these cluster-level buckets unless a new image clearly requires another:

- Ambient companion / AI around human context
- Luminous boundary / protected container / privacy-safe void
- Soft loop / orbital feedback / emergence states
- Product/component grammar: processing, progress, metrics, controls
- Human-scale navigation and biomorphic content systems
- Editorial/package/archive surface systems
- Physical brand system and modular labels
- Motion/mobility/audio presence
- Human perception / signal trace / identity campaign
- Playful reaction microcopy patterns

## Cautions to preserve

- Health/personal-state images need privacy, consent, agency, evidence/overclaim, hide/delete/edit controls.
- Human profile/sensing images need explicit non-surveillance framing.
- Driving/mobility images need glanceability and distraction restraint.
- Third-party brand references need originality guardrails.
- Common AI aesthetics—glow, gradient orbs, chrome/glass—need restraint rules around saturation, blur, density, motion, and usage frequency.
