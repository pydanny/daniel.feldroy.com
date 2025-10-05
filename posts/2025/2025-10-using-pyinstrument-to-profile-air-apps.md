---
date: '2025-10-05T08:00:13.982725+00:00'
description: Quick instructions for a drop-in Air middleware for identifying performance bottlenecks in Air apps
published: true
tags:
- python
- air
- howto
title: Using pyinstrument to profile Air apps
---

[Air](https://github.com/feldroy/air) is built on FastAPI, so we could use [pyinstrument's instructions](https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-web-request-in-fastapi) modified. However, because profilers reveal a LOT of internal data, in our example we actively use an environment variable.

You will need both `air` and `pyinstrument` to get this working:

```sh
# preferred
uv add "air[standard]" pyinstrument
# old school
pip install "air[standard]" pyinstrument
```

And here's how to use pyinstrument to find bottlenecks:


```python
import asyncio
from os import getenv
import air
from pyinstrument import Profiler

app = air.Air()

# Use an environment variable to control if we are profiling
# This is a value that should never be set in production
if getenv("PROFILING"):
    @app.middleware("http")
    async def profile_request(request: air.Request, call_next):
        profiling = request.query_params.get("profile", False)
        if profiling:
            profiler = Profiler()
            profiler.start()
            await call_next(request)
            profiler.stop()
            return air.responses.HTMLResponse(profiler.output_html())
        else:
            return await call_next(request)


@app.page
async def index(pause: float = 0):
    if pause:
        await asyncio.sleep(pause)

    title = f"Pausing for {pause} seconds"
    return air.layouts.mvpcss(
        air.Title(title),
        air.H1(title),
        # Provide three options for testing the profiler
        air.P('Using asyncio.sleep to simulate bottlenecks'),
        air.Ol(
            air.Li(
                air.A(
                    f"Pause for 0.1 seconds",
                    href="/?profile=1&pause=0.1",
                    target="_blank",
                )
            ),
            air.Li(
                air.A(
                    f"Pause for 0.3 seconds",
                    href="/?profile=1&pause=0.3",
                    target="_blank",
                )
            ),
            air.Li(
                air.A(
                    f"Pause for 1.0 seconds",
                    href="/?profile=1&pause=1.0",
                    target="_blank",
                )
            ),
        ),
    )
```

## Running the test app:

Rather than set the environment variable, for this kind of thing I like to prefix the CLI command with a `PROFILING=1` prefix to send the environment variable for just this run of the project. By doing so we trigger `pyinstrument`:

```python
PROFILING=1 fastapi dev main.py
```

Once you have it running, check it out here: <http://localhost:8000>

## Screenshots

![](/public/images/pyinstrument-call-stack.png)

---

![](/public/images/pyinstrument-timeline.png)