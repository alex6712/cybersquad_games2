from typing import AnyStr

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import UserWithPasswordSchema
from database.models import UserModel


async def get_user_by_username(session: AsyncSession, username: AnyStr) -> UserModel:
    """
    Возвращает модель записи пользователя для дальнейшей работы.

    :param session: AsyncSession, объект сессии запроса
    :param username: AnyStr, логин пользователя, уникальное имя
    :return: User, модель записи пользователя
    """
    return await session.scalar(select(UserModel).where(UserModel.username == username))


async def update_refresh_token(session: AsyncSession, username: AnyStr, refresh_token: AnyStr):
    """
    Перезаписывает токен обновления пользователя.

    :param session: AsyncSession, объект сессии запроса
    :param username: AnyStr, логин пользователя, уникальное имя
    :param refresh_token: AnyStr, новый токен обновления
    """
    (await get_user_by_username(session, username)).refresh_token = refresh_token


def add_user(session: AsyncSession, user: UserWithPasswordSchema):
    """
    Добавляет запись о пользователе в базу данных.

    :param session: AsyncSession, объект сессии запроса
    :param user: APIUserWithPasswordModel, модель объекта пользователя с паролем
    """
    session.add(UserModel(username=user.username, password=user.password, email=user.email, phone=user.phone))
