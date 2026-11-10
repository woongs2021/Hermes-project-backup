# Kling Character Asset Quality Gate

Use when generating profile-referenced illustrated or pixel character assets for a product UI.

## Before submitting paid work

1. Get explicit approval for the paid generation and clarify whether the target is a **production asset** or only art-direction exploration.
2. Run one subject as a style/frame pilot before charging a whole cast, unless the user explicitly approves a full-batch experiment.
3. Put non-negotiables in the prompt: `one character`, `full body head-to-shoes`, intended camera (for example `3/4 top-down`), plain single-color background, no extra people, no text/logo/UI/frame, and non-photoreal pixel illustration.
4. Use reference images only for broad public identity cues (hair silhouette, glasses, clothing color family); do not promise biometric likeness.

## Mandatory acceptance gate

Inspect a contact sheet before copying anything into product assets. Every candidate must pass:

- consistent camera/view and pixel-art rendering treatment across the cast;
- full body is visible and readable at intended UI scale;
- no photoreal/close-up output when the product needs a stylized sprite;
- no text, logo, signature, provider watermark, UI frame, or accidental extra figure;
- background is clean enough for the planned compositing method;
- public-safe reference use and no invented sensitive identity claims.

A single failed cast member makes the batch **candidate-only**. Do not publish a mixed-quality cast simply because several images worked.

## Watermarks and failed generations

- Never remove, mask, or crop out a provider watermark for production use.
- Keep rejected outputs outside public assets and do not stage or deploy them.
- Explain the failure concisely, show the quality reason, and get user approval before a new paid retry.
- If repeated outputs cannot meet camera consistency or watermark requirements, use the results only as private art-direction reference and create a clean original sprite system manually (or change to an approved provider/workflow).

## Product integration

Treat generated character art as a separate accepted-asset phase. Only after the quality gate passes should it be normalized, mapped to the UI, given an original-image fallback, and validated in desktop/mobile screenshots. Movement should be deterministic, avoid collisions, and stop or substantially reduce under `prefers-reduced-motion`.
