from typing import Annotated

from fastapi import (
    Depends,
    status,
    HTTPException,
    Security,
)
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.jwt import jwt_decode
from app.models import APIUserModel
from app.services import user_service
from database.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign_in")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)


async def validate_access_token(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: Annotated[AsyncSession, Depends(get_session)],
) -> APIUserModel:
    """
    Dependency авторизации.

    Получает на вход JSON Web Token, декодирует его и проверяет на наличие пользователя в базе данных.
    Возвращает модель записи пользователя.

    :param token: str, JSON Web Token
    :param session: AsyncSession, объект сессии запроса
    :return: APIUserModel, модель записи пользователя
    """
    global credentials_exception

    try:
        if (username := jwt_decode(token).get("sub")) is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    if (user := await user_service.get_user_by_username(session, username)) is None:
        raise credentials_exception

    try:
        await session.commit()
    except IntegrityError as _:
        raise credentials_exception

    return APIUserModel(username=user.username, email=user.email, phone=user.phone)


async def validate_refresh_token(
        credentials: Annotated[HTTPAuthorizationCredentials, Security(HTTPBearer())],
        session: Annotated[AsyncSession, Depends(get_session)]
) -> APIUserModel:
    """
    Dependency автоматической аутентификации.

    В заголовке запросе получает refresh_token пользователя, декодирует его,
    проверяет на соответствие в базе данных.

    :param credentials: HTTPAuthorizationCredentials, данные автоматической аутентификации (токен обновления)
    :param session: AsyncSession, объект сессии запроса
    :return: APIUserModel, модель записи пользователя
    """
    global credentials_exception

    refresh_token = credentials.credentials

    try:
        if (username := jwt_decode(refresh_token).get("sub")) is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    if (user := await user_service.get_user_by_username(session, username)).refresh_token != refresh_token:
        raise credentials_exception

    try:
        await session.commit()
    except IntegrityError as _:
        raise credentials_exception

    return APIUserModel(username=user.username, email=user.email, phone=user.phone)
