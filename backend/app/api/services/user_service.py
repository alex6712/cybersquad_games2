from typing import AnyStr

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import UserWithPasswordSchema
from app.database.models import UserModel


async def get_user_by_username(session: AsyncSession, username: AnyStr) -> UserModel:
    """Возвращает модель записи пользователя для дальнейшей работы.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    username : AnyStr
        Логин пользователя, уникальное имя.

    Returns
    -------
    user : UserModel
        Модель записи пользователя в базе данных.
    """
    return await session.scalar(select(UserModel).where(UserModel.username == username))


async def update_refresh_token(session: AsyncSession, username: AnyStr, refresh_token: AnyStr):
    """Перезаписывает токен обновления пользователя.

    Note
    ----
    В данном случае используются возможности ORM SQLAlchemy, которые позволяют
    изменить значение атрибута объекта записи пользователя, и при следующем
    commit'е сессии эти изменения будут сохранены в базе данных.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    username : AnyStr
        Логин пользователя, уникальное имя.
    refresh_token : AnyStr
        Новый токен обновления.
    """
    (await get_user_by_username(session, username)).refresh_token = refresh_token


def add_user(session: AsyncSession, user: UserWithPasswordSchema):
    """Добавляет запись о пользователе в базу данных.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    user : UserWithPasswordSchema
        Схема объекта пользователя с паролем.
    """
    session.add(UserModel(username=user.username, password=user.password, email=user.email, phone=user.phone))
