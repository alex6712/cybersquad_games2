from datetime import timedelta
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

from app.jwt import create_jwt
from app.models import APIUserWithPasswordModel, APIJSONWebTokenModel
from app.responses import StandardResponse
from app.services import user_service
from database.session import get_session

router = APIRouter(
    prefix="/auth",
    tags=["authorization"],
)


@router.post("/sign_in", status_code=status.HTTP_200_OK, response_model=APIJSONWebTokenModel, tags=["authorization"])
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    """
    Метод авторизации.

    В теле запроса получает аутентификационные данные пользователя (username, password), проводит аутентификацию
    и возвращает JWT.

    :param form_data: OAuth2PasswordRequestForm, аутентификационные данные пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: dict[str, str], словарь с вложенным JWT
    """
    user = await user_service.authenticate_user(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    jwt = create_jwt({"sub": form_data.username}, timedelta(minutes=15))
    return APIJSONWebTokenModel(access_token=jwt, token_type="bearer")


@router.post("/sign_up", status_code=status.HTTP_201_CREATED, response_model=StandardResponse, tags=["authorization"])
async def sign_up(user: APIUserWithPasswordModel, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Метод регистрации.

    Получает на вход модель пользователя и добавляет запись в базу данных.

    :param user: UserModel, модель объекта пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: StandardResponse, положительная обратная связь о регистрации пользователя
    """
    user_already_exists = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User already exists.",
    )

    if not await user_service.add_user(session, user):
        raise user_already_exists

    try:
        await session.commit()
    except IntegrityError as _:
        await session.rollback()

        raise user_already_exists

    return StandardResponse(code=status.HTTP_201_CREATED, message="User created successfully.")
