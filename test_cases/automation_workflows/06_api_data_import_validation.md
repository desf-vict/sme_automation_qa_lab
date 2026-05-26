# Test Case 06 — API Data Import Validation

## Purpose

Validate an automation that imports data from an external API into a file, spreadsheet, database, CRM, ERP, or reporting workflow.

This is relevant because many SME automations depend on SaaS APIs.

## Business Scenario

The customer wants to import data from an external service into an internal workflow.

Examples:

- CRM contacts
- invoices
- stock levels
- support tickets
- order records
- analytics events
- accounting transactions

## Input

Possible inputs:

- API endpoint
- API token
- date range
- pagination settings
- customer account ID
- import destination
- mapping configuration

## Expected Output

The automation should:

- connect successfully
- handle authentication errors
- retrieve the expected records
- handle pagination
- validate required fields
- avoid duplicate imports
- log import results
- expose clear errors

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Valid API response | Data imported correctly |
| Invalid API key | Clear authentication error |
| Expired token | Clear token error |
| Empty API response | Safe empty import result |
| Rate limit response | Retry or clear rate-limit message |
| Pagination required | All pages imported |
| Missing required field | Record flagged |
| Duplicate record | Duplicate prevented or flagged |
| API timeout | Clear timeout error |

## Failure Conditions

The test fails if:

- only the first API page is imported
- authentication errors are unclear
- duplicate records are inserted
- missing fields are not detected
- API tokens are printed in logs
- import counts do not match expected records
- the automation fails silently

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| Example API response | datasets/ |
| Imported output | outputs/ |
| Import log | outputs/ |
| Bug report | bug_reports/ |
| Incident report if data is corrupted | incidents/ |

## QA Principle

API automations must be tested for authentication, pagination, data quality, duplication, and failure handling.
