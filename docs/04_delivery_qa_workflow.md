# 04 — Delivery QA Workflow

## Purpose

This document defines a simple QA workflow for validating automations before customer delivery.

## Workflow

| Step | Action | Output |
|---|---|---|
| 1 | Understand the customer request | Requirement notes |
| 2 | Identify inputs and outputs | Input/output map |
| 3 | Run smoke test | Basic pass/fail result |
| 4 | Test realistic customer data | Evidence files |
| 5 | Test edge cases | Edge-case results |
| 6 | Check integrations | Integration notes |
| 7 | Review errors and logs | Error-handling notes |
| 8 | Report bugs | Bug report files |
| 9 | Retest fixes | Retest result |
| 10 | Confirm handover readiness | Delivery checklist |

## QA Rule

A workflow is not complete until the output has been checked against the customer's expected result.

## Practical Evidence

Evidence may include:

- input files
- output files
- screenshots
- logs
- bug reports
- incident notes
- checklist status

## Expected Learning Outcome

The reader should understand the basic delivery QA loop:

> test, observe, document, retest, approve.
