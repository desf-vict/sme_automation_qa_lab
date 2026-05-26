# Regression Test Checklist

## Purpose

Regression testing checks whether a new fix or change has broken something that previously worked.

This is important when developers are working under tight schedules.

---

## Regression Scope

| Area | What To Check | Status | Notes |
|---|---|---|---|
| Main workflow | Still runs end to end | Pending | |
| Previous bug fix | Original defect remains fixed | Pending | |
| Input handling | Existing accepted inputs still work | Pending | |
| Output format | Output schema did not change unexpectedly | Pending | |
| Error handling | Existing errors still handled clearly | Pending | |
| Logs | Logs still generated | Pending | |
| Customer instructions | Instructions still accurate | Pending | |

---

## Regression Evidence

Save or reference:

- previous failing input
- new output after fix
- log file
- screenshot if useful
- related bug report
- retest notes

---

## QA Principle

A fix is not complete until the original issue is retested and nearby functionality is checked.
