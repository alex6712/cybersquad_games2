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
)
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import validate_refresh_token
from app.jwt import create_jwt_pair
from app.models import APIUserModel, APIUserWithPasswordModel
from app.models.responses import StandardResponse, TokenResponse
from app.services import user_service
from database.session import get_session

router = APIRouter(
    prefix="/auth",
    tags=["authorization"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/sign_in", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Метод аутентификации.

    В теле запроса получает аутентификационные данные пользователя (username, password), проводит аутентификацию
    и возвращает JWT.

    :param form_data: OAuth2PasswordRequestForm, аутентификационные данные пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: APIJSONWebTokenModel, модель ответа с вложенной парой JWT
    """
    user = await user_service.get_user_by_username(session, form_data.username)

    if not user:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not pwd_context.verify(form_data.password, user.password):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {**await _get_jwt_pair(user.username, session), "token_type": "bearer"}


@router.post("/sign_up", status_code=status.HTTP_201_CREATED, response_model=StandardResponse)
async def sign_up(user: APIUserWithPasswordModel, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Метод регистрации.

    Получает на вход модель пользователя и добавляет запись в базу данных.

    :param user: UserModel, модель объекта пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: StandardResponse, положительная обратная связь о регистрации пользователя
    """
    if await user_service.get_user_by_username(session, user.username):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )

    user.password = pwd_context.hash(user.password)

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


@router.get("/refresh", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def refresh(
        user: Annotated[APIUserModel, Depends(validate_refresh_token)],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Метод повторной аутентификации через токен обновления.

    В заголовке получает refresh_token, проверяет на совпадение в базе данных по закодированной информации
    и перезаписывает токен обновления в базе данных.

    :param user: APIUserModel, пользователь получен из зависимости на автоматическую аутентификацию
    :param session: AsyncSession, объект сессии запроса
    :return: APIJSONWebTokenModel, модель ответа с вложенной парой JWT
    """
    return {**await _get_jwt_pair(user.username, session), "token_type": "bearer"}


async def _get_jwt_pair(username: AnyStr, session: AsyncSession) -> Dict[AnyStr, AnyStr]:
    """
    Функция создания новой пары JWT.

    Создаёт пару access_token и refresh_token, перезаписывает токен обновления пользователя
    в базе данных и возвращает пару JWT.

    :param username: AnyStr, имя пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: Dict[AnyStr, AnyStr], пара JWT
    """
    tokens = create_jwt_pair({"sub": username})

    _ = await user_service.update_refresh_token(session, username, tokens["refresh_token"])

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect request.",
        )

    return tokens
