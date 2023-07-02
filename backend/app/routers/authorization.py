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
from app.models import APIUserWithPasswordModel
from app.responses import StandardResponse
from app.services import user_service
from database.session import get_session

router = APIRouter(
    prefix="/authorization",
    tags=["authorization"],
)


@router.post("/sign_in", status_code=status.HTTP_200_OK, tags=["authorization"])
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    """
    Метод аутентификации.

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
    return {"access_token": jwt, "token_type": "bearer"}


@router.post("/sign_up", status_code=status.HTTP_201_CREATED, response_model=StandardResponse, tags=["authorization"])
async def sign_up(user: APIUserWithPasswordModel, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Метод регистрации.

    Получает на вход модель пользователя и добавляет запись в базу данных.

    :param user: UserModel, модель объекта пользователя
    :param session: AsyncSession, объект сессии запроса
    :return: StandardResponse, положительная обратная связь о регистрации пользователя
    """
    user_service.add_user(session, user)

    try:
        await session.commit()
    except IntegrityError as _:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )

    return StandardResponse(code=status.HTTP_201_CREATED, message="User created successfully.")
