# Claude Context — private handover

> LOCAL ONLY. Lives in `_planning/`, gitignored, never committed or pushed.
> Written for Claude Code. Dense, scannable, instructive. Holds current state, next task, and anything not safe for the committed `CLAUDE.md`.

## Project
One-paragraph description. What it is, who it's for, current phase.

## Current state
- Built: ...
- In progress: ...
- Immediate next task: ...

## Active context
- Recent decisions in play (reference `decisions.md` IDs)
- Things mid-flight that aren't obvious from the code
- Anything sensitive that can't go in the committed `CLAUDE.md`

## Pitfalls / gotchas
Known traps specific to this project.

## References (local planning docs)
- `_planning/prd.md`
- `_planning/architecture.md`
- `_planning/content-guide.md`
- `_planning/design-language.md`
- `_planning/main-content.md`
- `_planning/setup-guide.md`
- `_planning/gitignore-guidance.md`
- `_planning/decisions.md`
- `_planning/session-history.md`
- `_planning/glossary.md` (if present)
- `_planning/ai-spec.md` (if present)
- `_planning/testing.md` (if present)

## When in doubt
Ask the human before:
- Introducing a new dependency
- Changing an API contract
- Touching auth, payments, data deletion, or anything with regulatory implications
- Reversing a decision logged in `decisions.md`

Never commit planning docs. Never push `_planning/` to the remote.
