# CLAUDE.md

> Committed file. Shareable build conventions only — no secrets, no private context.
> If a local `_planning/` folder is present, also read `_planning/claude-context.md` for current state and private handover notes. `_planning/` is gitignored and won't exist for people who clone this repo; that's expected.

## Project
One-paragraph description. What it is, who it's for, current phase. (Keep it shareable.)

## How to work in this repo

### Commands
- Install: `...`
- Dev: `...`
- Test: `...`
- Lint: `...`
- Typecheck: `...`
- Build: `...`

Run lint and typecheck before declaring a task done.

### Directory map
```
src/
  components/     # ...
  lib/            # ...
```

### Conventions
- Module boundaries
- Naming
- Style (formatter, lint rules)
- Testing policy
- Commit message format (e.g., Conventional Commits)
- Branching strategy (trunk-based / git flow / feature branches) and branch naming
- PR policy (size, review expectations, who can merge)

### Dependency policy
- When to add a new dep: must justify in PR description; prefer stdlib / existing deps
- Bundle size: check impact on initial JS budget before adding
- License: MIT / Apache 2 / BSD only; no AGPL or unclear licenses
- Update cadence: security patches immediately, minor versions monthly, majors deliberately

### Patterns we use
State management, data fetching, error handling, logging.

### Patterns we DON'T use
Explicit anti-patterns for this codebase.

## Definition of done
A task is done only when:
- [ ] Lint + typecheck clean
- [ ] Tests written and passing (unit minimum; integration if it touches API/DB; e2e if it's a critical path)
- [ ] Manual smoke check of the user-facing flow
- [ ] Logs/metrics added for new code paths
- [ ] Errors handled gracefully (no unhandled rejections, no silent failures)
- [ ] If `_planning/` is present: update `_planning/claude-context.md` "Current state" if scope shifted
- [ ] If a real architectural choice was made, ask the human to record it in `_planning/decisions.md`

## Pitfalls
Known gotchas (shareable ones).

## When in doubt
Ask the human before:
- Introducing a new dependency
- Changing an API contract
- Touching auth, payments, data deletion, or anything with regulatory implications
- Reversing a logged decision

## Local-only zone — do not commit
If a `_planning/` folder exists locally, never stage, commit, or push it. It is gitignored on purpose and contains private planning docs.
