# Git Workflow Commands

## Purpose

This file documents the basic Git workflow used to manage the repository.

It is useful for showing familiarity with controlled change, traceability, and small-team collaboration.

---

## 1. Check Repository Status

```bash
# Show changed, staged, and untracked files.
git status
```

### Explanation

Use this before and after making changes.

It shows:

- current branch
- modified files
- staged files
- untracked files

---

## 2. Stage Files

```bash
# Stage all current changes.
git add .
```

### Explanation

This prepares all current changes for commit.

---

## 3. Commit Files

```bash
# Commit staged files with a meaningful message.
git commit -m "Build SME automation QA lab repository"
```

### Explanation

A commit is a named snapshot of the project.

Use clear commit messages that explain what changed.

---

## 4. Rename Branch To Main

```bash
# Rename current branch to main.
git branch -M main
```

### Explanation

This ensures the default branch is named `main`.

---

## 5. Add GitHub Remote

```bash
# Connect the local repository to GitHub.
git remote add origin https://github.com/desf-vict/sme_automation_qa_lab.git
```

### Explanation

Replace the URL if your GitHub username or repository name is different.

---

## 6. Push To GitHub

```bash
# Push the main branch to GitHub.
git push -u origin main
```

### Explanation

This uploads the local repository to GitHub.

The `-u` option links the local branch to the remote branch.

---

## 7. Normal Update Workflow

After the first push, use:

```bash
git status
git add .
git commit -m "Describe the change"
git push
```

---

## QA Principle

Git supports QA by making project changes traceable and reviewable.
