---
date: '2025-10-22T13:00:56.868382+00:00'
description: In the old days we relied on tox and nox to test a Python project against multiple Python versions, now we can lean on uv+just. For most projects this keeps our configuration straightforward and reduces dependencies.
published: true
tags:
- python
- uv
- howto
title: 'uv+just for testing multiple Python versions'
---

For years I used tox and nox to test my Python projects against multiple Python versions on multiple operating systems. While both tools are powerful, they require configuration complex enough that I usually just copy/paste it from project to project. In comparison, `uv+just` isn't just a completely workable replacement, it's simple enough that I can either memorize the commands or if I forget can look up in moments.

## What is Just?

[Just](https://github.com/casey/just) is a rust-powered command runner inspired by [Make](https://en.wikipedia.org/wiki/Make_(software)) but with a slightly simpler syntax. Where Make was originally designed to build executable code, just focuses more on being a command-runner. Also, `Just` benefits from the lessons learned by Make. The result is an easier-to-use tool that is also much easier to get running on Windows than `Make`. The way `Just` works is you define commands in a `Justfile` that can be easily executed from the command line. It can be installed from pypi as the [rust-just](https://pypi.org/project/rust-just/) package.

## Assumptions about our project

1. Uses `pytest` for testing
2. Has a `tests/` directory containing the test cases
3. Supposed to work with both Python 3.13 and 3.14

## Installing dependencies using pyproject.toml

Make sure to include the necessary dependencies in your `pyproject.toml` file:

```toml
[dependency-groups]
dev = [
    "rust-just"
]

test = [
    "pytest",
]
```

Once in your `pyproject.toml` get your development dependencies ready with this command:

```bash
uv sync --group dev
```

## Building the Justfile

Justfiles are simple to write. Create a file named `Justfile` in the root of your project with the following content:


```Makefile
# Run all the tests against multiple Python versions
test:
    uv run --python 3.13 --group test pytest tests/
    uv run --python 3.14 --group test pytest tests/
```

If you have more Python versions to test against, simply add more `uv run` lines with the desired version. 

## Running the tests

```bash
just test
```

And that's it! You now have a simple and effective way to test your Python projects against multiple Python versions using `uv` and `just`, without the overhead of more complex tools like `tox` or `nox`. This setup is easy to maintain and adapt as your project evolves.

## Just bonus feature: command lookup

A nice feature about `just` is you can trivially look up the commands you've authored with `just -l`, and leading docstrings are included in the display:

```bash
$ just -l
Available recipes:
    test # Run all the tests against multiple Python versions
```

If you don't specify a command, `just` will run the first one it finds in the file. This means you can set up a default command to run when you just type `just` with no arguments. What I like to do is put a `list` action as the first command. By that I mean something like this:

```Makefile
# List all the commands in this file
list:
    just -l

# Run all the tests against multiple Python versions
test:
    uv run --python 3.13 --group test pytest tests/
    uv run --python 3.14 --group test pytest tests/
```