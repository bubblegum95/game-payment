from pydantic import BaseModel, Field, EmailStr

class SignUpDto(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=10,
        description="이름 (2~10자)",
        example="홍길동"
    )
    username: str = Field(
        ...,
        min_length=2,
        max_length=20,
        description="닉네임 (2~8자)",
        example="길동이"
    )
    email: EmailStr = Field(
        ...,
        description="이메일 주소",
        example="user@email.com"
    )
    password: str = Field(
        ...,
        min_length=8,
        description="비밀번호는 최소 8자 이상이어야 합니다",
        example="Example123!"
    )
    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{1,14}$",
        description="전화번호는 국제 표준 형식이어야 합니다 (예: +821012345678)",
        example="+821012345678"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "name": "홍길동",
                "username": "gildong123",
                "email": "gildong@example.com",
                "password": "securepassword123",
                "phone": "+821012345678"
            }
        }
