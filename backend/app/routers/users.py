from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import get_settings
from app.config import Settings
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
    """
    Метод личной страницы пользователя.

    Возвращает информацию о владельце токена.

    :param user: APIUserModel, пользователь получен из зависимости на авторизацию
    :return: APIUserModel, объект пользователя без пароля
    """
    return user


@router.get("/{username}", response_model=APIUserModel)
async def person(
        username: str,
        user: Annotated[APIUserModel, Depends(get_current_user)],
        session: Annotated[AsyncSession, Depends(get_session)],
        settings: Annotated[Settings, Depends(get_settings)],
):
    """
    Метод страницы пользователя.

    Если владелец токена посылает запрос на этот метод, то возвращается redirect на личную страницу. В ином
    случае возвращается страница запрашиваемого пользователя.

    :param username: str, логин пользователя, чья страница запрашивается
    :param user: APIUserModel, пользователь получен из зависимости на авторизацию
    :param session: AsyncSession, объект сессии запроса
    :param settings: Settings, настройки приложения
    :return: APIUserModel, объект пользователя без пароля
    """
    if user.username == username:
        return RedirectResponse(f"http://{settings.DOMAIN}:{settings.BACKEND_PORT}/users/me")

    return await user_service.get_user_by_username(session, username)
