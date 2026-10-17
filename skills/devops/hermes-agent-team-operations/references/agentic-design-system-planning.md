# Agentic Design System / Personal Design DNA Planning Pattern

Use this reference when Chris proposes a new loop or product around `PROJECT_DESIGN_DNA.md`, Design DNA Studio, Personal Design DNA Engine, agentic brand/package workflows, or turning personal design judgment into reusable system logic.

## Primary constitution

Treat `PROJECT_DESIGN_DNA.md` as the project constitution and highest product-direction source for this class of work. If the file exists in the repo/workspace, read it first. If Chris pasted the contents in chat, treat that pasted content as the constitution until it is saved.

Core north star:

- Do **not** build an AI image generator or package mockup toy.
- Build an **Agentic Design System** that extracts a designer's visual judgment from references, combines it with brand strategy/product constraints/market context, generates or packages design directions, evaluates outputs, and improves the process.
- Preserve this distinction: Generative AI creates outputs; Agentic AI executes processes; AX transforms design intelligence into a reusable system.

## Mandatory first response before implementation

Do not implement first. Return a planning/assessment report with these sections:

1. Current architecture assessment
2. Gap analysis
3. Proposed MVP scope
4. Agent responsibility mapping
5. Technical architecture
6. Data/file architecture
7. Image provider strategy
8. Design DNA analysis methodology
9. Evaluation/refinement loop
10. Implementation phases
11. Risks and unknowns
12. Decisions that require Chris approval

Only after Chris approves should implementation be delegated or started.

## Existing agent mapping

Do not add new agents unless an existing role clearly cannot cover the responsibility.

- Karina: orchestrator, phase gates, synthesis, approval checkpoints, product/narrative integrity.
- Go Youn-jung: Design DNA extraction, visual dimensions, art direction, visual critic, packaging/design quality.
- Yuna: market/category/competitor/technology/provider research.
- Son: MVP scope, roadmap, UX journey, success metrics, approval decision framing.
- Faker: implementation, JSON schemas, data adapters, webapp, provider-adapter code, validation/deploy after approval.
- Muyeol: copyright/style-copy/privacy/public-safe/score-overclaim/security validation and go/no-go.

## Recommended MVP boundary

Start with a Phase 1.5 MVP rather than the full product:

- Reference intake / inventory
- Per-reference visual analysis
- Design DNA profile + confidence
- Brand brief
- Art direction
- structured prompt package
- one-provider or prompt-only generation path
- DNA Match / Brand Fit evaluation
- critique/action list
- Chris approval checkpoint

Defer automatic multi-iteration generation, LoRA/fine-tuning, full brand expansion, multiple provider comparison, organization/team DNA, print production automation, and full Figma/Photoshop replacement.

## Data architecture pattern

Prefer a private project data root outside the public webapp repo, for example:

```text
/opt/data/design-dna-studio/
  PROJECT_DESIGN_DNA.md
  /projects/<project_id>/
    /references/source_images/
    /references/reference_index.json
    /references/reference_analysis.jsonl
    /design_dna/DESIGN_DNA.md
    /design_dna/design_dna.json
    /design_dna/color.json
    /design_dna/typography.json
    /design_dna/composition.json
    /design_dna/motifs.json
    /brand/BRAND_BRIEF.md
    /brand/brand.json
    /research/market.md
    /research/competitors.md
    /research/research_signals.jsonl
    /direction/ART_DIRECTION.md
    /direction/art_direction.json
    /prompts/prompt_packages/*.json
    /generations/iteration_01/
    /evaluation/dna_scores.json
    /evaluation/brand_scores.json
    /evaluation/critique.md
    /evaluation/refinement_actions.json
    /decisions/decisions.md
    /decisions/decisions.jsonl
    /feedback/user_feedback.jsonl
    /feedback/preference_weights.json
    /public/public_manifest.json
```

Keep original references/private analysis out of GitHub Pages. Expose only public-safe manifests and selected assets.

## Design DNA extraction method

Analyze references by repeated visual decision patterns, not captioning or copying. At minimum track:

- Color
- Typography
- Composition
- Shape & Geometry
- Graphic Motif
- Texture
- Photography
- Visual Density
- Mood

For every conclusion, separate `FACT`, `INFERENCE`, `PREFERENCE`, and `DECISION`. Store confidence and evidence counts; show low/medium/high confidence rather than hiding ambiguity.

## Evaluation / refinement principles

Evaluation must produce actions, not just scores:

- What worked
- What did not work
- Why
- What to change
- How much to change
- Next generation instruction

Treat DNA Match and Brand Fit scores as model-estimated alignment, never objective truth. Chris's design judgment has final authority. Default max iterations is 3, with human checkpoints for Design DNA approval, Art Direction approval, final selection, and expansion approval.

## Provider strategy

Keep image providers replaceable. Use a canonical Prompt Package as the source of truth, then adapt it to OpenAI/Gemini/Kling/Midjourney/FAL/Higgsfield/future models. Midjourney can be prompt-only/manual execution: Hermes owns art direction, prompt engineering, evaluation, and refinement even if Chris runs the external generator.

## Common pitfalls

- Starting by coding or generating images before architecture assessment and Chris approval.
- Treating reference images as style-copy targets rather than design-logic evidence.
- Putting private reference images or local paths into public webapp data.
- Adding a new specialist agent when GoYJ/Yuna/Son/Faker/Muyeol can cover the work.
- Letting provider-specific prompt details become the product architecture.
- Reporting aesthetic scores as objective measurements.
