---
date: '2026-02-22T10:09:16.103693+00:00'
description: Another part of the process of switching from marked.js and python-markdown
  to just using mistletoe.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Using PygmentsRenderer with mistletoe as a partial'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

For the past 18 months or so on this site, I've been using [marked.js](https://marked.js.org/) for the web and [python-markdown](https://pypi.org/project/Markdown/) for the atom feed. I decided not long ago to switch to using [mistletoe](https://github.com/miyuchina/mistletoe) so there's one consistent source of truth for markdown rendering.

I also thought that instead of defining a reusable function that both the web and atom feed could use, I would just use Python's `functools.partial` to create a new function that has the `renderer` argument set to `PygmentsRenderer`. Normally I prefer fully defined functions over using `partial`, but in this case, since it is for my personal site it felt like a good use of [partial](https://daniel.feldroy.com/posts/python-partials-are-fun).

## Add the dependencies

```sh
uv add mistletoe pygments
```

## Create the partial function

```python
from functools import partial

import mistletoe
from mistletoe.contrib.pygments_renderer import PygmentsRenderer

markdown = partial(mistletoe.markdown, renderer=PygmentsRenderer)
```

## Use the new function

```python

html = markdown(markdown_string)
```

## See it in action

Here's the commits where I implemented this change, at least on the web side: [Using pygments for highlighting of code](https://github.com/pydanny/daniel.feldroy.com/commit/7cbeec1ff7a5835e0eed882b3dba483554012677). Before I change the atom feed generation to use this, I'll make sure that it renders nicely on planetpython and other feed aggregators. I'll post that in a seperate TIL when I do figure out how to do that.