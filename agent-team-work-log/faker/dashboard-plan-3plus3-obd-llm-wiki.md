---
title: Faker 3+3 OBD LLM Wiki & Dashboard 개발 계획
created: 2026-07-14
updated: 2026-07-14
owner: faker
status: planned-not-started
requested_by: Chris Park
handoff_from: karina
---

# Faker 3+3 OBD LLM Wiki & 대시보드 개발 계획

## 0. 현재 상태

- **상태:** 계획 저장만 완료. 구현 시작 금지.
- **재논의 시점:** 2026년 8월 이후, 또는 Chris가 명시적으로 시작 요청할 때.
- **담당:** Faker.
- **Karina 역할:** 범위 정리, 데이터 출처 확인, 최종 UX/브랜드/의사결정 합성.
- **목표:** 3+3 리서치, OBD 성장 질문, Son 질문 출처 흐름, weekly/monthly 성장 리포트를 나중에 한눈에 볼 수 있는 LLM-maintained wiki 및 웹 대시보드로 발전시킨다.

## 1. 배경

Chris는 매일/매주 쌓이는 3+3 리서치와 OBD 성장 루프를 단순 로그가 아니라, 나중에 탐색 가능한 지식 시스템으로 보고 싶어 한다.

참고 방향:

- Karpathy식 LLM-maintained Markdown wiki 패턴
- raw source는 보존
- LLM은 요약, 분류, 교차링크, 업데이트, 모순/중복 체크를 담당
- 이후 Markdown wiki를 기반으로 웹사이트 대시보드 구축

## 2. 핵심 데이터 소스

### 2.1 3+3 리서치 / 논문 후보

- `/opt/data/agent-team-work-log/paper-후보s/`
- `all-research-items.jsonl`가 존재할 경우 우선 확인
- Yuna daily AI/AI×UX/LLM/agent 후보
- Go Youn-jung daily UX/HCI/brand/design-management 후보
- DOI, arXiv, OpenReview, ACM, URL, title 등 직접 source identifier 보존

### 2.2 Weekly / Monthly 성장 리포트

- Karina weekly synthesis outputs
- Muyeol Friday validation / best-3 selection
- monthly research-growth report outputs
- weekly-selected-papers.md 등 최종 selection 파일이 있으면 기준 소스로 사용

### 2.3 Son daily growth question / Chris answer loop

- Son Telegram profile sessions
- Son daily team work logs
- Chris 답변 요약
- 질문별 출처 태그 및 이유

### 2.3.1 OBD Growth Timeline 기록

Chris가 2026-08-10에 명시적으로 요청한 추가 요구사항이다. Son이 정리한 “7월 대비 성장”, “OBD 프로그램 시작 시점”, “우선순위 판단 변화” 같은 회고성 기록도 Faker 개발 루프의 계획 범위에 포함한다.

초기 seed event 후보:

- 2026-07-03: 4주 OBD/3+3 성장 루프 기획 시작
- 2026-07-04: Son의 첫 `오늘의 성장 질문` DM 발송
- 2026-07-06: Son 프로필 Telegram cron 운영 안정화
- 2026-07-10 전후: AI UX/브랜드 감각 판단에서 브랜드 관점·선택/포기·디자인경영 판단으로 선명화
- 2026-07-31: AX 시장, 역할·검수·교육·가격 모델 재설계 관점으로 확장
- 2026-08-08~2026-08-10: 디자인팀 내부 QA → 내부 검증 → 유관부서 협의 → 실행 문서 구조로 전환
- 2026-08-10: Chris의 우선순위 판단 `C → D`를 “전체 비교 모드에서 핵심 진행 모드로 압축한 성장 신호”로 기록

초기 schema 후보:

```json
{
  "date_kst": "YYYY-MM-DD",
  "event_type": "program_start|question_sent|answer_signal|son_interpretation|priority_shift|monthly_synthesis",
  "title": "짧은 성장 이벤트 제목",
  "summary": "Chris의 판단 변화 또는 루프 변화 요약",
  "source_paths": ["관련 Son/Faker/Karina/Muyeol 로그 또는 source-flow 경로"],
  "obd_themes": ["AI UX judgment", "brand asset", "design management", "organizational decision quality"],
  "growth_shift": "감각 → 기준 → 우선순위 → 조직 언어 → 운영체계 중 해당 변화",
  "privacy_level": "public_safe_summary|private_summary|raw_private_excluded",
  "dashboard_candidate": true
}
```

대시보드 표현 원칙:

- raw Telegram/Slack 대화는 직접 노출하지 않는다.
- UI에는 Son/Karina가 요약한 public-safe 성장 이벤트만 사용한다.
- “얼마나 성장했는가”를 점수화하기보다, 판단 방식이 어떻게 바뀌었는지 timeline과 theme shift로 보여준다.
- `C → D` 같은 짧은 선택도 맥락이 있으면 중요한 OBD growth signal로 보존한다.

### 2.4 Son 질문 출처 흐름 로그

- 스키마:
  - `/opt/data/agent-team-work-log/growth-question-sources/SCHEMA.md`
- machine-readable 기준 소스:
  - `/opt/data/agent-team-work-log/growth-question-sources/son-question-source-log.jsonl`

이 파일은 Faker 대시보드에서 매우 중요하다. 질문이 어떤 출처에서 나왔는지 시각화할 수 있게 해준다.

예상 필드:

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
    {"type": "karina_framing", "path": "...", "note": "..."},
    {"type": "muyeol_guardrail", "path": "...", "note": "..."}
  ],
  "related_research_ids": ["DOI/arXiv/URL/title if explicitly used"],
  "obd_theme": "시장/가치교환/브랜드자산/조직판단 등",
  "status": "sent"
}
```

## 3. 대시보드에서 보고 싶은 핵심 질문

1. 이번 주/이번 달에 어떤 리서치 주제가 반복해서 등장했는가?
2. 최종 best-3로 뽑힌 논문/리서치는 어떤 테마와 연결되는가?
3. Son의 성장 질문은 어떤 출처에서 주로 만들어졌는가?
4. Chris의 답변은 어떤 OBD theme로 축적되고 있는가?
5. 질문과 답변이 실제로 Chris의 사고 언어를 어떻게 바꾸고 있는가?
6. 연구 → 질문 → 답변 → weekly synthesis → monthly growth insight가 하나의 흐름으로 보이는가?

## 4. 정보 구조 초안

### 4.1 Wiki Layer

Markdown wiki로 먼저 구축한다.

예상 페이지:

- `index.md`
- `topics/`
  - OBD themes
  - AI UX themes
  - brand/design-management themes
  - business/value-exchange themes
- `papers/`
  - paper/item 별 요약 페이지
- `questions/`
  - Son daily question pages
- `growth-events/`
  - OBD 프로그램 시작, 7월 대비 성장 회고, 우선순위 판단 변화 같은 growth timeline event pages
- `weeks/`
  - weekly synthesis pages
- `months/`
  - monthly growth report pages
- `entities/`
  - agents, papers, concepts, Chris answer themes

### 4.2 Data Layer

원본과 가공본을 분리한다.

- Raw sources
  - paper 후보 files
  - cron outputs
  - Son source log JSONL
  - weekly/monthly reports
- Processed summaries
  - normalized paper/item index
  - question-source graph
  - OBD theme index
  - Chris answer theme extraction
  - OBD growth event timeline

### 4.3 대시보드 Layer

초기 화면 후보:

1. **Growth Timeline**
   - 날짜별 research → question → answer → synthesis 흐름
   - 7월 대비 성장 변화, 시작 시점, 우선순위 판단 변화 같은 OBD growth event를 카드로 표시
2. **Question Source Map**
   - Son 질문이 어떤 source tag에서 나왔는지 비율/흐름
3. **OBD Theme Graph**
   - 시장, 가치교환, 브랜드자산, 조직판단, AI UX 등 누적 theme
4. **Weekly Best-3 Panel**
   - Muyeol 최종 best-3와 Karina synthesis
5. **Paper / Question / Answer Link View**
   - 특정 논문이 어떤 질문으로 이어졌고, Chris가 어떻게 답했는지 추적

## 5. 단계별 개발 계획

### Phase history logging 원칙

Faker는 각 개발 단계가 시작/진행/완료될 때 히스토리를 남긴다. 이 히스토리는 나중에 대시보드 자체의 “어떻게 만들어졌는가” 기록이자, Chris의 OBD 성장 시스템이 제품화되는 과정의 증거가 된다.

기본 저장 위치:

- `/opt/data/agent-team-work-log/faker/대시보드-history/phase-history.jsonl`
- `/opt/data/agent-team-work-log/faker/대시보드-history/phase-logs/YYYY-MM-DD.md`

각 phase entry의 권장 필드:

```json
{
  "date_kst": "YYYY-MM-DD",
  "phase": "Phase 1 — 데이터 인벤토리",
  "status": "planned|started|in_progress|blocked|completed|revised",
  "decision": "그날의 핵심 결정",
  "artifact_paths": ["생성/수정한 파일 경로"],
  "data_sources_checked": ["확인한 source path"],
  "design_notes": ["woongdesignv2 적용/수정 메모"],
  "risks_or_blockers": ["리스크/블로커"],
  "next_action": "다음 행동",
  "handoff_to_karina": "Karina가 알아야 할 요약"
}
```

운영 규칙:

- phase가 바뀔 때마다 `phase-history.jsonl`에 append한다.
- 중요한 설계 변경, 데이터 스키마 변경, UI 방향 변경은 별도 daily phase log에 짧게 남긴다.
- 구현 결과뿐 아니라 “왜 이 방향으로 갔는지”도 남긴다.
- raw private chat, token, credential, 긴 원문 로그는 저장하지 않는다.
- phase history는 대시보드에서 나중에 “Build Timeline” 또는 “System Evolution” 뷰로 시각화할 수 있게 유지한다.

### Phase 0 — 계획 보존

- **상태:** 완료
- Chris 요청 내용을 Markdown 계획표로 저장
- 구현 시작하지 않음
- 8월 이후 재논의
- phase history logging 구조까지 함께 계획에 포함

### Phase 1 — 데이터 인벤토리

목표: 실제로 어떤 파일과 로그가 안정적으로 존재하는지 확인.

작업:

- 3+3 후보 파일 구조 확인
- weekly/monthly output 위치 확인
- Son source log JSONL 누적 상태 확인
- Son daily logs에서 OBD Growth Timeline seed event 후보 확인
- 2026-07-03/07-04/07-06 시작 기준과 2026-08-10 성장 회고 기록 확인
- 누락 필드 확인
- source URL/DOI/arXiv 보존 여부 확인

산출물:

- data inventory markdown
- source path map
- missing-field checklist
- OBD Growth Timeline seed event inventory

### Phase 2 — LLM Wiki 스키마 설계

목표: raw data를 Markdown wiki로 변환하는 규칙 정의.

작업:

- paper item schema
- question source schema
- Chris answer theme schema
- OBD growth event schema
- OBD theme taxonomy
- wikilink 규칙
- duplicate paper handling 규칙

산출물:

- `wiki/SCHEMA.md`
- `wiki/index.md` 초안
- sample pages 3~5개

### Phase 3 — Wiki Generator Prototype

목표: local script로 raw data를 읽어 Markdown wiki를 생성/갱신.

작업:

- Python/Node 중 가벼운 구현 선택
- JSONL/Markdown parser
- paper item normalization
- question-source log ingestion
- OBD growth event ingestion
- weekly/monthly report linking
- wikilink generation

산출물:

- local generator script
- generated wiki sample
- validation log

### Phase 4 — 대시보드 IA / UX Prototype

목표: Chris가 한눈에 볼 첫 화면 정의.

작업:

- 대시보드 IA
- main navigation
- timeline / graph / card layout 초안
- 모바일/데스크톱 우선순위
- Karina + Go Youn-jung 디자인 리뷰 가능

산출물:

- 대시보드 wireframe markdown 또는 HTML prototype
- first-screen spec
- data-to-UI mapping

### Phase 5 — Web 대시보드 구현

목표: 실제 웹 대시보드 구현.

작업 후보:

- Static site first
- Markdown/JSONL 기반 prebuild
- Search/filter
- Weekly/monthly views
- Question source visualization
- OBD theme graph

산출물:

- working local web 대시보드
- README
- build/run instructions
- sample data verification

## 6. 질문 출처 로그의 대시보드 활용 방식

`son-question-source-log.jsonl`는 아래 시각화에 쓰인다.

### 6.1 Source Tag Distribution

- Chris 답변 기반 질문 비율
- OBD 프레임 기반 질문 비율
- PM/비즈니스 판단 기반 질문 비율
- 리서치/논문 기반 질문 비율
- 브랜드/디자인경영 기반 질문 비율

### 6.2 Question Lineage

한 질문이 어떤 흐름에서 나왔는지 추적한다.

```text
Daily paper candidates
→ Karina framing memo
→ Muyeol guardrail
→ Son question
→ Chris answer
→ Weekly synthesis
→ Monthly growth insight
```

### 6.3 OBD Growth Signals

질문과 답변을 theme별로 묶는다.

- 시장/category framing
- customer value
- brand asset
- business strategy
- design management
- value exchange
- organizational decision quality
- AI UX judgment

추가로 2026-08-10 Chris 요청에 따라, 질문/답변 단위뿐 아니라 Son이 해석한 성장 변화도 별도 event로 묶는다.

- program start / 운영 시작점
- judgment shift / 판단 방식 변화
- priority shift / 우선순위 압축
- business translation / 디자인 감각의 비즈니스 언어화
- organization translation / 디자인 판단의 협업·QA·실행 구조화

### 6.4 대시보드 Card 예시

```text
2026-W29 / Question #3
Tag: [Chris 답변 기반 · OBD 프레임 기반]
Theme: 브랜드 자산 / 도메인 지식 DB
Question: ...
Chris Answer Signal: 브랜드 도메인지식 DB + 디자인 식별성
Linked Research: ...
Weekly Synthesis: ...
```

## 7. 디자인 스타일 원칙

- 대시보드 visual direction은 **woongdesignv2**를 참조한다.
- 목표는 흔한 AI 대시보드 / generic SaaS / overly neon data-viz 느낌을 피하고, Chris의 디자인 감각에 맞는 정제된 연구 OS처럼 보이게 하는 것이다.
- 핵심 키워드:
  - restrained but warm
  - editorial research system
  - calm hierarchy
  - refined typography
  - generous spacing
  - quiet semantic color
  - card-based but not startup-template-like
  - AI티가 안 나는 시각 품질
- 정보 구조는 복잡해도 화면은 차분해야 한다.
- Son question source map, OBD theme graph, weekly best-3 cards는 정보 밀도를 높이되, 타이포 위계와 여백으로 읽기 쉽게 만든다.
- Go Youn-jung에게 디자인 리뷰를 요청할 경우, woongdesignv2 기준으로 typography, spacing, semantic color, density, card rhythm, graph legibility를 비평하게 한다.

## 8. 보류 원칙

- Chris가 명시적으로 시작 요청하기 전까지 Faker는 구현하지 않는다.
- 현재는 계획, 스키마, 로그 경로만 보존한다.
- 자동화나 대시보드 생성이 토큰/메모리 비용을 키우지 않도록 Phase 1에서 데이터 인벤토리부터 한다.
- 원시 private chat log를 그대로 대시보드에 노출하지 않는다.
- public paper/source link는 보존하되, private IDs/토큰/raw 자격 증명는 기록하지 않는다.

## 9. 8월 재개 시 첫 질문

Chris에게 먼저 확인할 것:

1. 첫 화면은 “주간 성장 타임라인”이 좋을까, “논문/질문/답변 연결 그래프”가 좋을까?
2. 웹 대시보드는 local-only로 시작할까, 나중에 배포 가능한 static site로 시작할까?
3. Son 질문/Chris 답변은 어느 수준까지 시각화해도 괜찮을까?
4. 3+3 best-3 중심으로 볼까, daily 후보s까지 모두 탐색 가능하게 할까?
5. 디자인 톤은 research OS에 가깝게 갈까, warm growth companion 대시보드에 가깝게 갈까?
6. 2026-07-03/07-04/07-06 중 어떤 날짜를 OBD Growth Timeline의 공식 시작점으로 표시할까?
7. `C → D` 같은 짧은 선택과 Son의 해석을 timeline card로 어느 정도까지 보여줄까?

## 10. Karina 인수인계 메모

- 이 문서는 Faker가 8월 이후 3+3/OBD LLM wiki와 대시보드 개발을 시작할 때의 계획표다.
- 최근 추가된 요구는 **Son 질문 출처 흐름 로그를 대시보드-ready data로 남기는 것**과 **7월 대비 성장·프로그램 시작일·우선순위 변화 같은 OBD Growth Timeline event를 계획 범위에 포함하는 것**이다.
- machine-readable 질문 출처 로그는 `/opt/data/agent-team-work-log/growth-question-sources/son-question-source-log.jsonl`를 우선 사용한다.
- growth event seed는 우선 Son daily logs와 Son/Karina weekly/monthly synthesis의 public-safe 요약을 사용한다.
- 구현 전에는 반드시 실제 누적 데이터 품질을 확인해야 한다.
- 개발 단계 history는 `/opt/data/agent-team-work-log/faker/대시보드-history/phase-history.jsonl`와 `phase-logs/YYYY-MM-DD.md`에 남기도록 계획했다.
- 디자인 스타일은 **woongdesignv2**를 기준으로 삼고, 흔한 AI/SaaS 대시보드 느낌을 피한다.
