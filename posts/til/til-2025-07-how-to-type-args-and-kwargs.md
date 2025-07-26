---
date: '2025-07-26T16:35:07.896468'
description: A reduction in boilerplate confused me, the answer is that the type to
  define is the value in the containers.
image: /public/logos/til-1.png
published: true
tags:
- howto
- python
- TIL
title: 'TIL: How to type args and kwargs'
twitter_image: /public/logos/til-1.png
---

An oddity of my work for a while has been that I haven't used `*args` and `**kwargs` with type annotations. Recently, however I've been working on code that leans on those things a lot. And I've been ignoring setting types there because this fails wretchedly with type checking libraries:

```python
# This fails type checls. :(
from typing import Any

def func(*args: tuple[str], **kwargs: dict[str, Any]):
    pass
```

That's because the types you set apparently the value of the container. So to make my code pass the type checkers I need to do:

```python
# This passes type checks!
from typing import Any

def func(*args: str, **kwargs: Any):
    pass
```

Thanks to [Will McGugan](https://willmcgugan.github.io/) for explaining this to me. I'm a fan of his work, which includes the inestimable [Rich](https://github.com/Textualize/rich) and [Textualize](https://textual.textualize.io/) libraries!