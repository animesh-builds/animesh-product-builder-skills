# [Project Name] — Architecture

## Overview
One paragraph + simple diagram (ASCII or mermaid).

## Tech stack
| Layer | Choice | Why |
|---|---|---|
| Frontend | ... | ... |
| Backend | ... | ... |
| Database | ... | ... |
| Hosting | ... | ... |
| Auth | ... | ... |

## Data model
Core entities and relationships. Schema-level.

## API design
Endpoints. Input/output shape. Auth requirements. Versioning policy.

## Key flows
Walk through 2–4 critical flows step by step.

## Non-functional requirements
Numbers, not adjectives — latency targets, availability, expected/peak concurrency.

## Testing strategy
Unit / integration / e2e split, what blocks merge, critical paths that need e2e.

## Deployment
Local → production. CI/CD shape. Environments. Migration policy.

## Security & data handling
- Auth mechanism and session policy
- Secrets storage
- Data classification (public / internal / sensitive / regulated)
- PII: what's collected, retention, deletion-on-request
- Regulatory scope (GDPR / DPDP / PCI / HIPAA as applicable)
- Rate limiting & input validation at edges

## Risks & rollback
Top technical risks by blast radius, and how a bad deploy is reverted.

## Observability
Logging, key metrics, alerts, error tracking.

## Cost
Rough per-month estimate at expected load.
