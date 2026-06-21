# [Project Name] — Testing Strategy

Use only when testing strategy is complex enough to outgrow the section in `architecture.md`. Most projects won't need it.

## Philosophy
What we're optimizing for. Confidence-per-minute, not coverage-for-its-own-sake.

## Pyramid
- Unit (target %): scope, framework
- Integration (target %): scope, framework, what "integration" means here
- E2E (target %): scope, framework, browser/device matrix

## Critical paths
Flows that must have e2e coverage, with reasoning.

## Test data
- Fixtures location and format
- Factories
- Seeded DB for integration tests
- Production-data masking policy (if any test uses prod-derived data)

## CI gates
| Stage | What runs | Blocks merge? |
|---|---|---|
| PR | lint, typecheck, unit, integration | yes |
| Main | full suite + e2e | yes (blocks deploy) |
| Nightly | e2e cross-browser, perf regression | no (alerts) |

## Flakiness policy
What we do when a test flakes. Quarantine rules. How tests get un-quarantined.

## Coverage
Target overall and per-package. What's exempted (generated code, types, config).

## Performance testing
Load test approach if applicable. Where the harness lives.
