# 03 — Small Team Delivery Reality

## Purpose

Small developer teams often work under tight delivery schedules.

They need practical QA support that is clear, fast, and useful.

## Typical Small-Team Workflow

A common workflow may look like this:

1. Customer requests automation.
2. Developer builds a script or workflow.
3. Automation is tested with sample data.
4. QA checks expected versus observed behaviour.
5. Bugs are reported clearly.
6. Fixes are retested.
7. Customer-environment readiness is checked.
8. Handover material is prepared.
9. Customer accepts or rejects delivery.

## What Can Go Wrong

Automations may fail because:

- test data is too clean
- the customer file format is slightly different
- the script assumes a local path
- credentials are missing
- the API response changes
- the customer uses a different spreadsheet format
- the workflow fails silently
- the automation produces plausible but wrong output

## QA Value

QA adds value by making failure visible before the customer sees it.

## Expected Learning Outcome

The reader should understand why delivery QA is useful even when the automation appears simple.
