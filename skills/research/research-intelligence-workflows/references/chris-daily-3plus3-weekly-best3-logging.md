# Chris daily 3+3 → Friday Muyeol best-3 paper loop

Use this reference for Chris Park's recurring paper/research briefing loop when maintaining cron prompts, logs, or future dashboard data sources.

## Current operating model

- Daily discovery remains **3+3**:
  - Yuna: 3 AI / AI×design / LLM / agent / human-centered AI candidates per day.
  - Go Youn-jung: 3 UX / HCI / design-management / branding / design-education candidates per day.
- Friday weekly report is **not** 3+3. It shows exactly **3 final selected items total** across both lanes.
- Karina compiles and de-duplicates the weekly candidate pool for comparison.
- Muyeol owns final weekly selection and validation: choose exactly 3, verify source/link plausibility, de-duplicate, reduce overclaims, mark GO/HOLD/WATCH, and explain why those 3 were selected.
- Karina delivers Muyeol's finalized report to Telegram + Slack, preserving Muyeol's structure/wording unless a safety or format issue requires a light edit.

## Local logging contract

All daily candidates should be locally reusable for later Faker dashboard/search work.

- Lane weekly Markdown logs:
  - `/opt/data/agent-team-work-log/paper-candidates/yuna-YYYY-WW.md`
  - `/opt/data/agent-team-work-log/paper-candidates/goyounjung-YYYY-WW.md`
- Searchable all-candidate JSONL index:
  - `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl`
- Weekly Muyeol-finalized selected-paper log:
  - `/opt/data/agent-team-work-log/paper-candidates/weekly-selected-papers.md`
- Data contract/readme:
  - `/opt/data/agent-team-work-log/paper-candidates/README.md`

## JSONL fields

Append one compact JSON object per daily selected candidate, preserving direct source links/IDs:

- `date_kst`
- `iso_week`
- `lane`: `yuna` or `goyounjung`
- `title`
- `url_or_id`
- `source_venue`
- `publication_date`
- `core_claim`
- `chris_relevance`
- `korean_source_status`
- `source_access`: full / abstract / metadata / snippet / paywalled / unclear
- `initial_score_5`
- `duplicate_key`
- `duplicate_repeat_signal`
- `owner`

## Cron prompt maintenance checklist

When Chris changes the paper-loop format, update all relevant surfaces together:

1. Daily Yuna prompt: keep exactly 3 visible picks and log to weekly MD + JSONL.
2. Daily Go Youn-jung prompt: keep exactly 3 visible picks and log to weekly MD + JSONL.
3. Friday Karina prep: compile candidate pool only; do not make final best-3 decision.
4. Friday Muyeol validation/report: choose exactly final 3 total and write the report.
5. Friday Karina delivery: preserve Muyeol-selected final 3; do not expand to 6.
6. Son/weekend/monthly/dashboard follow-up prompts if they reference the weekly report shape.
7. Durable skill guidance and concise user/memory preference if the change is stable.

## Pitfalls

- Do not confuse daily 3+3 with Friday report shape. Daily stays 3+3; Friday final is best 3 total.
- Do not let Karina become the final selector when Chris assigned final weekly selection to Muyeol.
- Do not lose non-winning candidates. They are useful for dashboard search, trend clustering, and later ontology-designer growth analysis.
- Do not store raw chat logs, secrets, private IDs, or credentials in the research logs.
- For past data before the JSONL contract existed, note that it may require a separate backfill from weekly MD files or cron outputs.