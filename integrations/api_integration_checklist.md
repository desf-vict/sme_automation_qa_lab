# API Integration Checklist

## Purpose

This checklist validates API-based automations before customer delivery.

---

## API Connection Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Endpoint configured | Correct API URL used | Pending | |
| Authentication works | Valid token or key accepted | Pending | |
| Invalid token handled | Clear error returned | Pending | |
| Expired token handled | Clear error returned | Pending | |
| Timeout handled | Retry or clear failure | Pending | |
| Rate limit handled | Wait, retry, or clear failure | Pending | |

---

## API Data Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Required fields present | Missing fields detected | Pending | |
| Duplicate records detected | Duplicates flagged | Pending | |
| Pagination handled | All pages imported | Pending | |
| Counts reconciled | Received/imported/rejected counts match | Pending | |
| Invalid records rejected | Bad data not imported silently | Pending | |

---

## Security Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| API keys not hard-coded | No secrets in source code | Pending | |
| API keys not logged | No secrets in output logs | Pending | |
| Minimum permissions used | Token scope appropriate | Pending | |

---

## QA Principle

API success means more than a 200 response.

The imported data must also be complete, correct, and safe to use.
