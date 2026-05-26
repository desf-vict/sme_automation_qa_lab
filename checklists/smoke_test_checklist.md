# Smoke Test Checklist

## Purpose

A smoke test checks whether the automation is basically usable before deeper testing starts.

It should be fast, repeatable, and focused on obvious blockers.

---

## Smoke Test Steps

| Step | Expected Result | Status | Notes |
|---|---|---|---|
| Automation starts | No startup crash | Pending | |
| Required config loads | Config detected | Pending | |
| Test input is found | Input file or source available | Pending | |
| Main workflow runs | Process completes | Pending | |
| Output is created | Output file or record exists | Pending | |
| Logs are created | Execution evidence available | Pending | |
| No obvious exception | No unhandled crash | Pending | |

---

## Pass Criteria

The smoke test passes only if:

- the automation starts
- the main workflow runs
- an output is produced
- no unhandled crash occurs
- there is enough evidence to continue testing

---

## Fail Criteria

The smoke test fails if:

- the automation does not start
- the required input is missing
- configuration is missing
- credentials are missing
- the workflow crashes
- no output is created
- there is no visible error or log

---

## QA Principle

A failed smoke test means deeper testing should stop until the basic blocker is fixed.
