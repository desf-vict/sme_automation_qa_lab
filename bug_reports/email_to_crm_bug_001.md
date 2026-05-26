# Email To CRM Bug 001 — Automation Invents Customer Details

## Summary

The email-to-CRM workflow invented customer details from an ambiguous email.

This is unsafe because it may update the wrong CRM record or create false customer data.

## Automation / Workflow

Email to CRM update automation.

## Input

Ambiguous customer email from:

```text
datasets/customer_email_samples.md
```

## Expected Result

The automation should require human review because the email does not clearly identify:

- customer name
- company name
- phone number
- previous issue
- specific required action

## Observed Result

The defective output invented:

- customer name
- company name
- phone number
- urgency
- required action

Affected output:

```text
outputs/email_to_crm_defective_output.json
```

## Steps To Reproduce

1. Use Email 2 from `datasets/customer_email_samples.md`.
2. Run the email-to-CRM extraction workflow.
3. Review the generated structured output.
4. Observe invented fields.
5. Confirm that `human_review_required` is incorrectly set to `False`.

## Severity

High

## Evidence

| Evidence | Path |
|---|---|
| Source email | datasets/customer_email_samples.md |
| Defective output | outputs/email_to_crm_defective_output.json |
| Test case | test_cases/automation_workflows/02_email_to_crm_update.md |

## Recommended Action

Update the workflow so ambiguous emails require human review.

The automation should not invent fields that are not present in the source text.

## Retest Notes

Retest with ambiguous and complete email samples.
