# Kling AI video generation fallback for Chris

Use this when Higgsfield credits block turntable/video generation and Chris wants to try Kling AI instead.

## Recommended lanes

### 1. Official Kling CLI for Chris's existing Kling account

This is the safest first path when Chris says he already has Kling AI credits/account access.

- Install/update under the user's writable npm prefix, not `/usr/local`:
  ```bash
  export PATH="/opt/data/.npm-global/bin:$PATH"
  npm install -g --prefix /opt/data/.npm-global @klingai/cli-global@latest
  kling --version
  ```
- Use `HOME=/opt/data` for Karina/default, or the specialist profile home for Go Youn-jung-owned runs:
  ```bash
  HOME=/opt/data kling login
  HOME=/opt/data kling who_am_i --quiet
  HOME=/opt/data kling account --quiet
  ```
- In a headless Hermes host, `kling login` prints an authorization URL and waits on a local callback such as `http://127.0.0.1:8787/callback?...`.
  1. Ask Chris to open the authorization URL in his browser.
  2. If his browser lands on a failed localhost callback page, ask him to paste the full callback URL only.
  3. Call that URL from the Hermes host while `kling login` is still waiting, so the local listener receives the OAuth code.
  4. Never ask for or print tokens, passwords, cookies, or raw credential files.

Useful commands after login:

```bash
HOME=/opt/data kling who_am_i --quiet
HOME=/opt/data kling tool_list --quiet
HOME=/opt/data kling image_to_video --model <model> --image ./input.png "slow premium product turntable, gentle orbit camera" --duration 5 --aspectRatio 1:1 --poll 300
HOME=/opt/data kling query_tasks <generationId> --poll 300
```

Generated asset URLs appear in `works[].url` or `works[].url_without_watermark` when available.

### 2. Native Hermes MCP server route

Use this when Chris has Kling Developer Console credentials or wants first-class MCP tools inside Hermes.

- Hermes native MCP requires a configured MCP server and an agent restart for discovered tools to appear.
- For the community `mcp-kling` server, Kling Developer Console credentials are required:
  - `KLING_ACCESS_KEY`
  - `KLING_SECRET_KEY`
- Add with environment variables rather than editing secrets into chat:
  ```bash
  hermes mcp add kling --command npx --args -y mcp-kling@latest --env KLING_ACCESS_KEY=... KLING_SECRET_KEY=...
  ```
- Restart the relevant gateway/profile after adding the MCP server.
- Tool names will be prefixed like `mcp_kling_*` after discovery.

### 3. RunAPI Kling MCP alternative

`@runapi.ai/kling-mcp` is a separate RunAPI-based Kling route. It can inspect pricing before login, but actual generation requires RunAPI login/API key, not necessarily Chris's direct Kling account credits.

```bash
hermes mcp add kling_runapi --command npx --args -y @runapi.ai/kling-mcp
```

Use this only if Chris intends to use RunAPI billing/credentials.

## Integration notes for Go Youn-jung visual loop

- Treat Kling as a fallback video/turntable lane, not a silent replacement for Higgsfield still-image generation.
- Preserve Chris's visual quality bar: premium, calm, tactile, not generic AI-startup, no unnecessary glow/glass/neon.
- Store generated video URLs/files, prompt, model, task ID, and credit/account status notes under the same daily visual log folder pattern used for Higgsfield.
- For specialist-owned execution, verify the profile-local `HOME` login state before scheduled use; do not assume Karina/default's Kling credentials exist under Go Youn-jung's profile home.

## Pitfalls

- `npm install -g` may try `/usr/local` and fail with permissions. Use `--prefix /opt/data/.npm-global` and export that bin path.
- The official Kling CLI is a thin MCP client but is not itself the same as registering native Hermes MCP tools. CLI automation can work immediately after login; native MCP requires config plus restart.
- Developer/API credentials and user OAuth login may draw from different credit pools. Confirm which billing pool Chris intends to use before scheduling recurring generations.
