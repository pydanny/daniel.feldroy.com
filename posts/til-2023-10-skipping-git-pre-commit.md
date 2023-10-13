---
date: "2023-10-13T15:45:00.00Z"
published: true
slug: til-2023-10-skipping-git-pre-commit
tags:
  - git
  - TIL
time_to_read: 1
title: "TIL: Skipping git pre-commit"
description: For saving WIP commits to a remote repo.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

For saving WIP commits to a remote repo. You really don't want to know what I was doing before.

Just add `--no-verify` to whatever you are doing:

```bash
git commit -am "Fun code noodling" --no-verify
git commit --amend
```