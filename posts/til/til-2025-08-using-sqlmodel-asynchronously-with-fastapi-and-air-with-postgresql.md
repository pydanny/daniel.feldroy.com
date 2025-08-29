---
date: '2025-08-29T05:54:58.034855+00:00'
description: SQLModel is a really useful library for working with SQL databases in Python, built on top of SQLAlchemy and Pydantic. However, AFAIK there's no documentation supporting asynchronous operations for PostgreSQL, which can be a limitation when building high-performance web applications with FastAPI and Air.
image: /public/logos/til-1.png
published: true
tags:
- air
- fastapi
- python
- TIL
title: 'TIL: Using SQLModel Asynchronously with FastAPI (and Air) with PostgreSQL'
twitter_image: /public/logos/til-1.png
---

First, let's set up our environment. We'll need to install the necessary packages:

```bash
uv venv
uv add "FastAPI[standard]" SQLModel asyncpg psycopg2-binary greenlet
```

A quick quick guide to these dependencies:

- **FastAPI**: The web framework we'll be using. We install with the [standard] extras to make running in the shell easy
- **SQLModel**: The ORM for interacting with our SQL database
- **psycopg2-binary**: A PostgreSQL adapter for Python, which will be used by SQLModel for synchronous operations
- **asyncpg**: An asynchronous PostgreSQL client library, which will be used by SQLModel for async operations
- **greenlet**: A dependency for SQLAlchemy, which powers SQLModel, to support asynchronous operations.

Yes, we need BOTH synchronous and asynchronous PostgreSQL drivers. SQLModel (and SQLAlchemy) use the synchronous driver for certain operations, even when we are mostly working in an async context.

## FastAPI

Here we'll set up a simple FastAPI application that uses SQLModel asynchronously (and synchronously).  As far as I can tell, to create tables we need to use a synchronous engine, which explains the need for both drivers and engines. Specifically we'll create (synchronously) a `Story` model and two asynchronous endpoints: one for retrieving stories and another for creating a new story.

When creating my example database, I used 'drg' as my username and called the database 'my-database'. Adjust the connection strings as needed for your setup.

```bash

```python
# main.py
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, select, Field, create_engine
from typing import AsyncGenerator


# Step 0: sync engine for non-web db actions like creating tables
sync_engine = create_engine("postgresql://username@localhost/my-database", echo=True)


# Step 1: Create async engine and session
async_engine = create_async_engine(
    "postgresql+asyncpg://username@localhost/my-database",  # Async connection string
    echo=True,  # Optional: Set to False in production
    future=True,
)

# Step 2: Set up async session
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Step 3: Create a dependency to yield an async session
async def _get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# Wrap _get_async_session with Depends for FastAPI to keep type checking happy
get_async_session = Depends(_get_async_session)

# Define a SQL model table
class Story(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    slug: str

# Create tables (synchronously, outside of request handling)
SQLModel.metadata.create_all(sync_engine)


# Step 4: Create FastAPI app and endpoints
app = FastAPI()


@app.get("/")
async def index(session: AsyncSession = get_async_session):
    stmt = select(Story)
    stories = await session.exec(stmt)
    return {"stories": [x.slug for x in stories]}


@app.post("/{slug}")
async def create_story(slug: str, session: AsyncSession = get_async_session):
    story = Story(slug=slug)
    session.add(story)  # Don't commit standard db actions
    await session.commit()  # Always await commits
    return {"slug": story.slug}
```

Start it up with:

```bash
fastapi dev main.py
```

Go to the API docs and try it out: [http://localhost:8000/docs](http://localhost:8000/docs)

## Air

[Air](https://airdocs.fastapicloud.dev/) is a FastAPI-based framework for building HTML-focused web applications. It builds on top of FastAPI and adds features like easier templating, improved form handling, and more. You can combine it with FastAPI routes and SQLModel to create the web pages for your API application.

In any case, except for single import change, as well as defining the app and endpoints, the code is identical to the FastAPI example above. The main difference is that instead of returning JSON responses, we return HTML using Air's components and layouts. Air can return Jinja-powered responses, web but here we'll use Air's built-in components for simplicity.

First let's set up our environment. We'll need to install the necessary packages:

```bash
uv venv
uv add "Air[standard]" SQLModel asyncpg psycopg2-binary greenlet
```

- **Air**: The FastAPI-powered web framework we'll be using. We install with the [standard] extras to make running in the shell easy
- **SQLModel**: The ORM for interacting with our SQL database
- **psycopg2-binary**: A PostgreSQL adapter for Python, which will be used by SQLModel for synchronous operations
- **asyncpg**: An asynchronous PostgreSQL client library, which will be used by SQLModel for async operations
- **greenlet**: A dependency for SQLAlchemy, which powers SQLModel, to support asynchronous operations.

Now for the code. When creating my example database, I used 'drg' as my username and called the database 'my-database'. Adjust the connection strings as needed for your setup.

```python
# main.py
import air  # air is built on FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, select, Field, create_engine
from typing import AsyncGenerator


# Step 0: sync engine for non-web db action
sync_engine = create_engine("postgresql://username@localhost/my-database", echo=True)


# Step 1: Create async engine and session
async_engine = create_async_engine(
    "postgresql+asyncpg://username@localhost/my-database",  # Async connection string
    echo=True,  # Optional: Set to False in production
    future=True,
)

# Step 2: Set up async session
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Step 3: Create a dependency to yield an async session
async def _get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


get_async_session = Depends(_get_async_session)


class Story(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    slug: str


SQLModel.metadata.create_all(sync_engine)

# After this comment, the project diverges from the FastAPI example

# Step 4: Create FastAPI app and endpoints
app = air.Air()


@app.page
async def index(session: AsyncSession = get_async_session):
    stmt = select(Story)
    stories = await session.exec(stmt)
    return air.layouts.mvpcss(
        air.Article(
            air.Ol(*[air.Li(x.slug) for x in stories])
        )
    )


@app.get("/{slug}")
async def create_story(slug: str, session: AsyncSession = get_async_session):
    "Note: This is a GET endpoint for simplicity; in a real app, use POST for creating resources."
    story = Story(slug=slug)
    session.add(story)  # Don't commit standard db actions
    await session.commit()  # Always await commits
    return air.layouts.mvpcss(
        air.H1(story.slug),
        air.P("Story created! ", air.A("Go back", href="/"))
    )

```

Start it up with:

```bash
fastapi dev main.py
```

Try it out:

- [http://localhost:8000/first-article](http://localhost:8000/first-article) - Just clicking this will create a new article with the slug "first-article". In a real app, you'd want to use a POST request for creating resources, but this is just for demonstration.
- [http://localhost:8000/second-article](http://localhost:8000/second-article) - Create a second article.
- [http://localhost:8000](http://localhost:8000) - View the list of articles.
