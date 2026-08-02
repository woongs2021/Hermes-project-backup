# Karina-led Slack team orchestration session

Session pattern captured from configuring a Hermes multi-profile team for Chris Park.

## Team shape

- One main orchestrator profile acts as the single front door, coordination lead, and final synthesizer.
- Specialist profiles remain independent Slack/Telegram gateway processes with their own profile homes, SOUL.md files, and tokens.
- Shared Slack channel usage should be mention-driven (`SLACK_REQUIRE_MENTION=true`) to avoid every specialist responding to every message.
- Specialist SOUL.md files should explicitly say they are managed by the main orchestrator and should provide handoff notes for final synthesis.

## Recommended role lanes

- Research specialist: evidence, papers, benchmarks, market signals, AI × design/UX/HCI implications.
- PM specialist: priorities, sequencing, roadmap, decision memo, acceptance criteria.
- Technical specialist: implementation, prototyping, debugging, automation, verification evidence.
- Validation specialist: fact-checking, QA, risk, security, privacy, go/no-go review.

## SOUL.md operating rules to add

For the orchestrator:
- Interpret Chris's request and decide which specialists are needed.
- Use Slack for visible teamwork and Kanban for substantial multi-step work.
- Give each specialist context, owner, acceptance criteria, expected output, and handoff target.
- Synthesize outputs into one calm, Chris-facing recommendation.

For specialists:
- Stay inside your lane unless explicitly asked otherwise.
- If Chris mentions you directly, answer directly but frame output so the orchestrator can synthesize it.
- Avoid duplicating another specialist's role.
- Report concise findings, evidence, blockers, next actions, and handoff notes.

## Per-agent Markdown work logs

For date-bound learning, use Markdown work logs rather than memory:

- Root used in this session: `/opt/data/agent-team-work-log/`.
- Include a root `SCHEMA.md` and per-agent folders: `<agent>/daily/`, `<agent>/topics/`, `<agent>/index.md`.
- Create daily notes only on days where that agent performed substantive work.
- Do not create files for no-work days, greetings, `/start`, platform checks, or routine connection tests.
- Do not mirror raw logs or write secrets/tokens/private IDs.
- Recommended daily cron jobs run locally near end-of-day KST, one per profile, using `session_search` and `file` tools, with `deliver=local`.

## Verification pattern

After SOUL.md or env changes:

1. Restart affected gateways so cached sessions pick up new defaults.
2. Verify `hermes gateway list` shows all expected profiles running.
3. Verify each latest gateway log startup block has:
   - `✓ telegram connected` when Telegram configured
   - `Socket Mode connected` and `✓ slack connected` when Slack configured
   - `Gateway running with 2 platform(s)` when both Telegram and Slack are configured
4. If a Slack Socket Mode process logs `transport disconnected` followed by repeated `Connector is closed` / `Session is closed`, restart only that affected profile gateway and re-check its latest startup block.

## Public documentation / anonymization

When asked to document the architecture publicly or semi-publicly, avoid exposing real profile/persona names. Use anonymized labels such as Agent A/B/C/D/E while preserving roles and flow.
