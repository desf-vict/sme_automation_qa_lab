# 07 — Customer Environment Readiness

## Purpose

Customer-environment readiness checks whether the automation is likely to work outside the developer's machine.

## Environment Factors

Check the following:

- operating system
- Python or runtime version
- required packages
- file paths
- user permissions
- network access
- proxy or firewall restrictions
- API credentials
- spreadsheet software
- database access
- email account access
- input data location
- output destination

## Failure Example

A script may work on the developer's machine because the path is:

```text
C:\Users\developer\Desktop\input.csv
```

But the customer may need:

```text
C:\Users\customer\Documents\Automation\input.csv
```

## QA Principle

Hard-coded local assumptions should be found before delivery.

## Expected Learning Outcome

The reader should understand why real customer environment testing is different from local development testing.
