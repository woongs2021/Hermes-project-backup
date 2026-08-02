# Session note: creating role-agent profiles yuna / son / faker / muyeol

Role profiles created:
- `yuna`: research agent for market research, paper search, benchmarking, insight synthesis
- `son`: PM agent for planning, prioritization, roadmap, task breakdown, coordination
- `faker`: coding agent for implementation, debugging, prototyping, automation, technical review
- `muyeol`: validation/security agent for fact-checking, QA, risk analysis, security review, final audit

Observed setup behavior:
- `hermes --profile <name> setup --non-interactive` printed non-interactive guidance but did not populate the model field.
- `hermes --profile <name> auth list` showed inherited/copied OAuth credentials for `nous` and `openai-codex` without needing raw secrets.
- Direct config set worked for all profiles:
  - provider `openai-codex`
  - model `gpt-5.5`
  - base URL `https://chatgpt.com/backend-api/codex`
  - terminal backend `local`
- Each profile passed a one-shot smoke test with `hermes --profile <name> chat -Q -q "Smoke test: reply with exactly OK-<name>"`.

Reporting distinction:
- Profiles were ready for CLI/worker use after smoke tests.
- Their individual gateways remained stopped, which is normal unless explicitly started.