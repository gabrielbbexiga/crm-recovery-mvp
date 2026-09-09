# Project Overview

## Problem

B2B sales teams often accumulate dormant CRM records. Over time, the data becomes incomplete, inconsistent, or outdated, while manual review becomes increasingly expensive.

The product question behind this project is:

> Can software reduce a large dormant CRM database into a smaller, explainable set of records that deserve human attention?

## Product hypothesis

A useful system should do more than generate a score. It should explain the evidence behind the recommendation and how reliable that recommendation is.

For each dormant record, a future version should ideally help answer:

- Is there evidence of previous buying intent?
- Does the record still appear relevant?
- What important information is missing?
- How confident is the system in its assessment?
- Is research, outreach, or no action the best next step?

## Potential and confidence are different

Missing information should not automatically be interpreted as negative evidence.

For example:

- unknown company size does not mean the company is too small;
- missing job title does not mean the contact lacks influence;
- missing sales notes do not prove there was no interest.

Instead, missing information should reduce **confidence**.

That creates two separate outputs:

### Reactivation potential

How commercially interesting the record appears based on the available evidence.

### Confidence

How much evidence exists to trust that assessment.

A record can therefore have high potential but low confidence, making research a more sensible next action than immediate outreach.

## MVP strategy

The first version is intentionally narrow:

```text
raw CSV
  ↓
ingestion
  ↓
normalization
  ↓
validation
  ↓
normalized CSV
```

Before adding an AI layer, the project needs reliable and testable data handling.

The first milestone focuses on:

- flexible CSV ingestion;
- normalization of common text, date, and boolean fields;
- tolerant handling of missing optional values;
- explicit detection of missing fields;
- validation with Pydantic;
- clean CSV export;
- automated tests.

## Planned AI layer

The AI-assisted stage is intentionally separate from the deterministic foundation.

Possible future uses include:

- interpreting unstructured sales notes;
- extracting evidence of buying intent;
- identifying commercial signals;
- summarizing why a record may deserve attention;
- suggesting a next action;
- producing structured outputs that can be evaluated.

## Evaluation philosophy

The project should eventually be judged by business usefulness rather than by model sophistication.

Potential evaluation metrics include:

- time required to review dormant records;
- response rate from selected records;
- meeting rate;
- qualified-opportunity rate;
- false-positive rate;
- percentage of records with insufficient evidence.

## Public-data policy

This repository is intentionally generic.

All sample records are synthetic. No employer data, customer records, CRM exports, private contacts, credentials, internal metrics, or proprietary business information are included.
