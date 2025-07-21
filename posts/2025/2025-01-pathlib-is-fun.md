---
date: "2025-01-26T16:30:00.00Z"
description: "When using Python to interact with file systems, Pathlib is where you should start."
published: false
tags:
  - python
  - howto
  - fastcore
time_to_read: 5
title: "Pathlib is fun!"
type: post
---
<!---->
## Directory objects
<!---->
First, we import the `Path` class from pathlib. The `Path` is 99.9% of what you'll ever need to use.

```python {.marimo}
from pathlib import Path
```

Let's create a object representation of the directory in which this file resides:

```python {.marimo}
dir_path = Path('.')
dir_path
```

Now on this blog post's file:

```python {.marimo}
blog_post = Path('2025-01-pathlib-is-fun.ipynb')
blog_post
```

Let's create a new file:

```python {.marimo}
new_file = Path('blarg.md')
new_file.exists() # Not yet created
```

Create the file using the `touch` method. This creates a blank text file

```python {.marimo}
new_file.touch()
new_file.exists()
```

## Coding Standard: PEP-8
<!---->
With a few exceptions, Pathlib adheres to the [PEP-8 style guide](https://peps.python.org/pep-0008/). Following any styleguide eases discovery and reduces coding errors.

Below is a table that shows some of the naming differences

```python {.marimo hide_code="true"}
mo.md(
    r"""

    """
)
```

```python {.marimo hide_code="true"}
mo.md(
    r"""

    """
)
```

```python {.marimo}
import marimo as mo
```