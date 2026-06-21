# [Project Name] — AI Spec

Add when the product has LLM features. Separates "model behavior" from app code — easier to iterate on, easier to eval.

## Scope
What AI features exist in this product. What problems they solve. What they explicitly don't do.

## Model choice
- **Provider + model + version:** e.g., latest Claude (Opus/Sonnet) via Anthropic API
- **Why this model:** capability fit, latency, cost
- **Fallback model:** what we use if primary is down

## System prompt(s)
Full text of each system prompt the product uses. Versioned (note when changed and why — reference a `decisions.md` ID).

## Tools / function calling
List of tools exposed to the model. For each: name, input schema, what it does, side effects.

## Guardrails
- **Input validation:** what we sanitize before sending to the model
- **Output validation:** what we check before showing the response to the user
- **Jailbreak handling:** how we detect and respond to off-policy requests
- **PII policy:** what the model is/isn't allowed to see

## Evals
- **Eval set:** where it lives, how many cases, how it's run
- **Metrics:** what we measure (accuracy, latency, cost, refusal rate)
- **Pass bar:** threshold for shipping a prompt change
- **Cadence:** when evals run (every prompt change, nightly, before release)

## Fallback behavior
What the product does when the model is unavailable, slow, or returns garbage.

## Observability
- Logging policy for prompts and responses (what's redacted)
- Cost tracking per feature
- Latency tracking p50/p95

## Known failure modes
Things the model gets wrong and how we handle them.
