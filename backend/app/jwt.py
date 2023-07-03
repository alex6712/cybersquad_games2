from datetime import datetime, timedelta

from jose import jwt

from app import get_settings

settings = get_settings()


def jwt_encode(to_encode: dict) -> str:
    """
    Кодирует переданный словарь в JWT.

    :param to_encode: dict[str, str], словарь, который будет вложен в JWT
    :return: str, JSON Web Token
    """
    return jwt.encode(to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def jwt_decode(token: str) -> dict:
    """
    Декодирует переданный JWT в словарь.

    :param token: str, JWT, из которого будет получен словарь
    :return: dict[str, str], словарь с информацией из JWT
    """
    return jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


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
