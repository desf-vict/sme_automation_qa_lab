# Test Case 03 — Invoice Extraction Validation

## Purpose

Validate an automation that extracts invoice data from a PDF, image, email attachment, or structured file.

This is a common SME automation use case because invoice processing is repetitive and error-prone.

## Business Scenario

The customer receives supplier invoices and wants an automation to extract key fields for accounting review.

The automation must not invent missing values.

## Input

Possible input formats:

- PDF invoice
- scanned image
- email attachment
- CSV invoice export
- supplier portal download

## Fields To Extract

| Field | Required | QA Notes |
|---|---|---|
| supplier_name | Yes | Must match invoice |
| invoice_number | Yes | Must not be invented |
| invoice_date | Yes | Date format must be valid |
| due_date | No | Blank if missing |
| subtotal | Yes | Must be numeric |
| tax | Yes | Must be numeric |
| total | Yes | Must match subtotal plus tax where applicable |
| currency | Yes | Must be detected or flagged |
| payment_terms | No | Extract if present |

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Clean invoice | Fields extracted correctly |
| Missing due date | Field blank or flagged |
| Blurry scan | Human review required |
| Multiple totals | Human review required |
| Different currency | Currency detected |
| Tax mismatch | Calculation warning |
| Duplicate invoice number | Duplicate warning |
| Unsupported format | Clear error message |

## Failure Conditions

The test fails if:

- the automation invents an invoice number
- totals are extracted incorrectly
- tax and subtotal do not reconcile
- unsupported files fail silently
- duplicate invoices are not flagged
- low-confidence extraction is not escalated
- the output is written to the wrong customer file

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| Sample invoice | datasets/ |
| Extracted output | outputs/ |
| Validation notes | outputs/ |
| Bug report | bug_reports/ |
| Incident report if financial risk exists | incidents/ |

## QA Principle

Financial automation output should be treated as unsafe until extracted values are checked against the source document.
