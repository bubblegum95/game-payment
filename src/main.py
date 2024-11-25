from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from src.controllers.items import items
from src.controllers.user_controller import users
from tortoise import Tortoise

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("App startup: Initializing DB")
    await Tortoise.init(
        db_url="postgres://bubblegum:postgres@localhost:5432/game",
        modules={"models": ["src.models.user_model"]},
    )
    yield  # 서버가 이 시점에서 실행됨
    logging.info("App shutdown: Closing DB")
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

# 라우터 등록
app.include_router(items)
app.include_router(users)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# FastAPI startup 이벤트에서 Tortoise 초기화

