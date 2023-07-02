from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import UserModel
from database.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    """
    Возвращает модель записи пользователя для дальнейшей работы.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :return: User, модель записи пользователя
    """
    return await session.scalar(select(User).where(User.username == username))


async def authenticate_user(session: AsyncSession, username: str, password: str) -> User | None:
    """
    Проводит аутентификацию пользователя.

    Запрашивает модель записи пользователя по логину, после чего сверяет чистый и хешированый пароли.

    :param session: AsyncSession, объект сессии запроса
    :param username: str, логин пользователя, уникальное имя
    :param password: str, пароль пользователя
    :return: User, модель записи пользователя
    """
    db_user = await get_user_by_username(session, username)

    if not db_user:
        return None

    if not pwd_context.verify(password, db_user.password):
        return None

    return db_user


def add_user(session: AsyncSession, user: UserModel):
    """
    Добавляет запись о пользователе в базу данных.

    :param session: AsyncSession, объект сессии запроса
    :param user: UserModel, модель объекта пользователя
    """
    new_user = User(username=user.username, email=user.email, phone=user.phone)
    new_user.password = pwd_context.hash(user.password)

    session.add(new_user)
