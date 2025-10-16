---
title: Code
---

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates("templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def index(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )
```


```python
import air

app = air.App()
app.mount("/static", StaticFiles(directory="static"), name="static")
jinja = air.JinjaRenderer("templates")


@app.get("/items/{id}")
async def index(request: Request, id: str):
    return render(request=request, name="item.html", id=id)
```

```python
import air
from fastapi import FastAPI

app = air.Air()
api = FastAPI()

# Air's JinjaRenderer is a shortcut for using Jinja templates
jinja = air.JinjaRenderer(directory="templates")

@app.get("/")
def index(request: Request):
    return jinja(request, name="home.html")

@api.get("/")
def api_root():
    return {"message": "Awesome SaaS is powered by FastAPI"}

# Combining the Air and and FastAPI apps into one
app.mount("/api", api)    
```

```python
@app.post('contact-form')
def contact_form(request: air.Request):
    form = await request.body()
    # Do something with the form data
    return air.Article(
        P("We'll get back to you soon!"),
        class_="contact-form",
        id='contact-form',
        hx_swap='outerHTML
    )
```