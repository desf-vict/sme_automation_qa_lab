# SQL QA Review Notes

## Purpose

This document records QA observations for SQL used in automation workflows.

SQL generated or executed by automation should be reviewed before it touches customer systems.

---

## Reviewed File

```text
sql/report_queries.sql
```

---

## QA Findings

| Query | Status | Issue |
|---|---|---|
| Sales report by customer | Pass | Valid report query |
| Low-stock inventory report | Pass | Valid report query |
| `SELEC customer_id...` | Fail | SELECT is misspelled and FROM is missing |
| Orders query without date filter | Fail | Missing date range control |
| `DELETE FROM orders` | Critical | Destructive query |
| `WHERE status = active` | Fail | String value should be quoted |
| Customer records updated this month | Pass | Valid date-filtered query |

---

## SQL QA Checklist

Before approving SQL in an automation, check:

- Is the syntax valid?
- Are table names correct?
- Are required filters present?
- Are date ranges controlled?
- Are strings quoted correctly?
- Is the query read-only where expected?
- Are destructive actions blocked?
- Are credentials protected?
- Is the output schema expected?

---

## QA Principle

SQL automation defects can create incorrect reports, data loss, or customer trust issues.
