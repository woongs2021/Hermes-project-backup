---
name: platform-messaging-operations
description: "Operate social and messaging platforms safely: X/Twitter via xurl and Yuanbao group/DM workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [social-media, messaging, platform-operations, x, twitter, xurl, yuanbao, group, dm]
    related_skills: [xurl, yuanbao]
---

# Platform Messaging Operations

Use this umbrella when the user asks to read, post, reply, DM, mention, search, or otherwise operate an external social/messaging platform from Hermes. It consolidates platform-specific operational skills into one class-level workflow with labeled subsections and detailed provider notes in `references/`.

## Universal workflow

1. Identify the platform and requested action: read/search, compose, reply, quote, DM, mention, moderation/social graph action, or media upload.
2. Load the platform subsection below before calling any tool or CLI.
3. For read-only actions, verify credentials/tool availability with the platform's safe status command, then fetch a small sample before doing broad work.
4. For write actions (posting, replying, liking, reposting, following, blocking, deleting, DMs, group mentions), confirm the exact target and message unless the current gateway message itself is already the final platform response.
5. Never expose credentials, token files, auth headers, private chat dumps, or platform secrets to the conversation.
6. Prefer structured outputs returned by the platform tools/CLIs; parse JSON directly where available.

## X/Twitter via `xurl`

Use for X/Twitter posting, reading, search, timeline/mentions, engagement, social graph, DMs, media upload, or raw X API v2 access.

Detailed commands, setup instructions, safety rules, and troubleshooting are in `references/xurl.md`.

Key rules:

- Never read or print `~/.xurl`; only verify with `xurl auth status`.
- Never ask the user to paste client secrets or tokens into chat.
- Never run `xurl` with inline credential flags or verbose mode.
- If auth is missing, direct the user to do the one-time xurl setup outside the agent session.
- For write actions, confirm the target post/user and text before executing.

## Yuanbao group and DM workflows

Use for Yuanbao (元宝/派) group info, member lookup, @mentions, and private/direct messages.

Detailed gateway behavior and tool patterns are in `references/yuanbao.md`.

Key rules:

- In a Yuanbao group, the assistant's final text reply is the message sent to the group.
- To @mention someone, query group members first for the exact nickname, then include `@nickname` in the final reply.
- Do not claim you cannot @mention users; the gateway handles mention conversion.
- Use `yb_send_dm` for Yuanbao DMs, not generic `send_message`.
- Extract `group_code` from the Yuanbao chat id when needed.

## Choosing a platform subsection

| User asks for... | Use subsection |
| --- | --- |
| tweet, post on X, read/search X, Twitter DM, X media upload | X/Twitter via `xurl` |
| 元宝, 派, group member, 艾特/@mention in Yuanbao, Yuanbao DM | Yuanbao group and DM workflows |

## Package hygiene

Platform-specific quirks that are too detailed for the umbrella should live under `references/<platform>.md`. Reusable starter payloads belong in `templates/`, and deterministic probes or verification helpers belong in `scripts/`.
