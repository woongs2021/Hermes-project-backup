# August 대시보드 Bilingual Copy Draft

> **For Hermes:** July planning artifact only. 하지 않는다 implement UI from this document until Chris explicitly asks. Use this as seed copy for a future KR/EN toggle.

**Goal:** 8월 대시보드 제작 전에 주요 탭의 한글/영문 문구 초안을 저장해두고, 나중에 KR/EN 토글 버튼으로 전환 가능한 구조를 준비한다.

**Architecture:** 모든 UI copy는 `ko`와 `en`을 동시에 가진다. React UI에서는 `locale: 'ko' | 'en'` 상태를 두고 같은 content key의 문구만 교체한다. v1에서는 static TypeScript 또는 Markdown frontmatter로 시작하고, 이후 content JSON/Markdown loader와 연결한다.

**Tone:** 따뜻하지만 절제된 운영 대시보드. 과장된 AI 마케팅 문구보다 Chris의 판단, 성장, 리서치, 검증 루프가 조용히 읽히는 문장.

---

## 1. Language Toggle

```ts
type Locale = 'ko' | 'en';

type LocalizedText = {
  ko: string;
  en: string;
};
```

### UI Label

- ko: `KR / EN`
- en: `KR / EN`

### Toggle states

```txt
한국어 보기: KR active / EN inactive
English view: KR inactive / EN active
```

### Helper copy

- ko: `언어를 전환해도 같은 구조와 데이터가 유지됩니다.`
- en: `Switching language keeps the same structure and data.`

---

## 2. Global App Copy

## App Title

- ko: `August 대시보드`
- en: `August 대시보드`

## App Subtitle

- ko: `Chris의 AI 운영, 리서치, 성장, 검증 루프를 한곳에서 보는 로컬 대시보드`
- en: `A local 대시보드 for Chris’s AI operations, research, growth, and validation loops.`

## Local Status Pill

- ko: `Local Draft`
- en: `Local Draft`

## Empty State

- ko: `아직 연결된 데이터가 없습니다. 8월에는 Markdown 데이터와 샘플 기록이 이 영역에 표시됩니다.`
- en: `No data is connected yet. In August, Markdown records and sample entries will appear here.`

---

## 3. Primary Navigation Labels

```ts
const navCopy = {
  metaphorLoops: { ko: 'Metaphor Loops', en: 'Metaphor Loops' },
  overview: { ko: 'Overview', en: 'Overview' },
  team: { ko: 'Team', en: 'Team' },
  obd: { ko: 'OBD', en: 'OBD' },
  research: { ko: 'Research', en: 'Research' },
  muyeolReport: { ko: 'Muyeol Report', en: 'Muyeol Report' },
  devArchitecture: { ko: 'Dev Architecture', en: 'Dev Architecture' },
  chrisResume: { ko: 'Chris Resume', en: 'Chris Resume' },
};
```

---

## 4. Metaphor Loops

## Page Title

- ko: `Youn-jung’s 3 Metaphor Loops`
- en: `Youn-jung’s 3 Metaphor Loops`

## Page Intro

- ko: `Chris의 명령, 리서치, 성장이 하나의 운영 감각으로 이어지는 방식을 세 개의 메타포로 정리합니다.`
- en: `Three metaphors describe how Chris’s commands, research, and growth become one operating system.`

## Command Garden

- ko title: `Command Garden`
- en title: `Command Garden`
- ko summary: `Chris의 의도가 Karina를 통해 작업으로 심기고, Agent Team의 실행과 Muyeol의 검증을 지나 하나의 결과로 자랍니다.`
- en summary: `Chris’s intent is planted through Karina, grows through Agent Team execution and Muyeol’s validation, then returns as one finished result.`
- ko CTA: `팀 루프 보기`
- en CTA: `View team loop`

## Research Constellation

- ko title: `Research Constellation`
- en title: `Research Constellation`
- ko summary: `논문, 자료, 인사이트가 별자리처럼 연결되고, Yuna의 리서치와 Karina의 종합을 거쳐 Chris의 판단 재료가 됩니다.`
- en summary: `Papers, sources, and insights connect like a constellation, becoming decision material through Yuna’s research and Karina’s synthesis.`
- ko CTA: `리서치 보기`
- en CTA: `View research`

## Growth Loom

- ko title: `Growth Loom`
- en title: `Growth Loom`
- ko summary: `OBD 질문, 일간 기록, 주간 보고가 직조물처럼 쌓이며 Chris의 성장 패턴과 다음 행동을 선명하게 만듭니다.`
- en summary: `OBD questions, daily records, and weekly reports weave together to reveal Chris’s growth patterns and next actions.`
- ko CTA: `성장 루프 보기`
- en CTA: `View growth loop`

---

## 5. Overview

## Page Title

- ko: `Operating Overview`
- en: `Operating Overview`

## Page Intro

- ko: `오늘의 Agent Team 운영 상태와 성장·리서치·검증 흐름을 한 화면에서 요약합니다.`
- en: `A one-screen summary of today’s Agent Team operations, growth, research, and validation flow.`

## Section Labels

- ko: `오늘의 운영 상태`
- en: `Today’s Operating Status`

- ko: `핵심 지표`
- en: `Key Metrics`

- ko: `최근 활동`
- en: `Recent Activity`

- ko: `다음 행동`
- en: `Next Actions`

## 요약 Placeholder

- ko: `Karina가 오늘의 루프를 최종 정리하면 이 영역에 Chris-facing summary가 표시됩니다.`
- en: `When Karina synthesizes today’s loop, the Chris-facing summary will appear here.`

---

## 6. Team

## Page Title

- ko: `Karina Hermes Team Orchestration`
- en: `Karina Hermes Team Orchestration`

## Page Intro

- ko: `Chris의 의도가 Karina를 통해 분해되고, 전문 에이전트들이 실행한 뒤, Muyeol의 검증과 Karina의 최종 종합을 거쳐 하나의 결과로 돌아오는 구조입니다.`
- en: `Chris’s intent is decomposed by Karina, executed by specialist agents, validated by Muyeol, and returned as one synthesized result.`

## Loop Label

- ko: `Task Completion Loop`
- en: `Task Completion Loop`

## Role Copy

### Karina

- ko: `조율 리드. Chris의 의도를 작업 단위로 분해하고, 에이전트 실행 결과를 하나의 응답으로 종합합니다.`
- en: `Orchestration lead. Translates Chris’s intent into tasks and synthesizes agent outputs into one response.`

### Faker

- ko: `코딩과 프로토타이핑 담당. 실제 산출물을 구현하고 실행 결과로 검증합니다.`
- en: `Coding and prototyping specialist. Builds working artifacts and verifies them with real execution.`

### Yuna

- ko: `리서치 인텔리전스 담당. 논문, 자료, 외부 지식을 탐색하고 프로젝트 판단 재료로 정리합니다.`
- en: `Research intelligence specialist. Finds papers, sources, and external knowledge, then turns them into project decision material.`

### Son

- ko: `범위와 우선순위 담당. 작업의 수용 기준, 성장 질문, OBD 관점을 구조화합니다.`
- en: `Scope and priority specialist. Structures acceptance criteria, growth questions, and the OBD lens.`

### Muyeol

- ko: `최종 검증 담당. 품질, 보안, 프라이버시, 리스크를 점검하고 수정 권고를 제공합니다.`
- en: `최종 validation specialist. Reviews quality, security, privacy, and risk, then provides recommendations.`

---

## 7. OBD

## Page Title

- ko: `OBD Growth Loop`
- en: `OBD Growth Loop`

## Page Intro

- ko: `일간 질문과 주간 요약을 통해 Chris의 판단, 작업, 성장 신호를 축적합니다.`
- en: `Daily questions and weekly summaries accumulate Chris’s judgment, work, and growth signals.`

## OBD Lens Copy

- ko: `OBD는 디자인 판단을 브랜드, 조직, 가치 교환의 언어로 번역하는 성장 렌즈입니다. One UI와 연결할 때도 억지로 끼워 맞추지 않고, 실제 신호가 있을 때만 연결합니다.`
- en: `OBD is a growth lens that translates design judgment into the language of brand, organization, and value exchange. One UI connections should appear only when the signal genuinely fits.`

## Section Labels

- ko: `일간 성장표`
- en: `Daily Growth Table`

- ko: `주간 성장표`
- en: `Weekly Growth Table`

- ko: `성장 신호`
- en: `Growth Signals`

- ko: `다음 행동`
- en: `Next Actions`

---

## 8. Research

## Page Title

- ko: `Research Loop`
- en: `Research Loop`

## Page Intro

- ko: `논문과 자료를 수집하고, 요약하고, Chris의 프로젝트와 연결되는 인사이트로 변환합니다.`
- en: `Collects papers and sources, summarizes them, and converts them into insights connected to Chris’s projects.`

## Search Placeholder

- ko: `논문 제목, 태그, 주제, 요약을 검색하세요.`
- en: `Search paper titles, tags, topics, and summaries.`

## 상태 Labels

- ko: `수집됨`
- en: `Collected`

- ko: `읽는 중`
- en: `Reading`

- ko: `요약됨`
- en: `Summarized`

- ko: `종합됨`
- en: `Synthesized`

- ko: `적용됨`
- en: `Applied`

---

## 9. Muyeol Report

## Page Title

- ko: `Muyeol Validation Report`
- en: `Muyeol Validation Report`

## Page Intro

- ko: `주간/월간 기준으로 품질, 보안, 프라이버시, 리스크, 권고사항을 확인합니다.`
- en: `Reviews quality, security, privacy, risk, and recommendations on a weekly and monthly basis.`

## Section Labels

- ko: `검증 상태`
- en: `Validation Status`

- ko: `리스크 레벨`
- en: `Risk Level`

- ko: `카테고리`
- en: `Category`

- ko: `권고사항`
- en: `Recommendation`

## Recommendation Copy

- ko: `pass/fail은 보조 지표입니다. 최종 판단은 상태, 리스크 레벨, 카테고리, 권고사항의 조합으로 봅니다.`
- en: `Pass/fail is only a supporting metric. 최종 judgment comes from the combination of status, risk level, category, and recommendation.`

---

## 10. Dev Architecture

## Page Title

- ko: `Dev Architecture`
- en: `Dev Architecture`

## Page Intro

- ko: `앱의 IA, 데이터 레이어, UI 컴포넌트, 구현 로드맵을 이미지가 아닌 실제 UI 하이어라키로 탐색합니다.`
- en: `Explore the app IA, data layer, UI components, and 구현 roadmap as a real UI hierarchy instead of a static image.`

## Panel Labels

- ko: `앱 IA 맵`
- en: `App IA Map`

- ko: `데이터 레이어 하이어라키`
- en: `Data Layer Hierarchy`

- ko: `UI 컴포넌트 구조`
- en: `UI Component Hierarchy`

- ko: `구현 로드맵`
- en: `구현 Roadmap`

## Helper Copy

- ko: `노드를 선택하면 관련 데이터 파일, 화면, 컴포넌트가 함께 표시됩니다.`
- en: `Select a node to see its related data files, screens, and components.`

---

## 11. Chris Resume

## Page Title

- ko: `Chris Resume`
- en: `Chris Resume`

## Page Intro

- ko: `Chris의 이력, 대표 프로젝트, 역량, 디자인/AI UX 철학을 하나의 살아있는 프로필로 정리합니다.`
- en: `A living profile of Chris’s experience, selected projects, skills, and design/AI UX philosophy.`

## Section Labels

- ko: `프로필 요약`
- en: `Profile Summary`

- ko: `경력 타임라인`
- en: `Experience Timeline`

- ko: `대표 프로젝트`
- en: `Selected Projects`

- ko: `역량과 시스템`
- en: `Skills & Systems`

- ko: `작업 철학`
- en: `Working Philosophy`

- ko: `연락 / 내보내기`
- en: `Contact / Export`

## Privacy Copy

- ko: `이 페이지는 Chris가 제공한 공개 가능한 정보만 사용합니다. 비공개 이력과 공개용 export는 분리됩니다.`
- en: `This page uses only 공개 안전 information provided by Chris. Private resume details and public exports remain separate.`

## Placeholder Copy

- ko: `아직 이력 데이터가 연결되지 않았습니다. 7월에는 문구와 구조를 준비하고, 실제 내용은 Chris가 제공한 자료로 채웁니다.`
- en: `Resume data is not connected yet. In July, we prepare the structure and copy; the actual content will be filled with material provided by Chris.`

---

## 12. Future Content File Shape

```ts
type LocalizedCopy = {
  key: string;
  ko: string;
  en: string;
};

type LocalizedSection = {
  id: string;
  title: LocalizedText;
  summary?: LocalizedText;
  body?: LocalizedText;
};
```

Example:

```ts
const overviewCopy = {
  title: {
    ko: 'Operating Overview',
    en: 'Operating Overview',
  },
  intro: {
    ko: '오늘의 Agent Team 운영 상태와 성장·리서치·검증 흐름을 한 화면에서 요약합니다.',
    en: 'A one-screen summary of today’s Agent Team operations, growth, research, and validation flow.',
  },
};
```

---

## 13. 구현 Notes for Later

1. Add a top-level `locale` state in `AppShell`.
2. Store all tab labels and page copy as localized objects.
3. Use stable keys, not raw text, for rendering sections.
4. Keep data language-independent where possible; localize only labels, summaries, and body copy.
5. For resume content, never generate career claims without Chris-provided source material.
6. Add KR/EN toggle before real content migration so every new copy field is bilingual from the start.
