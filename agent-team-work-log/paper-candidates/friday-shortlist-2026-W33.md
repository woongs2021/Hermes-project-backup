---
title: 2026-W33 금요일 후보 풀 준비 — Muyeol
created: 2026-08-14
updated: 2026-08-14
owner: muyeol
iso_week: 2026-W33
type: friday-shortlist-prep
final_selection_status: pending_09:35_validation
---

# 2026-W33 금요일 후보 풀 준비 — 김무열

## 범위와 입력 확인
- 기준일: 2026-08-14 KST, ISO week `2026-W33`.
- 확인한 입력:
  - `/opt/data/agent-team-work-log/paper-candidates/yuna-2026-W33.md`
  - `/opt/data/agent-team-work-log/paper-candidates/goyounjung-2026-W33.md`
  - `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl` 중 `2026-W33` 항목 20개(`jsonl` 라인 172–191).
- 수집량: Yuna AI/AI×design lane 10개, Go Youn-jung UX/HCI/design lane 10개. 주간 2+2 운영 기준에는 부합한다.
- 이 문서는 09:35 최종 검증/선정 전 후보 풀 준비 문서이다. 최종 2개 선정은 아직 확정하지 않는다.

## 중복·정규화 메모
- DOI/arXiv/KoreaScience URL 기준 명시적 동일 논문 중복은 현재 주간 풀 안에서 발견하지 못했다.
- `From Device-Centered HCI to AI Agent-Centered HCI`는 Yuna 로그에 `2026-W29` 반복/병합 신호가 명시되어 있어 신규성 점수에서 감점한다. 다만 한국 AI-agent HCI 맥락 보강 가치는 유지한다.
- 생성형 디자인 툴 비교 논문이 2건 있다. `doi:10.46248/kidrs.2025.3.532`와 `doi:10.21186/IPR.2026.11.2.125`는 도구·표본·출처가 다른 별도 논문으로 보되, 최종 보고에서는 둘 중 하나만 채택하거나 “도구 비교 클러스터”로 병합 설명하는 편이 안전하다.
- 일부 출처는 본문 전문 접근이 아닌 초록/메타데이터 확인 상태이다. 최종 선정 전 과도한 방법론·효과크기 주장은 금지한다.

## 상위 후보 — Yuna AI/AI×design lane

### Y-1. AI as a reflection partner in UX strategy
- 정규 제목: `AI as a reflection partner in UX strategy`
- ID/URL: `https://doi.org/10.1515/icom-2026-0049`
- 출처/일자: i-com / Walter de Gruyter; Crossref DOI metadata; 2026-08-12
- 접근 상태: 초록/메타데이터 확인, 출판사 전문 접근은 환경상 제한적.
- 핵심 가치: AI를 답 생성기가 아니라 UX 전략의 가정·판단 기준을 드러내는 질문형 reflection partner로 다룬다.
- Chris 관련성: 디자인 리더십, 팀 리뷰 문화, 전략적 판단 언어, AI×UX 교육 관점에서 매우 직접적이다.
- 경량 점수: Chris relevance 5 / evidence 3 / novelty 5 / practical implication 5 / risk 3 → 종합 4.6/5.
- 리스크/주의: 전문 미확인 상태이므로 사례의 깊이, 연구 설계, 일반화 가능성은 WATCH. 최종 보고에서는 “사례/관점 제시”로 제한한다.

### Y-2. Unpacking the dynamics of generative AI use in our daily lives: towards an integrative trust calibration framework
- 정규 제목: `Unpacking the dynamics of generative AI use in our daily lives: towards an integrative trust calibration framework`
- ID/URL: `https://doi.org/10.1007/s00146-026-03279-0` / `https://link.springer.com/article/10.1007/s00146-026-03279-0`
- 출처/일자: AI & Society / Springer Nature; 2026-08-11
- 접근 상태: 초록/메타데이터 확인.
- 핵심 가치: 생성 AI 신뢰를 단일 수용/거부가 아니라 시간에 따른 과신·과소신뢰 보정, trustee 모호성, 에이전트 온톨로지 문제로 정리한다.
- Chris 관련성: AI 에이전트 UX의 관계·피드백·상태 설계를 판단하는 깊은 프레임을 제공한다.
- 경량 점수: Chris relevance 5 / evidence 3 / novelty 5 / practical implication 4 / risk 3 → 종합 4.5/5.
- 리스크/주의: 초록 기반이면 “통합 프레임워크”의 검증 수준을 단정하면 안 된다. 민감한 신뢰/의존성 주제라 과도한 감성 UX 일반화도 피한다.

### Y-3. IntentLint: Supporting Intent Scaffolding and Prompt-time Linting in Human-AI Collaborative Data Analysis
- 정규 제목: `IntentLint: Supporting Intent Scaffolding and Prompt-time Linting in Human-AI Collaborative Data Analysis`
- ID/URL: `https://arxiv.org/abs/2608.04331`
- 출처/일자: arXiv cs.HC/cs.AI 추정; 2026-08-05 색인/ID `2608.04331`
- 접근 상태: arXiv 초록/PDF 링크 메타데이터 확인, 전문 정독 전.
- 핵심 가치: 협업 분석에서 공유 의도 문서와 prompt-time linting으로 에이전트 행동 오류를 줄이는 설계 접근.
- Chris 관련성: agent UX를 프롬프트 입력이 아니라 의도·규칙·위임 경계의 외재화 문제로 보게 한다.
- 경량 점수: Chris relevance 5 / evidence 3 / novelty 4 / practical implication 5 / risk 3 → 종합 4.4/5.
- 리스크/주의: arXiv라 동료심사 전일 가능성이 있다. 실험 결과나 실제 오류 감소율은 최종 검증에서 확인 필요.

### Y-4. Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design
- 정규 제목: `Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design`
- ID/URL: `https://arxiv.org/abs/2608.07091`
- 출처/일자: arXiv cs.HC/cs.AI; 2026-08-07 submitted
- 접근 상태: arXiv 초록/PDF 링크 메타데이터 확인, 전문 정독 전.
- 핵심 가치: 온디바이스/TinyML XAI를 이해관계자 선호, 설명 품질, 배포 비용의 Pareto 선택 문제로 본다.
- Chris 관련성: 온디바이스 AI UX와 자원 제약·설명가능성·신뢰를 함께 보는 제품 판단에 유용하다.
- 경량 점수: Chris relevance 4 / evidence 3 / novelty 4 / practical implication 4 / risk 3 → 종합 4.2/5.
- 리스크/주의: 기술 프레임이 강해 이번 주 최종 2개 중 Chris 성장 질문으로는 Y-1/Y-2보다 덜 넓을 수 있다.

### Y-5. Practical UX/UI Guidelines for AI-Mediated Smartphone App Interfaces in the Age of AI
- 정규 제목: `Practical UX/UI Guidelines for AI-Mediated Smartphone App Interfaces in the Age of AI`
- ID/URL: `https://doi.org/10.7236/IJASC.2026.15.1.81` / `https://koreascience.kr/article/JAKO202611032496429.page`
- 출처/일자: International journal of advanced smart convergence / KoreaScience; 2026-03-31
- 접근 상태: KoreaScience 메타데이터/초록/PDF 링크/DOI 확인.
- 핵심 가치: AI 중재 스마트폰 앱에서 agency, intent, recoverability, trust를 UX/UI 가이드라인으로 제안한다.
- Chris 관련성: 스마트폰 AI 인터페이스 품질 기준을 언어화하는 데 직접적이다.
- 경량 점수: Chris relevance 5 / evidence 3 / novelty 3 / practical implication 5 / risk 3 → 종합 4.2/5.
- 리스크/주의: 실무 가이드라인형 논문은 근거 수준과 검증 방식 확인이 중요하다. One UI로 과잉 연결하지 않는다.

## 상위 후보 — Go Youn-jung UX/HCI/design lane

### G-1. Recommendation-as-Experience: A Framework for Context-Sensitive Adaptation in Conversational Recommender Systems
- 정규 제목: `Recommendation-as-Experience: A Framework for Context-Sensitive Adaptation in Conversational Recommender Systems`
- ID/URL: `https://doi.org/10.1145/3838803`
- 출처/일자: ACM Transactions on Recommender Systems / ACM; 2026-08-11
- 접근 상태: 초록 확인.
- 핵심 가치: 대화형 추천을 정확도 최적화가 아니라 설명, 탐색, 정서적 공명, 자율성 등 경험 목표로 조정하는 RAE 프레임워크.
- Chris 관련성: 개인화/추천/대화 UX를 브랜드 신뢰와 사용자 선택권 관점으로 확장한다.
- 경량 점수: Chris relevance 5 / evidence 4 / novelty 5 / practical implication 5 / risk 3 → 종합 4.7/5.
- 리스크/주의: 전문 미확인 상태면 프레임워크 검증 범위는 WATCH. “정확도보다 경험”이라는 문장을 KPI 폐기로 오해하지 않게 균형 필요.

### G-2. Designing artificial intelligence-driven knowledge governance frameworks for public sector digital transformation
- 정규 제목: `Designing artificial intelligence-driven knowledge governance frameworks for public sector digital transformation`
- ID/URL: `https://doi.org/10.36922/dp026200020`
- 출처/일자: Design+ / AccScience Publishing; 2026-08-07
- 접근 상태: DOI landing page와 Crossref 메타데이터 확인.
- 핵심 가치: AI 도입을 기술 기능이 아니라 지식관리, 거버넌스, 사회기술 아키텍처의 시스템 디자인 문제로 다룬다.
- Chris 관련성: OBD, 조직 실행력, 디자인 리더십, AI 서비스 운영 책임을 연결하는 주간 후보 중 매우 강한 항목이다.
- 경량 점수: Chris relevance 5 / evidence 3 / novelty 5 / practical implication 4 / risk 3 → 종합 4.5/5.
- 리스크/주의: 공공부문 맥락이라 소비자 제품/디자인 조직에 바로 일반화하면 안 된다. 출판사/저널 영향력은 최종 검증에서 재확인 필요.

### G-3. The architecture of AI credentials: how design quality and educational context build self-efficacy and shape readiness for AI-intensive work
- 정규 제목: `The architecture of AI credentials: how design quality and educational context build self-efficacy and shape readiness for AI-intensive work`
- ID/URL: `https://doi.org/10.1108/et-01-2026-0069`
- 출처/일자: Education + Training / Emerald; 2026-08-06
- 접근 상태: 초록/메타데이터 확인.
- 핵심 가치: AI 마이크로자격의 설계 품질, 자기효능감, 윤리적 AI 문화, 교수자 역량이 AI 집약 직무 준비도와 연결된다는 교육 프레임.
- Chris 관련성: 디자인 교육과 인재 성장, AI 시대 리더십 언어에 유용하다.
- 경량 점수: Chris relevance 4 / evidence 4 / novelty 4 / practical implication 4 / risk 3 → 종합 4.2/5.
- 리스크/주의: 중국 대학 표본 기반으로 보이며 디자인 직군 전반에 직접 일반화하기 전 표본·측정 확인 필요.

### G-4. Affective-Utilitarian Brand Strategies and Their Pathways to Consumer Affect and Behavior: A Comparative Study of Olive Young and Daiso
- 정규 제목: `Affective-Utilitarian Brand Strategies and Their Pathways to Consumer Affect and Behavior: A Comparative Study of Olive Young and Daiso`
- ID/URL: `https://doi.org/10.21186/IPR.2026.11.1.061` / `https://koreascience.kr/article/JAKO202609339655812.page`
- 출처/일자: Industry Promotion Research / KoreaScience; 2026 Volume 11 Issue 1
- 접근 상태: 초록/메타데이터 및 PDF URL 확인.
- 핵심 가치: 감성형/실용형 리테일 브랜드 전략이 BX 요소, 감정 반응, 소비자 행동 경로로 다르게 작동함을 비교한다.
- Chris 관련성: BX와 비즈니스 디자인 언어를 연결하는 한국 맥락 후보로 강하다.
- 경량 점수: Chris relevance 4 / evidence 3 / novelty 3 / practical implication 5 / risk 3 → 종합 4.1/5.
- 리스크/주의: 특정 브랜드·리테일 맥락이라 모바일/AI 제품으로 과잉 확장하지 않는다. 방법론 품질 확인 필요.

### G-5. Agonistic diplomacy: a participatory method for structuring dissensus in co-design
- 정규 제목: `Agonistic diplomacy: a participatory method for structuring dissensus in co-design`
- ID/URL: `https://doi.org/10.1080/15710882.2026.2710164`
- 출처/일자: CoDesign / Taylor & Francis; 2026-08-06
- 접근 상태: DOI/Crossref 메타데이터 확인, Taylor 본문 페이지 접근 제한.
- 핵심 가치: 공동디자인에서 합의보다 이해관계자 이견을 구조화하는 참여 방법을 제안한다.
- Chris 관련성: 복잡한 조직 의사결정, 디자인 리더십, 워크숍 품질을 다루는 데 좋다.
- 경량 점수: Chris relevance 4 / evidence 3 / novelty 4 / practical implication 4 / risk 3 → 종합 4.0/5.
- 리스크/주의: 본문 접근 제한으로 방법의 구체성, 사례 검증 수준 확인 전에는 최종 후보로 보류가 안전하다.

## 전체 후보 풀 요약 표
| lane | 후보 수 | 강한 후보 | 보류/감점 사유 |
|---|---:|---|---|
| Yuna AI/AI×design | 10 | Y-1, Y-2, Y-3 | arXiv/초록 기반 후보는 방법론 확인 필요. W29 반복 1건 존재. |
| Go Youn-jung UX/design | 10 | G-1, G-2, G-3 | 일부 DOI 후보 본문 접근 제한. 한국 실증 논문은 맥락 일반화 주의. |

## 리스크 플래그
- WATCH: `AI as a reflection partner in UX strategy` — Chris relevance는 매우 높지만 전문 접근 제한으로 사례 강도 검증 필요.
- WATCH: `Unpacking the dynamics... trust calibration framework` — 신뢰/의존성 주제는 사용자 심리·과신 관련 과장 표현을 피해야 한다.
- WATCH: `IntentLint` 및 `Human-Centered Explainable AI for TinyML Edge Devices` — arXiv 기반이므로 동료심사 상태와 실험 검증 수준 확인 필요.
- WATCH: `Designing artificial intelligence-driven knowledge governance frameworks...` — 출처 신뢰도와 프레임워크 검증 방식 최종 확인 필요.
- HOLD 가능: `Agonistic diplomacy...` — 본문 접근 제한이 계속되면 최종 2개에는 부적합할 수 있다.
- LOW/NOVELTY 감점: `From Device-Centered HCI to AI Agent-Centered HCI` — W29 반복 후보.

## 09:35 검증 작업을 위한 예비 후보 조합
- lane-balanced 예비 1순위: Yuna `AI as a reflection partner in UX strategy` + Go Youn-jung `Recommendation-as-Experience`.
  - 이유: AI를 “정답 생성”에서 “전략/경험 조율”로 확장하는 한 주의 학습 패키지로 일관성이 높다.
  - 검증 과제: 두 항목 모두 초록 기반 해석을 넘어 본문/방법론 접근 가능 여부 확인.
- lane-balanced 예비 2순위: Yuna `Unpacking the dynamics... trust calibration framework` + Go Youn-jung `Designing artificial intelligence-driven knowledge governance frameworks...`.
  - 이유: AI 신뢰 보정과 조직 지식 거버넌스를 묶어 “에이전트 시대의 운영 가능한 신뢰”라는 더 넓은 리더십 주제로 만들 수 있다.
  - 검증 과제: G-2 저널/출판사 신뢰도와 공공부문 맥락 일반화 한계 확인.
- 한국 맥락 보완 후보: Yuna `Practical UX/UI Guidelines for AI-Mediated Smartphone App Interfaces...` 또는 Go Youn-jung `Affective-Utilitarian Brand Strategies...`.
  - 이유: 최종 2개에 한국 출처가 빠질 경우, 보고서의 “한국 소스 갭/보완” 문단에서 언급 가능하다.

## 누락·차단 사항
- 명시적 링크 누락 후보는 없다.
- 다만 일부 항목은 DOI/초록/메타데이터만 확인되었고 전문 접근이 제한적이다. 최종 검증 전에는 방법론·효과·실험 결과를 단정하지 않는다.
- 현재 주간 입력은 충분하여 previous ISO week 파일은 보조 입력으로 열람하지 않았다.
