---
date: '2026-03-13T02:41:19.009972+00:00'
description: I believe operations that change things should always return values.
published: true
tags:
- python
- rant
title: To return a value or not return a value
---

I believe any function that changes a variable should return a variable. For example, I argue that Python's `random.shuffle()` is  flawed. This is how `random.shuffle()` unfortunately works:

```python
import random

my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Change happens in place
# my_list is forever changed
random.shuffle(my_list) 
print(f"Shuffled list: {my_list}")
```

In my opinion, `random.shuffle()` should work like this:

```python
import random

my_list = [1, 2, 3, 4, 5]

# Function returns a new, shuffled list
new_list = random.shuffle(my_list)
print(f"Original list: {my_list}")
print(f"Shuffled list: {new_list}")
```

Of course, Python won't fix this mistake to fit my preference. There's too many places in the universe expecting `random.shuffle` to change a list in place. Yet it still bugs me every time I see the function. Stuff like this is why I created my [listo](https://github.com/pydanny/listo) package, it allowed me to get past my own sense of annoyance. It's a library that is barely used, even by myself, serving as mostly a fun exercise that allowed me to scratch an itch about objects changing in place.


## Counterargument

Some of you might say, "It's not practical to return giant `dict` or `list` objects when you are changing a single value". You are correct. However, does it make sense for `random.shuffle` and other offenders to muck around with the entirety of a variable's contents? Why shouldn't a function that disrupts the entirety of a variable just return a new variable?

## Closing statement

My preference is that when it is reasonable, that the scope is not outrageous, to create functions that return values.

Also, to the people who implemented the original `random.shuffle` function, you are awesome. I'm just taking advantage of having 20/20 hindsight.
