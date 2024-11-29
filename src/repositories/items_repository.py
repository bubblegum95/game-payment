from src.models.item_model import Item
from src.dtos.create_item_dto import CreateItemDto
from src.dtos.get_item_dto import GetItemDto

class ItemRepository:
  def __init__(self, repository=Item):
    self.repository = repository

  async def create(self, dto: CreateItemDto):
    try:
      return await self.repository.create(name=dto.name, description=dto.description, price=dto.price)
    except Exception as error:
      raise error
  
  async def find_items(self, page: int, limit: int):
    skip = (page - 1) * limit
    items = await self.repository.all().offset(skip).limit(limit).values()
    item_list = list(items)
    return item_list
  
  async def get_item(self, item_id: str):
    return await self.repository.get(id=item_id).values()