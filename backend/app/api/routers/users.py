from typing import Annotated, AnyStr

from fastapi import (
    APIRouter,
    Depends,
    status,
    Path,
)
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import UserSchema
from app.api.schemas.responses import UserResponse
from app.api.services import user_service
from app.database.session import get_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK, summary="Личная страница.")
async def me(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """Метод личной страницы пользователя.

    Возвращает информацию о владельце токена.

    Parameters
    ----------
    user : UserSchema
        Пользователь получен из зависимости на авторизацию.

    Returns
    -------
    user : UserSchema
        Схема пользователя без пароля.
    """
    return user


@router.get(
    "/{username}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Страница пользователя с именем \"username\".",
)
async def person(
        username: Annotated[AnyStr, Path(title="Логин пользователя, на чью личную страницу необходимо перейти.")],
        user: Annotated[UserSchema, Depends(validate_access_token)],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """Метод страницы пользователя.

    Если владелец токена посылает запрос на этот метод, то возвращается redirect на личную страницу. В ином
    случае возвращается страница запрашиваемого пользователя.

    Parameters
    ----------
    username : AnyStr
        Имя пользователя, чья страница запрашивается.
    user : UserSchema
        Пользователь получен из зависимости на авторизацию.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    user : UserSchema
        Схема пользователя без пароля.
    """
    if user.username == username:
        return RedirectResponse("/users/me")

    if (result := await user_service.get_user_by_username(session, username)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User \"{username}\" not found.",
        )

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough information in request.",
        )

    return result
