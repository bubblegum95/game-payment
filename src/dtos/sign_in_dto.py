from pydantic import BaseModel, Field

class SignInDto(BaseModel): 
  email: str
  password: str