---
date: "2023-09-06T15:45:00.00Z"
published: true
slug: til-2023-09-pytest-with-breakpoints
tags:
  - python
  - testing
  - til
time_to_read: 5
title: pytest with breakpoints
description: Adding breakpoints to pytest
type: post
---

To inject a breakpoint into a failing pytest run, add `--pdb` to your `pytest` command:

```bash
py.test --pdb
```

This will drop you into a pdb session at the point of failure. You can then inspect the state of the program just like you would if you injected a `breakpoint()`.

