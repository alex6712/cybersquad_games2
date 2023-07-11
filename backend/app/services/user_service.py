from passlib.context import CryptContext
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    APIUserModel,
    APIUserWithPasswordModel,
)
from database.models import DBUserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_username(session: AsyncSession, username: str) -> DBUserModel | None:
    """
    Возвращает модель записи пользователя для дальнейшей работы.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :return: User, модель записи пользователя
    """
    db_user: DBUserModel = await session.scalar(select(DBUserModel).where(DBUserModel.username == username))

    if not db_user:
        return None

    return db_user


async def get_refresh_token_by_username(session: AsyncSession, username: str) -> str | None:
    """
    Возвращает токен обновления пользователя по его имени.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :return: str | None, токен обновления пользователя
    """
    db_user: DBUserModel = await session.scalar(select(DBUserModel).where(DBUserModel.username == username))

    if not db_user:
        return None

    return db_user.refresh_token


async def update_refresh_token(session: AsyncSession, username: str, refresh_token: str) -> bool:
    """
    Перезаписывает токен обновления пользователя.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :param refresh_token: str, новый токен обновления
    :return: bool, оповещение об успешном обновлении записи
    """
    if await session.execute(
            update(DBUserModel)
            .where(DBUserModel.username == username)
            .values(refresh_token=refresh_token)
            .returning(DBUserModel.id)
    ) is None:
        return False

    return True


async def authenticate_user(session: AsyncSession, username: str, password: str) -> DBUserModel | None:
    """
    Проводит аутентификацию пользователя.

    Запрашивает модель записи пользователя по логину, после чего сверяет чистый и хэшированный пароли.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :param password: str, пароль пользователя
    :return: User, модель записи пользователя
    """
    db_user: DBUserModel = await session.scalar(select(DBUserModel).where(DBUserModel.username == username))

    if not db_user:
        return None
    if not pwd_context.verify(password, db_user.password):
        return None

    return db_user


async def add_user(session: AsyncSession, user: APIUserWithPasswordModel) -> bool:
    """
    Добавляет запись о пользователе в базу данных.

    :param session: AsyncSession, объект сессии запроса
    :param user: UserModel, модель объекта пользователя
    """
    db_user: APIUserModel = await get_user_by_username(session, user.username)

    if db_user:
        return False

    new_user = DBUserModel(username=user.username, email=user.email, phone=user.phone)
    new_user.password = pwd_context.hash(user.password)

    session.add(new_user)

    return True
