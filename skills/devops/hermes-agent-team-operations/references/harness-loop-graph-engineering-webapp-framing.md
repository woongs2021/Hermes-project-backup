# Harness / Loop / Graph Engineering Webapp Framing

Use this reference when Chris asks to explain, plan, or implement the Hermes/OBD webapp as a product system rather than a generic dashboard.

## Core framing

Chris's Hermes/OBD webapp should be explained as three layers:

1. **Harness / 하네스** — the safe execution base that connects the agent team, tools, schedules, messaging, files, routing, permissions, and public/private boundaries.
2. **Loop / 루프** — the recurring daily/weekly rhythm where specialists accumulate research, design interpretation, growth questions, visual artifacts, webapp structure candidates, and validation.
3. **Graph Engineering / 그래프 엔지니어링** — the step that converts loop outputs from loose Markdown/JSONL logs into explicit knowledge/judgment relationships.

A compact Chris-facing product sentence:

> Hermes/OBD 웹앱은 에이전트 팀을 실행하는 Harness, 반복적으로 지식을 쌓는 Loop, 그 결과를 관계형 지식 구조로 바꾸는 Graph Engineering을 보여주는 Chris의 사고 운영 웹앱이다.

## Why Hermes

Do not claim Hermes is the only way. The correct positioning:

- The loop could be implemented without Hermes using LangGraph, CrewAI, OpenAI Agents SDK, cron, Slack/Telegram APIs, a storage layer, and governance logic.
- Hermes is chosen because it already provides the **Harness**: profiles, cron jobs, gateway/messaging, memory, skills, file workflow, session search, and tool execution.
- This lets the project focus on Loop design and Graph Engineering instead of rebuilding orchestration infrastructure from scratch.

Project-intro copy candidate:

> Hermes는 이 프로젝트의 하네스다. 에이전트 팀, 도구, 스케줄, 메시징, 기억, 작업 로그를 하나로 묶어주기 때문에 Chris는 별도 인프라를 처음부터 만들지 않고 Loop와 Graph Engineering 설계에 집중할 수 있다.

## Graph MVP guidance

Start with a file-based graph MVP before introducing a graph database:

- `data/graph/schema.md` — node/edge definitions, field contracts, privacy rules.
- `data/graph/nodes.jsonl` — graph node candidates.
- `data/graph/edges.jsonl` — graph relation candidates.

Evaluate KuzuDB or Neo4j only after the file-based schema proves useful.

Initial node types:

- `Agent`
- `ResearchItem`
- `Theme`
- `Insight`
- `GrowthQuestion`
- `Artifact`
- `Decision`
- `RiskReview`

Initial relations:

- `FOUND`
- `SUPPORTS`
- `INTERPRETED_AS`
- `TRANSLATED_INTO`
- `VALIDATED_BY`
- `HAS_RISK`
- `APPROVED_BY`
- `FEEDS`
- `BELONGS_TO_THEME`

Useful breadcrumb pattern:

```text
ResearchItem → Insight → GrowthQuestion → RiskReview → Decision → Artifact
```

## Webapp planning implications

When updating Faker or August webapp plans:

- Add a project-intro section such as `왜 Hermes인가` / `Hermes as Harness`.
- Include a `/graph` route or home section that explains Harness / Loop / Graph Engineering.
- Prefer cards + relation breadcrumbs over a complex force-directed network for the first UI.
- Keep Graph Engineering implementation planning-only until Chris approves coding scope.
- Keep public/private/admin visibility explicit. Public pages show polished narratives; private/admin areas may show validation status, risk flags, and source refs.

## Safety boundaries

- Never expose raw Telegram/Slack logs, tokens, credentials, private IDs, or raw prompts in public UI.
- Do not treat pending Go Youn-jung visuals as canonical until Chris final-save or the finalizer promotes them.
- Do not overstate graph maturity: call it a file-based Graph MVP unless a real graph DB has been implemented and verified.
