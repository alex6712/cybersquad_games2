from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.dependencies import validate_access_token
from app.models import APIUserModel
from app.models.responses import StandardResponse

router = APIRouter(
    prefix="/blackjack",
    tags=["blackjack"],
)


@router.post("/join", status_code=status.HTTP_200_OK, response_model=StandardResponse)
def blackjack(user: Annotated[APIUserModel, Depends(validate_access_token)]):
    return {"message": f"User {user.username} successfully joined room."}
