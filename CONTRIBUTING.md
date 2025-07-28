
# Contributing Guide

This guide will help you contribute effectively and consistently.

we use git branches and pull request (PRs) to merge contributions

This guide walks you through the correct steps to create your branch, push your work, and submit it for review.
...

## GETTING STARTED

## 📦 Cloning the Repository (First-Time Setup)
--If you haven’t cloned the repo yet:

```bash
git clone https://github.com/YOUR_ORG/YOUR_REPO.git
```
## Navigate into the directory that was created after cloning in your IDE(text-editor)
```
cd your-repo
```

## 🌱 Create a New Branch
--Give your branch a meaningful name that describes your work

examples:
kyc-document,
user-auth,
api-endpoints.

```bash
git checkout -b your-branch-name
```
PS. you can create a branch without being ready to push


## ✍️ Make Your Changes
Work on your Django project as needed.

```bash
git add .
git commit -m "your commit message"
```


## 🚀 Push Your Branch to GitHub

1. push to your branch first
   ```bash
   git push origin your-branch-name
   ```
   
2.Visit the GitHub repository in your browser,

3.You’ll see a prompt to "Compare & pull request" — click it.
3.Add a title and description for your work.
4. wait for review before merging.

## ❗ Troubleshooting
-Always create a new branch before working, never commit directly to main.

```bash
"fatal: not a git repository" — This means you're not inside the repo directory. Use cd YOUR-REPO to enter it.
```

## 🗒️ Final Notes
-Every contributor works on their own branch to avoid conflicts.

-Code reviews are done via pull requests before merging into main.

Thank You.

