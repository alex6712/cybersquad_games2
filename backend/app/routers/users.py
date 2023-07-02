from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import settings
from app.dependencies import get_current_user
from app.models import APIUserModel
from app.services import user_service
from database.session import get_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", status_code=200, response_model=APIUserModel)
async def me(user: Annotated[APIUserModel, Depends(get_current_user)]):
    return user


@router.get("/{username}")
async def person(
        username: str,
        user: Annotated[APIUserModel, Depends(get_current_user)],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    if user.username == username:
        return RedirectResponse(f"http://{settings.DOMAIN}:{settings.BACKEND_PORT}/users/me")

    return await user_service.get_user_by_username(session, username)
