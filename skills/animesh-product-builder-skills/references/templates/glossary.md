# Glossary

Domain terms used in this project. Plain-language definitions; not Wikipedia depth.
Add when the domain has heavy jargon (payments, finance, healthcare, infra).

| Term | Definition | Notes |
|---|---|---|
| Idempotency key | A unique ID attached to a request so retrying doesn't double-apply the effect (e.g. double-charge) | Required for all payment-gateway calls in this system |
| MOP | Mode of Payment (UPI, card, COD, etc.) | List the ones supported; see `prd.md` |
| ... | ... | ... |
