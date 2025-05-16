import logging
import traceback
import bcrypt
from app.models.user_model import User
from app.schemas.sign_up_dto import SignUpDto
from app.schemas.sign_in_dto import SignInDto
from app.services.token_service import TokenService
from app.repositories.user_repository import UserRepository

import uuid

class UserService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, repository: UserRepository | None = None, token_service: TokenService | None = None):
    if not hasattr(self, "initialized"):
      self.repository = repository or UserRepository()
      self.token_service = token_service or TokenService()
      self.initialized = True

  async def exist_email(self, email: str) -> bool:
    return await self.repository.exist_email(email)

  async def exist_phone(self, phone: str):
    return await self.repository.exist_phone(phone)
  
  async def create_acnt(self, dto: dict):
    return await self.repository.create(dto)
  
  async def find_user(self, email: str) -> User | None:
    return await self.repository.find(email)

  async def update_token(self, id: uuid.UUID, token: str) -> int:
    return await self.repository.update_token(id, token)
  
  async def sign_up(self, dto: SignUpDto):
    try:
      exist_email = await self.exist_email(dto.email)
      if exist_email == True:
        raise Exception('해당 이메일은 사용할 수 없습니다.')
      
      exist_phone = await self.exist_phone(dto.phone)
      if exist_phone == True:
        raise Exception('해당 휴대전화번호는 사용할 수 없습니다.')
      
      hashed_password = bcrypt.hashpw(dto.password.encode('utf-8'), bcrypt.gensalt())
      new_dto = dict(
        name=dto.name,
        username=dto.username,
        email=dto.email,
        password=hashed_password.decode(),
        phone=dto.phone
      )

      await self.create_acnt(new_dto)
      return True
    
    except Exception as error:
      logging.error(traceback.format_exc())
      raise error
    
  async def sign_in(self, dto: SignInDto):
    try:
      exist_user = await self.find_user(dto.email)
      if exist_user is None:
        raise Exception("해당 계정이 존재하지 않습니다.")
      
      is_correct = bcrypt.checkpw(dto.password.encode(), exist_user.password.encode())
      if not is_correct:
        raise Exception("비밀번호가 일치하지 않습니다.")
      
      refresh_token = await self.token_service.create_token(user_id=exist_user.id, refresh=False)
      updated = await self.update_token(id=exist_user.id, token=refresh_token)
      if updated != 1:
        raise Exception("토큰을 업데이트 할 수 없습니다.")
      
      access_token = await self.token_service.create_token(user_id=exist_user.id, refresh=True)
      return access_token

    except Exception as error:
      logging.error(traceback.format_exc())
      raise error