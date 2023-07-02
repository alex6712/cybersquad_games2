from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    APIUserModel,
    APIUserWithPasswordModel,
)
from database.models import DBUserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_username(session: AsyncSession, username: str) -> APIUserModel | None:
    """
    Возвращает модель записи пользователя для дальнейшей работы.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :return: User, модель записи пользователя
    """
    db_user = await session.scalar(select(DBUserModel).where(DBUserModel.username == username))

    if not db_user:
        return None

    return APIUserModel(username=db_user.username, email=db_user.email, phone=db_user.phone)


async def authenticate_user(session: AsyncSession, username: str, password: str) -> APIUserModel | None:
    """
    Проводит аутентификацию пользователя.

    Запрашивает модель записи пользователя по логину, после чего сверяет чистый и хэшированный пароли.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :param password: str, пароль пользователя
    :return: User, модель записи пользователя
    """
    db_user = await session.scalar(select(DBUserModel).where(DBUserModel.username == username))

    if not db_user:
        return None
    if not pwd_context.verify(password, db_user.password):
        return None

    return APIUserModel(username=db_user.username, email=db_user.email, phone=db_user.phone)


def add_user(session: AsyncSession, user: APIUserWithPasswordModel):
    """
    Добавляет запись о пользователе в базу данных.

    :param session: AsyncSession, объект сессии запроса
    :param user: UserModel, модель объекта пользователя
    """
    new_user = DBUserModel(username=user.username, email=user.email, phone=user.phone)
    new_user.password = pwd_context.hash(user.password)

    session.add(new_user)
