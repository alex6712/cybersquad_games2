from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)

from app.models import APIUserModel
from app.dependencies import validate_access_token

router = APIRouter(
    prefix="/blackjack",
    tags=["blackjack"],
)


@router.get("/join")
def blackjack(user: Annotated[APIUserModel, Depends(validate_access_token)]):
    pass
