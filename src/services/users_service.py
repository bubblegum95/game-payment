import logging
import bcrypt
from src.dtos.sign_up_dto import SignUpDto
from src.repositories.users_repository import UserRepository

class UserService:
  def __init__(self, repository = UserRepository):
    self.repository = repository

  async def exist_email(self, email: str):
    print(email)
    return await self.repository.exist_email(email)

  async def exist_phone(self, phone: str):
    print(phone)
    return await self.repository.exist_phone(phone)
  
  async def create_acnt(self, dto: dict):
    return await self.repository.create(dto)
    
  async def create(self, dto: SignUpDto):
    try:
      print(dto) # 여기서 출력이 안됨
      exist_email = await self.exist_email(dto.email)
      if exist_email == True:
        raise Exception('해당 이메일은 사용할 수 없습니다.')
      
      exist_phone = await self.exist_phone(dto.phone)
      if exist_phone == True:
        raise Exception('해당 휴대전화번호는 사용할 수 없습니다.')
      
      hashed_password = bcrypt.hashpw(dto.password.encode(), bcrypt.gensalt())
      print("hashed password:", hashed_password)

      new_dto = dict(
        name=dto.name,
        username=dto.username,
        email=dto.email,
        password=hashed_password,
        phone=dto.phone
      )

      await self.create_acnt(new_dto)
      return True
    except Exception as error:
      logging.error(error)
      raise error