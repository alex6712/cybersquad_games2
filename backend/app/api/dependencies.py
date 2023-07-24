from typing import Annotated, AnyStr

from fastapi import (
    Depends,
    status,
    HTTPException,
    Security,
)
from fastapi.security import (
    OAuth2PasswordBearer,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from jose import JWTError, ExpiredSignatureError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.jwt import jwt_decode
from app.api.schemas import UserSchema
from app.api.services import user_service
from app.database.models import UserModel
from app.database.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign_in")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)


async def validate_access_token(
        token: Annotated[AnyStr, Depends(oauth2_scheme)],
        session: Annotated[AsyncSession, Depends(get_session)],
) -> UserSchema:
    """Dependency авторизации.

    Получает на вход JSON Web Token, декодирует его и проверяет на наличие пользователя в базе данных.
    Возвращает модель записи пользователя.

    Parameters
    ----------
    token : AnyStr
        JSON Web Token, токен доступа.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    user : UserSchema
        Схема данных пользователя.
    """
    user = await _get_user_from_token(token, session)

    return UserSchema(username=user.username, email=user.email, phone=user.phone)


async def validate_refresh_token(
        credentials: Annotated[HTTPAuthorizationCredentials, Security(HTTPBearer())],
        session: Annotated[AsyncSession, Depends(get_session)],
) -> UserSchema:
    """Dependency автоматической аутентификации.

    В заголовке запросе получает refresh_token пользователя, декодирует его,
    проверяет на соответствие в базе данных.

    Parameters
    ----------
    credentials : HTTPAuthorizationCredentials
        Данные автоматической аутентификации (токен обновления).
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    user : UserSchema
        Схема данных пользователя.
    """
    global credentials_exception

    user = await _get_user_from_token(refresh_token := credentials.credentials, session)

    if user.refresh_token != refresh_token:
        raise credentials_exception

    return UserSchema(username=user.username, email=user.email, phone=user.phone)


async def _get_user_from_token(token: AnyStr, session: AsyncSession) -> UserModel:
    """Функция получения записи пользователя из базы данных по data из JWT.

    Получает на вход JSON Web Token, декодирует его и проверяет на наличие пользователя в базе данных.
    Возвращает модель записи пользователя из базы данных.

    Parameters
    ----------
    token : AnyStr
        JSON Web Token, токен доступа.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    user : UserModel
        Модель записи пользователя из базы данных.
    """
    global credentials_exception

    try:
        if (username := jwt_decode(token).get("sub")) is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Signature has expired.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception

    if (user := await user_service.get_user_by_username(session, username)) is None:
        raise credentials_exception

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise credentials_exception

    return user
