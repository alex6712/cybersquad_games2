from typing import Annotated, AnyStr

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import validate_access_token
from api.schemas import UserSchema
from api.schemas.responses import UserResponse
from api.services import user_service
from database.session import get_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def me(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """
    Метод личной страницы пользователя.

    Возвращает информацию о владельце токена.

    :param user: APIUserModel, пользователь получен из зависимости на авторизацию
    :return: APIUserModel, объект пользователя без пароля
    """
    return user


@router.get("/{username}", response_model=UserResponse)
async def person(
        username: AnyStr,
        user: Annotated[UserSchema, Depends(validate_access_token)],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Метод страницы пользователя.

    Если владелец токена посылает запрос на этот метод, то возвращается redirect на личную страницу. В ином
    случае возвращается страница запрашиваемого пользователя.

    :param username: AnyStr, логин пользователя, чья страница запрашивается
    :param user: APIUserModel, пользователь получен из зависимости на авторизацию
    :param session: AsyncSession, объект сессии запроса
    :return: APIUserModel, объект пользователя без пароля
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
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return result