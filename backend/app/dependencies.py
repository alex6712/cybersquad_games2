from typing import Annotated

from fastapi import (
    Depends,
    status,
    HTTPException,
)
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.jwt import jwt_decode
from app.services import user_service
from database.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign_in")


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    """
    Dependency для проверки JWT.

    Получает на вход JSON Web Token, декодирует его и проверяет на наличие пользователя в базе данных.
    Возвращает модель записи пользователя.

    :param token: str, JSON Web Token
    :param session: AsyncSession, объект сессии запроса
    :return: User, модель записи пользователя
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        if (username := jwt_decode(token).get("sub")) is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    if (user := await user_service.get_user_by_username(session, username)) is None:
        raise credentials_exception

    return user
