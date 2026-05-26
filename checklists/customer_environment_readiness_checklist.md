# Customer Environment Readiness Checklist

## Purpose

This checklist verifies whether an automation is likely to work in the customer's real environment.

The goal is to identify environment blockers before delivery.

---

## Customer Environment Details

| Item | Value | Status | Notes |
|---|---|---|---|
| Customer name | | Pending | |
| Contact person | | Pending | |
| Operating system | | Pending | |
| User permissions confirmed | | Pending | |
| Required runtime available | | Pending | |
| Required application installed | | Pending | |
| Network access confirmed | | Pending | |
| API access confirmed | | Pending | |
| Test data available | | Pending | |
| Output destination confirmed | | Pending | |

---

## Runtime Checks

Check whether the automation requires any of the following:

- Python
- Node.js
- PowerShell
- Bash
- Excel
- Google Sheets
- Outlook
- Gmail
- browser automation
- database client
- API client
- third-party desktop software

---

## File And Folder Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| Input folder exists | Folder available | Pending | |
| Output folder exists | Folder available | Pending | |
| User can read input files | Read permission available | Pending | |
| User can write output files | Write permission available | Pending | |
| File naming convention confirmed | Names match automation expectation | Pending | |
| Test file available | Realistic test data available | Pending | |

---

## Credential And Secret Checks

| Check | Expected Result | Status | Notes |
|---|---|---|---|
| API key available | Key provided securely | Pending | |
| Password not hard-coded | No secret in script | Pending | |
| Environment variables documented | Variables listed | Pending | |
| Token expiry understood | Expiry documented | Pending | |
| Access level confirmed | Minimum access only | Pending | |

---

## Network And Access Checks

- Internet access available if required
- Corporate proxy reviewed if present
- Firewall restrictions checked
- API endpoint reachable
- Database reachable
- Email service reachable
- Cloud storage reachable if used

---

## Blocking Conditions

Mark the automation as blocked if:

- required credentials are missing
- the customer cannot access required folders
- the runtime is unavailable
- the required application is missing
- the API cannot be reached
- the customer cannot provide test data
- the output location is unclear

---

## QA Principle

Customer-environment readiness should be checked before the automation is considered deliverable.
