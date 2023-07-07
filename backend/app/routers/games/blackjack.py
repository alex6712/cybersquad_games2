from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)

from app.models import APIUserModel
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/blackjack",
    tags=["blackjack"],
)
