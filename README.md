# animesh-product-builder-skills

Think your software project all the way through before you build it. A free skill for [Claude Code](https://docs.claude.com/en/docs/claude-code).

**New here?** Skip to [how to start](#how-to-start). It takes about a minute, and you can try it without installing anything.

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

## What it is

A planning partner you talk to before you write any code. It does not build the thing for you. You describe what you have in mind, it asks good questions, and it helps you turn the idea into a clear, written plan. By the time you are done, the decisions are made and written down, so building it later is the easy part.

## Why it helps

Most projects start with a great conversation. A few weeks in, nobody quite remembers why things were decided the way they were, because none of it was written down. This catches your thinking while it is fresh and keeps it somewhere you can actually find it.

## What it feels like

You start with something simple, like "a small tool that reminds my team to log their hours." It asks a few quick questions: who is this for, is it a weekend experiment or the real thing, anything sensitive involved. Then it writes the plan out a piece at a time and pauses so you can read each part and push back. When you are happy, it hands you a tidy summary you can give straight to whoever builds it.

No forms. No setup ritual. You talk, it does the organizing.

## What you walk away with

One clear plan for your project, in one place: what you are building and why, how it should work, how it should look and sound, the choices you made and the reasons behind them, and enough notes that you can stop today and pick it back up next week. It stays in your own project folder, on your machine, not posted anywhere public.

## How to start

There are two ways in, depending on what you use.

### Install it in Claude Code

Skills live in Claude Code (the coding app), so that is where you install one for good. Run these two lines:

```
/plugin marketplace add animesh-builds/animesh-product-builder-skills
/plugin install animesh-product-builder-skills@animesh-skills
```

Restart if it asks. Then say "new project: ..." and it takes over from there.

### Try it in a normal Claude chat (no install)

Using Claude on the web or in the app instead? You cannot install a skill there, but you can still use it for a session. Paste this into a fresh chat:

> Read https://raw.githubusercontent.com/animesh-builds/animesh-product-builder-skills/main/skills/animesh-product-builder-skills/SKILL.md and act as the planning partner it describes. It points to other files using relative paths like `references/workflow.md` and `references/templates/prd.md`. Resolve those against the folder that SKILL.md is in (keep the same URL prefix) and fetch them whenever it needs one. Start by asking me a few questions about my project.

If your Claude cannot open web links, copy the contents of that page into the chat instead.

## License

Free to use under the [MIT license](LICENSE).
