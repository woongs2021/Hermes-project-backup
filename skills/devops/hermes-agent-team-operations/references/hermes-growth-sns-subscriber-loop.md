# Hermes Growth SNS Subscriber Loop

Use this reference when Chris asks Son/Karina to turn Chris's Hermes-building journey into recurring SNS/subscriber growth work and reusable product/OBD data.

## Goal

The Son daily marketing loop should not be generic social-media advice. Its explicit objective is:

- Translate Chris's real Hermes growth journey into public SNS narratives.
- Help those narratives earn followers/subscribers through trust, usefulness, and continuity.
- Accumulate structured signals that can later feed OBD growth, coding work, a dashboard, a wiki, or homepage/productization.

## Cron configuration pattern

For the active daily Son job:

- Profile: `son`
- Delivery: explicit Telegram DM/home target when possible; avoid assuming `origin` when the job should appear as Son.
- Schedule: daily 09:50 KST unless Chris changes it.
- Ownership: Son owns both growth-question framing and the SNS/subscriber-growth DM. Do **not** put Karina in the daily growth-framing path; Karina's personal scheduled loops should remain the original warm greeting/weather loops unless Chris explicitly changes that.
- Context: include Muyeol's local pre-flight guardrail and weekly governance review via `context_from` when available. Do not require a Karina framing job.
- Prompt must tell Son to write as Son in Korean 존댓말, frame the question himself, and return only the Chris-facing DM.

Recommended DM structure:

- Short warm opening.
- `🧭 오늘의 성장 질문` — one question about what to share from the Hermes journey.
- `📣 오늘의 SNS/구독 전환 팁` — one concrete hook/format/framing/distribution/CTA/retention tactic.
- `🧪 오늘의 작은 실험` — one 10–20 minute action.
- `🧩 OBD/제품화 메모` — how today's signal feeds OBD, coding, wiki, dashboard, homepage, or agent-team productization.

Guardrails:

- No generic startup cliché or vague AI hype.
- Tie advice to Chris's actual Hermes system: Karina as orchestrator, specialist agents, future One UI, warm AI UX, design leadership, OBD, and high-quality non-generic AI aesthetics.
- Keep it DM-sized and actionable.
- Use source tags only when they improve traceability, e.g. `[Hermes Growth]`, `[SNS]`, `[OBD]`, `[Future One UI]`, `[Design Leadership]`.

## Data accumulation pattern

Create a local root for compounding data:

`/opt/data/hermes-growth-sns-loop/`

Recommended structure:

- `SCHEMA.md` — purpose, rules, fields, and privacy guardrails.
- `daily/YYYY-MM-DD.md` — Son's daily message, growth objective, audience/channel assumption, story angle, subscriber hypothesis, small action, OBD/product/coding implications, source tags, follow-up questions.
- `events.jsonl` — append one compact JSON object per run with `date_kst`, `growth_question`, `sns_tip`, `experiment`, `obd_product_implication`, and `source_tags`.
- `experiments/YYYY-MM.md` — monthly experiment backlog/results and intended metric/signal.
- `insights.md` — reusable cross-day insights only; keep concise.

Privacy rules:

- Do not store raw tokens, private IDs, credentials, or raw chat logs.
- Store concise reusable learning, not every intermediate thought.

## Verification pattern

When updating this loop:

1. Update the active Son cron prompt, not just Karina memory.
2. Ensure delivery is Son-to-Chris DM, not Karina-origin unless Chris explicitly wants Karina delivery.
3. Ensure the prompt writes the accumulation files and returns only the DM.
4. If Chris asks for today's run, trigger the cron job once and then verify artifacts exist under `/opt/data/hermes-growth-sns-loop/` before saying it worked.
5. Update Karina's daily team work log for substantive loop changes.
6. Store the root path in durable memory only in compact form; detailed state belongs in the local loop files.
