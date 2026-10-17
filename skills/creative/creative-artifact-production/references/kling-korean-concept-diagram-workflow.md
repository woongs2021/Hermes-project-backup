# Kling 기반 한국어 개념도/인포그래픽 제작 워크플로우

## Trigger
- Chris가 Son/Go Youn-jung/Karina가 만든 개념도, 구조도, OBD/AX 프레임, 시장조사 요약 등을 `PNG로 만들어줘`, `클링 사용해서`, `고윤정이 만들어주게 해줘`라고 요청할 때.
- 특히 한국어 텍스트가 많은 다이어그램/카드/인포그래픽에 적용한다.

## Core lesson
Kling 같은 이미지 생성 모델에 한국어 다이어그램 텍스트를 직접 렌더링시키면 깨진 글자, 가짜 한글, 의미 없는 라벨이 생길 수 있다. 안전한 방식은:

1. **소스 확인**
   - 원본 SVG/Markdown/Mermaid/메모 경로를 먼저 확인한다.
   - 텍스트와 구조는 원본에서 가져오고, 임의로 내용을 바꾸지 않는다.

2. **Kling 역할 제한**
   - Kling은 텍스트 없는 배경, visual motif, premium editorial mood 생성에만 사용한다.
   - Prompt에 `no text, no letters, no numbers, no labels, no watermark`를 명시한다.

3. **로컬 오버레이**
   - 한국어 제목, 레이어명, 설명, 화살표/관계 라벨은 로컬에서 정확히 렌더링한다.
   - Pretendard/Noto Sans CJK KR/Apple SD Gothic Neo 계열을 우선한다.
   - 산출물은 공유용이면 16:9 1920×1080, 원본 보존이면 원본 비율 PNG를 따로 만든다.

4. **Go Youn-jung specialist delivery**
   - Chris가 `고윤정이` 하게 해달라고 말하면 Go Youn-jung 프로필/목소리로 실행·전달하게 한다.
   - 가능하면 Go Youn-jung Telegram bot으로 직접 보내고, `telegram-send-status.json`에 실제 message_id를 남긴다.

5. **Verification**
   - PNG 파일 존재/크기 확인.
   - vision review로 레이아웃, 한글 가독성, 명백한 깨짐/가짜 글자 여부를 확인.
   - Telegram 직접 전송 status 파일의 text/photo `ok`와 message_id 확인.

## Recommended folder pattern
`/opt/data/agent-team-work-log/visuals/requested-concepts/YYYY-MM-DD-topic/`

Include:
- `final-name.png`
- `source-note.md` — source paths, Kling model/command summary, quality notes, limitations, Chris-facing rationale
- `telegram-send-status.json` — attempted, text/photo/video ok, message_id, errors

## Chris-facing summary
Keep it short and warm:
- 생성/전송 완료 여부
- 한글 깨짐 방지를 위해 Kling은 배경에만 쓰고 텍스트는 로컬 오버레이했다는 점
- 원본 비율인지 16:9 재배치인지
- 필요하면 발표용/카드뉴스/원본비율 파생본 가능
