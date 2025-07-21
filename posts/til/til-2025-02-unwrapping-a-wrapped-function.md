---
date: '2025-02-21T18:00:00.000000'
description: Another reason to use functools.wraps!
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Undecorating a functools.wraps decorated function'
twitter_image: /public/logos/til-1.png
---
<!---->
In the Python standard library there is a function in the functools library that allows decorated functions to carry forward their original docstring. Executing it is rather easy:

```python {.marimo}
from functools import wraps
def kerpow(f):
    """Prints the string KERPOW!"""
    @wraps(f)
    def wrapper(*args, **kwds):
        print(f'KERPOW {f.__name__}!')
        return f(*args, **kwds)
    return wrapper
```

Let's try it out.

```python {.marimo}
@kerpow
def adder(a,b):
    """Adds the arguments together"""
    return a+b
```

Let's call the function. What we should get in addition to the sum of the values passed is the printed value of "KERPOW" plus the name of the function.

```python {.marimo}
adder(1,2)
```

As mentioned, the `functools.wraps` decorator preserves the docstring:

```python {.marimo}
adder.__doc__
```

As you can see, `functools.wraps` is an easy addition to any decorator that makes keeping documentation valid trivial to do.
<!---->
However, what if we want to use the `adder` function without printing "KERPOW adder!" to the terminal? In other words, can we remove the decorator?

Fortunately, because we used `functools.wraps` we can do just that. You see, what `functools.wraps` does is add a `__wrapped__` attribute to the wrapped function. If we want to restore the function to the original we do this:

```python {.marimo}
adder_1 = adder.__wrapped__
```

Now if we call `adder`, we won't see "KERPOW adder!" any longer going to the terminal.

```python {.marimo}
adder_1(2, 3)
```

## Postscript
<!---->
In a follow-up discussion about this TIL I learned that `functools.wraps` is syntactical sugar for the [functools.update_wrapper()](https://docs.python.org/3/library/functools.html#functools.update_wrapper) function.

```python {.marimo hide_code="true"}
mo.md(
    r"""

    """
)
```

```python {.marimo}
import marimo as mo
```