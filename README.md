# animesh-product-builder-skills

[![validate](https://github.com/animesh-builds/animesh-product-builder-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/animesh-builds/animesh-product-builder-skills/actions/workflows/validate.yml)

> Plan your software project properly before you build it. A planning skill for [Claude Code](https://docs.claude.com/en/docs/claude-code).

**New here?** Jump to [how to try it](#installing-it-or-trying-it-with-no-install). It takes about a minute, and there is a no-install option if you just want to see it work.

## About the author

Animesh is an AI builder and product manager working at the intersection of payments, fintech, and agentic commerce, and building in public the whole way.

He builds the systems that sit behind modern checkout: AI-powered risk decisioning, conversational and agentic checkout, MCP-enabled multi-step payment execution, and the orchestration logic that ties checkout, settlement, and refunds into reliable flows. His work spans the full payments surface, from UPI and card flows to pre-authorization for high-value orders, EMI and offers, intelligent gateway routing, and cross-border multi-currency payments.

Beyond product, Animesh ships agentic AI hands-on. His experiments include a WhatsApp AI agent (OpenClaw), an AI decisioning copilot for auto lending (AutoLendingOS), a citation-grounded personal "second brain," and an AI assistant embedded in Slack. Small, real builds that probe where agentic interfaces and autonomous commerce are actually heading.

He writes about all of it (AI, product strategy, fintech, and building in public) through Build Signals, his newsletter and YouTube channel.

An IIM Calcutta MBA and an Electronics & Communication engineer from VNIT Nagpur, Animesh pairs product judgment with a builder's instinct to ship. Always up for a conversation on agentic AI, payments, or the future of commerce.

**Find me here:**

- Website: https://animeshgiradkar.com
- Newsletter: https://buildsignals.substack.com/
- YouTube: https://youtube.com/@buildsignals
- GitHub: https://github.com/animesh-builds
- X: https://x.com/animeshbuilds
- Email: hello@animeshgiradkar.com (or animeshg.connect@gmail.com)

*Disclaimer: Content here is informational, not promotional. Views are my own and do not reflect any past or present employer or academic institution. Please do your own research before acting on anything shared. I respect copyrights, so reach out with any concerns.*

---

## A planning partner, not a coder

The skill acts as a planning partner, not a coder. You talk your idea through with it, and it writes up a clean plan: what you are building, how it fits together, the decisions you made along the way, and a handoff note for whoever codes it. The build then starts from a real spec instead of a fuzzy memory of a conversation.

## The "why did we decide that?" problem it fixes

Most projects start with a great conversation and, three weeks later, a quiet "wait, why did we decide that?" The thinking lives in someone's head or scattered across old chats, and whoever builds it (usually future-you) ends up guessing.

This skill catches that thinking and writes it down while it is still fresh. Your code ships to GitHub as normal. Your planning stays on your machine.

## A planning session, start to finish

You say:

> New project: a small tool that nudges my team to log their hours.

It asks a handful of questions first. Who is it for? How serious is this, a weekend hack or something real? Any payments or sensitive data? Then it writes `_planning/prd.md` and stops so you can read it. You say `next doc`, it writes the architecture. And so on, one file at a time, pausing for you to react.

When the plan is solid, you say `ready for Claude Code` and it hands you a short brief to paste into a fresh build session. That is the whole loop: you talk, it documents, you review.

## Installing it (or trying it with no install)

**On Claude Code,** install it:

```
/plugin marketplace add animesh-builds/animesh-product-builder-skills
/plugin install animesh-product-builder-skills@animesh-skills
```

Restart if it asks. Then type `/animesh-product-builder-skills`, or just say "new project: ..." and it wakes up on its own.

**Only have the link and want to try it right now?** You do not need to install anything. Paste this into a new Claude chat:

> Read https://raw.githubusercontent.com/animesh-builds/animesh-product-builder-skills/main/skills/animesh-product-builder-skills/SKILL.md and act as the planning partner it describes. Pull in the files it points to under `references/` when you need them, and start by asking me the discovery questions.

## The planning documents it produces

Everything lands in a `_planning/` folder inside your project:

- `prd.md`: what you are building and why
- `architecture.md`: how it is put together, including the stack, data, API, security, and the parts most likely to break
- `content-guide.md` and `design-language.md`: how it should sound and look
- `setup-guide.md` and `gitignore-guidance.md`: getting it running, and keeping secrets out of git
- `decisions.md`: a running log of the calls you made and the reasons behind them
- `session-history.md`: where you left off, so you can pick the thread back up later
- `CLAUDE.md` and `_planning/claude-context.md`: the handoff for the build phase

Not every project needs all of that. The skill picks a tier with you at the start. Lite for a weekend build, Standard for a real MVP, Full for something that ships or handles regulated data, and it sizes the kit to fit.

## How it keeps planning docs out of your remote

The skill treats your repo as two halves. Your application code is committed and pushed like always. The `_planning/` folder is gitignored and never leaves your machine. To make that stick, the skill writes the gitignore rules, adds a pre-commit guard, and checks the planning folder is actually excluded before your first commit. The `CLAUDE.md` it commits holds only the conventions that are safe to share. Anything sensitive stays in `_planning/`.

## This edition vs the fuller private one

This is the essentials edition. It is complete and genuinely useful on its own. There is also a fuller private edition with deeper templates and a few extra documents (an AI spec, a testing strategy, a glossary, and a heavier architecture template), but you do not need it to get real work done with this one.

## Instructions for an AI agent running this skill from the repo

If you are an agent asked to run this skill straight from the repository:

1. Read `skills/animesh-product-builder-skills/SKILL.md`. Those are your instructions.
2. Open the files in `references/` only when you need them, not all at once.
3. Follow `references/workflow.md`: ask the discovery questions, then write one document at a time into `_planning/`, pausing after each.
4. Write to disk. Do not paste whole documents into the chat.
5. Never commit or push `_planning/`. Set up the guard from `references/git-safety.md` first.

## What's in this repository

```
.
├── .claude-plugin/marketplace.json   # plugin manifest
├── skills/
│   └── animesh-product-builder-skills/
│       ├── SKILL.md                  # the instructions
│       └── references/               # templates, workflow, git-safety
├── scripts/validate_bundle.py        # sanity-checks the bundle
└── LICENSE
```

## How the bundle stays clean (validation)

`scripts/validate_bundle.py` checks the manifest, the skill's frontmatter, and that no private files slipped in. Run `python3 scripts/validate_bundle.py`. The same check runs in CI on every push.

## License

[MIT](LICENSE)
