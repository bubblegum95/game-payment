from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from app.api.item import items
from app.api.user import users
from starlette.config import Config
from tortoise import Tortoise


config = Config('.env')

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await Tortoise.init(
            db_url=config("DB_URL"),
            modules={"models": ["app.models.user_model", "app.models.pay_model"]},
        )
        await Tortoise.generate_schemas()
        logging.info("DB initialized successfully")
        print("DB initialized successfully.")
        yield  # 서버가 이 시점에서 실행됨
    finally:
        await Tortoise.close_connections()
        print("DB shutdown complete.")

app = FastAPI(lifespan=lifespan)

# 라우터 등록
app.include_router(items)
app.include_router(users)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# 로그 설정
logging.basicConfig(level=logging.INFO)
