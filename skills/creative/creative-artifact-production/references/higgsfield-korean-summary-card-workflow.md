# Higgsfield Korean Summary Card Workflow

Use this when Chris asks for a Korean one-card summary, infographic, or square visual generated in Go Youn-jung/Higgsfield style where the exact Korean wording must be readable.

## Why this pattern

Image models can produce strong visual metaphors, but Korean text rendered directly by the model is unreliable. For exact Korean typography, split the job:

1. Generate a **text-free** visual background/metaphor in Higgsfield.
2. Overlay the final Korean typography locally at the requested pixel size.
3. Verify dimensions and legibility before delivery.

## Recommended steps

1. **Extract the message first.** Reduce the source material into a short hierarchy: title, subtitle, 3 key blocks, and one conclusion line.
2. **Prompt Higgsfield for background only.** Include explicit constraints: `no text`, `no letters`, `no pseudo text`, `no numbers`, `no logos`, and enough negative prompts to avoid fake UI/pseudo-type.
3. **Leave composition space.** Ask for a clean off-white/paper panel or generous negative space where local typography will be placed.
4. **Use local composition.** Render 1080×1080 or the requested size with a real Korean-capable font when available. Keep headings, body, and conclusion visually separated.
5. **Verify.** Check file dimensions and visually inspect text readability/cropping. If typography is crowded, shorten text before delivery rather than shrinking everything.
6. **Delivery identity.** If Chris asks for Go Youn-jung style/DM, send from Go Youn-jung’s Telegram bot/profile when configured; otherwise label the sender identity clearly.

## Content pattern that worked

For a “왜 Hermes인가” card:

- Title: `왜 Hermes여야 하는가`
- Subtitle: `유일해서가 아니라, 이미 실행 하네스이기 때문에`
- Blocks: `Harness`, `Loop`, `Graph Engineering`
- Conclusion: Chris can focus on judgment/productization instead of infrastructure assembly.

## Pitfalls

- Do not ask Higgsfield/Imagen/GPT Image to render Korean paragraphs directly.
- Do not promote a one-off DM card into the webapp/gallery unless Chris explicitly asks; keep ad-hoc explanatory cards separate from final visual feed.
- Do not include exact prompts in Chris-facing delivery unless he asks; save them locally for traceability when relevant.
