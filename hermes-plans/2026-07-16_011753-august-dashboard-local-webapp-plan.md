# August 대시보드 Local Webapp 구현 Plan

> **For Hermes:** 이 문서는 아직 구현하지 않는 계획 문서입니다. Chris가 승인하기 전까지 코딩을 시작하지 않습니다.

**Goal:** 8월에 Chris가 로컬호스트에서 확인할 수 있는 반응형 운영 대시보드 웹앱을 만든다.

**Architecture:** Markdown/JSON 기반 로컬 데이터 레이어를 먼저 정의하고, Vite React 또는 Next.js 기반 UI에서 Metaphor Loops, Overview, Team, OBD, Research, Muyeol Report, Dev Architecture, Chris Resume 탭을 렌더링한다. Dev Architecture 탭은 이미지가 아니라 실제 UI 컴포넌트로 IA와 데이터 레이어 하이어라키를 탐색하는 화면이다. Chris Resume 탭은 Chris의 이력, 프로젝트, 역량, 작업 철학을 대시보드 내부에서 정리해 보여주는 마지막 페이지다. 모든 주요 UI copy는 `ko`/`en`을 동시에 가진 localized copy 구조로 저장해, 나중에 KR/EN 토글 버튼으로 전환 가능하게 한다. 초기 버전은 배포 없이 로컬호스트에서 샘플 데이터로 확인하고, 이후 실제 OBD/리서치/보고 데이터와 연결한다.

**Tech Stack:** Next.js 또는 Vite React, TypeScript, Markdown/MDX 또는 gray-matter, lightweight chart library, local file-based data.

---

## 1. 제품 방향

8월 대시보드는 Chris의 AI 운영 체계를 시각화하는 로컬 웹앱이다.

핵심 루프:

```txt
Chris → Karina → Agent Team → Muyeol Validation → Karina Synthesis → Chris
```

주요 화면:

1. Metaphor Loops: Chris의 운영 세계관과 3개 메타포 루프
2. Overview: 전체 운영 상태 요약
3. Team: Karina Hermes Team 오케스트레이션 설명
4. OBD: OBD 루프 개요, 일간/주간 성장표
5. Research: 리서치 루프 및 논문 검색
6. Muyeol Report: Muyeol 주간/월간 보고 수치와 그래프
7. Dev Architecture: IA, 데이터 레이어, 파일/콘텐츠 하이어라키, 향후 구현 구조를 UI로 탐색하는 개발자 관점 구성도
8. Chris Resume: Chris의 이력, 대표 프로젝트, 역량, 연구/디자인 방향성을 보여주는 마지막 페이지

---

## 2. 현재 가정

- 첫 버전은 로컬호스트에서만 확인한다.
- 배포, 로그인, 권한 관리, 원격 DB는 v1 범위에서 제외한다.
- 데이터는 처음에는 샘플 Markdown/JSON으로 시작한다.
- 7월 중 주요 탭의 한글/영문 문구 초안을 함께 저장해두고, 8월 구현 시 KR/EN 토글이 가능한 copy 구조로 연결한다.
- bilingual copy 초안은 `/opt/data/.hermes/plans/2026-07-22_072003-august-대시보드-bilingual-copy-draft.md`에 저장한다.
- 실제 OBD 정의와 Muyeol 지표는 Chris가 추후 확정한다.
- UI는 Chris의 디자인 방향성에 맞춰 따뜻한 오프화이트 캔버스, 절제된 카드, 명확한 정보 계층을 사용한다.

---

## 3. 권장 프로젝트 구조

아직 생성하지 않을 파일 구조 초안:

```txt
august-dashboard/
├─ app/ 또는 src/
│  ├─ page.tsx
│  ├─ layout.tsx
│  ├─ components/
│  │  ├─ AppShell.tsx
│  │  ├─ Header.tsx
│  │  ├─ MobileNav.tsx
│  │  ├─ MetricCard.tsx
│  │  ├─ LoopDiagram.tsx
│  │  ├─ AgentCard.tsx
│  │  ├─ GrowthTable.tsx
│  │  ├─ PaperCard.tsx
│  │  ├─ ReportChart.tsx
│  │  ├─ ArchitectureTree.tsx
│  │  ├─ DataLayerMap.tsx
│  │  └─ HierarchyNode.tsx
│  ├─ features/
│  │  ├─ metaphor-loops/
│  │  ├─ overview/
│  │  ├─ team/
│  │  ├─ obd/
│  │  ├─ research/
│  │  ├─ reports/
│  │  ├─ dev-architecture/
│  │  └─ chris-resume/
│  ├─ lib/
│  │  ├─ data.ts
│  │  ├─ markdown.ts
│  │  └─ search.ts
│  └─ styles/
│     └─ tokens.css
├─ content/
│  ├─ metaphor-loops/
│  │  ├─ command-garden.md
│  │  ├─ research-constellation.md
│  │  └─ growth-loom.md
│  ├─ overview/
│  │  ├─ today.md
│  │  └─ weekly-summary.md
│  ├─ team/
│  │  ├─ agents.md
│  │  └─ orchestration.md
│  ├─ obd/
│  │  ├─ daily/
│  │  └─ weekly/
│  ├─ research/
│  │  ├─ papers/
│  │  └─ notes/
│  ├─ reports/
│  │  └─ muyeol/
│  │     ├─ weekly/
│  │     └─ monthly/
│  └─ dev-architecture/
│     ├─ ia-map.md
│     ├─ data-layer.md
│     └─ implementation-map.md
│  └─ chris-resume/
│     ├─ profile.md
│     ├─ experience.md
│     ├─ projects.md
│     ├─ skills.md
│     └─ philosophy.md
├─ public/
├─ package.json
└─ README.md
```

---

## 4. Phase Plan

## Phase 0: Scope 확인ation

**Objective:** 구현 전 데이터 의미와 v1 범위를 확정한다.

**Tasks:**

1. OBD의 정확한 의미 확정
   - O, B, D가 각각 무엇인지 정의
   - 일간 기록 필드 정의
   - 주간 요약 필드 정의
   - 성장 점수 기준 정의

2. 리서치 논문 입력 방식 결정
   - 이 결정은 Research 탭이 단순 목록인지, 검색 가능한 지식 베이스인지 결정한다.
   - v1 기본값: 사람이 읽기 좋고 llm-wiki 스타일로 확장 가능한 Markdown 입력
   - v2 후보: Markdown + JSON index로 검색 성능과 구조화 보강
   - v3 후보: Zotero/BibTeX/CSV export 또는 자동 수집 연동
   - 초기에는 CSV/BibTeX/Zotero를 직접 연동하지 않고, 추후 import/export 대상으로 남긴다.

3. Muyeol 리포트 지표 결정
   - 단순 pass/fail 중심이 아니라 “검증 상태 + 리스크 레벨 + 카테고리 + 권고사항” 중심으로 설계한다.
   - validation status: pass, needs-fix, recheck-needed, deferred
   - risk level: low, medium, high, critical
   - category: UX, security, privacy, reliability, data-quality, product-logic
   - recommendation: fix-now, watch, accept-risk, revisit-later
   - pass/fail은 보조 집계 지표로만 사용한다.

4. 디자인 톤 확정
   - Chris의 기존 디자인 시스템 사용 여부 확인
   - 카드 밀도, 차트 스타일, 정보 우선순위 결정

**Acceptance Criteria:**

- v1에서 반드시 보여줄 화면과 제외할 기능이 정해진다.
- 데이터 필드 초안이 확정된다.
- 구현 시작 전에 Chris가 방향을 승인한다.

---

## Phase 1: Local UI Skeleton

**Objective:** 로컬호스트에서 반응형 웹앱의 기본 탭과 레이아웃을 확인한다.

**Likely 파일:**

- Create: `package.json`
- Create: `src/main.tsx` 또는 `app/page.tsx`
- Create: `src/components/AppShell.tsx`
- Create: `src/components/Header.tsx`
- Create: `src/components/MobileNav.tsx`
- Create: `src/styles/토큰.css`

**Tasks:**

1. 프로젝트 생성
   - Next.js 또는 Vite React 중 선택
   - TypeScript 사용
   - 로컬 실행 명령 준비

2. 앱 셸 구현
   - 상단 헤더
   - 데스크톱 탭 내비게이션
   - 모바일 하단 탭 내비게이션
   - 현재 선택 탭 상태

3. 빈 화면 8개 연결
   - Metaphor Loops
   - Overview
   - Team
   - OBD
   - Research
   - Muyeol Report
   - Dev Architecture
   - Chris Resume

4. 반응형 레이아웃 확인
   - 데스크톱: 넓은 카드 그리드
   - 태블릿: 2열
   - 모바일: 1열 + 하단 탭

**Validation:**

- `npm run dev` 또는 `pnpm dev` 실행
- `http://localhost:3000` 또는 `http://localhost:5173` 접속
- 8개 탭 전환 확인
- 모바일 뷰포트에서 내비게이션 깨짐 없는지 확인

---

## Phase 2: Static Sample Data Layer

**Objective:** 실제 데이터 연결 전, 샘플 데이터로 UI 구조를 검증한다.

**Likely 파일:**

- Create: `src/data/sampleMetaphorLoops.ts`
- Create: `src/data/sampleOverview.ts`
- Create: `src/data/sampleTeam.ts`
- Create: `src/data/sampleObd.ts`
- Create: `src/data/sampleResearch.ts`
- Create: `src/data/sampleReports.ts`
- Create: `src/data/sampleDevArchitecture.ts`
- Create: `src/data/sampleChrisResume.ts`
- Create: `src/types/대시보드.ts`

**Tasks:**

1. TypeScript 타입 정의
   - `Agent`
   - `ObdDailyEntry`
   - `ObdWeeklyEntry`
   - `ResearchPaper`
   - `MuyeolWeeklyReport`
   - `MuyeolMonthlyReport`
   - `ArchitectureNode`
   - `DataLayerNode`
   - `ResumeProfile`
   - `ResumeProject`
   - `ResumeExperience`

2. 샘플 데이터 작성
   - 팀원 역할 데이터
   - OBD 일간/주간 샘플
   - 논문 카드 샘플
   - Muyeol 보고 샘플
   - Dev Architecture용 IA / data layer / 구현 hierarchy 샘플
   - Chris Resume용 profile / experience / projects / skills / philosophy 샘플

3. Home 화면에 메트릭 카드 연결
   - OBD daily score
   - research item count
   - validation status count
   - high/critical risk count
   - 검토 대기 decisions

**Validation:**

- 각 화면에서 샘플 데이터가 표시된다.
- TypeScript 에러가 없다.
- 데이터가 없는 경우 empty state가 표시된다.

---

## Phase 3: Screen-by-Screen UI Build

**Objective:** 8개 주요 화면을 실제 사용 가능한 수준의 정적 UI로 만든다.

### 3.1 Metaphor Loops

**Components:**

- `MetaphorLoopBoard`
- `MetaphorLoopCard`
- `LoopEntryLinks`

**Validation:** 첫 화면에서 Command Garden / Research Constellation / Growth Loom의 의미와 다음 진입 탭이 명확히 보인다.

### 3.2 Overview

**Components:**

- `HeroSummary`
- `OperatingLoopOverview`
- `MetricCardGrid`
- `RecentActivityList`
- `QuickActions`

**Validation:** Chris가 하루 운영 상태를 한 화면에서 파악할 수 있다.

### 3.3 Team

**Components:**

- `LoopDiagram`
- `AgentCardGrid`
- `ResponsibilityMatrix`
- `HandoffLog`

**Validation:** Chris → Karina → Agent Team → Muyeol → Karina → Chris 루프가 명확히 보인다.

### 3.4 OBD

**Components:**

- `ObdOverview`
- `DailyGrowthTable`
- `WeeklyGrowthTable`
- `GrowthChartPlaceholder`
- `ObdNotes`

**Validation:** 일간/주간 기록이 표로 표시되고 OBD 정의 변경에 유연하다.

### 3.5 Research

**Components:**

- `ResearchLoopOverview`
- `PaperSearchInput`
- `ResearchFilters`
- `PaperCardGrid`
- `ResearchNotesPanel`

**Validation:** 논문 제목, 태그, 요약 기준 검색이 가능하다.

### 3.6 Muyeol Report

**Components:**

- `ReportOverview`
- `WeeklyReportPanel`
- `MonthlyReportPanel`
- `ValidationMetricGrid`
- `RiskChartPlaceholder`

**Validation:** 주간/월간 QA 상태와 리스크 수치가 표시된다.

### 3.7 Dev Architecture

**Purpose:** 이미지가 아니라 실제 UI 탭으로, 현재 IA와 데이터 레이어/콘텐츠 폴더/구현 컴포넌트의 하이어라키를 한 화면에서 탐색한다. Chris가 지금 Markdown으로 보는 IA를 웹앱 내부의 인터랙티브 구성도로 확인할 수 있게 한다.

**Components:**

- `ArchitectureOverview`
- `ArchitectureTree`
- `DataLayerMap`
- `ContentHierarchyPanel`
- `구현MapPanel`
- `SchemaPreviewCard`

**Information Architecture:**

```txt
Dev Architecture
├─ App IA Map
│  ├─ Metaphor Loops
│  ├─ Overview
│  ├─ Team
│  ├─ OBD
│  ├─ Research
│  ├─ Muyeol Report
│  └─ Dev Architecture
│
├─ Data Layer Hierarchy
│  ├─ content/metaphor-loops
│  ├─ content/overview
│  ├─ content/team
│  ├─ content/obd/daily + weekly
│  ├─ content/research/papers + notes + index
│  ├─ content/reports/muyeol/weekly + monthly
│  └─ content/dev-architecture
│
├─ UI Component Hierarchy
│  ├─ AppShell / Header / Nav
│  ├─ shared cards / tables / panels
│  ├─ feature pages
│  └─ chart / search / hierarchy components
│
└─ Implementation Roadmap
   ├─ UI skeleton
   ├─ sample data
   ├─ markdown loader
   ├─ search/filter
   └─ charts/metrics
```

**Interaction:**

- 좌측: 하이어라키 트리
- 우측: 선택한 노드 설명, 연결 데이터 파일, 관련 UI 컴포넌트 표시
- 모바일: accordion 형태로 IA / Data / UI / Roadmap 섹션을 접고 펼침

**Validation:** Dev Architecture 탭만 봐도 앱의 전체 IA, 데이터 레이어, 향후 구현 순서를 이해할 수 있다. 이미지 파일 없이 HTML/CSS/React UI로 렌더링된다.

### 3.8 Chris Resume

**Purpose:** 대시보드의 마지막 페이지로 Chris의 이력, 대표 프로젝트, 역량, 연구/디자인 방향성, 작업 철학을 보여준다. 일반적인 PDF 이력서 복제가 아니라, Chris의 AI 운영/디자인/연구/OBD 맥락과 연결되는 살아있는 프로필 페이지로 구성한다.

**Components:**

- `ResumeHero`
- `ExperienceTimeline`
- `ProjectCaseStudyGrid`
- `SkillSystemMap`
- `DesignResearchStatement`
- `ResumeDownloadCard` 또는 `ContactCard`

**Information Architecture:**

```txt
Chris Resume
├─ Profile Summary
│  ├─ 이름 / 타이틀
│  ├─ 핵심 한 줄 소개
│  └─ 현재 탐구 주제
│
├─ Experience Timeline
│  ├─ 주요 경력
│  ├─ 역할 변화
│  └─ 누적된 디자인/AI/운영 경험
│
├─ Selected Projects
│  ├─ 프로젝트명
│  ├─ 역할
│  ├─ 문제 / 접근 / 결과
│  └─ 관련 역량
│
├─ Skills & Systems
│  ├─ Design direction
│  ├─ AI operation / orchestration
│  ├─ Research synthesis
│  ├─ Product thinking
│  └─ Technical collaboration
│
├─ Philosophy / Statement
│  ├─ 디자인 관점
│  ├─ AI UX 관점
│  ├─ One UI / 미래 UI 탐구 방향
│  └─ OBD 성장 관점
│
└─ Contact / Export
   ├─ 공개 가능한 연락 정보
   ├─ PDF/Markdown export 후보
   └─ private/public version guardrail
```

**Privacy Guardrail:**

- v1에서는 실제 개인정보를 임의로 채우지 않는다.
- Chris가 제공한 공개 가능한 문장/경력/프로젝트만 사용한다.
- private 대시보드용 상세 이력과 public export용 이력서를 분리할 수 있게 설계한다.

**Validation:** Chris Resume 탭은 대시보드의 마지막 페이지로 배치되고, Chris가 자신의 이력/프로젝트/철학을 앱 안에서 검토할 수 있다. 임의 경력이나 개인정보를 생성하지 않는다.

---

## Phase 4: Markdown Data Connection

**Objective:** 샘플 TypeScript 데이터를 Markdown 기반 콘텐츠로 교체한다.

**Likely 파일:**

- Create: `content/metaphor-loops/command-garden.md`
- Create: `content/metaphor-loops/research-constellation.md`
- Create: `content/metaphor-loops/growth-loom.md`
- Create: `content/overview/today.md`
- Create: `content/team/agents.md`
- Create: `content/team/orchestration.md`
- Create: `content/obd/daily/2026-08-01.md`
- Create: `content/obd/weekly/2026-W31.md`
- Create: `content/research/papers/example-paper.md`
- Create: `content/reports/muyeol/weekly/2026-W31.md`
- Create: `content/dev-architecture/ia-map.md`
- Create: `content/dev-architecture/data-layer.md`
- Create: `content/dev-architecture/구현-map.md`
- Create: `content/chris-resume/profile.md`
- Create: `content/chris-resume/experience.md`
- Create: `content/chris-resume/projects.md`
- Create: `content/chris-resume/skills.md`
- Create: `content/chris-resume/philosophy.md`
- Create: `src/lib/markdown.ts`
- Modify: `src/lib/data.ts`

**Tasks:**

1. Markdown frontmatter 스키마 정의
2. Markdown 파일 읽기 유틸 구현
3. OBD daily/weekly loader 구현
4. research paper loader 구현
5. Muyeol report loader 구현
6. Dev Architecture content loader 구현
7. Chris Resume content loader 구현
8. UI를 Markdown loader로 전환

**Validation:**

- Markdown 파일을 수정하면 UI에 반영된다.
- frontmatter 누락 시 명확한 에러 또는 fallback을 제공한다.

---

## Phase 5: Search & Filtering

**Objective:** 리서치 논문과 기록을 빠르게 찾을 수 있게 한다.

**Likely 파일:**

- Create: `src/lib/search.ts`
- Modify: `src/features/research/ResearchPage.tsx`
- Modify: `src/features/obd/ObdPage.tsx`

**Tasks:**

1. 클라이언트 사이드 검색 구현
2. 제목/태그/요약/상태 검색 지원
3. Research 필터 구현
4. OBD 날짜/주제 필터 구현
5. empty result 상태 구현

**Validation:**

- 특정 키워드로 논문이 검색된다.
- 태그 필터와 검색어 조합이 동작한다.
- 모바일에서도 검색 UI가 사용 가능하다.

---

## Phase 6: Charts & Metrics

**Objective:** 성장과 검증 상태를 그래프로 확인한다.

**Possible Libraries:**

- Recharts
- Chart.js
- Visx
- CSS-only simple bars for v1

**Recommendation:** v1은 Recharts 또는 CSS-only simple chart로 시작한다.

**Charts:**

- OBD daily growth line chart
- OBD weekly summary bar chart
- Muyeol weekly validation-status stacked bar
- Risk-level and risk-category chart
- Open vs resolved issues trend

**Validation:**

- 데이터가 없는 경우 차트가 깨지지 않는다.
- 모바일에서 차트가 좌우 스크롤 없이 읽힌다.
- 수치와 그래프가 같은 데이터에서 나온다.

---

## Phase 7: QA, Polish, and Local Handoff

**Objective:** Chris가 로컬에서 안정적으로 실행하고 확인할 수 있는 상태로 정리한다.

**Tasks:**

1. README 작성
   - 설치 방법
   - 실행 방법
   - 데이터 파일 수정 방법
   - 폴더 구조 설명

2. 로컬 실행 검증
   - clean install
   - dev server
   - build
   - responsive check

3. 기본 QA
   - 탭 전환
   - 검색
   - empty state
   - 잘못된 Markdown 처리
   - 모바일 레이아웃

4. Muyeol 최종 검증 요청
   - privacy/security 검토
   - 로컬 데이터에 비밀값 저장 금지 확인
   - UX 흐름 검토

**Validation Commands:**

```bash
npm install
npm run dev
npm run build
npm run lint
```

Expected:

- dev server starts 성공fully
- production build succeeds
- no TypeScript errors
- no lint errors or only documented non-blocking warnings

---

## 5. v1 범위

## 포함

- 로컬호스트 실행
- 반응형 앱 셸
- 8개 주요 탭
- 샘플 데이터
- Markdown 데이터 구조
- Dev Architecture 탭: IA / 데이터 레이어 / UI 컴포넌트 / 구현 로드맵 하이어라키
- Chris Resume 탭: Chris의 이력 / 대표 프로젝트 / 역량 / 작업 철학 페이지
- 논문 검색
- OBD 일간/주간 표
- Muyeol 주간/월간 보고 카드
- 기본 차트
- README

## 제외

- 원격 배포
- 사용자 로그인
- 원격 DB
- 자동 논문 수집
- Slack/Telegram 실시간 연동
- Agent 상태 실시간 업데이트
- 복잡한 권한 관리

---

## 6. 데이터 스키마 초안

## Localized Copy

KR/EN 토글을 위해 UI copy는 처음부터 bilingual object로 관리한다.

```ts
type Locale = 'ko' | 'en';

type LocalizedText = {
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

## Architecture Node

Dev Architecture 탭은 별도 이미지가 아니라 아래 같은 트리 데이터를 UI로 렌더링한다.

```ts
type ArchitectureNode = {
  id: string;
  label: string;
  kind: 'route' | 'section' | 'component' | 'data' | 'content' | 'phase';
  description: string;
  children?: ArchitectureNode[];
  relatedFiles?: string[];
  relatedComponents?: string[];
};
```

## Data Layer Node

```ts
type DataLayerNode = {
  id: string;
  path: string;
  purpose: string;
  format: 'markdown' | 'json' | 'typescript' | 'generated';
  ownerLoop: 'metaphor' | 'overview' | 'team' | 'obd' | 'research' | 'muyeol' | 'dev-architecture';
  children?: DataLayerNode[];
};
```

## Resume Profile

Chris Resume 탭은 공개 가능한 이력 정보만 사용하고, private/public export를 분리할 수 있게 설계한다.

```ts
type ResumeProfile = {
  name: string;
  title: string;
  summary: string;
  focusAreas: string[];
  publicContact?: string;
};

type ResumeExperience = {
  id: string;
  period: string;
  organization?: string;
  role: string;
  summary: string;
  highlights: string[];
  visibility: 'private' | 'public';
};

type ResumeProject = {
  id: string;
  title: string;
  role: string;
  problem: string;
  approach: string;
  outcome?: string;
  relatedSkills: string[];
  visibility: 'private' | 'public';
};
```

## Agent

```ts
type Agent = {
  id: string;
  name: string;
  role: string;
  responsibilities: string[];
  outputs: string[];
  status?: 'active' | 'idle' | 'blocked';
};
```

## OBD Daily Entry

```ts
type ObdDailyEntry = {
  date: string;
  theme: string;
  input: string;
  action: string;
  output: string;
  reflection: string;
  growthScore: number;
  nextAction: string;
};
```

## Research Paper

```ts
type ResearchPaper = {
  id: string;
  title: string;
  authors: string[];
  year: number;
  source: string;
  url?: string;
  pdf?: string;
  abstract?: string;
  summary: string;
  tags: string[];
  relevanceScore: number;
  projectLink: string;
  status: 'collected' | 'reading' | 'summarized' | 'synthesized' | 'applied';
};
```

## Research Paper Markdown Frontmatter

v1에서는 논문을 Markdown 파일 하나로 관리한다. 이유는 논문 데이터가 검색 대상인 동시에 사람이 읽는 지식 노트이기 때문이다.

```md
---
id: paper-001
title: "Paper title"
authors: ["Author A", "Author B"]
year: 2026
source: "arXiv"
url: "https://example.com"
tags: ["agent", "memory", "dashboard"]
status: summarized
relevanceScore: 4
---

## Summary

핵심 요약.

## Why it matters to Chris

Chris 프로젝트와 연결되는 지점.

## Yuna Notes

리서치 메모.

## Karina Synthesis

프로젝트 적용 관점의 종합.
```

## Muyeol Report

```ts
type MuyeolWeeklyReport = {
  week: string;
  overallStatus: 'good' | 'caution' | 'risk' | 'blocked';
  validationItems: MuyeolValidationItem[];
  summary: string;
};

type MuyeolValidationItem = {
  id: string;
  title: string;
  status: 'pass' | 'needs-fix' | 'recheck-needed' | 'deferred';
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  category: 'UX' | 'security' | 'privacy' | 'reliability' | 'data-quality' | 'product-logic';
  finding: string;
  recommendation: 'fix-now' | 'watch' | 'accept-risk' | 'revisit-later';
  owner?: string;
};
```

Muyeol 리포트에서 `pass/fail`은 최종 판단의 전부가 아니라 집계용 보조 지표로만 사용한다. 실제 의사결정은 `status`, `riskLevel`, `category`, `recommendation` 조합으로 한다.

---

## 7. 리스크와 트레이드오프

## Risk 1: OBD 정의 미확정

- 영향: OBD 화면과 데이터 모델 변경 가능
- 대응: v1은 flexible schema와 샘플 데이터로 시작

## Risk 2: Markdown 기반 검색 한계

- 영향: 데이터가 많아지면 클라이언트 검색이 느려질 수 있음
- 대응: v1은 로컬 소량 데이터, 이후 SQLite/FlexSearch/Lunr 검토

## Risk 3: 차트 과투자

- 영향: 실제 데이터가 적을 때 그래프가 장식이 될 수 있음
- 대응: 먼저 표와 카드 중심, 차트는 최소 구현

## Risk 4: 운영 대시보드와 문서 위키의 경계

- 영향: 앱이 너무 복잡해질 수 있음
- 대응: v1은 운영 현황 중심, Markdown wiki는 후속 단계로 분리

## Risk 5: Dev Architecture 탭이 문서 덤프처럼 보일 위험

- 영향: UI 탭이 실제 탐색 경험이 아니라 긴 문서 뷰어처럼 보일 수 있음
- 대응: 트리/카드/accordion 기반으로 IA, data layer, component map을 분리하고, 각 노드는 목적·연결 파일·관련 화면만 짧게 보여준다.

## Risk 6: Chris Resume 탭의 개인정보/이력 과생성 위험

- 영향: 공개하면 안 되는 개인정보나 검증되지 않은 경력 문장이 UI에 들어갈 수 있음
- 대응: v1은 placeholder와 Chris가 제공한 공개 가능한 내용만 사용한다. `visibility: private | public` 필드를 두고 public export와 private 대시보드 표시를 분리한다.

---

## 8. Chris에게 필요한 다음 결정

구현 전에 Chris가 정하면 좋은 항목:

1. OBD의 정확한 정의
2. OBD growth score 기준
3. 리서치 논문 입력 방식은 v1 Markdown 기본값으로 진행할지 여부
4. Muyeol 리포트의 상태/리스크/카테고리/권고 체계 세부값
5. Next.js vs Vite React 선호
6. UI 톤: 더 운영 대시보드형인지, 더 매거진/위키형인지
7. Dev Architecture 탭에서 우선 보여줄 깊이: route 수준만인지, content path와 component path까지 포함할지
8. Chris Resume 탭에 넣을 공개 가능한 이력/프로젝트/연락 정보 범위
9. KR/EN 토글의 기본 언어와 영문 copy의 톤: 직역형인지, 글로벌 포트폴리오형인지

---

## 9. 추천 실행 순서

1. Phase 0에서 OBD/리포트 스키마 확정
2. Next.js 또는 Vite React 프로젝트 생성
3. 로컬 UI skeleton 완성
4. localized copy 구조와 KR/EN toggle 상태 추가
5. Dev Architecture 탭의 정적 하이어라키 UI 추가
6. Chris Resume 탭의 placeholder UI 추가
7. 샘플 데이터 연결
8. 화면별 UI 완성
9. Markdown 데이터 연결
10. 검색/필터 추가
11. 차트 추가
12. README와 QA 완료

---

## 10. Definition of Done

v1이 완료되었다고 볼 수 있는 기준:

- Chris가 로컬호스트에서 앱을 실행할 수 있다.
- Metaphor Loops, Overview, Team, OBD, Research, Muyeol Report, Dev Architecture, Chris Resume 탭이 모두 동작한다.
- 데스크톱과 모바일에서 레이아웃이 깨지지 않는다.
- OBD 일간/주간 데이터가 표시된다.
- Research 탭에서 논문 검색이 가능하다.
- Muyeol 보고 수치와 상태/리스크/권고 그래프가 표시된다.
- Markdown 파일을 수정하면 대시보드 콘텐츠를 갱신할 수 있다.
- Dev Architecture 탭에서 앱 IA, 데이터 레이어, UI 컴포넌트 하이어라키를 이미지 없이 UI로 확인할 수 있다.
- Chris Resume 탭에서 Chris의 이력/프로젝트/역량/작업 철학을 확인할 수 있고, 임의 경력이나 개인정보가 생성되지 않는다.
- KR/EN 토글로 주요 navigation, page title, intro, section label이 한글/영문으로 전환된다.
- README에 실행/수정 방법이 명확히 적혀 있다.
- 비밀값이나 개인 토큰을 저장하지 않는다.
