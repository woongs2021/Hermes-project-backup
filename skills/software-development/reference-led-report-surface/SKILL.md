---
name: reference-led-report-surface
description: "Create and publish Korean reference-led research reports in a calm editorial web surface, with evidence boundaries, downloadable HTML/PDF-print, image prompts, and restrained marker highlights."
---

# Reference-led research report surface

## Use when
- Chris asks to turn accumulated research into a blog/report tab in a web app.
- A report needs Korean editorial prose grounded in papers, reports, or official sources.
- The task includes report tabs, downloadable HTML, Print / Save as PDF, visual-prompt placeholders, or visual emphasis.

## Editorial principles
1. **Lead with sources, not team process.** Never expose agent names, internal selection labels (`GO`, `WATCH`), private work logs, or operational provenance in public copy unless Chris explicitly requests it.
2. **Use a paper-like structure.** Each report should cover:
   - research scope / problem;
   - source-specific evidence (method, sample, corpus, or access level only when verified);
   - central finding;
   - product, design, or operational interpretation;
   - generalization limit.
3. **Separate evidence from interpretation.** State what the source studied before explaining why it matters. Do not turn a prototype, abstract-only item, student sample, or literature review into a universal product claim.
4. **Keep an editorial, readable Korean voice.** Use short headings, paragraphs, and bullets; favor direct research terms over generic AI-startup language.
5. **Target requested length honestly.** For a target of 3,000 Korean characters, measure Hangul characters in body text only. Treat 2,700–3,300 as the practical range. Do not count headings, references, prompts, or shared UI copy.

## Recommended report data contract
Use a typed data module so one reusable panel can render every topic:

```ts
export type ReportSource = {
  title: string
  href: string
  access: '원문 확인' | '초록·메타데이터 확인'
}

export type Report = {
  id: string
  label: string
  eyebrow: string
  title: string
  dek: string
  sections: Array<{ heading: string; paragraphs: string[]; bullets?: string[] }>
  sources: ReportSource[]
  prompts: string[]
}
```

- Add new domains as another item in the same data array; do not build a parallel report UI.
- This automatically preserves tabs, HTML download, and browser Print / Save as PDF behavior.
- Include 2–3 image-prompt placeholders per report unless actual approved visuals are available. When they are displayed to readers, label the block only **미드저니 프롬프트**; never show internal wording such as “placeholder,” “visual direction only,” or an explanatory disclaimer.
- For Korean editorial body copy, apply a first-line indent of `1em` to article-section paragraphs only. Keep the dek, headings, citations, and bullet lists flush so the reading hierarchy remains calm.

## First-party social-content analysis report

Use this when Chris asks to add a report tab based on their own exported social posts (for example Threads), rather than third-party papers.

1. **Use an authorized, minimal dataset.** Prefer the user's read-only export or an authorized first-party API retrieval. Do not infer historic posts from a public-profile preview when the platform gates pagination.
2. **Fetch enough before sampling.** Retrieve at least the requested sample plus a buffer when paging is available. Keep pagination URLs, OAuth keys, access tokens, raw provider responses, and private export data out of the public app, repository, user-facing report, and work log.
3. **Classify exclusions semantically.** If Chris asks to exclude cooking/food posts, exclude posts that are substantively about food, cooking, restaurants, or recipes. Do not discard an otherwise relevant post merely because it contains an incidental word such as “morning,” “eat,” or “alcohol.” State if no posts actually meet the exclusion category.
4. **State the analytic boundary in the reader-facing report.** Include the retrieval scope (for example, latest 50 own posts and 30 qualitative samples), the exclusion rule, and the fact that engagement, comments, and reach are not being analyzed unless they were actually supplied.
5. **Disclose the permitted integration in plain language.** When a report exists because a user-approved read-only social integration supplied the source material, include a short sentence such as: “Threads와 Hermes의 읽기 전용 연동이 완료되어 이 분석을 작성할 수 있었다.” Treat this as a transparency statement, not an endorsement or a performance claim.
6. **Apply the report lens.** Distinguish: recurring content themes; repeatable brand strengths; insights about reader value and differentiation; marketer-facing improvements; and a practical editorial cadence. Base each on observable post text, not invented performance outcomes.
7. **Keep shared UI truthful.** If the report panel normally describes academic references, add a report-specific byline/note instead of presenting first-party qualitative analysis as a literature review. Preserve existing report behavior unchanged.
8. **Highlight sparingly.** Add the integration disclosure and 8–12 reader-useful claims to the existing restrained marker list, then verify every highlighted phrase actually appears in rendered text.
9. **Verify the surface.** Check the new tab, scope note, disclosure highlight, source count, rendered text length, desktop/mobile overflow, and browser page errors before publishing.

## Evidence-only report expansion

Use this when Chris asks to make an existing report longer while keeping its content intact.

1. **Preserve the editorial contract.** Keep the existing thesis, title, dek, section order, cited-source set, and practical conclusion. Add evidence rather than reframing the report or introducing a new argument.
2. **Expand with source-specific detail.** Prefer research object, method, participant/sample scope, comparison condition, and stated limitation. Explain what each detail permits—and does not permit—the reader to infer.
3. **Keep evidence boundaries visible.** For abstract/metadata-only sources, do not add effect sizes, causal detail, or full-text claims. Keep source-access labels accurate; do not upgrade them merely because the prose became longer.
4. **Place additions near the matching claim.** Append evidence paragraphs to the relevant existing section instead of creating a detached appendix or duplicating the reference list.
5. **Measure the right thing.** Count Korean body characters separately from headings, prompts, and citations during authoring; then verify the rendered article text in the live UI. For a requested 5,000-character report, target roughly 4,500–5,000 characters of editorial body and confirm the reader-facing rendered surface meets the requested scale.
6. **Verify every tab.** When reports are rendered through shared data, use browser automation to open each tab, check that the expanded text appears, confirm tab switching, and capture page errors before publishing.

## Package-design report lens
For packaging reports, cover the full experience chain rather than graphics alone:
- attention and shelf selection;
- information hierarchy and interpretation;
- opening, storage, use, disposal, or reuse;
- material and sustainability claims;
- brand meaning and perceived quality.

Scope evidence by its product category, country, method, and access level.

## Calm marker-highlight treatment
Use highlights sparingly but consistently: roughly 10 meaningful claims per report. Prefer full conceptual phrases, not isolated keywords.

- Place the marker **behind the text**, not as a solid foreground background.
- Use a restrained lime at **20% opacity**.
- Highlight only claims that summarize a finding, principle, trade-off, or action criterion.
- Maintain an explicit phrase list grouped by report category, then render matching text with a semantic `<mark>` element.

```css
.report-highlight {
  position: relative;
  z-index: 0;
  isolation: isolate;
  color: inherit;
  padding: 0 0.12em 0.05em;
  background: transparent;
  border-radius: 0.14em;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}
.report-highlight::before {
  position: absolute;
  z-index: -1;
  content: '';
  inset: 34% -0.12em 7%;
  border-radius: 0.14em;
  background: rgb(218 255 70 / 20%);
  transform: skewX(-2deg);
}
```

Do not use bright blocks, excessive neon, or generic dashboard decoration. Preserve generous whitespace and a calm research-publication surface.

## Prompt-section copy and cover-image intake
- When Chris provides real cover images, use them at the start of the matching reports and preserve the supplied order unless he asks for semantic remapping. Store durable public assets, not chat-cache paths.
- If the report retains Midjourney prompts after covers are added, label the section simply **`미드저니 프롬프트`**. Remove placeholder labels such as `Midjourney prompt placeholder`, `자리표시자`, and meta-explanations about images not yet being generated.
- Strip placeholder prefixes from every prompt string in the typed report data, not only the visible section title. Mirror the concise Korean heading and cleaned prompt text in HTML downloads as well.
- Keep prompt prose itself copy-ready; do not add explanatory paragraphs unless Chris explicitly requests production notes.

## Download / print behavior
- Generate a self-contained escaped HTML Blob in-browser for HTML download.
- Offer `window.print()` as **Print / Save as PDF**. Do not claim a server-rendered native PDF exists unless one was actually generated and verified.
- Keep source title, URL, access scope, cover image, and cleaned prompt copy consistent between screen and downloaded formats.

## Verification and publishing
1. Verify every cited item through an official DOI, publisher, arXiv, or otherwise stable source when possible.
2. Run lint, production build, and `git diff --check` from the actual app directory.
3. If the build regenerates unrelated manifests, stage only the reviewed report-owned source files.
4. Commit and push the approved scope.
5. Verify the specific GitHub Pages workflow for the pushed SHA succeeds.
6. Fetch the deployed index and hashed JS/CSS bundle; assert that new report labels/copy and visual CSS declarations are present.
7. Share the live URL and the in-product navigation path in every web-app update completion message, including small copy or typography fixes.

## Common pitfalls
- Do not count citations or prompts toward the requested report-body length.
- Do not claim causal impact when a paper is abstract-only, correlational, category-specific, or a review.
- Do not omit evidence limits merely to make prose more persuasive.
- Do not stage build-generated public data unless it is deliberately part of the requested change.
- Do not describe a browser print flow as an actual PDF download.
