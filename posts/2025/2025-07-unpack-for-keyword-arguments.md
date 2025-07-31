---
date: '2025-07-27T16:55:06.265059+00:00'
description: "Keyword arguments can now be more narrowly typed by using typing.Unpack and typing.TypeDict."
published: true
tags:
- howto
- python
title: 'Unpack for keyword arguments'
---

Previously I wrote a [TIL on how to better type annotate callables with `*args` and `**kwargs`](https://daniel.feldroy.com/posts/til-2025-07-how-to-type-args-and-kwargs) - in essence you ignore the container and worry just about the content of the container. This makes sense, as `*args` are a tuple and `**kwargs` keys are strings.

Here's an example of that in action:

```python
>>> def func(*args, **kwargs):
...     print(f'{args=}')
...     print(f'{kwargs=}')
args=(1, 2, 3)
kwargs={'one': 1, 'two': 2}
```

In fact, if you try to force `**kwargs` to accept a non-string type Python stops you with a TypeError:

```python
>>> func(**{1:2})
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    func(**{1:2})
    ~~~~^^^^^^^^^
TypeError: keywords must be strings
```

This is all great, but what if you want your keyword arguments to consistently accept a pattern of arguments? So this passes type checks:

```python
from typing import TypedDict, Unpack

class Cheese(TypedDict):
    name: str
    price: int


def func(**cheese: Unpack[Cheese]) -> None:
    print(cheese)
```

Let's try it out:

```python
>>> func(name='Paski Sir', price=30)
{'name': 'Paski Sir', 'price': 30}
```

Works great! Now let's break it by forgetting a keyword argument:

```python
>>> func(name='Paski Sir')
{'name': 'Paski Sir'}
```

What? How about adding an extra keyword argument and replacing the `int` with a `float`:

```python
>>> func(name='Paski Sir', price=30.5, country='Croatia')
{'name': 'Paski Sir', 'price': 30.5, 'country': 'Croatia'}
```

**Still no errors? What gives?** The answer is that type annotations are for type checkers, and don't catch during runtime. See the [note at the top of the core Python docs on typing]:

> Note The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

For those times when we do need runtime evaluations of types, we lean on built-ins like `isinstance` and `issubclass`, which are quite seperate from type hints and annotations.

---

Thanks to the astute [Luke Plant](https://lukeplant.me.uk/) for pointing out `Unpack` to me and sending me down a quite pleasant rabbit hole. 