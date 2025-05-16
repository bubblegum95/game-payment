from fastapi import HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from app.services.items_service import ItemService
from app.repositories.item_repository import ItemRepository
from app.schemas.create_item_dto import CreateItemDto
from app.schemas.get_item_dto import GetItemDto

items = APIRouter(
  prefix="/items",
  tags = ["items"],
  responses = {404: {"description": "Not Found"}},
)

def get_item_service():
  repository = ItemRepository()
  return ItemService(repository)

@items.post("/")
async def create_items(dto: CreateItemDto, service: ItemService = Depends(get_item_service)):
  try:
    item = await service.create_item(dto)
    if not item:
      raise Exception('아이템 생성 실패')
    
    return JSONResponse(
      content={"message" : "아이템 등록을 완료하였습니다."},
      status_code=201
    )
  except Exception as error:
    print(error)
    raise HTTPException(
      status_code=400,
      detail={"error": {str(error)}}
    )

@items.get("/")
async def get_items(page: int, limit: int, service: ItemService = Depends(get_item_service)):
  try:
    if limit < 10 or limit > 51:
      raise Exception("한 번에 가져올 수 있는 아이템 개수는 10~50 입니다.")
    items = await service.get_items(page, limit)
    print(items)
    return [GetItemDto(**item) for item in items]
  
  except Exception as error:
    print(error)
    raise HTTPException(
      status_code=400,
      detail={"error": str(error)}
    )
  
@items.get("/{item_id}")
async def read_items(item_id: str, service: ItemService = Depends(get_item_service)):
  try:
    item = await service.get_item(item_id)
    return GetItemDto(**item)
  
  except Exception as error:
    raise HTTPException(
      status_code=400,
      detail={"error": error}
    )