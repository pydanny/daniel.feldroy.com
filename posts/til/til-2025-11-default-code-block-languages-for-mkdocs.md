---
date: '2025-11-22T12:08:34.618632+00:00'
description: Really useful for making inline code examples have code highlighting.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
- markdown
title: 'TIL: Default code block languages for mkdocs'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

When using [Mkdocs with Material](https://squidfunk.github.io/mkdocs-material/) theme, you can set default languages for code blocks in your `mkdocs.yml` configuration file. This is particularly useful for inline code examples that may not have explicit language tags.

```yaml
markdown_extensions:
  - pymdownx.highlight:
      default_lang: python
```

You can see what this looks like in practice with Air's API reference for forms here: [feldroy.github.io/air/api/forms/](https://feldroy.github.io/air/api/forms/). With this configuration, any code block without a specified language defaults to Python syntax highlighting, making documentation clearer and more consistent.