from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from app.core.db import Base, engine, LocalSession
from app.core.security import hash_password
import app.models.expense
import app.models.user
from app.models.user import User
from app.routers.expense import expense_router
from app.routers.user import user_router

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine)

    db = LocalSession()
    try:
        users = db.query(User).all()
        for user in users:
            if not user.password.startswith("$argon2"):
                user.password = hash_password(user.password)
        db.commit()
    finally:
        db.close()

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(expense_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message" : "hello from root",
        "status" :200
    }