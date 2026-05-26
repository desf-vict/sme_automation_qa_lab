# Test Case 01 — CSV To Excel Report Automation

## Purpose

Validate an automation that receives a CSV file, checks the data, and produces a clean report.

This is a common SME automation pattern because many small businesses still depend on spreadsheets and manual reporting.

## Business Scenario

A customer exports inventory data from an internal system as a CSV file.

The automation must:

- read the CSV file
- validate the rows
- detect missing or invalid values
- calculate summary totals
- generate a clean output report
- make errors visible to the user

## Input

Expected input file:

```text
datasets/customer_inventory_input.csv
```

Expected columns:

| Column | Type | Required | Notes |
|---|---|---|---|
| item_id | text | Yes | Unique item identifier |
| item_name | text | Yes | Product name |
| quantity | integer | Yes | Must be numeric |
| unit_price | decimal | Yes | Must be numeric |
| category | text | No | Optional classification |

## Expected Output

Expected output file:

```text
outputs/inventory_report_output.csv
```

The output should include:

- valid inventory rows
- rejected row count
- duplicate row count
- missing value count
- total inventory value
- clear QA summary

## Test Scenarios

| Scenario | Input Condition | Expected Result |
|---|---|---|
| Clean CSV | All rows valid | Report generated successfully |
| Missing quantity | Quantity is blank | Row flagged or rejected |
| Non-numeric quantity | Quantity is text | Row flagged or rejected |
| Duplicate item_id | Same item appears twice | Duplicate flagged |
| Empty file | No data rows | Clear error message |
| Extra column | Unexpected column appears | Column ignored or documented |
| Missing required column | quantity column missing | Automation stops safely |

## Failure Conditions

The test fails if:

- the automation silently ignores invalid rows
- totals are calculated incorrectly
- duplicate records are not detected
- the output file is not created
- the original input file is overwritten
- the user receives no useful error message
- the script only works with hard-coded local paths

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| Input CSV | datasets/ |
| Output report | outputs/ |
| Error log | outputs/ |
| Bug report | bug_reports/ |
| Screenshot if relevant | screenshots/ |

## QA Principle

Spreadsheet automations must be tested with dirty data, not only perfect example files.
