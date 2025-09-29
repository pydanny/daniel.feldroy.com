---
date: '2025-09-02T02:29:33.084710+00:00'
description: An easier way of doing it then modifying os.environ
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- python
- TIL
- testing
title: 'TIL: Setting environment variables for pytest'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

When writing tests in pytest, often there's a need to set environment variables for your tests. Instead of modifying `os.environ` directly, which can lead to side effects and make tests harder to manage, here's how to do it with the [pytest-env](https://pypi.org/project/pytest-env/) package.

First, install the package. 

```sh
pip install pytest-env # classic but works great
uv add pytest-env # if you're one of us cool kids using uv
uv add pytest-env --group test # if you use a specific test group of dependencies
```

A lot of people use `pytest.ini` to configure pytest, but I prefer using `pyproject.toml` for a more modern approach. Here's how you can set environment variables in `pyproject.toml`:

```toml
[tool.pytest_env]
# Test value for the SUPER_SECRET_KEY environment variable
SUPER_SECRET_KEY = "ABC123"
```

Then run your tests just like you would normally do, and now the environment variable will be picked up by whatever test or code is looking for it. That's correct, you don't need to do any further configuration.

```sh
pytest .
```
  
Since a lot of API SDK libraries use environment variables for configuration, this is a great way to ensure your tests run in a controlled environment. Either with mock replies or against a test instance of the service.