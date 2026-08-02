# Hermes Organizational Memory Policy

## 상태

```text
Status: Draft / Planning Only
Implementation: Not started
Owner: Karina
Purpose: Future organizational memory and workflow-learning layer for the Hermes agent team
```

> This policy is 저장됨 for future use. It should not be treated as active operating procedure until Chris explicitly approves 구현.

---

## 목표

Hermes는 단순히 작업을 수행하는 에이전트 팀이 아니다.

모든 작업 과정에서 발생하는 의사결정, 라우팅 패턴, 실행 결과, 성공 및 실패 사례를 조직 자산으로 축적한다.

장기적으로 축적된 데이터를 기반으로 다음을 가능하게 한다.

- 워크플로우 최적화
- 온톨로지 구축
- 멀티 에이전트 자동화
- LangGraph 기반 전환

---

## Karina 책임

Karina는 모든 요청에 대해 다음을 판단한다.

1. 어떤 에이전트를 호출했는가
2. 왜 해당 에이전트를 호출했는가
3. 어떤 결과를 얻었는가
4. 최종적으로 어떤 의사결정을 내렸는가

중요한 작업은 반드시 Work Log에 기록한다.

---

## Work Log 저장 위치

```text
/opt/data/agent-team-work-log
```

---

## 기록해야 하는 항목

## 1. Daily Log

포함 항목:

- 날짜
- 사용자 요청
- 호출된 에이전트
- 주요 결과
- 최종 결정
- 다음 액션

권장 저장 위치:

```text
/opt/data/agent-team-work-log/{agent}/daily/YYYY-MM-DD.md
```

---

## 2. Decision Log

다음 조건 중 하나에 해당하면 반드시 생성한다.

- 아키텍처 변경
- 역할 변경
- 새로운 워크플로우 채택
- 중요한 제품 방향 결정
- 기술 스택 결정

포함 항목:

- 문제 정의
- 고려한 대안
- 선택한 안
- 선택 이유
- 예상 영향

권장 저장 위치:

```text
/opt/data/agent-team-work-log/decisions/YYYY-MM-DD-short-title.md
```

---

## 3. Routing Log

Karina는 주요 작업마다 라우팅 판단을 기록한다.

포함 항목:

- 사용자 요청
- 호출한 에이전트
- 호출 이유
- 결과 평가

권장 추가 필드:

```yaml
expected_output: ""
actual_result: ""
result_quality: good | partial | failed | not_verified
follow_up_needed: true | false
next_agent: null
```

권장 저장 위치:

```text
/opt/data/agent-team-work-log/routing/YYYY-MM-DD.md
```

---

## 패턴 발견

Karina는 주기적으로 Work Log를 분석한다.

다음을 발견하면 Pattern 문서로 저장한다.

- 반복되는 질문
- 반복되는 워크플로우
- 반복되는 에이전트 조합
- 성공률이 높은 실행 방식
- 실패가 반복되는 유형

권장 기준:

```text
같은 유형이 3회 이상 반복됨
또는
한 번의 사례지만 매우 중요한 성공/실패임
```

권장 저장 위치:

```text
/opt/data/agent-team-work-log/patterns/pattern-name.md
```

Pattern 문서 권장 항목:

- Pattern Name
- Observed In
- Trigger
- Agent Combination
- What Worked
- What 실패
- Recommended Workflow
- Confidence
- LangGraph Conversion Potential
- Last 업데이트됨

---

## 로그 레벨 제안

과도한 기록을 방지하기 위해 기록 강도를 나눈다.

```text
Level 0 — 기록 안 함
단순 인사, 확인, 날씨, 짧은 잡담

Level 1 — Daily Log만 기록
일반적인 업무, 간단한 저장/전송/정리

Level 2 — Routing Log 포함
에이전트 라우팅이 있었거나, 작업 분배 판단이 중요한 경우

Level 3 — Decision Log 포함
제품 방향, 역할 변경, 아키텍처, 워크플로우, 기술 스택 결정

Level 4 — Pattern 후보
반복되는 성공/실패 방식이 발견된 경우
```

---

## 조직 기억의 분리 원칙

```text
Memory:
Chris의 안정적인 선호, 장기 원칙, 지속적 컨텍스트

Work Log:
날짜 기반 업무 과정, 결과, 다음 액션

Decision Log:
조직적으로 중요한 선택

Routing Log:
Karina의 에이전트 호출 판단과 결과 평가

Pattern:
반복되는 운영 방식과 성공/실패 패턴

Skill:
재사용 가능한 절차와 검증된 실행 방법
```

---

## LangGraph 전환을 위한 관점

이 정책의 장기 목적은 수동 오케스트레이션을 구조화된 자동 워크플로우로 발전시키는 것이다.

진화 단계:

```text
Manual Orchestration
→ Logged Orchestration
→ Pattern-based Routing
→ Semi-automated Workflow
→ LangGraph Agent Organization
```

Routing Log와 Decision Log는 향후 LangGraph의 node, edge, condition 설계 데이터로 활용될 수 있다.

예시:

```text
요청 유형: 시장 조사
선택 에이전트: Yuna
조건: 외부 근거 필요
후속 에이전트: Muyeol fact-check
성공 기준: 출처 있는 인사이트 5개 이상
```

향후 자동화 가능 형태:

```python
if request.requires_external_research:
    route_to_yuna()

if result.contains_high_stakes_claims:
    route_to_muyeol()
```

---

## 원칙

로그는 사람과 AI가 모두 읽기 쉬운 Markdown 형식을 기본으로 한다.

가능하면 YAML Frontmatter를 포함한다.

데이터 저장의 목적은 단순 기록이 아니라 미래의 조직 기억과 워크플로우 학습 자산을 구축하는 것이다.

---

## 구현 Note

현재 문서는 정책 초안 저장용이다.

Chris가 명시적으로 승인하기 전까지 다음 작업은 수행하지 않는다.

- 기존 SCHEMA.md 변경
- 새 폴더 구조 생성
- 크론잡 추가 또는 변경
- 에이전트 운영 규칙 변경
- Routing Log / Decision Log 의무화
- Pattern 분석 자동화

