from pydantic import BaseModel, Field

class SignUpDto(BaseModel):
  name: str
  username: str
  email: str
  password: str
  phone: str

# class SignUpDto(BaseModel):
#     name: str = Field(min_length=1, max_length=50, description="User's full name")
#     username: str = Field(min_length=3, max_length=20, description="Unique username")
#     email: str = Field(regex=r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", description="Valid email address")
#     password: str = Field(min_length=8, description="Secure password")
#     phone: str = Field(regex=r"^\d{10,15}$", description="Phone number with 10-15 digits")
