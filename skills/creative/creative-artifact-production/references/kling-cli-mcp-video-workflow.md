# Kling AI CLI / MCP-style Video Workflow for Chris

Use this when Higgsfield credits block video or turntable generation and Chris wants to try Kling AI as the fallback generation studio.

## Preferred integration path

1. **Start with the official Kling CLI when Chris has a normal Kling account.**
   - Install under the user npm prefix, not system `/usr/local`, when permissions are restricted:
     ```bash
     npm install -g --prefix /opt/data/.npm-global @klingai/cli-global@latest
     export PATH="/opt/data/.npm-global/bin:$PATH"
     ```
   - Use `HOME=/opt/data kling ...` for the default/Karina profile, or `HOME=/opt/data/profiles/<profile>/home kling ...` for a specialist profile if credentials should live there.
   - The CLI is a thin client over Kling's MCP backend and supports commands such as `who_am_i`, `account`, `text_to_image`, `image_to_image`, `text_to_video`, `image_to_video`, `query_tasks`, and `file_upload`.

2. **Use native Hermes MCP only when an MCP server and credentials are clear.**
   - Community `mcp-kling` usually needs Kling Developer Console `KLING_ACCESS_KEY` and `KLING_SECRET_KEY`.
   - `@runapi.ai/kling-mcp` uses RunAPI login/API key, not necessarily Chris's direct Kling account credits.
   - Do not assume these share the same credit pool as Chris's normal Kling web account.

## Headless OAuth login pattern

1. Start login in a PTY so the authorization URL is visible promptly:
   ```bash
   export PATH="/opt/data/.npm-global/bin:$PATH"
   HOME=/opt/data kling login
   ```
   If running via Hermes, use a tracked background process with `pty=true`.

2. Send Chris only the currently active `https://kling.ai/auth/authorize?...` URL.

3. Chris opens it, approves, then the browser may fail at a local callback like:
   ```text
   http://127.0.0.1:8787/callback?code=...&state=...
   ```

4. While the login process is still waiting, call that callback URL from the Hermes host:
   ```bash
   curl 'http://127.0.0.1:8787/callback?code=...&state=...'
   ```

5. Verify login without printing credentials:
   ```bash
   HOME=/opt/data kling who_am_i --quiet
   HOME=/opt/data kling account --quiet
   ```

## Pitfalls

- **State mismatch:** if multiple login attempts were started, only the callback whose `state=` matches the currently running login process will work. Kill old attempts, keep one active process, and tell Chris which URL is current. A callback from a timed-out or older process returns `state mismatch`.
- **Timeout:** Kling login can time out after about 300 seconds. If that happens, start a fresh login and discard all older authorization/callback URLs.
- **Buffered output:** non-PTY background login may not show the URL until exit. Use `pty=true` for interactive OAuth flows.
- **Credential hygiene:** never paste tokens, raw credentials, or Kling auth files into chat/logs. Ask Chris for the browser callback URL only.
- **Profile-local auth:** Go Youn-jung/Faker cron jobs may run with profile-specific `HOME`; if they need to generate with Kling directly, login or copy credentials deliberately into that profile home with restrictive permissions, without exposing secrets.

## Turntable fallback shape

For Higgsfield turntable replacement:

1. Generate or select a still image asset first.
2. Upload local image if needed:
   ```bash
   HOME=/opt/data kling file_upload ./image.png
   ```
3. Use `image_to_video` with a restrained turntable prompt: slow 360-degree object rotation, fixed camera distance, soft studio lighting, seamless loop intent, no text, no extra objects, no morphing.
4. Poll with `query_tasks` until complete, download the result URL, and verify the video file exists/plays before reporting success.
