# Direct specialist change sync: Son question transparency + Faker future wiki/dashboard

Use this reference when Chris says he told Son/Faker something directly and asks Karina to “내용 파악하고 저장해줘” or similar.

## Pattern

1. Treat the specialist profile session as the source of truth.
   - Search/read the specialist profile conversations or logs for the relevant day rather than relying only on Karina/default memory.
   - Summarize only the operational delta, not the full chat transcript.
2. Decide the persistence layer:
   - Durable user preference or operating rule → memory + SKILL.md.
   - Date-bound plan or future handoff → agent-team work log under Karina, and memory only if it prevents future steering.
   - Actual scheduled behavior change → patch the relevant profile cron/job prompt, not just memory.
3. Verify the changed surface where possible: e.g. JSON parses, prompt contains the new rule, next run remains scheduled.
4. Record Karina’s daily work log for multi-agent continuity.

## Session-proven deltas

### Son: daily growth-question transparency

Chris asked Son to explain where growth questions come from. Future Son “오늘의 성장 질문” prompts should include:

- Compact source tags, e.g. `[Chris 답변 기반]`, `[OBD 프레임 기반]`, `[PM/비즈니스 판단 기반]`, `[리서치/논문 기반]`, `[브랜드/디자인경영 기반]`.
- A short reason under each question.
- The same low-burden style: 1–2 questions, answerable in 1–3 minutes.

If Son’s daily growth-question cron exists, patch the actual Son profile cron prompt so future deliveries reflect the preference; do not stop at summarizing to Chris.

### Faker: future 3+3 / OBD LLM wiki and dashboard

Chris told Faker that after July / into August, Faker may own a future build:

1. 3+3 + OBD source data → LLM-maintained Markdown wiki, inspired by Karpathy’s llm-wiki gist.
2. Wiki/schema layer → website dashboard for weekly/monthly growth summaries and research flow.

Operational rule: do not start implementation until Chris explicitly asks. When work starts, split scope into raw-source preservation, wiki/update schema, and dashboard UI layers. Preserve direct paper/source URLs, DOIs, arXiv/OpenReview/venue IDs, and other stable source handles so the dashboard can open original sources.
