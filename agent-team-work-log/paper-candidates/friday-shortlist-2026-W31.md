---
title: 2026-W31 금요일 논문 후보 풀 준비
created: 2026-07-31
updated: 2026-07-31
agent: muyeol
type: friday-shortlist
iso_week: 2026-W31
sources:
  - /opt/data/agent-team-work-log/paper-candidates/yuna-2026-W31.md
  - /opt/data/agent-team-work-log/paper-candidates/goyounjung-2026-W31.md
  - /opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl
---

# 2026-W31 금요일 후보 풀 준비 — Muyeol

## 준비 상태
- KST 기준 2026-07-31 금요일, ISO week `2026-W31` 후보 풀을 정리했습니다.
- 입력 파일 확인: `yuna-2026-W31.md`, `goyounjung-2026-W31.md`, `all-research-items.jsonl`의 `iso_week=2026-W31` 항목을 확인했습니다.
- 집계 결과: Yuna 15개 + Go Youn-jung 15개 = 총 30개 로컬 후보가 확인되었습니다.
- 중복 처리 결과: 현재 주 내부의 명백한 동일 논문 중복은 발견하지 못했습니다. 단, 아래 2개는 이전 주/과거 후보와 반복 신호가 있어 가중 신호로 보되, 이번 주 풀에는 1회만 남겼습니다.
- 주의: 이 문서는 09:35 최종 검증/선정 전 후보 풀 준비본입니다. **최종 best 3 선정본이 아닙니다.**

## 선별 기준 — 가벼운 1차 점수 렌즈
- Chris 성장 관련성: AI/UX/design leadership, OBD/business design, 디자인교육/조직 판단에 주는 학습 가치.
- 근거 신뢰도: ACM/ACL/CHI/OpenReview/peer-reviewed DOI/공식 연구 페이지/KCI 등 출처 품질과 접근 가능성.
- 새로움/시의성: 2026년 최근 출판·공개, 이번 주 반복 발견 신호.
- 실무적 함의: 에이전트 UX, 권한·안전, 협업 평가, 브랜드/경험 시스템, 디자인교육 루브릭으로 번역 가능한 정도.
- 리스크/과장 가능성: arXiv-only, abstract/metadata-only, 모델 성능을 곧바로 제품 UX로 일반화하는 위험, 민감영역/프라이버시/의인화 관련 위험.

## 1차 상위 후보군 — 최종 3개 후보가 아니라 검증 우선순위

| 우선순위 | 후보 | 정규화 ID/링크 | 출처/날짜 | 1차 판단 | 주요 리스크 |
|---|---|---|---|---|---|
| HIGH | Don’t Click That: Teaching Web Agents to Resist Deceptive Interfaces | ACL `2026.acl-long.310`; https://aclanthology.org/2026.acl-long.310/ | ACL 2026 Long Papers | 웹/GUI 에이전트가 기만 UI에 저항해야 한다는 안전·브랜드 신뢰 축이 매우 강합니다. | 벤치마크/훈련 효과를 실제 상용 agent UX로 과도 일반화하지 않도록 확인 필요. |
| HIGH | Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | ACL `2026.acl-long.2192`; DOI `10.18653/v1/2026.acl-long.2192`; https://aclanthology.org/2026.acl-long.2192/ | ACL 2026 Long Papers | “합성 사용자 평가”의 한계를 직접 찌르는 검증형 논문입니다. Chris에게 빠른 AI 평가와 느린 인간 검증의 역할 구분을 분명히 줍니다. | 최종 선정 시 실제 연구 설계·참여자 범위와 claim 강도를 확인해야 합니다. |
| HIGH | Collaborative Gym: A Framework for Enabling and Evaluating Human-Agent Collaboration | OpenReview `GDYueXtKXT`; https://openreview.net/forum?id=GDYueXtKXT | ICLR 2026 Poster / OpenReview | 완전 자율보다 인간 개입·선호·통제를 평가하는 human-agent collaboration 프레임워크라 OBD/agentic workflow 학습 가치가 큽니다. | OpenReview 논문은 최종 버전/리뷰 상태와 실험 범위 확인 필요. |
| HIGH | ADCanvas: Accessible and Conversational Audio Description Authoring for Blind and Low Vision Creators | Google Research page; PDF https://storage.googleapis.com/gweb-research2023-media/pubtools/1033936.pdf | Google Research Publications, 2026 | 접근성·창작자 agency·편집 가능한 AI 도구라는 균형이 좋습니다. 자동 생성보다 검증/수정 권한을 강조합니다. | 로컬 로그에 DOI/학회 ID가 없어 최종 선정 전 venue/peer-review 상태 확인 필요. |
| HIGH | Multiexperience: Core principles grounded in experience theory, theory of embodied cognition, and schema theory | DOI `10.1016/j.jretconser.2026.104980`; https://doi.org/10.1016/j.jretconser.2026.104980 | Journal of Retailing and Consumer Services, 2026-07-28 | UX·CX·다중 기기/모달리티 경험을 연결하는 경영/경험 프레임워크로 Chris의 제품군·생태계 사고에 유익합니다. | 소비자서비스/리테일 맥락이므로 OS/디자인 시스템 일반화는 신중해야 합니다. |
| HIGH | Scaling Agentic UX | DOI `10.1201/9781003738374-13`; https://doi.org/10.1201/9781003738374-13 | Designing Agentic AI Experiences / Taylor & Francis, 2026-07-28 | 개별 기능보다 Agentic CoE, Master Agent Persona, 공용 패턴 라이브러리 등 조직적 UX 거버넌스 언어가 강합니다. | 단행본 챕터 성격상 실증 논문보다 주장/프레임 성격이 강할 수 있습니다. |
| HIGH | A Framework of User Experience Principles for Human-AI Agent Interaction in the Workplace | arXiv `2607.19941v1`; http://arxiv.org/abs/2607.19941v1 | arXiv cs.HC/cs.AI, 2026-07-22 | 업무용 에이전트 UX 원칙을 다중 방법으로 구조화했다는 점에서 디자인 리더십과 조직 채택 판단에 유용합니다. | arXiv-only라 peer review 상태와 방법론 세부 확인이 필요합니다. |
| HIGH | Tech Worker Challenges Managing Humanlike GenAI | Google Research page; https://research.google/pubs/tech-worker-challenges-managing-humanlike-genai/ | Google Research / CHI 2026 | 의인화의 위험과 조직 내 역할별 해석 차이를 다뤄 AI 페르소나/브랜드 판단에 좋습니다. | “인간형 GenAI” 주제는 감성 UX로 과잉 포장되기 쉬우므로 책임 경계 중심으로 읽어야 합니다. |
| WATCH-HIGH | WebSTAR: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering | ACL `2026.acl-long.21`; DOI `10.18653/v1/2026.acl-long.21`; https://aclanthology.org/2026.acl-long.21/ | ACL 2026 Long Papers | computer-use agent의 단계별 데이터 품질 관리 신호가 강합니다. | 훈련 데이터 정제 논문이라 Chris-facing UX 학습으로는 안전/평가 후보보다 한 단계 기술적입니다. |
| WATCH-HIGH | See2Refine: Vision-Language Feedback Improves LLM-Based eHMI Action Designers | arXiv `2602.02063`; https://research.google/pubs/see2refine-vision-language-feedback-improves-llm-based-ehmi-action-designers/ | Google Research / ACL 2026 | VLM 피드백 폐루프로 인터페이스 행동 설계를 검증한다는 점이 안전·의도 전달 설계에 좋습니다. | 자율주행 eHMI 특수 맥락이므로 일반 AI UX로 확장할 때 제한을 명시해야 합니다. |

## 나머지 후보 풀 — 정규화/중복 메모

| 상태 | Lane | 후보 | 정규화 ID/URL | 출처/날짜 | 메모 |
|---|---|---|---|---|---|
| WATCH | yuna | Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models | DOI `10.18653/v1/2026.acl-long.6`; ACL `2026.acl-long.6`; https://aclanthology.org/2026.acl-long.6/ | ACL 2026 Long Papers, 2026-07 | 음성 AI 품질을 의미/turn-taking으로 분해하는 지표 가치가 있으나 최종 3에는 다소 모델 평가 중심입니다. |
| WATCH | yuna | ReContraster: Making Your Posters Stand Out with Regional Contrast | DOI `10.18653/v1/2026.acl-long.98`; ACL `2026.acl-long.98`; https://aclanthology.org/2026.acl-long.98/ | ACL 2026 Long Papers, 2026-07 | 시각 위계/대비 평가 루프라는 디자인 언어가 좋지만 포스터 도메인 특수성이 있습니다. |
| WATCH | yuna | Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets | arXiv `2606.25760`; https://arxiv.org/abs/2606.25760 | arXiv, 2026-06-24 | GUI agent가 불확실할 때 멈추는 기준과 safety region이 좋습니다. arXiv-only 위험을 확인해야 합니다. |
| WATCH | goyounjung | “It Became My Buddy, But I’m Not Afraid to Disagree”: A Multi-Session Study of UX Evaluators Collaborating with Conversational AI Assistants | DOI `10.1145/3772318.3790536`; https://doi.org/10.1145/3772318.3790536 | CHI 2026 / ACM, 2026-04-13 | UX 평가자가 AI와 신뢰를 조정하는 실무 연구라 교육/리서치 품질관리에 유용합니다. |
| WATCH | goyounjung | Transparent by Design, Usable in Practice? A Formative Usability Study of a Conversational Product Advisor | arXiv `2607.21513v1`; http://arxiv.org/abs/2607.21513v1 | arXiv cs.HC, 2026-07-23 | “설명 추가=투명성” 과잉 단순화를 막는 커머스 AI UX 후보입니다. arXiv-only입니다. |
| WATCH | goyounjung | A Closed-Loop Framework for Cross-Cultural Visual Symbol Adaptation of Global Brand Advertising in Mobile Human-Computer Interaction | DOI `10.4018/ijmhci.411213`; https://doi.org/10.4018/ijmhci.411213 | IJMHCI / IGI Global, 2026-05-29 | 글로벌 브랜드 상징의 문화적 오해를 폐루프로 다루는 점이 BX/모바일 HCI에 유용합니다. |
| WATCH | goyounjung | Examining the influence of cultural variations on user interface design and user experience: a systematic review | DOI `10.1007/s10209-026-01365-0`; https://doi.org/10.1007/s10209-026-01365-0 | Universal Access in the Information Society, 2026-07-21 | 문화권별 UI/UX 근거를 체계 검토로 정리한 후보입니다. 최종 선정 시 리뷰 품질 확인 필요. |
| WATCH | goyounjung | A Comparison of Thematic Analysis by Large Language Models and Junior UX Researchers in Early UX Problem Definition | DOI `10.31678/sdc118.6`; https://doi.org/10.31678/sdc118.6 | Design Convergence Study, 2026-06-30 | W30에도 등장한 반복 신호입니다. 주니어 UX 교육/문제정의 품질에 유용하나 동일 후보 반복 노출로 신선도는 낮습니다. |
| WATCH | yuna | AI VTuber 체감 반응성 향상을 위한 지연 은폐 아키텍처 | KCI `ART003363306`; https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003363306 | 한국컴퓨터그래픽스학회논문지 32(3), KCI, 2026 | 실시간 AI 캐릭터 latency UX 후보입니다. 표본/효과 제한을 최종 검증해야 합니다. |
| WATCH | yuna | 웹툰의 영상화를 위한 생성형 AI 기반 제작 플랫폼 | KCI `ART003363302`; https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003363302 | 한국컴퓨터그래픽스학회논문지 32(3), KCI, 2026.07 | 한국형 생성 제작 파이프라인 후보입니다. 제작 시스템 사례로 좋으나 UX/HCI 실증성은 제한적일 수 있습니다. |
| WATCH | yuna | 가상 프로덕션에서의 시각 언어 모델을 이용한 각본 기반 카메라 촬영 자동화 | KCI `ART003363300`; https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003363300 | 한국컴퓨터그래픽스학회논문지 32(3), KCI, 2026 | 시각 제작 온톨로지 후보입니다. 자동화 성능과 디자인 리더십 학습 사이의 연결을 신중히 해야 합니다. |
| WATCH | yuna | 사용자 상호작용을 지원하는 SAM3D 기반 단일 뷰 실내 공간 및 가구 3D 재구성 시스템 | KCI `ART003363297`; https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003363297 | 한국컴퓨터그래픽스학회논문지 32(3), KCI, 2026 | 사용자의 수정 권한과 3D 장면 온톨로지 신호가 있으나 HCI 연구라기보다 시스템 구현 성격이 강할 수 있습니다. |
| WATCH | goyounjung | Reconstructing Publicness in Generative AI-Based Industrial Design | DOI `10.18208/ksdc.2026.32.2.549`; https://doi.org/10.18208/ksdc.2026.32.2.549 | 한국디자인문화학회지 / DBpia, 2026-06-30 | AI 산업디자인의 공공성/책임 렌즈가 좋습니다. 다만 실증보다 개념/담론 성격일 가능성이 있습니다. |
| WATCH | goyounjung | A Study on Identifying Convergence UX Design Components of Gen AI-Based Web Applications Using the Delphi Method | DOI `10.17548/ksaf.2026.06.30.575`; https://doi.org/10.17548/ksaf.2026.06.30.575 | The Korean Society of Science & Art, 2026-06-30 | W28에도 기록된 반복 후보입니다. AI 웹앱 UX 평가 루브릭으로 유용하나 반복/신선도 체크 필요. |
| HOLD | yuna | Design and evaluation model of AIGC multimodal interactive system for user experience optimization | DOI `10.1007/s43926-026-00455-y`; https://doi.org/10.1007/s43926-026-00455-y | Discover Internet of Things / Springer, 2026-07-25 | 멀티모달 시스템 평가 후보이나 HCI 현장성보다 모델/시스템 중심으로 보입니다. |
| HOLD | goyounjung | The Impact of Digitalization on Net Promoter Score (NPS) among Banking Customers in Europe | DOI `10.24818/rej/2026/92/09`; https://doi.org/10.24818/rej/2026/92/09 | The Romanian Economic Journal, 2026-07-28 | UX를 경영 언어로 번역하는 보조 후보입니다. 디자인/AI 직접성은 낮습니다. |
| HOLD | goyounjung | From anthropomorphism to prosocial intention: a PLS-SEM and fsQCA study of virtual influencers | DOI `10.3389/fpsyg.2026.1899105`; https://doi.org/10.3389/fpsyg.2026.1899105 | Frontiers in Psychology, 2026-07-28 | 가상 인플루언서/의인화 후보입니다. 조작적 설득·의존 리스크를 함께 표시해야 합니다. |
| HOLD | goyounjung | Evolutionary Trends and Efficiency Factors of XR Remote Collaboration: Toward an Integrated User Experience (UX) Framework | DOI `10.5392/jkca.2026.26.06.532`; https://doi.org/10.5392/jkca.2026.26.06.532 | 한국콘텐츠학회논문지, 2026-06-30 | XR 협업 문헌분석 후보입니다. 이번 주 핵심 AI/agent UX 흐름과는 연결 강도가 낮습니다. |
| HOLD | goyounjung | A Study on an Adaptive Dark Mode UX Design Framework Considering AI Applicability - Focusing on Case Studies of e-commerce Platforms - | DOI `10.18208/ksdc.2026.32.2.719`; https://doi.org/10.18208/ksdc.2026.32.2.719 | 한국디자인문화학회지, 2026-06-30 | 로컬 UX 프레임워크 후보이나 범위가 다크모드/이커머스에 좁고 최종 best 3 경쟁력은 낮아 보입니다. |
| HOLD | goyounjung | "Is This Not Enough?": Asymmetries in Institutional Accountability and Collective Sensemaking in the Case of Canada's Algorithmic Visa Triage System | DOI `10.1145/3811242.3819106`; https://doi.org/10.1145/3811242.3819106 | ACM SIGCAS/SIGCHI Computing and Sustainable Societies, 2026-07-27 | 알고리즘 책임성 사례로 중요하지만 Chris의 이번 주 논문 3개 학습 패키지에서는 다소 제도정책 중심입니다. |

## 중복/반복 신호
- `A Comparison of Thematic Analysis by Large Language Models and Junior UX Researchers in Early UX Problem Definition`는 `2026-W30` JSONL에도 존재합니다. 이번 주에는 Go Youn-jung 후보로 다시 들어왔으나 풀에는 1회만 유지했습니다. 반복 자체는 디자인교육/UX 리서치 방법론의 가중 신호로 볼 수 있습니다.
- `A Study on Identifying Convergence UX Design Components of Gen AI-Based Web Applications Using the Delphi Method`는 과거 Yuna 후보에 기록된 반복 신호가 있습니다. 이번 주에는 Go Youn-jung 후보로 1회 유지했습니다.
- KCI URL의 `artiId=ART...`는 OpenReview ID가 아니라 KCI article ID입니다. 정규화에서 `KCI ART...`로만 취급합니다.
- Google Research 후보 2개(`ADCanvas`, `Tech Worker Challenges Managing Humanlike GenAI`)는 로컬 로그 기준 DOI가 없습니다. 최종 검증 시 공식 PDF/venue metadata 확인이 필요합니다.

## 리스크 플래그
- **arXiv-only 후보**: `Transparent by Design`, `A Framework of User Experience Principles...`, `Uncertainty Quantification...`는 최종 선정 전 peer-review 상태와 방법론 신뢰도를 확인해야 합니다.
- **모델 성능 → UX 가치 과장 위험**: `WebSTAR`, `Dual-Axis Reward`, `AIGC multimodal`, `ReContraster`, `See2Refine`는 기술 성능을 사용자 경험 품질로 바로 치환하지 않도록 제한을 붙여야 합니다.
- **민감/안전 주제**: `Don’t Click That`, `Lost in Simulation`, `Uncertainty Quantification`는 에이전트 안전·권한·사용자 보호와 관련되어 강점이지만, 상용 제품 적용 주장은 보수적으로 표현해야 합니다.
- **의인화/가상 인플루언서 후보**: `Tech Worker Challenges...`, `From anthropomorphism...`, `AI VTuber...`는 친근함·정서적 유대보다 책임 경계, 의존, 조작 가능성, 브랜드 신뢰를 먼저 검토해야 합니다.
- **한국 후보 접근성**: KCI/DBpia/국내 DOI 후보는 원문 접근 제한이 있을 수 있습니다. 최종 리포트에는 `초록/메타데이터 확인` 또는 `원문 확인` 수준을 명시해야 합니다.

## 09:35 최종 검증 작업에 넘길 권고
- 최종 best 3는 한 주의 coherent learning package로 묶는 것이 좋습니다. 현재 풀에서는 “agentic UX의 안전·평가·협업 거버넌스” 축이 가장 강합니다.
- 단, 최종 3개 중 전부 agent 기술 논문으로만 구성하면 UX/브랜드/디자인 리더십 다양성이 약해질 수 있습니다. `Multiexperience` 또는 `Scaling Agentic UX` 같은 경험/조직 프레임 후보를 함께 검토하면 균형이 좋아집니다.
- 한국 후보는 이번 주 수량은 충분하지만 최종 3 경쟁력은 “로컬 맥락 보강” 성격이 많습니다. 약한 국내 후보로 억지 포함하지 말고, 최종 3에 들어가지 않으면 한국 후보는 “보조 신호는 있었으나 최상위 3에는 미달”로 정직하게 처리하는 편이 안전합니다.
