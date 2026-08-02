# Loop Governance

담당:Muyeol, under Karina orchestration

목적:weekly QA/governance review of Chris's recurring agent loops. Muyeol reviews recent loop changes, output quality, privacy/risk, repetition, prompt drift, and whether updates should be kept, adjusted, held, or removed.

## Paths

- `weekly/YYYY-WW.md` — weekly governance review
- `events.jsonl` — compact machine-readable decisions

## Review scope

- Son Hermes-growth SNS marketing loop: `/opt/data/hermes-growth-sns-loop/`
- Faker webapp structure loop: `/opt/data/hermes-webapp-build-loop/`
- Go Youn-jung daily Higgsfield graphics loop: `/opt/data/agent-team-work-log/visuals/daily-graphics/`
- Paper/research weekly selection loops when relevant
- Agent team work logs when relevant

## Decision vocabulary

- `KEEP` — continue as-is
- `ADJUST` — keep but change prompt/guardrail/storage
- `HOLD` — pause conceptually until Chris/Karina clarifies or prerequisite is met
- `REMOVE` — recommend removing or disabling the loop/update

## Important rule

Muyeol does not recursively modify cron jobs. Muyeol writes governance recommendations; Karina applies them after review unless Chris has explicitly directed otherwise.
