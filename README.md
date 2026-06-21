# animesh-product-builder-skills

[![validate](https://github.com/animesh-builds/animesh-product-builder-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/animesh-builds/animesh-product-builder-skills/actions/workflows/validate.yml)

A planning skill for [Claude Code](https://docs.claude.com/en/docs/claude-code). It helps you turn a rough idea into a documented, build-ready plan before any code gets written. It is distributed through the `animesh-skills` plugin marketplace.

## What it does

The skill acts as a planning partner, not a coder. You talk through the idea, and it writes a set of planning documents into a local `_planning/` folder: the requirements, the architecture, the design, the decisions you made and the reasons for them, and a handoff file for whoever builds it next. When the plan is ready, you hand it to Claude Code (or any engineer) and the build starts from a clear spec instead of guesswork.

It also keeps your planning private. The `_planning/` folder is gitignored and never pushed, so only your code ends up on the remote.

## Quick start

### If you use Claude Code

Add the marketplace, then install the skill:

```
/plugin marketplace add animesh-builds/animesh-product-builder-skills
/plugin install animesh-product-builder-skills@animesh-skills
```

Restart Claude Code if it asks. After that you can run `/animesh-product-builder-skills`, or just describe a planning task and the skill activates on its own.

### If you only have this link (no install)

You can use it without installing anything. Paste this into a new Claude session:

> Read https://raw.githubusercontent.com/animesh-builds/animesh-product-builder-skills/main/skills/animesh-product-builder-skills/SKILL.md and act as the planning partner it describes. Fetch the files it references under `references/` from the same repo when you need them. Start by asking me the discovery questions.

This works on any Claude surface that can read a web page.

## For an AI agent reading this repo

If you have been pointed at this repository to act as the skill, do this:

1. Read `skills/animesh-product-builder-skills/SKILL.md`. That file is your operating instructions.
2. Open files under `skills/animesh-product-builder-skills/references/` only when you need them (the templates, the workflow steps, the git-safety steps). Do not load everything up front.
3. Follow `references/workflow.md`: run discovery first, then write one document at a time into the project's `_planning/` folder, pausing for review after each.
4. Write files to disk. Do not paste whole documents into chat.
5. Never commit or push anything under `_planning/`. Set up the gitignore and pre-commit guard from `references/git-safety.md` before the project's first commit.

## What you get

The skill builds a planning kit under `_planning/`:

- `prd.md`: what you are building and why
- `architecture.md`: tech stack, data model, API, non-functional requirements, security, risk and rollback
- `content-guide.md` and `design-language.md`: voice and visual system
- `setup-guide.md` and `gitignore-guidance.md`: dev environment and what stays local
- `decisions.md`: a short log of each significant decision and the reasoning behind it
- `session-history.md`: notes that carry context across sessions
- `CLAUDE.md` (committed) plus `_planning/claude-context.md` (private handover)

It scales to the project. Lite tier is for prototypes, Standard for MVPs and internal tools, Full for products that ship or handle regulated data. The skill confirms the tier during discovery and adjusts the document set.

## How the two zones work

The skill treats your repo as two zones in one folder. The code zone is your application source, committed and pushed as normal. The planning zone (`_planning/`) is local only, gitignored, and never pushed. The skill writes the gitignore entries, installs a pre-commit guard, and checks that the planning zone is excluded before your first commit. The committed `CLAUDE.md` holds only conventions that are safe to share. Anything private stays in `_planning/`.

## About this edition

This is the essentials edition, a complete and working kit. The author keeps a fuller private edition with deeper templates and a few extra documents (an AI spec, a dedicated testing strategy, a domain glossary, and a more detailed architecture template). The essentials edition is enough to plan and ship a real project on its own.

## Repo layout

```
.
├── .claude-plugin/marketplace.json   # plugin manifest
├── skills/
│   └── animesh-product-builder-skills/
│       ├── SKILL.md                  # the skill's instructions
│       └── references/               # templates, workflow, git-safety (loaded on demand)
├── scripts/validate_bundle.py        # checks the bundle is well-formed
└── LICENSE
```

## Validation

`scripts/validate_bundle.py` checks the manifest, the skill frontmatter, and that no private files slipped in. Run it with `python3 scripts/validate_bundle.py`. A GitHub Action runs the same check on every push.

## License

[MIT](LICENSE)
