# Integration QA Notes

## Purpose

This document summarises QA checks for common integrations used in SME automations.

---

## Integration Types

| Integration | Example Risk | QA Check |
|---|---|---|
| Email | Wrong message parsed | Check source email and extracted fields |
| CRM | Wrong record updated | Confirm customer ID and duplicate handling |
| Spreadsheet | Format changes | Validate columns and data types |
| API | Pagination missed | Confirm all pages are processed |
| Database | Wrong query result | Validate SQL and row counts |
| File system | Wrong path | Check customer input/output folders |
| Cloud storage | Permission failure | Test read/write access |
| AI service | Hallucinated output | Validate against source data |

---

## Generic Integration Checks

Before approving an integration automation, check:

- authentication works
- credentials are not exposed
- source data is reachable
- destination is reachable
- permissions are sufficient
- error messages are clear
- rate limits are handled if relevant
- duplicate handling is defined
- audit or log evidence exists
- rollback or correction path exists

---

## QA Principle

Integration automations fail at the boundaries between systems.

Those boundaries should be tested explicitly.
