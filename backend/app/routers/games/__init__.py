"""
Factory CRM API games routers

Модуль с описанием роутеров игр.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.dependencies import validate_access_token
from app.models import APIUserModel
from app.models.responses import StandardResponse
from .blackjack import router as _blackjack_router

router = APIRouter(
    prefix="/games",
)
router.include_router(_blackjack_router)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=StandardResponse, tags=["games"])
def create_room(user: Annotated[APIUserModel, Depends(validate_access_token)]):
    return {"code": status.HTTP_201_CREATED, "message": "Room created successfully."}
