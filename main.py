from fastapi import FastAPI
from controllers.items import items

app = FastAPI() 

app.include_router(items)

@app.get("/")
def read_root():
  return {"Hello": "World"}

