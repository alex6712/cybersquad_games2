from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)
from fastapi.security import OAuth2PasswordRequestForm
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
    user = await user_service.authenticate_user(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    tokens = create_jwt_pair({"sub": form_data.username})

    if not await user_service.update_refresh_token(session, user.username, tokens["refresh_token"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        await session.commit()
    except IntegrityError as _:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect request.",
        )

    return {**tokens, "token_type": "bearer"}


@router.post("/sign_up", status_code=status.HTTP_201_CREATED, response_model=StandardResponse)
async def sign_up(user: APIUserWithPasswordModel, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Метод регистрации.

    Получает на вход модель пользователя и добавляет запись в базу данных.

    :param user: UserModel, модель объекта пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: StandardResponse, положительная обратная связь о регистрации пользователя
    """
    if not await user_service.add_user(session, user):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )

    try:
        await session.commit()
    except IntegrityError as _:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough information in request.",
        )

    return {"code": status.HTTP_201_CREATED, "message": "User created successfully."}


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
    tokens = create_jwt_pair({"sub": user.username})

    if not await user_service.update_refresh_token(session, user.username, tokens["refresh_token"]):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    try:
        await session.commit()
    except IntegrityError as _:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect request.",
        )

    return {**tokens, "token_type": "bearer"}
