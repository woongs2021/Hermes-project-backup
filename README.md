# Hermes Project Backup

Chris Park과 Karina/Hermes agent team의 운영 지식, 작업 로그, reusable skill, 복구 문서를 안전하게 보관하기 위한 **curated backup repository**입니다.

이 저장소는 실행 중인 Hermes home 전체를 복사한 것이 아닙니다. 비밀값과 런타임 상태를 제외한, 재구성 가능한 운영 지식만 선별해서 백업합니다.

## 현재 원칙

- **백업은 루프가 아닙니다.** Chris가 적절한 시점에 “지금 백업해줘”라고 지시할 때만 실행합니다.
- 백업은 항상 `curated export → safety scan → branch push → main 반영` 순서로 진행합니다.
- broad copy 금지: `/opt/data`, Hermes home, profile home, sessions, logs를 통째로 넣지 않습니다.
- Karina/default는 전체 오케스트레이션과 최종 정리를 맡고, Faker는 구현/웹앱/자동화 관점의 후속 실행을 맡습니다.

## 이 저장소의 역할

이 repo는 두 GitHub 저장소 중 **백업용**입니다.

- Backup repo: `https://github.com/woongs2021/Hermes-project-backup`
- Webapp repo: `https://github.com/woongs2021/Hermes-project-webapp`
- Webapp Pages URL: `https://woongs2021.github.io/Hermes-project-webapp/`

저장소 구분:

- `Hermes-project-backup`
  - Karina-led agent team 운영 체계
  - daily/team work-log Markdown
  - reusable skills/workflows
  - restore/boundary/security notes
  - Hermes 계획 문서 중 안전한 Markdown

- `Hermes-project-webapp`
  - Faker-built dashboard/webapp source
  - public-safe dashboard manifest/data
  - future HomeVisualHero / visual archive data
  - GitHub Pages deployment workflow

## 포함되는 내용

대표 포함 범위:

- `agent-team-work-log/`
  - Karina, Yuna, Go Youn-jung, Son, Faker, Muyeol의 날짜별 작업 기억
  - paper candidate, visual loop notes, loop governance notes 등 안전한 Markdown 중심 기록
- `skills/`
  - 반복 작업을 위한 reusable skill과 reference 문서
  - Hermes/GitHub/creative/research/devops workflow 지식
- `hermes-plans/`
  - 안전한 planning Markdown
- `docs/`
  - restore notes
  - repo boundary
  - security omissions
- `scripts/scan_export_safety.py`
  - push 전 안전 스캔 스크립트

## 절대 포함하지 않는 내용

이 저장소에는 다음을 넣지 않습니다.

- `.env`, `.env.*`
- `auth.json`, OAuth store, credential pool
- Telegram/Slack bot token, API key, PAT, refresh token
- Hermes `state.db`, session DB, raw transcript DB
- gateway logs, request dumps, raw private DM dump
- `node_modules/`, cache, generated runtime directory
- 개인 식별자/비밀값처럼 보이는 긴 문자열

## 현재 팀/프로젝트 맥락

Chris는 Hermes agent team을 자신의 AI/UX/brand/design operating system으로 실험하고 있습니다.

핵심 역할:

- **Karina**: Chris의 warm Korean front door, CDO, main orchestrator, 최종 synthesizer
- **Yuna**: AI 기술, LLM, 논문, 스타트업/미래 시나리오 research
- **Go Youn-jung**: UX/design research, design benchmark, Higgsfield visual loop
- **Son**: PM, growth, SNS/subscriber framing
- **Faker**: coding, prototype, webapp, automation
- **Muyeol**: validation, security, risk, QA/governance

현재 운영 방향:

- daily/weekly research loop는 specialist-owned로 유지합니다.
- Friday final report는 Karina가 종합합니다.
- Go Youn-jung visual loop는 Higgsfield credit을 고려해 daily 2 images + 7-day color/metaphor diversity 기준으로 조정되어 있습니다.
- Faker webapp loop는 Hermes/OBD webapp을 Harness / Loop / Graph Engineering 관점으로 구조화합니다.

## 백업 실행 절차

로컬 기준:

```bash
python3 /opt/data/github-backup-sets/scripts/export_backup_sets.py
python3 /opt/data/github-backup-sets/repos/chris-karina-agent-system/scripts/scan_export_safety.py /opt/data/github-backup-sets/repos/chris-karina-agent-system
```

스캔이 `status: clean`일 때만 GitHub에 push합니다.

권장 git 흐름:

```bash
git checkout -B backup-curated-YYYYMMDD
git add .
python3 scripts/scan_export_safety.py .
git commit -m "chore: curated Hermes project backup"
git push -u origin backup-curated-YYYYMMDD
git checkout main
git merge --ff-only backup-curated-YYYYMMDD
git push -u origin main
```

## 복구 시 주의

이 repo만으로 Hermes runtime을 그대로 복원하려고 하면 안 됩니다.

복구 원칙:

1. 새 환경에서 Hermes를 정상 설치합니다.
2. 실제 credentials와 gateway tokens는 GitHub가 아니라 안전한 비밀 저장소/수동 설정으로 재구성합니다.
3. skills/docs/work-log는 필요한 범위만 검토 후 복사합니다.
4. 오래된 session DB, auth store, raw logs는 복구하지 않습니다.
5. profile별 책임 경계와 Telegram/Slack bot identity는 새 환경에서 다시 확인합니다.

## 현재 상태

- Initial backup branch: `backup-curated-20260802`
- Main 반영 완료
- Safety scan: clean
- 운영 방식: Chris command-triggered backup only
