from app.repositories.item_repository import ItemRepository
from app.schemas.create_item_dto import CreateItemDto

class ItemService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, repository: ItemRepository):
    if not hasattr(self, 'initialized'):
      self.repository = repository
      self.initialized = True

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