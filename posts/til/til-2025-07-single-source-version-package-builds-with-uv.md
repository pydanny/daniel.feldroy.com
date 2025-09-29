---
date: '2025-07-23T01:59:20.353392'
description: Tired of updating the version in multiple places before publishing a package update? Leery of using inspect.metadata to fetch the package? Here's how to have a single source of version using UV's build subcommand.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Single source version package builds with uv'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

1. Remove `version` in `pyproject.toml` and replace with `dynamic = ["version"]`
2. Add `[tool.setuptools.dynamic]` and specify the location of the version using this dialogue: `version = { attr = "mypackage.__version__" }`
3. In your project's root `__init__.py`, add a `__version__` attribute.

Example:


```toml
# pyproject.toml
[project]
name = "mypackage"
dynamic = ["version"]
# version = "0.1.0" # Don't set version here

[tool.setuptools.dynamic]
version = { attr = "mypackage.__version__" } # Set version here
```

Don't forget to specify the version in Python:

```python
# mypackage/__init__.py
__version__ = "0.1.0"
```

Thanks to Audrey Roy Greenfeld for pairing with me on getting this to work.