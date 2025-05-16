from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class GetItemDto(BaseModel):
  id: UUID
  name: str
  description: str
  price: int
  created_at: datetime