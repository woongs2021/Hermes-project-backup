# Chris Archive intake lessons — 2026-09 initial batch

Use this as a compact reference for future Chris Archive intake sessions.

## User-facing behavior learned

- Chris may upload many images in rapid succession with `추가해줘`.
- For this class of task, avoid step-by-step progress chatter in Telegram. Work quietly and send one concise completion after verification.
- If a previous archive step was interrupted, first finish/verify the pending archive write, then process the newly attached image in the same clean completion message.
- Chris values confidence that the image is actually saved: include asset path, entry path, and note that `index.md` / `DESIGN_SYSTEM_DRAFT.md` were updated.

## Efficient execution pattern

Prefer a single combined script pass per image:

1. Compute KST date.
2. Copy source from `/opt/data/image_cache/...` to `/opt/data/chris-archive/images/YYYY/MM/YYYY-MM-DD_<slug>_<sha12>.jpg`.
3. Write `entries/YYYY/YYYY-MM-DD_<slug>.md` with full first-pass analysis.
4. Append to `/opt/data/chris-archive/index.md` idempotently.
5. Patch `/opt/data/chris-archive/DESIGN_SYSTEM_DRAFT.md` with tentative candidate clusters only.
6. Verify both asset and entry exist and have non-zero size.
7. Reply concisely with saved paths and 3–6 strongest design-DNA signals.

## Archive cluster vocabulary observed

Treat these as candidate clusters, not final rules:

- Protected luminous container / protected inner void.
- Biomorphic protected core / living signal bloom.
- Calm luminous boundary / edge as signal / empty readiness.
- Interface as cushion / pressure-absorbing AI layer.
- Calm AI state component / progress without pressure.
- Soft personal metrics layer / body-adjacent data.
- Human-scale circular navigation / thumb-safe interaction field.
- Story-based product OS / technical story card.
- Physical brand system / everyday toolkit.
- Editorial discipline / quiet spatial intelligence.
- Flat signal pattern / playful reaction token field.
- Mobility ambient media UI / violet displacement field.
- Human perception identity / human signal trace.

## Guardrails reinforced

- Never claim final design-system rules from one image. Update `DESIGN_SYSTEM_DRAFT.md` as candidate language only.
- If third-party brand text/logos/product UI appear, mark brand-safety in the entry and extract only structure, composition, palette, material, and metaphor.
- For personal-state, health, biometric, or emotion-related UI, explicitly flag privacy, consent, agency, explainability, correction, hide/delete, and overclaim restraints.
- For driving/cockpit contexts, include glanceability, distraction, motion speed, brightness, and information-density review prompts.
- For repeated/similar visuals, still archive when Chris says `추가해줘`, but mark as related/supporting evidence rather than pretending it creates a new cluster.
