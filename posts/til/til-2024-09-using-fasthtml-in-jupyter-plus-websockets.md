---
date: '2024-09-23T15:13:34.609190'
description: A simple websockets example hosted in a Jupyter notebook!
image: /public/logos/til-1.png
published: true
tags:
- TIL
- FastHTML
- python
- jupyter
title: 'TIL: Using FastHTML in Jupyter notebooks plus websockets'
twitter_image: /public/logos/til-1.png
---

# Websockets in Jupyter

A simple websockets example hosted in a Jupyter notebook! Check it out!

Use at least FastHTML 0.6.5. This code is heavily inspired by this [code](https://docs.fastht.ml/tutorials/by_example.html#websockets) written by Jeremy Howard.

```python {.marimo unparsable="true"}
# import necessary pieces
from fasthtml.common import *
from asyncio import sleep

# Might be merged into fasthtml.common
from fasthtml.jupyter import *
```

```python {.marimo}
def mk_inp(): return Input(id='msg')
```

```python {.marimo}
# FastJupy() is a wrapper around the FastHTML() class
# ws_hdr brings in the websocket headers
app = FastJupy(ws_hdr=True)
rt = app.route
```

```python {.marimo}
@rt('/')
async def get(request):
    cts = Div(
        Div(id='notifications'),
        Form(mk_inp(), id='form', ws_send=True),
        hx_ext='ws', ws_connect='/ws')
    return Titled('Websocket Test', cts)
```

```python {.marimo}
async def on_connect(send):
    print('Connected!')
    await send(Div('Hello, you have connected', id="notifications"))

async def on_disconnect(ws):
    print('Disconnected!')
```

```python {.marimo}
@app.ws('/ws', conn=on_connect, disconn=on_disconnect)
async def ws(msg:str, send):
    await send(Div('Hello ' + msg, id="notifications"))
    await sleep(2)
    return Div('Goodbye ' + msg, id="notifications"), mk_inp()
```

```python {.marimo}
port = 8000
server = JupyUvi(app, port=port)
```

```python {.marimo}
HTMX()
```

```python {.marimo}
# Run me if you want to gracefully stop the HTTP server
# without restarting Jupyter
server.stop()
```

```python {.marimo}
import marimo as mo
```