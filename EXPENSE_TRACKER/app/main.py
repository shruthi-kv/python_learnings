from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from app.core.db import Base, engine
import app.models.expense
import app.models.user


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {
        "message" : "hello from root",
        "status" :200
    }