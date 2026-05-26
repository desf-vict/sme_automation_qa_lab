# AI Output Review Checklist

## Purpose

This checklist helps QA review AI-generated outputs used in customer-facing automation workflows.

---

## Source Alignment

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Output uses only source facts | No invented data | Pending | |
| Missing information handled safely | Blank, unknown, or review flag | Pending | |
| Ambiguous input handled safely | Human review required | Pending | |
| Customer meaning preserved | No distortion of request | Pending | |
| No unsupported commitment | No invented price, date, refund, or promise | Pending | |

---

## Format Validation

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Requested format followed | JSON, CSV, SQL, or text as requested | Pending | |
| JSON parses correctly | Valid JSON if required | Pending | |
| Required fields present | Schema complete | Pending | |
| Field names stable | No unexpected schema drift | Pending | |
| No extra prose | Machine-readable output remains clean | Pending | |

---

## Safety Review

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| No hidden/internal data exposed | Internal notes protected | Pending | |
| No confidential data leaked | Sensitive information controlled | Pending | |
| Human approval required where needed | Review gate active | Pending | |
| Risky cases escalated | Legal, financial, or complaint cases flagged | Pending | |

---

## QA Principle

AI output should be reviewed against the source, not judged by how fluent it sounds.
