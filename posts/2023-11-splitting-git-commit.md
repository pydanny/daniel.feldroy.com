---
date: "2023-11-13T14:00:00.00Z"
published: true
slug: 2023-11-splitting-git-commit
tags:
  - git
  - howto
time_to_read: 5
title: Splitting Git Commits
description: How to split a git commit into multiple commits.
type: post
---

Something I periodically do and need to document here where I can find it fast.

To reset the most recent commit:

```sh
git reset HEAD~
```

This reverts the commit. Then you can commit individual or groups of files in multiple commits


## What if your commit isn't the most recent one?

Use an interactive rebase to commit things further back. Follow these steps

1. Find the commit hash with either `git log` or `git reflog`

2. Start a rebase with the commit hash replacing `HASH` below

```sh
git rebase -i HASH
```

3. In the rebase edit screen that comes up, find the line with the commit you want to split. Replace `pick` with `edit`

4. Save and close the rebase edit screen

5. Reset to the previous commit with `git rebase HEAD~`

6. Create new commits using the files and writing the messages that go along with them

```sh
git add file/to/be/committed.xyz
git commit -m "Enhance the algorithm to support Mars rovers"
```

7. Finish the rebase:

```sh
git rebase --continue
```