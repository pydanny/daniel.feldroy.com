---
date: '2025-10-19T05:07:02.438338+00:00'
description: "Asyncpg is the connector for PostgreSQL and asyncio-flavored Python. Here's how to use it without other libraries on FastAPI and Air projects."
published: true
tags:
- python
- fastapi
- air
- howto
title: Using Asyncpg with FastAPI and Air
---

Recently I've been on a few projects using PostgreSQL where SQLAlchemy and SQLModel felt like overkill. Instead of using those libraries I leaned on writing SQL queries and running those directly in [asyncpg](https://pypi.org/project/asyncpg/) instead of using an ORM powered by asyncpg. 

Here's how I got it to work

## Defined a lifespan function for ASGIApp

Starlette ASGIApp frameworks like FastAPI (and by extension [Air](https://github.com/feldroy/air)) can leverage lifespan functions, which are generators. I've commented the `lifespan` object for clarity. 

```python
from contextlib import asynccontextmanager
from os import environ
from typing import AsyncIterator

import asyncpg
from starlette.types import ASGIApp

DATABASE_URL = environ['DATABASE_URL']


@asynccontextmanager 
async def lifespan(app: ASGIApp) -> AsyncIterator[None]:
    """A lifespan for maintaining the connection to the PostgreSQL DB
        Without this, the connection will timeout and queries will fail.
    """
    # app.state is where the connection pool is created, which can
    # be accessed later inside of views. The is only run once during
    # app startup.
    app.state.pool = await asyncpg.create_pool(
        dsn=DATABASE_URL,
        min_size=1,
        max_size=10,
    )
    try:
        # This is where the app runs all the URL route functons.
        yield
    finally:
        # This is run once when the app is shut down.
        await app.state.pool.close()
```

## Using the lifespan function

Just add the `lifespan` function to the app when it is instantiated.

### Using the lifespan function for FastAPI projects

All you have to do is pass the `lifespan` callable to the FastAPI app instantiation.

```py
from fastapi import FastAPI

# Adding the lifespan app
app = FastAPI(lifespan=lifespan) 

@app.get('/users')
async def users(): # every function must be async
    # Use the pool object to get the database connection object
    async with app.state.pool.acquire() as conn:
        results = await conn.fetch('SELECT * from users;')

    # FastAPI responses automatically convert dicts to JSON
    return {'count': len(results), 'users': [results]}
```

### Using the lifespan function for Air projects

Air is powered by FastAPI (and Starlette), so uses this `lifespan` function the same way as FastAPI. 


```py
import air

# Adding the lifespan app
app = air.Air(lifespan=lifespan)


@app.get('/users')
async def users(): # every function must be async
    # Use the pool object to get the database connection object
    async with app.state.pool.acquire() as conn:
        users = await conn.fetch('SELECT * from users;')

    # Air tags are converted to HTML during the response stage
    # Jinja is also an option, but is outside the scope of this article
    return air.layouts.mvpcss(
        air.H1(f'Users: {len(users)}'),
        air.Ul(
            *[air.Li(u['email']) for u in users]
        )
    )
```

## Incoming data

Changing data requires use of the `conn.execute` function. Of course these examples will show how to use `pydantic` to validate the incoming data before we allow it to touch our database.

### Adding data with FastAPI via asyncpg

As part of the request process for REST API, FastAPI uses pydantic to validate incoming data. This results a delightfully small view for accepting data.

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# Adding the lifespan app
app = FastAPI(lifespan=lifespan) 


class User(BaseModel):
    email: EmailStr


@app.post('/users')
async def users_add(user: User):
    # Get the conn object from the database connection pool
    async with app.state.pool.acquire() as conn:
        # Insert the record with an execute method
        await conn.execute(
            'INSERT INTO users (email, created_at) VALUES ($1, NOW())',
            user.email
        )

    return user
```


### Adding data with Air via asyncpg

There's no consistent standard within HTML for how to construct a form, much less respond to a bad implementation. Therefore in order to handle incoming data Air needs a bit more code than FastAPI. 


```python
import air
from pydantic import BaseModel, EmailStr

# Adding the lifespan app
app = air.Air(lifespan=lifespan) 


class User(BaseModel):
    email: EmailStr


class UserForm(air.AirForm):
    model = User    


@app.post('/users')
async def users_add(request: air.Request):
    # AirForms make handling incoming forms easier
    form = await UserForm.from_request(request)
    
    # AirForms, once instantiated with data, have an `is_valid` property
    # which returns a boolean of whether or not the submitted data has
    # passed pydantic.
    if form.is_valid:
        # Get the conn object from the database connection pool
        async with app.state.pool.acquire() as conn:
            # Insert the record with an execute method
            await conn.execute(
                'INSERT INTO users (email, created_at) VALUES ($1, NOW())',
                form.data.email
            )
        return air.layouts.mvpcss(
            air.H1(f"User: {form.data.email}"),
        )        

    # Simplistic handling of bad signup. 
    return air.RedirectResponse('/signup')
```

AirForms supports reporting of bad data. I'll cover how to do that in follow-up article.