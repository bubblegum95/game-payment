from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from services.users_service import UserService
from src.dtos.sign_up_dto import SignUpDto
from src.repositories.users_repository import UserRepository
from src.dtos.sign_in_dto import SignInDto

def get_user_repository():
  repository = UserRepository()  
  return UserService(repository) 


users = APIRouter(
  prefix= "/users", 
  tags=["users"], 
  responses={404: {"description": "Not Found"}}
)

@users.get("/")
def read_users():
  return {"hello": "world"}

@users.post("/sign-up")
async def sign_up(dto: SignUpDto, service: UserService = Depends(get_user_repository)):
  try:
    user_acnt = await service.sign_up(dto)

    if user_acnt:
      return JSONResponse(
        content={"message": "계정 생성을 완료하였습니다. 로그인 해주세요."},
        status_code=201
      )
  except Exception as error:
    raise HTTPException(
      status_code=400, 
      detail=f"Sign-up failed: {str(error)}"
    )

@users.post("/sign-in")
async def sign_in(res: Response ,dto: SignInDto, service: UserService = Depends(get_user_repository)):
  try: 
    token = await service.sign_in(dto)
    res.set_cookie("authorization", f"Bearer {token}", secure=True, httponly=True, samesite=None)
    return JSONResponse(
      content={"message": "로그인 성공"}, status_code=200
    )
  except Exception as error: 
    raise HTTPException(
      status_code=400, 
      detail=f"Sign-up failed: {str(error)}"
    )