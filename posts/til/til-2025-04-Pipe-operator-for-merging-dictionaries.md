---
date: '2025-04-27T19:05:35.433062'
description: In Python 3.9 and later, the pipe operator | can be used to merge dictionaries.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Pipe operator for merging dictionaries'
twitter_image: /public/logos/til-1.png
---
<!---->
Pipe `|` returns a new dictionary containing the key-value pairs from both operands.

```python {.marimo}
a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
_merged = a | b
print(a)
```

If there are duplicate keys, the value from the right-hand operand will overwrite  the value from the left-hand operand.

```python {.marimo}
left = {'a': 1, 'b': 2}
right = {'a': 3, 'b': 4}
_merged = left | right
print(_merged)
```

The `|=` is related, updating the left-hand operand in place much like the `+=` operator.

```python {.marimo}
original = {'a': 1, 'b': 2}
new = {'b': 3, 'c': 4}
original |= new # Analogous to original.update(new)
print(original)
```

```python {.marimo}
import marimo as mo
```