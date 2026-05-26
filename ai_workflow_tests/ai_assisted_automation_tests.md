# AI-Assisted Automation Tests

## Purpose

This document defines QA checks for AI components used inside business automations.

The focus is on whether AI output is safe and reliable enough to support a customer workflow.

---

## AI Workflow Risks

| Risk | Example | QA Check |
|---|---|---|
| Hallucination | AI invents customer data | Compare output against source |
| Schema drift | JSON fields change between runs | Validate structure |
| Unsupported commitment | AI promises a price or deadline | Check source evidence |
| Unsafe automation action | AI triggers update without review | Require approval gate |
| Ambiguous extraction | AI guesses missing fields | Require human review |
| Format failure | AI returns prose instead of JSON | Validate output format |

---

## Test 1 — Email Field Extraction

### Input

Use:

```text
datasets/customer_email_samples.md
```

### Expected Behaviour

The AI extraction should:

- extract only fields present in the source
- leave missing fields blank
- mark ambiguous cases for human review
- avoid inventing names, phone numbers, companies, or actions
- return valid structured output if JSON is requested

### Failure Conditions

The test fails if:

- the AI invents missing information
- the AI marks ambiguous data as certain
- the AI changes the customer request
- the AI output cannot be parsed
- the AI skips the human review flag

---

## Test 2 — Customer Reply Draft

### Input

Use a customer email, ticket, or CRM note.

### Expected Behaviour

The draft reply should:

- respond to the customer request
- stay within known facts
- avoid unsupported promises
- use a professional tone
- escalate sensitive or contractual issues
- remain a draft unless approved by a human

### Failure Conditions

The test fails if:

- the AI promises a refund without source approval
- the AI invents a delivery date
- the AI invents pricing
- the AI exposes internal notes
- the AI sends or finalises the reply without review

---

## Test 3 — Structured JSON Output

### Prompt Pattern

```text
Extract the customer name, company, request type, urgency, and required action.
Return only valid JSON.
```

### QA Checks

- Is the output valid JSON?
- Are all required fields present?
- Are field names stable?
- Are unknown values blank or marked unknown?
- Is human review flagged where required?
- Does the AI add prose outside the JSON?

---

## QA Principle

AI inside an automation should be treated as an unreliable component until its output is validated.
