# Chris Archive high-volume intake lessons

Use this reference when Chris is adding many visual references to `/opt/data/chris-archive/` with the trigger phrase `추가해줘`.

## Session learning

In a long Telegram intake session, Chris repeatedly uploaded images and asked to add them to Chris Archive. The workflow worked best when Karina stayed quiet during processing and returned one concise completion message after verification.

A user correction occurred after multiple progress fragments: Chris said, “왜 말을 하다말어 ㅎ”. Treat this as a style/workflow correction for Chris Archive intake.

## Preferred interaction pattern

- Do not narrate every internal step such as “분석할게”, “복사할게”, “인덱스 업데이트할게”.
- If the request is straightforward and the image includes `추가해줘`, run the archive workflow quietly.
- Send one final Korean completion message only after:
  - original asset is copied to `images/YYYY/MM/`,
  - entry markdown is written under `entries/YYYY/`,
  - `index.md` is updated,
  - `DESIGN_SYSTEM_DRAFT.md` is updated with tentative candidates,
  - asset and entry existence/size are verified.
- Send an interim message only for a real blocker, ambiguity, missing file, or unusually long operation.

## High-volume execution pattern

For many repeated archive additions, prefer one consolidated tool/script-style operation per image after analysis instead of many small visible tool steps:

1. Compute KST date with `TZ=Asia/Seoul date +%Y-%m-%d`.
2. Use a concise visual-DNA slug, not the cache filename.
3. Copy the uploaded file to:
   `images/YYYY/MM/YYYY-MM-DD_<slug>_<sha12>.<ext>`.
4. Write a structured entry:
   `entries/YYYY/YYYY-MM-DD_<slug>.md`.
5. Append one index block only if the entry path is not already present.
6. Patch `DESIGN_SYSTEM_DRAFT.md` with class-level candidate language only; do not promote single-image observations to final rules.
7. Verify asset and entry exist and have non-zero bytes before reporting.

## Final reply shape

Keep completion replies short:

```text
저장 완료했어, Chris.

## 저장 위치
- 이미지 원본
  `<asset path>`
- 분석 노트
  `<entry path>`
- `index.md`, `DESIGN_SYSTEM_DRAFT.md` 업데이트 완료.

## 핵심 디자인 DNA
이번 이미지는 **<cluster name>** 계열로 넣어뒀어.

강한 신호는:
- <3–6 bullets>

주의점은 <one concise caution>.
```

Avoid dumping the full analysis in chat; the detailed entry file is the archive of record.

## Duplicate / near-duplicate handling

If a new upload has the same content hash as an existing archive image, still follow Chris’s explicit `추가해줘` unless he asked for deduplication, but note in the entry or final summary that it is a supporting/detail crop or duplicate-source reference. If exact duplicates become frequent, ask Chris whether he wants dedupe behavior.

## Design-system draft discipline

- Add reusable cluster headings such as `Soft Squircle Interface Boundary`, `Calm AI State Component`, `Human-scale Circular Navigation`, etc.
- Prefer candidate language and review prompts over final rules.
- Include GoYJ review questions when an image could be core DNA, is aesthetically risky, or involves third-party brand/privacy/safety concerns.
- Brand-safety notes are mandatory when third-party logos, product UI, song/artist names, brand names, or literal copy appear.
