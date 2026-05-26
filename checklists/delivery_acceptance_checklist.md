# Delivery Acceptance Checklist

## Purpose

This checklist verifies whether an automation is ready to be delivered to the customer.

It focuses on practical delivery risk, not only whether the script runs once.

---

## Functional Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Main workflow runs end to end | Automation completes successfully | Pending | |
| Correct input accepted | Valid input processed | Pending | |
| Bad input handled | Clear error or rejection | Pending | |
| Empty input handled | Clear error or safe stop | Pending | |
| Duplicate input handled | Duplicate flagged or handled | Pending | |
| Output generated | Expected output file or update created | Pending | |
| Output reviewed | Output matches expectation | Pending | |

---

## Data Quality Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Missing values handled | Missing fields flagged | Pending | |
| Invalid data types handled | Invalid values rejected or flagged | Pending | |
| Unexpected columns handled | Clear behaviour documented | Pending | |
| Duplicate records handled | Duplicate handling confirmed | Pending | |
| Totals or calculations checked | Calculations correct | Pending | |

---

## Error Handling Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Missing file error | Clear error shown | Pending | |
| Missing credential error | Clear error shown | Pending | |
| API failure error | Clear error shown | Pending | |
| Permission error | Clear error shown | Pending | |
| Invalid format error | Clear error shown | Pending | |
| No silent failure | Failure is visible | Pending | |

---

## Security And Safety Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| No secrets in source code | No passwords or tokens exposed | Pending | |
| No secrets in logs | Logs do not expose credentials | Pending | |
| Customer data handled safely | No unnecessary exposure | Pending | |
| Destructive actions confirmed | Deletes/updates require control | Pending | |
| Rollback possible | Recovery path documented | Pending | |

---

## Handover Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Setup instructions written | Customer can follow them | Pending | |
| Run instructions written | Customer can run automation | Pending | |
| Known issues documented | Limitations visible | Pending | |
| Support contact defined | Escalation route known | Pending | |
| Customer sign-off criteria clear | Acceptance criteria documented | Pending | |

---

## Final Delivery Decision

| Decision | Meaning |
|---|---|
| Ready | Automation can be delivered |
| Ready with notes | Minor issues exist but delivery is acceptable |
| Blocked | Major defect prevents delivery |
| Needs customer clarification | Requirement or environment is unclear |
| Needs developer fix | Code or workflow must be corrected |

---

## QA Principle

Delivery readiness means the customer can run, understand, and trust the automation.
