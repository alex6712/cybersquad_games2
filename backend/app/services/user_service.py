from typing import AnyStr

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import APIUserWithPasswordModel
from database.models import DBUserModel


async def get_user_by_username(session: AsyncSession, username: AnyStr) -> DBUserModel:
    """
    Возвращает модель записи пользователя для дальнейшей работы.

    :param session: AsyncSession, объект сессии запроса
    :param username: AnyStr, логин пользователя, уникальное имя
    :return: User, модель записи пользователя
    """
    return await session.scalar(select(DBUserModel).where(DBUserModel.username == username))


async def update_refresh_token(session: AsyncSession, username: AnyStr, refresh_token: AnyStr):
    """
    Перезаписывает токен обновления пользователя.

    :param session: AsyncSession, объект сессии запроса
    :param username: AnyStr, логин пользователя, уникальное имя
    :param refresh_token: AnyStr, новый токен обновления
    """
    return await session.execute(
        update(DBUserModel)
        .where(DBUserModel.username == username)
        .values(refresh_token=refresh_token)
        .returning(DBUserModel.id)
    )


async def add_user(session: AsyncSession, user: APIUserWithPasswordModel):
    """
    Добавляет запись о пользователе в базу данных.

    :param session: AsyncSession, объект сессии запроса
    :param user: APIUserWithPasswordModel, модель объекта пользователя с паролем
    """
    session.add(DBUserModel(username=user.username, password=user.password, email=user.email, phone=user.phone))
