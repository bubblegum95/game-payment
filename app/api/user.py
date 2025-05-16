from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from app.dependencies.auth import get_current_user
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.schemas.sign_in_dto import SignInDto
from app.schemas.sign_up_dto import SignUpDto
from app.services.token_service import TokenService
from typing import Annotated


users = APIRouter(
  prefix= "/users", 
  tags=["users"], 
  responses={404: {"description": "Not Found"}}
)

def get_user_service() -> UserService:
  repository = UserRepository()
  token_service = TokenService()
  service = UserService(repository, token_service)
  return service

def get_token_service() -> TokenService:
  token_service = TokenService()
  return token_service

@users.get("/")
def read_users():
  return {"hello": "world"}

@users.post("/sign-up")
async def sign_up(dto: SignUpDto, service: UserService = Depends(get_user_service)):
  try:
    print("dto", dto)
    user_acnt = await service.sign_up(dto)

    if user_acnt:
      return JSONResponse(
        content={"message": "계정 생성을 완료하였습니다. 로그인 해주세요."},
        status_code=201
      )
    
  except Exception as error:
    raise HTTPException(
      status_code=400, 
      detail=f"error: {str(error)}"
    )

@users.post("/sign-in")
async def sign_in(res: Response ,dto: SignInDto, service: UserService = Depends(get_user_service)):
  try: 
    token = await service.sign_in(dto)
    return JSONResponse(
      content={"message": "로그인 성공", "authorization": f"Bearer {token}"}, 
      status_code=200
    )
  except Exception as error: 
    raise HTTPException(
      status_code=400, 
      detail=f"error: {str(error)}"
    )
  
@users.get("/user_id/")
async def read_items(user_id: str = Depends(get_current_user)):
    return {"user_id": user_id}