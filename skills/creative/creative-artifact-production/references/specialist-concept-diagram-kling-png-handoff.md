# Specialist concept diagram → Kling-assisted PNG handoff

Use this when Chris asks Karina to have Go Youn-jung turn another specialist's concept diagram, SVG, Mermaid, or strategy map into a PNG using Kling.

## Pattern

1. Locate the source specialist artifact first:
   - Prefer explicit paths from the specialist work log or session output.
   - Typical Son paths may include `/opt/data/profiles/son/artifacts/*.svg` and matching Mermaid/Markdown files.
2. Route the visual production to Go Youn-jung rather than having Karina silently own the design lane.
3. Preserve text accuracy:
   - Do **not** ask Kling to render Korean diagram text as the final source of truth.
   - Use Kling for a text-free premium background, motif, material mood, or visual atmosphere.
   - Render the actual Korean labels, hierarchy, arrows, cards, and diagram structure locally with a reliable font such as Pretendard/Noto Sans CJK.
4. Use a Chris-appropriate visual direction:
   - Premium soft editorial / woongdesignv2 restraint.
   - Off-white/mint/ink/orange restrained palette.
   - Clear hierarchy, generous spacing, calm Samsung/One UI-compatible polish.
   - Avoid fake UI text, pseudo lettering, neon/glassmorphism, and AI-startup clichés.
5. Store a complete requested-concept package under a stable folder, for example:
   - `/opt/data/agent-team-work-log/visuals/requested-concepts/YYYY-MM-DD-topic/`
   - Final PNG, source-note.md, raw Kling result/background if used, and telegram-send-status.json if delivered.
6. For specialist voice delivery, send from Go Youn-jung's Telegram bot when possible and save real message IDs. Never print or log credentials.
7. Verify before reporting to Chris:
   - PNG exists and is non-empty.
   - The image opens in vision review.
   - Korean text is legible and not hallucinated/fake model text.
   - Delivery status contains real message IDs if a direct DM was attempted.

## Reporting to Chris

Karina's final synthesis should be short and warm:

- Say that Go Youn-jung produced the PNG and delivered it.
- Mention that Kling was used for background/mood only if text accuracy required local overlay.
- State any relevant format caveat, e.g. “원본 비율 그대로가 아니라 16:9 공유용으로 재배치했어.”
- Do not expose prompts, raw URLs, bot tokens, or internal logs unless Chris asks for implementation details.
