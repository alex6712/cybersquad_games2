from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

SECRET_KEY = "79871f2dd656ab8e91a5f96142763f12aed8d6a4d6bc7cf9aaa9ebe597487323"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def jwt_encode(to_encode: dict) -> str:
    """
    Кодирует переданный словарь в JWT.

    :param to_encode: dict[str, str], словарь, который будет вложен в JWT
    :return: str, JSON Web Token
    """
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)


def jwt_decode(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Декодирует переданный JWT в словарь.

    :param token: str, JWT, из которого будет получен словарь
    :return: dict[str, str], словарь с информацией из JWT
    """
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def create_jwt(data: dict, expires_delta: timedelta = timedelta(minutes=5)):
    """
    Создаёт JWT.

    На вход получает информацию для кодирования и срок жизни токена.

    :param data: dict[str, str], словарь с данными
    :param expires_delta: timedelta, время жизни JWT
    :return: str, JSON Web Token
    """
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})

    return jwt_encode(to_encode)
