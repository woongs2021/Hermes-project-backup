# Inline Source Weaving for AI/AX SNS Posts

## Session learning

Chris corrected the reference style for AI/AX SNS loop posts: a separate `## 레퍼런스` section with full URL bullets feels too much like an appended report and interrupts the SNS reading flow.

## Preferred public-post pattern

- Do not default to a full URL dump in the public SNS copy.
- Weave credible source names naturally into the main sentences:
  - `한국은행이 ... 짚은 것처럼, ...다.`
  - `ILO도 ... 직무 전환에 가깝다고 본다.`
  - `WEF의 일자리 전망처럼 ... 운영 체계로 보기 시작한다.`
  - `Figma Make처럼 ... 디자인의 가치는 ... 이동한다.`
  - `NN/g가 ... 보는 것처럼 ... 품질 운영체계에 있다.`
- End with one compact line beginning `참고 흐름:` that lists source/publisher + short title names only.
- Preserve full URL/DOI traceability in local JSONL `references` and upstream raw/source files.

## Example ending

```text
## [오늘자 총평]

🧠 오늘의 핵심은 한국은행·ILO·WEF·Figma·NN/g가 각기 다른 방향에서 보여주듯, AI 이후의 경쟁력이 생성 속도보다 판단·검증·책임·교육 구조를 누가 더 잘 설계하느냐로 이동한다는 점이다.

참고 흐름: 한국은행 청년고용·AI 노출 업종 분석, ILO 생성형 AI 직무노출 지수, WEF Future of Jobs, Figma Make, NN/g AI UI 패러다임 글을 함께 봤다.
```

## Pitfall

Avoid treating “references are mandatory” as “public URL block is mandatory.” The durable rule is source traceability; the public UX should feel like a natural SNS market interpretation.