# Chris AI/AX SNS post loop

Use this reference when converting Chris's Wednesday/Friday AI/AX job-shift loop into SNS-ready copy, especially through Son's specialist profile.

## Trigger
- Chris asks to summarize the Wednesday/Friday AI/AX loop for SNS.
- Source loop combines Yuna AI/AX job-impact research, Go Youn-jung design-job implications, and Son business/market implications.
- This replaces older Son growth-question / business-value-language framing for this use case.

## Delivery ownership
- Son owns the SNS copy layer.
- Deliver from Son's specialist Telegram profile/bot, not Karina/default.
- Use explicit Telegram target `telegram:8935285603` in cron delivery for specialist-owned DM loops.
- If replaying same-day output and profile `send_message target=telegram` fails because home is unset, send via the specialist profile/bot delivery path or explicit target; verify actual delivery before claiming success.

## Output shape
- First line: title inside square brackets, e.g. `[AI가 디자인 일을 바꾸는 방식이다]`.
- After title: 5-7 short lines/sentences.
- Every line after the title starts with a varied emoji.
- Every sentence ends with Korean declarative `다.`.
- DM wrapper may start with `손입니다.` and end with one compact saved-path line; the SNS post itself should be copy/paste-ready.

## Tone and content
- Human, warm, reflective, and plainspoken; avoid stiff consulting-report language.
- Do not mention Chris or OBD in the SNS copy unless explicitly requested.
- Center the relationship between AI and design:
  - AI makes production, variation, organization, and documentation faster.
  - Design judgment, context reading, brand meaning, user understanding, quality control, and responsibility become more important.
- Make job/career implications visible:
  - Repeated junior tasks may shrink.
  - Learning paths, first career steps, portfolios, and roles may need redesign.
- Mention education/business lightly as support, not as the center.

## Avoid
- Avoid phrases that feel like a bot/report: `핵심 변화`, `시장 변화`, `관점에서 중요한 질문`, `가치교환 구조`.
- Avoid jargon overload and source caveats in the user-facing SNS post.
- Avoid raw file paths, cron/tool language, and private diagnostics inside the post.

## Good example
```text
[AI가 디자인 일을 바꾸는 방식이다]
🌿 AI는 초안 제작, 이미지 변주, 문서 정리처럼 반복되는 일을 훨씬 빠르게 만들어 준다.
🎨 그래서 디자인의 가치는 손으로 오래 만드는 능력보다 맥락을 읽고 무엇이 좋은 선택인지 판단하는 능력으로 더 이동한다.
🧭 브랜드가 어떤 의미를 가져야 하는지, 사용자가 무엇을 불편해하는지, 결과물이 우리다운지 살피는 일은 더 중요해진다.
🛠️ 주니어가 배우던 리사이징, 레퍼런스 정리, 시안 변형 같은 일이 줄어들면 경력의 첫 계단도 다시 설계되어야 한다.
📁 포트폴리오는 예쁜 결과물만 보여주는 자료가 아니라 어떤 문제를 정의했고, AI를 어디에 썼고, 어떤 기준으로 고쳤는지 보여주는 기록이 된다.
🤝 교육과 비즈니스도 툴 사용법을 가르치는 데서 멈추지 않고, 사람의 판단력과 AI의 속도를 함께 일하게 만드는 방향으로 바뀌어야 한다.
```
