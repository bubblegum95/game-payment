from fastapi import APIRouter
from typing import Union

items = APIRouter(
  prefix="/items",
  tags = ["items"],
  responses = {404: {"description": "Not Found"}},
)

# @items.get("/{item_id}")
# def read_items(item_id: int, q: Union[str, None] = None):
#   return {"item id": item_id, "q": q}