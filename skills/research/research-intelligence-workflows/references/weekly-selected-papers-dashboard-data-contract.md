# Weekly Selected Papers Dashboard Data Contract

Session-derived note for Chris Park's recurring 3+3 paper-growth loop and future Faker dashboard.

## Purpose

The weekly selected 3+3 paper log is not only an archive. It is a growth-record dataset that should support monthly synthesis and later dashboard visualizations: weekly timelines, paper clusters, repeated growth themes, and ontology-designer growth graphs.

Primary file:

- `/opt/data/agent-team-work-log/paper-candidates/weekly-selected-papers.md`

## Required weekly entry fields

Each Friday-selected set should append one compact entry with:

- ISO week and selection date.
- Selection rationale: why the six items form one coherent weekly learning package.
- Exactly 3 Yuna-lane AI / AI×design / LLM / agent / human-centered AI items.
- Exactly 3 Go Youn-jung-lane UX / HCI / branding / design-management / design-education items.
- For each item:
  - Title.
  - Source/venue/date when available.
  - Direct URL whenever available.
  - DOI / arXiv / ACM / KCI / DBpia / KoreaScience / other stable ID when available.
  - Chris growth relevance.
  - Muyeol status: GO / HOLD / WATCH.
  - Key caution or source-access limitation.
- Korean-source coverage note.
- Visible de-duplication note.
- Repeat weighting note when applicable.
- 3–6 monthly synthesis hooks.

## Dashboard-oriented rules

- Preserve direct URLs, not just IDs, so dashboard paper cards can open the original source immediately.
- Keep stable IDs too; URLs can change, but IDs help deduplicate and recover sources.
- Use consistent labels for recurring themes so future graphs can cluster them. Examples:
  - warm AI metrics
  - emotional safety
  - companion/embodiment boundaries
  - human-in-the-loop research
  - failure-state brand trust
  - design-system leadership
  - productive friction
  - design education
  - ontology-designer growth
- Do not expose raw logs, private IDs, tokens, or confidential internal context.
- Do not store every daily candidate in the weekly selected log; store the final weekly selected set only.

## Monthly synthesis use

Monthly reports should read `weekly-selected-papers.md` first, then use daily candidate files and cron outputs only as supporting evidence. The monthly report should cluster weekly selections into growth themes rather than relisting every paper.

## Future Faker dashboard ideas

Potential views:

- Weekly 3+3 paper timeline.
- Paper-card list with direct source links.
- Theme accumulation graph across weeks.
- Paper cluster map by theme and source type.
- Muyeol validation status distribution.
- Korean vs international source coverage.
- Chris ontology-designer growth curve based on weekly synthesis hooks and Son Q&A evidence.
