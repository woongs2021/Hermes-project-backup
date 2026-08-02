# Faker Dashboard Planning with Son Question Source Lineage

Use this reference when Chris asks Karina to preserve future Faker dashboard plans around the 3+3 research loop, OBD growth loop, Son daily questions, and weekly/monthly reports.

## Context

Chris wants Faker to eventually build a dashboard, but implementation must not start until Chris explicitly reopens the project (planned after July/into August). Until then, preserve the plan, data paths, phase history, and design direction.

## Core planning artifact

Create or update a planning Markdown under Faker's work-log area, e.g.

`/opt/data/agent-team-work-log/faker/dashboard-plan-3plus3-obd-llm-wiki.md`

It should include:

- status: planned-not-started
- owner: Faker
- Karina handoff role
- data sources
- LLM-maintained Markdown wiki direction
- dashboard IA candidates
- phased development plan
- explicit no-implementation-before-Chris-approval rule

## Source-lineage data for Son questions

Preserve Son's daily question origin as machine-readable data so Faker can visualize it later.

Recommended paths:

- schema: `/opt/data/agent-team-work-log/growth-question-sources/SCHEMA.md`
- JSONL source of truth: `/opt/data/agent-team-work-log/growth-question-sources/son-question-source-log.jsonl`

Recommended fields per question:

```json
{
  "date_kst": "YYYY-MM-DD",
  "week_kst": "YYYY-Www",
  "agent": "son",
  "delivery_label": "오늘의 성장 질문",
  "question_index": 1,
  "question_text": "...",
  "source_tags": ["Chris 답변 기반", "OBD 프레임 기반"],
  "source_reason": "why this question was asked",
  "upstream_refs": [
    {"type": "karina_framing", "path": "...", "note": "..."},
    {"type": "muyeol_guardrail", "path": "...", "note": "..."}
  ],
  "related_research_ids": ["DOI/arXiv/URL/title if explicitly used"],
  "obd_theme": "market/value-exchange/brand-asset/org-decision/etc.",
  "status": "sent"
}
```

Rules:

- Preserve paper URLs/DOIs/arXiv IDs when a question is directly research-derived.
- Use empty lists for unknown research IDs; do not invent identifiers.
- Do not store raw private chat dumps, tokens, credentials, or private IDs.
- Keep entries concise and dashboard-friendly.

## Phase history logging

Dashboard development phases should leave their own history so Chris can later see how the system evolved.

Recommended paths:

- schema: `/opt/data/agent-team-work-log/faker/dashboard-history/SCHEMA.md`
- JSONL history: `/opt/data/agent-team-work-log/faker/dashboard-history/phase-history.jsonl`
- human logs: `/opt/data/agent-team-work-log/faker/dashboard-history/phase-logs/YYYY-MM-DD.md`

Recommended phase entry fields:

```json
{
  "date_kst": "YYYY-MM-DD",
  "phase": "Phase 1 — 데이터 인벤토리",
  "status": "planned|started|in_progress|blocked|completed|revised",
  "decision": "core decision",
  "artifact_paths": ["/path/to/artifact"],
  "data_sources_checked": ["/path/to/source"],
  "design_notes": ["woongdesignv2 notes"],
  "risks_or_blockers": ["risk or blocker"],
  "next_action": "next action",
  "handoff_to_karina": "short summary"
}
```

Append when a phase starts, changes status, is blocked, completes, or is materially revised. Record why the direction changed, not just what changed.

## Design direction

Use **woongdesignv2** as the visual reference for dashboard design.

Direction:

- restrained but warm
- editorial research system / research OS
- calm hierarchy
- refined typography
- generous spacing
- quiet semantic color
- card-based without generic SaaS/startup-template aesthetics
- avoid obvious AI-dashboard/neon data-viz tropes
- “AI티가 안 나는” quality bar

If Go Youn-jung reviews the dashboard, ask for critique against woongdesignv2: typography, spacing, semantic color, density, card rhythm, and graph legibility.

## Dashboard view candidates

- Growth Timeline: research → question → answer → synthesis
- Question Source Map: source-tag distribution and trends
- OBD Theme Graph: market, value exchange, brand asset, organizational decision quality, AI UX judgment
- Weekly Best-3 Panel: Muyeol final best-3 + Karina synthesis
- Paper / Question / Answer Link View: lineage from source research to Chris answer and weekly/monthly insight

## Pitfalls

- Do not let planning drift into implementation before Chris explicitly starts the project.
- Do not expose raw private chat content on a dashboard; summarize and link internally where appropriate.
- Do not lose direct source IDs/URLs; they are critical for future dashboard drill-downs.
- Do not treat Son's displayed question tag as enough — keep the machine-readable lineage log too.
