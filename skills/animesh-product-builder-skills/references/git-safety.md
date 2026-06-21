# Git safety — enforce and verify the planning zone stays local

Running inside Claude Code, you can *do* the protection, not just advise it. Set this up **before the project's first commit**, and re-verify whenever the repo gains a remote.

## 1. Write the `.gitignore` entries

Ensure these lines exist in the repo-root `.gitignore` (create the file if absent; append if it exists — don't clobber existing rules):

```gitignore
# Planning zone — LOCAL ONLY, never commit or push
_planning/

# Secrets
.env
.env.*
!.env.example
```

Note: the root `CLAUDE.md` is intentionally **committed** (shareable build conventions). The private handover lives in `_planning/claude-context.md`, which the `_planning/` rule already covers. Do **not** add `CLAUDE.md` to `.gitignore`.

## 2. Verify the ignore actually works

A `.gitignore` only prevents tracking; it does nothing against `git add -f` or files already tracked. Verify:

```bash
# Should print the path(s) → confirms they are ignored
git check-ignore -v _planning/ _planning/claude-context.md

# Should return NOTHING → confirms nothing in the planning zone is already tracked
git ls-files _planning/
```

If `git ls-files` lists anything under `_planning/`, it was committed before the ignore rule. Untrack it (keeps the local file):

```bash
git rm -r --cached _planning/
```

Then confirm `git status` shows `_planning/` as untracked/ignored, not staged.

## 3. Install a pre-commit guard

`.gitignore` is not enough. Install a pre-commit hook that hard-blocks any staged planning file or obvious secret, even under `git add -f`. Write it to `.git/hooks/pre-commit` and `chmod +x` it:

```bash
#!/usr/bin/env bash
# Block planning-zone files and obvious secrets from ever being committed.
staged=$(git diff --cached --name-only)

blocked=$(echo "$staged" | grep -E '^_planning/|(^|/)\.env($|\.)' | grep -vE '\.env\.example$')
if [ -n "$blocked" ]; then
  echo "BLOCKED: these files are local-only and must not be committed:"
  echo "$blocked" | sed 's/^/  - /'
  echo "Planning docs (_planning/) and secrets (.env) never leave this machine."
  exit 1
fi
```

If the project already has a pre-commit framework (Husky, pre-commit, lefthook), add the equivalent check there instead of overwriting their hook.

## 4. Recommend a secret scanner

Suggest the user add `gitleaks` or `trufflehog` to CI and/or as a second pre-commit hook for defense-in-depth. This is a recommendation, not something you silently install.

## 5. Secrets-at-rest caution

Planning docs can contain API keys, real user data, or PII in plaintext. The `.gitignore` + hook protect the *remote*, but the files still sit unencrypted on disk. Remind the user not to paste live secrets into planning docs — reference where a secret lives (e.g. "`STRIPE_KEY` in 1Password") rather than the value.

## Reminders

- Never write `git add`/`git commit`/`git push` commands that touch `_planning/`.
- If the user asks to commit or push planning docs, stop them and restate the hard rule.
- This protection applies to **the user's projects**, not to this skill's own repository.
