# EHR Upgrade UAT & Defect Reporting Framework

> **Portfolio demonstration | Synthetic / fictional data only**

A simulated release-testing framework covering core EHR workflows, reproducible acceptance criteria, and go-live readiness indicators.

## What this demonstrates
- Catalog fictional registration, scheduling, clinical documentation, and reporting tests
- Compute pass rates by module and open defect counts
- Provide editable UAT evidence template and release gate checklist

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/test_cases.csv`: fictional UAT case results
- `docs/uat-plan.md`: scope, gates, and evidence template
- `src/main.py`: readiness summary

## Relevant skills
UAT, EHR workflow, requirements traceability, QA, release readiness

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.

## How to discuss in an interview
Explain the input, validations or transformations, measurable outputs, tests, and what you would change for a real deployment (authentication, audit logs, monitoring, regulatory review, and secure storage). Describe this as a **personal portfolio project**, not as an implementation at an employer.

## License
MIT — see [LICENSE](LICENSE).
