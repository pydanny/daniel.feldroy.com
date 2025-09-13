---
date: '2025-09-13T08:49:50.670264+00:00'
description: "Attribution matters to me, I want contributors to always get full credit for their effort. This is how you preserve the git history of a project you are bringing into another project."
image: /public/logos/til-1.png
published: true
tags:
- TIL
- git
title: 'TIL: Merging two git projects'
twitter_image: /public/logos/til-1.png
---

Of course this task can be done with copy/paste. The challenge there is the loss of git history. All the history of struggles and tribulations are gone. More important is the attribution - unless any and all contributors are made co-authors. But then the volume of attribution isn't accurate, some one who made one tiny change gets as much credit as the leading contributor.

A better way is to merge the repos together while preserving the git history. Let's imagine we want to merge repo #2 into repo #1:

1. **[AIR](https://github.com/feldroy/air)** (A new Python web framework). This is in a repo on my laptop called `air`
2. **AirDocs** (Documentation for AIR, getting merged into air). This is in a repo on github located at [github.com/feldroy/airdocs](https://github.com/feldroy/airdocs)

Here's how I did it:

## Step 1: Add an airdocs git remote to air

```sh
cd air/
git remote add -f airdocs git@github.com:feldroy/airdocs.git
```

## Step 2: Merge AirDocs into AIR

```sh
git merge airdocs/main --allow-unrelated-histories
```

At this point code conflicts may arise, which can be resolved. In our case, we made sure that the repos didn't have overlapping files. 