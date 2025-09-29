---
date: '2025-08-22T02:20:08.473528+00:00'
description: Tired of updating the version in multiple places before publishing a
  package update? Here's how Adam Johnson told me I should be doing it.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Single source version package builds with uv (redux)'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

Not that long ago I wrote about [how to use UV to build packages with a single source of truth for the version number](https://daniel.feldroy.com/posts/til-2025-07-single-source-version-package-builds-with-uv). Since then, my friend [Adam Johnson](https://adamj.eu/) has pointed out that I could be doing it better. Here's how [he demonstrated](https://adamj.eu/tech/2025/07/30/python-check-package-version-importlib-metadata-version/) I should be doing it instead.

```toml
# pyproject.toml
[project]
name = "air"
version = "0.25.0" # This is the source of truth for the version number
```

The way to check programmatically the version number is to rely not on someone setting `__version__` in the code, but rather to use the following technique:

```python
from importlib.metadata import version
version = version("air")
print(version)  # This will print "0.25.0"
```

Thanks for the tip, Adam! This is a much cleaner and tool friendly way to ensure that the version number is consistent across your package without having to manually update it in multiple places.