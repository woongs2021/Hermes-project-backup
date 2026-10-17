# source-note

## 원본 소스
- SVG: `/opt/data/profiles/son/artifacts/obd_ax_concept_graph.svg`
- Mermaid: `/opt/data/profiles/son/artifacts/obd_ax_concept_graph.md`

## 사용 방법
- Kling AI는 한국어 텍스트 렌더링 신뢰도가 낮을 수 있어 최종 한글 텍스트 생성에는 사용하지 않았습니다.
- Kling으로 텍스트 없는 프리미엄 배경/visual motif만 생성한 뒤, Son의 SVG/Mermaid 내용을 기준으로 정확한 한글 텍스트와 다이어그램 구조를 로컬 PIL 오버레이로 제작했습니다.
- 최종 PNG: `/opt/data/agent-team-work-log/visuals/requested-concepts/2026-08-11-obd-ax/obd-ax-concept-goyounjung.png`

## Kling 모델/명령
- 모델: `kling-image-v3_0_omni`
- 주요 옵션: `--img_resolution 2k --aspect_ratio 16:9 --imageCount 1 --poll 300`
- 명령:
```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
HOME=/opt/data kling text_to_image \
  --model kling-image-v3_0_omni \
  --img_resolution 2k \
  --aspect_ratio 16:9 \
  --imageCount 1 \
  --poll 300 \
  -q "Premium soft editorial background for a Samsung One UI future strategy infographic, off-white paper field with subtle mint gradient, restrained warm orange accent, ink-green fine abstract ontology network motifs, soft depth, clean empty center and corners, no text, no letters, no numbers, no fake UI labels, no watermark, minimal refined product-design polish, calm trustworthy Korean business design mood"
```

## 품질 메모
- 최종 이미지는 1920×1080 PNG, 16:9입니다.
- 한국어 텍스트는 로컬 Pretendard 폰트로 직접 렌더링해 깨진 글자/가짜 글자 사용을 피했습니다.
- 스타일은 woongdesignv2 방향의 premium soft editorial 톤으로, off-white/mint/ink/orange 절제 팔레트와 큰 여백, 카드형 정보 위계, One UI에 어울리는 차분한 polish를 우선했습니다.

## 한계
- Kling 배경은 텍스트 없는 추상 motif로만 사용했으며, 최종 다이어그램의 모든 문구와 구조는 로컬에서 재구성했습니다.
- 원본 SVG의 1600×1100 비율을 그대로 래스터 변환한 것이 아니라, Chris 공유용 16:9 인포그래픽으로 레이아웃을 재조정했습니다.

## Chris에게 전할 짧은 설명
OBD를 ‘AI 툴 도입’이 아니라 조직의 업무·지식·판단·책임·성과 구조를 다시 설계하는 역량으로 보이게 정리했습니다. 한글 가독성을 위해 Kling은 배경 질감에만 쓰고, 핵심 텍스트와 다이어그램은 로컬에서 정확히 오버레이했습니다.
