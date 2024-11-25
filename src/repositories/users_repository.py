from src.models.user_model import User
from src.dtos.sign_up_dto import SignUpDto

class UserRepository:
  def __init__(self, repository=User):
    self.repository = repository

  async def exist_email(self, email: str) -> bool:
    exist_user = await self.repository.filter(email=email).exists()
    return exist_user

  async def exist_phone(self, phone: str) -> bool:
    exist_phone = await self.repository.filter(phone=phone).exists()
    return exist_phone

  async def create(self, dto: dict):
    return await self.repository.create(**dto)