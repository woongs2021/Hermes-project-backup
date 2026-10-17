# Chris webapp Visual Archive asset replacement

Use when Chris asks to replace the Visual Archive hero/camera image in the Hermes webapp.

## Pattern

1. Keep the existing public asset path stable unless Chris asks for a new asset name:
   - `august-dashboard/public/assets/visuals/visual-archive-camera-object.jpg`
   - app reference: `publicAssetPath('/assets/visuals/visual-archive-camera-object.jpg')`
2. Replace the file contents with the provided image rather than changing many render paths.
3. Update the image `alt` text in `src/App.tsx` so it describes the new image, not the previous camera object.
4. If the user recently asked not to capture screenshots, do not create screenshots for verification. Use direct asset hash checks and browser DOM/image-load checks instead.
5. Revert generated manifest timestamp-only changes after validation (`public/data/dashboard-manifest.json`, `home-visual-set.json`, `research-board.json`) unless the manifest content intentionally changed.

## Verification

- Compare source and destination SHA-256 after copying.
- Confirm dimensions with a lightweight parser or browser `naturalWidth`/`naturalHeight` if image tools are unavailable.
- Run:
  - `npm run validate:data`
  - `npm run lint`
  - `npm run build:public`
  - `git diff --check`
- Local browser check on `#visuals`:
  - `.visual-archive-image-card img` exists,
  - `src` resolves under `/Hermes-project-webapp/assets/visuals/visual-archive-camera-object.jpg`,
  - `alt` is updated,
  - `complete === true`,
  - `naturalWidth > 0`,
  - horizontal overflow is `0`.
- After pushing, wait for the GitHub Pages workflow to complete, then fetch the live asset and compare SHA-256.
- For live browser checks, use `waitUntil: 'load'` or explicitly `waitForFunction(() => img.complete && img.naturalWidth > 0)`. A `domcontentloaded` check can see the correct `src` before the image finishes decoding and produce a false negative.

## GitHub Pages delay note

If the Pages URL still serves the previous image after `git push`, inspect Actions instead of assuming failure:

- Query recent runs for `main` and the target commit.
- Check job/step status; the build or deploy job can remain `in_progress`/`queued` for several minutes.
- Poll until the workflow reaches `completed success`, then verify the live asset hash and browser image state.
