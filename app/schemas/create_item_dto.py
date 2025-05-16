from pydantic import BaseModel

class CreateItemDto(BaseModel):
  name: str
  description: str
  price: int
  