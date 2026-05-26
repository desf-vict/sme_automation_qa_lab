# CSV Inventory Bug 001 — Dirty Rows Accepted As Valid

## Summary

The inventory automation accepted rows with missing, invalid, duplicate, and negative values.

This creates incorrect reporting and could mislead the customer.

## Automation / Workflow

CSV to Excel report automation.

## Input

```text
datasets/customer_inventory_dirty.csv
```

## Expected Result

The automation should flag or reject:

- missing quantity
- non-numeric quantity
- missing unit price
- duplicate item ID
- missing item ID
- negative quantity

## Observed Result

The defective output accepted all rows and calculated incorrect values.

```text
outputs/inventory_report_defective.csv
```

## Steps To Reproduce

1. Use `datasets/customer_inventory_dirty.csv` as input.
2. Run the inventory report automation.
3. Open the generated report.
4. Compare the output against expected validation rules.
5. Observe that defective rows are marked as accepted.

## Severity

High

## Evidence

| Evidence | Path |
|---|---|
| Dirty input | datasets/customer_inventory_dirty.csv |
| Defective output | outputs/inventory_report_defective.csv |
| Validator | validation/csv_inventory_validator.py |

## Recommended Action

Add row-level validation before report generation.

The automation should stop safely or produce a QA summary showing rejected rows.

## Retest Notes

Retest using the dirty CSV after validation rules are added.
