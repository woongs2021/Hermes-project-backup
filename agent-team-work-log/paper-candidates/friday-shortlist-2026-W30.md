# Muyeol Friday 후보-pool prep — 2026-W30

- 작성자: Kim Muyeol
- 작성일: 2026-07-24 KST
- 목적: 09:35 KST 최종 검증/선정을 위한 주간 후보군 정규화 및 리스크 사전 점검
- 입력: `yuna-2026-W30.md`, `goyounjung-2026-W30.md`, `all-research-items.jsonl`
- 범위: 최종 best 3 선정 전 단계입니다. 아래 Top tier는 강한 예비 후보군이며, 사용자-facing 최종 3개 확정이 아닙니다.

## 1. 수집 상태 / 완전성

- 현재 ISO 주차: 2026-W30.
- 주간 후보 수: 총 30개 확인.
  - Yuna lane: 15개 — 2026-07-20~2026-07-24, 매일 3개.
  - Go Youn-jung lane: 15개 — 2026-07-20~2026-07-24, 매일 3개.
- `all-research-items.jsonl`에도 2026-W30 항목 총 30개가 존재하며, 주간 Markdown 파일과 수량상 일치합니다.
- 현재 주 파일이 충분히 완전하므로 이전 주 파일은 후보 보강용으로 사용하지 않았습니다.

## 2. 중복 정규화 메모

확인 기준: 제목, DOI/arXiv/ACM/PoPETs ID, URL, duplicate_key, 명백한 동일 논문 변형.

- 명백한 동일 논문 중복: 발견하지 못했습니다.
- arXiv/venue variant 병합 필요 항목: 이번 주 후보에서는 발견하지 못했습니다.
- 주제상 근접하지만 별도 논문으로 유지할 항목:
  - 모바일/GUI 에이전트 안전·평가: `DAC-Bench`, `SeerGuard`는 모두 모바일 GUI agent를 다루지만 각각 benchmark/evaluation과 safety/world-model prediction으로 목적이 달라 별도 유지합니다.
  - AI 신뢰·검증 멘탈모델: `U-Lens`, `Beliefs and Misconceptions around Integrated Conversational AI`, `Personalizing Agent Privacy Decisions...`는 모두 신뢰·검증·개인정보 문제를 다루지만 UX 불확실성 관리, 통합 CUI 멘탈모델, 프라이버시 의사결정 거버넌스로 구분됩니다.
  - AI×브랜드 의미/비주얼 비평: Genesis 전면부 디자인 의미론 논문과 `Di전송됨angling Vision from Meaning`은 모두 AI 생성 디자인 비평과 브랜드/문화 의미를 다루지만 DOI와 프레임이 다른 별도 항목입니다.

## 3. 후보군 정규화 표

점수는 Chris 성장 관련성, OBD/비즈니스 디자인 학습가치, evidence/source 접근성, novelty, 실무적 함의, 과장/리스크를 함께 본 5점 척도입니다. 일일 initial score를 참고하되 Muyeol 관점으로 가볍게 재조정했습니다.

| # | Lane | 정규화 제목 | ID / URL | Venue/date | Access | Muyeol prep score | 판단 메모 |
|---:|---|---|---|---|---|---:|---|
| 1 | Yuna | DAC-Bench: A Decision-Aware Benchmark for Compositional Mobile GUI Tasks | https://aclanthology.org/2026.acl-long.2064/ | ACL 2026 Long, Jul 2026 | full via ACL | 4.8 | 모바일 에이전트 평가를 분기·조건·실패 회복으로 바꾸는 강한 AI UX 품질 언어. |
| 2 | Yuna | Personalizing Agent Privacy Decisions via Logical Entailment | https://petsymposium.org/popets/2026/popets-2026-0087.php / DOI:10.56553/popets-2026-0087 | PoPETs 2026, Jul 2026 | full/PDF | 4.9 | 개인 에이전트 개인정보 결정을 설명 가능한 논리 구조로 다루는 매우 강한 신뢰·거버넌스 후보. 민감데이터 주의 필요. |
| 3 | Yuna | SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction | https://arxiv.org/abs/2607.15550 / arXiv:2607.15550 | arXiv cs.AI/cs.HC, 2026-07-17 | full via arXiv | 4.8 | 실행 전 위험 예측·차단이라는 에이전트 안전 UX 핵심. 다만 arXiv 단독이라 검증 강도는 venue 논문보다 낮게 표시 필요. |
| 4 | Go Youn-jung | A designszemlélet megjelenése a vállalati menedzsmentfolyamatokban | https://doi.org/10.14267/veztud.2026.07-08.01 | Vezetéstudomány / Budapest Management Review, 2026-07-14 | abstract/metadata | 4.8 | 디자인을 조직 의사결정·성숙도·경쟁력 언어로 번역하는 design-management 강후보. 언어/지역 맥락 차이 주의. |
| 5 | Go Youn-jung | Reimagining infrastructure for video game accessibility: exploring Access Profiles with players with disabilities and game designer-developers | https://doi.org/10.3389/fcomp.2026.1823366 | Frontiers in Computer Science, 2026-07-20 | full/OA | 4.8 | 접근성을 기능이 아니라 생태계 인프라·운영 품질로 확장. 플랫폼 리더십 관점에서 강함. |
| 6 | Go Youn-jung | Algorithmic opacity and the distortion of B2B signalling: evidence from digital marketing client-agency services | https://doi.org/10.1108/jbim-04-2025-0328 | Journal of Business & Industrial Marketing, 2026-07-24 | abstract/metadata, likely paywalled | 4.7 | 플랫폼/AI 시대 품질·책임 신호 왜곡을 B2B 신뢰로 설명. 비즈니스 디자인 강점, full text 접근 제한 주의. |
| 7 | Yuna | 브랜드 언어 관점에서 본 AI 생성 자동차 전면부 디자인의 의미론적 일관성 진단 - Genesis 콘셉트카를 중심으로 - | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12892343 / DOI:10.17548/ksaf.2026.06.30.235 | 한국과학예술융합학회/DBpia, 2026-06 | snippet/metadata | 4.7 | AI 생성 비주얼을 브랜드 온톨로지·의미 일관성으로 검토하는 한국 맥락 강후보. DBpia full access 제한. |
| 8 | Yuna | Beliefs and Misconceptions around Integrated Conversational AI | https://doi.org/10.1145/3816046.3816203 | ACM CUI 2026, 2026-07-21 | abstract/metadata/OA signal | 4.7 | 출처 표시가 검증 생략을 만들 수 있다는 실무적 HCI 리스크가 선명함. |
| 9 | Go Youn-jung | Consumer responses to AI-designed virtual luxury products: a double-edged sword for perceived brand innovativeness and authenticity | https://doi.org/10.1108/apjml-03-2026-0543 | Asia Pacific Journal of Marketing and Logistics, 2026-07-20 | abstract/metadata, closed | 4.6 | AI 제작물의 혁신성-진정성 tradeoff. 브랜드/BX 판단에 유용하나 paywall/카테고리 일반화 주의. |
| 10 | Yuna | SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery | https://arxiv.org/abs/2607.16038 / arXiv:2607.16038 | arXiv cs.HC/cs.AI, 2026-07-17 | full via arXiv | 4.6 | 객체·관계·결정 로그를 보존하는 AI workbench 관점이 OBD에 적합. arXiv 단독. |
| 11 | Yuna | U-Lens: Supporting User Uncertainty Management in Long-Form LLM Responses | https://arxiv.org/abs/2607.10604 / arXiv:2607.10604 | arXiv cs.HC, 2026-07-12 | full via arXiv | 4.6 | LLM 답변 검증/판단 UX의 좋은 후보. 최종 3에서는 유사 신뢰 후보와 비교 필요. |
| 12 | Go Youn-jung | Beyond the screen: craft as inquiry in human-computer interaction | https://doi.org/10.3389/fcomp.2026.1830238 | Frontiers in Computer Science/HCI, 2026-07-22 | full/OA | 4.6 | 화면/효율 중심 HCI를 재료성·감각·비판적 제작으로 넓히는 교육 가치. AI 주간 테마와 결합력은 다소 낮음. |
| 13 | Yuna | Di전송됨angling Vision from Meaning: A Neuro-Symbolic Framework for Semiotically Grounded Design Criticism | https://doi.org/10.3837/tiis.2026.03.007 | KSII Transactions on Internet and Information Systems, 2026-03-31 | abstract/OA signal | 4.6 | AI 비주얼 비평의 semantic smearing 문제는 Chris OBD/브랜드 의미론에 강함. 날짜가 오래됨. |
| 14 | Yuna | TAMA: A Human-AI Collaborative Thematic Analysis Framework Using Multi-Agent LLMs for Clinical Interviews | https://doi.org/10.1145/3828752 | ACM Transactions on Computing for Healthcare, 2026-07-06 | abstract/Crossref, ACM 403 | 4.5 | 리서치 워크플로·역할 분담·검토 루프에 유익. 임상 인터뷰라 민감영역 및 일반화 주의. |
| 15 | Go Youn-jung | Human-centred AI governance and sustainability capability development in higher education: the AIMS AI-Human Framework | https://doi.org/10.47556/j.wjemsd.22.5.2026.5 | WJEMSD, 2026-07-20 | abstract/metadata, closed | 4.5 | AI governance/education 조직 역량 프레임. 리뷰 논문이나 full text 접근 제한. |
| 16 | Yuna | Conversational Tactile Data Interfaces... | https://arxiv.org/abs/2607.14588 | arXiv cs.HC, 2026-07-16 | full via arXiv | 4.5 | 멀티모달/접근성 오케스트레이션 관점. 좋은 reserve 후보. |
| 17 | Go Youn-jung | Accessibility in UX Design: The 필요 for Workflow Support and Accessibility Features in Design Tools | https://doi.org/10.1007/978-3-032-31308-9_64 | Springer LNCS/HCII, 2026-07-17 | abstract/snippet | 4.5 | 접근성의 툴링/워크플로 내재화. Reimagining accessibility와 비교 시 후순위. |
| 18 | Go Youn-jung | Influenced by Design—How Design Cues Can Shape Sustainable Design and Evaluation Choices | https://doi.org/10.3390/su18147256 | Sustainability, 2026-07-16 | abstract; publisher 403 | 4.5 | 가치 cue와 선택 구조 관계. 브랜드/지속가능성 함의 좋으나 venue/접근 제한 고려. |
| 19 | Yuna | OctoTools: A Multi-Agent Framework with Extensible Tools for Complex Reasoning | https://aclanthology.org/2026.acl-long.1/ | ACL 2026 Long, Jul 2026 | full via ACL | 4.4 | 에이전트 아키텍처 이해에는 좋으나 Chris 성장 관점에서는 GUI/프라이버시/UX 논문보다 기술 중심. |
| 20 | Yuna | Visualization Autocomplete: Visualization Authoring via Stepwise Design Recommendations | https://arxiv.org/abs/2607.15608 | arXiv cs.HC, 2026-07-17 | full via arXiv | 4.4 | 단계별 추천형 창작 도구 관점. 후보군 내 유사 workbench/agent 후보와 비교 필요. |
| 21 | Go Youn-jung | Navigating Transitions: Envisioning Conversational User Interfaces to Support International Students | https://doi.org/10.1145/3816046.3816271 | ACM CUI 2026, 2026-07-21 | abstract/metadata | 4.4 | 전환기 사용자 지원·서비스 책임. 민감/취약 사용자 해석 과장 주의. |
| 22 | Go Youn-jung | Platform Architecture and Consumer Motivation... | https://doi.org/10.33422/icnmbe.v4i1.1887 | ICNMBE proceedings, 2026-07-20 | full/OA metadata | 4.3 | 브랜드 커뮤니티 구조 신호. venue 신뢰도는 ACM/PoPETs보다 약함. |
| 23 | Yuna | 통합 디자인교육을 위한 인지적 오케스트레이션 | https://doi.org/10.25111/jcd.2026.95.19 | 커뮤니케이션 디자인학연구, 2026-04-01 | abstract/metadata | 4.3 | 한국 디자인교육 언어가 좋으나 추상 개념 중심 가능성. 최종에서는 근거 강도 확인 필요. |
| 24 | Go Youn-jung | Effects of Visual Expression Elements in Natural Cosmetics Packaging Design... | https://doi.org/10.29056/jdaem.2026.06.04 | JDAEM, 2026-06-26 | abstract/metadata | 4.2 | BX/패키징 실무 연결은 가능하나 AI/OBD 주간 핵심성과는 낮음. |
| 25 | Go Youn-jung | Cross-cultural analysis of kimchi perceptions... | https://doi.org/10.1186/s42779-026-00324-7 | Journal of Ethnic Foods, 2026-07-21 | full/OA | 4.2 | 로컬 문화 브랜딩에는 유익. 이번 주 AI/UX/design leadership coherent package와는 결합 약함. |
| 26 | Yuna | 패션 소비자의 생성형 AI 기반 챗봇 사용경험에 관한 연구 | https://doi.org/10.5850/JKSCT.2026.50.1.121 | JKSCT, 2026-02-30 as listed | full via journal | 4.1 | 브랜드 챗봇 소비자 경험. 날짜 표기 `2026-02-30`은 원천 오류 가능성이 커서 확인 필요. |
| 27 | Go Youn-jung | Game Industry Trends Analyzed Through Global Game Exhibition G-STAR | https://doi.org/10.56977/jicce.2026.24.2.175 | JICCE, 2026-06-30 | full/OA | 4.1 | 한국 산업/시장 신호로는 유익하나 paper best-3 근거력은 중간. |
| 28 | Go Youn-jung | Analysis of Brand Trust and Consumer Switching Behavior according to UI Design of Airline Ticket Reservation Platform | https://doi.org/10.46248/kidrs.2026.2.1136 | Design Research/KIDRS, 2026-06-30 | metadata only | 4.0 | 한국 UI/BX 맥락이나 abstract/full text 미확인으로 blocker. |
| 29 | Yuna | AI-Assisted Analysis of PowerPoint Slides... | https://doi.org/10.1177/07356331261468611 / https://openalex.org/W7168759378 | Journal of Educational Computing Research/SAGE, 2026-07-21 | metadata/OpenAlex; DOI 403 | 4.0 | 교육 아티팩트 감사 아이디어는 흥미롭지만 DOI/접근성 이슈와 주제 주변성. |
| 30 | Go Youn-jung | The Effect of Short-form Platform Types on User Reuse Intention... | https://doi.org/10.35174/jkci.2026.06.26.2.155 | Journal of Korea Culture Industry, 2026-06-30 | abstract/metadata | 3.9 | SNS 감정/재이용 의도 연구. Son의 SNS 팁 보조에는 가능하나 최종 3 후보로는 약함. |

## 4. Top-tier preliminary 후보 pool — 최종선정 전 예비 강후보

아래는 09:35 검증에서 우선 비교할 예비 후보입니다. 최종 best 3은 coherence, source confidence, 과장 리스크, 한국/비한국 균형을 재평가한 뒤 확정하십시오.

1. **Personalizing Agent Privacy Decisions via Logical Entailment** — PoPETs 2026, DOI:10.56553/popets-2026-0087  
   - 강점: 개인 에이전트의 데이터 공유/프라이버시 의사결정을 제품 신뢰·거버넌스 UX로 연결합니다. Chris가 AI 개인화의 안전한 판단 구조를 배울 수 있는 주간 최강 후보입니다.
   - 리스크: 민감한 개인정보/사용자 선호 주제이므로 “논리 결합이 완전한 해결책”처럼 과장하면 안 됩니다.

2. **DAC-Bench: A Decision-Aware Benchmark for Compositional Mobile GUI Tasks** — ACL 2026 Long  
   - 강점: 모바일 GUI 에이전트를 짧은 자동화 데모가 아니라 조건·분기·장기 실행 실패 회복으로 평가해야 한다는 명확한 품질 언어를 줍니다.
   - 리스크: benchmark 결과를 특정 제품 성능 예측으로 직접 일반화하지 마십시오.

3. **SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction** — arXiv:2607.15550  
   - 강점: `실행 전 결과 예측/위험 차단`은 autonomous mobile agent UX의 핵심 guardrail입니다. DAC-Bench와 coherent pair가 됩니다.
   - 리스크: arXiv preprint라 독립 검증/peer-review 강도는 낮습니다. 최종 3에 넣을 경우 이를 명시하십시오.

4. **A designszemlélet megjelenése a vállalati menedzsmentfolyamatokban** — DOI:10.14267/veztud.2026.07-08.01  
   - 강점: AI 중심 후보들 사이에서 Chris의 디자인 리더십·경영 언어 성장을 담당할 수 있는 균형 후보입니다.
   - 리스크: 헝가리어/지역 경영 맥락이라 세부 사례 일반화에는 주의가 필요합니다.

5. **Reimagining infrastructure for video game accessibility** — DOI:10.3389/fcomp.2026.1823366  
   - 강점: 접근성을 기능 옵션이 아니라 플랫폼 인프라·운영 품질로 보는 대형 서비스 리더십 후보입니다.
   - 리스크: 게임 접근성 맥락을 모바일 OS/일반 플랫폼에 그대로 이전하지 말고 구조적 원리만 가져가야 합니다.

6. **브랜드 언어 관점에서 본 AI 생성 자동차 전면부 디자인의 의미론적 일관성 진단** — DOI:10.17548/ksaf.2026.06.30.235  
   - 강점: 한국 AI×브랜드 의미론 후보 중 Chris의 BX/OBD 성장 관련성이 가장 높습니다.
   - 리스크: DBpia snippet/metadata 수준이면 최종 report에서 접근 신뢰도를 낮게 표시해야 합니다.

7. **Beliefs and Misconceptions around Integrated Conversational AI** — DOI:10.1145/3816046.3816203  
   - 강점: 출처/검증 UI가 신뢰를 높이면서도 실제 검증 생략을 만들 수 있다는 좋은 리스크 교훈입니다.
   - 리스크: CUI/브라우저 통합 맥락이므로 일반 LLM UX 전반으로 확장 시 조심해야 합니다.

8. **Algorithmic opacity and the distortion of B2B signalling** — DOI:10.1108/jbim-04-2025-0328  
   - 강점: 디자인/마케팅 서비스의 품질 신호와 책임 구조를 B2B 신뢰로 다루어 OBD/business design에 좋습니다.
   - 리스크: full text likely paywalled라 최종 3에는 abstract-only confidence로 표시해야 합니다.

## 5. Risk flags / overclaim cautions

- **민감 주제**: 프라이버시, 개인화 에이전트, 임상 인터뷰, 취약 사용자/접근성, 유학생 전환기 지원은 사용자 데이터·취약성·의존성 리스크를 포함합니다. 보고서에서는 benefit만 말하지 말고 책임 경계와 인간 감독을 함께 명시해야 합니다.
- **arXiv 단독 후보**: `SeerGuard`, `SciForge`, `U-Lens`, `Conversational Tactile Data Interfaces`, `Visualization Autocomplete`는 강한 아이디어일 수 있으나 peer-review 상태가 확인되지 않았습니다. 최종 선정 시 source-access confidence에 `preprint/full read 가능, peer-review 미확인`을 표시하십시오.
- **Paywall/metadata-only 후보**: Emerald, SAGE, 일부 Springer/ACM/국내 DOI 후보는 full text 접근이 제한되거나 자동 fetch가 403이었습니다. abstract-only 항목은 claim을 좁게 유지해야 합니다.
- **한국 후보 주의**: 한국 맥락 후보가 다수 있으나 최신성·full access·근거 강도가 고르지 않습니다. 한국 후보를 넣어야 한다는 이유만으로 약한 항목을 최종 3에 넣지 않는 편이 안전합니다.
- **날짜 이상치**: `패션 소비자의 생성형 AI 기반 챗봇 사용경험...`은 원천 로그에 `2026-02-30`으로 기재되어 있습니다. 실제 날짜 확인 전에는 최종 report에서 날짜를 그대로 단정하지 마십시오.
- **One UI 강제 연결 금지**: 이번 주 strongest theme은 “자율 에이전트가 판단·검증·안전을 어떻게 인터페이스 품질로 바꾸는가”와 “디자인 리더십이 품질·책임·의미 신호를 어떻게 조직 언어로 번역하는가”입니다. One UI 적용은 downstream reflection으로만 두는 것이 적절합니다.

## 6. Missing-source blockers for 09:35 validation

우선 검증 필요 항목:

- `브랜드 언어 관점에서 본 AI 생성 자동차 전면부 디자인...`: DBpia full text 접근 불가/스니펫 중심이면 최종 선정 시 근거 confidence를 낮춰야 합니다.
- `Algorithmic opacity...`: Emerald full text likely paywalled. abstract-only로는 방법·표본·한계 확인이 제한됩니다.
- `A designszemlélet...`: DOI/abstract는 있으나 언어 장벽 및 세부 방법 확인 제한. 최종 보고서에서는 “design-management 사례/인터뷰 기반” 정도로 보수적 기술이 안전합니다.
- `Beliefs and Misconceptions...`: ACM DOI metadata/OA signal은 있으나, full 논문 본문 접근 상태를 09:35에서 한 번 더 확인하면 좋습니다.
- `패션 소비자의 생성형 AI 기반 챗봇...`: 날짜 오류 가능성 확인 없이는 제외 또는 낮은 순위 유지 권고.

## 7. 09:35 최종-selection guidance

- 강한 coherent package 후보 A: **Privacy governance + Mobile agent evaluation + Mobile agent safety**
  - `Personalizing Agent Privacy Decisions...` + `DAC-Bench` + `SeerGuard`
  - 장점: 매우 일관된 AI-agent trust/safety learning package.
  - 약점: 디자인/브랜드/리더십 lane이 약하고, SeerGuard는 arXiv preprint.

- 균형 package 후보 B: **Agent privacy/safety + Design-management/OBD + Korean AI-brand semantics**
  - `Personalizing Agent Privacy Decisions...` + `DAC-Bench` 또는 `SeerGuard` + `브랜드 언어 관점...` 또는 `A designszemlélet...`
  - 장점: Chris 성장 폭이 넓고 Yuna/Go Youn-jung lane 균형이 좋음.
  - 약점: 한국/디자인관리 후보의 full access confidence가 낮을 수 있음.

- 플랫폼 리더십 package 후보 C: **Agent safety + Accessibility infrastructure + B2B trust signalling**
  - `SeerGuard` 또는 `DAC-Bench` + `Reimagining infrastructure...` + `Algorithmic opacity...`
  - 장점: 제품 운영·책임·신뢰 신호를 넓게 학습.
  - 약점: AI/LLM 직접성은 package A보다 낮음.

Muyeol 사전 권고: 09:35에서는 우선 package A와 B를 비교하십시오. Chris에게 이번 주 가장 선명하게 남길 질문이 “에이전트가 자율적일수록 어떤 판단 구조가 사용자에게 보여야 하는가?”라면 package A가 강합니다. “AI 시대 디자인 리더가 기술 신뢰와 브랜드/조직 의미를 함께 배워야 한다”까지 넓히려면 package B가 더 균형 잡혀 있습니다.
