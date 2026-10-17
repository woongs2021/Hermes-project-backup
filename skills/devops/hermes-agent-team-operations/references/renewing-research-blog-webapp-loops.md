# Renewing Chris's Research + Blog + Webapp Loops

Use this reference when Chris asks to adjust existing scheduled loops while keeping paused jobs stopped.

## Core pattern

1. List current cron jobs first; never guess job IDs.
2. Keep already paused jobs paused unless Chris explicitly asks to resume them.
3. Identify active jobs that will duplicate the new request and pause only those predecessor jobs.
4. Create new specialist-owned jobs with explicit profile, schedule, delivery target, toolsets, and self-contained prompts.
5. Verify with a fresh cron list after changes.
6. Save concise durable memory only for stable operating preferences, not transient job IDs.
7. Write a Karina daily work-log note for multi-agent loop changes.

## Current loop shape captured from 2026-09-07

### Daily 3+3 research

- Yuna daily: exactly 3 AI/AX/AI×design items.
- Go Youn-jung daily: exactly 3 UX/design/brand/design-management items.
- Each 3-item set contains:
  - one global/foreign research item
  - one Korean research item
  - one package-design-related item
- Deliver directly from specialist profile to Slack + Chris Telegram DM.
- Append graph/dashboard-ready items to `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl`.

### Friday validation and webapp update

- Muyeol reviews the weekly pool and selects exactly one weekly 1-pick total.
- Faker updates the webapp from Muyeol's 1-pick, creates a feature branch, pushes it, merges to main, waits for GitHub Pages, and live-smoke-checks the result when Chris asked for continued webapp updates.

### Son blog loop

- Replace Son's OBD question prompt with Tue/Thu blog drafts when Chris asks for blog-style output.
- Draft should be under 2000 Korean characters and grounded in Chris's actual Hermes/OBD/team data.
- Required opening: `안녕하세요. AX디자이너 Chris입니다.`
- Required closing:

```text
감사합니다. 좋은 하루되세요!
Chris 드림
```

- Topic mix can combine:
  - Chris's Hermes team-building story
  - Hermes AX market research
  - Hermes AX paper research
  - changing role of designers
- Friday Faker job can create/update a lightweight webapp tab with the week's two drafts, but should not fabricate a missing draft.

## Pitfalls

- Do not simply resume older paused 1+1, best-2, or Wed/Fri AI/AX SNS loops when Chris says “재개”; read whether he asked for a new shape.
- Do not leave predecessor active jobs running if their output overlaps the new loop; pause those active duplicates to prevent noisy double delivery.
- Do not put private file paths, chat IDs, raw user answers, tokens, or raw logs into webapp-visible content.
- Treat branch push → main merge → deployment as a side-effect explicitly allowed only when Chris requested webapp update/deploy automation.
