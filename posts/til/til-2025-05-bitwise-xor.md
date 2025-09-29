---
date: '2025-05-07T03:30:43.170061'
description: How to mark a comparison of booleans as True or False using bitwise XOR.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: ^ bitwise XOR'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

The bitwise XOR operator `^`, also known as `exclusive or`, can be used to compare boolean objects to see if one and only one is `True`.

Let's see it in action, first comparing three `False` booleans, which will return `False`.

```python {.marimo}
False ^ False ^ False
```

Now let's demonstrate three different combinations of a single `True` and any number of `False` booleans, which will return `True` in each case.

```python {.marimo}
print(True ^ False ^ False)
print(False ^ True ^ False)
print(False ^ False ^ True)
```

However, if we have two or more values that are `True`, the result will be `False` because more than one value are `True`.

```python {.marimo}
print(True ^ True ^ False)
print(True ^ False ^ True)
print(False ^ True ^ True)
```

## What about non-boolean types?

The `^` operator only works with boolean types. If you try to use it on non-boolean types, you'll get a `TypeError`. For example, if you try to use it on integers or strings to check for truthiness, you'll get an error.

```python
'' ^ '' ^ 'one'
```

```
>>>
TypeError                   Traceback (most recent call last)
Cell In[20], line 1
>>> 1 '' ^ '' ^ 'one'

TypeError: unsupported operand type(s) for ^: 'str' and 'str'
```
To make this comparison works, you can convert the non-boolean types to boolean first. For example, you can use the `bool()` function to convert an integer or string to a boolean before using the `^` operator.

```python {.marimo}
bool('') ^ bool('') ^ bool('one')
```

## Updates

- 2025-05-07: Updated the post to describe XOR only returns `True` if one (and only one) of the values is `True`. Removed the segment on `any()` as it is too far away in design from `XOR`.  Credit for this fix goes to [Curt Merrill](https://bsky.app/profile/cmerrill.com) and [Rens Dimmendaal](https://rensdimmendaal.com/).

```python {.marimo hide_code="true"}
mo.md(
    r"""

    """
)
```

```python {.marimo}
import marimo as mo
```