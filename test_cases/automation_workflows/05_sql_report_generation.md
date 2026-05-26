# Test Case 05 — SQL Report Generation Automation

## Purpose

Validate an automation that generates or runs SQL queries to produce a business report.

This is relevant when a developer creates reporting automations for customers using databases, exports, or internal systems.

## Business Scenario

The customer wants a recurring sales, inventory, finance, or operations report.

The automation must run a query, generate a result, and export it safely.

## Input

Possible inputs:

- SQL query file
- database connection settings
- report date range
- customer filter
- product category filter
- export destination

## Expected Output

The automation should produce:

- correct query result
- expected columns
- expected row counts
- correct date range
- no duplicated records
- no destructive database action
- export file in the correct location

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Valid SELECT query | Report generated |
| Invalid SQL syntax | Clear error message |
| Empty result set | Empty report with explanation |
| Missing date filter | Warning or blocked execution |
| Wrong table name | Clear error message |
| Destructive query | Blocked or requires approval |
| Connection failure | Clear connection error |
| Permission failure | Clear permission error |

## Failure Conditions

The test fails if:

- SQL syntax errors are not detected
- destructive queries run without control
- the wrong date range is used
- the output schema changes unexpectedly
- credentials are exposed in logs
- the automation fails silently
- exported data is incomplete or duplicated

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| SQL query | sql/ |
| Query output | outputs/ |
| Validation notes | outputs/ |
| Bug report | bug_reports/ |

## QA Principle

SQL automations should be checked for correctness, safety, and business meaning before customer delivery.
