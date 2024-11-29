from src.models.item_model import Item
from src.dtos.create_item_dto import CreateItemDto

class ItemRepository:
  def __init__(self, repository=Item):
    self.repository = repository

  async def create(self, dto: CreateItemDto):
    return await self.repository.create(**dto.model_dump())
  
  async def find_items(self, page: int, limit: int):
    skip = (page - 1) * limit
    items = await self.repository.all().offset(skip).limit(limit).values()
    return list(items)
  
  async def get_item(self, item_id: str):
    return await self.repository.get(id=item_id).values()