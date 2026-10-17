# Webapp DNA Dashboard image crop + description cleanup

Use this reference when tuning Chris's Hermes webapp DNA Dashboard / manifest-backed visual archives, especially when the user reports that asset borders, thumbnails, detail views, or descriptions feel wrong.

## Lessons from the DNA Dashboard crop session

### 1. Distinguish CSS frame issues from pixels inside the source image
- If a thumbnail/detail image appears to have an ivory/light outer stroke, verify whether the light edge is part of the image pixels.
- CSS `border-radius`, `clip-path`, `overflow: hidden`, or `box-shadow` can make a frame cleaner, but they do **not** remove a border baked into the image.
- If the user is comfortable with destructive edits, crop the actual public asset file and update manifest hashes instead of layering CSS transforms.

### 2. Prefer asset-level crop when the source image itself contains unwanted margins
Recommended safe destructive workflow:
1. Identify all manifest-backed files affected by the displayed item: `imageSrc` and, if present, `highResImageSrc`.
2. Back up originals outside `public/`, e.g. `/opt/data/backups/<project>-dna-crop-YYYY-MM-DD/`, preserving relative paths.
3. Crop inward by a small ratio, commonly 4% on each side, then resize back to the original dimensions so layout and manifest dimensions remain compatible.
4. Save JPEGs with high quality (`quality=95`, `optimize=True`, `progressive=True`) and PNGs without changing dimensions.
5. Update `assetHash` / `highResAssetHash` in the corresponding manifest from the actual written files.
6. Remove temporary CSS display crops (`transform: scale(...)`) once the asset itself is cropped, to avoid double cropping.
7. Verify: manifest hash mismatch count is 0; each live asset URL returns `200` and `image/*`; representative thumbnails/detail images render with `transform: none` and no overflow.

### 3. Be careful: visible item number may not equal manifest array index
- This app sorts DNA archive items before rendering:
  - `items: [...archive.items].sort((left, right) => left.created.localeCompare(right.created) || left.title.localeCompare(right.title))`
- When Chris says “18번”, resolve the **visible screen order**, not raw manifest index 17.
- For each relevant lane (GPT Image 2.5 and Midjourney), compute or probe the rendered/sorted list and map visible index → item id/title/path before editing files.
- If there are multiple lanes, clarify through evidence or apply the visible item number in each lane only when that matches the context. Do not silently edit manifest index 18.

### 4. Detail modal layout pitfall
- In CSS grid modals, grid items stretch by default. A long text column can make the image/media panel stretch vertically and visually “break” the image/content composition.
- Fix by setting `align-items: start` on the modal grid so media and copy panels keep independent heights.
- Verify desktop/tablet/mobile geometry: media panel top/size, copy panel top/size, image natural dimensions, `overflowX: 0`, and no console errors.

### 5. Description cleanup for public-facing visual archives
When Chris asks for “원래 이미지 설명” or says not to show history:
- Remove process/history phrases from `analysis`, e.g. “저장했습니다”, “교체 요청”, “Chris가 선택”, “몇 번째 결과”, “생성 의도”, “업데이트”.
- Write image-native descriptions instead:
  - visible form / composition
  - color palette
  - material or texture
  - mood / metaphor
  - plausible brand, package, card, background, or UI-surface use
- Keep descriptions public-safe and avoid internal workflow or agent-operation language.

## Verification snippets

### Resolve visible item order from manifests
```python
import json, pathlib
root = pathlib.Path('/path/to/app')
for label, mf in [('GPT','public/data/dna-archive.json'), ('MJ','public/data/midjourney-dna-archive.json')]:
    data = json.loads((root / mf).read_text())
    items = sorted(data['items'], key=lambda x: (x['created'], x['title']))
    item = items[17]  # visible #18
    print(label, item['id'], item['title'], item['imageSrc'], item.get('highResImageSrc'))
```

### Hash-check manifest files after destructive edits
```python
import json, pathlib, hashlib
root = pathlib.Path('/path/to/app')
bad = []
for mf in ['public/data/dna-archive.json', 'public/data/midjourney-dna-archive.json']:
    data = json.loads((root / mf).read_text())
    for item in data['items']:
        if item.get('imageSrc'):
            h = hashlib.sha256((root / 'public' / item['imageSrc'].lstrip('/')).read_bytes()).hexdigest()
            if h != item.get('assetHash'):
                bad.append((mf, item['title'], 'assetHash'))
        if item.get('highResImageSrc'):
            h = hashlib.sha256((root / 'public' / item['highResImageSrc'].lstrip('/')).read_bytes()).hexdigest()
            if h != item.get('highResAssetHash'):
                bad.append((mf, item['title'], 'highResAssetHash'))
print('hash_bad', len(bad), bad[:5])
```
