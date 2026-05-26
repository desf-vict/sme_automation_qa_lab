# 05 — Test Matrix

## Purpose

The test matrix tracks what has been tested, what result was expected, what happened, and where the evidence is stored.

## Test Matrix

| Test ID | Category | Scenario | Expected Result | Status | Evidence |
|---|---|---|---|---|---|
| QA-001 | CSV automation | Clean CSV import | Report generated | Pending | datasets/ |
| QA-002 | CSV automation | Missing quantity | Row flagged | Pending | outputs/ |
| QA-003 | CRM automation | Complete email | CRM update prepared | Pending | test_cases/ |
| QA-004 | AI workflow | Customer reply draft | No invented facts | Pending | ai_workflow_tests/ |
| QA-005 | SQL workflow | Basic report query | Valid SQL | Pending | sql/ |
| QA-006 | Environment | Missing credential | Clear error | Pending | customer_environment/ |
| QA-007 | Delivery | Handover review | Checklist complete | Pending | handover/ |

## Status Values

Use the following values:

- Pass
- Fail
- Pending
- Blocked
- Needs review

## QA Principle

If a test is not documented, it is difficult to prove that it was performed.

## Expected Learning Outcome

The reader should understand how to track QA coverage across automation workflows.
