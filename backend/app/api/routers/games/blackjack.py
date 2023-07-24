from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.api.dependencies import validate_access_token
from app.api.schemas import UserSchema
from app.api.schemas.responses import StandardResponse

router = APIRouter(
    prefix="/blackjack",
    tags=["blackjack"],
)


@router.get(
    "/state",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Получение состояния игры для пользователя.",
)
def blackjack(user: Annotated[UserSchema, Depends(validate_access_token)]):
    return {"message": f"There's current game state for {user.username}."}
