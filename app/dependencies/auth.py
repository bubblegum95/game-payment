from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.token_service import TokenService
from starlette.status import HTTP_401_UNAUTHORIZED


token_service = TokenService()
bearer_scheme = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
  token = credentials.credentials
  user_id = await token_service.verify_token(token)

  if user_id is None:
    raise HTTPException(
      status_code=HTTP_401_UNAUTHORIZED,
      detail="Invalid or expired token",
      headers={"WWW-Authenticate": "Bearer"},
    )
  return user_id