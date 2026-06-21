# Workflow

Read this when starting, resuming, or wrapping a planning session.

## Session start

On the same machine, planning docs are already on disk — resume from them.

1. Read `_planning/session-history.md` and `_planning/decisions.md`.
2. If they exist: give a one-paragraph recap + 2–3 next steps from the latest entry's "Next up." Wait for confirmation.
3. If absent: it's a new project (→ Discovery) or a different device (the user pastes the docs). Ask which.
4. Don't make catch-up a hard gate — if the user is clearly mid-flow, continue.

## Step 0 — Discovery (new projects)

Don't jump to the PRD. Ask 5–7 questions: what it is in one sentence; who it's for; the problem; greenfield or existing codebase; tier (Lite/Standard/Full); stack preference; deadline; whether it touches regulated data or has LLM features. Skip what the user already answered.

## Brownfield onramp (existing codebase)

1. Inspect the repo (top-level dirs, manifests, README) and ask the user for gaps: what it does today, its state (live/prototype/abandoned), the immediate problem.
2. Write `_planning/claude-context.md` first, then `architecture.md` (document what exists), then backfill `prd.md` and `decisions.md`.
3. Mark reconstructed content `[inferred — confirm]`.
4. Set up git safety early (`git-safety.md`).

## Producing each doc

1. Confirm you have enough input; if not, ask.
2. Load the matching template from `references/templates/`.
3. Write the doc to `_planning/<doc>.md`. Drop inapplicable sections rather than padding.
4. Summarize the 2–3 decisions it locks in; append load-bearing ones to `_planning/decisions.md`.
5. Ask: "Ready for the next doc, or revise this one?"

## Kit review

Once required docs exist, read across them and flag contradictions and missing-but-implied items. Offer to fix each.

## Ready-for-Claude-Code handoff

1. Finalize committed `CLAUDE.md` and gitignored `_planning/claude-context.md`.
2. Run the consistency pass; confirm git safety is in place.
3. Produce a starter task brief the user can paste into the first Claude Code session:

   > Read `CLAUDE.md`, and `_planning/` if present locally. Your first task is **X**. Confirm your plan before coding.

## Session end ("wrap up")

1. Read `_planning/session-history.md`.
2. **Prepend** a dated entry (template: `templates/session-history.md`): Type, Goal, Done, Decisions (IDs), Docs touched, Next up, Open questions.
3. Write the file. Confirm new decisions are logged in `decisions.md`.
4. Don't summarize in chat — the file is the summary.
