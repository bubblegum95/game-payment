import logging
import traceback
from fastapi import APIRouter


payments = APIRouter(
  prefix= "/payments", 
  tags=["payments"], 
  responses={404: {"description": "Not Found"}}
)

@payments.post("/identity-verify")
async def identity_verify(dto):
  print(dto)
  try: 
    if not dto: 
      raise Exception("본인인증 정보가 정확하지 않습니다.")
  except Exception as error: 
    print(error)
    logging.error(traceback.format_exc())
    