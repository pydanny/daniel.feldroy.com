---
date: '2025-12-11T08:25:02.790731+00:00'
description: Using pyrefly to identify type failures on this site and then fixing one of them.
published: true
tags:
- python
- howto
- air
title: Adding Type Hints to my Blog
---

I've decided to add static type checking to my [blog engine project](https://github.com/pydanny/daniel.feldroy.com). The tool I chose is [pyrefly](https://pyrefly.org/), a fast, Rust-based library for checking types in Python.

### Installing Pyrefly with UV

My project uses `uv` for package management. To install `pyrefly` as a development-only dependency, I ran the following command:

```sh
uv add pyrefly --dev
```

`pyrefly` is a Rust-based Python tool, so its package includes pre-compiled binaries. This makes the package larger (around 10MB) than a pure Python equivalent. This can be an issue with a slower connection. However, `uv` caches the downloaded package, making subsequent installations of the same version much faster.

### Running the First Type Check

With `pyrefly` installed, I ran the first check across the entire project.

```sh
uv run pyrefly check .
```

The initial scan found 31 errors. To make the task more manageable, I narrowed the scope to just the main application file.

```sh
uv run pyrefly check main.py
```

This reduced the list to 11 errors, giving me a focused starting point.

### Debugging a Type Error

I decided to tackle one of the reported errors. `pyrefly` pointed out an issue with the `get_post` function. Here's the pyrefly output

```sh
ERROR Type `None` is not iterable [not-iterable]
   --> main.py:258:9
    |
258 |         content, metadata = get_post(slug)
    |         ^^^^^^^^^^^^^^^^^
    |
```

The function's type hint declared that it returns a `tuple` or `None`.

```python
# The incorrect type hint
def get_post(...) -> tuple | None:
    # ... function implementation
```

However, after reviewing the code, I saw that the function never actually returns `None`. If a post is not found, it raises a `ContentNotFound` exception. The type hint was wrong.

```python
def get_post(slug: str) -> tuple | None:
    posts = list_posts(content=True)
    post = next((x for x in posts if x["slug"] == slug), None)
    if post is None:
        raise ContentNotFound
    return (post["content"], post)
```

### Verifying the Fix

I corrected the type hint by removing the incorrect `| None` part.

```python
# The corrected type hint
def get_post(...) -> tuple:
    # ... function implementation
```

After saving the change, I re-ran the check on `main.py`.

```sh
uv run pyrefly check main.py
```

The error count dropped from 11 to 10. The fix was successful. You can [see the commit where the work was done on the repo](https://github.com/pydanny/daniel.feldroy.com/commit/343eff8d1d286818a611e418c9fdeac7ae8b9fc9).

### Conclusion

Adding a type checker like `pyrefly` immediately exposed incorrect type hints in the codebase. The process of installing the tool, running a check, and fixing the first error was straightforward. This small change improved the code's correctness and demonstrated the value of static analysis for maintaining a healthy project.

As for the rest of the errors, rather than attack them in one big effort as this is a stable side project what I like to do is make it a daily chore to do a single correction per day. This is slower (and could be done quickly with an LLM assist) but through practice I get better with the tool. Mastery is found through repetition.