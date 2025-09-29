---
date: '2025-09-28T22:44:18.296914+00:00'
description: Replacing python-dotenv with uv
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Loading .env files with uv run'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

We don't need python-dotenv, use `uv run` with `--env-file`, and your env vars from `.env` get loaded. 

For example, if we've got a FastAPI or Air project we can run it locally with env vars like:

```sh
uv run --env-file .env fastapi dev
```

You can specific different env files for different environments, like `.env.dev`, `.env.prod`, etc.

```sh
uv run --env-file .env.dev fastapi dev
```

All credit goes to [Audrey Roy Greenfeld](https://audrey.feldroy.com) for [pointing this out](https://x.com/audreyfeldroy/status/1964565105599009078).