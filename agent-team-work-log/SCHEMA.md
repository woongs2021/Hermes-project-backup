# 에이전트 팀 작업 로그 스키마

루트 경로: `/opt/data/agent-team-work-log/`

## 목적

Karina가 이끄는 전문 에이전트 팀의 작업 기억을 간결한 Markdown으로 남긴다. 이 로그는 날짜가 있는 작업 요약을 위한 것이며, 장기적으로 유지할 사용자 선호나 비밀값을 저장하는 곳이 아니다.

## 구조

- `karina/daily/YYYY-MM-DD.md`
- `yuna/daily/YYYY-MM-DD.md`
- `goyounjung/daily/YYYY-MM-DD.md`
- `son/daily/YYYY-MM-DD.md`
- `faker/daily/YYYY-MM-DD.md`
- `muyeol/daily/YYYY-MM-DD.md`
- `<agent>/topics/` — 반복되는 주제가 있을 때 사용
- `<agent>/index.md` — 라우팅과 최근 중요 메모가 필요할 때 사용

## 규칙

1. 해당 에이전트가 그날 실질적인 작업을 수행했을 때만 일일 Markdown 노트를 작성한다.
2. 빈 노트, 플레이스홀더, 하트비트, 인사, 무작업 기록은 만들지 않는다.
3. 노트에는 결정, 산출물, 블로커, 근거, 다음 행동을 요약한다. 원시 채팅 로그를 그대로 붙여 넣지 않는다.
4. 원시 Telegram/Slack 토큰, OAuth/API 키, 비공개 ID, 자격 증명처럼 보이는 긴 문자열은 절대 기록하지 않는다.
5. 날짜 경계는 사용자가 따로 지정하지 않는 한 Chris의 작업일 기준, 즉 KST를 따른다.
6. 안정적인 선호는 `memory` 또는 `SOUL.md`에 저장하고, 날짜가 지나면 변할 수 있는 임시 진행 상황은 이 작업 로그에 저장한다.

## 권장 일일 템플릿

```markdown
---
title: YYYY-MM-DD <Agent> 작업 로그
created: YYYY-MM-DD
updated: YYYY-MM-DD
agent: <karina|yuna|goyounjung|son|faker|muyeol>
type: daily-work-log
sources: [slack, telegram, cli, kanban]
---

# YYYY-MM-DD <Agent> 작업 로그

## 요약
- 

## 수행한 작업
- 

## 결정 / 추천
- 

## 산출물 / 근거
- 

## 블로커 / 리스크
- 

## 다음 행동
- 

## Karina를 위한 인수인계 메모
- 
```
