# Higgsfield CLI generation workflow

Use this when Chris wants images/videos generated with Higgsfield while Hermes/Karina/Go Youn-jung handle direction, prompt writing, and critique.

## Operating model

- Treat GPT/Hermes as the design director: brief, prompt, model/option selection, result review, and iteration logic.
- Treat Higgsfield as the generation studio: actual image/video creation consumes Higgsfield credits rather than GPT image-generation budget.
- For Chris, prefer Higgsfield generation when credits are available; fall back only when credits/model fit/quality blocks the task.

## Setup and verification

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
higgsfield version
higgsfield model list --image
higgsfield model get gpt_image_2
```

If global install hits `/usr/local` permissions, use a user npm prefix rather than sudo:

```bash
npm config set prefix /opt/data/.npm-global
export PATH="/opt/data/.npm-global/bin:$PATH"
npm install -g @higgsfield/cli
```

## OAuth loopback callback pattern

`higgsfield auth login --port <port>` starts a loopback server and prints an authorization URL. On remote/chat environments, the user's browser may reach `localhost` on their own device, not the agent host.

Workflow:

1. Start login in a tracked terminal/background process:

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
higgsfield auth login --port 8765
```

2. Send the printed `https://clerk.higgsfield.ai/oauth/authorize?...` URL to the user.
3. If their browser ends on a failed `http://localhost:8765/callback?code=...&state=...`, ask them to paste the full callback URL.
4. From the agent host, call that exact callback URL locally so the waiting CLI receives the code:

```bash
curl -sS 'http://localhost:8765/callback?code=...&state=...' >/tmp/higgsfield-auth.html
```

5. Wait/poll the login process and verify it reports `Successfully authenticated.`
6. Verify authenticated access with a non-secret command such as:

```bash
higgsfield model list --image --json >/tmp/hf_models.json
```

Never print access tokens from `higgsfield auth token`.

## Generation pattern

Inspect params before choosing options:

```bash
higgsfield model get gpt_image_2
```

### Known CLI pitfall: S3 `SignatureDoesNotMatch` on local uploads

If local image/video reference upload fails with an AWS S3 `SignatureDoesNotMatch` XML error, first check the Higgsfield CLI version. Older builds can produce invalid presigned upload requests. Updating the user-prefix global CLI fixed this in practice:

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
higgsfield version
npm view @higgsfield/cli version
npm install -g @higgsfield/cli@latest
higgsfield version
```

After updating, retry the same `higgsfield generate create ... --image-references <local-file>` command before changing the prompt or assets.

Example:

```bash
higgsfield generate create gpt_image_2 \
  --aspect_ratio 1:1 \
  --quality high \
  --resolution 2k \
  --prompt "<design brief style prompt>" \
  --wait
```

## Prompting guidance for design artifacts

Write prompts like design briefs, not just image captions:

- purpose and audience
- channel/aspect ratio
- core message
- information architecture
- layout system
- typography hierarchy
- spacing/density
- semantic color and emotional tone
- what to avoid, especially generic neon/glass AI startup aesthetics
- text legibility constraints
- success criteria

For Korean-heavy infographics, prefer short labels. If generated Korean text is broken or crowded, switch to HTML/SVG/editable-card production or use Higgsfield for background/visual language only.

## Logo/text-on-mockup workflow

When compositing brand marks onto product mockups:

1. Generate a pattern-only/product-surface version first.
2. If exact text is required, create the logo as a separate transparent PNG/SVG-like image with the requested font/color/no-shadow rules and pass it as an image reference. Do not ask the model to invent the text from prompt alone.
3. Prompt the model to integrate the logo as physical ink on a specific bright/printable surface, following perspective, curvature, grain, and lighting.
4. Make a contact sheet and inspect naturalness before replacing web assets. If the logo still feels like a digital overlay, the better design call may be to remove it and keep the pattern-only mockup.
5. Keep web manifests honest: remove logo metadata when the final asset has no logo.

This is especially important for Chris's Design DNA / DNA Brand Asset work, where natural brand-surface integration is preferred over forced logo legibility.

## Logo-on-mockup fusion pattern

When Chris asks for a logo on a generated product/package mockup, avoid treating the logo as a simple post-process text overlay unless the user explicitly wants flat annotation. Chris prefers the logo to feel physically printed or embedded in the surface, even if the full word is not visible in every crop.

Recommended workflow:

1. Generate or prepare the mockup/pattern composite first without text if possible.
2. Render the approved logo text as a clean transparent PNG reference using the requested font (for example Open Sans), with no drop shadow, glow, stroke, or emboss.
3. Use Nano Banana Pro with two references: the prepared mockup composite and the logo PNG.
4. Prompt for natural material integration: printed ink, surface curvature/perspective, paper/fabric/sign grain, lighting inheritance, and no floating digital overlay.
5. Review for naturalness before total legibility. One clearly readable hero example is enough if the set overall feels more physically plausible.
6. If the logo feels too much like a pasted-on label, reduce scale and move it to a bright corner/surface area rather than forcing a large centered mark. For Chris's brand mockups, small corner marks (e.g. ~30% scale, navy on a light area) can read more premium and natural than large high-contrast hero logos.
7. When the user asks for a specific scale/color/placement correction, regenerate the logo PNG reference at that scale/color first, then re-run Nano Banana Pro with explicit placement language (corner, bright background, subtle printed ink, not centered). Do not just resize a deterministic overlay unless the user prefers exactness over physical integration.
8. Only fall back to deterministic text overlay when exact spelling/positioning matters more than natural mockup integration.
