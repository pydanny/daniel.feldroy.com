---
date: "2025-01-01T19:30:00.00Z"
description: "For the past six months or so I've been using fastcore. It provides two handy bunch-class style that I've leveraged into projects."
published: false
tags:
  - python
  - fastcore
  - bunch
time_to_read: 2
title: "Exploring fastcore bunch classes"
type: post
---

The fastcore library has a lot of really useful tools. As a fan of bunch classes, here's two useful utilities for working with them.

## AttrDict

`AttrDict` adds attributes to python `dict` without changing equality or how it prints.

```python {.marimo}
from fastcore.basics import AttrDict
```

```python {.marimo}
daughter = AttrDict(name='Uma', age=6)
daughter
```

Equality is the same as a `dict`.

```python {.marimo}
daughter == {'age': 6, 'name': 'Uma'}
```

Values can be accessed either as `dict` or with `dot` notation.

```python {.marimo}
daughter['name']
```

```python {.marimo}
daughter.name
```

## NS

`NS` extends `types.SimpleNamespace` (which I covered [here](/posts/til-2024-12-types-simplenamespace-is-a-bunch-class)), providing useful access functionality similar to that of `AttrDict`. Unlike `AttrDict`, equality is not that of a `dict` and is covered below.

```python {.marimo}
from fastcore.basics import NS
```

```python {.marimo}
daughter_1 = NS(name='Uma', age=6)
```

Equality of `NS` is with `types.SimpleNamespace`, which is the difference between it and `AttrDict`, whose equality is as a `dict` type.

```python {.marimo}
import types
daughter_1 == types.SimpleNamespace(name='Uma', age=6)
```

Values can be accessed either as `dict` or with `dot` notation.

```python {.marimo}
daughter_1['name']
```

```python {.marimo}
daughter_1.name
```

```python {.marimo}
list(daughter_1)
```

```python {.marimo}
import marimo as mo
```