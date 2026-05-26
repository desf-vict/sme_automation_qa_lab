# Validation Utilities

## Purpose

This folder contains lightweight validation utilities for the SME Automation QA Lab.

The scripts demonstrate how QA can support a small developer team by checking structured data before it is used in customer-facing automations.

---

## Current Scripts

| Script | Purpose |
|---|---|
| json_validator.py | Checks whether selected JSON files are valid JSON |
| csv_inventory_validator.py | Checks customer inventory CSV data quality |
| api_import_validator.py | Checks API contact import data quality |

---

## How To Run

From the repository root:

```bash
# Validate JSON syntax.
python validation/json_validator.py

# Validate customer inventory CSV files.
python validation/csv_inventory_validator.py

# Validate API contact import examples.
python validation/api_import_validator.py
```

---

## QA Lesson

A file can be syntactically valid but still fail QA.

Examples:

- valid JSON with duplicate customer IDs
- valid CSV with missing quantities
- valid API response with invalid emails
- valid AI output that invents customer data

Automation QA must check both structure and business meaning.
