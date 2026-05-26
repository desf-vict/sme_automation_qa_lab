# GitHub Project Setup

## Purpose

This document explains how to create and publish the new SME Automation QA Lab repository.

---

## Recommended Repository Name

```text
sme_automation_qa_lab
```

---

## Recommended Repository Description

```text
Practical QA lab for validating SME business automations, customer-environment readiness, integrations, AI-assisted workflows, and delivery handover.
```

---

## Repository Visibility

Use **Private** while preparing the project.

Change to **Public** only if you are ready to show it externally.

---

## GitHub Creation Steps

1. Go to GitHub.
2. Create a new repository.
3. Name it `sme_automation_qa_lab`.
4. Keep it private if the project is still being prepared.
5. Do not initialise with README, `.gitignore`, or licence.
6. Create the repository.
7. Push the local files using the commands in `docs/git_workflow_commands.md`.

---

## Initial Push Commands

Run from the local project folder:

```bash
git init
git add .
git commit -m "Build SME automation QA lab repository"
git branch -M main
git remote add origin https://github.com/desf-vict/sme_automation_qa_lab.git
git push -u origin main
```

---

## After Push

Check GitHub and confirm:

- README displays correctly
- folders are visible
- dashboard file exists
- validation scripts are uploaded
- test cases are uploaded
- bug reports are uploaded
- handover documents are uploaded

---

## Interview Use

During an interview, this repository can be explained as:

> A practical QA lab for checking whether automations, scripts, integrations, and AI-assisted workflows are reliable enough for SME customer delivery.

---

## QA Principle

A GitHub repository should make the project understandable before anyone opens the code.
