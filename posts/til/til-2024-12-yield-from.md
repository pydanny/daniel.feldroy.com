---
date: "2024-12-27T23:15:00.00Z"
description: "A variant of the yield statement that can result in more concise code."
published: true
tags:
  - python
  - TIL
time_to_read: 2
title: "TIL: yield from"
type: post
---
<!---->
Lets create a function that uses yield to deliver a generator.

```python {.marimo}
def row_fetcher(rows=5):
    for _x in range(rows):
        yield _x
row_fetcher()
```

```python {.marimo}
_cursor = row_fetcher()
print(next(_cursor))
for _x in _cursor:
    print(_x)
```

That works, but we can use `yield from` to make things more concise. Like the result of `row_fetcher()`, it it converts the function into a generator expression.

```python {.marimo}
def row_fetcher2(rows=5):
    yield from range(rows)
row_fetcher2()
```

The behavior is identical to a regular `yield`, just the [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) of `yield from` delivers more concise code.

```python {.marimo}
_cursor = row_fetcher2()
print(next(_cursor))
for _x in _cursor:
    print(_x)
```

Thanks to Jeremy Howard for suggesting `yield from` in a pull request that prompted me to finally look it up.

```python {.marimo hide_code="true"}
mo.md(
    r"""

    """
)
```

```python {.marimo}
import marimo as mo
```