from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.models import UserModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me")
async def me(user: Annotated[UserModel, Depends(get_current_user)]):
    return user
