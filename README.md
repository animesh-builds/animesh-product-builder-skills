# animesh-skills

A growing collection of [Claude Code](https://docs.claude.com/en/docs/claude-code) skills, distributed as a plugin marketplace.

## Install

Add the marketplace, then install the plugin:

```
/plugin marketplace add animesh-builds/animesh-product-builder-skills
/plugin install animesh-product-builder-skills@animesh-skills
```

Then restart Claude Code if prompted. The skill activates automatically when relevant, or you can invoke it directly.

## Skills

### animesh-product-builder-skills

A **product architect and planning partner**. It doesn't write application code — it scopes, designs, and documents a software project so completely that you can hand it to Claude Code (or any engineer) to build with no major judgment calls left open.

It produces a local planning doc kit under `_planning/`:

- **`prd.md`** — what you're building and why
- **`architecture.md`** — tech, NFRs, testing, security, risk & rollback, observability, cost
- **`content-guide.md`** / **`design-language.md`** / **`main-content.md`** — voice, visual system, copy
- **`setup-guide.md`** / **`gitignore-guidance.md`** — environment and what stays local
- **`decisions.md`** — a lightweight ADR log (why each call was made)
- **`session-history.md`** — cross-session memory so context carries over
- **`CLAUDE.md`** (committed conventions) + **`_planning/claude-context.md`** (private handover)

Optional add-ons for jargon-heavy domains (`glossary.md`), LLM features (`ai-spec.md`), and complex test strategies (`testing.md`).

**Use it when** starting a new project, scoping or designing before writing code, setting up planning docs, resuming a planning session, adding the kit to an existing (brownfield) codebase, or preparing a "ready for Claude Code" handoff.

**Tiers:** Lite (prototypes), Standard (MVPs/internal tools), Full (shippable / regulated products) — the skill confirms the right tier in discovery and scales the doc set to match.

#### The two-zone model

The skill treats your repo as two zones in one folder:

- **Code zone** — application source, committed and pushed as normal.
- **Planning zone** (`_planning/`) — local-only, gitignored, never pushed.

It enforces this actively: it writes the `.gitignore` entries, installs a pre-commit guard, and verifies the planning zone is truly excluded before your first commit. The committed `CLAUDE.md` carries only shareable build conventions; anything private lives in the gitignored `_planning/`.

## License

[MIT](LICENSE)
