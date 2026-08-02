# Faker 대시보드 단계 이력 스키마

루트: `/opt/data/agent-team-work-log/faker/dashboard-history/`

목적: 미래 3+3/OBD LLM wiki와 대시보드의 개발 이력을 보존해 Chris, Karina, Faker가 나중에 시스템이 어떻게 진화했는지 확인할 수 있게 한다.

## 파일

- `phase-history.jsonl` — append-only machine-readable 단계 이력.
- `phase-logs/YYYY-MM-DD.md` — 실질적인 대시보드 작업이 있었던 날의 human-readable 일일 단계 로그.

## JSONL 필드

```json
{
  "date_kst": "YYYY-MM-DD",
  "phase": "Phase 1 — 데이터 인벤토리",
  "status": "planned|started|in_progress|blocked|completed|revised",
  "decision": "core decision made that day",
  "artifact_paths": ["/path/to/artifact"],
  "data_sources_checked": ["/path/to/source"],
  "design_notes": ["woongdesignv2 application notes"],
  "risks_or_blockers": ["risk or blocker"],
  "next_action": "next action",
  "handoff_to_karina": "short handoff summary"
}
```

## 규칙

- 단계가 시작되거나, 상태가 바뀌거나, 막히거나, 완료되거나, 의미 있게 수정될 때마다 항목 1개를 append한다.
- 무엇이 바뀌었는지만이 아니라 왜 방향이 바뀌었는지도 기록한다.
- 비공개 채팅 로그는 요약만 남기고 원문을 붙여 넣지 않는다.
- 원시 토큰, OAuth/API key, private IDs, 자격 증명을 절대 저장하지 않는다.
- 대시보드 관련 design notes의 시각 디자인 기준으로 `woongdesignv2`를 사용한다.
