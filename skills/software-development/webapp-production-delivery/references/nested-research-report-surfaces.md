# Nested research report surfaces

## When to use
Use when one parent dashboard route (for example, a Dissertation tab) needs multiple research ideas/reports without making existing top-level navigation more complex.

## Implementation pattern

1. First disambiguate the information architecture. Use a local report-tab navigation only when the user asks for ideas *within* one Dissertation route. If they ask for ideas to be “아예 다른 탭” (separate tabs), create distinct primary `TabId` records, navigation labels, and hash URLs for each idea instead of nesting them under a shared panel.
2. Store each idea as a separately typed report record. Give each a stable ID, label, title/dek, sections, sources, and prompts.
3. For nested variants, keep the parent URL/hash stable and extend the panel API with an explicit ordered list of record IDs (for example `reportIds`) rather than coupling the panel to a single hard-coded record. For primary variants, render one explicit report ID per top-level tab.
4. If Chris specifies that **Dissertation itself** is a top-level peer of `Report`, make `dissertation` the sole primary `TabId` and put `Dissertation Idea 01`, `Dissertation Idea 02`, and `References` in an ordered local tab nav inside that parent. Reuse the established renderers (`PersonalAxReportPanel` filtered by report ID and `DissertationReferencesPanel`) to preserve existing content rather than moving or duplicating data.
5. Preserve legacy entry hashes deliberately: map `#dissertation-idea-1`, `#dissertation-idea-2`, and `#references` to the parent Dissertation workspace while initializing the matching local tab. Use `#dissertation` as the canonical hash after local navigation unless direct subtab deep links are explicitly requested.
6. Update the general-report filter so dissertation records are excluded from unrelated report listings.
6. Keep proposal content accurately framed:
   - Small-N and short-duration usage studies are exploratory multi-case studies, not proof of learning outcomes or market fit.
   - Separate journal suitability, expected contribution, product hypothesis, and commercialization measures.
   - Treat gender or other demographics as participant-diversity context, never as deterministic learner traits.
   - For personal-data-based personalization, include granular consent, data minimization, profile/log access and correction/deletion, and human handoff boundaries.

## Required browser QA

Use a real click on the nested tab and assert all of the following at ultra-narrow mobile, tablet, and desktop widths:

- The intended local tab is active.
- The proposal title, agent roles, and journal/business section render.
- `document.documentElement.scrollWidth === window.innerWidth`.
- The deployed hosted URL passes the same test only after the CI/Pages workflow reports success.

This catches the common regression where a new long report or tab label expands the entire page horizontally even though source-level CSS looks correct.
