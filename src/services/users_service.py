import logging
import traceback
import bcrypt
import jwt
from src.dtos.sign_up_dto import SignUpDto
from src.repositories.users_repository import UserRepository
from src.dtos.sign_in_dto import SignInDto
from starlette.config import Config

class UserService:
  config = Config('.env')

  def __init__(self, repository = UserRepository):
    self.repository = repository

  async def exist_email(self, email: str):
    return await self.repository.exist_email(email)

  async def exist_phone(self, phone: str):
    return await self.repository.exist_phone(phone)
  
  async def create_acnt(self, dto: dict):
    return await self.repository.create(dto)
  
  async def find_user(self, email: str):
    return await self.repository.find(email)
  
  async def create_token(self, id: str):
    jwt_secret = self.config("JWT_SECRET")
    return jwt.encode({"id": str(id)}, jwt_secret, algorithm="HS256")
  
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
      
      return await self.create_token(exist_user.id)

    except Exception as error:
      logging.error(traceback.format_exc())
      raise error