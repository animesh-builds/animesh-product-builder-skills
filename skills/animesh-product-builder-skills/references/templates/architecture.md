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

## Non-functional requirements
Numbers, not adjectives.
- **Latency:** p50 / p95 targets per endpoint type
- **Bundle size:** initial JS budget, per-route budget
- **Lighthouse / Core Web Vitals:** targets
- **Availability:** uptime target, maintenance window policy
- **Cold start tolerance** (if serverless)
- **Concurrency:** expected and peak

## Data model
Core entities and relationships. Schema-level.

## API design
Endpoints. Input/output shape. Auth requirements. Versioning policy. Breaking-change policy.

## Key flows
Walk through 2–4 critical flows step by step.

## Third-party services
Dependencies, cost, lock-in risk. Per service: what happens if it goes down.

## Testing strategy
- **Pyramid:** unit / integration / e2e split (rough %)
- **Coverage policy:** target, what's exempt, what blocks merge
- **Critical paths:** flows that must have e2e coverage
- **Test data:** fixtures, factories, seeded DBs, masking policy for prod data
- **CI gates:** what runs on PR vs main vs nightly
(Promote to standalone `testing.md` if this section grows past ~1 page.)

## Deployment
Local → production. CI/CD shape. Environments (dev/staging/prod). Migration policy.

## Scaling considerations
Where bottlenecks surface first. What we'd do at 10x current load.

## Security & data handling
- **Auth:** mechanism, session policy, MFA
- **Secrets:** storage, rotation
- **Data classification:** what's public / internal / sensitive / regulated
- **PII handling:** what we collect, why, retention period, deletion-on-request flow
- **Audit trail:** what's logged, retention, who can access
- **Regulatory scope:** GDPR / DPDP / PCI / HIPAA / other as applicable
- **Rate limiting & input validation:** policy at edges
- **For payments-adjacent products:** idempotency keys, webhook signature verification, refund/dispute flow, reconciliation cadence

## Risks & rollback
- **Technical risks:** failure modes ranked by blast radius
- **Rollback strategy:** how we revert a bad deploy (DB migrations, feature flags, blue/green)
- **Incident playbook pointer:** where the runbook lives

## Observability
- **Logging:** what gets logged, structured format, retention
- **Metrics:** golden signals (latency, traffic, errors, saturation) per service
- **Tracing:** if applicable
- **Alerts:** thresholds and where they fire
- **Error tracking:** tool and ownership

## Cost
Per-month estimate at expected load. Unit economics if user-facing (cost per user, cost per transaction).
