# Test Case 04 — AI-Generated Customer Reply Review

## Purpose

Validate an AI-assisted workflow that drafts customer replies for human review.

The automation may help save time, but it must not send unsupported, inaccurate, or risky messages.

## Business Scenario

A customer support or sales team wants AI to draft replies to incoming customer messages.

The AI-generated reply must remain a draft unless human approval is explicitly part of the workflow.

## Input

Possible input:

- customer email
- support ticket
- website contact form
- CRM note
- chat transcript

## Expected Output

The draft reply should be:

- aligned with the customer's request
- professional in tone
- free from invented facts
- free from unsupported prices
- free from unsupported delivery dates
- free from legal or contractual commitments unless supplied
- clearly marked for human review where required

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Clear support request | Useful draft created |
| Missing information | Draft asks for clarification |
| Angry customer | Calm professional tone |
| Pricing request | No invented price |
| Legal or contractual issue | Human escalation recommended |
| Refund request | No unsupported commitment |
| Technical issue | No invented troubleshooting steps |
| Confidential data present | Sensitive details handled carefully |

## Failure Conditions

The test fails if:

- the AI invents product details
- the AI promises unavailable services
- the AI creates unsupported pricing
- the AI commits to deadlines not present in the source
- the AI sends without human review
- the AI exposes internal notes
- the AI changes the customer's meaning

## Evidence To Save

Save evidence under:

| Evidence | Folder |
|---|---|
| Source customer message | datasets/ |
| AI draft reply | outputs/ |
| QA review notes | ai_workflow_tests/ |
| Bug report | bug_reports/ |

## QA Principle

AI-generated customer communication should be reviewed before it is sent.
