from fastapi import FastAPI

from src.database.configs import init_db
from src.users.router import router

app = FastAPI(
    description="This is a copy of the Telegram API's core features.",
    version="1.0")

app.include_router(router)


@app.get("/", tags=["root"])
async def root():
    return {"message": "This is a copy of the Telegram API's core features.", "version": "1.0"}


@app.on_event("startup")
async def startup():
    init_db()
