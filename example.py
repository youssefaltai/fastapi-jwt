from fastapi import Depends, APIRouter

from auth.auth_bearer import JWTBearer
from auth.auth_handler import sign_jwt

router = APIRouter(prefix="/example", tags=["JWT example"])


@router.post("/")
async def create_token(username: str):
    return sign_jwt({"username": username})


@router.get("/", dependencies=[Depends(JWTBearer())])
async def get_secret():
    return {"secret": "im potato"}
