# Git safety — keep the planning zone local

Running inside Claude Code, you can enforce this, not just advise it. Set it up **before the project's first commit**.

## 1. Write the `.gitignore` entries

Ensure these exist in the repo-root `.gitignore` (create if absent; append, don't clobber):

```gitignore
# Planning zone — LOCAL ONLY, never commit or push
_planning/

# Secrets
.env
.env.*
!.env.example
```

The root `CLAUDE.md` is intentionally **committed** (shareable conventions); the private handover lives in `_planning/claude-context.md`, covered by the `_planning/` rule. Don't gitignore `CLAUDE.md`.

## 2. Verify it actually works

`.gitignore` only prevents tracking, not `git add -f` or already-tracked files. Verify:

```bash
git check-ignore -v _planning/        # should print the path → ignored
git ls-files _planning/               # should print NOTHING → not tracked
```

If `git ls-files` lists planning files, they were committed before the rule. Untrack them (keeps the local copy):

```bash
git rm -r --cached _planning/
```

## 3. Install a pre-commit guard

`.gitignore` isn't enough. Add a hook at `.git/hooks/pre-commit` (`chmod +x`) that blocks staged planning files and secrets even under `-f`:

```bash
#!/usr/bin/env bash
blocked=$(git diff --cached --name-only | grep -E '^_planning/|(^|/)\.env($|\.)' | grep -vE '\.env\.example$')
if [ -n "$blocked" ]; then
  echo "BLOCKED — local-only files must not be committed:"; echo "$blocked" | sed 's/^/  - /'; exit 1
fi
```

If the project uses Husky / pre-commit / lefthook, add the check there instead of overwriting their hook.

## Reminders

- Never write `git add`/`commit`/`push` commands that touch `_planning/`.
- If the user asks to commit or push planning docs, stop them.
- Don't paste live secrets into planning docs — reference where a secret lives, not the value.
