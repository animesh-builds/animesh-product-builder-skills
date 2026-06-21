# Decisions

Lightweight log of architectural and product decisions. Append-only. Newest at bottom.

For each decision: a short title, the date, the call, the reasoning, and the status (Proposed / Locked / Superseded).

**Update rules:**
- Append a new decision when a real architectural or product choice gets locked in. Skip trivial ones (lint config, file naming).
- Never delete or rewrite an old decision. To reverse one, write a new one with `Supersedes: D###` and mark the old one `Status: Superseded`.
- Reference decision IDs in `session-history.md` and `claude-context.md` so future-you can find the reasoning.
- Keep entries tight — if it doesn't fit on a phone screen, it's too long.

---

## D001 — [Title]
**Date:** YYYY-MM-DD
**Status:** Locked
**Decision:** One sentence — what we're doing.
**Why:** 2–4 bullets. Tradeoffs considered. What we rejected and why.
**Consequences:** What this commits us to. What it makes harder later.
**Supersedes:** (if applicable) — D### that this replaces.

---

## D002 — [Title]
...
