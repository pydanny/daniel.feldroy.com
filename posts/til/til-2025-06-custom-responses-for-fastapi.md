---
date: '2025-06-12T11:07:07.890416'
description: How to create new and exciting responses for FastAPI.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: false
tags:
- FastAPI
- Python
- Starlette
- TIL
title: 'TIL: Custom Responses for FastAPI'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

FastAPI provides a lot of built-in functionality for handling responses. However, sometimes you might want to create custom responses that go beyond the standard JSON or HTML responses. In this TIL, I'll show what I've learned about creating custom responses in FastAPI.

I do want to mention that FastAPI provides some documentation on this topic, but there are nuances to it worth exploring. You can find the official documentation [here](https://fastapi.tiangolo.com/advanced/custom-response/).

## Basics

```python
from typing import Any

import json
from fastapi import FastAPI, Response

app = FastAPI()

class AwesomeJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return json.dumps({"awesome": content})


@app.get("/", response_class=AwesomeJSONResponse)
async def main():
    return {"message": "Hello World"}
```

This will return a response with the content below and the media type set to `application/json`.

```json
{"awesome": {"message": "Hello World"}}
```

## Customizing Return Objects

What if you want to return instantiated objects instead of dictionaries? Where the attributes of the object are serialized to JSON? So you can have a design like this:

```python
class MyObject:
    def __init__(self, message: str):
        self.message = message

    def to_dict(self):
        return {"message": self.message}
```

@app.get("/", response_class=AwesomeObjResponse)
async def main():
    return MyObject("Hello World")
```