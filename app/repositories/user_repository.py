from app.models.user_model import User
import uuid

class UserRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, repository=User):
    if not hasattr(self, "initialized"):
      self.repository = repository
      self.initialized = True 

  async def exist_email(self, email: str) -> bool:
    exist_user = await self.repository.filter(email=email).exists()
    return exist_user

  async def exist_phone(self, phone: str) -> bool:
    exist_phone = await self.repository.filter(phone=phone).exists()
    return exist_phone

  async def create(self, dto: dict):
    return await self.repository.create(**dto)
  
  async def find(self, email: str) -> User | None:
    return await self.repository.filter(email=email).first()
  
  async def update_token(self, id: uuid.UUID, token: str) -> int:
    return await self.repository.filter(id=id).update(refresh_token=token)