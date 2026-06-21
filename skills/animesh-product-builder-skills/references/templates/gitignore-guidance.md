# [Project Name] — Gitignore Guidance

## Philosophy
If it's generated, personal, secret, or planning-related, it does not belong in the remote repo.

## Category 1 — Planning zone (CRITICAL)
The planning docs in this kit are local-only and must never be pushed.
- `_planning/` (entire folder, including `claude-context.md`)

Note: the root `CLAUDE.md` is **committed** on purpose — it carries shareable build conventions only. The private handover lives in `_planning/claude-context.md`, already covered above. Do NOT gitignore `CLAUDE.md`.

## Category 2 — Secrets (NEVER commit)
- `.env` and all `.env.*` except `.env.example`
- API keys, tokens, certs, keystores, credential files

## Category 3 — Build artifacts
`dist/`, `build/`, `.next/`, `out/`, `target/`, production source maps.

## Category 4 — Dependencies
`node_modules/`, `.venv/`, `vendor/`

## Category 5 — Editor & OS
`.DS_Store`, `Thumbs.db`, `.vscode/` (except team-shared `settings.json`), `.idea/`

## Category 6 — Logs & caches
`*.log`, `.cache/`, `.turbo/`, `.parcel-cache/`

## Category 7 — Test & coverage
`coverage/`, `.nyc_output/`

## Category 8 — Project-specific
List anything unique — local DB dumps, generated assets, scratch folders.

## The `.gitignore` itself
```gitignore
# Planning zone — LOCAL ONLY
_planning/

# Secrets
.env
.env.*
!.env.example

# [rest generated for project]
```

## Pre-commit safety net
Install a secret scanner (gitleaks, trufflehog) and add a pre-commit hook that also refuses commits touching `_planning/`. A `.gitignore` alone is not enough — it only prevents tracking, not accidental `git add -f`. See the skill's `references/git-safety.md` for a ready-to-install hook.
