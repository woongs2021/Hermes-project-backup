# Threads read-only analysis integration

Use when Chris wants Hermes to read his Threads posts for summaries, pattern analysis, or next-content advice.

## Product boundary

- Default to **read-only** access and workflow.
- Goal: retrieve Chris's own posts and permitted public performance data, then summarize themes, writing patterns, and opportunities for the next post.
- Do **not** draft-to-platform, publish, schedule, reply, like, repost, follow, or alter Threads content unless Chris explicitly asks for that separate action.
- Treat an OAuth grant for reading as permission to retrieve data, not permission to act on the account.

## Recommended setup

1. Create/configure a Meta Developer app with Threads API access.
2. Register a controlled OAuth redirect URI.
3. Request only `threads_basic` for initial own-profile/post analysis. Add `threads_manage_insights` only if performance metrics are needed. Never request `threads_content_publish` for this workflow.
4. Store refresh/access credentials only in the platform's private credential store or runtime secret configuration; never in repositories, public manifests, task logs, or chat.
5. After authorization, make a small read-only sample request first (for example recent posts) and show the retrieved scope/data shape before adding a recurring collection job.

## OAuth callback deployment: mandatory sequence

Threads authorization-code exchange requires the Threads App Secret. Therefore a static page (including GitHub Pages) cannot be the callback processor.

1. Build a server-side HTTPS callback with a `/oauth/threads/start` route and an exact `/oauth/threads/callback` route.
2. Generate a high-entropy state nonce, keep it in an `HttpOnly; Secure; SameSite=Lax` short-lived cookie, and validate it on callback before code exchange.
3. Deploy the callback first. Only then give the user the *exact* deployed callback URI to register in Meta. Never invent an expected `workers.dev` hostname.
4. Store `THREADS_APP_ID` and `THREADS_APP_SECRET` as runtime secrets. Never ask for them in chat, show them in screenshots, commit them, or put them in GitHub Actions logs.
5. Exchange the code server-side, keep token responses out of HTML/logs, and clear the state cookie on every callback path.

### Cloudflare Worker via GitHub Actions

Use this when a standalone secure callback is needed and Chris chooses Cloudflare.

- Create a **private** repository containing the worker; include `.env`/`.dev.vars` in `.gitignore`.
- Before first deploy, the Cloudflare account owner must register a `workers.dev` subdomain in Cloudflare Dashboard → **Workers & Pages**. CI cannot safely answer that interactive first-run prompt.
- The owner creates a least-privilege Cloudflare Workers edit API token and saves it directly as GitHub repository secret `CLOUDFLARE_API_TOKEN`; never paste it into chat.
- Pin a current Wrangler version in `package.json` and use `npm ci` plus `npx wrangler deploy` in CI. Do not depend on an action's implicit Wrangler installer, which can conflict with the project's Workers types/version.
- Once deployment succeeds, copy the exact public origin from Wrangler output and append `/oauth/threads/callback`; register that precise URI in Meta's valid OAuth redirect URI field. `/oauth/threads/start` is only the URL that starts login.
- Add the two Threads credentials directly in Cloudflare Worker secret settings as `THREADS_APP_ID` and `THREADS_APP_SECRET`, then test only a small own-post read.
- Do not give the user an interactive `wrangler login` URL from a remote agent: it is bound to the agent host's localhost callback and will fail from the user's device.

## Analysis output

Keep the first delivery practical:

- compact summary of recent post themes and narrative through-line
- recurring writing voice/structure patterns
- notable engagement signals where authorized and available
- 3–5 next-content directions, with rationale and an optional opening-angle suggestion

Do not claim model fine-tuning. Treat the collected posts as a private, editable retrieval corpus so removals and changing editorial direction can take effect without retraining.

## Privacy guardrails

- Exclude direct messages and private audience data by default.
- Minimize retention: keep normalized post text and permitted public metrics only when needed for the approved analysis workflow.
- Keep OAuth callback URLs, authorization codes, app secrets, access tokens, and raw API responses out of agent logs and user-facing summaries.
