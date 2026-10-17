# AI/AX 시장조사 다중 리포트 Karina 종합 패턴

## Trigger
- Chris가 `오늘 2명의 시장 조사를 카리나가 각각 분야별로 전체 요약해줘`, `오늘 AI/AX 시장조사 종합해줘`, `Yuna/Go Youn-jung/Son 리포트 합쳐줘`라고 요청할 때.

## Source order
1. 현재 KST 날짜를 확인한다.
2. 해당 날짜의 raw reports를 우선 확인한다:
   - `/opt/data/ai-ax-job-shift-loop/raw/yuna/YYYY-MM-DD.md`
   - `/opt/data/ai-ax-job-shift-loop/raw/goyounjung/YYYY-MM-DD.md`
   - `/opt/data/ai-ax-job-shift-loop/raw/son/YYYY-MM-DD.md` when present
3. 오늘 파일이 없으면 직전 실행일의 raw reports를 찾고, 날짜 차이를 사용자에게 명시한다.

## Synthesis shape for Chris
Keep it concise and 분야별로 나눈다.

1. **한 줄 요약**
   - `직업 대체`보다 `과업·역할·가격 모델 재편`으로 프레임한다.
2. **Yuna lane — 노동시장/과업 변화**
   - Korea/global evidence, job/task exposure, junior ladder, education/reskilling.
3. **Go Youn-jung lane — 디자인 직군/교육 변화**
   - 생성에서 판단으로 이동, UX context, portfolio evidence, design quality ops.
4. **Son lane — 비즈니스 시장 변화**
   - Who pays, productizable offers, Korea/global market budgets, blockers.
5. **OBD/Chris implications**
   - 가능한 서비스 언어: `AI Design Quality OS`, `Brand AI Governance`, `AI-era Portfolio Clinic`, `Human-AI Workflow Audit`, `Junior Craft Ladder Program`, `SMB AX Readiness Sprint`.
6. **Cautions**
   - AI exposure ≠ actual layoffs.
   - RSS/news/vendor/consulting figures stay WATCH until Muyeol validation.
   - Do not turn `junior roles need senior skills` into individual blame; frame it as organizational ladder redesign.

## Logging
If Karina performs a substantive synthesis, update `/opt/data/agent-team-work-log/karina/daily/YYYY-MM-DD.md` with source file paths, synthesis decision, and validation caveats. Do not store raw report dumps or secret/private IDs.
