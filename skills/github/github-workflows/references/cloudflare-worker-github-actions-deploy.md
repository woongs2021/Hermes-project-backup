# Cloudflare Worker deployment through GitHub Actions

Use this when a private repository deploys a Cloudflare Worker with a repository secret rather than an interactive local `wrangler login`.

## Safe setup

1. Create the repository as **private** and confirm its remote before pushing.
2. In GitHub repository **Settings → Secrets and variables → Actions**, add `CLOUDFLARE_API_TOKEN`. Never place the token in a workflow, `.env`, commit, chat, or screenshots.
3. Install a project-pinned Wrangler version as a dev dependency, then use the same version in CI. This avoids action-managed version drift and peer-dependency conflicts.
4. Prefer this workflow shape:

```yaml
- uses: actions/checkout@v4
- uses: actions/setup-node@v4
  with:
    node-version: 22
    cache: npm
- run: npm ci
- run: npx wrangler deploy
  env:
    CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
```

5. Before the first `workers.dev` deployment, the Cloudflare account must register its account-level `workers.dev` subdomain. If no subdomain exists, have the account owner open **Workers & Pages → Create application → Start with Hello World**, choose the intended Worker name, and complete the initial placeholder deploy. The GitHub deployment then overwrites that placeholder Worker with the repository code.
6. Trigger the workflow after the Secret and `workers.dev` subdomain exist. Verify the completed run is `success`, then request the live Worker root endpoint and confirm the expected non-sensitive response.

## OAuth callback additions

- A callback URL is not an authorization start URL. Opening it directly should fail state validation; this is expected and should not be treated as a deployment failure.
- Add the exact callback URL to the provider configuration, but start consent at the Worker’s separate authorization-start endpoint.
- Keep provider client ID and client secret as Cloudflare Worker Secrets, not GitHub repository variables. Use the provider-specific OAuth client pair; do not substitute a parent-platform app ID/secret when the provider exposes a distinct pair.

## Pitfalls

- A `push` trigger and a manual `workflow_dispatch` trigger can produce two runs. Explain that these are deployment attempts, not necessarily two deployed Workers, and inspect each run before retrying.
- Do not ask the user for a Cloudflare Account ID when a `workers.dev` subdomain or worker URL is needed.
- Do not direct users to a server-local `wrangler login` authorization URL. It is tied to the initiating machine’s localhost callback and cannot be completed from their device.
