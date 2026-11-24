from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from app.core.db import Base, engine
import app.models.expense
import app.models.user
from app.routers.expense import expense_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(expense_router)

@app.get("/")
def root():
    return {
        "message" : "hello from root",
        "status" :200
    }