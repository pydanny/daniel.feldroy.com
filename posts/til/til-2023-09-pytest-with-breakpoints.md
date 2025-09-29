---
date: "2023-09-06T15:45:00.00Z"
published: true
slug: til-2023-09-pytest-with-breakpoints
tags:
  - python
  - testing
  - TIL
time_to_read: 1
title: "TIL: pytest with breakpoints"
description: Injecting breakpoints into a failing pytest run
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

To inject a breakpoint into a failing pytest run, add `--pdb` to your `pytest` command:

```bash
py.test --pdb
```

This will drop you into a pdb session at the point of failure. You can then inspect the state of the program just like you would if you injected a `breakpoint()`.

