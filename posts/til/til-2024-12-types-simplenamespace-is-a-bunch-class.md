---
date: "2024-12-25T02:00:00.00Z"
description: "Did you know that Python's types library has a bunch class implementation? How did I not see this before?!"
published: true
tags:
  - python
  - TIL
  - bunch
time_to_read: 2
title: "TIL: types.SimpleNamespace is a Bunch class"
type: post
---
<!---->
Early in my coding career I stumbling across the easy dot notations of bunch classes. I've created my own and even documented it a [two](/posts/2011-11-loving-bunch-class) [times](/posts/exploring-the-bunch-class). What I did not know until recently was the `types` library in core Python provides easy bunch class functionality. Credit to Jeremy Howard for schooling me on this one.

```python {.marimo}
from types import SimpleNamespace as ns
```

```python {.marimo}
daughter = ns(age=6, name='Uma')
daughter
```

Accessing attributes

```python {.marimo}
daughter.name
```

Accessing all the data at once

```python {.marimo}
daughter.__dict__
```

Useful for tracking age over time! And in list comprehension (and by extension generator expressions).

```python {.marimo}
ages = [ns(age=i, name='Uma') for i in range(5,10)]
ages
```

```python {.marimo}
import marimo as mo
```