# Final Commands

## Purpose

This file lists the final commands to run after generating the repository.

---

## 1. Run The Repository Generator

```bash
python build_sme_automation_qa_repo.py
```

---

## 2. Run Validation Scripts

```bash
python validation/json_validator.py
python validation/csv_inventory_validator.py
python validation/api_import_validator.py
```

---

## 3. Check Git Status

```bash
git status
```

---

## 4. Commit And Push

```bash
git add .
git commit -m "Build SME automation QA lab repository"
git branch -M main
git remote add origin https://github.com/desf-vict/sme_automation_qa_lab.git
git push -u origin main
```

---

## 5. Open Dashboard

Open this file in a browser:

```text
dashboard/index.html
```

---

## Expected Result

The repository should contain:

- documentation
- checklists
- automation test cases
- datasets
- expected and defective outputs
- validation scripts
- SQL review examples
- bug reports
- incident reports
- integration notes
- AI workflow tests
- handover templates
- dashboard

---

## Final QA Principle

A repository is interview-ready when the structure, purpose, evidence, and demonstration path are clear.
