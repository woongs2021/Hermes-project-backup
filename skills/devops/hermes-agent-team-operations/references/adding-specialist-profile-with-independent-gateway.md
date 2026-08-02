# Adding a specialist profile with independent Telegram/Slack gateway

Session-proven pattern from adding `goyounjung` as a UX research specialist beside `yuna`.

## When to use

Use this when Chris adds a new named specialist agent who should share a current agent's workload and later appear as an independent Telegram/Slack bot.

## Procedure

1. Define the split before creating files.
   - Example split: keep `yuna` on AI technology, LLMs, agent frameworks, AI papers, startups/investment, future scenarios; move UX research, interviews, competitive service analysis, design benchmarks, IA/journey, Persona/JTBD, and design insights to the new profile.

2. Create the profile with a routing description.
   - `hermes profile create <profile> --description "..."`
   - Prefer lowercase ASCII profile names, e.g. `goyounjung`.

3. Write the new profile's `SOUL.md`.
   - Include primary mission, core responsibilities, working style, deliverables, collaboration rules, Slack team-channel rules, and daily work-log protocol.
   - For Chris's named companion team: only Karina uses banmal; specialists use 존댓말.
   - State that Karina is the coordination lead and final synthesizer.

4. Update the existing peer profile's `SOUL.md`.
   - Narrow its responsibilities so the two agents do not duplicate each other.
   - Add an explicit collaboration rule naming when to hand off to the new specialist.

5. Update Karina/default `SOUL.md` routing.
   - Add the new profile to the specialist roster.
   - Update orchestration rules and Slack team-channel routing rules with clear task-lane boundaries.

6. Prepare independent messaging credentials.
   - Create `/opt/data/profiles/<profile>/.env` with blank token slots; do not copy real tokens from another profile.
   - Recommended keys:
     - `TELEGRAM_BOT_TOKEN=`
     - `TELEGRAM_ALLOWED_USERS=`
     - `SLACK_BOT_TOKEN=`
     - `SLACK_APP_TOKEN=`
     - `SLACK_ALLOWED_USERS=`
     - `SLACK_HOME_CHANNEL=`
     - `SLACK_REQUIRE_MENTION=true`
   - Set mode `0600`.
   - Never print raw token values while verifying; report only set/empty and lengths if needed.

7. Add work-log support.
   - Add the profile to `/opt/data/agent-team-work-log/SCHEMA.md` if the schema enumerates agents.
   - Create `/opt/data/agent-team-work-log/<profile>/daily/`.

8. Smoke test.
   - `hermes -p <profile> chat -q "한 문장으로 본인 역할을 한국어 존댓말로 소개해 주세요." -Q`
   - Verify the answer matches the intended lane and tone.

9. Start and verify gateway.
   - In normal service environments: `hermes -p <profile> gateway start`.
   - In Docker/container environments where service start is not applicable: run `hermes -p <profile> gateway run` as a tracked background process, then verify status/logs.
   - Verify with `hermes -p <profile> gateway status` and profile gateway log lines showing Telegram connected and Slack Socket Mode connected.

## Pitfalls

- Do not share Telegram/Slack tokens across profiles. Each independent bot needs its own bot/app credentials.
- Do not leave specialists with overlapping broad research mandates; split the task lanes in both agents' SOUL files and Karina's routing rules.
- Avoid printing or copying `.env` contents; use redacted checks only.
- If shell/background detection is confused by credential-like strings while inspecting `.env`, use a safer non-shell inspection path and only emit key presence/length, never values.
- Gateway `start` can be unavailable inside containers; this is not a failure of credentials. Use tracked `gateway run` and verify logs/status.
