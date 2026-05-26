# 06 — Severity Levels

## Purpose

Severity levels help prioritise issues found during automation QA.

## Severity Model

| Severity | Meaning | Example |
|---|---|---|
| Critical | Data loss, security exposure, or unusable automation | Customer records overwritten |
| High | Main workflow broken or output unusable | Report not generated |
| Medium | Partial failure with workaround | Some rows require manual cleanup |
| Low | Minor issue or documentation defect | Typo in handover notes |

## Severity Guidance

Severity should be based on customer impact, not personal frustration.

## Examples

| Issue | Suggested Severity |
|---|---|
| Automation silently updates wrong CRM record | Critical |
| CSV report fails when quantity is blank | High |
| Error message is unclear but workflow stops safely | Medium |
| Dashboard link text is unclear | Low |
| AI invents a customer commitment | High |
| API key printed in logs | Critical |

## Expected Learning Outcome

The reader should be able to classify automation QA defects by operational risk.
