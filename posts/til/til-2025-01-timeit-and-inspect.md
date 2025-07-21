---
date: "2025-01-14T15:30:00.00Z"
description: "Two libraries in Python's standard library that are useful for keeping load testing code all in one module."
published: true
tags:
  - python
  - TIL
  - load testing
time_to_read: 2
title: "TIL: Using inspect and timeit together"
type: post
---

When working with `timeit` you either have to write code in string variables or load a seperate Python module as code. The former is a really not a good idea, the latter is ideal but annoying for quick tests. So I thought this up today, probably reinventing what someone else has done.

For an example let's define a simple function we want to test that generates a random 10 character string:

```python {.marimo}
def get_random_string(length=10):
    from random import choice
    from string import ascii_letters
    return ''.join(choice(ascii_letters) for _ in range(length))
get_random_string()
```

You'll notice that the imports are in the calling function. That makes the next step a bit easier. That's where we use `inspect.getsource()` to save the code of get_random_string to a variable called `setup_stmt`.

```python {.marimo}
from inspect import getsource
setup_stmt = getsource(get_random_string)
print(setup_stmt)
# The 'code' below is a printed string in a notebook cell, not actual code
```

Next step is we create a `code_stmt` variable that calls that function.

```python {.marimo}
code_stmt = 'get_random_string()'
```

Now we can plug that into a timeit module to see how fast it runs.

```python {.marimo}
from timeit import timeit
timeit(stmt=code_stmt, setup=setup_stmt)
```

Again, the advantage of this approach is that it's all in one module and we can easily test that the function works before sticking it in timeout.

```python {.marimo}
import marimo as mo
```