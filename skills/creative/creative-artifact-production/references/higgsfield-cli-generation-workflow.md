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
