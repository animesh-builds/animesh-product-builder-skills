# Workflow — detailed

Read this when starting, resuming, or wrapping a planning session. The summary lives in `SKILL.md`; this is the full procedure.

## Session start

On the same machine, the planning docs are already on disk. Resume from them — don't ask the user to paste.

1. **Try to read** `_planning/session-history.md` and `_planning/decisions.md`.
2. **If they exist:** produce a one-paragraph recap of where things stand plus 2–3 proposed next steps drawn from the latest entry's "Next up." Wait for the user to confirm or redirect.
3. **If they're absent:** this is either a brand-new project (→ Discovery) or a different device (→ Cross-device). Ask which.
4. Don't make catch-up a hard gate. If the user is clearly mid-flow on the same machine, take the cue and continue.

### Cross-device

Planning docs are gitignored, so they don't sync via git. On a new device the user pastes or uploads `session-history.md` and `decisions.md`; read those, write them into the local `_planning/`, then proceed. Syncing planning docs across devices (iCloud/Dropbox/private gist) is the user's choice — never propose storing them in the git remote to solve sync.

## During the session

- Write docs to `_planning/` one at a time. Pause at review gates.
- Update `_planning/decisions.md` the moment a real architectural/product choice locks in — don't wait for session end.
- Leave `_planning/session-history.md` untouched until wrap-up.

## Step 0 — Discovery (brand-new projects)

Don't jump to the PRD. Ask a short batch of 5–7 questions, at minimum:

- What is the project in one sentence?
- Who is it for?
- What problem does it solve?
- **Greenfield or existing codebase?** (existing → Brownfield onramp)
- **Tier: Lite, Standard, or Full?**
- Stack preference, if any?
- Deadline or constraint?
- Does it touch regulated data (payments, health, PII at scale) or have LLM features?

Skip questions the user already answered in their opening message.

## Brownfield onramp (existing codebase)

Skip cold discovery. Instead:

1. Inspect the repo yourself where possible (read top-level dirs, package manifests, README) and ask the user to fill gaps: what the product does today, what state it's in (live / prototype / abandoned), and the immediate problem to solve.
2. Write `_planning/claude-context.md` **first** (so Claude Code is useful immediately), then `architecture.md` (document what exists, not aspirations), then backfill `prd.md` and `decisions.md` from what you can reconstruct.
3. Mark reconstructed content `[inferred — confirm]` so the user can validate.
4. Set up git safety (`git-safety.md`) early — the repo may already have a remote.

## Steps 1–N — produce each doc

For each document:

1. Confirm you have enough input; if not, ask targeted questions.
2. Load the matching template from `references/templates/`.
3. Write the doc to `_planning/<doc>.md` (Write tool). Adapt sections to the project — drop inapplicable sections rather than padding.
4. Summarize the 2–3 key decisions it locks in.
5. Append load-bearing decisions to `_planning/decisions.md` now (next ID); defer trivial ones.
6. Ask: "Ready to move to [next doc], or revise this one?"

## Kit review (consistency pass)

Once all required docs exist, read across them and flag:

- **Contradictions** — e.g. PRD says "mobile-first" but design-language only specifies desktop breakpoints.
- **Missing-but-implied** — e.g. PRD mentions payments but architecture has no idempotency/audit-trail story; LLM feature but no `ai-spec.md`.

Report findings as a short list; offer to fix each.

## Ready-for-Claude-Code handoff

When the user says "ready for Claude Code":

1. Finalize the committed `CLAUDE.md` (build conventions) and gitignored `_planning/claude-context.md` (private handover), incorporating everything decided.
2. Run the consistency pass.
3. Confirm git safety is in place and verified (`git-safety.md`).
4. Produce a **starter task brief** — a short prompt the user can paste into the first Claude Code session:

   > Here's the project. Read `CLAUDE.md`, and `_planning/` if present locally. Your first task is **X**. Confirm your understanding and plan before you start coding.

## Session end ("wrap up", "that's it", "let's end here")

1. Read the current `_planning/session-history.md`.
2. **Prepend** a new entry with today's date (template: `templates/session-history.md`): Type, Goal, Done, Decisions (IDs only), Docs touched, Code touched, Next up, Lessons, Open questions/blockers.
3. Write the updated file.
4. Confirm any new decisions are logged in `_planning/decisions.md`.
5. Do not summarize the session in chat — the file is the summary.
