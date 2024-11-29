from src.repositories.items_repository import ItemRepository
from src.dtos.create_item_dto import CreateItemDto

class ItemService:
  def __init__(self, repository: ItemRepository):
    self.repository = repository

  async def create_item(self, dto: CreateItemDto):
    return await self.repository.create(dto)
  
  async def get_items(self, page: int, limit: int):
    try:
      items = await self.repository.find_items(page, limit)
      return items
    
    except Exception as error:
      raise error
  
  async def get_item(self, item_id: str):
    try: 
      item = await self.repository.get_item(item_id)
      return item
    
    except Exception as error:
      raise error