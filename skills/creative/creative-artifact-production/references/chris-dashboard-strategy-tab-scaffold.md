# Chris Dashboard Strategy Tab Scaffold

Use this when Chris asks to add or expand a conceptual/product-process tab in the Hermes Project Webapp from a project constitution, strategy brief, or long-form product direction document.

## Trigger

- Chris provides a project constitution / MD spec and asks to reflect it in the webapp.
- The content is a product/AX/process narrative, not a normal data dashboard.
- The tab may include sub-tabs such as About, Archive/Evidence, and System/Workflow.

## Product handling pattern

1. **Treat the source MD as a constitution, not page copy.** Extract the public-facing structure and rewrite it into concise product cards. Do not dump the entire MD into the UI.
2. **Keep private roots separate from the webapp repo.** Store source/reference/preference/prompt/evaluation data in a private workspace such as `/opt/data/<project>/`; publish only public-safe summaries in the webapp.
3. **Use the dashboard's existing IA and card language.** Preserve existing tab arrays, sub-tab nav patterns, `content-card` styling, bento grids, restrained typography, and responsive breakpoints.
4. **Recommended content layers:**
   - About / definition / north star
   - Archive or evidence surface for future inputs
   - System or workflow layer showing how the process operates
5. **For About pages, include the middle hierarchy.** Chris values seeing the process between raw input and final output, e.g. `Reference Images → Visual Pattern Recognition → Design Principles → Design DNA → Reusable Design System`.
6. **For agentic systems, show role contracts.** Summarize Karina / Go Youn-jung / Yuna / Son / Faker / Muyeol responsibilities as a judgment/workflow contract, not as internal implementation noise.
7. **Use named case anchors as starter cases, not product definitions.** If Chris names a case such as Coca-Cola special-edition bottle packaging, keep the page language broad (`Brand & Package System`) and frame the named case as the first/starter experiment only. Avoid headings or hero copy that make the product sound Coca-Cola-specific.
8. **Separate mockup execution from the canonical design logic.** If Chris approves Higgsfield for package mockups, describe it as an execution/provider layer for presentation-quality concepts. The source of truth remains the structured Design DNA + Brand Strategy + Product Constraints + Market Context prompt package, not the generated image itself.

## Verification pattern

Run the normal webapp checks:

```bash
npm run validate:data
npm run lint
npm run build:public
git diff --check
```

If Playwright/Chromium is not available in the current environment, do not claim full browser visual QA. Instead:

1. Verify built JS/CSS assets contain the exact new tab labels, sub-tab labels, case names, hierarchy copy, and CSS class names.
2. Deploy via the repo's normal GitHub Pages flow.
3. Poll Actions or equivalent deployment status.
4. Fetch the live HTML, resolve hashed JS/CSS assets, and search live assets for the exact new strings/classes before claiming live deployment.
5. State clearly that this is live asset/content verification, not a substitute for pixel/interaction QA.

## Pitfalls

- Do not put raw private references, prompts, feedback weights, or internal logs into public webapp source.
- Do not over-center image generation. For AX/process tabs, the story is the reusable decision system, not a generated picture.
- Do not create a narrow one-off visual style that breaks the existing dashboard tone; use the existing high-end SaaS/bento editorial language.
- Do not treat brand-case concepts as client claims; frame them as public concept/prototype cases when relevant.
