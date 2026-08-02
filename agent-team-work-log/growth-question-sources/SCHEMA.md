# 성장 질문 소스 로그 스키마

루트: `/opt/data/agent-team-work-log/growth-question-sources/`

목적: Son의 일일 “오늘의 성장 질문” 뒤에 있는 source flow를 기록해, Faker가 나중에 3+3 + OBD 성장 데이터 기반 LLM wiki/대시보드를 만들 수 있게 한다.

## 파일

- `son-question-source-log.jsonl` — 전달된 질문마다 JSON 객체 1개를 남기는 append-only machine-readable 로그.
- `daily/YYYY-MM-DD.md` — 필요할 때 작성하는 human-readable 일일 요약.

## JSONL 객체 필드

```json
{
  "date_kst": "YYYY-MM-DD",
  "week_kst": "YYYY-Www",
  "agent": "son",
  "delivery_label": "오늘의 성장 질문",
  "question_index": 1,
  "question_text": "...",
  "source_tags": ["Chris 답변 기반", "OBD 프레임 기반"],
  "source_reason": "왜 이 질문이 나왔는지 한 문장",
  "upstream_refs": [
    {"type": "karina_framing", "path": "/opt/data/cron/output/e29c81ee7ed3/...", "note": "..."},
    {"type": "muyeol_guardrail", "path": "/opt/data/cron/output/125e42f5b925/...", "note": "..."},
    {"type": "son_prior_reply", "session_title": "...", "note": "..."}
  ],
  "related_research_ids": ["DOI/arXiv/URL/title if explicitly used"],
  "obd_theme": "시장/가치교환/브랜드자산/조직판단 등",
  "status": "sent"
}
```

## 규칙

- raw private IDs, 토큰, raw chat dumps, 긴 copied logs를 포함하지 않는다.
- 질문이 직접 research-derived일 때는 paper URL/DOI/arXiv ID를 보존한다.
- 모르는 필드는 fabricated data 대신 empty list 또는 짧은 `unknown`을 사용한다.
- 항목은 간결하고 대시보드 친화적으로 유지한다.
