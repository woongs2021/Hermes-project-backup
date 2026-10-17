# Vite GitHub Pages public assets and live smoke checks

Use this when deploying Chris's Vite webapp to GitHub Pages and public images or CSS/JS changes might break only after `base` path rewriting.

## Problem pattern

For a Vite app hosted under a repo path such as `/Hermes-project-webapp/`, public assets under `public/assets/...` are served at:

```text
https://<owner>.github.io/<repo>/assets/...
```

A leading root path like `/assets/team/son_profile.jpg` can work locally but is fragile on Pages because it points to the domain root. A helper that prepends `import.meta.env.BASE_URL` fixes that, but applying the helper twice can create double-prefix paths such as:

```text
/Hermes-project-webapp//Hermes-project-webapp/assets/team/...
```

## Safer helper

Use a helper that is idempotent for already-prefixed paths:

```ts
const publicAssetPath = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`

function toAppAssetSrc(path: string) {
  if (path.startsWith('http') || path.startsWith(import.meta.env.BASE_URL)) return path
  return path.startsWith('/') ? `${import.meta.env.BASE_URL}${path.slice(1)}` : path
}
```

Then either:

- store raw public paths in data (`/assets/team/foo.jpg`) and call `toAppAssetSrc()` at render time, or
- store already-prefixed paths from `publicAssetPath()` and ensure render-time helpers do not prefix again.

Do not mix the two without the idempotent guard.

## Live smoke checklist

After deployment, verify more than HTTP 200 on the page:

1. Fetch the live HTML and identify the current hashed JS/CSS assets.
2. Fetch live JS/CSS and check for expected marker strings/styles from the change.
3. Fetch each public asset URL directly and confirm HTTP 200 plus image content type.
4. For image-heavy UI, run a browser smoke and check each relevant `img` has:
   - `complete === true`
   - `naturalWidth > 0`
   - no console/page errors
   - the expected `alt` text when the asset was replaced
   - if verifying immediately after navigation, wait for `load` or explicitly wait on `img.complete && img.naturalWidth > 0`; `domcontentloaded` alone can observe the correct `src` before the image is decoded and create a false negative.
5. For CSS/layout fixes, use browser computed styles on the live page, not only source grep.
6. If live Pages still serves a previous asset hash after `git push`, inspect the Actions run/job status for the pushed commit and wait for `completed success` before declaring failure. Pages build/deploy jobs may remain `in_progress` or `queued` for several minutes.

## Example browser assertions

```js
const imgs = await page.$$eval('img', imgs => imgs.map(img => ({
  alt: img.alt,
  src: img.src,
  complete: img.complete,
  naturalWidth: img.naturalWidth,
  naturalHeight: img.naturalHeight,
})))
const broken = imgs.filter(img => !img.complete || img.naturalWidth === 0)
```

For responsive/sticky fixes, capture computed layout values at both desktop and mobile viewport widths, e.g. `gridTemplateColumns`, `strokeWidth`, `topbar.getBoundingClientRect().top`, and `marginTop`.