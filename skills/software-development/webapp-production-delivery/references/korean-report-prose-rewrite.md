# Korean report prose rewrite QA

Use this checklist when converting a report collection from academic Korean to an accessible blog-editorial voice while preserving its research value.

## Scope inventory

Count every reader-visible Korean value in the typed data: title, dek, headings, paragraphs, bullets, post-bullet paragraphs, and alt text. A shared byline or CSS-only change is not a collection rewrite.

## Preserve exactly

Keep study titles, samples, methods, numeric details, source URLs, access labels, IDs, data structure, and stated generalization limits. Rephrase voice and sentence rhythm, not evidence.

## Editorial pass

- Break overloaded sentences into clear beats.
- Prefer direct verbs and reader-facing transitions.
- Remove stiff framing such as `본 리포트는` without adding empty filler.
- Avoid repeated mechanical openings such as `요지를 정리하면`.
- Do not apply blind synonym replacement; inspect natural Korean in every topic.
- Keep roughly the same amount of body text unless a new target is specified.

## Verification

1. Compare data shape and source/prompt metadata before and after.
2. Count rewritten visible values and inspect representative passages from every report.
3. Search for repeated filler, duplicated adverbs, or malformed substitutions.
4. Run lint, TypeScript/build, and whitespace checks.
5. State local-versus-live deployment truthfully.
