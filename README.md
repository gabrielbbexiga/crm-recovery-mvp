# CRM Recovery MVP

An AI-assisted product experiment for helping B2B sales teams decide **which dormant CRM opportunities are worth reviewing first**.

## The problem

Sales teams often accumulate large databases of old leads and opportunities. Over time, records become incomplete, inconsistent, or outdated, and manually reviewing everything does not scale.

This project explores a simple question:

> **Can software turn a dormant CRM database into a smaller, explainable set of opportunities worth investigating?**

The goal is not to let AI make sales decisions blindly. The goal is to combine reliable data handling with AI-assisted analysis so a salesperson can understand **why** a record may deserve attention and how confident the system is in that recommendation.

## Product concept

```text
CRM / CSV data
      ↓
Ingestion
      ↓
Normalization & validation
      ↓
Missing-data detection
      ↓
Commercial signal extraction
      ↓
AI-assisted analysis
      ↓
Priority + confidence
      ↓
Recommended next action
```

A key design principle is separating **potential** from **confidence**.

A record can look commercially interesting while still having too little information to justify immediate outreach. Missing data should lower confidence, not automatically be treated as negative evidence.

## Current MVP

I am building the project in small, testable stages rather than starting with a full SaaS platform.

The current public prototype focuses on the deterministic foundation:

- CSV ingestion
- schema validation
- text, date, and boolean normalization
- missing-field detection
- safe handling of incomplete records
- normalized CSV export
- automated tests

The AI-assisted prioritization layer is a later stage and is still under development and validation.

## Why start with deterministic data work?

Before asking an LLM to interpret a CRM record, the system needs to know whether the underlying data is usable.

Tasks such as parsing CSV files, validating fields, normalizing dates, and detecting missing information are deterministic problems. Keeping them outside the model layer makes the system easier to test, explain, and improve.

## How I use AI in the project

I use AI in two ways:

1. **Development partner** — to challenge assumptions, structure requirements, review architecture, think through edge cases, and accelerate iteration.
2. **Future product capability** — to interpret unstructured CRM context, extract commercial signals, summarize evidence, and suggest next actions.

The second use is intentionally separated from deterministic data processing.

## What I am learning

This project is a practical learning environment for:

- product discovery and MVP scoping
- Python project structure
- Pydantic schemas and validation
- automated testing with pytest
- data quality and normalization
- working with incomplete information
- explainable AI-assisted decision systems
- structured model outputs
- separating business logic from model reasoning
- turning a commercial problem into a testable software hypothesis

## Repository structure

```text
crm-recovery-mvp/
├── README.md
├── requirements.txt
├── data/
│   └── sample_leads.csv
├── docs/
│   └── project-overview.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
└── tests/
    └── test_models.py
```

## Running the sample

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main data/sample_leads.csv data/normalized_leads.csv
pytest
```

## Privacy

This public repository contains **only synthetic demonstration data**.

It contains no customer records, employer data, CRM exports, internal business information, credentials, or proprietary material.

## Next experiments

- extract structured signals from unstructured sales notes
- create separate reactivation-potential and confidence outputs
- test explainable ranking logic
- build synthetic evaluation datasets
- compare prioritization strategies against a simple baseline
- explore CRM integrations only after the core hypothesis is validated

## Product mindset

> **Optimize for useful sales decisions, not impressive-looking AI.**

---

Built as an independent learning and product-development project by **Gabriel Batista Bexiga**.