# 08 — Final Review Process

## Purpose

This document defines the final review process before an automation is considered ready for customer handover.

## Final Review Questions

Ask:

- Does the automation satisfy the customer request?
- Has it been tested with realistic data?
- Has bad input been tested?
- Are outputs correct?
- Are logs or errors understandable?
- Are credentials protected?
- Are assumptions documented?
- Is rollback possible?
- Are known issues documented?
- Is the handover material clear?

## Delivery Decision

| Decision | Meaning |
|---|---|
| Ready | Automation can be delivered |
| Ready with notes | Minor known issues exist |
| Blocked | Major issue prevents delivery |
| Needs customer clarification | Requirement is unclear |
| Needs developer fix | Defect must be corrected |

## QA Principle

Final review is a delivery-risk decision, not only a technical check.

## Expected Learning Outcome

The reader should understand how to decide whether an automation is ready to be handed over.
