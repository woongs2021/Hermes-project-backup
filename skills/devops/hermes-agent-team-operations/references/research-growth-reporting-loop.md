# Research growth reporting loop for Chris

Use this when Chris wants recurring research to become a personal growth system rather than a simple digest.

## Ownership model

- **Yuna**: daily AI / AI×UX / LLM / agent / human-centered AI research picks.
- **Go Youn-jung**: daily UX / HCI / brand / design-management / design-education research picks.
- **Karina**: orchestrator and final synthesizer. Frames daily growth-question angles, produces Friday and monthly synthesis, and keeps Telegram + Slack summaries coherent.
- **Muyeol**: validation/risk. Reviews overclaims, sensitive themes, source-access limits, duplicate/repeat handling, and whether questions are psychologically safe.
- **Son**: owns growth questions/dialogue with Chris. Son sends the actual daily questions and keeps the Q&A in the Son↔Chris Telegram DM thread.
- **Faker**: future implementation/prototyping owner when reports become a UI/website artifact; do not start implementation until Chris asks after the monthly report.

## Daily question pipeline

1. Yuna and Go Youn-jung run daily research as usual.
2. Karina runs a local-only framing job after the daily research: choose 1-2 growth angles and draft 1-2 candidate questions.
3. Muyeol runs a local-only review job: GO / ADJUST / HOLD, with guardrails against overclaiming, emotional intrusion, sensitive topics, and forced One UI linkage.
4. Son sends the final “오늘의 성장 질문” to Chris by Telegram DM.
5. Keep each Son question answerable in 1-3 minutes. One question is enough; two only when genuinely useful.

## Weekly synthesis

Karina's Friday weekly report should combine:

- Karina weekly 3+3 shortlist.
- Muyeol paper validation memo.
- Son profile Telegram Q&A for the week.

When collecting Q&A, search Son's profile sessions for “오늘의 성장 질문” and Chris's replies. Treat Son's session as the source of truth; Karina should not insert herself into the daily Q&A. If Chris answered sparsely, say so and avoid overclaiming growth.

Weekly report sections should include:

- why this 3+3 set was selected as a coherent learning package;
- the six validated picks;
- Chris answer-based growth signals;
- three sentences of growth language for Chris;
- Muyeol cautions;
- next growth-dialogue seeds for Son.

## Monthly synthesis

Schedule monthly reports for the **last day of each month**, regardless of weekday. Hermes cron does not support `L` in the day-of-month field, so use a daily cron plus a script guard:

```bash
if [[ "$(TZ=Asia/Seoul date -d 'tomorrow' +%d)" != "01" ]]; then
  exit 0
fi
# generate the report and print it to stdout
```

Use `no_agent=True` with a script under `~/.hermes/scripts/` when you want silence on non-last-days. Empty stdout means no delivery; non-empty stdout is delivered to Telegram/Slack.

Monthly reports should summarize:

- how daily research and Friday 3+3 reports changed Chris's thinking;
- how Son's daily Q&A shows concept/language growth;
- how Chris is developing as an ontology designer;
- the strongest paper/trend clusters;
- Muyeol's caution notes;
- next-month Son dialogue directions;
- Karina's continue/stop/adjust recommendation.

## Future UI artifact

If Chris wants a website for weekly/monthly summaries:

- Log the future plan for Faker, but do not implement until Chris explicitly reopens it.
- Revisit after the monthly report, when real report formats and data sources exist.
- Likely data sources: cron outputs, `agent-team-work-log/paper-candidates`, weekly Karina reports, monthly reports, and Son Q&A summaries.
- First planning decisions: scope, data source, and first screen.
