# Test Case 02 — Email To CRM Update Automation

## Purpose

Validate an automation that reads customer emails, extracts useful fields, and prepares a CRM update.

This test case is relevant to SME automation because many business workflows still begin with unstructured emails.

## Business Scenario

A customer receives sales or support requests by email.

The automation must identify:

- customer name
- company name
- email address
- phone number if present
- request type
- urgency
- required action

The automation must then prepare a CRM update or structured output for review.

## Input

Example email content:

| Field | Example |
|---|---|
| From | customer@example.com |
| Subject | Request for maintenance contract update |
| Body | Free-text customer message |

## Expected Structured Output

The automation should produce structured data similar to:

| Field | Expected Behaviour |
|---|---|
| customer_name | Extract only if clearly present |
| company_name | Extract only if clearly present |
| email | Extract from sender or body |
| phone | Extract if present, otherwise blank |
| request_type | Classify from the message |
| urgency | Classify only if supported by text |
| required_action | Summarise next action |

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Complete email | CRM update prepared correctly |
| Missing phone number | Phone field left blank |
| Ambiguous company name | Human review required |
| Multiple people mentioned | Human review required |
| Angry customer tone | Escalation flag added |
| Empty email body | Clear error message |
| Attachment-only request | Attachment handling documented |

## Failure Conditions

The test fails if:

- the wrong CRM record is updated
- the automation invents missing customer data
- the automation treats uncertainty as fact
- duplicate CRM records are created
- the output has no audit trail
- the automation sends or updates without required human review

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| Source email sample | datasets/ |
| Extracted structured output | outputs/ |
| QA notes | bug_reports/ or incidents/ |
| Review screenshot | screenshots/ |

## QA Principle

Customer-data automations require correctness, traceability, and safe handling of ambiguity.
