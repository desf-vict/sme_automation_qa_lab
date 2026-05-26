# Incident Report — API Import Data Quality Failure

## Date

2026-05-26

## Incident Summary

An API import workflow accepted duplicate, incomplete, and invalid contact records.

## Affected Workflow

API data import validation.

## Source File

```text
datasets/api_contacts_response_dirty.json
```

## Defective Output

```text
outputs/api_import_defective_summary.json
```

## Impact

The workflow could import poor-quality customer data into a CRM, reporting tool, or business database.

Potential customer impact:

- duplicate contact records
- invalid email addresses
- incomplete customer records
- incorrect reporting
- manual cleanup effort

## Detection

The issue can be detected by running:

```bash
python validation/api_import_validator.py
```

## Root Cause

The defective import summary shows that the automation did not detect:

- duplicate contact ID
- missing name
- invalid email format

## Severity

High

## Mitigation

Add validation before import completion.

Required checks:

- duplicate ID detection
- required field validation
- email format validation
- rejected record summary
- import count reconciliation

## Lessons Learned

Valid JSON does not mean valid business data.

Automation QA must check structure, business rules, and customer impact.
