# Automation Runbook Template

## Purpose

A runbook explains how to operate, monitor, and troubleshoot an automation.

---

## Automation Name

Add automation name here.

## Normal Run Procedure

1. Confirm input file or source is available.
2. Confirm credentials are available if required.
3. Run the automation.
4. Review console output or log file.
5. Confirm output was created.
6. Review rejected rows or warnings.
7. Send output to customer or business user if approved.

---

## Pre-Run Checklist

| Check | Status | Notes |
|---|---|---|
| Input available | Pending | |
| Output folder available | Pending | |
| Credentials available | Pending | |
| Network available | Pending | |
| Previous run completed | Pending | |

---

## Common Errors

| Error | Meaning | Action |
|---|---|---|
| Input file not found | File path is wrong or file missing | Check input location |
| Permission denied | User cannot read or write path | Check permissions |
| Authentication failed | API key or token invalid | Check credentials |
| Invalid CSV format | Input file structure changed | Review input columns |
| Empty output | No valid records found | Review source data |

---

## Rollback / Recovery

Document how to recover if the automation causes a bad output or update.

Examples:

- restore previous output file
- remove imported records
- rerun with corrected input
- disable scheduled execution
- escalate to developer

---

## Monitoring Evidence

Save:

- log file
- output file
- rejected rows file
- screenshot if needed
- bug report if failed

---

## QA Principle

A runbook reduces support dependency and makes customer operation safer.
