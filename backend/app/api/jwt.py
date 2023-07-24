from datetime import datetime, timedelta
from typing import Dict, AnyStr

from jose import jwt

from app import get_settings

settings = get_settings()


def jwt_encode(to_encode: Dict) -> AnyStr:
    """Кодирует переданный словарь в JWT.

    Parameters
    ----------
    to_encode : Dict
        Словарь, который будет вложен в JWT.

    Returns
    -------
    token : AnyStr
        JSON Web Token.
    """
    return jwt.encode(to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def jwt_decode(token: AnyStr) -> Dict:
    """Декодирует переданный JWT в словарь.

    Parameters
    ----------
    token : AnyStr
        JWT, из которого будет получен словарь.

    Returns
    -------
    dictionary : Dict
        Словарь с информацией из JWT.
    """
    return jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


def create_jwt(data: Dict, expires_delta: timedelta) -> AnyStr:
    """Создаёт JWT.

    На вход получает информацию для кодирования и срок жизни токена.

    Parameters
    ----------
    data : Dict
        Словарь с данными.
    expires_delta : timedelta
        Время жизни токена.

    Returns
    -------
    token : AnyStr
        JSON Web Token.
    """
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})

    return jwt_encode(to_encode)


def create_jwt_pair(
        access_token_data: Dict,
        refresh_token_data: Dict = None,
        at_expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_LIFETIME_MINUTES),
        rt_expires_delta: timedelta = timedelta(days=settings.REFRESH_TOKEN_LIFETIME_DAYS),
) -> Dict[AnyStr, AnyStr]:
    """Создаёт пару JWT, состоящую из токена доступа и токена обновления.

    Parameters
    ----------
    access_token_data : Dict
        Информация, которая будет закодирована в токен доступа.
    refresh_token_data : Dict
        Информация, которая будет закодирована в токен обновления.
    at_expires_delta : timedelta
        Время жизни токена доступа.
    rt_expires_delta : timedelta
        Время жизни токена обновления.

    Returns
    -------
    tokens : Dict[AnyStr, AnyStr]
        Пара JWT (access_token + refresh_token).
    """
    if refresh_token_data is None:
        refresh_token_data = access_token_data

    return {
        "access_token": create_jwt(access_token_data, at_expires_delta),
        "refresh_token": create_jwt(refresh_token_data, rt_expires_delta)
    }
