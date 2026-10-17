# Paper loop 2+2 → Friday 1+1 / best-2 + dashboard handoff

## Trigger
Use this reference when Chris changes the recurring paper/research briefing count, Friday validation count, or asks for paper outputs to feed the Hermes Project Webapp dashboard.

## Current operating rule
- Daily paper discovery is **2+2**:
  - Yuna: exactly 2 AI / AI×design / LLM / agent / human-centered AI paper or research items.
  - Go Youn-jung: exactly 2 UX / HCI / design management / branding / interaction / design education paper or research items.
- Friday Muyeol validation is **1+1 / best-2**:
  - exactly 1 final Yuna-lane item.
  - exactly 1 final Go Youn-jung-lane item.
  - Do not expand to 3, 4, or 6 unless Chris explicitly restores that format.
- Karina delivers the final Friday overall report using Muyeol’s best-2 selection as authoritative.

## Surfaces to patch together
When this format changes, update all relevant prompts/surfaces in the same pass:
1. Yuna daily AI-paper cron job name + prompt.
2. Go Youn-jung daily UX/design-paper cron job name + prompt.
3. Muyeol Friday candidate-pool prep prompt.
4. Muyeol Friday final validation/report prompt.
5. Karina Friday final overall report prompt.
6. Downstream paused/active Son or Muyeol weekly-summary prompts if they mention selected paper count.
7. Faker daily coding prompt and Saturday approval-gate prompt if dashboard/webapp output shape changes.
8. `hermes-agent-team-operations` skill guidance and Karina durable memory when the preference is durable.
9. Karina daily team work log if the change affects team continuity.

## Verification pattern
After patching, search the affected cron prompts and the skill for stale count phrases such as:
- `3+3`
- `best-3`
- `exactly 3`
- `final best 3`
- `선정 논문 3개`

A valid update should leave no stale phrases in active/potentially resumable paper-report surfaces, except when explicitly framed as historical context and not an instruction. Prefer removing even historical literals if they could confuse future cron runs.

## Faker/webapp handoff requirement
For the Hermes Project Webapp, paper outputs should become a searchable board/dashboard tab rather than a static report page.

Recommended tab shape:
- Name: `Paper Research Board` or a similarly clear label.
- Board lanes/cards:
  - `Yuna AI`
  - `Go Youn-jung UX/design`
  - `Friday final picks`
- Card fields:
  - title
  - lane
  - source / venue / date
  - DOI / URL / stable ID
  - tags
  - OBD / business / design relevance
  - Muyeol validation/risk note
  - week/date
  - status
- Search/filter over:
  - title
  - source
  - tags
  - lane
  - week/date
  - relevance / validation notes

## Design and safety constraints
- UI direction: calm premium SaaS / bento admin dashboard using woongdesignv2 restraint.
- Avoid generic AI-startup aesthetics, neon, glassmorphism, and fake 3D.
- Use only public-safe curated exports. Do not include raw sessions, raw DMs, credentials, gateway logs, private IDs, or pending/private prompts.
- Daily Faker work remains local; push/merge/GitHub Pages deployment happens only through the Saturday approval gate after Chris approves.
