# Customer Handover Template

## Purpose

This template documents what the customer receives when an automation is delivered.

---

## Automation Name

Add automation name here.

## Business Purpose

Describe the business problem the automation solves.

## What The Automation Does

Explain the workflow in simple operational terms.

Example:

1. Reads an input CSV file.
2. Validates required fields.
3. Generates a cleaned report.
4. Saves the report in the output folder.
5. Logs accepted and rejected rows.

---

## Customer Requirements Covered

| Requirement | Covered | Notes |
|---|---|---|
| Input data processed | Pending | |
| Output report created | Pending | |
| Errors visible | Pending | |
| Customer can run workflow | Pending | |
| Known limitations documented | Pending | |

---

## How To Run

Add clear run steps.

Example:

```bash
python run_inventory_report.py
```

---

## Required Inputs

| Input | Description | Required |
|---|---|---|
| Input file | Customer data file | Yes |
| Config file | Automation settings | If applicable |
| API key | Required for API workflows | If applicable |

---

## Expected Outputs

| Output | Description |
|---|---|
| Report file | Main customer output |
| Log file | Execution evidence |
| Rejected rows file | Data-quality issues if applicable |

---

## Success Criteria

The automation is successful when:

- the workflow completes without unhandled errors
- the expected output is created
- rejected or invalid rows are reported
- logs are available
- customer acceptance criteria are met

---

## Known Limitations

Document anything the automation does not handle.

Examples:

- only supports CSV input
- only supports one worksheet
- requires stable column names
- requires valid API credentials
- does not send emails automatically
- requires human review for ambiguous AI outputs

---

## Support / Escalation

Add support route here.

## Customer Sign-Off

| Name | Role | Date | Approved |
|---|---|---|---|
| | | | |
