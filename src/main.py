from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from controllers.item_controller import items
from src.controllers.user_controller import users
from starlette.config import Config
from tortoise import Tortoise

config=Config('.env')

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url=config("DB_URL"),
        modules={"models": ["src.models.user_model", "src.models.item_model"]},
    )
    await Tortoise.generate_schemas()
    print("DB initialized successfully.")
    logging.info(msg="DB initialized successfully")
    yield  # 서버가 이 시점에서 실행됨

    print("DB shutdown complete.")
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

# 라우터 등록
app.include_router(items)
app.include_router(users)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# FastAPI startup 이벤트에서 Tortoise 초기화

