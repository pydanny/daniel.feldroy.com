from typing import AsyncGenerator
from datetime import datetime

from os import getenv

import air  # air is built on FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, select, Field, create_engine
from enum import Enum, StrEnum
import pydantic


# Step 0: sync engine for non-web db action
sync_url = "postgresql://" + getenv('DANIEL_DB_URL', 'drg@localhost/danielblog')
sync_engine = create_engine(sync_url, echo=True)


# Step 1: Create async engine and session
async_url = "postgresql+asyncpg://" + getenv('DANIEL_DB_URL', 'drg@localhost/danielblog')
async_engine = create_async_engine(
    async_url, # Async connection string
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

class StatusEnum(StrEnum):
    unconfirmed = 'Unconfirmed'
    subscribed = 'Subscribed'
    unsubscribed = 'Unsubscribed'
    on_hold = 'On Hold'

class Subscription(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: pydantic.EmailStr = Field(unique=True)
    status: StatusEnum = StatusEnum.unconfirmed
    attempts_to_subscribe: int = 1 # How many attempts to subscribe. If we get more than 3 for an email we put them on hold
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


