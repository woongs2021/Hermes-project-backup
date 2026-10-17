# Son-data-grounded webapp graph handoff

Use this when Chris asks Karina to check Slack/Faker requests and make Faker apply a webapp graph using Son's real data.

## Session-proven pattern

1. **Confirm Slack state first.** Inspect the relevant team-channel request/thread and distinguish:
   - Faker's request/report exists.
   - Son has or has not replied in Slack.
2. **Do not pretend Slack reply exists.** If Son has not answered in-thread, say so and use Son's stored local loop data as the grounding source instead of inventing a Son response.
3. **Ground graph labels in actual Son data.** Useful current Son sources include:
   - `/opt/data/hermes-growth-sns-loop/events.jsonl`
   - `/opt/data/hermes-growth-sns-loop/insights.md`
   - `/opt/data/hermes-growth-sns-loop/daily/`
   - `/opt/data/hermes-growth-sns-loop/son-prep/`
   - `/opt/data/hermes-growth-sns-loop/muyeol-guardrails/`
4. **Translate Son data into graph axes.** For the OBD/Hermes webapp, a strong Son-grounded sequence is:
   - Role ontology
   - Public-safe decision log
   - Artifact relationship
   - Delegation boundary
   - Control & adoption map
   - Evaluation validity
5. **Keep public-safe quantitative loop data as support, not the source of Son interpretation.** Research counts, visual counts, final picks, and public-safe docs can support the story, but the growth questions and maturity criteria should come from Son's own growth-question/insight logs.
6. **Verify before reporting.** For the React/Vite webapp, run the same minimum gate Faker uses: `npm run validate:data`, `npm run lint`, `npm run build:public`, and `git diff --check`.
7. **Respect Chris's deployment boundary.** Local implementation and verification are okay once Chris requests application; commit/push/deploy only after Chris explicitly says to deploy.
8. **Close the Slack loop.** Reply in the original Slack thread with concise evidence: changed files, source data used, validation results, and whether deployment was held or completed.

## Pitfalls

- Do not label an implementation “Son's real Slack answer” when the only available grounding is Son's stored local logs.
- Do not let Faker's plausible Son-style copy remain in the graph after Chris asks whether real Son data was used.
- Do not expose raw private logs; use public-safe summaries, counts, and extracted concepts only.
