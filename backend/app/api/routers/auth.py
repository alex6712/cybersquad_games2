from typing import (
    Annotated,
    Dict,
    AnyStr,
)

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
    Body,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_refresh_token
from app.api.jwt import create_jwt_pair
from app.api.schemas import UserSchema, UserWithPasswordSchema
from app.api.schemas.responses import StandardResponse, TokenResponse
from app.api.security import hash_, verify
from app.api.services import user_service
from app.database.session import get_session

router = APIRouter(
    prefix="/auth",
    tags=["authorization"],
)


@router.post(
    "/sign_in",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Аутентификация.",
)
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """Метод аутентификации.

    В теле запроса получает аутентификационные данные пользователя (username, password), проводит аутентификацию
    и возвращает JWT.

    Parameters
    ----------
    form_data : OAuth2PasswordRequestForm
        Аутентификационные данные пользователя.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    response : TokenResponse
        Модель ответа сервера с вложенной парой JWT.
    """
    user = await user_service.get_user_by_username(session, form_data.username)

    if not user:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify(form_data.password, user.password):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {**await _get_jwt_pair(user.username, session), "token_type": "bearer"}


@router.post(
    "/sign_up",
    response_model=StandardResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Регистрация.",
)
async def sign_up(
        user: Annotated[UserWithPasswordSchema, Body(title="Данные для регистрации пользователя.")],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    """Метод регистрации.

    Получает на вход модель пользователя и добавляет запись в базу данных.

    Parameters
    ----------
    user : UserWithPasswordSchema
        Схема объекта пользователя.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    response : StandardResponse
        Положительная обратная связь о регистрации пользователя.
    """
    if await user_service.get_user_by_username(session, user.username):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )

    user.password = hash_(user.password)

    user_service.add_user(session, user)

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough information in request.",
        )

    return {"code": status.HTTP_201_CREATED, "message": f"User created successfully."}


@router.get(
    "/refresh",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Обновление токена доступа.",
)
async def refresh(
        user: Annotated[UserSchema, Depends(validate_refresh_token)],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """Метод повторной аутентификации через токен обновления.

    В заголовке получает refresh_token, проверяет на совпадение в базе данных по закодированной информации
    и перезаписывает токен обновления в базе данных.

    Parameters
    ----------
    user : UserSchema
        Пользователь получен из зависимости на автоматическую аутентификацию.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    response : TokenResponse
        Модель ответа сервера с вложенной парой JWT.
    """
    return {**await _get_jwt_pair(user.username, session), "token_type": "bearer"}


async def _get_jwt_pair(username: AnyStr, session: AsyncSession) -> Dict[AnyStr, AnyStr]:
    """Функция создания новой пары JWT.

    Создаёт пару access_token и refresh_token, перезаписывает токен обновления пользователя
    в базе данных и возвращает пару JWT.

    Parameters
    ----------
    username : AnyStr
        Имя пользователя.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    tokens : Dict[AnyStr, AnyStr]
        Пара JWT в виде словаря с двумя ключами: access_token и refresh_token.

        ``access_token``:
            Токен доступа (``str``).
        ``refresh_token``:
            Токен обновления (``str``).
    """
    tokens = create_jwt_pair({"sub": username})

    await user_service.update_refresh_token(session, username, tokens["refresh_token"])

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect request.",
        )

    return tokens
